"""Run the DurianLeafAI dataset audit from the project root."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data.validate_dataset import DEFAULT_CLASSES, DEFAULT_SPLITS, audit_dataset, write_reports


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only audit for Dataset/train, val and test.")
    parser.add_argument("--dataset-root", type=Path, default=PROJECT_ROOT / "Dataset", help="Dataset root directory.")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "outputs" / "metrics" / "dataset_audit", help="Directory for Markdown and CSV reports.")
    parser.add_argument("--near-duplicate-threshold", type=int, default=6, help="Maximum pHash Hamming distance; default: 6.")
    parser.add_argument("--skip-near-duplicates", action="store_true", help="Skip perceptual-hash screening.")
    args = parser.parse_args()
    result = audit_dataset(args.dataset_root, DEFAULT_SPLITS, DEFAULT_CLASSES, not args.skip_near_duplicates, args.near_duplicate_threshold)
    if result.get("fatal_error"):
        print(f"ERROR: {result['fatal_error']}", file=sys.stderr)
        return 2
    md_path, csv_path = write_reports(result, args.output_dir)
    print(f"Dataset audit completed. Markdown: {md_path}")
    print(f"CSV: {csv_path}")
    print(f"Files: {len(result['files'])}; exact duplicate groups: {len(result['exact_groups'])}; near-duplicate pairs: {len(result['near_duplicates'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
