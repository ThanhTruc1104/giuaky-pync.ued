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
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col justify-between hover:shadow-md transition-shadow">
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
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col justify-between hover:shadow-md transition-shadow">
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
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col justify-between hover:shadow-md transition-shadow">
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
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex flex-col justify-between hover:shadow-md transition-shadow">
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

            <!-- THANH MENU ĐIỀU HƯỚNG BẤM ĐƯỢC VÀ CÓ HIỆU ỨNG HOVER -->
            <div class="flex flex-wrap gap-3 py-2 overflow-x-auto">
                <!-- Mục 1: Đang chọn (Active) -->
                <button class="cursor-pointer flex items-center gap-2 bg-slate-300 text-gray-900 font-bold px-4 py-2.5 rounded-xl text-sm border border-gray-400 shadow-md hover:bg-slate-400 hover:shadow-lg hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-play text-gray-800 text-xs"></i>
                    <span>1. Mô Phỏng & Quy Tắc</span>
                </button>

                <!-- Mục 2 -->
                <button class="cursor-pointer flex items-center gap-2 bg-white text-gray-700 font-medium px-4 py-2.5 rounded-xl text-sm border border-gray-200 shadow-sm hover:bg-slate-100 hover:text-gray-900 hover:border-gray-300 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-chart-column text-gray-400 text-xs"></i>
                    <span>2. Diễn Biến Tháng/Quý</span>
                </button>

                <!-- Mục 3 -->
                <button class="cursor-pointer flex items-center gap-2 bg-white text-gray-700 font-medium px-4 py-2.5 rounded-xl text-sm border border-gray-200 shadow-sm hover:bg-slate-100 hover:text-gray-900 hover:border-gray-300 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-bars-staggered text-gray-400 text-xs"></i>
                    <span>3. Bất Thường & Phân Bố</span>
                </button>

                <!-- Mục 4 -->
                <button class="cursor-pointer flex items-center gap-2 bg-white text-gray-700 font-medium px-4 py-2.5 rounded-xl text-sm border border-gray-200 shadow-sm hover:bg-slate-100 hover:text-gray-900 hover:border-gray-300 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-regular fa-lightbulb text-gray-400 text-xs"></i>
                    <span>4. Hiện Tượng Kỹ Thuật</span>
                </button>

                <!-- Mục 5 -->
                <button class="cursor-pointer flex items-center gap-2 bg-white text-gray-700 font-medium px-4 py-2.5 rounded-xl text-sm border border-gray-200 shadow-sm hover:bg-slate-100 hover:text-gray-900 hover:border-gray-300 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-regular fa-newspaper text-gray-400 text-xs"></i>
                    <span>5. Kết Luận & Mở Rộng</span>
                </button>
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

            <!-- KHỐI QUY TẮC 5 MÀU CHỨNG KHOÁN -->
            <div class="bg-white/80 backdrop-blur rounded-2xl p-6 shadow-sm border border-gray-100 space-y-4">
                <div class="space-y-1">
                    <h2 class="text-lg font-bold text-gray-900 flex items-center gap-2">
                        <span class="text-amber-500">🎨</span> Quy Tắc 5 Màu Chứng Khoán
                    </h2>
                    <p class="text-xs text-gray-500">
                        Chuẩn màu bảng điện giao dịch chứng khoán áp dụng trong mô phỏng Python:
                    </p>
                </div>

                <div class="space-y-2">
                    <!-- Giá Trần -->
                    <div class="flex justify-between items-center bg-purple-50/60 p-3.5 rounded-xl border border-purple-100/50 hover:bg-purple-100/80 transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="w-3.5 h-3.5 rounded-full bg-purple-600 inline-block shadow-sm"></span>
                            <span class="font-semibold text-sm text-gray-800">Giá Trần (Ceiling)</span>
                        </div>
                        <span class="text-xs font-semibold text-purple-700">+10% so với Tham chiếu</span>
                    </div>

                    <!-- Tăng Giá -->
                    <div class="flex justify-between items-center bg-emerald-50/60 p-3.5 rounded-xl border border-emerald-100/50 hover:bg-emerald-100/80 transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="w-3.5 h-3.5 rounded-full bg-emerald-500 inline-block shadow-sm"></span>
                            <span class="font-semibold text-sm text-gray-800">Tăng Giá (Increase)</span>
                        </div>
                        <span class="text-xs font-semibold text-emerald-700">Giá đóng > Tham chiếu</span>
                    </div>

                    <!-- Tham Chiếu -->
                    <div class="flex justify-between items-center bg-amber-50/60 p-3.5 rounded-xl border border-amber-100/50 hover:bg-amber-100/80 transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="w-3.5 h-3.5 rounded-full bg-amber-500 inline-block shadow-sm"></span>
                            <span class="font-semibold text-sm text-gray-800">Tham Chiếu (Reference)</span>
                        </div>
                        <span class="text-xs font-semibold text-amber-700">Giá đóng ngày trước ($P_{ref}$)</span>
                    </div>

                    <!-- Giảm Giá -->
                    <div class="flex justify-between items-center bg-rose-50/60 p-3.5 rounded-xl border border-rose-100/50 hover:bg-rose-100/80 transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="w-3.5 h-3.5 rounded-full bg-rose-500 inline-block shadow-sm"></span>
                            <span class="font-semibold text-sm text-gray-800">Giảm Giá (Decrease)</span>
                        </div>
                        <span class="text-xs font-semibold text-rose-700">Giá đóng < Tham chiếu</span>
                    </div>

                    <!-- Giá Sàn -->
                    <div class="flex justify-between items-center bg-cyan-50/60 p-3.5 rounded-xl border border-cyan-100/50 hover:bg-cyan-100/80 transition-colors">
                        <div class="flex items-center gap-3">
                            <span class="w-3.5 h-3.5 rounded-full bg-cyan-500 inline-block shadow-sm"></span>
                            <span class="font-semibold text-sm text-gray-800">Giá Sàn (Floor)</span>
                        </div>
                        <span class="text-xs font-semibold text-cyan-700">-10% so với Tham chiếu</span>
                    </div>
                </div>

                <!-- Xử Lý Kỹ Thuật -->
                <div class="pt-2 text-xs text-gray-500 flex items-center gap-2">
                    <span class="font-mono bg-gray-100 px-1.5 py-0.5 rounded text-gray-700 font-semibold">&lt;/&gt; Xử lý Kỹ thuật:</span>
                    <span>Sử dụng LineCollection trong Matplotlib để vẽ đồ thị đường đa sắc nối tiếp mượt mà.</span>
                </div>
            </div>

        </div>
    </body>
    </html>
    """
    return html_content
