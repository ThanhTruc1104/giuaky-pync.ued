📈 Mô Phỏng Biến Động Giá Của Một Mã Chứng Khoán
> **Học phần:** Lập trình Python Nâng cao[cite: 2]  
> **Giảng viên hướng dẫn:** Phan Trần Đức Minh[cite: 2]  
> **Học viên thực hiện:** Nguyễn Thị Thanh Trúc[cite: 3]  
> **Mã sinh viên / Lớp:** 25CKDL - Khoa học dữ liệu (Khoa Toán - Tin)[cite: 3]  
> **Trường:** Trường Đại học Sư phạm – Đại học Đà Nẵng (UED-UDN)

🎯 Giới thiệu đề tài
Đề tài được thực hiện nhằm xây dựng một hệ thống mô phỏng toàn diện vòng đời biến động giá cổ phiếu trong suốt **365 ngày giao dịch**. Chương trình không chỉ tái hiện trực quan diễn biến thị trường thông qua biểu đồ nến Min-Max và đường chuỗi phiên đa sắc tuân thủ quy tắc bảng điện chứng khoán, mà còn tiến hành bóc tách sâu các tầng dữ liệu:
- Phân tích biên độ nội phiên và nhận diện các phiên giao dịch biến động cực đoan (Trần, Sàn, Tham chiếu).
- Đánh giá xu hướng biến động theo tháng và quý.
- So sánh phân bố giá giữa các giai đoạn và xác định điểm cực trị toàn năm.

📂 Cấu trúc thư mục kho lưu trữ
```text
├── main.py                    # Mã nguồn Python xử lý dữ liệu và tạo Animation đồ thị
├── abc-9.csv                  # Tệp dữ liệu lịch sử giá chứng khoán 365 ngày[cite: 6]
├── mo_phong_chung_khoan.mp4   # Video hoạt ảnh động mô phỏng trực quan[cite: 14]
├── requirements.txt           # Danh sách các thư viện Python phụ thuộc
└── README.md                  # Tài liệu mô tả dự án
