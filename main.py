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

            <!-- THANH MENU ĐIỀU HƯỚNG TỰ ĐỘNG CUỘN (SCROLL) -->
            <div class="flex flex-wrap gap-3 py-2 overflow-x-auto sticky top-4 z-50 bg-gray-100/90 backdrop-blur p-2 rounded-2xl">
                <a href="#section-1" class="cursor-pointer flex items-center gap-2 bg-slate-300 text-gray-900 font-bold px-4 py-2.5 rounded-xl text-sm border border-gray-400 shadow-md hover:bg-slate-400 hover:shadow-lg hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-play text-gray-800 text-xs"></i>
                    <span>1. Mô Phỏng & Quy Tắc</span>
                </a>

                <a href="#section-2" class="cursor-pointer flex items-center gap-2 bg-white text-gray-700 font-medium px-4 py-2.5 rounded-xl text-sm border border-gray-200 shadow-sm hover:bg-slate-100 hover:text-gray-900 hover:border-gray-300 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-chart-column text-gray-400 text-xs"></i>
                    <span>2. Diễn Biến Tháng/Quý</span>
                </a>

                <a href="#section-2" class="cursor-pointer flex items-center gap-2 bg-white text-gray-700 font-medium px-4 py-2.5 rounded-xl text-sm border border-gray-200 shadow-sm hover:bg-slate-100 hover:text-gray-900 hover:border-gray-300 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-solid fa-bars-staggered text-gray-400 text-xs"></i>
                    <span>3. Bất Thường & Phân Bố</span>
                </a>

                <a href="#section-2" class="cursor-pointer flex items-center gap-2 bg-white text-gray-700 font-medium px-4 py-2.5 rounded-xl text-sm border border-gray-200 shadow-sm hover:bg-slate-100 hover:text-gray-900 hover:border-gray-300 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-regular fa-lightbulb text-gray-400 text-xs"></i>
                    <span>4. Hiện Tượng Kỹ Thuật</span>
                </a>

                <a href="#section-2" class="cursor-pointer flex items-center gap-2 bg-white text-gray-700 font-medium px-4 py-2.5 rounded-xl text-sm border border-gray-200 shadow-sm hover:bg-slate-100 hover:text-gray-900 hover:border-gray-300 hover:shadow-md hover:-translate-y-0.5 active:scale-95 transition-all duration-200">
                    <i class="fa-regular fa-newspaper text-gray-400 text-xs"></i>
                    <span>5. Kết Luận & Mở Rộng</span>
                </a>
            </div>

            <!-- PHẦN 1: MÔ PHỎNG & QUY TẮC -->
            <div id="section-1" class="space-y-6 pt-2">
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
                            <span class="text-amber-500">🎨</span> Quy Tắc 5 Màu Chứng Khoán
                        </h2>
                        <p class="text-xs text-gray-500">
                            Chuẩn màu bảng điện giao dịch chứng khoán áp dụng trong mô phỏng Python:
                        </p>
                    </div>

                    <div class="space-y-2">
                        <div class="flex justify-between items-center bg-purple-50/60 p-3.5 rounded-xl border border-purple-100/50 hover:bg-purple-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-purple-600 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Giá Trần (Ceiling)</span>
                            </div>
                            <span class="text-xs font-semibold text-purple-700">+10% so với Tham chiếu</span>
                        </div>

                        <div class="flex justify-between items-center bg-emerald-50/60 p-3.5 rounded-xl border border-emerald-100/50 hover:bg-emerald-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-emerald-500 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Tăng Giá (Increase)</span>
                            </div>
                            <span class="text-xs font-semibold text-emerald-700">Giá đóng > Tham chiếu</span>
                        </div>

                        <div class="flex justify-between items-center bg-amber-50/60 p-3.5 rounded-xl border border-amber-100/50 hover:bg-amber-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-amber-500 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Tham Chiếu (Reference)</span>
                            </div>
                            <span class="text-xs font-semibold text-amber-700">Giá đóng ngày trước ($P_{ref}$)</span>
                        </div>

                        <div class="flex justify-between items-center bg-rose-50/60 p-3.5 rounded-xl border border-rose-100/50 hover:bg-rose-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-rose-500 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Giảm Giá (Decrease)</span>
                            </div>
                            <span class="text-xs font-semibold text-rose-700">Giá đóng < Tham chiếu</span>
                        </div>

                        <div class="flex justify-between items-center bg-cyan-50/60 p-3.5 rounded-xl border border-cyan-100/50 hover:bg-cyan-100/80 transition-colors">
                            <div class="flex items-center gap-3">
                                <span class="w-3.5 h-3.5 rounded-full bg-cyan-500 inline-block shadow-sm"></span>
                                <span class="font-semibold text-sm text-gray-800">Giá Sàn (Floor)</span>
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
                        <h2 class="text-xl font-bold text-gray-900">2. Diễn Biến Tháng / Quý</h2>
                        <p class="text-xs text-gray-500">Phân tích xu hướng trung bình, độ biến động và phân bố giá theo thời gian</p>
                    </div>
                </div>

                <!-- 1. Biểu đồ cột: Giá trung bình theo tháng -->
                <div class="bg-black rounded-2xl p-5 shadow-md border border-gray-800 space-y-4">
                    <h3 class="text-center font-bold text-white text-base md:text-lg">
                        Giá Trung Bình Mã Cổ Phiếu Theo Tháng
                    </h3>
                    <div class="w-full flex justify-center">
                        <svg viewBox="0 0 1000 500" class="w-full h-auto text-sky-400 font-sans">
                            <line x1="80" y1="50" x2="950" y2="50" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="55" fill="#fff" font-size="12" text-anchor="end">50000</text>

                            <line x1="80" y1="140" x2="950" y2="140" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="145" fill="#fff" font-size="12" text-anchor="end">40000</text>

                            <line x1="80" y1="230" x2="950" y2="230" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="235" fill="#fff" font-size="12" text-anchor="end">30000</text>

                            <line x1="80" y1="320" x2="950" y2="320" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="325" fill="#fff" font-size="12" text-anchor="end">20000</text>

                            <line x1="80" y1="410" x2="950" y2="410" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="415" fill="#fff" font-size="12" text-anchor="end">10000</text>

                            <line x1="80" y1="450" x2="950" y2="450" stroke="#fff" stroke-width="1.5"/>
                            <text x="70" y="455" fill="#fff" font-size="12" text-anchor="end">0</text>

                            <g fill="#87ceeb">
                                <rect x="100" y="357" width="55" height="93" rx="2"/>
                                <rect x="172" y="384" width="55" height="66" rx="2"/>
                                <rect x="244" y="396" width="55" height="54" rx="2"/>
                                <rect x="316" y="391" width="55" height="59" rx="2"/>
                                <rect x="388" y="391" width="55" height="59" rx="2"/>
                                <rect x="460" y="377" width="55" height="73" rx="2"/>
                                <rect x="532" y="375" width="55" height="75" rx="2"/>
                                <rect x="604" y="242" width="55" height="208" rx="2"/>
                                <rect x="676" y="119" width="55" height="331" rx="2"/>
                                <rect x="748" y="44" width="55" height="406" rx="2"/>
                                <rect x="820" y="96" width="55" height="354" rx="2"/>
                                <rect x="892" y="149" width="55" height="301" rx="2"/>
                            </g>

                            <g fill="#fff" font-size="13" text-anchor="end">
                                <text x="135" y="475" transform="rotate(-45 135 475)">Tháng 1</text>
                                <text x="207" y="475" transform="rotate(-45 207 475)">Tháng 2</text>
                                <text x="279" y="475" transform="rotate(-45 279 475)">Tháng 3</text>
                                <text x="351" y="475" transform="rotate(-45 351 475)">Tháng 4</text>
                                <text x="423" y="475" transform="rotate(-45 423 475)">Tháng 5</text>
                                <text x="495" y="475" transform="rotate(-45 495 475)">Tháng 6</text>
                                <text x="567" y="475" transform="rotate(-45 567 475)">Tháng 7</text>
                                <text x="639" y="475" transform="rotate(-45 639 475)">Tháng 8</text>
                                <text x="711" y="475" transform="rotate(-45 711 475)">Tháng 9</text>
                                <text x="783" y="475" transform="rotate(-45 783 475)">Tháng 10</text>
                                <text x="855" y="475" transform="rotate(-45 855 475)">Tháng 11</text>
                                <text x="927" y="475" transform="rotate(-45 927 475)">Tháng 12</text>
                            </g>
                        </svg>
                    </div>

                    <!-- Lời giải thích cho Biểu đồ 1 -->
                    <div class="bg-gray-900/90 p-4 rounded-xl border border-gray-800 text-xs md:text-sm text-gray-300 space-y-1.5 leading-relaxed">
                        <p class="font-semibold text-sky-400 flex items-center gap-2">
                            <i class="fa-solid fa-circle-info"></i> Nhận xét & Phân tích xu hướng:
                        </p>
                        <p>
                            • <b>Giai đoạn tích lũy (Tháng 1 - Tháng 7):</b> Mức giá trung bình duy trì ổn định ở vùng giá thấp dưới 10.000 VNĐ, giá giao dịch dao động đi ngang (sideway).
                        </p>
                        <p>
                            • <b>Giai đoạn bùng nổ (Tháng 8 - Tháng 10):</b> Giá cổ phiếu bước vào sóng tăng trưởng mạnh mẽ (uptrend), đạt đỉnh kỷ lục vào <b>Tháng 10</b> với mức giá trung bình vượt <b>50.000 VNĐ</b>.
                        </p>
                        <p>
                            • <b>Giai đoạn điều chỉnh (Tháng 11 - Tháng 12):</b> Xuất hiện áp lực chốt lời khiến giá trung bình giảm dần về mức ~33.000 VNĐ cuối năm.
                        </p>
                    </div>
                </div>

                <!-- 2. Biểu đồ Boxplot -->
                <div class="bg-black rounded-2xl p-5 shadow-md border border-gray-800 space-y-4">
                    <h3 class="text-center font-bold text-white text-base md:text-lg">
                        Biểu Đồ Hộp (Boxplot) Biến Động Giá Mỗi Tháng
                    </h3>
                    <div class="w-full flex justify-center">
                        <svg viewBox="0 0 1000 500" class="w-full h-auto">
                            <line x1="80" y1="50" x2="950" y2="50" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="55" fill="#fff" font-size="12" text-anchor="end">80000</text>

                            <line x1="80" y1="150" x2="950" y2="150" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="155" fill="#fff" font-size="12" text-anchor="end">60000</text>

                            <line x1="80" y1="250" x2="950" y2="250" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="255" fill="#fff" font-size="12" text-anchor="end">40000</text>

                            <line x1="80" y1="350" x2="950" y2="350" stroke="#444" stroke-dasharray="4,4"/>
                            <text x="70" y="355" fill="#fff" font-size="12" text-anchor="end">20000</text>

                            <line x1="80" y1="450" x2="950" y2="450" stroke="#fff" stroke-width="1.5"/>
                            <text x="70" y="455" fill="#fff" font-size="12" text-anchor="end">0</text>

                            <g stroke="#fff" fill="#8edac8" stroke-width="1">
                                <rect x="110" y="390" width="40" height="15" />
                                <rect x="182" y="405" width="40" height="15" />
                                <rect x="254" y="415" width="40" height="12" />
                                <rect x="326" y="412" width="40" height="12" />
                                <rect x="398" y="412" width="40" height="12" />
                                <rect x="470" y="405" width="40" height="15" />
                                <rect x="542" y="405" width="40" height="15" />

                                <rect x="614" y="305" width="40" height="58" />
                                <rect x="686" y="250" width="40" height="30" />
                                <rect x="758" y="135" width="40" height="120" />
                                <rect x="830" y="200" width="40" height="45" />
                                <rect x="902" y="255" width="40" height="45" />
                            </g>

                            <g fill="#fff" font-size="13" text-anchor="middle">
                                <text x="130" y="475">T1</text>
                                <text x="202" y="475">T2</text>
                                <text x="274" y="475">T3</text>
                                <text x="346" y="475">T4</text>
                                <text x="418" y="475">T5</text>
                                <text x="490" y="475">T6</text>
                                <text x="562" y="475">T7</text>
                                <text x="634" y="475">T8</text>
                                <text x="706" y="475">T9</text>
                                <text x="778" y="475">T10</text>
                                <text x="850" y="475">T11</text>
                                <text x="922" y="475">T12</text>
                            </g>
                        </svg>
                    </div>

                    <!-- Lời giải thích cho Biểu đồ 2 -->
                    <div class="bg-gray-900/90 p-4 rounded-xl border border-gray-800 text-xs md:text-sm text-gray-300 space-y-1.5 leading-relaxed">
                        <p class="font-semibold text-teal-300 flex items-center gap-2">
                            <i class="fa-solid fa-chart-line"></i> Phân tích độ biến động (Volatility):
                        </p>
                        <p>
                            • <b>Chiều cao hộp (IQR):</b> Chiều cao thân hộp từ <b>T1 đến T7</b> rất hẹp, cho thấy độ rủi ro và biến động giá theo ngày ở mức thấp.
                        </p>
                        <p>
                            • <b>Độ rộng râu (Whisker) & Ngoại lệ:</b> Khung <b>T10</b> có chiều cao hộp và đường râu kéo dài nhất (từ ~28.000 VNĐ lên hơn 89.000 VNĐ), thể hiện đây là tháng cổ phiếu có độ rung lắc mạnh nhất năm và chứa nhiều điểm giá đột biến (Outliers).
                        </p>
                    </div>
                </div>

                <!-- 3. Biểu đồ Phân Bố Giá 2 Quý Đầu & Cuối Năm -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Q1 + Q2 -->
                    <div class="bg-black rounded-2xl p-5 shadow-md border border-gray-800 space-y-3">
                        <h4 class="text-center font-bold text-white text-sm md:text-base">
                            Phân Bố Giá 2 Quý Đầu Năm (Q1 + Q2)
                        </h4>
                        <div class="w-full flex justify-center">
                            <svg viewBox="0 0 500 300" class="w-full h-auto">
                                <line x1="50" y1="40" x2="470" y2="40" stroke="#333" stroke-dasharray="3,3"/>
                                <line x1="50" y1="100" x2="470" y2="100" stroke="#333" stroke-dasharray="3,3"/>
                                <line x1="50" y1="160" x2="470" y2="160" stroke="#333" stroke-dasharray="3,3"/>
                                <line x1="50" y1="220" x2="470" y2="220" stroke="#333" stroke-dasharray="3,3"/>
                                <line x1="50" y1="260" x2="470" y2="260" stroke="#fff" stroke-width="1"/>

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
                            </svg>
                        </div>
                        <p class="text-xs text-gray-300 leading-relaxed bg-gray-900/90 p-3 rounded-xl border border-gray-800">
                            <b>Đặc điểm Q1 + Q2:</b> Phân bố dạng hình chuông (Chuẩn - Normal Distribution) tập trung chủ yếu quanh tần suất giá <b>6.000 – 8.000 VNĐ</b>. Không xuất hiện hiện tượng biến động giá bất thường.
                        </p>
                    </div>

                    <!-- Q3 + Q4 -->
                    <div class="bg-black rounded-2xl p-5 shadow-md border border-gray-800 space-y-3">
                        <h4 class="text-center font-bold text-white text-sm md:text-base">
                            Phân Bố Giá 2 Quý Cuối Năm (Q3 + Q4)
                        </h4>
                        <div class="w-full flex justify-center">
                            <svg viewBox="0 0 500 300" class="w-full h-auto">
                                <line x1="50" y1="40" x2="470" y2="40" stroke="#333" stroke-dasharray="3,3"/>
                                <line x1="50" y1="100" x2="470" y2="100" stroke="#333" stroke-dasharray="3,3"/>
                                <line x1="50" y1="160" x2="470" y2="160" stroke="#333" stroke-dasharray="3,3"/>
                                <line x1="50" y1="220" x2="470" y2="220" stroke="#333" stroke-dasharray="3,3"/>
                                <line x1="50" y1="260" x2="470" y2="260" stroke="#fff" stroke-width="1"/>

                                <g fill="#b85333" stroke="#000" stroke-width="0.5">
                                    <rect x="60" y="50" width="18" height="210"/>
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
                            </svg>
                        </div>
                        <p class="text-xs text-gray-300 leading-relaxed bg-gray-900/90 p-3 rounded-xl border border-gray-800">
                            <b>Đặc điểm Q3 + Q4:</b> Phân bố bị lệch phải (Right-skewed) kéo dài ra vùng giá cao <b>30.000 – 80.000 VNĐ</b>, phản ánh sự thay đổi về quy mô thị trường và biên độ giá trong nửa cuối năm.
                        </p>
                    </div>
                </div>
            </div>

        </div>
    </body>
    </html>
    """
    return html_content
