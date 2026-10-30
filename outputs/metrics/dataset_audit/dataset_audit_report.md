# DurianLeafAI Dataset Audit Report

- Dataset root: `D:\DoAn_ChuyenNganh\DOANCHUYENNGANH-NHANDIENBENHCAYSAURIENG\Dataset`
- Audit is read-only; no source image was modified, moved, renamed, deleted, or relabeled.
- Per-file details: `dataset_audit_files.csv`

## Result

- Total files found: **2595**
- Readable images: **2595**
- Problematic files: **0**
- Structural issues: **0**
- Exact duplicate groups: **12**
- Exact duplicate groups crossing splits: **9**
- Exact duplicate groups with different labels: **5**
- Near-duplicate status: **enabled**
- Near-duplicate pairs at Hamming threshold 6: **131**

## Split Summary

| Split | Files |
|---|---:|
| train | 1814 |
| val | 387 |
| test | 394 |

## Class Counts

| Split | Class | Files |
|---|---|---:|
| train | Leaf_Algal | 323 |
| train | Leaf_Blight | 308 |
| train | Leaf_Colletotrichum | 280 |
| train | Leaf_Healthy | 338 |
| train | Leaf_Phomopsis | 287 |
| train | Leaf_Rhizoctonia | 278 |
| val | Leaf_Algal | 69 |
| val | Leaf_Blight | 66 |
| val | Leaf_Colletotrichum | 60 |
| val | Leaf_Healthy | 72 |
| val | Leaf_Phomopsis | 61 |
| val | Leaf_Rhizoctonia | 59 |
| test | Leaf_Algal | 70 |
| test | Leaf_Blight | 66 |
| test | Leaf_Colletotrichum | 60 |
| test | Leaf_Healthy | 74 |
| test | Leaf_Phomopsis | 63 |
| test | Leaf_Rhizoctonia | 61 |

## Image Properties

- Modes: `RGB`=2591, `RGBA`=4.
- Formats: `JPEG`=2591, `PNG`=4.

## Structural Issues

- None detected.

## Unreadable or Invalid Files

- None detected.

## Exact Duplicate Groups

Identical content is grouped by SHA-256. The labels below are derived from the current folder paths and were not changed.

1. **same-split/same-label**
   - `test/Leaf_Algal/Leaf_Algal_39.jpg` (test, Leaf_Algal, 944c9967f207...)
   - `test/Leaf_Algal/Leaf_Algal_40.jpg` (test, Leaf_Algal, 944c9967f207...)
2. **cross-split/different-label**
   - `test/Leaf_Blight/Leaf_Blight_105.jpg` (test, Leaf_Blight, d48f8a0888c2...)
   - `val/Leaf_Colletotrichum/Leaf_Colletotrichum_399.jpg` (val, Leaf_Colletotrichum, d48f8a0888c2...)
3. **cross-split/different-label**
   - `test/Leaf_Blight/Leaf_Blight_109.jpg` (test, Leaf_Blight, 0a2eeb79429f...)
   - `train/Leaf_Colletotrichum/Leaf_Colletotrichum_400.jpg` (train, Leaf_Colletotrichum, 0a2eeb79429f...)
4. **different-label**
   - `test/Leaf_Blight/Leaf_Blight_73.jpg` (test, Leaf_Blight, 20b9118681f8...)
   - `test/Leaf_Colletotrichum/Leaf_Colletotrichum_396.jpg` (test, Leaf_Colletotrichum, 20b9118681f8...)
5. **cross-split**
   - `test/Leaf_Colletotrichum/Leaf_Colletotrichum_390.jpg` (test, Leaf_Colletotrichum, 8bbf227ebbb5...)
   - `train/Leaf_Colletotrichum/Leaf_Colletotrichum_389.jpg` (train, Leaf_Colletotrichum, 8bbf227ebbb5...)
6. **cross-split/different-label**
   - `test/Leaf_Colletotrichum/Leaf_Colletotrichum_395.jpg` (test, Leaf_Colletotrichum, 6ccbc51f3a69...)
   - `train/Leaf_Blight/Leaf_Blight_70.jpg` (train, Leaf_Blight, 6ccbc51f3a69...)
7. **cross-split**
   - `train/Leaf_Algal/Leaf_Algal_24.jpg` (train, Leaf_Algal, 09dcb5402db3...)
   - `val/Leaf_Algal/Leaf_Algal_23.jpg` (val, Leaf_Algal, 09dcb5402db3...)
8. **cross-split**
   - `train/Leaf_Algal/Leaf_Algal_28.jpg` (train, Leaf_Algal, 6d6bd15f0d93...)
   - `val/Leaf_Algal/Leaf_Algal_29.jpg` (val, Leaf_Algal, 6d6bd15f0d93...)
9. **cross-split**
   - `train/Leaf_Algal/Leaf_Algal_290.jpg` (train, Leaf_Algal, 534a0157040c...)
   - `val/Leaf_Algal/Leaf_Algal_288.jpg` (val, Leaf_Algal, 534a0157040c...)
10. **cross-split**
   - `train/Leaf_Algal/Leaf_Algal_38.jpg` (train, Leaf_Algal, d24a6e9ba9f4...)
   - `val/Leaf_Algal/Leaf_Algal_37.jpg` (val, Leaf_Algal, d24a6e9ba9f4...)
11. **cross-split**
   - `train/Leaf_Blight/Leaf_Blight_40.jpg` (train, Leaf_Blight, b8c182667331...)
   - `val/Leaf_Blight/Leaf_Blight_41.jpg` (val, Leaf_Blight, b8c182667331...)
12. **different-label**
   - `train/Leaf_Blight/Leaf_Blight_75.jpg` (train, Leaf_Blight, dec1566db5e8...)
   - `train/Leaf_Colletotrichum/Leaf_Colletotrichum_397.jpg` (train, Leaf_Colletotrichum, dec1566db5e8...)

## Near Duplicate Pairs

Perceptual hash is a screening heuristic; all pairs require human review.
- distance=0: `test/Leaf_Algal/Leaf_Algal_39.jpg` <-> `test/Leaf_Algal/Leaf_Algal_40.jpg`
- distance=6: `test/Leaf_Blight/Leaf_Blight_105.jpg` <-> `train/Leaf_Blight/Leaf_Blight_134.jpg`
- distance=0: `test/Leaf_Blight/Leaf_Blight_105.jpg` <-> `val/Leaf_Colletotrichum/Leaf_Colletotrichum_399.jpg`
- distance=0: `test/Leaf_Blight/Leaf_Blight_109.jpg` <-> `train/Leaf_Colletotrichum/Leaf_Colletotrichum_400.jpg`
- distance=4: `test/Leaf_Blight/Leaf_Blight_188.jpg` <-> `train/Leaf_Blight/Leaf_Blight_89.jpg`
- distance=6: `test/Leaf_Blight/Leaf_Blight_71.jpg` <-> `train/Leaf_Blight/Leaf_Blight_168.jpg`
- distance=6: `test/Leaf_Blight/Leaf_Blight_71.jpg` <-> `train/Leaf_Blight/Leaf_Blight_49.jpg`
- distance=0: `test/Leaf_Blight/Leaf_Blight_73.jpg` <-> `test/Leaf_Colletotrichum/Leaf_Colletotrichum_396.jpg`
- distance=2: `test/Leaf_Blight/Leaf_Blight_93.jpg` <-> `train/Leaf_Blight/Leaf_Blight_177.jpg`
- distance=0: `test/Leaf_Colletotrichum/Leaf_Colletotrichum_390.jpg` <-> `train/Leaf_Colletotrichum/Leaf_Colletotrichum_389.jpg`
- distance=0: `test/Leaf_Colletotrichum/Leaf_Colletotrichum_395.jpg` <-> `train/Leaf_Blight/Leaf_Blight_70.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_101.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_445.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_103.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_112.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_110.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_121.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_116.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_403.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_146.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_55.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_207.jpg` <-> `test/Leaf_Healthy/Leaf_Healthy_354.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_207.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_420.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_224.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_435.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_227.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_237.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_228.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_337.jpg`
- distance=2: `test/Leaf_Healthy/Leaf_Healthy_245.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_378.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_257.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_282.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_283.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_308.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_284.jpg` <-> `test/Leaf_Healthy/Leaf_Healthy_412.jpg`
- distance=2: `test/Leaf_Healthy/Leaf_Healthy_290.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_419.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_298.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_385.jpg`
- distance=2: `test/Leaf_Healthy/Leaf_Healthy_314.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_72.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_323.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_210.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_323.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_443.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_326.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_240.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_346.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_241.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_346.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_329.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_350.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_186.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_354.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_420.jpg`
- distance=2: `test/Leaf_Healthy/Leaf_Healthy_377.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_302.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_388.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_262.jpg`
- distance=6: `test/Leaf_Healthy/Leaf_Healthy_390.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_408.jpg`
- distance=0: `test/Leaf_Healthy/Leaf_Healthy_402.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_252.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_409.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_278.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_442.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_163.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_455.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_130.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_79.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_424.jpg`
- distance=4: `test/Leaf_Healthy/Leaf_Healthy_98.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_159.jpg`
- distance=4: `test/Leaf_Rhizoctonia/Leaf_Rhizoctonia_27.jpg` <-> `train/Leaf_Rhizoctonia/Leaf_Rhizoctonia_82.jpg`
- distance=0: `train/Leaf_Algal/Leaf_Algal_24.jpg` <-> `val/Leaf_Algal/Leaf_Algal_23.jpg`
- distance=0: `train/Leaf_Algal/Leaf_Algal_28.jpg` <-> `val/Leaf_Algal/Leaf_Algal_29.jpg`
- distance=0: `train/Leaf_Algal/Leaf_Algal_290.jpg` <-> `val/Leaf_Algal/Leaf_Algal_288.jpg`
- distance=0: `train/Leaf_Algal/Leaf_Algal_38.jpg` <-> `val/Leaf_Algal/Leaf_Algal_37.jpg`
- distance=6: `train/Leaf_Blight/Leaf_Blight_118.jpg` <-> `train/Leaf_Blight/Leaf_Blight_87.jpg`
- distance=2: `train/Leaf_Blight/Leaf_Blight_123.jpg` <-> `train/Leaf_Blight/Leaf_Blight_58.jpg`
- distance=6: `train/Leaf_Blight/Leaf_Blight_134.jpg` <-> `val/Leaf_Colletotrichum/Leaf_Colletotrichum_399.jpg`
- distance=0: `train/Leaf_Blight/Leaf_Blight_154.jpg` <-> `val/Leaf_Blight/Leaf_Blight_163.jpg`
- distance=6: `train/Leaf_Blight/Leaf_Blight_155.jpg` <-> `train/Leaf_Blight/Leaf_Blight_67.jpg`
- distance=6: `train/Leaf_Blight/Leaf_Blight_168.jpg` <-> `train/Leaf_Blight/Leaf_Blight_49.jpg`
- distance=6: `train/Leaf_Blight/Leaf_Blight_180.jpg` <-> `train/Leaf_Blight/Leaf_Blight_209.jpg`
- distance=2: `train/Leaf_Blight/Leaf_Blight_219.jpg` <-> `train/Leaf_Blight/Leaf_Blight_50.jpg`
- distance=0: `train/Leaf_Blight/Leaf_Blight_40.jpg` <-> `val/Leaf_Blight/Leaf_Blight_41.jpg`
- distance=0: `train/Leaf_Blight/Leaf_Blight_75.jpg` <-> `train/Leaf_Colletotrichum/Leaf_Colletotrichum_397.jpg`
- distance=0: `train/Leaf_Healthy/Leaf_Healthy_108.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_203.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_109.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_261.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_115.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_136.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_115.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_174.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_124.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_467.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_135.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_465.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_136.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_174.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_145.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_56.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_148.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_428.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_148.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_482.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_149.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_86.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_155.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_441.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_158.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_175.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_161.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_480.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_166.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_436.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_167.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_439.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_169.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_435.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_185.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_332.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_192.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_301.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_195.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_406.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_198.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_310.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_199.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_362.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_200.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_361.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_200.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_311.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_205.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_320.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_208.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_316.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_210.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_443.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_216.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_351.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_217.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_271.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_222.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_313.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_225.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_299.jpg`
- distance=0: `train/Leaf_Healthy/Leaf_Healthy_232.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_335.jpg`
- distance=0: `train/Leaf_Healthy/Leaf_Healthy_232.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_342.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_234.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_306.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_234.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_331.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_238.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_324.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_241.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_329.jpg`
- distance=0: `train/Leaf_Healthy/Leaf_Healthy_248.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_344.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_249.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_375.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_250.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_400.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_251.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_268.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_254.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_407.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_255.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_345.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_263.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_379.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_267.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_364.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_270.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_93.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_273.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_415.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_274.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_413.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_297.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_386.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_306.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_331.jpg`
- distance=0: `train/Leaf_Healthy/Leaf_Healthy_335.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_342.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_347.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_66.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_357.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_226.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_361.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_311.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_368.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_219.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_370.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_221.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_371.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_280.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_373.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_85.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_401.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_60.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_426.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_276.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_427.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_80.jpg`
- distance=6: `train/Leaf_Healthy/Leaf_Healthy_433.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_73.jpg`
- distance=4: `train/Leaf_Healthy/Leaf_Healthy_463.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_134.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_470.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_188.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_472.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_178.jpg`
- distance=0: `train/Leaf_Healthy/Leaf_Healthy_477.jpg` <-> `train/Leaf_Healthy/Leaf_Healthy_74.jpg`
- distance=2: `train/Leaf_Healthy/Leaf_Healthy_481.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_144.jpg`
- distance=2: `train/Leaf_Rhizoctonia/Leaf_Rhizoctonia_215.jpg` <-> `train/Leaf_Rhizoctonia/Leaf_Rhizoctonia_326.jpg`
- distance=6: `train/Leaf_Rhizoctonia/Leaf_Rhizoctonia_216.jpg` <-> `train/Leaf_Rhizoctonia/Leaf_Rhizoctonia_327.jpg`
- distance=0: `train/Leaf_Rhizoctonia/Leaf_Rhizoctonia_92.jpg` <-> `train/Leaf_Rhizoctonia/Leaf_Rhizoctonia_93.jpg`
- distance=2: `val/Leaf_Healthy/Leaf_Healthy_265.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_416.jpg`
- distance=4: `val/Leaf_Healthy/Leaf_Healthy_380.jpg` <-> `val/Leaf_Healthy/Leaf_Healthy_58.jpg`

## Required Human Review

- Review every exact duplicate crossing train/val/test because it may cause evaluation leakage.
- Review every exact duplicate with different labels because it may indicate labeling conflict or source-data error.
- Review near-duplicate pairs before training; this audit does not remove or relabel anything.
- Confirm whether grayscale/RGBA images are intentional and whether the selected preprocessing handles them.
- Validate domain labels against the original dataset documentation; folder names alone are not proof of correctness.

## Recommendation

- Dataset is structurally suitable for the next Data Pipeline step only after the duplicate and label conflicts above are reviewed.
