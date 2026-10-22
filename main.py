from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Mô phỏng Chứng khoán 365 Ngày - FastAPI trên Render")

# Mount thư mục hiện tại để Render có thể truy cập các tệp tĩnh (như video .mp4)
app.mount("/static", StaticFiles(directory="."), name="static")


@app.get("/", response_class=HTMLResponse)
async def main_page():
  html_content = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mô Phỏng Biến Động Giá Cổ Phiếu</title>
    <!-- Nhúng font Google Inter cho giao diện hiện đại -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        /* 1. Đặt nền web sáng nhạt */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        /* 2. Card bao quanh nội dung chính */
        .container {
            max-width: 1000px;
            width: 100%;
            background: #ffffff;
            padding: 32px;
            border-radius: 16px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
            border: 1px solid #e2e8f0;
            text-align: center;
        }

        /* 3. Tiêu đề chính */
        h1 {
            color: #0f172a;
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 12px;
            letter-spacing: -0.5px;
        }

        /* 4. Nhãn thông tin học phần & lớp học */
        .sub-header {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 28px;
        }

        .badge {
            background-color: #f1f5f9;
            color: #475569;
            font-size: 13px;
            font-weight: 500;
            padding: 6px 14px;
            border-radius: 20px;
            border: 1px solid #e2e8f0;
        }

        .badge-primary {
            background-color: #eff6ff;
            color: #2563eb;
            border-color: #bfdbfe;
            font-weight: 600;
        }

        /* 5. Khung hiển thị Video/Đồ thị */
        .media-wrapper {
            background-color: #0f172a; /* Giữ nền tối cho video để đồ thị nổi bật */
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            border: 1px solid #334155;
        }

        video, img {
            width: 100%;
            height: auto;
            display: block;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Tiêu đề chính -->
        <h1>MÔ PHỎNG BIẾN ĐỘNG GIÁ CỔ PHIẾU TRONG 365 NGÀY</h1>
        
        <!-- Nhãn thông tin -->
        <div class="sub-header">
            <span class="badge badge-primary">Học phần: Lập trình Python Nâng cao</span>
            <span class="badge">Ngành: Khoa học dữ liệu</span>
            <span class="badge">Khoa: Toán - Tin</span>
            <span class="badge">Lớp: 25CKDL</span>
        </div>

        <!-- Khung Video mô phỏng -->
        <div class="media-wrapper">
            <video controls autoplay loop muted>
                <source src="mo_phong_chung_khoan.mp4" type="video/mp4">
                Trình duyệt của bạn không hỗ trợ thẻ video.
            </video>
        </div>
    </div>

</body>
</html>
    """
  return html_content
