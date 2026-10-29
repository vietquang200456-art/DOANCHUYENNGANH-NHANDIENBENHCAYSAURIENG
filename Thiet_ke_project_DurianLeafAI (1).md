# Thiết kế Project AI nhận diện bệnh lá cây sầu riêng bằng Deep Learning

## 1. Tổng quan dự án

**Tên dự án đề xuất:** DurianLeafAI -- Nhận diện tình trạng lá cây sầu
riêng từ ảnh và video.

Mục tiêu là xây dựng một mô hình Deep Learning phân loại ảnh lá thành 6
lớp theo dataset hiện có:

-   `Leaf_Algal`
-   `Leaf_Blight`
-   `Leaf_Colletotrichum`
-   `Leaf_Healthy`
-   `Leaf_Phomopsis`
-   `Leaf_Rhizoctonia`

Các tên lớp trên cần được đối chiếu với nguồn dataset và tài liệu chuyên
ngành để xác nhận rằng nhãn thực sự thuộc cây sầu riêng và được gán
chính xác. Không nên xem tên thư mục là bằng chứng đủ để xác nhận bệnh.

### Phạm vi triển khai

1.  Kiểm tra và chuẩn hóa dataset.
2.  Huấn luyện một mô hình phân loại ảnh bằng transfer learning.
3.  Đánh giá mô hình bằng tập test độc lập.
4.  Nhận diện ảnh lá riêng lẻ.
5.  Mở rộng sang video: trích xuất frame, chọn/cắt vùng lá khi cần, phân
    loại từng frame và tổng hợp kết quả.
6.  Lưu trọng số, chỉ số đánh giá và ví dụ dự đoán để phục vụ báo cáo đồ
    án.

**Lưu ý:** Đây là công cụ hỗ trợ nhận diện từ hình ảnh, không phải kết
luận chẩn đoán bệnh chắc chắn. Nếu ảnh đầu vào không giống dữ liệu huấn
luyện, lá bị che khuất hoặc có nhiều yếu tố gây nhiễu, kết quả có thể
không đáng tin cậy.

------------------------------------------------------------------------

## 2. Công nghệ đề xuất

  -----------------------------------------------------------------------
  Thành phần              Công nghệ đề xuất       Mục đích
  ----------------------- ----------------------- -----------------------
  Ngôn ngữ                Python 3.11             Ngôn ngữ chính

  Deep Learning           PyTorch, Torchvision    Huấn luyện và suy luận
                                                  mô hình

  Xử lý ảnh/video         OpenCV, Pillow          Đọc ảnh, đọc video,
                                                  trích xuất frame

  Dữ liệu và đánh giá     NumPy, pandas,          Thống kê dữ liệu, tính
                          scikit-learn            chỉ số đánh giá

  Biểu đồ                 Matplotlib              Vẽ đường cong huấn
                                                  luyện và confusion
                                                  matrix

  Cấu hình                YAML                    Quản lý tham số huấn
                                                  luyện

  Mô hình ban đầu         MobileNetV3 hoặc        Phân loại 6 lớp, tương
                          EfficientNet-B0         đối gọn nhẹ
                          pretrained              
  -----------------------------------------------------------------------

Nên bắt đầu với **một mô hình chính**. Có thể chọn MobileNetV3 để ưu
tiên nhẹ và nhanh, hoặc EfficientNet-B0 để làm mô hình thử nghiệm có
tính cân bằng. Không cần huấn luyện cả hai ngay từ đầu; nếu muốn so
sánh, hãy thực hiện như một thí nghiệm bổ sung có cùng điều kiện đánh
giá.

------------------------------------------------------------------------

## 3. Cấu trúc thư mục project

``` text
DurianLeafAI/
├── Dataset/
│   ├── train/
│   │   ├── Leaf_Algal/
│   │   ├── Leaf_Blight/
│   │   ├── Leaf_Colletotrichum/
│   │   ├── Leaf_Healthy/
│   │   ├── Leaf_Phomopsis/
│   │   └── Leaf_Rhizoctonia/
│   ├── val/
│   │   ├── Leaf_Algal/
│   │   ├── Leaf_Blight/
│   │   ├── Leaf_Colletotrichum/
│   │   ├── Leaf_Healthy/
│   │   ├── Leaf_Phomopsis/
│   │   └── Leaf_Rhizoctonia/
│   └── test/
│       ├── Leaf_Algal/
│       ├── Leaf_Blight/
│       ├── Leaf_Colletotrichum/
│       ├── Leaf_Healthy/
│       ├── Leaf_Phomopsis/
│       └── Leaf_Rhizoctonia/
│
├── configs/
│   └── config.yaml
│
├── src/
│   ├── data/
│   │   ├── dataset.py
│   │   ├── transforms.py
│   │   └── validate_dataset.py
│   ├── model/
│   │   ├── classifier.py
│   │   └── predictor.py
│   ├── training/
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── metrics.py
│   ├── inference/
│   │   ├── predict_image.py
│   │   ├── predict_video.py
│   │   ├── frame_extractor.py
│   │   └── leaf_cropper.py
│   └── utils/
│       ├── logger.py
│       ├── checkpoint.py
│       └── visualization.py
│
├── models/
│   ├── best_model.pth
│   └── class_names.json
│
├── data_samples/
│   ├── images/
│   └── videos/
│
├── outputs/
│   ├── logs/
│   ├── metrics/
│   ├── plots/
│   └── predictions/
│
├── scripts/
│   ├── check_dataset.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── tests/
│   └── test_prediction.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

### Vai trò các thư mục

-   **`Dataset/`**: dữ liệu đã chia thành train, val và test. Mỗi ảnh
    nằm trong thư mục tương ứng với nhãn.
-   **`configs/`**: chứa tham số như đường dẫn dữ liệu, kích thước ảnh,
    batch size, số epoch và learning rate.
-   **`src/data/`**: đọc dữ liệu, tiền xử lý và kiểm tra tính hợp lệ của
    dataset.
-   **`src/model/`**: định nghĩa mô hình phân loại và lớp hỗ trợ dự
    đoán.
-   **`src/training/`**: vòng lặp huấn luyện, đánh giá và tính các chỉ
    số.
-   **`src/inference/`**: dự đoán ảnh hoặc video sau khi đã có mô hình
    được huấn luyện.
-   **`models/`**: lưu checkpoint tốt nhất và thứ tự tên lớp.
-   **`data_samples/`**: ảnh/video dùng để demo, tách riêng khỏi dữ liệu
    train.
-   **`outputs/`**: lưu log, biểu đồ, kết quả đánh giá và ảnh/video minh
    họa.
-   **`scripts/`**: các lệnh chạy thường dùng để thuận tiện cho người
    phát triển.
-   **`tests/`**: kiểm tra các chức năng quan trọng, ví dụ nạp mô hình
    và dự đoán ảnh.

Không cần tạo sẵn mọi file ngay từ ngày đầu. Hãy triển khai theo từng
giai đoạn; có thể bắt đầu với các file kiểm tra dữ liệu, dataset loader,
mô hình, huấn luyện, đánh giá và dự đoán ảnh.

------------------------------------------------------------------------

## 4. Quy trình tổng thể của hệ thống

``` text
Dataset ảnh đã gán nhãn
        |
        v
Kiểm tra dữ liệu và nhãn
        |
        v
Đọc train / val / test
        |
        v
Tiền xử lý và augmentation (chỉ áp dụng phù hợp cho train)
        |
        v
Khởi tạo mô hình pretrained, thay lớp đầu ra thành 6 lớp
        |
        v
Huấn luyện trên train
        |
        v
Đánh giá trên val sau mỗi epoch
        |
        v
Lưu checkpoint tốt nhất theo chỉ số đã chọn
        |
        v
Đánh giá cuối cùng trên test
        |
        v
Lưu metrics, confusion matrix và biểu đồ
        |
        v
Dùng mô hình đã lưu để dự đoán ảnh / video mới
```

### 4.1. Kiểm tra và chuẩn bị dữ liệu

Trước khi train:

1.  Đếm số ảnh của từng lớp trong từng tập.
2.  Kiểm tra ảnh bị hỏng, định dạng không hỗ trợ và file trùng.
3.  Xem ảnh mẫu để xác nhận nhãn và loại cây.
4.  Kiểm tra ảnh gần trùng hoặc cùng ảnh gốc có nằm ở nhiều tập hay
    không.
5.  Xác nhận cách chia train/val/test không làm rò rỉ dữ liệu.

Nếu có nhiều ảnh chụp từ cùng một lá, cùng một cây hoặc cùng một video,
nên chia dữ liệu theo nguồn/cây/video trước khi tạo các tập train, val
và test. Nếu không, ảnh gần giống nhau có thể xuất hiện ở cả train và
test khiến kết quả đánh giá quá lạc quan.

### 4.2. Tiền xử lý

-   Đọc ảnh RGB.
-   Resize về kích thước đầu vào thống nhất, ví dụ 224 × 224.
-   Chuẩn hóa theo cấu hình tương thích với mô hình pretrained đã chọn.
-   Dùng augmentation hợp lý cho train, ví dụ lật ảnh hoặc thay đổi độ
    sáng nhẹ khi phù hợp với dữ liệu.
-   Không dùng augmentation ngẫu nhiên cho validation và test.
-   Dùng đúng cùng một quy trình tiền xử lý khi suy luận ảnh/video mới.

### 4.3. Huấn luyện mô hình

1.  Tải mô hình pretrained.
2.  Thay lớp phân loại cuối để đầu ra có 6 lớp.
3.  Tạo DataLoader cho train và validation.
4.  Chọn loss phù hợp, thường bắt đầu với CrossEntropyLoss.
5.  Chọn optimizer, ví dụ AdamW.
6.  Huấn luyện theo epoch.
7.  Theo dõi train loss, validation loss và các chỉ số trên validation.
8.  Lưu checkpoint tốt nhất, không mặc định chọn epoch cuối cùng.

Nên bắt đầu bằng cách đóng băng phần lớn backbone và huấn luyện lớp phân
loại mới. Sau khi có baseline, có thể mở một phần backbone để fine-tune
nếu tài nguyên cho phép.

### 4.4. Đánh giá

Dùng tập test độc lập sau khi đã chốt mô hình và tham số. Nên báo cáo:

-   Accuracy.
-   Precision, Recall và F1-score theo từng lớp.
-   Macro F1-score để quan sát hiệu quả giữa các lớp.
-   Confusion matrix.
-   Số lượng ảnh của mỗi lớp trong test.

Không chỉ dựa vào Accuracy, đặc biệt khi số lượng ảnh giữa các lớp không
cân bằng. Không dùng tập test để điều chỉnh mô hình lặp đi lặp lại.

### 4.5. Dự đoán ảnh mới

Đầu vào: một ảnh lá.

Các bước:

1.  Đọc ảnh.
2.  Chuyển sang RGB và tiền xử lý giống lúc validation/test.
3.  Nạp `best_model.pth` cùng danh sách lớp.
4.  Chạy suy luận.
5.  Lấy lớp có điểm dự đoán cao nhất.
6.  Hiển thị nhãn dự đoán và điểm tin cậy.
7.  Nếu điểm tin cậy thấp hoặc ảnh khác biệt nhiều so với dữ liệu train,
    nên trả về thông báo "chưa đủ tin cậy", thay vì khẳng định bệnh.

Điểm softmax cao không đồng nghĩa với xác suất đúng đã được hiệu chuẩn
hoặc bảo đảm chẩn đoán chính xác.

------------------------------------------------------------------------

## 5. Quy trình nhận diện video quay tại vườn

Mô hình phân loại ảnh không trực tiếp hiểu toàn bộ video. Chương trình
video cần chuyển video thành các ảnh/frame rồi đưa từng frame hoặc vùng
lá đã cắt vào mô hình.

``` text
Video quay tại vườn
        |
        v
Đọc video bằng OpenCV
        |
        v
Lấy frame theo khoảng thời gian
        |
        v
Kiểm tra frame có nhìn rõ lá không
        |
        v
[Tuỳ chọn] Phát hiện / cắt vùng lá
        |
        v
Tiền xử lý vùng lá
        |
        v
Mô hình phân loại 6 lớp
        |
        v
Tổng hợp kết quả qua nhiều frame
        |
        v
Xuất bảng kết quả và video minh họa
```

### Lưu ý khi thiết kế phần video

-   Nếu video quay cận cảnh một lá, có thể phân loại frame trực tiếp sau
    khi loại bỏ frame mờ.
-   Nếu video quay toàn cây và lá chỉ chiếm diện tích nhỏ, cần có bước
    tìm/cắt vùng lá. Phân loại trực tiếp toàn frame có thể cho kết quả
    sai.
-   `leaf_cropper.py` chỉ nên được hiện thực theo phương pháp phù hợp
    với dữ liệu. Crop theo tọa độ cố định chỉ phù hợp nếu cách quay được
    kiểm soát; không nên mặc định nó sẽ tìm đúng lá trong mọi video.
-   Có thể lấy một frame mỗi 0,5--1 giây để giảm số ảnh phải xử lý; điều
    chỉnh tùy tốc độ quay và hiệu năng máy.
-   Không nên coi mỗi frame là một mẫu độc lập khi tính độ tin cậy tổng
    thể, vì các frame liền kề thường rất giống nhau.
-   Tổng hợp kết quả theo đa số phiếu hoặc trung bình điểm dự đoán có
    thể giảm dao động, nhưng cần kiểm thử thực tế.
-   Cần lưu cả kết quả từng frame và kết quả tổng hợp để dễ kiểm tra
    lỗi.

### Kết quả đầu ra dự kiến

-   Tên video đầu vào.
-   Thời điểm/frame được phân tích.
-   Nhãn dự đoán và điểm tin cậy cho từng frame.
-   Kết quả tổng hợp của video.
-   Danh sách frame không rõ hoặc có điểm tin cậy thấp.
-   File CSV/JSON và video minh họa có thể được lưu vào
    `outputs/predictions/`.

Kết quả trên video thực tế cần được đánh giá riêng. Một mô hình có kết
quả tốt trên test set ảnh tĩnh vẫn có thể hoạt động kém khi video có ánh
sáng, góc chụp, khoảng cách hoặc nền khác biệt.

------------------------------------------------------------------------

## 6. File cấu hình tham khảo

Ví dụ nội dung `configs/config.yaml`:

``` yaml
project:
  name: DurianLeafAI
  seed: 42

data:
  root: Dataset
  image_size: 224
  num_classes: 6
  class_names:
    - Leaf_Algal
    - Leaf_Blight
    - Leaf_Colletotrichum
    - Leaf_Healthy
    - Leaf_Phomopsis
    - Leaf_Rhizoctonia

training:
  batch_size: 32
  epochs: 20
  learning_rate: 0.0001
  num_workers: 2
  model_name: mobilenet_v3_small
  pretrained: true

paths:
  checkpoint_dir: models
  output_dir: outputs
```

Đây chỉ là cấu hình khởi đầu. Batch size và `num_workers` cần điều chỉnh
theo RAM, GPU và hệ điều hành. Nếu máy không đủ bộ nhớ, giảm batch size
xuống 16 hoặc 8. Danh sách lớp trong cấu hình phải khớp với nhãn thực tế
mà bộ nạp dữ liệu sử dụng; tránh tự giả định thứ tự nhãn nếu thư viện tự
sắp xếp tên lớp.

------------------------------------------------------------------------

## 7. Cài đặt môi trường và chạy project

Các lệnh dưới đây giả định bạn đang đứng ở thư mục gốc `DurianLeafAI/`
và dùng Windows với PowerShell. Có thể cần điều chỉnh đường dẫn theo vị
trí project trên máy.

### Bước 1: Tạo môi trường ảo

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Nếu PowerShell chặn kích hoạt script, có thể chạy các lệnh qua Command
Prompt hoặc dùng cách kích hoạt phù hợp với chính sách máy; không cần
thay đổi chính sách hệ thống một cách tùy tiện.

### Bước 2: Cài thư viện

Tạo `requirements.txt` với các thư viện nền tảng:

``` text
torch
torchvision
numpy
pandas
scikit-learn
matplotlib
opencv-python
Pillow
PyYAML
tqdm
```

Sau đó chạy:

``` powershell
pip install -r requirements.txt
```

Lệnh cài PyTorch có thể cần chọn bản phù hợp với CPU hoặc CUDA theo phần
cứng. Nên kiểm tra hướng dẫn cài đặt chính thức của PyTorch để chọn đúng
phiên bản; không mặc định rằng máy có GPU NVIDIA hoặc CUDA hoạt động.

### Bước 3: Kiểm tra dataset

Sau khi triển khai script kiểm tra dữ liệu:

``` powershell
python scripts/check_dataset.py
```

Script nên in số ảnh của từng lớp trong train/val/test, báo ảnh lỗi và
cảnh báo lớp thiếu dữ liệu. Nếu chưa tạo script này, cần triển khai
trước khi chạy lệnh.

### Bước 4: Huấn luyện

``` powershell
python scripts/train_model.py
```

Script huấn luyện cần đọc cấu hình, tạo dataset loader, khởi tạo mô
hình, huấn luyện, đánh giá trên validation và lưu checkpoint tốt nhất.

### Bước 5: Đánh giá trên test

``` powershell
python scripts/evaluate_model.py
```

Chỉ chạy sau khi đã chọn xong mô hình. Kết quả cần lưu vào
`outputs/metrics/` và `outputs/plots/`.

### Bước 6: Dự đoán ảnh

Sau khi triển khai `src/inference/predict_image.py`, có thể chạy theo
giao diện dòng lệnh dự kiến:

``` powershell
python -m src.inference.predict_image --image "data_samples/images/la_sau_rieng.jpg"
```

Lệnh trên là giao diện chạy được đề xuất; cần bảo đảm script đã hỗ trợ
tham số `--image` trước khi sử dụng.

### Bước 7: Dự đoán video

Sau khi triển khai `src/inference/predict_video.py`:

``` powershell
python -m src.inference.predict_video --video "data_samples/videos/vuon_sau_rieng.mp4"
```

Đây cũng là lệnh dự kiến; script phải được viết để nhận tham số
`--video`, nạp checkpoint và xuất kết quả tương ứng.

------------------------------------------------------------------------

## 8. Quy tắc quản lý mô hình và kết quả

### File mô hình

-   `models/best_model.pth`: trọng số của checkpoint tốt nhất.
-   `models/class_names.json`: danh sách tên lớp theo đúng thứ tự đầu
    ra.
-   Nếu cần tái lập huấn luyện, nên lưu thêm optimizer state, epoch, cấu
    hình và seed trong checkpoint.

### Kết quả

-   `outputs/logs/`: log theo từng lần chạy.
-   `outputs/metrics/`: JSON/CSV chứa các chỉ số đánh giá.
-   `outputs/plots/`: loss curve, accuracy curve và confusion matrix.
-   `outputs/predictions/`: kết quả dự đoán ảnh/video.

Mỗi lần huấn luyện nên có thông tin về ngày chạy, phiên bản cấu hình,
dataset và checkpoint để tránh nhầm lẫn kết quả.

### `.gitignore` tham khảo

``` gitignore
.venv/
__pycache__/
*.py[cod]
.ipynb_checkpoints/
outputs/
models/*.pth
Dataset/
```

Nếu cần chia sẻ dataset hoặc checkpoint qua Git, hãy cân nhắc dung
lượng, quyền sử dụng và cách quản lý file lớn. Có thể bỏ các dòng
`Dataset/` hoặc `models/*.pth` nếu dự án thực sự cần quản lý những file
đó trong một hệ thống lưu trữ phù hợp.

------------------------------------------------------------------------

## 9. Lộ trình thực hiện theo thứ tự ưu tiên

### Giai đoạn 1 --- Kiểm tra dataset

-   [ ] Xác nhận nguồn và quyền sử dụng dataset.
-   [ ] Xác minh các lớp là bệnh/tình trạng trên lá sầu riêng.
-   [ ] Thống kê số ảnh mỗi lớp.
-   [ ] Kiểm tra ảnh lỗi, trùng lặp và rò rỉ giữa các tập.
-   [ ] Xem trực tiếp các ảnh đại diện của từng lớp.

### Giai đoạn 2 --- Baseline phân loại ảnh

-   [ ] Viết dataset loader và transforms.
-   [ ] Khởi tạo một mô hình pretrained.
-   [ ] Huấn luyện và lưu checkpoint tốt nhất.
-   [ ] Theo dõi train loss và validation loss.
-   [ ] Chạy dự đoán thử trên một ảnh.

### Giai đoạn 3 --- Đánh giá

-   [ ] Chạy test một lần sau khi chốt mô hình.
-   [ ] Tính Accuracy, Precision, Recall và F1-score.
-   [ ] Tạo confusion matrix.
-   [ ] Phân tích các lớp thường bị nhầm lẫn.
-   [ ] Ghi rõ hạn chế của dataset và mô hình.

### Giai đoạn 4 --- Kiểm thử thực tế

-   [ ] Chụp ảnh lá tại vườn với nhiều góc và điều kiện ánh sáng.
-   [ ] Kiểm thử trên ảnh không thuộc sáu lớp đã biết.
-   [ ] Ghi nhận trường hợp dự đoán sai hoặc thiếu tin cậy.
-   [ ] Không coi ảnh tự quay là dữ liệu test độc lập nếu đã dùng chúng
    để điều chỉnh mô hình.

### Giai đoạn 5 --- Mở rộng video và hoàn thiện báo cáo

-   [ ] Viết module trích xuất frame.
-   [ ] Lọc frame mờ và xử lý vùng lá khi cần.
-   [ ] Tổng hợp dự đoán qua các frame.
-   [ ] Xuất kết quả minh họa và log.
-   [ ] Viết báo cáo kiến trúc, dữ liệu, phương pháp, thực nghiệm và hạn
    chế.

------------------------------------------------------------------------

## 10. Các rủi ro cần chú ý

1.  **Sai nhãn hoặc sai loài cây:** mô hình có thể học nhầm đặc trưng
    nếu dataset không đúng cây sầu riêng.
2.  **Mất cân bằng lớp:** Accuracy có thể cao dù mô hình nhận diện kém
    một số lớp; cần xem F1-score từng lớp.
3.  **Rò rỉ dữ liệu:** ảnh cùng cây hoặc cùng video xuất hiện trong
    nhiều tập làm kết quả test thiếu khách quan.
4.  **Khác biệt giữa dataset và vườn thực tế:** nền, ánh sáng, khoảng
    cách và thiết bị chụp có thể làm hiệu quả giảm.
5.  **Video có nhiều lá:** mô hình phân loại ảnh không tự tìm vùng lá;
    cần xử lý/cắt vùng thích hợp.
6.  **Điểm tin cậy bị hiểu sai:** xác suất softmax cao không bảo đảm kết
    quả đúng.
7.  **Khả năng tổng quát hóa:** nếu muốn nhận diện bệnh ngoài sáu lớp,
    cần dữ liệu và chiến lược xử lý lớp chưa biết; mô hình hiện tại chỉ
    được thiết kế để chọn trong sáu lớp.

------------------------------------------------------------------------

## 11. Tiêu chí hoàn thành đồ án

Project có thể xem là hoàn thành phiên bản cơ bản khi:

-   Có cấu trúc mã nguồn rõ ràng, dễ chạy lại.
-   Có mô tả nguồn dataset, cách chia dữ liệu và ý nghĩa từng lớp.
-   Huấn luyện được một mô hình và lưu checkpoint.
-   Có kết quả đánh giá trên test độc lập.
-   Có confusion matrix và các chỉ số theo lớp.
-   Có chương trình dự đoán ảnh mới.
-   Có thử nghiệm video nếu phạm vi đồ án yêu cầu.
-   Có ví dụ dự đoán đúng, sai và phân tích giới hạn.
-   Có README hướng dẫn cài đặt và chạy lại.

**Thứ tự ưu tiên khuyến nghị:** xác minh dataset → train baseline → đánh
giá độc lập → dự đoán ảnh thực tế → xử lý video. Không nên bắt đầu bằng
video khi mô hình phân loại ảnh chưa được kiểm chứng.

------------------------------------------------------------------------

## 12. Tài liệu tham khảo kỹ thuật

-   PyTorch: https://pytorch.org/
-   Torchvision datasets:
    https://pytorch.org/vision/stable/datasets.html
-   Torchvision models: https://pytorch.org/vision/stable/models.html
-   scikit-learn metrics:
    https://scikit-learn.org/stable/modules/model_evaluation.html
-   OpenCV: https://opencv.org/

Tài liệu này mô tả kiến trúc và quy trình triển khai đề xuất. Các lệnh
chạy cho script huấn luyện, đánh giá và suy luận chỉ hoạt động sau khi
những script tương ứng đã được triển khai đúng giao diện tham số nêu
trên.
