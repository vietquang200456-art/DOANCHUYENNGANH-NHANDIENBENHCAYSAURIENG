"""Dataset audit utilities for DurianLeafAI.

The audit is read-only: it never modifies files under the dataset directory.
"""
from __future__ import annotations

import csv
import hashlib
import io
import math
import os
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = False

DEFAULT_SPLITS = ("train", "val", "test")
DEFAULT_CLASSES = (
    "Leaf_Algal",
    "Leaf_Blight",
    "Leaf_Colletotrichum",
    "Leaf_Healthy",
    "Leaf_Phomopsis",
    "Leaf_Rhizoctonia",
)
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


@dataclass
class FileAudit:
    relative_path: str
    split: str
    label: str
    extension: str
    size_bytes: int
    sha256: str = ""
    readable: bool = False
    width: Optional[int] = None
    height: Optional[int] = None
    mode: str = ""
    format: str = ""
    error: str = ""
    kind: str = "image"


@dataclass
class NearDuplicate:
    path_a: str
    path_b: str
    distance: int
    hash_size: int


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _sha256(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _phash(path: Path, hash_size: int = 8) -> int:
    """Small dependency-free perceptual hash based on a low-frequency DCT."""
    image_size = hash_size * 4
    with Image.open(path) as image:
        gray = image.convert("L").resize((image_size, image_size), Image.Resampling.LANCZOS)
        pixels = list(gray.getdata())
    n = image_size
    values = []
    for u in range(hash_size):
        for v in range(hash_size):
            total = 0.0
            for x in range(n):
                for y in range(n):
                    total += pixels[x * n + y] * math.cos(math.pi * (x + 0.5) * u / n) * math.cos(math.pi * (y + 0.5) * v / n)
            values.append(total)
    median = sorted(values[1:])[len(values[1:]) // 2]
    result = 0
    for value in values:
        result = (result << 1) | int(value > median)
    return result


def _hamming(a: int, b: int) -> int:
    return bin(a ^ b).count("1")


def audit_dataset(
    dataset_root: Path,
    expected_splits: Sequence[str] = DEFAULT_SPLITS,
    expected_classes: Sequence[str] = DEFAULT_CLASSES,
    near_duplicates: bool = True,
    near_duplicate_threshold: int = 6,
) -> Dict[str, object]:
    """Scan dataset structure and image contents without changing source files."""
    root = Path(dataset_root).resolve()
    files: List[FileAudit] = []
    structural_issues: List[str] = []
    if not root.exists() or not root.is_dir():
        return {"dataset_root": str(root), "fatal_error": f"Dataset directory does not exist: {root}", "files": [], "structural_issues": []}

    for split in expected_splits:
        split_dir = root / split
        if not split_dir.is_dir():
            structural_issues.append(f"Missing split directory: {split}/")
            continue
        actual_classes = {p.name for p in split_dir.iterdir() if p.is_dir()}
        for label in expected_classes:
            if label not in actual_classes:
                structural_issues.append(f"Missing class directory: {split}/{label}/")
        for class_dir in sorted((p for p in split_dir.iterdir() if p.is_dir()), key=lambda p: p.name):
            for path in sorted(class_dir.iterdir(), key=lambda p: p.name.lower()):
                if not path.is_file():
                    continue
                item = FileAudit(_relative(path, root), split, class_dir.name, path.suffix.lower(), path.stat().st_size)
                if item.extension not in SUPPORTED_EXTENSIONS:
                    item.kind = "unsupported_extension"
                    item.error = "Unsupported file extension"
                    files.append(item)
                    continue
                if item.size_bytes == 0:
                    item.kind = "empty_file"
                    item.error = "File is empty"
                    files.append(item)
                    continue
                try:
                    item.sha256 = _sha256(path)
                    with Image.open(path) as image:
                        image.verify()
                    with Image.open(path) as image:
                        item.width, item.height, item.mode, item.format = image.width, image.height, image.mode, image.format or ""
                    item.readable = True
                except Exception as exc:  # Pillow raises several format-specific exceptions.
                    item.kind = "unreadable_image"
                    item.error = f"{type(exc).__name__}: {exc}"
                files.append(item)

    exact_groups: List[List[FileAudit]] = []
    by_hash: Dict[str, List[FileAudit]] = defaultdict(list)
    for item in files:
        if item.readable and item.sha256:
            by_hash[item.sha256].append(item)
    for group in by_hash.values():
        if len(group) > 1:
            exact_groups.append(sorted(group, key=lambda item: item.relative_path))
    exact_groups.sort(key=lambda group: group[0].relative_path)

    near_groups: List[NearDuplicate] = []
    phashes: Dict[str, int] = {}
    near_status = "enabled"
    if near_duplicates:
        try:
            for item in files:
                if item.readable:
                    phashes[item.relative_path] = _phash(root / item.relative_path)
            paths = sorted(phashes)
            for index, path_a in enumerate(paths):
                for path_b in paths[index + 1 :]:
                    distance = _hamming(phashes[path_a], phashes[path_b])
                    if distance <= near_duplicate_threshold and not any(path_a == x.path_a and path_b == x.path_b for x in near_groups):
                        near_groups.append(NearDuplicate(path_a, path_b, distance, 8))
        except Exception as exc:
            near_status = f"skipped: {type(exc).__name__}: {exc}"
    else:
        near_status = "disabled"

    near_records = []
    by_path = {item.relative_path: item for item in files}
    for pair in near_groups:
        first = by_path.get(pair.path_a)
        second = by_path.get(pair.path_b)
        if first and second:
            near_records.append({"path_a": pair.path_a, "path_b": pair.path_b, "split_a": first.split, "split_b": second.split, "label_a": first.label, "label_b": second.label, "distance": pair.distance, "hash_size": pair.hash_size})

    return {
        "dataset_root": str(root),
        "expected_splits": list(expected_splits),
        "expected_classes": list(expected_classes),
        "files": files,
        "structural_issues": structural_issues,
        "exact_groups": exact_groups,
        "near_duplicates": near_groups,
        "near_duplicate_records": near_records,
        "near_duplicate_status": near_status,
        "near_duplicate_threshold": near_duplicate_threshold,
    }


def write_reports(result: Dict[str, object], output_dir: Path) -> Tuple[Path, Path]:
    """Write one Markdown report and one row-level CSV report."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    files: List[FileAudit] = result["files"]  # type: ignore[assignment]
    exact_groups: List[List[FileAudit]] = result["exact_groups"]  # type: ignore[assignment]
    near_groups: List[NearDuplicate] = result["near_duplicates"]  # type: ignore[assignment]
    near_csv_path = output_dir / "dataset_audit_near_duplicates.csv"
    near_records = result.get("near_duplicate_records", [])
    with near_csv_path.open("w", newline="", encoding="utf-8") as handle:
        fields = ["path_a", "path_b", "split_a", "split_b", "label_a", "label_b", "distance", "hash_size"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(near_records)

    csv_path = output_dir / "dataset_audit_files.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(files[0]).keys()) if files else list(FileAudit.__annotations__.keys()))
        writer.writeheader()
        writer.writerows(asdict(item) for item in files)

    split_counts = Counter(item.split for item in files)
    class_counts = Counter((item.split, item.label) for item in files)
    readable = [item for item in files if item.readable]
    modes = Counter(item.mode for item in readable)
    formats = Counter(item.format for item in readable)
    errors = [item for item in files if not item.readable]
    cross_split = []
    cross_label = []
    for group in exact_groups:
        splits = {item.split for item in group}
        labels = {item.label for item in group}
        if len(splits) > 1:
            cross_split.append(group)
        if len(labels) > 1:
            cross_label.append(group)

    lines = [
        "# DurianLeafAI Dataset Audit Report", "", 
        f"- Dataset root: `{result['dataset_root']}`",
        "- Audit is read-only; no source image was modified, moved, renamed, deleted, or relabeled.",
        "- Per-file details: `dataset_audit_files.csv`", "",
        "## Result", "",
        f"- Total files found: **{len(files)}**",
        f"- Readable images: **{len(readable)}**",
        f"- Problematic files: **{len(errors)}**",
        f"- Structural issues: **{len(result['structural_issues'])}**",
        f"- Exact duplicate groups: **{len(exact_groups)}**",
        f"- Exact duplicate groups crossing splits: **{len(cross_split)}**",
        f"- Exact duplicate groups with different labels: **{len(cross_label)}**",
        f"- Near-duplicate status: **{result['near_duplicate_status']}**",
        f"- Near-duplicate pairs at Hamming threshold {result['near_duplicate_threshold']}: **{len(near_groups)}**", "",
        "## Split Summary", "", "| Split | Files |", "|---|---:|",
    ]
    for split in result["expected_splits"]: lines.append(f"| {split} | {split_counts[split]} |")
    lines += ["", "## Class Counts", "", "| Split | Class | Files |", "|---|---|---:|"]
    for split in result["expected_splits"]:
        for label in result["expected_classes"]:
            lines.append(f"| {split} | {label} | {class_counts[(split, label)]} |")
    lines += ["", "## Image Properties", "", "- Modes: " + (", ".join(f"`{k}`={v}" for k, v in sorted(modes.items())) or "none") + ".", "- Formats: " + (", ".join(f"`{k}`={v}" for k, v in sorted(formats.items())) or "none") + ".", "", "## Structural Issues"]
    lines += ["", *([f"- {x}" for x in result["structural_issues"]] or ["- None detected."])]
    lines += ["", "## Unreadable or Invalid Files", "", *([f"- `{x.relative_path}`: {x.error}" for x in errors] or ["- None detected."])]
    lines += ["", "## Exact Duplicate Groups", "", "Identical content is grouped by SHA-256. The labels below are derived from the current folder paths and were not changed.", ""]
    if exact_groups:
        for index, group in enumerate(exact_groups, 1):
            flags = []
            if len({x.split for x in group}) > 1: flags.append("cross-split")
            if len({x.label for x in group}) > 1: flags.append("different-label")
            lines.append(f"{index}. **{'/'.join(flags) or 'same-split/same-label'}**")
            for item in group: lines.append(f"   - `{item.relative_path}` ({item.split}, {item.label}, {item.sha256[:12]}...)" )
    else: lines.append("- None detected.")
    lines += ["", "## Near Duplicate Pairs", "", "Perceptual hash is a screening heuristic; all pairs require human review."]
    if near_groups:
        for pair in near_groups: lines.append(f"- distance={pair.distance}: `{pair.path_a}` <-> `{pair.path_b}`")
    else: lines.append("- None detected or feature skipped.")
    lines += ["", "## Required Human Review", "", "- Review every exact duplicate crossing train/val/test because it may cause evaluation leakage.", "- Review every exact duplicate with different labels because it may indicate labeling conflict or source-data error.", "- Review near-duplicate pairs before training; this audit does not remove or relabel anything.", "- Confirm whether grayscale/RGBA images are intentional and whether the selected preprocessing handles them.", "- Validate domain labels against the original dataset documentation; folder names alone are not proof of correctness.", "", "## Recommendation", "", "- Dataset is structurally suitable for the next Data Pipeline step only after the duplicate and label conflicts above are reviewed."]
    md_path = output_dir / "dataset_audit_report.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return md_path, csv_path


