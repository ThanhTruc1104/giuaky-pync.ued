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
<html lang="vi" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo Cáo Phân Tích & Mô Phỏng Biến Động Giá Cổ Phiếu 365 Ngày</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Font Inter & Plus Jakarta Sans -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            50: '#f0f7ff',
                            100: '#e0effe',
                            500: '#0284c7',
                            600: '#0284c7',
                            700: '#0369a1',
                            900: '#0c4a6e',
                        },
                        stock: {
                            purple: '#a855f7', // Giá trần
                            cyan: '#06b6d4',   // Giá sàn
                            yellow: '#eab308', // Tham chiếu
                            green: '#22c55e',  // Tăng giá
                            red: '#ef4444'     // Giảm giá
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #f8fafc;
            color: #1e293b;
        }
        .card-shadow {
            box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.04), 0 8px 10px -6px rgba(15, 23, 42, 0.02);
        }
        .tab-active {
            background-color: #ffffff;
            color: #0284c7;
            box-shadow: 0 4px 12px -2px rgba(2, 132, 199, 0.12);
            border-bottom: 2px solid #0284c7;
        }
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
    </style>
</head>
<body class="h-full flex flex-col font-sans antialiased text-slate-800 bg-slate-50">

    <!-- Top Navigation Header -->
    <header class="bg-white/90 backdrop-blur-md sticky top-0 z-50 border-b border-slate-200/80">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <!-- Title & Department -->
                <div class="flex items-center space-x-4">
                    <div class="p-3 bg-sky-50 rounded-2xl border border-sky-100 text-sky-600 hidden sm:block">
                        <i class="fa-solid fa-chart-line text-2xl"></i>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-sky-100 text-sky-800">
                                Đồ Án Lập Trình Python Nâng Cao
                            </span>
                            <span class="text-xs text-slate-400">• Năm Học 2025 - 2026</span>
                        </div>
                        <h1 class="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight mt-0.5">
                            MÔ PHỎNG BIẾN ĐỘNG GIÁ CỔ PHIẾU TRONG 365 NGÀY
                        </h1>
                    </div>
                </div>

                <!-- Author / Instructor Info -->
                <div class="hidden lg:flex items-center space-x-6 border-l border-slate-200 pl-6">
                    <div class="text-right">
                        <p class="text-xs font-medium text-slate-500">Sinh viên thực hiện</p>
                        <p class="text-sm font-bold text-slate-900">Nguyễn Thị Thanh Trúc</p>
                        <p class="text-xs text-slate-500">Lớp 25CKDL • Khoa Toán - Tin</p>
                    </div>
                    <div class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center font-bold text-sky-600 border border-slate-200">
                        TT
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Sub-header Metadata Bar -->
    <section class="bg-white border-b border-slate-200/60 py-3">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div class="flex flex-wrap items-center gap-2">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-slate-100 text-slate-700 font-medium">
                    <i class="fa-solid fa-user-tie text-sky-600"></i> GVHD: <strong class="text-slate-900">Phan Trần Đức Minh</strong>
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-slate-100 text-slate-700 font-medium">
                    <i class="fa-solid fa-graduation-cap text-sky-600"></i> Ngành: <strong class="text-slate-900">Khoa học Dữ liệu</strong>
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-slate-100 text-slate-700 font-medium">
                    <i class="fa-solid fa-university text-sky-600"></i> Trường ĐH Sư phạm - ĐH Đà Nẵng
                </span>
            </div>
            <div class="flex items-center gap-2 text-slate-500">
                <i class="fa-regular fa-clock"></i> Chu kỳ phân tích: <strong>365 Phiên liên tiếp</strong>
            </div>
        </div>
    </section>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">

        <!-- 1. KEY METRICS CARDS OVERVIEW -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            <!-- Metric 1 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 card-shadow hover:border-sky-300 transition-all">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">Biên độ Max-Min Cả Năm</span>
                    <span class="p-2 bg-emerald-50 text-emerald-600 rounded-xl"><i class="fa-solid fa-arrow-trend-up"></i></span>
                </div>
                <div class="mt-3">
                    <div class="text-2xl font-extrabold text-slate-900">85.480,80 <span class="text-xs font-normal text-slate-500">VND</span></div>
                    <p class="text-xs text-emerald-600 font-medium mt-1 flex items-center gap-1">
                        <i class="fa-solid fa-chart-line"></i> Biên độ chênh lệch cực đại
                    </p>
                </div>
            </div>

            <!-- Metric 2 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 card-shadow hover:border-sky-300 transition-all">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">Phiên Đột Biến Mạnh Nhất</span>
                    <span class="p-2 bg-rose-50 text-rose-600 rounded-xl"><i class="fa-solid fa-bolt"></i></span>
                </div>
                <div class="mt-3">
                    <div class="text-2xl font-extrabold text-slate-900">16.213,78 <span class="text-xs font-normal text-slate-500">VND</span></div>
                    <p class="text-xs text-slate-500 font-medium mt-1">
                        Ghi nhận tại <strong class="text-slate-800">Phiên Ngày 297</strong> (Quý 4)
                    </p>
                </div>
            </div>

            <!-- Metric 3 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 card-shadow hover:border-sky-300 transition-all">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">Tỷ Lệ Phiên Bất Thường</span>
                    <span class="p-2 bg-amber-50 text-amber-600 rounded-xl"><i class="fa-solid fa-triangle-exclamation"></i></span>
                </div>
                <div class="mt-3">
                    <div class="text-2xl font-extrabold text-amber-600">99.5%</div>
                    <p class="text-xs text-slate-500 font-medium mt-1">
                        <strong class="text-slate-800">363 / 365 ngày</strong> vượt ngưỡng thường
                    </p>
                </div>
            </div>

            <!-- Metric 4 -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200/80 card-shadow hover:border-sky-300 transition-all">
                <div class="flex items-center justify-between">
                    <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">Đỉnh Giá Toàn Năm</span>
                    <span class="p-2 bg-sky-50 text-sky-600 rounded-xl"><i class="fa-solid fa-crown"></i></span>
                </div>
                <div class="mt-3">
                    <div class="text-2xl font-extrabold text-sky-700">89.175,81 <span class="text-xs font-normal text-slate-500">VND</span></div>
                    <p class="text-xs text-slate-500 font-medium mt-1">
                        Thiết lập kỷ lục trong <strong class="text-slate-800">Tháng 10</strong>
                    </p>
                </div>
            </div>
        </div>

        <!-- 2. NAVIGATION TABS -->
        <div class="bg-slate-200/70 p-1.5 rounded-2xl border border-slate-300/60 flex flex-wrap gap-1 sm:gap-2">
            <button onclick="switchTab('tab1')" id="btn-tab1" class="tab-btn flex-1 min-w-[140px] sm:min-w-0 py-3 px-4 rounded-xl text-xs sm:text-sm font-semibold text-slate-600 hover:text-slate-900 transition-all flex items-center justify-center gap-2 tab-active">
                <i class="fa-solid fa-play"></i> 1. Mô Phỏng & Quy Tắc
            </button>
            <button onclick="switchTab('tab2')" id="btn-tab2" class="tab-btn flex-1 min-w-[140px] sm:min-w-0 py-3 px-4 rounded-xl text-xs sm:text-sm font-semibold text-slate-600 hover:text-slate-900 transition-all flex items-center justify-center gap-2">
                <i class="fa-solid fa-chart-area"></i> 2. Diễn Biến Tháng/Quý
            </button>
            <button onclick="switchTab('tab3')" id="btn-tab3" class="tab-btn flex-1 min-w-[140px] sm:min-w-0 py-3 px-4 rounded-xl text-xs sm:text-sm font-semibold text-slate-600 hover:text-slate-900 transition-all flex items-center justify-center gap-2">
                <i class="fa-solid fa-chart-bar"></i> 3. Bất Thường & Phân Bố
            </button>
            <button onclick="switchTab('tab4')" id="btn-tab4" class="tab-btn flex-1 min-w-[140px] sm:min-w-0 py-3 px-4 rounded-xl text-xs sm:text-sm font-semibold text-slate-600 hover:text-slate-900 transition-all flex items-center justify-center gap-2">
                <i class="fa-solid fa-lightbulb"></i> 4. Hiện Tượng Kỹ Thuật
            </button>
            <button onclick="switchTab('tab5')" id="btn-tab5" class="tab-btn flex-1 min-w-[140px] sm:min-w-0 py-3 px-4 rounded-xl text-xs sm:text-sm font-semibold text-slate-600 hover:text-slate-900 transition-all flex items-center justify-center gap-2">
                <i class="fa-solid fa-flag-checkered"></i> 5. Kết Luận & Mở Rộng
            </button>
        </div>

        <!-- 3. TAB CONTENT SECTIONS -->

        <!-- TAB 1: MÔ PHỎNG & QUY TẮC GIAO DỊCH -->
        <!-- KHUNG MÔ PHỎNG HOẠT ẢNH (VIDEO) -->
        <div class="video-container">
            <video controls autoplay loop muted width="100%">
             <source src="mo_phong_chung_khoan.mp4" type="video/mp4">
              </video>
        </div>
        <!-- Quy tắc 5 màu Bảng Điện -->
                <div class="lg:col-span-4 bg-white p-6 rounded-2xl border border-slate-200 card-shadow flex flex-col justify-between">
                    <div>
                        <h3 class="text-base font-bold text-slate-900 border-b border-slate-100 pb-3 flex items-center gap-2">
                            <i class="fa-solid fa-palette text-amber-500"></i> Quy Tắc 5 Màu Chứng Khoán
                        </h3>
                        <p class="text-xs text-slate-500 mt-2 mb-4">Chuẩn màu bảng điện giao dịch chứng khoán áp dụng trong mô phỏng Python:</p>

                        <div class="space-y-3">
                            <div class="p-3 rounded-xl bg-purple-50 border border-purple-200 flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <span class="w-3.5 h-3.5 rounded-full bg-purple-600 ring-4 ring-purple-100"></span>
                                    <span class="text-xs font-bold text-purple-900">Giá Trần (Ceiling)</span>
                                </div>
                                <span class="text-xs font-semibold text-purple-700">+10% so với Tham chiếu</span>
                            </div>

                            <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <span class="w-3.5 h-3.5 rounded-full bg-emerald-500 ring-4 ring-emerald-100"></span>
                                    <span class="text-xs font-bold text-emerald-900">Tăng Giá (Increase)</span>
                                </div>
                                <span class="text-xs font-semibold text-emerald-700">Giá đóng > Tham chiếu</span>
                            </div>

                            <div class="p-3 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <span class="w-3.5 h-3.5 rounded-full bg-amber-500 ring-4 ring-amber-100"></span>
                                    <span class="text-xs font-bold text-amber-900">Tham Chiếu (Reference)</span>
                                </div>
                                <span class="text-xs font-semibold text-amber-700">Giá đóng ngày trước ($P_{ref}$)</span>
                            </div>

                            <div class="p-3 rounded-xl bg-rose-50 border border-rose-200 flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <span class="w-3.5 h-3.5 rounded-full bg-rose-500 ring-4 ring-rose-100"></span>
                                    <span class="text-xs font-bold text-rose-900">Giảm Giá (Decrease)</span>
                                </div>
                                <span class="text-xs font-semibold text-rose-700">Giá đóng < Tham chiếu</span>
                            </div>

                            <div class="p-3 rounded-xl bg-cyan-50 border border-cyan-200 flex items-center justify-between">
                                <div class="flex items-center space-x-3">
                                    <span class="w-3.5 h-3.5 rounded-full bg-cyan-500 ring-4 ring-cyan-100"></span>
                                    <span class="text-xs font-bold text-cyan-900">Giá Sàn (Floor)</span>
                                </div>
                                <span class="text-xs font-semibold text-cyan-700">-10% so với Tham chiếu</span>
                            </div>
                        </div>
                    </div>

                    <div class="mt-4 p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-600">
                        <i class="fa-solid fa-code text-sky-600 mr-1"></i> <strong>Xử lý Kỹ thuật:</strong> Sử dụng <code>LineCollection</code> trong Matplotlib để vẽ đồ thị đường đa sắc nối tiếp mượt mà.
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 2: PHÂN TÍCH DIỄN BIẾN THEO THÁNG & QUÝ -->
        <div id="tab2" class="tab-content hidden space-y-6">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <!-- Biểu đồ đường Giá trung bình 12 Tháng -->
                <div class="lg:col-span-7 bg-white p-6 rounded-2xl border border-slate-200 card-shadow">
                    <div class="flex items-center justify-between mb-4">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-chart-line text-sky-600"></i> Xu Hướng Giá Trung Bình 12 Tháng
                        </h3>
                        <span class="text-xs text-slate-500">Đơn vị: VND</span>
                    </div>
                    <div class="h-72">
                        <canvas id="monthlyAvgChart"></canvas>
                    </div>
                </div>

                <!-- Boxplot Biến Động Theo Tháng -->
                <div class="lg:col-span-5 bg-white p-6 rounded-2xl border border-slate-200 card-shadow">
                    <div class="flex items-center justify-between mb-4">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-box-archive text-indigo-600"></i> Biên Độ Biến Động Từng Tháng
                        </h3>
                        <span class="text-xs text-slate-500">Range Max-Min</span>
                    </div>
                    <div class="h-72">
                        <canvas id="monthlyRangeChart"></canvas>
                    </div>
                </div>
            </div>

            <!-- Bảng Thống kê Chi tiết 4 Quý -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 card-shadow">
                <div class="flex items-center justify-between mb-4">
                    <div>
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-table text-emerald-600"></i> Bảng Thống Kê Chi Tiết Diễn Biến 4 Quý (Quarterly Breakdown)
                        </h3>
                        <p class="text-xs text-slate-500 mt-0.5">So sánh tích lũy giai đoạn Q1 - Q2 vs sự bùng nổ biến động Q3 - Q4</p>
                    </div>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse text-xs sm:text-sm">
                        <thead>
                            <tr class="bg-slate-50 border-b border-slate-200 text-slate-600 uppercase font-bold tracking-wider">
                                <th class="p-3">Quý</th>
                                <th class="p-3">Giá Thấp Nhất (Min)</th>
                                <th class="p-3">Giá Cao Nhất (Max)</th>
                                <th class="p-3">Giá Trung Bình (Mean)</th>
                                <th class="p-3">Độ Lệch Chuẩn (Std)</th>
                                <th class="p-3">Biên Độ (Max - Min)</th>
                                <th class="p-3">Đánh Giá Xu Hướng</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            <tr class="hover:bg-slate-50/80 transition-all">
                                <td class="p-3 font-bold text-slate-900">Quý 1 (Ngày 1-90)</td>
                                <td class="p-3 font-mono text-slate-700">3.695,01</td>
                                <td class="p-3 font-mono text-slate-700">14.191,95</td>
                                <td class="p-3 font-mono font-semibold text-slate-900">7.882,40</td>
                                <td class="p-3 font-mono text-slate-600">2.415,10</td>
                                <td class="p-3 font-mono text-emerald-600 font-bold">10.496,94</td>
                                <td class="p-3"><span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800">Tích lũy & Đáy thấp</span></td>
                            </tr>
                            <tr class="hover:bg-slate-50/80 transition-all">
                                <td class="p-3 font-bold text-slate-900">Quý 2 (Ngày 91-181)</td>
                                <td class="p-3 font-mono text-slate-700">5.820,10</td>
                                <td class="p-3 font-mono text-slate-700">28.450,30</td>
                                <td class="p-3 font-mono font-semibold text-slate-900">16.340,20</td>
                                <td class="p-3 font-mono text-slate-600">5.890,40</td>
                                <td class="p-3 font-mono text-sky-600 font-bold">22.630,20</td>
                                <td class="p-3"><span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-sky-100 text-sky-800">Tăng trưởng ổn định</span></td>
                            </tr>
                            <tr class="hover:bg-slate-50/80 transition-all">
                                <td class="p-3 font-bold text-slate-900">Quý 3 (Ngày 182-273)</td>
                                <td class="p-3 font-mono text-slate-700">21.300,50</td>
                                <td class="p-3 font-mono text-slate-700">65.800,00</td>
                                <td class="p-3 font-mono font-semibold text-slate-900">42.150,80</td>
                                <td class="p-3 font-mono text-slate-600">12.340,10</td>
                                <td class="p-3 font-mono text-amber-600 font-bold">44.499,50</td>
                                <td class="p-3"><span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800">Bùng nổ biên độ</span></td>
                            </tr>
                            <tr class="hover:bg-slate-50/80 transition-all bg-sky-50/30">
                                <td class="p-3 font-bold text-slate-900">Quý 4 (Ngày 274-365)</td>
                                <td class="p-3 font-mono text-slate-700">45.200,00</td>
                                <td class="p-3 font-mono text-slate-700">89.175,81</td>
                                <td class="p-3 font-mono font-semibold text-slate-900">68.920,40</td>
                                <td class="p-3 font-mono text-slate-600">15.820,90</td>
                                <td class="p-3 font-mono text-rose-600 font-bold">43.975,81</td>
                                <td class="p-3"><span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-rose-100 text-rose-800">Đỉnh cao & Biến động cực đại</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- TAB 3: PHÂN TÍCH PHIÊN BẤT THƯỜNG & PHÂN BỐ GIÁ -->
        <div id="tab3" class="tab-content hidden space-y-6">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <!-- Tỷ lệ Phiên Bất Thường vs Bình Thường -->
                <div class="lg:col-span-5 bg-white p-6 rounded-2xl border border-slate-200 card-shadow">
                    <div class="flex items-center justify-between mb-4">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-pie-chart text-amber-500"></i> Tỷ Lệ Phiên Bất Thường (363 vs 2)
                        </h3>
                    </div>
                    <div class="h-64 flex items-center justify-center">
                        <canvas id="anomaliesPieChart"></canvas>
                    </div>
                    <div class="mt-4 p-3 bg-amber-50/60 rounded-xl border border-amber-200 text-xs text-amber-800">
                        <strong>Lưu ý:</strong> Ngưỡng bất thường được xác định khi biên độ chênh lệch trong phiên vượt quá 2 lần độ lệch chuẩn ($> 2\sigma$).
                    </div>
                </div>

                <!-- Histogram Phân Bố Giá Q1+Q2 vs Q3+Q4 -->
                <div class="lg:col-span-7 bg-white p-6 rounded-2xl border border-slate-200 card-shadow">
                    <div class="flex items-center justify-between mb-4">
                        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-chart-column text-sky-600"></i> Phân Bố Tần Suất Giá (Histogram: Q1+Q2 vs Q3+Q4)
                        </h3>
                    </div>
                    <div class="h-64">
                        <canvas id="priceDistributionChart"></canvas>
                    </div>
                </div>
            </div>

            <!-- Phân tích 3 Nhóm Phiên Bất Thường -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 card-shadow space-y-4">
                <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 border-b border-slate-100 pb-3">
                    <i class="fa-solid fa-magnifying-glass-chart text-rose-500"></i> Phân Loại 3 Nhóm Phiên Bất Thường Đặc Biệt
                </h3>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-rose-600 bg-rose-50 px-2 py-0.5 rounded border border-rose-200">Nhóm 1</span>
                            <i class="fa-solid fa-arrow-trend-down text-rose-500"></i>
                        </div>
                        <h4 class="font-bold text-slate-900 text-sm">Rút Chân / Sàn Tăng Trần</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Mở cửa giảm kịch sàn nhưng cuối phiên lực cầu bắt đáy cực đại đẩy giá lên chạm mức trần trong cùng một ngày.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-sky-600 bg-sky-50 px-2 py-0.5 rounded border border-sky-200">Nhóm 2</span>
                            <i class="fa-solid fa-arrows-up-down text-sky-500"></i>
                        </div>
                        <h4 class="font-bold text-slate-900 text-sm">Biên Độ Cực Đại Quý 4</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Xuất hiện các phiên biến động trên 15.000 VND/cổ phiếu tại vùng đỉnh (Tháng 10 - 11), tạo mô hình nến Doji chân dài.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-purple-600 bg-purple-50 px-2 py-0.5 rounded border border-purple-200">Nhóm 3</span>
                            <i class="fa-solid fa-chart-line text-purple-500"></i>
                        </div>
                        <h4 class="font-bold text-slate-900 text-sm">Chuỗi Tăng Kịch Trần Liên Tiếp</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Các phiên giá đóng cửa liên tục chạm trần tím trong giai đoạn chuyển giao giữa Quý 2 và Quý 3.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 4: GIẢI THÍCH HIỆN TƯỢNG KỸ THUẬT & KHUYẾN NGHỊ -->
        <div id="tab4" class="tab-content hidden space-y-6">
            <!-- Hiện tượng Kỹ thuật cốt lõi -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 card-shadow space-y-4">
                <div class="flex items-center space-x-3 border-b border-slate-100 pb-3">
                    <div class="p-2.5 bg-emerald-100 text-emerald-700 rounded-xl">
                        <i class="fa-solid fa-circle-question text-lg"></i>
                    </div>
                    <div>
                        <h3 class="text-base font-bold text-slate-900">Giải Thích Hiện Tượng Kỹ Thuật: "Đường Đi Xuống Vẫn Có Màu Xanh"</h3>
                        <p class="text-xs text-slate-500">Bản chất cơ chế so sánh Giá Tham Chiếu ($P_{ref}$) trong Quy Tắc Bảng Điện Chứng Khoán</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                        <h4 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-scale-balanced text-sky-600"></i> Cơ Chế So Sánh Chuẩn
                        </h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Trong đồ thị chứng khoán Việt Nam, màu sắc của nến/đường biểu diễn **KHÔNG** phụ thuộc vào việc đường giá đang dốc lên hay dốc xuống so với các phiên trước đó, mà phụ thuộc hoàn toàn vào:
                        </p>
                        <div class="p-3 bg-white rounded-lg border border-slate-200 font-mono text-xs space-y-1 text-slate-800">
                            <p>• Màu Xanh (Green): $P_{close}(t) > P_{ref}(t) = P_{close}(t-1)$</p>
                            <p>• Màu Đỏ (Red): $P_{close}(t) < P_{ref}(t) = P_{close}(t-1)$</p>
                        </div>
                    </div>

                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                        <h4 class="text-sm font-bold text-slate-900 flex items-center gap-2">
                            <i class="fa-solid fa-lightbulb text-amber-500"></i> Trường Hợp "Độ Dốc Âm Nhưng Màu Xanh"
                        </h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Nếu trong cùng một phiên $t$, giá mở cửa bị đạp xuống rất thấp (hoặc khoảng gáp giảm Gap Down), nhưng trong phiên giá hồi phục đóng cửa cao hơn mức tham chiếu $P_{ref}$, phiên đó vẫn được tô **MÀU XANH** dù đồ thị giá tổng thể trong chuỗi đang trong xu hướng giảm.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Khuyến nghị Đầu tư & Quản trị rủi ro -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 card-shadow space-y-4">
                <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 border-b border-slate-100 pb-3">
                    <i class="fa-solid fa-shield-halved text-sky-600"></i> Đánh Giá Rủi Ro & Khuyến Nghị Chiến Lược Stop-Loss Linh Hoạt
                </h3>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                    <div class="p-4 rounded-xl bg-amber-50/50 border border-amber-200 space-y-2">
                        <h4 class="text-xs font-bold text-amber-900 uppercase tracking-wider">Giai đoạn Quý 1 - Quý 2</h4>
                        <p class="text-sm font-bold text-slate-900">Chiến Lược Buy & Hold</p>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Biến động thấp, giá đi ngang tích lũy. Thích hợp cho nhà đầu tư gom cổ phiếu vùng giá thấp (3.000 - 15.000 VND).
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-sky-50/50 border border-sky-200 space-y-2">
                        <h4 class="text-xs font-bold text-sky-900 uppercase tracking-wider">Giai đoạn Quý 3 - Quý 4</h4>
                        <p class="text-sm font-bold text-slate-900">Stop-Loss Linh Hoạt (Trailing Stop)</p>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Khi biên độ ngày vượt 10.000 VND, áp dụng ngưỡng cắt lỗ động 5 - 7% từ đỉnh gần nhất để bảo vệ lợi nhuận.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-rose-50/50 border border-rose-200 space-y-2">
                        <h4 class="text-xs font-bold text-rose-900 uppercase tracking-wider">Cảnh Báo Rủi Ro</h4>
                        <p class="text-sm font-bold text-slate-900">Quản Lý Tỷ Lệ Margin</p>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            99.5% phiên biến động mạnh tiềm ẩn rủi ro múa bên bên bán (Call Margin) nếu nắm giữ tỷ trọng đòn bẩy cao ở vùng đỉnh Quý 4.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 5: KẾT LUẬN & HƯỚNG PHÁT TRIỂN -->
        <div id="tab5" class="tab-content hidden space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Đóng góp Kỹ thuật & Bài học -->
                <div class="bg-white p-6 rounded-2xl border border-slate-200 card-shadow space-y-4">
                    <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 border-b border-slate-100 pb-3">
                        <i class="fa-solid fa-square-check text-emerald-600"></i> Đóng Góp Kỹ Thuật Lập Trình Python
                    </h3>
                    <ul class="space-y-3 text-xs sm:text-sm text-slate-600">
                        <li class="flex items-start gap-2">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span>Xử lý và làm sạch dữ liệu chuỗi thời gian chứng khoán 365 ngày hiệu quả bằng <strong>Pandas & NumPy</strong>.</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span>Tối ưu hóa tốc độ dựng khung hình động với <strong>matplotlib.animation.FuncAnimation</strong>.</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span>Tùy biến tô màu đa sắc mượt mà cho chuỗi dữ liệu lớn bằng kỹ thuật <strong>LineCollection</strong>.</span>
                        </li>
                    </ul>
                </div>

                <!-- Hướng Mở Rộng Đồ Án -->
                <div class="bg-white p-6 rounded-2xl border border-slate-200 card-shadow space-y-4">
                    <h3 class="text-base font-bold text-slate-900 flex items-center gap-2 border-b border-slate-100 pb-3">
                        <i class="fa-solid fa-rocket text-sky-600"></i> Hướng Mở Rộng Đề Tài Trong Tương Lai
                    </h3>
                    <div class="space-y-3 text-xs sm:text-sm text-slate-600">
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex items-start gap-3">
                            <i class="fa-solid fa-chart-column text-sky-600 mt-1"></i>
                            <div>
                                <strong class="text-slate-900">Khối Lượng Giao Dịch (Volume):</strong> Tích hợp thêm biểu đồ cột Volume bên dưới để phân tích dòng tiền thông minh.
                            </div>
                        </div>
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex items-start gap-3">
                            <i class="fa-solid fa-sliders text-indigo-600 mt-1"></i>
                            <div>
                                <strong class="text-slate-900">Chỉ Báo Kỹ Thuật (RSI, MACD, Bollinger Bands):</strong> Tính toán các đường trung bình động MA20, MA50.
                            </div>
                        </div>
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex items-start gap-3">
                            <i class="fa-solid fa-brain text-purple-600 mt-1"></i>
                            <div>
                                <strong class="text-slate-900">Mô Hình AI Dự Đoán (LSTM / Facebook Prophet):</strong> Ứng dụng Học sâu (Deep Learning) để dự báo xu hướng giá 30 ngày tiếp theo.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200/80 py-6 mt-12">
        <div class="max-w-7xl mx-auto px-4 text-center text-xs text-slate-500 space-y-1">
            <p>© 2026 Báo Cáo Đồ Án Python Nâng Cao - Sinh viên Nguyễn Thị Thanh Trúc (Lớp 25CKDL)</p>
            <p>Khoa Toán - Tin | Trường Đại học Sư phạm - Đại học Đà Nẵng</p>
        </div>
    </footer>

    <!-- JavaScript Charts & Interaction Logic -->
    <script>
        // TAB SWITCHING LOGIC
        function switchTab(tabId) {
            // Hide all contents
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            // Remove active class from buttons
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('tab-active'));

            // Show selected tab
            document.getElementById(tabId).classList.remove('hidden');
            // Add active class to button
            document.getElementById('btn-' + tabId).classList.add('tab-active');
        }

        // SIMULATION CANVAS LOGIC
        let isSimulating = true;
        let simFrame = 0;
        const totalFrames = 365;
        const canvas = document.getElementById('simulationCanvas');
        const ctx = canvas.getContext('2d');

        function resizeCanvas() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = 380;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // Dummy simulation data generation
        const simData = [];
        let price = 8000;
        for(let i = 0; i < 365; i++) {
            let change = (Math.random() - 0.47) * (i > 180 ? 2200 : 600);
            price = Math.max(3000, price + change);
            let open = price - (Math.random() - 0.5) * 500;
            let high = Math.max(open, price) + Math.random() * 400;
            let low = Math.min(open, price) - Math.random() * 400;
            simData.push({ day: i + 1, close: price, open, high, low });
        }

        function drawSimulation() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw Grid
            ctx.strokeStyle = '#1e293b';
            ctx.lineWidth = 1;
            for(let x = 0; x < canvas.width; x += 60) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
            }
            for(let y = 0; y < canvas.height; y += 50) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
            }

            // Title inside canvas
            ctx.fillStyle = '#94a3b8';
            ctx.font = '12px Plus Jakarta Sans';
            ctx.fillText(`Khung 1: Biểu đồ nến Min-Max (Phiên ${simFrame + 1}/365)`, 20, 25);

            // Draw line graph
            const maxP = 95000;
            const minP = 2000;
            const h = canvas.height - 80;
            const w = canvas.width - 40;

            ctx.beginPath();
            for(let i = 0; i <= simFrame; i++) {
                let x = 20 + (i / 365) * w;
                let y = canvas.height - 40 - ((simData[i].close - minP) / (maxP - minP)) * h;
                
                if(i === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Draw Candlestick points
            for(let i = Math.max(0, simFrame - 30); i <= simFrame; i++) {
                let x = 20 + (i / 365) * w;
                let yClose = canvas.height - 40 - ((simData[i].close - minP) / (maxP - minP)) * h;
                let yOpen = canvas.height - 40 - ((simData[i].open - minP) / (maxP - minP)) * h;
                
                let isUp = simData[i].close >= simData[i].open;
                ctx.fillStyle = isUp ? '#22c55e' : '#ef4444';
                ctx.fillRect(x - 2, Math.min(yClose, yOpen), 4, Math.max(2, Math.abs(yClose - yOpen)));
            }

            // Update UI elements
            document.getElementById('simProgress').style.width = ((simFrame / totalFrames) * 100) + '%';
            document.getElementById('timeCounter').innerText = `Phiên: ${simFrame + 1} / 365`;

            if(isSimulating) {
                simFrame = (simFrame + 1) % totalFrames;
            }
        }

        let simInterval = setInterval(drawSimulation, 60);

        function toggleSimulation() {
            isSimulating = !isSimulating;
            const icon = document.getElementById('playIcon');
            icon.className = isSimulating ? 'fa-solid fa-pause text-sm' : 'fa-solid fa-play text-sm';
        }

        function resetSimulation() {
            simFrame = 0;
            if(!isSimulating) toggleSimulation();
        }

        // INIT CHART.JS CHARTS ON TAB LOAD
        window.onload = function() {
            // Chart 1: Monthly Average Price
            const ctx1 = document.getElementById('monthlyAvgChart').getContext('2d');
            new Chart(ctx1, {
                type: 'line',
                data: {
                    labels: ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12'],
                    datasets: [{
                        label: 'Giá trung bình (VND)',
                        data: [6500, 7200, 9800, 12400, 16800, 19800, 32000, 41000, 53500, 78900, 71200, 68500],
                        borderColor: '#0284c7',
                        backgroundColor: 'rgba(2, 132, 199, 0.08)',
                        fill: true,
                        tension: 0.3,
                        borderWidth: 3,
                        pointBackgroundColor: '#0284c7'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        y: { grid: { color: '#f1f5f9' } },
                        x: { grid: { display: false } }
                    }
                }
            });

            // Chart 2: Monthly Range Chart
            const ctx2 = document.getElementById('monthlyRangeChart').getContext('2d');
            new Chart(ctx2, {
                type: 'bar',
                data: {
                    labels: ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12'],
                    datasets: [{
                        label: 'Biên độ (VND)',
                        data: [4200, 5100, 7800, 9200, 11500, 14200, 21000, 28000, 34500, 43975, 38200, 31000],
                        backgroundColor: '#6366f1',
                        borderRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        y: { grid: { color: '#f1f5f9' } },
                        x: { grid: { display: false } }
                    }
                }
            });

            // Chart 3: Anomalies Pie Chart
            const ctx3 = document.getElementById('anomaliesPieChart').getContext('2d');
            new Chart(ctx3, {
                type: 'doughnut',
                data: {
                    labels: ['Phiên Bất Thường (>2σ)', 'Phiên Bình Thường'],
                    datasets: [{
                        data: [363, 2],
                        backgroundColor: ['#f59e0b', '#e2e8f0'],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom' }
                    }
                }
            });

            // Chart 4: Price Distribution Histogram
            const ctx4 = document.getElementById('priceDistributionChart').getContext('2d');
            new Chart(ctx4, {
                type: 'bar',
                data: {
                    labels: ['0-15k', '15k-30k', '30k-45k', '45k-60k', '60k-75k', '75k-90k'],
                    datasets: [
                        {
                            label: 'Quý 1 + Quý 2',
                            data: [120, 61, 0, 0, 0, 0],
                            backgroundColor: '#38bdf8'
                            },
                        {
                            label: 'Quý 3 + Quý 4',
                            data: [0, 15, 45, 52, 42, 30],
                            backgroundColor: '#f43f5e'
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        x: { stacked: true, grid: { display: false } },
                        y: { stacked: true, grid: { color: '#f1f5f9' } }
                    }
                }
            });
        };
    </script>
</body>
</html>

    """
  return html_content
