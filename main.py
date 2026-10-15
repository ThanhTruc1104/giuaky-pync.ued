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
        <title>Mô Phỏng Biến Động Giá Cổ Phiếu 365 Ngày</title>
        <style>
            body {
                background-color: #0b0f19;
                color: #ffffff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .container {
                max-width: 1100px;
                width: 100%;
                text-align: center;
                background: #111827;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
                border: 1px solid #1f2937;
            }
            h1 {
                color: #38bdf8;
                font-size: 24px;
                margin-bottom: 10px;
            }
            p {
                color: #9ca3af;
                font-size: 14px;
                margin-bottom: 20px;
            }
            video {
                width: 100%;
                border-radius: 8px;
                border: 2px solid #374151;
                background-color: #000;
                outline: none;
            }
            .footer {
                margin-top: 20px;
                font-size: 13px;
                color: #6b7280;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>MÔ PHỎNG BIẾN ĐỘNG GIÁ CỔ PHIẾU TRONG 365 NGÀY</h1>
            <p>Học phần: Lập trình Python Nâng cao</p>
            <p1>Ngành: Khoa học dữ liệu | Khoa: Toán-Tin | Lớp: 25CKDL</p1>
            
            <video controls autoplay muted>
                <source src="/static/mo_phong_chung_khoan.mp4" type="video/mp4">
                Trình duyệt của bạn không hỗ trợ thẻ video.
            </video>
            
            <div class="footer">
                <p>Triển khai thành công trên nền tảng đám mây Render</p>
            </div>
        </div>
    </body>
    </html>
    """
  return html_content
