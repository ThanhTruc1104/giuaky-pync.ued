from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Mô phỏng Chứng khoán 365 Ngày - FastAPI trên Render")

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
async def main_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="vi" class="h-full scroll-smooth">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Báo cáo phân tích & Mô phỏng biến động giá cổ phiếu 365 ngày</title>
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
                        <span>Đồ án "Lập trình Python nâng cao"</span>
                        <span>•</span>
                        <span>Năm học 2026 – 2027</span>
                    </div>
                    <h1 class="text-2xl md:text-3xl font-extrabold text-gray-900 tracking-tight">
                        MÔ PHỎNG BIẾN ĐỘNG GIÁ CỔ PHIẾU TRONG 365 NGÀY
                    </h1>
                    <div class="flex flex-wrap items-center gap-4 text-xs md:text-sm text-gray-600 mt-3">
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-user-tie text-gray-400"></i> GVHD: <b>Phan Trần Đức Minh</b></span>
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-graduation-cap text-gray-400"></i> Ngành: <b>Khoa học dữ liệu</b></span>
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-building-columns text-gray-400"></i> <b>Trường Đại học Sư phạm - Đại học Đà Nẵng</b></span>
                    </div>
                </div>

                <div class="flex items-center gap-3 border-t md:border-t-0 md:border-l border-gray-200 pt-3 md:pt-0 md:pl-6">
                    <div class="text-right">
                        <div class="text-xs text-gray-400 font-medium">Sinh viên thực hiện</div>
                        <div class="font-bold text-gray-900 text-base">Nguyễn Thị Thanh Trúc</div>
                        <div class="text-xs text-gray-500">Lớp 25CKDL • Khoa: Toán - Tin</div>
                    </div>
                    <img src="/static/avatar.jpg" alt="Avatar" class="w-10 h-10 rounded-full object-cover border border-gray-200 shadow-sm" />
                </div>
            </div>

            <!-- 4 THẺ THỐNG KÊ (STAT CARDS) -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
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

            <!-- THANH MENU ĐIỀU HƯỚNG TỰ ĐỘNG CUỘN (ĐÃ ĐỒNG BỘ MÀU SẮC THEO TỪNG BIỂU TƯỢNG) -->
            <div class="flex flex-wrap gap-3 py-2 overflow-x-auto sticky top-4 z-50 bg-gray-100/90 backdrop-blur p-2 rounded-2xl shadow-sm">
                <!-- Nút 1: Chủ đề màu đỏ -->
                <a href="#section-1" class="cursor-pointer flex items-center gap-2 bg-red-50 text-red-800 font-bold px-4 py-2.5 rounded-xl text-sm border-2 border-red-300 shadow-sm hover:bg-red-100 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-play text-red-600 text-xs"></i>
                    <span>1. MÔ PHỎNG & QUY TẮC</span>
                </a>

                <!-- Nút 2: Chủ đề màu xanh dương -->
                <a href="#section-2" class="cursor-pointer flex items-center gap-2 bg-blue-50 text-blue-800 font-bold px-4 py-2.5 rounded-xl text-sm border-2 border-blue-300 shadow-sm hover:bg-blue-100 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-chart-column text-blue-600 text-xs"></i>
                    <span>2. DIỄN BIẾN THÁNG/QUÝ</span>
                </a>

                <!-- Nút 3: Chủ đề màu vàng cam (Amber) -->
                <a href="#section-3" class="cursor-pointer flex items-center gap-2 bg-amber-50 text-amber-800 font-bold px-4 py-2.5 rounded-xl text-sm border-2 border-amber-300 shadow-sm hover:bg-amber-100 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-bars-staggered text-amber-600 text-xs"></i>
                    <span>3. BẤT THƯỜNG & PHÂN BỐ</span>
                </a>

                <!-- Nút 4: Chủ đề màu tím -->
                <a href="#section-4" class="cursor-pointer flex items-center gap-2 bg-purple-50 text-purple-800 font-bold px-4 py-2.5 rounded-xl text-sm border-2 border-purple-300 shadow-sm hover:bg-purple-100 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-regular fa-lightbulb text-purple-600 text-xs"></i>
                    <span>4. HIỆN TƯỢNG ĐỒ THỊ</span>
                </a>

                <!-- Nút 5: Chủ đề màu xanh ngọc/lục (Emerald) -->
                <a href="#section-5" class="cursor-pointer flex items-center gap-2 bg-emerald-50 text-emerald-800 font-bold px-4 py-2.5 rounded-xl text-sm border-2 border-emerald-300 shadow-sm hover:bg-emerald-100 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-regular fa-newspaper text-emerald-600 text-xs"></i>
                    <span>5. KẾT LUẬN & MỞ RỘNG </span>
                </a>
            </div>
           
            <!-- PHẦN 1: MÔ PHỎNG & QUY TẮC -->
            <div id="section-1" class="space-y-6 pt-2">
                <!-- Tiêu đề mục 1 đồng bộ phong cách với các mục khác -->
                <div class="flex items-center gap-3">
                    <span class="p-2.5 bg-red-100 text-red-700 rounded-xl font-bold"><i class="fa-solid fa-play"></i></span>
                    <div>
                        <h2 class="text-xl font-bold text-gray-900">1. Mô phỏng & Quy tắc</h2>
                        <p class="text-xs text-gray-500">Mô phỏng trực quan hóa chuỗi thời gian và quy tắc phối màu chuẩn chứng khoán</p>
                    </div>
                </div>
            <!-- KHỐI GIẢI THÍCH LẬP TRÌNH TRƯỚC KHI CHẠY VIDEO -->
                <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100 space-y-4">
                    <div class="border-b border-gray-100 pb-3">
                        <h2 class="text-lg font-extrabold text-gray-900 flex items-center gap-2">
                            <i class="fa-solid fa-code text-blue-600"></i>
                            Giải thích kỹ thuật lập trình hoạt ảnh và xuất video mô phỏng
                        </h2>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm text-gray-700 leading-relaxed">
                        <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2">
                            <h3 class="font-bold text-gray-900 flex items-center gap-1.5">
                                <i class="fa-solid fa-list-check text-blue-600"></i> Xác định chuỗi & Cấu hình khung hình
                            </h3>
                            <p>• Định nghĩa tập hợp các khung hình cần thực thi (frames_to_run) bao gồm toàn bộ 365 ngày giao dịch trong năm (từ mốc 0 đến 364, ứng với mỗi khung hình đại diện cho 1 ngày giao dịch).</p>
                            <p>• Sử dụng lớp "animation.FuncAnimation" để liên kết đối tượng khung hình (fig) với hàm cập nhật dữ liệu (update). Thiết lập khoảng thời gian (interval = 165 ms) để đồ thị hiển thị trực tiếp (preview) với thời lượng hoàn chỉnh xấp xỉ 60 giây.</p>
                        </div>

                        <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2">
                            <h3 class="font-bold text-gray-900 flex items-center gap-1.5">
                                <i class="fa-solid fa-video text-emerald-600"></i> Trình ghi hình và mã hóa video
                            </h3>
                            <p>• Thiết lập tốc độ khung hình `fps = 6`, giúp tệp video MP4 đầu ra đạt thời lượng chính xác khoảng 60.8 giây (365 chia cho 6).</p>
                            <p>• Sử dụng "FFMpegWriter" với băng thông (bitrate = 8000) kết hợp tham số nén cao cấp của chuẩn H.264 (-crf 18) nhằm đảm bảo chất lượng hình ảnh sắc nét gần như nguyên bản (gần như không mất dữ liệu) ở độ phân giải 300 DPI.</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-2xl p-4 shadow-sm border border-gray-100">
                    <div class="relative overflow-hidden rounded-xl bg-black aspect-video">
                        <video controls autoplay loop muted class="w-full h-full object-contain">
                            <source src="/static/mo_phong_chung_khoan.mp4" type="video/mp4">
                            Trình duyệt không hỗ trợ xem video.
                        </video>
                    </div>
                </div>

                <div class="bg-white/80 backdrop-blur rounded-2xl p-6 shadow-sm border border-gray-100 space-y-4">
                    <div class="space-y-1">
                        <h2 class="text-lg font-bold text-gray-900 flex items-center gap-2">
                            <span class="text-amber-500">🎨</span> Quy tắc 5 màu chứng khoán
                        </h2>
                        <p class="text-xs text-gray-500">
                            Chuẩn màu bảng điện giao dịch chứng khoán áp dụng trong mô phỏng Python:
                        </p>
                    </div>

                    <div class="space-y-2">
                        <div class="flex justify-between items-center bg-purple-50/60 p-3.5 rounded-xl border border-purple-100/50 hover:bg-purple-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-purple-600 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Giá Trần</span>
                            </div>
                            <span class="text-xs font-semibold text-purple-700">+10% so với Tham chiếu</span>
                        </div>

                        <div class="flex justify-between items-center bg-emerald-50/60 p-3.5 rounded-xl border border-emerald-100/50 hover:bg-emerald-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-emerald-500 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Tăng Giá</span>
                            </div>
                            <span class="text-xs font-semibold text-emerald-700">Giá đóng > Tham chiếu</span>
                        </div>

                        <div class="flex justify-between items-center bg-amber-50/60 p-3.5 rounded-xl border border-amber-100/50 hover:bg-amber-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-amber-500 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Tham Chiếu</span>
                            </div>
                            <span class="text-xs font-semibold text-amber-700">Giá đóng ngày trước</span>
                        </div>

                        <div class="flex justify-between items-center bg-rose-50/60 p-3.5 rounded-xl border border-rose-100/50 hover:bg-rose-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-rose-500 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Giảm Giá</span>
                            </div>
                            <span class="text-xs font-semibold text-rose-700">Giá đóng < Tham chiếu</span>
                        </div>

                        <div class="flex justify-between items-center bg-cyan-50/60 p-3.5 rounded-xl border border-cyan-100/50 hover:bg-cyan-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-cyan-500 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Giá Sàn</span>
                            </div>
                            <span class="text-xs font-semibold text-cyan-700">-10% so với Tham chiếu</span>
                        </div>
                    </div>

                    <div class="pt-2 text-xs text-gray-500 flex items-center gap-2">
                        <span class="font-mono bg-gray-100 px-1.5 py-0.5 rounded text-gray-700 font-semibold">&lt;/&gt; Xử lý Kỹ thuật:</span>
                        <span>Sử dụng LineCollection trong Matplotlib để vẽ đồ thị đường đa sắc nối tiếp mượt mà.</span>
                    </div>
                </div>
            </div>

            <!-- PHẦN 2: DIỄN BIẾN THÁNG/QUÝ -->
            <div id="section-2" class="space-y-6 pt-6 border-t border-gray-200">
                <div class="flex items-center gap-3">
                    <span class="p-2.5 bg-blue-100 text-blue-700 rounded-xl font-bold"><i class="fa-solid fa-chart-column"></i></span>
                    <div>
                        <h2 class="text-xl font-bold text-gray-900">2. Diễn biến tháng/quý</h2>
                        <p class="text-xs text-gray-500">Phân tích xu hướng trung bình, độ biến động và phân bố giá theo thời gian</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    <!-- Biểu đồ 1 -->
                    <div class="bg-black rounded-2xl p-4 shadow-md border border-gray-800 flex flex-col justify-between space-y-3">
                        <h3 class="text-center font-bold text-white text-sm md:text-base">
                            Giá trung bình mã cổ phiếu theo tháng
                        </h3>
                        <div class="w-full flex justify-center">
                            <svg viewBox="0 0 500 300" class="w-full h-auto text-sky-400 font-sans">
                                <line x1="50" y1="30" x2="480" y2="30" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="34" fill="#fff" font-size="10" text-anchor="end">50000</text>
                                <line x1="50" y1="80" x2="480" y2="80" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="84" fill="#fff" font-size="10" text-anchor="end">40000</text>
                                <line x1="50" y1="130" x2="480" y2="130" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="134" fill="#fff" font-size="10" text-anchor="end">30000</text>
                                <line x1="50" y1="180" x2="480" y2="180" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="184" fill="#fff" font-size="10" text-anchor="end">20000</text>
                                <line x1="50" y1="230" x2="480" y2="230" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="234" fill="#fff" font-size="10" text-anchor="end">10000</text>
                                <line x1="50" y1="260" x2="480" y2="260" stroke="#fff" stroke-width="1"/>
                                <text x="42" y="264" fill="#fff" font-size="10" text-anchor="end">0</text>

                                <g fill="#87ceeb">
                                    <rect x="60" y="200" width="26" height="60" rx="1"/>
                                    <rect x="95" y="218" width="26" height="42" rx="1"/>
                                    <rect x="130" y="225" width="26" height="35" rx="1"/>
                                    <rect x="165" y="222" width="26" height="38" rx="1"/>
                                    <rect x="200" y="222" width="26" height="38" rx="1"/>
                                    <rect x="235" y="213" width="26" height="47" rx="1"/>
                                    <rect x="270" y="212" width="26" height="48" rx="1"/>
                                    <rect x="305" y="138" width="26" height="122" rx="1"/>
                                    <rect x="340" y="70" width="26" height="190" rx="1"/>
                                    <rect x="375" y="26" width="26" height="234" rx="1"/>
                                    <rect x="410" y="55" width="26" height="205" rx="1"/>
                                    <rect x="445" y="88" width="26" height="172" rx="1"/>
                                </g>

                                <g fill="#fff" font-size="9" text-anchor="end">
                                    <text x="73" y="275" transform="rotate(-45 73 275)">T1</text>
                                    <text x="108" y="275" transform="rotate(-45 108 275)">T2</text>
                                    <text x="143" y="275" transform="rotate(-45 143 275)">T3</text>
                                    <text x="178" y="275" transform="rotate(-45 178 275)">T4</text>
                                    <text x="213" y="275" transform="rotate(-45 213 275)">T5</text>
                                    <text x="248" y="275" transform="rotate(-45 248 275)">T6</text>
                                    <text x="283" y="275" transform="rotate(-45 283 275)">T7</text>
                                    <text x="318" y="275" transform="rotate(-45 318 275)">T8</text>
                                    <text x="353" y="275" transform="rotate(-45 353 275)">T9</text>
                                    <text x="388" y="275" transform="rotate(-45 388 275)">T10</text>
                                    <text x="423" y="275" transform="rotate(-45 423 275)">T11</text>
                                    <text x="458" y="275" transform="rotate(-45 458 275)">T12</text>
                                </g>
                            </svg>
                        </div>
                        <div class="bg-gray-900/90 p-3 rounded-xl border border-gray-800 text-xs text-gray-300 leading-relaxed space-y-1">
                            <p class="font-semibold text-sky-400 flex items-center gap-1.5">
                                <i class="fa-solid fa-circle-info"></i> Xu hướng giá:
                            </p>
                            <p>• <b>Tích lũy (T1–T7):</b> Giá đi ngang dưới 10k VNĐ.</p>
                            <p>• <b>Bùng nổ (T8–T10):</b> Tăng phi mã, đỉnh T10 >50k VNĐ.</p>
                            <p>• <b>Điều chỉnh (T11–T12):</b> Giảm dần về ~33k VNĐ.</p>
                        </div>
                    </div>

                    <!-- Biểu đồ 2: BOXPLOT CHUẨN MẪU GỐC -->
                    <div class="bg-black rounded-2xl p-4 shadow-md border border-gray-800 flex flex-col justify-between space-y-3">
                        <h3 class="text-center font-bold text-white text-sm md:text-base">
                            Biến động giá mỗi tháng
                        </h3>
                        <div class="w-full flex justify-center">
                            <svg viewBox="0 0 500 300" class="w-full h-auto font-sans">
                                <line x1="50" y1="20" x2="480" y2="20" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="24" fill="#fff" font-size="9" text-anchor="end">80000</text>
                                <line x1="50" y1="80" x2="480" y2="80" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="84" fill="#fff" font-size="9" text-anchor="end">60000</text>
                                <line x1="50" y1="140" x2="480" y2="140" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="144" fill="#fff" font-size="9" text-anchor="end">40000</text>
                                <line x1="50" y1="200" x2="480" y2="200" stroke="#444" stroke-dasharray="3,3"/>
                                <text x="42" y="204" fill="#fff" font-size="9" text-anchor="end">20000</text>
                                <line x1="50" y1="260" x2="480" y2="260" stroke="#fff" stroke-width="1"/>
                                <text x="42" y="264" fill="#fff" font-size="9" text-anchor="end">0</text>

                                <g stroke="#fff" stroke-width="0.8">
                                    <line x1="68" y1="220" x2="68" y2="240"/><line x1="61" y1="240" x2="75" y2="240"/>
                                    <line x1="103" y1="222" x2="103" y2="248"/><line x1="96" y1="248" x2="110" y2="248"/>
                                    <line x1="138" y1="233" x2="138" y2="249"/><line x1="131" y1="249" x2="145" y2="249"/>
                                    <line x1="173" y1="231" x2="173" y2="247"/><line x1="166" y1="247" x2="180" y2="247"/>
                                    <line x1="208" y1="230" x2="208" y2="247"/><line x1="201" y1="247" x2="215" y2="247"/>
                                    <line x1="243" y1="227" x2="243" y2="244"/><line x1="236" y1="244" x2="250" y2="244"/>
                                    <line x1="278" y1="225" x2="278" y2="243"/><line x1="271" y1="243" x2="285" y2="243"/>
                                    <line x1="313" y1="137" x2="313" y2="222"/><line x1="306" y1="137" x2="320" y2="137"/><line x1="306" y1="222" x2="320" y2="222"/>
                                    <line x1="348" y1="120" x2="348" y2="177"/><line x1="341" y1="120" x2="355" y2="120"/><line x1="341" y1="177" x2="355" y2="177"/>
                                    <line x1="383" y1="10" x2="383" y2="177"/><line x1="376" y1="10" x2="390" y2="10"/><line x1="376" y1="177" x2="390" y2="177"/>
                                    <line x1="418" y1="77" x2="418" y2="162"/><line x1="411" y1="77" x2="425" y2="77"/><line x1="411" y1="162" x2="425" y2="162"/>
                                    <line x1="453" y1="110" x2="453" y2="200"/><line x1="446" y1="110" x2="460" y2="110"/><line x1="446" y1="200" x2="460" y2="200"/>
                                </g>

                                <g stroke="#fff" fill="#8edac8" stroke-width="0.8">
                                    <rect x="58" y="225" width="20" height="8"/>
                                    <rect x="93" y="233" width="20" height="9"/>
                                    <rect x="128" y="238" width="20" height="7"/>
                                    <rect x="163" y="236" width="20" height="6"/>
                                    <rect x="198" y="236" width="20" height="6"/>
                                    <rect x="233" y="233" width="20" height="6"/>
                                    <rect x="268" y="233" width="20" height="7"/>
                                    <rect x="303" y="173" width="20" height="34"/>
                                    <rect x="338" y="142" width="20" height="18"/>
                                    <rect x="373" y="73" width="20" height="74"/>
                                    <rect x="408" y="117" width="20" height="27"/>
                                    <rect x="443" y="146" width="20" height="27"/>
                                </g>

                                <g stroke="#ffffb3" stroke-width="1.2">
                                    <line x1="58" y1="229" x2="78" y2="229"/>
                                    <line x1="93" y1="237" x2="113" y2="237"/>
                                    <line x1="128" y1="241" x2="148" y2="241"/>
                                    <line x1="163" y1="239" x2="183" y2="239"/>
                                    <line x1="198" y1="239" x2="218" y2="239"/>
                                    <line x1="233" y1="236" x2="253" y2="236"/>
                                    <line x1="268" y1="236" x2="288" y2="236"/>
                                    <line x1="303" y1="196" x2="323" y2="196"/>
                                    <line x1="338" y1="150" x2="358" y2="150"/>
                                    <line x1="373" y1="114" x2="393" y2="114"/>
                                    <line x1="408" y1="125" x2="428" y2="125"/>
                                    <line x1="443" y1="160" x2="463" y2="160"/>
                                </g>

                                <g fill="none" stroke="#fff" stroke-width="0.9">
                                    <circle cx="68" cy="218" r="2.2"/>
                                    <circle cx="243" cy="224" r="2.2"/>
                                    <circle cx="278" cy="218" r="2.2"/><circle cx="278" cy="221" r="2.2"/>
                                    <circle cx="348" cy="113" r="2.2"/>
                                </g>

                                <g fill="#fff" font-size="9" text-anchor="middle">
                                    <text x="68" y="275">T1</text><text x="103" y="275">T2</text>
                                    <text x="138" y="275">T3</text><text x="173" y="275">T4</text>
                                    <text x="208" y="275">T5</text><text x="243" y="275">T6</text>
                                    <text x="278" y="275">T7</text><text x="313" y="275">T8</text>
                                    <text x="348" y="275">T9</text><text x="383" y="275">T10</text>
                                    <text x="418" y="275">T11</text><text x="453" y="275">T12</text>
                                </g>
                            </svg>
                        </div>
                        <div class="bg-gray-900/90 p-3 rounded-xl border border-gray-800 text-xs text-gray-300 leading-relaxed space-y-1">
                            <p class="font-semibold text-teal-300 flex items-center gap-1.5">
                                <i class="fa-solid fa-chart-line"></i> Độ biến động giá:
                            </p>
                            <p>• <b>T1–T7:</b> Thân hộp hẹp dưới 10k, rủi ro biến động rất thấp.</p>
                            <p>• <b>T10:</b> Hộp dài nhất (28k–89k VNĐ), râu cao vượt 89k VNĐ.</p>
                            <p>• Các điểm tròn nhỏ đại diện cho phiên ngoại lệ.</p>
                        </div>
                    </div>
                </div>

                <!-- PHÂN BỐ GIÁ QUÝ GỐC -->
                <div class="bg-black rounded-2xl p-5 shadow-md border border-gray-800 space-y-4">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="space-y-2">
                            <h4 class="text-center font-bold text-white text-sm md:text-base">
                                Phân bố giá 2 quý đầu năm (Q1 + Q2) 
                            </h4>
                            <div class="w-full flex justify-center">
                                <svg viewBox="0 0 500 300" class="w-full h-auto">
                                    <line x1="50" y1="40" x2="470" y2="40" stroke="#333" stroke-dasharray="3,3"/>
                                    <text x="42" y="44" fill="#fff" font-size="10" text-anchor="end">120</text>
                                    <line x1="50" y1="95" x2="470" y2="95" stroke="#333" stroke-dasharray="3,3"/>
                                    <text x="42" y="99" fill="#fff" font-size="10" text-anchor="end">100</text>
                                    <line x1="50" y1="150" x2="470" y2="150" stroke="#333" stroke-dasharray="3,3"/>
                                    <text x="42" y="154" fill="#fff" font-size="10" text-anchor="end">80</text>
                                    <line x1="50" y1="205" x2="470" y2="205" stroke="#333" stroke-dasharray="3,3"/>
                                    <text x="42" y="209" fill="#fff" font-size="10" text-anchor="end">60</text>
                                    <line x1="50" y1="260" x2="470" y2="260" stroke="#fff" stroke-width="1"/>
                                    <text x="42" y="264" fill="#fff" font-size="10" text-anchor="end">0</text>

                                    <g fill="#005f60" stroke="#000" stroke-width="0.5">
                                        <rect x="60" y="220" width="18" height="40"/>
                                        <rect x="80" y="200" width="18" height="60"/>
                                        <rect x="100" y="150" width="18" height="110"/>
                                        <rect x="120" y="100" width="18" height="160"/>
                                        <rect x="140" y="70" width="18" height="190"/>
                                        <rect x="160" y="40" width="18" height="220"/>
                                        <rect x="180" y="90" width="18" height="170"/>
                                        <rect x="200" y="110" width="18" height="150"/>
                                        <rect x="220" y="130" width="18" height="130"/>
                                        <rect x="240" y="160" width="18" height="100"/>
                                        <rect x="260" y="180" width="18" height="80"/>
                                        <rect x="280" y="200" width="18" height="60"/>
                                        <rect x="300" y="220" width="18" height="40"/>
                                    </g>

                                    <g fill="#fff" font-size="10" text-anchor="middle">
                                        <text x="100" y="280">4000</text>
                                        <text x="180" y="280">6000</text>
                                        <text x="260" y="280">8000</text>
                                        <text x="340" y="280">10000</text>
                                        <text x="420" y="280">12000</text>
                                    </g>
                                    <text x="260" y="295" fill="#fff" font-size="10" text-anchor="middle">Giá (VNĐ)</text>
                                    <text x="15" y="150" fill="#fff" font-size="10" text-anchor="middle" transform="rotate(-90 15 150)">Tần suất</text>
                                </svg>
                            </div>
                        </div>

                        <div class="space-y-2">
                            <h4 class="text-center font-bold text-white text-sm md:text-base">
                                Phân bố giá 2 quý cuối  (Q3 + Q4)
                            </h4>
                            <div class="w-full flex justify-center">
                                <svg viewBox="0 0 500 300" class="w-full h-auto">
                                    <line x1="50" y1="40" x2="470" y2="40" stroke="#333" stroke-dasharray="3,3"/>
                                    <text x="42" y="44" fill="#fff" font-size="10" text-anchor="end">160</text>
                                    <line x1="50" y1="95" x2="470" y2="95" stroke="#333" stroke-dasharray="3,3"/>
                                    <text x="42" y="99" fill="#fff" font-size="10" text-anchor="end">120</text>
                                    <line x1="50" y1="150" x2="470" y2="150" stroke="#333" stroke-dasharray="3,3"/>
                                    <text x="42" y="154" fill="#fff" font-size="10" text-anchor="end">80</text>
                                    <line x1="50" y1="205" x2="470" y2="205" stroke="#333" stroke-dasharray="3,3"/>
                                    <text x="42" y="209" fill="#fff" font-size="10" text-anchor="end">40</text>
                                    <line x1="50" y1="260" x2="470" y2="260" stroke="#fff" stroke-width="1"/>
                                    <text x="42" y="264" fill="#fff" font-size="10" text-anchor="end">0</text>

                                    <g fill="#b85333" stroke="#000" stroke-width="0.5">
                                        <rect x="60" y="40" width="18" height="220"/>
                                        <rect x="80" y="190" width="18" height="70"/>
                                        <rect x="100" y="160" width="18" height="100"/>
                                        <rect x="120" y="180" width="18" height="80"/>
                                        <rect x="140" y="140" width="18" height="120"/>
                                        <rect x="160" y="80" width="18" height="180"/>
                                        <rect x="180" y="60" width="18" height="200"/>
                                        <rect x="200" y="70" width="18" height="190"/>
                                        <rect x="220" y="100" width="18" height="160"/>
                                        <rect x="240" y="150" width="18" height="110"/>
                                        <rect x="260" y="180" width="18" height="80"/>
                                        <rect x="280" y="210" width="18" height="50"/>
                                    </g>

                                    <g fill="#fff" font-size="10" text-anchor="middle">
                                        <text x="120" y="280">20000</text>
                                        <text x="220" y="280">40000</text>
                                        <text x="320" y="280">60000</text>
                                        <text x="420" y="280">80000</text>
                                    </g>
                                    <text x="260" y="295" fill="#fff" font-size="10" text-anchor="middle">Giá (VNĐ)</text>
                                    <text x="15" y="150" fill="#fff" font-size="10" text-anchor="middle" transform="rotate(-90 15 150)">Tần suất</text>
                                </svg>
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
                        <div class="bg-gray-900/90 p-3.5 rounded-xl border border-gray-800 text-xs text-gray-300 leading-relaxed">
                            <span class="font-bold text-teal-400">Đặc điểm Q1 + Q2:</span> Phân bố chuẩn dạng hình chuông, tập trung chủ yếu quanh tần suất giá <b>6.000 – 8.000 VNĐ</b>.
                        </div>
                        <div class="bg-gray-900/90 p-3.5 rounded-xl border border-gray-800 text-xs text-gray-300 leading-relaxed">
                            <span class="font-bold text-orange-400">Đặc điểm Q3 + Q4:</span> Phân bố bị lệch phải kéo dài ra vùng giá cao <b>30.000 – 80.000 VNĐ</b>, thể hiện đợt tăng trưởng quy mô lớn.
                        </div>
                    </div>
                </div>
            </div>

            <!-- PHẦN 3: BẤT THƯỜNG & PHÂN BỐ -->
            <div id="section-3" class="space-y-6 pt-6 border-t border-gray-200">
                <div class="flex items-center gap-3">
                    <span class="p-2.5 bg-amber-100 text-amber-700 rounded-xl font-bold"><i class="fa-solid fa-bars-staggered"></i></span>
                    <div>
                        <h2 class="text-xl font-bold text-gray-900">3. Bất thường & Phân bố</h2>
                        <p class="text-xs text-gray-500">Thống kê chi tiết các phiên giá chạm trần/sàn và tổng quan mức độ bất thường</p>
                    </div>
                </div>

                <!-- BẢNG THỐNG KÊ PHIÊN BẤT THƯỜNG -->
                <div class="bg-black rounded-2xl p-5 shadow-md border border-gray-800 space-y-4 overflow-hidden">
                    <h3 class="text-center font-bold text-white text-base md:text-lg">
                        THỐNG KÊ CÁC PHIÊN GIAO DỊCH BẤT THƯỜNG (Hiển thị 15/363 ngày đầu)
                    </h3>
                    
                    <div class="overflow-x-auto rounded-xl border border-emerald-600/40">
                        <table class="w-full text-center border-collapse text-xs md:text-sm">
                            <thead>
                                <tr class="bg-emerald-600 text-white font-bold">
                                    <th class="p-2.5 border border-emerald-500/50">Ngày</th>
                                    <th class="p-2.5 border border-emerald-500/50">Giá tham chiếu</th>
                                    <th class="p-2.5 border border-emerald-500/50">Giá sàn</th>
                                    <th class="p-2.5 border border-emerald-500/50">Giá trần</th>
                                    <th class="p-2.5 border border-emerald-500/50">Giá min ngày</th>
                                    <th class="p-2.5 border border-emerald-500/50">Giá max ngày</th>
                                    <th class="p-2.5 border border-emerald-500/50">Yếu tố bất thường</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-700/60 bg-gray-600/60 text-gray-100 font-mono">
                                <tr><td class="p-2 border border-gray-500/40">1</td><td class="p-2 border border-gray-500/40">9457.59</td><td class="p-2 border border-gray-500/40">8511.83</td><td class="p-2 border border-gray-500/40">10403.34</td><td class="p-2 border border-gray-500/40">9000.0</td><td class="p-2 border border-gray-500/40">11000.0</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm tham chiếu</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">2</td><td class="p-2 border border-gray-500/40">9000.0</td><td class="p-2 border border-gray-500/40">8100.0</td><td class="p-2 border border-gray-500/40">9900.0</td><td class="p-2 border border-gray-500/40">8100.0</td><td class="p-2 border border-gray-500/40">9900.0</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">3</td><td class="p-2 border border-gray-500/40">8100.0</td><td class="p-2 border border-gray-500/40">7290.0</td><td class="p-2 border border-gray-500/40">8910.0</td><td class="p-2 border border-gray-500/40">7290.0</td><td class="p-2 border border-gray-500/40">8910.0</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">4</td><td class="p-2 border border-gray-500/40">7591.76</td><td class="p-2 border border-gray-500/40">6832.58</td><td class="p-2 border border-gray-500/40">8350.93</td><td class="p-2 border border-gray-500/40">6832.58</td><td class="p-2 border border-gray-500/40">8350.93</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">5</td><td class="p-2 border border-gray-500/40">8350.93</td><td class="p-2 border border-gray-500/40">7515.84</td><td class="p-2 border border-gray-500/40">9186.03</td><td class="p-2 border border-gray-500/40">7515.84</td><td class="p-2 border border-gray-500/40">9186.03</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">6</td><td class="p-2 border border-gray-500/40">9186.03</td><td class="p-2 border border-gray-500/40">8267.42</td><td class="p-2 border border-gray-500/40">10104.63</td><td class="p-2 border border-gray-500/40">8421.46</td><td class="p-2 border border-gray-500/40">10104.63</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">7</td><td class="p-2 border border-gray-500/40">10104.63</td><td class="p-2 border border-gray-500/40">9094.17</td><td class="p-2 border border-gray-500/40">11115.09</td><td class="p-2 border border-gray-500/40">9094.17</td><td class="p-2 border border-gray-500/40">11115.09</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">8</td><td class="p-2 border border-gray-500/40">10654.45</td><td class="p-2 border border-gray-500/40">9589.01</td><td class="p-2 border border-gray-500/40">11719.9</td><td class="p-2 border border-gray-500/40">9589.01</td><td class="p-2 border border-gray-500/40">11719.9</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">9</td><td class="p-2 border border-gray-500/40">11719.9</td><td class="p-2 border border-gray-500/40">10547.91</td><td class="p-2 border border-gray-500/40">12891.89</td><td class="p-2 border border-gray-500/40">10547.91</td><td class="p-2 border border-gray-500/40">12891.89</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">10</td><td class="p-2 border border-gray-500/40">11729.18</td><td class="p-2 border border-gray-500/40">10556.26</td><td class="p-2 border border-gray-500/40">12902.1</td><td class="p-2 border border-gray-500/40">11019.5</td><td class="p-2 border border-gray-500/40">12902.1</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">11</td><td class="p-2 border border-gray-500/40">12902.1</td><td class="p-2 border border-gray-500/40">11611.89</td><td class="p-2 border border-gray-500/40">14192.31</td><td class="p-2 border border-gray-500/40">11611.89</td><td class="p-2 border border-gray-500/40">14192.31</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">12</td><td class="p-2 border border-gray-500/40">11611.89</td><td class="p-2 border border-gray-500/40">10450.7</td><td class="p-2 border border-gray-500/40">12773.08</td><td class="p-2 border border-gray-500/40">10450.7</td><td class="p-2 border border-gray-500/40">12773.08</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">13</td><td class="p-2 border border-gray-500/40">11574.05</td><td class="p-2 border border-gray-500/40">10416.65</td><td class="p-2 border border-gray-500/40">12731.46</td><td class="p-2 border border-gray-500/40">10416.65</td><td class="p-2 border border-gray-500/40">12731.46</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">14</td><td class="p-2 border border-gray-500/40">10416.65</td><td class="p-2 border border-gray-500/40">9374.98</td><td class="p-2 border border-gray-500/40">11458.31</td><td class="p-2 border border-gray-500/40">9374.98</td><td class="p-2 border border-gray-500/40">11458.31</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần, Chạm sàn</td></tr>
                                <tr><td class="p-2 border border-gray-500/40">15</td><td class="p-2 border border-gray-500/40">9374.98</td><td class="p-2 border border-gray-500/40">8437.48</td><td class="p-2 border border-gray-500/40">10312.48</td><td class="p-2 border border-gray-500/40">9296.04</td><td class="p-2 border border-gray-500/40">10312.48</td><td class="p-2 border border-gray-500/40 font-sans text-amber-300">Chạm trần</td></tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="bg-gray-900/90 p-3.5 rounded-xl border border-gray-800 text-xs md:text-sm text-gray-300 leading-relaxed">
                        <p class="font-semibold text-emerald-400 flex items-center gap-1.5">
                            <i class="fa-solid fa-triangle-exclamation"></i> Giải thích yếu tố bất thường:
                        </p>
                        <p>Một ngày được gắn nhãn <b>bất thường</b> khi giá cực đại trong ngày (giá max) chạm biên giá trần (+10%) hoặc giá cực tiểu trong ngày (giá min) chạm biên giá sàn (-10%) so với giá tham chiếu ngày trước đó.</p>
                    </div>
                </div>

                <!-- BIỂU ĐỒ SO SÁNH BẤT THƯỜNG -->
                <div class="bg-black rounded-2xl p-5 shadow-md border border-gray-800 space-y-4 max-w-4xl mx-auto">
                    <h3 class="text-center font-bold text-white text-base md:text-lg">
                        So sánh số lượng ngày giao dịch BÌNH THƯỜNG và BẤT THƯỜNG (365 Ngày)
                    </h3>

                    <div class="w-full flex justify-center py-2">
                        <svg viewBox="0 0 700 380" class="w-full max-w-2xl h-auto font-sans">
                            <line x1="60" y1="40" x2="660" y2="40" stroke="#333" stroke-dasharray="3,3"/>
                            <text x="50" y="44" fill="#fff" font-size="11" text-anchor="end">400</text>
                            <line x1="60" y1="105" x2="660" y2="105" stroke="#333" stroke-dasharray="3,3"/>
                            <text x="50" y="109" fill="#fff" font-size="11" text-anchor="end">350</text>
                            <line x1="60" y1="170" x2="660" y2="170" stroke="#333" stroke-dasharray="3,3"/>
                            <text x="50" y="174" fill="#fff" font-size="11" text-anchor="end">300</text>
                            <line x1="60" y1="235" x2="660" y2="235" stroke="#333" stroke-dasharray="3,3"/>
                            <text x="50" y="239" fill="#fff" font-size="11" text-anchor="end">200</text>
                            <line x1="60" y1="300" x2="660" y2="300" stroke="#333" stroke-dasharray="3,3"/>
                            <text x="50" y="304" fill="#fff" font-size="11" text-anchor="end">100</text>
                            <line x1="60" y1="330" x2="660" y2="330" stroke="#fff" stroke-width="1.5"/>
                            <text x="50" y="334" fill="#fff" font-size="11" text-anchor="end">0</text>

                            <rect x="110" y="328" width="160" height="2" fill="#8edac8" stroke="#fff" stroke-width="1"/>
                            <text x="190" y="300" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">2 ngày</text>
                            <text x="190" y="318" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">(0.5%)</text>

                            <rect x="450" y="70" width="180" height="260" fill="#d9534f" stroke="#fff" stroke-width="1"/>
                            <text x="540" y="42" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">363 ngày</text>
                            <text x="540" y="60" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">(99.5%)</text>

                            <text x="190" y="355" fill="#fff" font-size="12" text-anchor="middle">Ngày bình thường</text>
                            <text x="540" y="355" fill="#fff" font-size="12" text-anchor="middle">Ngày bất thường</text>
                            <text x="15" y="180" fill="#fff" font-size="11" text-anchor="middle" transform="rotate(-90 15 180)">Số lượng phiên giao dịch (Ngày)</text>
                        </svg>
                    </div>

                    <div class="bg-gray-900/90 p-3.5 rounded-xl border border-gray-800 text-xs md:text-sm text-gray-300 leading-relaxed">
                        <p class="font-semibold text-red-400 flex items-center gap-1.5">
                            <i class="fa-solid fa-chart-pie"></i> Kết luận tỷ lệ bất thường:
                        </p>
                        <p>Trong 365 ngày giao dịch mô phỏng, có đến <b>363 ngày (chiếm 99.5%)</b> xuất hiện hiện tượng chạm giá trần hoặc chạm giá sàn trong phiên, chỉ có duy nhất <b>2 ngày (0.5%)</b> dao động biến động bình thường trong biên độ cho phép.</p>
                    </div>
                </div>

            </div>

            <!-- PHẦN 4: HIỆN TƯỢNG ĐỒ THỊ -->
            <div id="section-4" class="space-y-6 pt-6 border-t border-gray-200">
                <div class="flex items-center gap-3">
                    <span class="p-2.5 bg-purple-100 text-purple-700 rounded-xl font-bold"><i class="fa-regular fa-lightbulb"></i></span>
                    <div>
                        <h2 class="text-xl font-bold text-gray-900">4. Hiện tượng đồ thị </h2>
                        <p class="text-xs text-gray-500">Phân tích chuyên sâu quy tắc phối màu bảng điện và thuật toán đồ thị</p>
                    </div>
                </div>
                <!-- KHỐI BÁO CÁO GIẢI THÍCH CHI TIẾT HIỆN TƯỢNG -->
                <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100 space-y-6">
                    <div class="border-b border-gray-100 pb-4">
                        <h3 class="text-lg font-extrabold text-gray-900 flex items-center gap-2">
                            <i class="fa-solid fa-circle-question text-emerald-600"></i>
                            Giải thích: "Vì sao đường biểu diễn đi xuống nhưng có màu xanh?"
                        </h3>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <!-- MỤC 1: SO SÁNH VỚI GIÁ THAM CHIẾU -->
                        <div class="bg-emerald-50/50 rounded-xl p-5 border border-emerald-100 space-y-3">
                            <div class="flex items-center gap-2 text-emerald-800 font-bold text-sm md:text-base">
                                <span class="flex items-center justify-center w-6 h-6 bg-emerald-600 text-white rounded-full text-xs">1</span>
                                <span>So sánh với giá tham chiếu</span>
                            </div>
                            <ul class="text-xs md:text-sm text-gray-700 space-y-2 leading-relaxed pl-2">
                                <li class="flex items-start gap-1.5">
                                    <i class="fa-solid fa-angle-right text-emerald-600 mt-1"></i>
                                    <span><b>Màu xanh lá:</b> Được quy định cho mức giá cao hơn giá tham chiếu.</span>
                                </li>
                                <li class="flex items-start gap-1.5">
                                    <i class="fa-solid fa-angle-right text-emerald-600 mt-1"></i>
                                    <span><b>Giá tham chiếu:</b> Chính là giá đóng cửa của ngày giao dịch trước đó.</span>
                                </li>
                            </ul>
                        </div>
                        <!-- MỤC 2: HIỆN TƯỢNG ĐƯỜNG ĐI XUỐNG CÓ MÀU XANH -->
                        <div class="bg-blue-50/50 rounded-xl p-5 border border-blue-100 space-y-3">
                            <div class="flex items-center gap-2 text-blue-800 font-bold text-sm md:text-base">
                                <span class="flex items-center justify-center w-6 h-6 bg-blue-600 text-white rounded-full text-xs">2</span>
                                <span>Hiện tượng "Đường đi xuống nhưng vẫn có màu xanh"</span>
                            </div>
                            <p class="text-xs md:text-sm text-gray-700 leading-relaxed">
                                Hiện tượng này xảy ra khi giá đang trong một xu hướng điều chỉnh/giảm ngắn hạn (đi xuống từ đỉnh của phiên hoặc của ngày hôm đó), nhưng mặt bằng giá hiện tại vẫn cao hơn mức giá tham chiếu của ngày.
                            </p>
                        </div>
                    </div>
                    <!-- THUẬT TOÁN XỬ LÝ LINECOLLECTION -->
                    <div class="bg-gray-900 text-gray-200 rounded-xl p-4 border border-gray-800 space-y-2 text-xs md:text-sm">
                        <div class="font-bold text-amber-400 flex items-center gap-2">
                            <i class="fa-solid fa-code"></i> Tóm tắt xử lý đồ họa trong Python (Matplotlib):
                        </div>
                        <p class="text-gray-300 leading-relaxed">
                            Màu sắc của mỗi phân đoạn đường không phụ thuộc vào độ dốc âm/dương (đi lên hay đi xuống) của đoạn đó, mà phụ thuộc hoàn toàn vào giá trị tại thời điểm giao dịch so với giá tham chiếu. Do đó, dù đường biểu diễn đi xuống nhưng thuộc vùng giá lớn hơn giá tham chiếu, mảng màu tô bằng LineCollection vẫn được gán màu xanh chuẩn chứng khoán.
                        </p>
                    </div>
                </div>
            </div>
            <!-- PHẦN 5: KẾT LUẬN & MỞ RỘNG -->
            <div id="section-5" class="space-y-6 pt-6 border-t border-gray-200">
                <div class="flex items-center gap-3">
                    <span class="p-2.5 bg-emerald-100 text-emerald-700 rounded-xl font-bold"><i class="fa-solid fa-newspaper"></i></span>
                    <div>
                        <h2 class="text-xl font-bold text-gray-900">5. Kết luận & Mở rộng</h2>
                        <p class="text-xs text-gray-500">Đánh giá tổng quan dự án đồ án và hướng phát triển ứng dụng thực tế</p>
                    </div>
                </div>

                <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 space-y-4">
                    <div class="space-y-2">
                        <h3 class="font-bold text-gray-900 text-base flex items-center gap-2">
                            <i class="fa-solid fa-check-circle text-emerald-600"></i> Tổng Kết Đồ Án
                        </h3>
                        <p class="text-xs md:text-sm text-gray-600 leading-relaxed">
                            Đồ án đã xây dựng thành công ứng dụng web trực quan hóa biến động giá cổ phiếu 365 ngày bằng Python (FastAPI & Matplotlib) triển khai lên môi trường Render. Ứng dụng đáp ứng đầy đủ yêu cầu mô phỏng nến Min-Max, biểu đồ chuỗi thời gian phân màu chuẩn chứng khoán, phân tích các chỉ số thống kê (Mean, Boxplot, Histogram) và lọc các ngày giao dịch có biến động bất thường.
                        </p>
                    </div>

                    <div class="space-y-2 pt-2 border-t border-gray-100">
                        <h3 class="font-bold text-gray-900 text-base flex items-center gap-2">
                            <i class="fa-solid fa-rocket text-blue-600"></i> Hướng Phát Triển Mở Rộng
                        </h3>
                        <ul class="text-xs md:text-sm text-gray-600 space-y-1.5 list-disc pl-5">
                            <li>Kết nối API dữ liệu chứng khoán thực tế theo thời gian thực (Real-time stock data).</li>
                            <li>Tích hợp thêm các chỉ báo kỹ thuật nâng cao như Moving Average (MA), RSI, Bollinger Bands.</li>
                            <li>Ứng dụng mô hình học máy (LSTM/RNN) để dự báo xu hướng giá cổ phiếu tương lai.</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- KHỐI CẢM ƠN (LỜI TRI ÂN LỊCH SỰ VÀ TRANG TRỌNG) -->
            <div class="bg-gradient-to-r from-gray-900 via-slate-800 to-gray-900 text-white rounded-2xl p-8 shadow-lg border border-gray-800 text-center space-y-3 my-8">
                <div class="inline-flex items-center justify-center w-12 h-12 bg-amber-500/20 text-amber-400 rounded-full mb-1">
                    <i class="fa-solid fa-heart text-xl"></i>
                </div>
                <h3 class="text-xl md:text-2xl font-extrabold text-amber-400 tracking-wide">
                    LỜI CẢM ƠN
                </h3>
                <p class="text-xs md:text-sm text-gray-300 max-w-2xl mx-auto leading-relaxed">
                    Em xin chân thành cảm ơn thầy <b>Phan Trần Đức Minh</b> đã tận tình hướng dẫn, hỗ trợ kiến thức chuyên môn và tạo điều kiện giúp em hoàn thành đồ án này!
                </p>
            </div>

        </div>
    </body>
    </html>
    """
    return html_content
