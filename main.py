from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Mô phỏng Chứng khoán 365 Ngày - FastAPI trên Render")

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
async def main_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="vi" class="h-full">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Báo Cáo Phân Tích & Mô Phỏng Biến Động Giá Cổ Phiếu 365 Ngày</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-gray-100 text-gray-800 min-h-screen p-6 font-sans">
        <div class="max-w-7xl mx-auto space-y-6">
            
            <!-- HEADER THÔNG TIN -->
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div>
                    <div class="flex items-center gap-2 text-sm text-gray-500 font-medium mb-1">
                        <i class="fa-solid fa-chart-line text-blue-600"></i>
                        <span>Đồ Án Lập Trình Python Nâng Cao</span>
                        <span>•</span>
                        <span>Năm Học 2025 – 2026</span>
                    </div>
                    <h1 class="text-2xl md:text-3xl font-extrabold text-gray-900 tracking-tight">
                        MÔ PHỎNG BIẾN ĐỘNG GIÁ CỔ PHIẾU TRONG 365 NGÀY
                    </h1>
                    <div class="flex flex-wrap items-center gap-4 text-xs md:text-sm text-gray-600 mt-3">
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-user-tie text-gray-400"></i> GVHD: <b>Phan Trần Đức Minh</b></span>
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-graduation-cap text-gray-400"></i> Ngành: <b>Khoa học Dữ liệu</b></span>
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-building-columns text-gray-400"></i> <b>Trường ĐH Sư phạm - ĐH Đà Nẵng</b></span>
                    </div>
                </div>

                <div class="flex items-center gap-3 border-t md:border-t-0 md:border-l border-gray-200 pt-3 md:pt-0 md:pl-6">
                    <div class="text-right">
                        <div class="text-xs text-gray-400 font-medium">Sinh viên thực hiện</div>
                        <div class="font-bold text-gray-900 text-base">Nguyễn Thị Thanh Trúc</div>
                        <div class="text-xs text-gray-500">Lớp 25CKDL • Khoa Toán - Tin</div>
                    </div>
                    <div class="w-10 h-10 rounded-full bg-slate-200 text-slate-700 font-bold flex items-center justify-center text-sm shadow-inner">
                        TT
                    </div>
                </div>
            </div>

            <!-- 4 THẺ THỐNG KÊ (STAT CARDS) -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <!-- Thẻ 1 -->
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col justify-between">
                    <div class="flex justify-between items-start">
                        <span class="text-xs font-bold text-gray-400 tracking-wider uppercase">Biên độ Max–Min cả năm</span>
                        <span class="p-2 bg-green-50 rounded-lg text-green-600"><i class="fa-solid fa-arrow-trend-up"></i></span>
                    </div>
                    <div class="mt-3">
                        <div class="text-2xl font-black text-gray-900">85.480,80 <span class="text-xs font-normal text-gray-400">VND</span></div>
                        <p class="text-xs text-gray-400 mt-1 flex items-center gap-1">
                            <i class="fa-solid fa-chart-simple text-gray-300"></i> Biên độ chênh lệch cực đại
                        </p>
                    </div>
                </div>

                <!-- Thẻ 2 -->
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col justify-between">
                    <div class="flex justify-between items-start">
                        <span class="text-xs font-bold text-gray-400 tracking-wider uppercase">Phiên đột biến mạnh nhất</span>
                        <span class="p-2 bg-red-50 rounded-lg text-red-500"><i class="fa-solid fa-bolt"></i></span>
                    </div>
                    <div class="mt-3">
                        <div class="text-2xl font-black text-gray-900">16.213,78 <span class="text-xs font-normal text-gray-400">VND</span></div>
                        <p class="text-xs text-gray-400 mt-1">Ghi nhận tại Phiên Ngày 297 (Quý 4)</p>
                    </div>
                </div>

                <!-- Thẻ 3 -->
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col justify-between">
                    <div class="flex justify-between items-start">
                        <span class="text-xs font-bold text-gray-400 tracking-wider uppercase">Tỷ lệ phiên bất thường</span>
                        <span class="p-2 bg-amber-50 rounded-lg text-amber-500"><i class="fa-solid fa-triangle-exclamation"></i></span>
                    </div>
                    <div class="mt-3">
                        <div class="text-2xl font-black text-amber-600">99.5%</div>
                        <p class="text-xs text-gray-400 mt-1">363 / 365 ngày vượt ngưỡng thường</p>
                    </div>
                </div>

                <!-- Thẻ 4 -->
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col justify-between">
                    <div class="flex justify-between items-start">
                        <span class="text-xs font-bold text-gray-400 tracking-wider uppercase">Đỉnh giá toàn năm</span>
                        <span class="p-2 bg-blue-50 rounded-lg text-blue-600"><i class="fa-solid fa-crown"></i></span>
                    </div>
                    <div class="mt-3">
                        <div class="text-2xl font-black text-gray-900">89.175,81 <span class="text-xs font-normal text-gray-400">VND</span></div>
                        <p class="text-xs text-gray-400 mt-1">Thiết lập kỷ lục trong Tháng 10</p>
                    </div>
                </div>
            </div>

            <!-- KHUNG VIDEO MÔ PHỎNG -->
            <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
                <div class="relative overflow-hidden rounded-xl bg-black aspect-video">
                    <video controls autoplay loop muted class="w-full h-full object-contain">
                        <source src="/static/mo_phong_chung_khoan.mp4" type="video/mp4">
                        Trình duyệt không hỗ trợ xem video.
                    </video>
                </div>
            </div>

        </div>
    </body>
    </html>
    """
    return html_content
            
           
