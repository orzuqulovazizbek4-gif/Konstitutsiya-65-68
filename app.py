```html
<!DOCTYPE html>
<html lang="uz" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>O'zbekiston Respublikasi Konstitutsiyasi - XII Bob Blanket Normalari Interaktiv Tizimi</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts Inter & Fira Code -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        emerald: {
                            400: '#34d399',
                            500: '#10b981',
                            600: '#059669',
                            900: '#064e3b',
                            950: '#022c22',
                        },
                        gold: {
                            400: '#fbbf24',
                            500: '#f59e0b',
                            600: '#d97706',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['Fira Code', 'monospace'],
                    },
                    animation: {
                        'breathing': 'breathing 12s ease-in-out infinite',
                        'pulse-glow': 'pulseGlow 3s ease-in-out infinite',
                        'float': 'float 6s ease-in-out infinite',
                    },
                    keyframes: {
                        breathing: {
                            '0%, 100%': { backgroundPosition: '0% 50%', backgroundSize: '150% 150%' },
                            '50%': { backgroundPosition: '100% 50%', backgroundSize: '200% 200%' },
                        },
                        pulseGlow: {
                            '0%, 100%': { opacity: '0.4', transform: 'scale(1)' },
                            '50%': { opacity: '0.8', transform: 'scale(1.03)' },
                        },
                        float: {
                            '0%, 100%': { transform: 'translateY(0px)' },
                            '50%': { transform: 'translateY(-8px)' },
                        }
                    }
                }
            }
        }
    </script>

    <style>
        /* Modern Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #10b981;
        }

        /* Dynamic Animated Background Mesh */
        .animated-bg {
            background: linear-gradient(-45deg, #022c22, #0f172a, #1e1b4b, #064e3b, #0f172a);
            background-size: 400% 400%;
            animation: breathing 16s ease infinite;
        }

        .glass-card {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }

        .glass-modal {
            background: rgba(10, 15, 29, 0.92);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(16, 185, 129, 0.2);
        }

        .blanket-tag {
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .blanket-tag:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 20px -2px rgba(16, 185, 129, 0.4);
        }

        /* Modal Animation */
        .modal-enter {
            opacity: 0;
            transform: scale(0.95) translateY(20px);
        }
        .modal-enter-active {
            opacity: 1;
            transform: scale(1) translateY(0);
            transition: opacity 300ms ease-out, transform 300ms ease-out;
        }
        
        .highlight-glow {
            box-shadow: 0 0 25px -5px rgba(16, 185, 129, 0.3);
        }
    </style>
</head>
<body class="animated-bg min-h-screen text-slate-100 font-sans selection:bg-emerald-500 selection:text-slate-900 flex flex-col justify-between">

    <div>
        <!-- Top Announcement Bar -->
        <header class="sticky top-0 z-40 glass-card border-b border-slate-800/80">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
                <div class="flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-400 flex items-center justify-center shadow-lg shadow-emerald-950/50">
                        <i class="fa-solid font-bold text-2xl text-slate-950 fa-scale-balanced"></i>
                    </div>
                    <div>
                        <h1 class="text-xl sm:text-2xl font-black tracking-tight bg-gradient-to-r from-emerald-400 via-teal-200 to-gold-400 bg-clip-text text-transparent">
                            O'ZBEKISTON KONSTITUTSIYASI
                        </h1>
                        <p class="text-xs sm:text-sm text-slate-400 flex items-center gap-2">
                            <span>UCHINCHI BOʻLIM. JAMIYAT VA SHAXS</span>
                            <span class="text-emerald-500">•</span>
                            <span class="text-emerald-400 font-medium">XII bob. Jamiyatning iqtisodiy negizlari</span>
                        </p>
                    </div>
                </div>

                <!-- Action Controls -->
                <div class="flex items-center gap-3">
                    <div class="relative hidden sm:block w-64 md:w-80">
                        <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm"></i>
                        <input type="text" id="searchInput" oninput="filterContent()" placeholder="Qonun yoki moddani qidirish..." 
                            class="w-full bg-slate-900/90 border border-slate-700/60 rounded-lg pl-9 pr-4 py-2 text-sm text-slate-200 focus:outline-none focus:border-emerald-500 transition-colors">
                    </div>
                    <button onclick="toggleAllCards()" id="toggleCollapseBtn" class="px-3.5 py-2 bg-slate-800/80 hover:bg-slate-700 rounded-lg text-xs font-semibold text-slate-300 border border-slate-700 transition flex items-center gap-2">
                        <i class="fa-solid fa-arrows-up-down"></i>
                        <span class="hidden md:inline">Barchasini yopish/ochish</span>
                    </button>
                </div>
            </div>
        </header>

        <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
            <!-- Hero Banner -->
            <div class="relative overflow-hidden rounded-2xl glass-card p-6 sm:p-8 border border-emerald-500/20 shadow-2xl">
                <div class="absolute -right-10 -bottom-10 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute -left-10 -top-10 w-80 h-80 bg-teal-500/10 rounded-full blur-3xl pointer-events-none"></div>

                <div class="relative z-10 max-w-4xl">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-semibold mb-4">
                        <i class="fa-solid fa-link text-xs"></i>
                        <span>Interaktiv Blanket Normalar Platformasi</span>
                    </div>
                    <h2 class="text-2xl sm:text-4xl font-extrabold text-white tracking-tight leading-tight">
                        Konstitutsiyaviy Normalar va Boshqa Qonun Hujjatlari Bilan O'zaro Aloqadorlik Kodeksi
                    </h2>
                    <p class="mt-3 text-slate-300 text-sm sm:text-base leading-relaxed">
                        Ushbu tizim O'zbekiston Respublikasi Konstitutsiyasining 65, 66, 67 hamda 68-moddalaridagi **har bir qism** uchun tegishli tarmoq qonunlariga (Fuqarolik, Yer, Ekologiya, Bojxona kodekslari va sohaviy qonunlarga) yo'naltirilgan blanket normalarini chuqur tahliliy ko'rinishda taqdim etadi. Matndagi ajratilgan havola tugmalarni bosing.
                    </p>

                    <!-- Quick Stats -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-6 pt-6 border-t border-slate-800">
                        <div class="flex flex-col">
                            <span class="text-2xl font-black text-emerald-400">4 ta</span>
                            <span class="text-xs text-slate-400 font-medium">Moddalar (65-68)</span>
                        </div>
                        <div class="flex flex-col">
                            <span class="text-2xl font-black text-emerald-400">11 ta</span>
                            <span class="text-xs text-slate-400 font-medium">Konstitutsiyaviy qismlar</span>
                        </div>
                        <div class="flex flex-col">
                            <span class="text-2xl font-black text-gold-400">28+ ta</span>
                            <span class="text-xs text-slate-400 font-medium">Blanket Normalar</span>
                        </div>
                        <div class="flex flex-col">
                            <span class="text-2xl font-black text-teal-300">100%</span>
                            <span class="text-xs text-slate-400 font-medium">Asl matn va Tahlil</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Mobile Search Bar -->
            <div class="sm:hidden">
                <div class="relative w-full">
                    <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm"></i>
                    <input type="text" id="mobileSearchInput" oninput="filterContentMobile()" placeholder="Qonun yoki moddani qidirish..." 
                        class="w-full bg-slate-900/90 border border-slate-700/60 rounded-lg pl-9 pr-4 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-emerald-500">
                </div>
            </div>

            <div id="articlesContainer" class="space-y-8">
                <!-- Dynamic Content Will Be Rendered Here by JS -->
            </div>
        </main>
    </div>

    <footer class="glass-card border-t border-slate-800/80 mt-16 py-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-3">
            <p class="text-sm text-slate-400">
                O'zbekiston Respublikasi Konstitutsiyasi (30.04.2023 tahriri) va milliy qonunchilik tizimi asosida ishlab chiqilgan.
            </p>
            <p class="text-xs text-slate-500">
                <i class="fa-solid fa-code text-emerald-500"></i> Barcha blanket normalar va huquqiy sharhlar Lex.uz qonunchilik bazasi hamda amaldagi normativ-huquqiy hujjatlarga muvofiq tuzilgan.
            </p>
        </div>
    </footer>

    <!-- MODAL POPUP FOR BLANKET NORM DETAILS -->
    <div id="normModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 md:p-10 hidden" aria-modal="true" role="dialog">
        <!-- Backdrop -->
        <div onclick="closeModal()" class="fixed inset-0 bg-slate-950/80 backdrop-blur-md transition-opacity"></div>

        <!-- Modal Container -->
        <div class="relative glass-modal w-full max-w-4xl max-h-[90vh] rounded-2xl shadow-2xl overflow-hidden flex flex-col z-10 border border-emerald-500/30 animate-pulse-glow">
            <!-- Modal Header -->
            <div class="p-5 sm:p-6 border-b border-slate-800/80 flex items-start justify-between bg-slate-900/60">
                <div class="space-y-1.5 pr-6">
                    <div class="flex items-center gap-2">
                        <span id="modalCategoryBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                            Fuqarolik Huquqi
                        </span>
                        <span id="modalRelationBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-gold-500/20 text-gold-400 border border-gold-500/30">
                            Direct Blanket Link
                        </span>
                    </div>
                    <h3 id="modalTitle" class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                        --
                    </h3>
                    <p id="modalLawSource" class="text-xs sm:text-sm text-emerald-400 font-mono font-medium flex items-center gap-2">
                        <i class="fa-solid fa-book-bookmark"></i>
                        <span>--</span>
                    </p>
                </div>
                <button onclick="closeModal()" class="w-9 h-9 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition border border-slate-700">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>
            </div>

            <!-- Modal Content Body (Scrollable) -->
            <div class="p-6 overflow-y-auto space-y-6 flex-1 text-slate-200">
                <!-- Original Law Text Section -->
                <div class="space-y-2">
                    <div class="flex items-center justify-between">
                        <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-2">
                            <i class="fa-solid fa-scroll text-emerald-400"></i>
                            Qonunning Asl Nusxasi (Matni)
                        </h4>
                        <button onclick="copyModalText()" class="text-xs text-slate-400 hover:text-emerald-400 transition flex items-center gap-1 bg-slate-800/50 px-2 py-1 rounded border border-slate-700">
                            <i class="fa-regular fa-copy"></i> Copy text
                        </button>
                    </div>
                    <div class="p-4 rounded-xl bg-slate-950/80 border border-slate-800 font-mono text-sm sm:text-base text-emerald-300/90 leading-relaxed relative">
                        <div class="absolute top-2 right-2 text-xs text-slate-600 font-sans">Lex.uz Asli</div>
                        <p id="modalOriginalText" class="whitespace-pre-line italic">
                            --
                        </p>
                    </div>
                </div>

                <!-- Comprehensive Legal Explanation / Relation Section -->
                <div class="space-y-2">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-2">
                        <i class="fa-solid fa-brain text-gold-400"></i>
                        Konstitutsiya Bilan Bog'liqligi va Tushuntirish
                    </h4>
                    <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800 text-slate-300 text-sm sm:text-base leading-relaxed space-y-3">
                        <p id="modalExplanation">
                            --
                        </p>
                    </div>
                </div>

                <!-- Practical Application / Example Section -->
                <div class="space-y-2">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-2">
                        <i class="fa-solid fa-gavel text-teal-400"></i>
                        Huquqiy Amaliyot va Kafolat Mexanizmi
                    </h4>
                    <div class="p-4 rounded-xl bg-emerald-950/30 border border-emerald-900/50 text-emerald-200/90 text-sm leading-relaxed">
                        <p id="modalPractical">
                            --
                        </p>
                    </div>
                </div>
            </div>

            <!-- Modal Footer -->
            <div class="p-4 sm:p-5 border-t border-slate-800/80 bg-slate-900/80 flex items-center justify-between">
                <span class="text-xs text-slate-500">O'zbekiston Respublikasi Qonunchilik Ma'lumotlari Milliy Bazasi</span>
                <button onclick="closeModal()" class="px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold text-sm rounded-lg transition shadow-lg shadow-emerald-900/40">
                    Tushunarli (Yopish)
                </button>
            </div>
        </div>
    </div>

    <script>
        // Full Structured Legal Database for Articles 65, 66, 67, 68 of Uzbekistan Constitution
        const legalDatabase = [
            {
                id: 65,
                number: "65-MODDA",
                title: "Iqtisodiyotning Negizi, Mulk Shakllari va Halol Raqobat Kafolati",
                constitutionalText: `Fuqarolar farovonligini oshirishga qaratilgan Oʻzbekiston iqtisodiyotining negizini xilma-xil shakllardagi mulk tashkil etadi. Davlat bozor munosabatlarini rivojlantirish va halol raqobat uchun shart-sharoitlar yaratadi, isteʼmolchilarning huquqlari ustuvorligini hisobga olgan holda iqtisodiy faoliyat, tadbirkorlik va mehnat qilish erkinligini kafolatlaydi.

Oʻzbekiston Respublikasida barcha mulk shakllarining teng huquqliligi va huquqiy jihatdan himoya qilinishi taʼminlanadi.

Xususiy mulk daxlsizdir. Mulkdor oʻz mol-mulkidan qonunda nazarda tutilgan hollardan va tartibdan tashqari hamda sudning qaroriga asoslanmagan holda mahrum etilishi mumkin emas.`,
                clauses: [
                    {
                        clauseNumber: "1-qism",
                        text: "Fuqarolar farovonligini oshirishga qaratilgan Oʻzbekiston iqtisodiyotining negizini xilma-xil shakllardagi mulk tashkil etadi. Davlat bozor munosabatlarini rivojlantirish va halol raqobat uchun shart-sharoitlar yaratadi, isteʼmolchilarning huquqlari ustuvorligini hisobga olgan holda iqtisodiy faoliyat, tadbirkorlik va mehnat qilish erkinligini kafolatlaydi.",
                        blanketNorms: [
                            {
                                id: "bn-65-1-1",
                                codeName: "FK 164-modda",
                                fullName: "O'zbekiston Respublikasi Fuqarolik Kodeksi",
                                articleRef: "164-modda. Mulk huquqining tushunchasi",
                                category: "Fuqarolik Huquqi",
                                relationType: "Asosiy Blanket norma",
                                originalText: "Mulk huquqi shaxsning o'ziga tegishli mol-mulkka o'z xohishi bilan va o'z manfaatlarini ko'zlab egalik qilish, undan foydalanish va uni tasarruf etish borasidagi qonun bilan e'tirof etiladigan va muhofaza qilinadigan huquqidir.",
                                explanation: "Ushbu norma Konstitutsiyaning 65-moddasi 1-qismida nazarda tutilgan 'xilma-xil shakllardagi mulk' tushunchasining mazmuni va mulkdorning vakolatlarini aniq belgilab beradi. Konstitutsiya tamoyilni e'lon qiladi, FK 164-modda esa mulk huquqining moddiy tarkibini (egalik, foydalanish, tasarruf etish) aniqlaydi.",
                                practical: "Amaliyotda har qanday mulk shakli (xususiy, davlat, munitsipal) ushbu uchta vakolat doirasida bir xil fuqarolik-huquqiy maqomga ega bo'ladi."
                            },
                            {
                                id: "bn-65-1-2",
                                codeName: "Raqobat to'g'risidagi Qonun (O'RQ-898)",
                                fullName: "O'zbekiston Respublikasining 'Raqobat to'g'risida'gi Qonuni (Yangi tahriri)",
                                articleRef: "8-modda. Halol raqobat va insofsiz raqobatni taqiqlash",
                                category: "Iqtisodiy Huquq",
                                relationType: "Tartibga soluvchi havola",
                                originalText: "Insofsiz raqobatga, shu jumladan tovar yoki moliya bozorida ustun mavqeni suiste'mol qilishga, xo'jalik yurituvchi sub'ektlar tomonidan raqobatni cheklovchi kelishuvlar hamda til biriktirishlarni amalga oshirishga yo'l qo'yilmaydi.",
                                explanation: "Konstitutsiyadagi 'davlat halol raqobat uchun shart-sharoitlar yaratadi' degan blanket norma to'g'ridan-to'g'ri 'Raqobat to'g'risida'gi Qonunning 8-moddasi va Antimonopol qo'mita vakolatlari bilan bog'lanadi.",
                                practical: "Monopoliyaga qarshi organ ushbu blanket norma asosida bozorda sun'iy narx oshirish yoki asossiz ustunlikni cheklash huquqiga ega."
                            },
                            {
                                id: "bn-65-1-3",
                                codeName: "Iste'molchilar huquqini himoya qilish Qonuni",
                                fullName: "O'zbekiston Respublikasining 'Iste'molchilarning huquqlarini himoya qilish to'g'risida'gi Qonuni",
                                articleRef: "4-modda. Iste'molchilarning asosiy huquqlari",
                                category: "Iste'molchi Huquqi",
                                relationType: "Himoya mexanizmi",
                                originalText: "Iste'molchilar tovar (ish, xizmat) haqida haqqoniy va to'liq ma'lumot olish, tovar (ish, xizmat)ni erkin tanlash va uning lozim darajadagi sifatiga ega bo'lish huquqiga egadirlar.",
                                explanation: "Konstitutsiyadagi 'iste'molchilarning huquqlari ustuvorligi' tamoyili ushbu qonun orqali ijro etiladi. Tadbirkorlik erkinligi iste'molchi huquqlaridan ustun bo'lishi mumkin emas.",
                                practical: "Nushoq tovar sotilganda iste'molchi tovar qiymatini qaytarish yoki almashtirishni sud va Monopoliyaga qarshi organdan talab qila oladi."
                            }
                        ]
                    },
                    {
                        clauseNumber: "2-qism",
                        text: "Oʻzbekiston Respublikasida barcha mulk shakllarining teng huquqliligi va huquqiy jihatdan himoya qilinishi taʼminlanadi.",
                        blanketNorms: [
                            {
                                id: "bn-65-2-1",
                                codeName: "FK 165-modda",
                                fullName: "O'zbekiston Respublikasi Fuqarolik Kodeksi",
                                articleRef: "165-modda. Barcha mulk shakllarining teng huquqliligi",
                                category: "Fuqarolik Huquqi",
                                relationType: "To'g'ridan-to'g me'yor",
                                originalText: "O'zbekiston Respublikasida xususiy mulk hamda ommaviy (davlat) mulk tan olinadi va bir xilda himoya qilinadi. Davlat barcha mulk shakllarining rivojlanishi uchun teng sharoitlar yaratadi hamda ularning daxlsizligini kafolatlaydi.",
                                explanation: "Konstitutsiyadagi 'barcha mulk shakllarining teng huquqliligi' blanket normasi davlat mulki va xususiy mulkka imtiyoz berishda kamsitishga yo'l qo'yilmasligini kafolatlaydi.",
                                practical: "Sud ishlarida Davlat organi va oddiy Fuqaro mulkdor sifatida mutlaq teng huquqqa ega bo'ladi."
                            },
                            {
                                id: "bn-65-2-2",
                                codeName: "Xususiy mulkni himoya qilish Qonuni (O'RQ-336)",
                                fullName: "O'zbekiston Respublikasining 'Xususiy mulkni himoya qilish va mulkdorlar huquqlarining kafolatlari to'g'risida'gi Qonuni",
                                articleRef: "2-modda. Xususiy mulk huquqining daxlsizligi va tengligi",
                                category: "Xususiy Huquq",
                                relationType: "Maxsus kafolat",
                                originalText: "Davlat xususiy mulk huquqi amal qilishining daxlsizligini kafolatlaydi. Davlat organlarining xususiy mulkdorlar huquqlarini cheklovchi qarorlar chiqarishiga yo'l qo'yilmaydi.",
                                explanation: "Mulk shakllarining teng himoyasi prinsipi doirasida ushbu qonun xususiy mulkdorga davlat aralashuvidan himoyalanish uchun aniq huquqiy vositalarni beradi.",
                                practical: "Davlat idorasi xususiy mulkdorning mol-mulkini noqonuniy musodara qila olmaydi, aks holda mansabdor shaxs jinoiy va moddiy javobgar bo'ladi."
                            }
                        ]
                    },
                    {
                        clauseNumber: "3-qism",
                        text: "Xususiy mulk daxlsizdir. Mulkdor oʻz mol-mulkidan qonunda nazarda tutilgan hollardan va tartibdan tashqari hamda sudning qaroriga asoslanmagan holda mahrum etilishi mumkin emas.",
                        blanketNorms: [
                            {
                                id: "bn-65-3-1",
                                codeName: "FK 199, 206-moddalar",
                                fullName: "O'zbekiston Respublikasi Fuqarolik Kodeksi",
                                articleRef: "206-modda. Mulkdorning huquqlari bekor qilinishida zararni qoplash",
                                category: "Fuqarolik Huquqi",
                                relationType: "Tovon va kompensatsiya blanket normasi",
                                originalText: "Mulk huquqining bekor qilinishiga olib keluvchi qonun hujjatlari qabul qilingan taqdirda, ushbu hujjatlarni qabul qilish natijasida mulkdorga yetkazilgan zararlar, shu jumladan mol-mulkning qiymati davlat tomonidan to'liq qoplanadi.",
                                explanation: "Konstitutsiyadagi 'sud qarorisiz mahrum etilishi mumkin emas' degan qoida FK 206-moddasi bilan birga qo'llaniladi. Mulk faqat jamoat ehtiyoji uchun va FAQAT oldindan bozor qiymatida kompensatsiya to'langan holda olinishi mumkin.",
                                practical: "'Snos' (buzilish) holatlarida mulkdorga bozor qiymatidagi kompensatsiya va zararlar to'liq to'lanmagunicha sud uy-joyni olib qo'yish haqida qaror chiqara olmaydi."
                            },
                            {
                                id: "bn-65-3-2",
                                codeName: "O'RQ-781 Qonuni (Snos Qonuni)",
                                fullName: "O'zbekiston Respublikasining 'Yer uchastkalarini kompensatsiya evaziga jamoat ehtiyojlari uchun olib qo'yish tartib-taomillari to'g'risida'gi Qonuni",
                                articleRef: "4, 5-moddalar. Kompensatsiyaning turlari va oshkoraligi",
                                category: "Yer va Mulk Huquqi",
                                relationType: "Tartib-taomil blanket normasi",
                                originalText: "Yer uchastkalarini jamoat ehtiyojlari uchun olib qo'yishga Oliy Majlis Qonunchilik palatasining yoki tegishli Xalq deputatlari Kengashining qaroriga asosan, faqat kompensatsiya to'liq va oldindan berilgandan keyin yo'l qo'yiladi.",
                                explanation: "Konstitutsiyaning 65-moddasi 3-qismidagi daxlsizlik kafolati ushbu qonunda belgilangan 'ochiq ovoz berish', 'deputatlar roziligi' va 'bozor baholovchi sertifikati' talablari orqali amalga oshiriladi.",
                                practical: "Hokimiyat bir tomonlama 'qaror' bilan fuqaroning mulkini olib qo'ya olmaydi; masala deputatlar Kengashida ko'rilib, sud orqali hal etiladi."
                            },
                            {
                                id: "bn-65-3-3",
                                codeName: "FPK 26-modda",
                                fullName: "O'zbekiston Respublikasi Fuqarolik Protsessual Kodeksi",
                                articleRef: "26-modda. Sudlovga tegishlilik",
                                category: "Protsessual Huquq",
                                relationType: "Sud vakolati blanket normasi",
                                originalText: "Mulk huquqini bekor qilish, mol-mulkni olib qo'yish va rekvizitsiya qilish bilan bog'liq barcha nizolar fuqarolik ishlari bo'yicha sudlar hamda tumanlararo iqtisodiy sudlar tomonidan ko'rib chiqiladi.",
                                explanation: "Konstitutsiyadagi 'sud qaroriga asoslanmagan holda mahrum etilishi mumkin emas' qoidasi ushbu protsessual normani ishga tushiradi.",
                                practical: "Ijro hokimiyati (hokimlik, soliq, militsiya) mulkni tortib olish huquqiga ega emas, faqat sud ijro varaqasi asosida harakat qila oladi."
                            }
                        ]
                    }
                ]
            },
            {
                id: 66,
                number: "66-MODDA",
                title: "Mulkdorning Vakolatlari va Ularni Amalga Oshirish Chegaralari",
                constitutionalText: `Mulkdor oʻziga tegishli boʻlgan mol-mulkka oʻz xohishicha egalik qiladi, undan foydalanadi va uni tasarruf etadi. Mol-mulkdan foydalanish atrof-muhitga zarar yetkazmasligi, boshqa shaxslarning, jamiyat va davlatning huquqlarini hamda qonuniy manfaatlarini buzmasligi kerak.`,
                clauses: [
                    {
                        clauseNumber: "1-qism",
                        text: "Mulkdor oʻziga tegishli boʻlgan mol-mulkka oʻz xohishicha egalik qiladi, undan foydalanadi va uni tasarruf etadi.",
                        blanketNorms: [
                            {
                                id: "bn-66-1-1",
                                codeName: "FK 172, 173, 174-moddalar",
                                fullName: "O'zbekiston Respublikasi Fuqarolik Kodeksi",
                                articleRef: "172-modda. Egalik qilish, foydalanish va tasarruf etish huquqi",
                                category: "Fuqarolik Huquqi",
                                relationType: "Klassik huquqlar triadalari",
                                originalText: "Egalik qilish huquqi — mol-mulkni amalda egallab turishning huquqiy ta'minlangan imkoniyatidir. Foydalanish huquqi — mol-mulkdan uning foydali xossalarini ajratib olish imkoniyatidir. Tasarruf etish huquqi — mol-mulkning huquqiy qismatining tayinlash imkoniyatidir.",
                                explanation: "Konstitutsiyaviy uchlik (egalik qilish, foydalanish, tasarruf etish) FK 172-moddasida batafsil izohlanadi. Mulkdor o'z uyi, mashinasi yoki aksiyalarini sotishi, hadya qilishi yoki garovga qo'yishi mumkin.",
                                practical: "Mulkdor o'z buyumini sotmoqchi bo'lsa, hech bir davlat organining ruxsatini olishi talab etilmaydi (qonunda maxsus belgilangan litsenziyalangan ob'ektlardan tashqari)."
                            },
                            {
                                id: "bn-66-1-2",
                                codeName: "FK 182-modda",
                                fullName: "O'zbekiston Respublikasi Fuqarolik Kodeksi",
                                articleRef: "182-modda. Mulk huquqi vujudga kelishining asoslari",
                                category: "Fuqarolik Huquqi",
                                relationType: "Vujudga kelish manbasi",
                                originalText: "Mulk huquqi oldi-sotdi, almashish, hadya shartnomalari, meros bo'lib o'tish, bitimlar hamda qonunga zid bo'lmagan boshqa harakatlar asosida vujudga keladi.",
                                explanation: "Mulkdor o'z mol-mulkini o'z xohishicha tasarruf etishi uchun avvalo u ushbu 182-moddada ko'rsatilgan qonuniy asosda ega bo'lgan bo'lishi lozim.",
                                practical: "Ko'chmas mulkka egalik va tasarruf huquqi davlat ro'yxatidan o'tkazilgan (Kadastr) paytdan e'tiboran kuchga kiradi."
                            }
                        ]
                    },
                    {
                        clauseNumber: "2-qism",
                        text: "Mol-mulkdan foydalanish atrof-muhitga zarar yetkazmasligi, boshqa shaxslarning, jamiyat va davlatning huquqlarini hamda qonuniy manfaatlarini buzmasligi kerak.",
                        blanketNorms: [
                            {
                                id: "bn-66-2-1",
                                codeName: "Ekologiya Kodeksi va Qonunlar",
                                fullName: "O'zbekiston Respublikasining 'Tabiatni muhofaza qilish to'g'risida'gi Qonuni",
                                articleRef: "19-modda. Korxonalar va mulkdorlarning ekologik majburiyatlari",
                                category: "Ekologik Huquq",
                                relationType: "Cheklovchi blanket norma",
                                originalText: "Mulkdorlar va xo'jalik yurituvchi sub'ektlar o'z faoliyatida atrof-muhitni ifloslantirmaslik, ekologik normativlarga rioya etish va tabiatga zarar yetkazmaslik majburiyatini oladilar.",
                                explanation: "Konstitutsiyadagi 'atrof-muhitga zarar yetkazmaslik' talabi mulk huquqi mutlaq emasligini va ekologik cheklovlarga ega ekanligini ko'rsatadi.",
                                practical: "Shaxs o'ziga tegishli xususiy yerda zaharli kimyoviy chiqindilarni noqonuniy saqlasa, mulkdor bo'lishiga qaramay jinoiy va ma'muriy javobgarlikka tortiladi."
                            },
                            {
                                id: "bn-66-2-2",
                                codeName: "FK 990-modda",
                                fullName: "O'zbekiston Respublikasi Fuqarolik Kodeksi",
                                articleRef: "990-modda. Zarar yetkazganlik uchun javobgarlikning umumiy asoslari",
                                category: "Fuqarolik Huquqi",
                                relationType: "Fuqarolik-huquqiy javobgarlik",
                                originalText: "Fuqaro yoki yuridik shaxsning mol-mulkidan foydalanishi natijasida boshqa shaxsga, jamiyatga yoki davlatga yetkazilgan zarar uni yetkazgan shaxs tomonidan to'liq hajmda qoplanishi shart.",
                                explanation: "Konstitutsiyaning 66-moddasi 2-qismidagi qo'shnilar va jamiyat huquqlarini buzmaslik prinsipi ushbu FK 990-moddasi bilan delimitatsiya qilinadi.",
                                practical: "Kvartira mulkdori ozining xonadonida ta'mirlash ishlarini olib borib, pastdagi qo'shnisining uyini suv bossa, moddiy zararni to'liq qoplab beradi."
                            },
                            {
                                id: "bn-66-2-3",
                                codeName: "Shaharsozlik Kodeksi 10-modda",
                                fullName: "O'zbekiston Respublikasi Shaharsozlik Kodeksi",
                                articleRef: "10-modda. Bino va inshootlar qurishda shaharsozlik hamda qo'shnichilik huquqi",
                                category: "Shaharsozlik Huquqi",
                                relationType: "Texnik-huquqiy cheklov",
                                originalText: "Mulkdor o'z yer uchastkasida inshoot qurishda qo'shni binolarning yorug'lik tushishi (insolyatsiya), yong'in xavfsizligi hamda seysmik normativlariga amal qilishi shart.",
                                explanation: "O'z mulkidan foydalanish boshqalarga xalaqit bermasligi lozim degan konstitutsiyaviy norma shaharsozlik normalarida o'z ifodasini topadi.",
                                practical: "Qo'shnisining derazasini butunlay tosh devor bilan tosib qo'yadigan noqonuniy bino qurgan mulkdorning ob'ekti sud qarori bilan buzdiriladi."
                            }
                        ]
                    }
                ]
            },
            {
                id: 67,
                number: "67-MODDA",
                title: "Investitsiyaviy Muhit, Tadbirkorlik Erkinligi va Iqtisodiy Makon Birligi",
                constitutionalText: `Davlat qulay investitsiyaviy va ishbilarmonlik muhitini taʼminlaydi.
Tadbirkorlar qonunchilikka muvofiq har qanday faoliyatni amalga oshirishga va oʻz faoliyati yoʻnalishlarini mustaqil ravishda tanlashga haqli.
Oʻzbekiston Respublikasi hududida iqtisodiy makon birligi, tovarlar, xizmatlar, mehnat resurslari va moliyaviy mablagʻlarning erkin harakatlanishi kafolatlanadi.
Monopol faoliyat qonun bilan tartibga solinadi va cheklanadi.`,
                clauses: [
                    {
                        clauseNumber: "1-qism",
                        text: "Davlat qulay investitsiyaviy va ishbilarmonlik muhitini taʼminlaydi.",
                        blanketNorms: [
                            {
                                id: "bn-67-1-1",
                                codeName: "Investitsiyalar to'g'risidagi Qonun (O'RQ-598)",
                                fullName: "O'zbekiston Respublikasining 'Investitsiyalar va investitsiya faoliyati to'g'risida'gi Qonuni",
                                articleRef: "19-modda. Investorlar huquqlarining kafolatlari",
                                category: "Investitsiya Huquqi",
                                relationType: "Davlat kafolati blanket normasi",
                                originalText: "Qonunchilikka investor uchun noqulay o'zgartishlar kiritilganda, investorlarga 10 yil davomida investitsiya qilingan sanadagi amalda bo'lgan qonunchilikni qo'llash (krokuror / kafolat davri) huquqi beriladi.",
                                explanation: "Konstitutsiyaviy 'qulay investitsiyaviy muhit' kafolati ushbu qonundagi 'Kafolat davri (stabilizatsiya me'yori)' orqali mustahkamlanadi.",
                                practical: "Xorijiy investor investitsiya kiritgandan so'ng soliq stavkalari oshirilsa, u 10 yil davomida eski soliq stavkasi bo'yicha to'lov qilish huquqiga ega."
                            },
                            {
                                id: "bn-67-1-2",
                                codeName: "Tadbirkorlik kafolatlari Qonuni (O'RQ-328)",
                                fullName: "O'zbekiston Respublikasining 'Tadbirkorlik faoliyati erkinligining kafolatlari to'g'risida'gi Qonuni",
                                articleRef: "18-modda. Tadbirkorlik sub'ektlari faoliyatiga aralashmaslik",
                                category: "Tadbirkorlik Huquqi",
                                relationType: "Himoya mezoni",
                                originalText: "Davlat organlari va ularning mansabdor shaxslari tadbirkorlik sub'ektlarining qonunchilikka muvofiq amalga oshirayotgan faoliyatiga aralashishga haqli emas.",
                                explanation: "Ishbilarmonlik muhitini yaratish bo'yicha Konstitutsiyaviy topshiriq mansabdor shaxslarning noqonuniy tekshiruvlarini taqiqlaydi.",
                                practical: "Tekshiruvchi organlar Biznes-ombudsman va maxsus elektron tizimda ro'yxatdan o'tmay turib tadbirkor korxonasiga kirishi taqiqlanadi."
                            }
                        ]
                    },
                    {
                        clauseNumber: "2-qism",
                        text: "Tadbirkorlar qonunchilikka muvofiq har qanday faoliyatni amalga oshirishga va oʻz faoliyati yoʻnalishlarini mustaqil ravishda tanlashga haqli.",
                        blanketNorms: [
                            {
                                id: "bn-67-2-1",
                                codeName: "FK 24-modda",
                                fullName: "O'zbekiston Respublikasi Fuqarolik Kodeksi",
                                articleRef: "24-modda. Fuqaroning tadbirkorlik faoliyati",
                                category: "Fuqarolik Huquqi",
                                relationType: "Tadbirkorlik sub'ektligi",
                                originalText: "Fuqaro davlat ro'yxatidan o'tkazilgan paytdan e'tiboran tadbirkorlik faoliyati bilan shug'ullanish huquqiga ega bo'ladi.",
                                explanation: "Tadbirkor faoliyat turini tanlashda qonun bilan taqiqlanmagan har qanday sohaga keta olishi ushbu kodeks normasi bilan tartibga solinadi.",
                                practical: "YPX yoki Soliq organi tadbirkorga 'Siz faqat shirinlik soting, kiyim sotmang' deb cheklov qo'ya olmaydi."
                            },
                            {
                                id: "bn-67-2-2",
                                codeName: "Litsenziyalash to'g'risidagi Qonun (O'RQ-701)",
                                fullName: "O'zbekiston Respublikasining 'Litsenziyalash, ruxsat berish va xabardor qilish tartib-taomillari to'g'risida'gi Qonuni",
                                articleRef: "7-modda. Litsenziyalanadigan faoliyat turlarining cheklanganligi",
                                category: "Ma'muriy Huquq",
                                relationType: "Ruxsat beruvchi blanket norma",
                                originalText: "Faqat ushbu Qonun bilan belgilangan ro'yxatdagi faoliyat turlari litsenziyalanishi lozim. Ushbu ro'yxatda bo'lmagan faoliyat turlari erkin va ruxsatnomalarsiz amalga oshiriladi.",
                                explanation: "Konstitutsiyadagi 'har qanday faoliyatni amalga oshirish' huquqi faqat maxsus xavfli sohalarda (tibbiyot, qurol, bank) litsenziya olish talabini bildiradi.",
                                practical: "IT dasturlash yoki konsalting xizmati ko'rsatish uchun hech qanday litsenziya yoki maxsus ruxsatnoma talab qilinmaydi."
                            }
                        ]
                    },
                    {
                        clauseNumber: "3-qism",
                        text: "Oʻzbekiston Respublikasi hududida iqtisodiy makon birligi, tovarlar, xizmatlar, mehnat resurslari va moliyaviy mablagʻlarning erkin harakatlanishi kafolatlanadi.",
                        blanketNorms: [
                            {
                                id: "bn-67-3-1",
                                codeName: "Bojxona Kodeksi 6-modda",
                                fullName: "O'zbekiston Respublikasi Bojxona Kodeksi",
                                articleRef: "6-modda. Yagona bojxona hududi va iqtisodiy makon",
                                category: "Bojxona Huquqi",
                                relationType: "Hududiy makon birligi",
                                originalText: "O'zbekiston Respublikasining bojxona hududi yagonadir. O'zbekiston hududida viloyatlararo va shaharlararo ichki bojxona postlari va tovarlar harakatiga to'siqlarni o'rnatish taqiqlanadi.",
                                explanation: "Konstitutsiyaviy iqtisodiy makon birligi viloyat hokimlariga o'z hududidan boshqa viloyatga tovar (masalan, g'alla, go'sht, sement) olib chiqishni taqiqlashni man etadi.",
                                practical: "Muayyan viloyat hokimligi 'Bizning viloyatdan un olib chiqib ketilmasin' deb noqonuniy post qo'ysa, bu respublika Konstitutsiyasiga mutlaq ziddir."
                            },
                            {
                                id: "bn-67-3-2",
                                codeName: "Valyutani tartibga solish Qonuni (O'RQ-573)",
                                fullName: "O'zbekiston Respublikasining 'Valyutani tartibga solish to'g'risida'gi Qonuni",
                                articleRef: "18-modda. Kapital harakati va moliyaviy o'tkazmalar erkinligi",
                                category: "Moliyaviy Huquq",
                                relationType: "Kapital erkinligi",
                                originalText: "O'zbekiston Respublikasi hududida rezidentlar va norezidentlar o'rtasida moliyaviy mablag'lar hamda pul o'tkazmalari noqonuniy cheklovlarsiz amalga oshiriladi.",
                                explanation: "Moliyaviy mablag'larning erkin harakatlanishi doirasida banklar orqali pullarni erkin o'tkazish va valyuta konvertatsiyasi kafolatlanadi.",
                                practical: "Tadbirkor o'z hisob raqamidagi pullarini mamlakat ichida erkin o'tkazishi yoki chet elga tovar uchun to'lov sifatida cheklovlarsiz yo'naltirishi mumkin."
                            },
                            {
                                id: "bn-67-3-3",
                                codeName: "Mehnat Kodeksi 12, 13-moddalar",
                                fullName: "O'zbekiston Respublikasi Mehnat Kodeksi (Yangi tahriri)",
                                articleRef: "12-modda. Mehnat va mashg'ulotlar erkinligi",
                                category: "Mehnat Huquqi",
                                relationType: "Mehnat resurslari harakati",
                                originalText: "Har bir shaxs mehnat qilish, ish joyini va kasbini erkin tanlash huquqiga ega. O'zbekiston hududida fuqarolarni ma'lum hududda ishlashga majburlash va propiska bo'yicha kamsitish taqiqlanadi.",
                                explanation: "Mehnat resurslarining erkin harakatlanishi har qanday fuqaroning mamlakatning istalgan hududida to'siqsiz ishga joylashishini anglatadi.",
                                practical: "Toshkent shahrida ishlash uchun doimiy Toshkent propiskasini talab qilish amaliyotining bekor qilinishi ushbu normaning yorqin misolidir."
                            }
                        ]
                    },
                    {
                        clauseNumber: "4-qism",
                        text: "Monopol faoliyat qonun bilan tartibga solinadi va cheklanadi.",
                        blanketNorms: [
                            {
                                id: "bn-67-4-1",
                                codeName: "Raqobat Qonuni (O'RQ-898) 13, 14-moddalar",
                                fullName: "O'zbekiston Respublikasining 'Raqobat to'g'risida'gi Qonuni",
                                articleRef: "13-modda. Ustun mavqega ega bo'lgan sub'ektlarning harakatlarini cheklash",
                                category: "Antimonopol Huquq",
                                relationType: "Cheklovchi asosiy norma",
                                originalText: "Bozorda ustun mavqeni egallab turgan korxonalar tomonidan asossiz yuqori narxlarni belgilash, tovarlarni muomaladan chiqarib tashlash va kamsituvchi shartlarni majburlab tiqishtirish taqiqlanadi.",
                                explanation: "Monopol faoliyat mutlaq taqiqlanmaydi, balki 'tartibga solinadi va cheklanadi'. Tabiash monopoliyalar (gaz, suv, temir yo'l) davlat nazoratida ishlaydi.",
                                practical: "Monopol korxona (masalan, Uzbekistan Airways yoki UzAuto Motors) narxlarni asossiz oshirsa, Antimonopol qo'mita unga nisbatan ma'muriy jarima va narxni tushirish talabini qo'yadi."
                            },
                            {
                                id: "bn-67-4-2",
                                codeName: "Tabiiy monopoliyalar to'g'risidagi Qonun",
                                fullName: "O'zbekiston Respublikasining 'Tabiiy monopoliyalar to'g'risida'gi Qonuni",
                                articleRef: "4, 7-moddalar. Davlat tomonidan narxlarni tartibga solish",
                                category: "Iqtisodiy Huquq",
                                relationType: "Tarif va nazorat blanket normasi",
                                originalText: "Tabiiy monopoliya sub'ektlarining tovarlari va xizmatlariga tariflar hamda narxlar davlat vakolatli organi tomonidan tasdiqlanadi va tartibga solinadi.",
                                explanation: "Raqobat mavjud bo'lmagan sohalarda (elektr tarmoqlari, gaz uzatish) davlat monopoliyaning salbiy ta'sirini tariflarni chegaralash orqali jilovlaydi.",
                                practical: "Aholi uchun elektr energiyasi yoki suv tarifi monopol korxona xohshi bilan emas, hukumat qarori va jamoatchilik muhokamasi bilan belgilanadi."
                            }
                        ]
                    }
                ]
            },
            {
                id: 68,
                number: "68-MODDA",
                title: "Tabiiy Resurslarning Umummilliy Boyligi va Yergilik Mulk Maqomi",
                constitutionalText: `Yer, yer osti boyliklari, suv, oʻsimlik va hayvonot dunyosi hamda boshqa tabiiy resurslar umummilliy boylikdir, ulardan oqilona foydalanish zarur va ular davlat muhofazasidadir.
Yer qonunda nazarda tutilgan hamda undan oqilona foydalanishni va uni umummilliy boylik sifatida muhofaza qilishni taʼminlovchi shartlar asosida va tartibda xususiy mulk boʻlishi mumkin.`,
                clauses: [
                    {
                        clauseNumber: "1-qism",
                        text: "Yer, yer osti boyliklari, suv, oʻsimlik va hayvonot dunyosi hamda boshqa tabiiy resurslar umummilliy boylikdir, ulardan oqilona foydalanish zarur va ular davlat muhofazasidadir.",
                        blanketNorms: [
                            {
                                id: "bn-68-1-1",
                                codeName: "Yer Kodeksi 1, 3-moddalar",
                                fullName: "O'zbekiston Respublikasi Yer Kodeksi",
                                articleRef: "1-modda. Yer qonunchiligining asosiy vazifalari",
                                category: "Yer Huquqi",
                                relationType: "Tabiiy resurslar davlat muhofazasi",
                                originalText: "Yer O'zbekiston Respublikasi xalqining milliy boyligidir. Yer fondi muayyan maqsadlarga mo'ljallanganligiga qarab davlat tomonidan muhofaza qilinadi va oqilona foydalanilishi shart.",
                                explanation: "Konstitutsiyaviy 'umummilliy boylik' tamoyili Yer Kodeksida yerdan unumli foydalanish, uning undorligini oshirish va noqonuniy egallashni taqiqlash mexanizmi orqali ta'minlanadi.",
                                practical: "Qishloq xo'jaligi yerlarini noqonuniy qurilish uchun egallab olish O'zbekiston Respublikasi Jinoyat Kodeksining 229-1-moddasi bo'yicha og'ir jinoyat hisoblanadi."
                            },
                            {
                                id: "bn-68-1-2",
                                codeName: "Yer osti boyliklari to'g'risidagi Qonun (O'RQ-939)",
                                fullName: "O'zbekiston Respublikasining 'Yer osti boyliklari to'g'risida'gi Qonuni (Yangi tahriri)",
                                articleRef: "5-modda. Yer osti boyliklariga mulkchilik",
                                category: "Ekologik va Kon Huquqi",
                                relationType: "Eksklyuziv davlat mulki",
                                originalText: "Yer osti boyliklari — oltin, neft, gaz, minerallar davlatga tegishli umummilliy boylikdir. Ulardan foydalanish faqat maxsus litsenziyalar va kon ajratmalari asosida amalga oshiriladi.",
                                explanation: "Yerdan farqli o'laroq, yer osti boyliklari xususiy mulk bo'la olmaydi. Ular to'liqligicha davlat mulki va muhofazasidadir.",
                                practical: "O'z xususiy yerida oltin yoki neft koni topgan fuqaro kon ustidan mulk huquqiga ega bo'lmaydi; u davlatga tegishli bo'lib, unga topilma uchun mukofot to'lanadi."
                            },
                            {
                                id: "bn-68-1-3",
                                codeName: "Suv va suvdan foydalanish to'g'risidagi Qonun",
                                fullName: "O'zbekiston Respublikasining 'Suv va suvdan foydalanish to'g'risida'gi Qonuni",
                                articleRef: "3, 18-moddalar. Suv resurslaridan oqilona foydalanish",
                                category: "Suv Huquqi",
                                relationType: "Oqilona foydalanish blanket normasi",
                                originalText: "Suv resurslari umummilliy boylik bo'lib, suv ob'ektlarini ifloslantirish, asossiz isrof qilish hamda suv obyektlarining muhofaza zonalarini buzish taqiqlanadi.",
                                explanation: "Suvdan oqilona foydalanish bo'yicha konstitutsiyaviy talab suv tejovchi texnologiyalarni (tomchilatib sug'orish) joriy etish majburiyatini yuklaydi.",
                                practical: "Daryo va kanallar boyida noqonuniy obyektlar qurgan mulkdorlarning inshootlari suv muhofaza zonasi qoidalariga ko'ra majburiy buzdiriladi."
                            },
                            {
                                id: "bn-68-1-4",
                                codeName: "O'simlik va Hayvonot dunyosi Qonunlari",
                                fullName: "O'zbekiston Respublikasining 'O'simlik dunyosini muhofaza qilish va undan foydalanish to'g'risida'gi Qonuni",
                                articleRef: "12, 15-moddalar. Qizil kitob va bio-xilma-xillik muhofazasi",
                                category: "Atrof-muhit Huquqi",
                                relationType: "Bio-muhofaza normasi",
                                originalText: "Noyob va yo'qolib ketish xavfi ostida turgan flora va fauna turlari davlat muhofazasidadir. Ularni kesish, ovlash yoki yo'q qilish taqiqlanadi.",
                                explanation: "Konstitutsiyadagi 'o'simlik va hayvonot dunyosi davlat muhofazasidadir' blanket normasi daraxtlarni noqonuniy kesganlik uchun moratoriy va jarimalar tizimini yaratadi.",
                                practical: "Katta yoshli qimmatbaho daraxtni noqonuniy keshgan shaxs har bir daraxt uchun tabiatga yetkazilgan millionlab so'mlik ziyonni to'laydi hamda ko'chat ekishga majbur qilinadi."
                            }
                        ]
                    },
                    {
                        clauseNumber: "2-qism",
                        text: "Yer qonunda nazarda tutilgan hamda undan oqilona foydalanishni va uni umummilliy boylik sifatida muhofaza qilishni taʼminlovchi shartlar asosida va tartibda xususiy mulk boʻlishi mumkin.",
                        blanketNorms: [
                            {
                                id: "bn-68-2-1",
                                codeName: "Qishloq xo'jaligiga mo'ljallanmagan yerlarni xususiylashtirish Qonuni (O'RQ-728)",
                                fullName: "O'zbekiston Respublikasining 'Qishloq xo'jaligiga mo'ljallanmagan yer uchastkalarini xususiylashtirish to'g'risida'gi Qonuni",
                                articleRef: "10, 13-moddalar. Yerni xususiylashtirish ob'ektlari va shartlari",
                                category: "Yer va Xususiy Huquq",
                                relationType: "Inqilobiy blanket norma",
                                originalText: "O'zbekiston Respublikasi fuqarolari va yuridik shaxslari o'zlariga tegishli bino va inshootlar joylashgan yer uchastkalarini yoki tadbirkorlik uchun ajratilgan yerlarni xususiylashtirish huquqiga ega.",
                                explanation: "Ushbu norma 2023-yilgi Konstitutsiyaning eng muhim islohotlaridan biridir. Ilgari yer faqat davlatga tegishli bo'lgan bo'lsa, endilikda qishloq xo'jaligiga mo'ljallanmagan yerlar xususiy mulk bo'lishi mumkin.",
                                practical: "Fuqaro o'zining xususiy uyi joylashgan yerni auksion yoki sotib olish orqali xususiylashtirib, unga xususiy mulk huquqi guvohnomasini (Kadastr) olishi mumkin."
                            },
                            {
                                id: "bn-68-2-2",
                                codeName: "Yer Kodeksi 23, 36-moddalar",
                                fullName: "O'zbekiston Respublikasi Yer Kodeksi",
                                articleRef: "36-modda. Yer uchastkasiga bo'lgan huquqlar bekor qilinishining asoslari",
                                category: "Yer Huquqi",
                                relationType: "Shartli daxlsizlik va oqilona foydalanish",
                                originalText: "Yer uchastkasidan ketma-ket uch yil davomida belgilangan maqsadda foydalanilmaganda, shuningdek yerning undorligi va ekologik holati yomonlashishiga olib kelganda yerga bo'lgan huquq bekor qilinishi mumkin.",
                                explanation: "Konstitutsiyadagi 'yerdan oqilona foydalanishni ta'minlovchi shartlar asosida' degan qoida xususiy mulkka aylangan yer ham qat'iy maqsadda ishlatilishi shartligini bildiradi.",
                                practical: "Tadbirkor zavod qurish uchun olgan va xususiylashtirgan yerini yillar davomida qarovsiz tashlab qo'ysa va ekologik zarar keltirsa, sud yerdan foydalanish huquqini cheklashi yoki bekor qilishi mumkin."
                            }
                        ]
                    }
                ]
            }
        ];

        // Global State
        let expandedState = { 65: true, 66: true, 67: true, 68: true };

        // Initialize App
        window.addEventListener('DOMContentLoaded', () => {
            renderArticles();
        });

        // Render Articles HTML
        function renderArticles(filterQuery = '') {
            const container = document.getElementById('articlesContainer');
            container.innerHTML = '';

            const query = filterQuery.toLowerCase().trim();

            legalDatabase.forEach(article => {
                // Filter matching check
                let articleMatches = article.number.toLowerCase().includes(query) || 
                                     article.title.toLowerCase().includes(query) || 
                                     article.constitutionalText.toLowerCase().includes(query);

                let matchingClauses = article.clauses.filter(clause => {
                    let clauseMatches = clause.text.toLowerCase().includes(query);
                    let normMatches = clause.blanketNorms.some(norm => 
                        norm.codeName.toLowerCase().includes(query) ||
                        norm.fullName.toLowerCase().includes(query) ||
                        norm.articleRef.toLowerCase().includes(query) ||
                        norm.originalText.toLowerCase().includes(query) ||
                        norm.explanation.toLowerCase().includes(query)
                    );
                    return clauseMatches || normMatches || articleMatches;
                });

                if (query !== '' && matchingClauses.length === 0) {
                    return; // Skip if query doesn't match
                }

                const isExpanded = expandedState[article.id];

                const articleCard = document.createElement('div');
                articleCard.className = `glass-card rounded-2xl border transition-all duration-300 overflow-hidden ${isExpanded ? 'border-emerald-500/30 shadow-xl' : 'border-slate-800'}`;
                
                articleCard.innerHTML = `
                    <!-- Article Accordion Header -->
                    <div onclick="toggleArticle(${article.id})" class="p-6 sm:p-7 flex items-center justify-between cursor-pointer bg-slate-900/50 hover:bg-slate-900/80 transition border-b border-slate-800/80 group">
                        <div class="flex items-center space-x-4 sm:space-x-5">
                            <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-teal-500/10 border border-emerald-500/40 flex items-center justify-center font-black text-emerald-400 text-lg sm:text-xl group-hover:scale-105 transition-transform shadow-lg shadow-emerald-950/40">
                                ${article.id}
                            </div>
                            <div>
                                <div class="flex items-center gap-3">
                                    <span class="text-xs font-bold uppercase tracking-widest text-emerald-400 font-mono">${article.number}</span>
                                    <span class="text-xs px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-400 font-medium border border-slate-700">${article.clauses.length} ta qism</span>
                                </div>
                                <h3 class="text-lg sm:text-2xl font-bold text-white mt-1 group-hover:text-emerald-300 transition-colors">
                                    ${article.title}
                                </h3>
                            </div>
                        </div>
                        <div class="w-10 h-10 rounded-xl bg-slate-800/60 border border-slate-700/80 flex items-center justify-center text-slate-300 group-hover:text-emerald-400 group-hover:border-emerald-500/50 transition">
                            <i class="fa-solid ${isExpanded ? 'fa-chevron-up' : 'fa-chevron-down'} text-sm"></i>
                        </div>
                    </div>

                    <!-- Article Body Content -->
                    <div class="${isExpanded ? 'block' : 'hidden'} p-6 sm:p-8 space-y-8 divide-y divide-slate-800/80 bg-slate-950/40">
                        <!-- Full Constitutional Text Summary -->
                        <div class="p-5 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
                            <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-2">
                                <i class="fa-solid fa-book-open-reader text-gold-400"></i>
                                Konstitutsiyaviy Moddaning To'liq Matni
                            </h4>
                            <p class="text-slate-200 text-sm sm:text-base leading-relaxed whitespace-pre-line font-serif italic">
                                "${article.constitutionalText}"
                            </p>
                        </div>

                        <!-- Clauses Breakdown with Blanket Norms -->
                        <div class="pt-6 space-y-8">
                            <h4 class="text-sm font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-2">
                                <i class="fa-solid fa-diagram-project"></i>
                                Modda Qismlari va Tegishli Blanket Normalar Tahlili
                            </h4>

                            ${article.clauses.map((clause, idx) => `
                                <div class="space-y-4 bg-slate-900/40 p-5 sm:p-6 rounded-2xl border border-slate-800/80 hover:border-slate-700 transition">
                                    <div class="flex items-start gap-3">
                                        <span class="px-3 py-1 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-extrabold text-xs font-mono shrink-0 mt-0.5">
                                            ${clause.clauseNumber}
                                        </span>
                                        <p class="text-slate-100 font-medium text-base sm:text-lg leading-relaxed">
                                            ${clause.text}
                                        </p>
                                    </div>

                                    <!-- Blanket Norm Interactive Links -->
                                    <div class="mt-4 pt-4 border-t border-slate-800/60 space-y-3">
                                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
                                            <i class="fa-solid fa-link text-xs text-emerald-400"></i>
                                            Ushbu qismga bog'liq Blanket Normalar (Bosib batafsil ko'ring):
                                        </span>
                                        
                                        <div class="flex flex-wrap gap-2.5">
                                            ${clause.blanketNorms.map(norm => `
                                                <button onclick="openModal('${norm.id}')" 
                                                    class="blanket-tag inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-slate-800/90 hover:bg-emerald-950/80 text-emerald-300 hover:text-emerald-200 border border-emerald-500/30 hover:border-emerald-400 text-xs sm:text-sm font-semibold shadow-sm text-left">
                                                    <i class="fa-solid fa-scale-balanced text-emerald-400"></i>
                                                    <span>${norm.codeName}</span>
                                                    <span class="text-[10px] opacity-60 font-mono">(${norm.articleRef.split('.')[0]})</span>
                                                    <i class="fa-solid fa-arrow-up-right-from-square text-[10px] text-emerald-500"></i>
                                                </button>
                                            `).join('')}
                                        </div>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;

                container.appendChild(articleCard);
            });

            if (container.children.length === 0) {
                container.innerHTML = `
                    <div class="text-center py-16 glass-card rounded-2xl border border-slate-800 space-y-4">
                        <i class="fa-solid fa-file-circle-xmark text-5xl text-slate-600"></i>
                        <h3 class="text-lg font-bold text-slate-300">Siz qidirgan so'z bo'yicha hech qanday blanket norma topilmadi</h3>
                        <p class="text-sm text-slate-500">Iltimos, qidiruv kalit so'zini o'zgartiring (masalan: "FK", "Yer", "Raqobat", "65-modda")</p>
                    </div>
                `;
            }
        }

        // Toggle Accordion
        function toggleArticle(id) {
            expandedState[id] = !expandedState[id];
            renderArticles(document.getElementById('searchInput').value);
        }

        // Collapse / Expand All
        function toggleAllCards() {
            const allExpanded = Object.values(expandedState).every(v => v);
            Object.keys(expandedState).forEach(k => expandedState[k] = !allExpanded);
            renderArticles(document.getElementById('searchInput').value);
        }

        // Search Filter Logic
        function filterContent() {
            const query = document.getElementById('searchInput').value;
            renderArticles(query);
        }

        function filterContentMobile() {
            const query = document.getElementById('mobileSearchInput').value;
            renderArticles(query);
        }

        // Modal Controls
        function openModal(normId) {
            let foundNorm = null;

            // Search in DB
            for (let article of legalDatabase) {
                for (let clause of article.clauses) {
                    let match = clause.blanketNorms.find(n => n.id === normId);
                    if (match) {
                        foundNorm = match;
                        break;
                    }
                }
                if (foundNorm) break;
            }

            if (!foundNorm) return;

            // Populate Modal Fields
            document.getElementById('modalTitle').innerText = foundNorm.fullName;
            document.getElementById('modalLawSource').innerText = foundNorm.articleRef;
            document.getElementById('modalOriginalText').innerText = `"${foundNorm.originalText}"`;
            document.getElementById('modalExplanation').innerText = foundNorm.explanation;
            document.getElementById('modalPractical').innerText = foundNorm.practical;
            document.getElementById('modalCategoryBadge').innerText = foundNorm.category;
            document.getElementById('modalRelationBadge').innerText = foundNorm.relationType;

            // Show Modal
            const modal = document.getElementById('normModal');
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden'; // Disable page scrolling
        }

        function closeModal() {
            const modal = document.getElementById('normModal');
            modal.classList.add('hidden');
            document.body.style.overflow = 'auto'; // Re-enable page scrolling
        }

        // Copy Text Function
        function copyModalText() {
            const textToCopy = document.getElementById('modalOriginalText').innerText;
            
            // Clipboard fallback
            const dummy = document.createElement("textarea");
            document.body.appendChild(dummy);
            dummy.value = textToCopy;
            dummy.select();
            document.execCommand("copy");
            document.body.removeChild(dummy);

            // Toast message or alert substitute
            const copyBtn = event.currentTarget;
            const originalHTML = copyBtn.innerHTML;
            copyBtn.innerHTML = `<i class="fa-solid fa-check text-emerald-400"></i> Nusxalandi!`;
            setTimeout(() => {
                copyBtn.innerHTML = originalHTML;
            }, 2000);
        }

        // Close modal on ESC key
        window.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>
```
