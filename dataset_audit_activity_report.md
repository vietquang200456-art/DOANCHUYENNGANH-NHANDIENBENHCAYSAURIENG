# Báo cáo hoạt động triển khai Dataset Audit – DurianLeafAI

- Ngày thực hiện: 30/10/2026
- Phạm vi: kiểm toán chất lượng dataset, không triển khai Data Pipeline, mô hình, huấn luyện hoặc inference.
- Dataset: `Dataset/`
- Nguyên tắc bảo toàn dữ liệu: chỉ đọc; không xóa, di chuyển, đổi tên, sửa nội dung hoặc đổi nhãn ảnh gốc.

## 1. Tình trạng project trước khi thực hiện

Project đã có cấu trúc thư mục theo thiết kế, gồm `Dataset/`, `src/data/`, `scripts/`, `configs/` và các thư mục output. Các file Python liên quan đến audit khi bắt đầu đều đang rỗng; `configs/config.yaml` cũng chưa có cấu hình. Báo cáo sơ bộ trước đó mới kiểm tra cấu trúc file, phần mở rộng, file rỗng và SHA-256, chưa giải mã ảnh, chưa ghi metadata ảnh và chưa kiểm tra ảnh gần trùng.

Các file nguồn khác của dự án như model, training, inference và prediction không thuộc phạm vi lần này và không được triển khai.

## 2. Các hoạt động đã thực hiện

### 2.1. Rà soát trước khi sửa

- Đọc cấu trúc thư mục hiện tại.
- Đọc README, tài liệu thiết kế `Thiet_ke_project_DurianLeafAI (1).md`, config và báo cáo sơ bộ.
- Kiểm tra môi trường Python và các thư viện cần cho audit.
- Xác nhận có thể sử dụng Pillow, NumPy, pandas, PyYAML và Matplotlib hiện có; không cài thêm thư viện nặng.

### 2.2. Xây dựng logic kiểm toán

Đã triển khai `src/data/validate_dataset.py` với các chức năng:

- Kiểm tra dataset root tồn tại và là thư mục.
- Kiểm tra ba split `train`, `val`, `test`.
- Kiểm tra sáu class dự kiến trong mỗi split.
- Đếm số file theo split và class.
- Phát hiện phần mở rộng không hỗ trợ và file rỗng.
- Đọc/giải mã từng ảnh bằng Pillow.
- Ghi nhận width, height, mode màu và định dạng thực tế.
- Tính SHA-256 cho ảnh đọc được.
- Nhóm exact duplicate và phân biệt duplicate cùng/khác split, cùng/khác nhãn.
- Kiểm tra near duplicate bằng perceptual hash DCT tự triển khai, không phụ thuộc thư viện ngoài.
- Xuất báo cáo Markdown và CSV.
- Bảo đảm logic audit không sửa dataset gốc.

### 2.3. Xây dựng lệnh chạy

Đã triển khai `scripts/check_dataset.py` làm entry point từ terminal, hỗ trợ:

- `--dataset-root`
- `--output-dir`
- `--near-duplicate-threshold`
- `--skip-near-duplicates`

### 2.4. Bổ sung cấu hình

Đã cập nhật `configs/config.yaml` với:

- Dataset root tương đối: `Dataset`.
- Danh sách split.
- Danh sách sáu class.
- Ngưỡng near duplicate mặc định là `6`.
- Thư mục output audit.

## 3. File đã tạo hoặc sửa

### File đã sửa/triển khai

- `src/data/validate_dataset.py`: logic audit và xuất báo cáo.
- `scripts/check_dataset.py`: chương trình chạy audit từ Windows PowerShell.
- `configs/config.yaml`: cấu hình cho bước audit.

### Báo cáo đã tạo

- `outputs/metrics/dataset_audit/dataset_audit_report.md`: báo cáo tổng hợp.
- `outputs/metrics/dataset_audit/dataset_audit_files.csv`: báo cáo theo từng file.

Không tạo file code ngoài phạm vi audit. Không sửa các module training, model, inference hoặc prediction.

## 4. Các lệnh đã chạy

```powershell
python -m py_compile src/data/validate_dataset.py scripts/check_dataset.py
```

```powershell
python scripts/check_dataset.py --skip-near-duplicates
```

```powershell
python scripts/check_dataset.py
```

```powershell
python scripts/check_dataset.py --dataset-root <duong-dan-khong-ton-tai> --skip-near-duplicates
```

Ngoài ra đã tạo dataset fixture tạm ngoài `Dataset/` để kiểm thử file rỗng, file không phải ảnh, duplicate giữa split và duplicate khác nhãn. Fixture được xóa sau khi kiểm thử; dataset thật không bị sửa.

## 5. Kết quả kiểm thử thực tế

- Kiểm tra cú pháp Python: **PASS**.
- Chạy audit với dataset thật: **PASS**.
- Xuất Markdown: **PASS**.
- Xuất CSV: **PASS**.
- Kiểm tra đường dẫn dataset không tồn tại: chương trình phát hiện lỗi và trả exit code lỗi phù hợp.
- Kiểm thử fixture độc lập với ảnh lỗi/file rỗng/file sai loại/duplicate: **PASS**.
- Audit không làm thay đổi dataset gốc.

## 6. Kết quả quét dataset thực tế

- Tổng số file: **2.595**.
- Ảnh đọc và giải mã thành công: **2.595**.
- Ảnh lỗi hoặc không đọc được: **0**.
- Lỗi cấu trúc split/class: **0**.
- Train: **1.814** ảnh.
- Validation: **387** ảnh.
- Test: **394** ảnh.

Phân bố mode màu:

- `RGB`: **2.591** ảnh.
- `RGBA`: **4** ảnh.

Phân bố định dạng thực tế:

- `JPEG`: **2.591** ảnh.
- `PNG`: **4** ảnh.

Exact duplicate:

- Tổng cộng: **12 nhóm**.
- Duplicate giữa các split: **9 nhóm**.
- Duplicate khác nhãn: **5 nhóm**.

Near duplicate:

- Tính năng đã bật.
- Ngưỡng Hamming distance: **6**.
- Phát hiện: **131 cặp nghi ngờ**.
- Đây là kết quả sàng lọc, không phải kết luận tự động rằng các ảnh là cùng một mẫu.

## 7. Tình trạng project sau khi hoàn thành

### Đã hoàn thành

- Có công cụ audit chạy được từ thư mục gốc project.
- Có kiểm tra cấu trúc, khả năng đọc ảnh, metadata, exact duplicate và near duplicate.
- Có báo cáo Markdown và CSV.
- Có thể chạy lại trên Windows bằng đường dẫn tương đối hoặc tham số CLI.
- Không cần cài thêm thư viện perceptual hash.

### Chưa triển khai và không thuộc nhiệm vụ này

- Data Pipeline.
- Dataset transforms cho training.
- MobileNetV3-Small.
- Training.
- Evaluation.
- Prediction ảnh/video.
- Frontend, API hoặc ứng dụng.
- Contact sheet trực quan.

## 8. Các vấn đề cần xác minh thủ công

1. Kiểm tra 9 nhóm exact duplicate giữa train, validation và test vì có nguy cơ data leakage.
2. Kiểm tra 5 nhóm exact duplicate khác nhãn vì có thể có lỗi nhãn hoặc tổ chức dataset nguồn không nhất quán.
3. Kiểm tra 131 cặp near duplicate để xác định ảnh cùng nguồn, cùng cây hoặc chỉ tương tự về hình thức.
4. Xác minh 4 ảnh `RGBA` có cần giữ alpha hay sẽ được chuẩn hóa ở Data Pipeline sau này.
5. Xác minh ý nghĩa chuyên ngành của sáu nhãn; tên thư mục không tự chứng minh nhãn đúng.
6. Ghi lại quyết định xử lý duplicate trước khi huấn luyện: giữ, loại khỏi split, hoặc xác minh lại nguồn.

## 9. Đánh giá điều kiện chuyển sang Data Pipeline

**Chưa nên chuyển dataset sang Data Pipeline chính thức ngay.**

Về kỹ thuật đọc file và cấu trúc, dataset đạt yêu cầu: toàn bộ 2.595 ảnh đều đọc được và không có lỗi cấu trúc. Tuy nhiên, chưa đạt điều kiện an toàn cho huấn luyện vì còn duplicate giữa các split, duplicate khác nhãn và nhiều near duplicate cần con người xác minh.

Sau khi các nhóm trên được xem xét và có quyết định rõ ràng, có thể chuyển sang bước xây dựng Data Pipeline. Không nên tự động xóa hoặc đổi nhãn chỉ dựa trên báo cáo này.

## 10. Lệnh chạy lại trên Windows

Từ thư mục gốc project:

```powershell
python scripts/check_dataset.py
```

Chạy nhanh, bỏ qua near duplicate:

```powershell
python scripts/check_dataset.py --skip-near-duplicates
```

Chỉ định đường dẫn dataset và output:

```powershell
python scripts/check_dataset.py `
  --dataset-root .\Dataset `
  --output-dir .\outputs\metrics\dataset_audit
```

Thay đổi ngưỡng near duplicate:

```powershell
python scripts/check_dataset.py --near-duplicate-threshold 8
```

## 11. Báo cáo chi tiết

- Markdown: `outputs/metrics/dataset_audit/dataset_audit_report.md`
- CSV: `outputs/metrics/dataset_audit/dataset_audit_files.csv`
- Logic audit: `src/data/validate_dataset.py`
- CLI: `scripts/check_dataset.py`
