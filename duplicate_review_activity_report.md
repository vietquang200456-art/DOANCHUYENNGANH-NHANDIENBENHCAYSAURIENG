# Báo cáo tổng hợp rà soát ảnh trùng lặp – DurianLeafAI

- Ngày thực hiện: 30/10/2026
- Phạm vi: hỗ trợ con người rà soát exact duplicate và near duplicate trong dataset.
- Dataset: `Dataset/`
- Nguyên tắc: không xóa, di chuyển, đổi tên, chỉnh sửa hoặc đổi nhãn ảnh gốc.
- Không triển khai Data Pipeline, model, training, evaluation hoặc inference.

## 1. Mục tiêu

Xây dựng công cụ đọc kết quả Dataset Audit, lập danh sách đầy đủ các nhóm ảnh trùng lặp, tạo contact sheet để kiểm tra trực quan và xuất CSV để ghi nhận quyết định xử lý thủ công.

## 2. Hoạt động đã thực hiện

- Đọc cấu trúc project và tài liệu audit hiện có.
- Kiểm tra header và nội dung thực tế của `dataset_audit_files.csv`.
- Tái sử dụng thông tin SHA-256, split, class và đường dẫn tương đối từ kết quả audit.
- Bổ sung xuất danh sách near duplicate có thông tin split/class và khoảng cách Hamming.
- Viết công cụ `scripts/review_duplicates.py`.
- Tạo CSV review với trạng thái ban đầu chưa rà soát.
- Tạo contact sheet cho exact duplicate.
- Tạo contact sheet cho near duplicate và chia thành nhiều trang.
- Kiểm tra cú pháp, import và chạy trên dataset thực tế.

## 3. File đã tạo hoặc sửa

### File code

- `scripts/review_duplicates.py`
  - Đọc CSV audit.
  - Nhóm exact duplicate theo SHA-256.
  - Phân loại duplicate theo split và class.
  - Tạo bảng review.
  - Tạo contact sheet có chú thích.
  - Xử lý lỗi đọc ảnh trong contact sheet mà không dừng toàn bộ chương trình.

### File code đã bổ sung

- `src/data/validate_dataset.py`
  - Bổ sung file CSV riêng cho near duplicate:
    `dataset_audit_near_duplicates.csv`.
  - Ghi đường dẫn, split, class, khoảng cách Hamming và kích thước hash.

### File báo cáo/dữ liệu đầu ra

- `outputs/metrics/dataset_audit/dataset_audit_near_duplicates.csv`
- `outputs/metrics/dataset_audit/review/duplicate_review.csv`
- `outputs/metrics/dataset_audit/review/contact_sheets/exact_duplicates_001.jpg`
- `outputs/metrics/dataset_audit/review/contact_sheets/exact_duplicates_002.jpg`
- `outputs/metrics/dataset_audit/review/contact_sheets/near_duplicates_001.jpg` đến `near_duplicates_022.jpg`

## 4. Kết quả rà soát được đưa vào review

- Exact duplicate: **12 nhóm**.
- File thuộc các nhóm exact duplicate: **24 dòng review**.
- Near duplicate: **131 cặp**.
- Tổng số dòng trong `duplicate_review.csv`: **155 dòng**.
- Contact sheet exact duplicate: **2 trang**.
- Contact sheet near duplicate: **22 trang**.

Các nhóm exact duplicate được ghi nhận đầy đủ từng file, không chỉ lưu một đại diện. Vì vậy, các nhóm có nhiều ảnh vẫn không bị mất thông tin.

## 5. Phân loại và mức độ ưu tiên

### Exact duplicate

Công cụ phân loại các nhóm theo các trạng thái:

- `exact_same_split_same_label`
- `exact_cross_split_same_label`
- `exact_same_split_different_label`
- `exact_cross_split_different_label`

Mức ưu tiên:

- `HIGH`: khác split hoặc khác class.
- `MEDIUM`: cùng split và cùng class.

### Near duplicate

Mỗi cặp near duplicate có:

- `pair_id` dạng `NEAR-001`, `NEAR-002`, ... trong cột `group_id`.
- Hai đường dẫn ảnh.
- Split và class của hai ảnh.
- Khoảng cách Hamming.
- Mức ưu tiên.
- Trạng thái và quyết định để trống cho người rà soát.

## 6. Cấu trúc CSV review

File chính:

`outputs/metrics/dataset_audit/review/duplicate_review.csv`

Các cột:

- `group_id`
- `file_path_1`
- `file_path_2`
- `split_1`
- `split_2`
- `class_1`
- `class_2`
- `duplicate_type`
- `sha256`
- `hamming_distance`
- `priority`
- `review_status`
- `decision`
- `review_notes`

Trạng thái ban đầu:

- `review_status`: `not_reviewed`
- `decision`: để trống.
- `review_notes`: để trống.

Công cụ không tự quyết định ảnh nào đúng, ảnh nào sai và không tự động xử lý dataset.

## 7. Contact sheet

Thư mục contact sheet:

`outputs/metrics/dataset_audit/review/contact_sheets/`

Mỗi ô ảnh có chú thích để đối chiếu:

- Mã nhóm hoặc mã cặp.
- Tên file.
- Split.
- Class.
- Khoảng cách Hamming nếu là near duplicate.

Contact sheet được chia thành nhiều trang, không tạo một ảnh duy nhất quá lớn. Có thể mở thư mục bằng Windows Explorer:

```powershell
ii .\outputs\metrics\dataset_audit\review\contact_sheets
```

## 8. Kiểm thử đã thực hiện

- Kiểm tra cú pháp `scripts/review_duplicates.py`: **PASS**.
- Kiểm tra import các module liên quan: **PASS**.
- Đọc CSV audit thực tế: **PASS**.
- Tạo CSV review: **PASS**.
- Tạo contact sheet exact duplicate: **PASS**.
- Tạo contact sheet near duplicate: **PASS**.
- Kiểm tra số nhóm exact duplicate: **12**, khớp kết quả audit.
- Kiểm tra số near duplicate: **131**, khớp kết quả audit.
- Xác minh đường dẫn trong CSV trỏ tới file thuộc `Dataset/`: **PASS**.
- Xác minh dữ liệu gốc không bị thay đổi: **PASS**.

## 9. Các nhóm cần ưu tiên kiểm tra thủ công

1. Exact duplicate nằm ở nhiều split, đặc biệt các nhóm có ảnh trong train và validation/test.
2. Exact duplicate nhưng khác class, vì có khả năng xung đột nhãn.
3. Near duplicate nằm khác split, vì có thể gây rò rỉ dữ liệu gần giống.
4. Near duplicate khác class, vì có thể chỉ ra vấn đề nhãn hoặc ảnh rất khó phân biệt.
5. Các ảnh có cùng nguồn chụp nhưng khác checksum; perceptual hash chỉ là cảnh báo và cần xem trực tiếp.

## 10. Cách ghi quyết định

Mở file:

`outputs/metrics/dataset_audit/review/duplicate_review.csv`

Sau khi xem contact sheet, cập nhật các cột:

- `review_status`: đặt thành `reviewed` khi đã kiểm tra.
- `decision`: ghi quyết định như `keep_both`, `needs_source_check`, `possible_leakage`, `label_conflict` hoặc quyết định phù hợp khác.
- `review_notes`: ghi lý do, ảnh cần giữ/xem lại và người xác minh nếu cần.

Chỉ cập nhật CSV review. Không sửa trực tiếp các ảnh trong `Dataset/` và không tự động áp dụng quyết định trong file CSV.

## 11. Tình trạng project sau nhiệm vụ

Project hiện đã có:

- Công cụ Dataset Audit.
- Công cụ tạo danh sách review duplicate.
- CSV exact/near duplicate phục vụ kiểm tra thủ công.
- Contact sheet để so sánh trực quan.
- Báo cáo audit theo file và theo nhóm.

Project vẫn chưa có:

- Quyết định cuối cùng của người dùng về các duplicate.
- Quy trình xử lý/xóa/di chuyển ảnh sau khi review.
- Data Pipeline.
- Mô hình MobileNetV3-Small.
- Training, evaluation hoặc inference.

## 12. Kết luận

Bước hỗ trợ rà soát ảnh trùng lặp đã hoàn thành về mặt công cụ và báo cáo. Dataset gốc được bảo toàn. Tuy nhiên, chưa thể kết luận dataset đã sẵn sàng huấn luyện cho đến khi người dùng kiểm tra các nhóm exact duplicate, các cặp near duplicate và các trường hợp khác nhãn trong `duplicate_review.csv`.
