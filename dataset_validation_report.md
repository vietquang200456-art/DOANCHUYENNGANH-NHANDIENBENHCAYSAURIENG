# Dataset Validation Report

- Checked: 2026-10-30
- Dataset root: `Dataset/`
- Scope: directory structure, class labels, file extensions, zero-byte files, and SHA-256 duplicate content.

## Overall Result

- **PASS with warning**: all expected folders and files passed basic structural checks.
- Total image files: **2,595** across **3 splits** and **6 classes**.
- Duplicate-content groups: **12**. These require review before training because duplicates can cause data leakage or indicate near-identical source images.
- No missing split/class directories were found.
- No unsupported extensions or zero-byte files were found.

## Split Summary

| Split | Images | Classes |
|---|---:|---:|
| train | 1814 | 6 |
| val | 387 | 6 |
| test | 394 | 6 |

## Class Counts

| Split | Leaf_Algal | Leaf_Blight | Leaf_Colletotrichum | Leaf_Healthy | Leaf_Phomopsis | Leaf_Rhizoctonia |
|---|---:|---:|---:|---:|---:|---:|
| train | 323 | 308 | 280 | 338 | 287 | 278 |
| val | 69 | 66 | 60 | 72 | 61 | 59 |
| test | 70 | 66 | 60 | 74 | 63 | 61 |

## Duplicate Content Groups

The following duplicate groups were detected by identical SHA-256 content. Paths are relative to `Dataset/`.

1. train/Leaf_Algal/Leaf_Algal_28.jpg  \\  val/Leaf_Algal/Leaf_Algal_29.jpg
2. train/Leaf_Algal/Leaf_Algal_38.jpg  \\  val/Leaf_Algal/Leaf_Algal_37.jpg
3. test/Leaf_Blight/Leaf_Blight_109.jpg  \\  train/Leaf_Colletotrichum/Leaf_Colletotrichum_400.jpg
4. test/Leaf_Colletotrichum/Leaf_Colletotrichum_395.jpg  \\  train/Leaf_Blight/Leaf_Blight_70.jpg
5. train/Leaf_Algal/Leaf_Algal_290.jpg  \\  val/Leaf_Algal/Leaf_Algal_288.jpg
6. train/Leaf_Blight/Leaf_Blight_40.jpg  \\  val/Leaf_Blight/Leaf_Blight_41.jpg
7. train/Leaf_Blight/Leaf_Blight_75.jpg  \\  train/Leaf_Colletotrichum/Leaf_Colletotrichum_397.jpg
8. train/Leaf_Algal/Leaf_Algal_24.jpg  \\  val/Leaf_Algal/Leaf_Algal_23.jpg
9. test/Leaf_Blight/Leaf_Blight_105.jpg  \\  val/Leaf_Colletotrichum/Leaf_Colletotrichum_399.jpg
10. test/Leaf_Colletotrichum/Leaf_Colletotrichum_390.jpg  \\  train/Leaf_Colletotrichum/Leaf_Colletotrichum_389.jpg
11. test/Leaf_Blight/Leaf_Blight_73.jpg  \\  test/Leaf_Colletotrichum/Leaf_Colletotrichum_396.jpg
12. test/Leaf_Algal/Leaf_Algal_39.jpg  \\  test/Leaf_Algal/Leaf_Algal_40.jpg

## Validation Details

- Expected classes: `Leaf_Algal`, `Leaf_Blight`, `Leaf_Colletotrichum`, `Leaf_Healthy`, `Leaf_Phomopsis`, `Leaf_Rhizoctonia`.
- Accepted image extensions: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.webp`.
- All 2,595 files use accepted image extensions and have non-zero size.
- This validation did not decode every image with an image library, so a later step should verify that each file can be opened and dimensions/color modes are valid.
- This validation did not determine whether duplicate files are visually identical under different encodings; it only detects identical SHA-256 content.

## Recommended Next Actions

1. Inspect the 12 duplicate groups and confirm whether they are intentional.
2. Perform image decode/dimension validation before training.
3. Check for near-duplicate or same-source images across train/val/test to reduce leakage risk.
4. After review, create the data pipeline and training configuration.
