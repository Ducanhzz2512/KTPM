# Nhận diện Ngôn ngữ Ký hiệu (Sign Language Recognition)
Giới thiệu

Dự án này tập trung xây dựng một hệ thống nhận diện ngôn ngữ ký hiệu từ hình ảnh hoặc video, nhằm hỗ trợ giao tiếp giữa người khiếm thính và cộng đồng. Hệ thống sử dụng các kỹ thuật xử lý ảnh, học sâu và mô hình phân loại để dự đoán ký hiệu thủ ngữ theo bộ dữ liệu chuẩn.

Mục tiêu của dự án:

Tự động nhận diện và phân loại các ký hiệu tay theo bảng chữ cái hoặc bộ từ khóa.

Cung cấp kết quả theo thời gian thực (nếu dùng webcam) hoặc từ ảnh đầu vào.

Xây dựng nền tảng có thể mở rộng để nhận diện câu, cụm từ trong tương lai.

Tính năng chính

Tiền xử lý ảnh (chuẩn hóa, tách bàn tay, tăng cường dữ liệu).

Nhận diện ký hiệu tay qua mô hình học sâu (CNN / Mediapipe / Transformer tùy triển khai).

Phân loại theo bảng chữ cái ASL/VSL hoặc tập ký hiệu tùy chỉnh.

Hỗ trợ input từ ảnh, video, hoặc webcam thời gian thực.

Kiến trúc hệ thống

Thu thập & Chuẩn hóa dữ liệu

Datasets: ASL Alphabet, MNIST Sign Language hoặc bộ dữ liệu tự thu thập.

Tiền xử lý: cân chỉnh kích thước, chuyển xám/RGB, phát hiện bàn tay.

Trích xuất đặc trưng

Mediapipe Hands / OpenCV / CNN Feature Extraction.

Huấn luyện mô hình phân loại

CNN, MobileNet, hoặc Transformer-based classifier.

Tối ưu hóa bằng kỹ thuật augmentation và regularization.

Suy luận (Inference)

Nhận đầu vào, xử lý và trả về ký hiệu dự đoán theo xác suất.

Công nghệ sử dụng

Python

OpenCV

Mediapipe (nếu dùng landmark)

TensorFlow / PyTorch

NumPy, Pandas, Matplotlib

