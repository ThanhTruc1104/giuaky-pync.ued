from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Mô phỏng Chứng khoán 365 Ngày - FastAPI trên Render")

# Mount thư mục hiện tại để phục vụ tập tin static (video mp4)
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
async def main_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="vi" class="h-full">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mô Phỏng Biến Động Giá Cổ Phiếu 365 Ngày</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-900 text-white min-h-screen flex flex-col items-center justify-center p-4">
        <div class="max-w-4xl w-full bg-gray-800 rounded-lg shadow-xl p-6 border border-gray-700">
            <h1 class="text-2xl md:text-3xl font-bold text-center mb-6 text-blue-400">
                MÔ PHỎNG BIẾN ĐỘNG GIÁ CỔ PHIẾU TRONG 365 NGÀY
            </h1>
            
            <!-- Trình phát Video -->
            <div class="relative overflow-hidden rounded-lg bg-black aspect-video shadow-inner">
                <video controls autoplay loop muted class="w-full h-full object-contain">
                    <source src="/static/mo_phong_chung_khoan.mp4" type="video/mp4">
                    Trình duyệt của bạn không hỗ trợ thẻ video.
                </video>
            </div>

            <div class="mt-6 text-sm text-gray-400 text-center">
                <p>Khung 1: Biểu đồ nến Min-Max | Khung 2: Biểu đồ đường phân theo màu</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content
