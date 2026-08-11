import streamlit as st
import sys
import os

# Menyambungkan logika dan data
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from modules.audit_engine import run_gemini_audit
from kriteria_data import DATA_PROPER

# --- KONFIGURASI STATE MEMORI (TABULASI SKOR) ---
if 'skor_tabulasi' not in st.session_state:
    st.session_state.skor_tabulasi = {}

# Konfigurasi Halaman (Lebih lebar & elegan)
st.set_page_config(page_title="Sistem Asesmen PROPER Hijau", layout="wide", page_icon="🌿")

# ==========================================
# SUNTIKAN CSS KUSTOM UNTUK TAMPILAN ELEGAN & SCROLL DINAMIS
# ==========================================
st.markdown("""
    <style>
    /* Sembunyikan menu bawaan Streamlit untuk kesan aplikasi mandiri */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Styling Header Utama */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E3A8A; /* Biru Tua Elegan */
        padding-bottom: 0px;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #64748b;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    
    /* ========================================= */
    /* FITUR: MENGUBAH RADIO BUTTON MENJADI SCROLLABLE & STRICT 1 KOLOM */
    [data-testid="stSidebar"] [role="radiogroup"] {
        max-height: 300px; /* Batas tinggi dinamis */
        overflow-y: auto;  /* Munculkan scrollbar ke bawah */
        overflow-x: hidden; /* Matikan scroll menyamping */
        padding-right: 10px;
        border-top: 1px solid #f1f5f9;
        border-bottom: 1px solid #f1f5f9;
        padding-top: 10px;
        padding-bottom: 10px;
        
        /* PAKSA 1 KOLOM VERTIKAL */
        display: flex !important;
        flex-direction: column !important;
        flex-wrap: nowrap !important;
        gap: 4px; /* Jarak antar pilihan */
    }
    
    /* Pastikan setiap item mengambil lebar penuh agar tidak berjejer */
    [data-testid="stSidebar"] [role="radiogroup"] label {
        width: 100% !important;
        margin-right: 0 !important;
    }

    /* FITUR: MENGUBAH TABULASI SKOR MENJADI SCROLLABLE */
    .score-scroll-container {
        max-height: 250px; /* Batas tinggi dinamis */
        overflow-y: auto;  /* Munculkan scrollbar ke bawah */
        overflow-x: hidden;
        padding-right: 10px;
        margin-bottom: 15px;
    }
    .score-item {
        padding: 8px 0;
        border-bottom: 1px dashed #e2e8f0;
        font-size: 0.9rem;
        color: #334155;
    }
    .score-item:last-child {
        border-bottom: none;
    }

    /* Styling Scrollbar agar cantik dan modern */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track {
        background: transparent;
    }
    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }
    /* ========================================= */
    
    /* Kartu Hasil Penilaian (Score Card) */
    .score-card-green {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 6px solid #22c55e;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .score-card-red {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        border-left: 6px solid #ef4444;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .score-title {
        font-size: 0.9rem;
        color: #475569;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }
    .score-value {
        font-size: 2.8rem;
        font-weight: 900;
        color: #0f172a;
        margin: 0;
        line-height: 1;
    }
    
    /* Efek Hover pada Tombol Utama */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER APLIKASI ---
st.markdown('<div class="main-header">🌿 Asesmen - PROPER Hijau KLH</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Asisten Cerdas untuk Evaluasi Dokumen Keberlanjutan</div>', unsafe_allow_html=True)
st.markdown("---")


# --- MENU SIDEBAR: NAVIGASI BERJENJANG & JANGKAR WAKTU ---
st.sidebar.title("⚙️ Konfigurasi")

# 0. JANGKAR WAKTU: Pilih Siklus Penilaian PROPER (2 Tahun Audit)
siklus_proper = st.sidebar.selectbox(
    "🗓️ Siklus Penilaian PROPER:",
    ["2023/2024", "2024/2025", "2025/2026", "2026/2027", "2027/2028"],
    index=2,  # Default ke 2025/2026
    help="Menentukan batas kedaluwarsa dokumen dinamis (Renja, Laporan, dll)."
)

tahun_akhir = siklus_proper.split("/")[1]
st.sidebar.caption(f"📌 **Timeline Riil:** 1 Juli {int(tahun_akhir)-1} s.d. 30 Juni {tahun_akhir}")
st.sidebar.markdown("---")

# 1. Pilih Jenis Dokumen
jenis_dokumen = st.sidebar.selectbox("📂 1. Pilih Jenis Dokumen", list(DATA_PROPER.keys()))

# 2. Pilih Kategori (berdasarkan Jenis Dokumen)
kategori_list = list(DATA_PROPER[jenis_dokumen].keys())
kategori = st.sidebar.selectbox("📑 2. Pilih Kategori", kategori_list)

st.sidebar.markdown("---")
st.sidebar.markdown("**🎯 3. Pilih Kriteria Penilaian:**")

# Menarik daftar pertanyaan di dalam kategori yang dipilih
kriteria_dict = DATA_PROPER[jenis_dokumen][kategori]

if not kriteria_dict:
    st.sidebar.warning("Kriteria untuk kategori ini belum tersedia (sedang dibangun).")
    st.info("Pilih Kategori atau Dokumen lain, atau tambahkan kriteria baru di gudang data.")
else:
    pilihan_menu = list(kriteria_dict.keys()) 
    
    selected_no = st.sidebar.radio(
        "Daftar Kriteria:",
        options=pilihan_menu,
        format_func=lambda x: f"Kriteria {x}",
        label_visibility="collapsed" 
    )

    # --- SCOREBOARD (PAPAN SKOR) DI SIDEBAR ---
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Tabulasi Skor Sementara")
    total_skor = 0.0
    maks_skor = 0.0
    
    html_scores = '<div class="score-scroll-container">'
    
    for no, data in kriteria_dict.items():
        kunci_skor = f"{jenis_dokumen}_{kategori}_{no}"
        skor_item = st.session_state.skor_tabulasi.get(kunci_skor, 0.0)
        total_skor += skor_item
        maks_skor += data['skor_maksimal']
        
        if skor_item > 0:
            html_scores += f'<div class="score-item">✅ Q{no}: <strong>{skor_item}</strong> <span style="color:#94a3b8;">/ {data["skor_maksimal"]}</span></div>'
        else:
            html_scores += f'<div class="score-item">⏳ Q{no}: - <span style="color:#94a3b8;">/ {data["skor_maksimal"]}</span></div>'
            
    html_scores += '</div>'
    
    # Tampilkan List Tabulasi Skor ke layar Sidebar
    st.sidebar.markdown(html_scores, unsafe_allow_html=True)
            
    # Tampilkan Total Skor Statis di bagian paling bawah Sidebar
    st.sidebar.success(f"**TOTAL SKOR: {total_skor} / {maks_skor}**")


    # ==========================================
    # DASHBOARD UTAMA (EVALUASI)
    # ==========================================
    active_rubric = kriteria_dict[selected_no]

    # Navigasi Breadcrumb
    st.caption(f"📍 **Modul Aktif:** {jenis_dokumen} ➔ {kategori} ➔ Kriteria {selected_no}")
    st.header(active_rubric['judul'])

    # ==========================================
    # MENAMPILKAN SEMUA DATA RUBRIK
    # ==========================================
    with st.expander("📖 Lihat Panduan Penilaian & Rubrik PROPER LHK", expanded=False):
        # Menampilkan Detail / Aspek Penilaian
        st.info(active_rubric.get('detail_ui', 'Aspek penilaian tidak tersedia.'))
        
        st.markdown("#### 🎯 Kriteria & Parameter Sistem")
        st.markdown(f"- **Fokus Analisis AI:** {active_rubric.get('kriteria_ai', '-')}")
        st.markdown(f"- **Skor Maksimal:** `{active_rubric.get('skor_maksimal', 0.0)}`")
        
        st.markdown("#### ⚙️ Aturan Skoring & Validasi Waktu")
        # Menampilkan rubrik_ai ke layar agar transparan
        st.warning(active_rubric.get('rubrik_ai', 'Aturan skoring tidak tersedia.'))
        
        if 'tabel_html' in active_rubric and active_rubric['tabel_html'].strip() != "":
            st.markdown("---")
            st.markdown("**📋 Format Tabel Acuan PROPER:**")
            st.markdown(active_rubric['tabel_html'], unsafe_allow_html=True)
    # ==========================================

    st.markdown("### 📄 Unggah Dokumen Bukti")
    
    uploaded_files = st.file_uploader(
        "Seret & lepas (Drag & Drop) file PDF di sini (Bisa lebih dari 1 file)", 
        type=["pdf"], 
        accept_multiple_files=True
    )

    if st.button("🚀 Mulai Asesmen Kriteria Ini", type="primary", use_container_width=True):
        if not uploaded_files:
            st.warning("⚠️ Silakan unggah minimal satu dokumen PDF terlebih dahulu!")
        else:
            with st.spinner(f"🔍 Mesin AI sedang memindai {len(uploaded_files)} dokumen bukti (Menerapkan Siklus {siklus_proper})..."):
                try:
                    # Membaca seluruh file yang diunggah ke dalam bentuk list bytes
                    list_file_bytes = [f.read() for f in uploaded_files]
                    
                    # Mengirimkan list dokumen + rubrik + siklus_proper ke Mesin Evaluasi
                    hasil = run_gemini_audit(list_file_bytes, active_rubric, siklus_proper)
                    skor_didapat = float(hasil.get('skor', 0.0))
                    
                    # Simpan skor ke memori tabulasi
                    kunci_skor = f"{jenis_dokumen}_{kategori}_{selected_no}"
                    st.session_state.skor_tabulasi[kunci_skor] = skor_didapat

                    st.markdown("---")
                    st.markdown("### 📊 Hasil Analisis Asesor AI")
                    
                    # Layout Kolom untuk Hasil
                    col_score, col_desc = st.columns([1.5, 3])
                    
                    # Render Kartu Skor (Hijau jika dapet nilai, Merah jika 0)
                    with col_score:
                        card_class = "score-card-green" if skor_didapat > 0 else "score-card-red"
                        st.markdown(f"""
                            <div class="{card_class}">
                                <div class="score-title">Skor Diberikan</div>
                                <div class="score-value">{skor_didapat} <span style="font-size:1.2rem; color:#64748b;">/ {active_rubric['skor_maksimal']}</span></div>
                            </div>
                        """, unsafe_allow_html=True)

                    with col_desc:
                        st.markdown("#### 📍 Lokasi Bukti Fisik:")
                        st.success(hasil.get('bukti_dokumen', 'Lokasi tidak ditemukan.'))

                    st.markdown("#### 💡 Alasan & Catatan Penilaian:")
                    
                    # Gunakan warning (kuning) jika nilainya 0, info (biru) jika nilainya ada
                    if skor_didapat == 0.0:
                        st.warning(hasil.get('alasan_penilaian', 'Alasan tidak diberikan.'))
                    else:
                        st.info(hasil.get('alasan_penilaian', 'Alasan tidak diberikan.'))

                except Exception as e:
                    st.error(f"🚨 Terjadi kesalahan teknis: {e}")