import os
import json
import urllib.request
import urllib.error
import streamlit as st
import sys

# Memuat file .env jika diuji secara lokal
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "").strip()

def register_user(nama, perusahaan, email, password):
    """Mendaftarkan user baru ke Supabase Auth & Tabel Profiles (Status default: pending)"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        return False, "Kredensial Supabase belum diatur di sistem."

    # 1. Daftar ke Supabase Auth
    signup_url = f"{SUPABASE_URL}/auth/v1/signup"
    payload_auth = json.dumps({"email": email, "password": password}).encode('utf-8')
    headers = {
        "apikey": SUPABASE_KEY,
        "Content-Type": "application/json"
    }

    req_auth = urllib.request.Request(signup_url, data=payload_auth, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req_auth) as res:
            res_data = json.loads(res.read().decode('utf-8'))
            user_id = res_data.get('user', {}).get('id') or res_data.get('id')

            if not user_id:
                return False, "Pendaftaran gagal. Pastikan email belum pernah terdaftar."

            # 2. Simpan Data ke Tabel Profiles (status: pending)
            profile_url = f"{SUPABASE_URL}/rest/v1/profiles"
            payload_profile = json.dumps({
                "id": user_id,
                "nama": nama,
                "nama_perusahaan": perusahaan,
                "email": email,
                "status": "pending"
            }).encode('utf-8')

            req_profile = urllib.request.Request(profile_url, data=payload_profile, headers=headers, method="POST")
            with urllib.request.urlopen(req_profile) as res_p:
                return True, "✅ Registrasi berhasil! Akun Anda berstatus 'PENDING'. Silakan hubungi Admin/Developer untuk persetujuan (Approval)."

    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8')
        if "User already registered" in err_body:
            return False, "Email ini sudah terdaftar. Silakan lakukan Login."
        return False, f"Gagal mendaftar: {err_body}"
    except Exception as e:
        return False, f"Terjadi kesalahan: {str(e)}"

def login_user(email, password):
    """Verifikasi email & password, lalu periksa status persetujuan dari Admin"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        return False, "Kredensial Supabase belum diatur di sistem.", None

    # 1. Autentikasi User
    login_url = f"{SUPABASE_URL}/auth/v1/token?grant_type=password"
    payload = json.dumps({"email": email, "password": password}).encode('utf-8')
    headers = {
        "apikey": SUPABASE_KEY,
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(login_url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as res:
            res_data = json.loads(res.read().decode('utf-8'))
            user_id = res_data.get('user', {}).get('id')

            # 2. Cek Status Approval di Tabel Profiles
            profile_url = f"{SUPABASE_URL}/rest/v1/profiles?id=eq.{user_id}&select=*"
            req_profile = urllib.request.Request(profile_url, headers=headers, method="GET")

            with urllib.request.urlopen(req_profile) as res_p:
                profiles = json.loads(res_p.read().decode('utf-8'))
                if not profiles:
                    return False, "Profil user tidak ditemukan di database.", None

                user_profile = profiles[0]
                status = user_profile.get('status', 'pending')

                if status.lower() == 'approved':
                    return True, "Login Berhasil!", user_profile
                else:
                    return False, f"🔒 Akun Anda masih berstatus '{status.upper()}'. Akses belum dibuka oleh Admin.", None

    except urllib.error.HTTPError as e:
        return False, "Email atau password yang Anda masukkan salah.", None
    except Exception as e:
        return False, f"Terjadi kesalahan login: {str(e)}", None


# Menyambungkan logika dan data
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from modules.audit_engine import run_gemini_audit
from kriteria_data import DATA_PROPER

# --- KONFIGURASI STATE MEMORI ---
if 'skor_tabulasi' not in st.session_state:
    st.session_state.skor_tabulasi = {}

if 'user_logged_in' not in st.session_state:
    st.session_state.user_logged_in = False

if 'user_info' not in st.session_state:
    st.session_state.user_info = None

# Konfigurasi Halaman (Lebih lebar & elegan)
st.set_page_config(page_title="Sistem Asesmen PROPER Hijau", layout="wide", page_icon="🌿")

# ==========================================
# SUNTIKAN CSS KUSTOM UNTUK TAMPILAN ELEGAN & SCROLL DINAMIS
# ==========================================
st.markdown("""
    <style>
    /* --- MENGHILANGKAN MENU BAWAAN STREAMLIT (White-label) --- */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    [data-testid="stDecoration"] {visibility: hidden !important;}
    
    /* Header Card Hijau Emas (Presisi mengikuti lebar kolom) */
    .header-card {
        background: linear-gradient(135deg, #064E3B 0%, #047857 100%);
        padding: 2.25rem 1.5rem;
        border-radius: 20px;
        color: white;
        box-shadow: 0 10px 25px -5px rgba(6, 78, 59, 0.25);
        border-bottom: 5px solid #D97706; /* Emas */
        margin-bottom: 1.5rem;
        text-align: center;
        width: 100%;
    }
    .header-card h1 {
        font-size: 1.75rem;
        font-weight: 800;
        margin: 0;
        color: #FFFFFF;
        letter-spacing: -0.5px;
        line-height: 1.25;
    }
    .header-subtitle {
        font-size: 0.85rem;
        color: #A7F3D0;
        margin-top: 0.6rem;
        font-weight: 400;
    }
    
    /* Styling Header Utama Setelah Login */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #064E3B;
        padding-bottom: 0px;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #64748b;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    
    /* FITUR: MENGUBAH RADIO BUTTON MENJADI SCROLLABLE & STRICT 1 KOLOM */
    [data-testid="stSidebar"] [role="radiogroup"] {
        max-height: 300px;
        overflow-y: auto;
        overflow-x: hidden;
        padding-right: 10px;
        border-top: 1px solid #f1f5f9;
        border-bottom: 1px solid #f1f5f9;
        padding-top: 10px;
        padding-bottom: 10px;
        display: flex !important;
        flex-direction: column !important;
        flex-wrap: nowrap !important;
        gap: 4px;
    }
    
    [data-testid="stSidebar"] [role="radiogroup"] label {
        width: 100% !important;
        margin-right: 0 !important;
    }

    /* FITUR: MENGUBAH TABULASI SKOR MENJADI SCROLLABLE */
    .score-scroll-container {
        max-height: 250px;
        overflow-y: auto;
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

    /* Styling Scrollbar */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    
    /* Kartu Hasil Penilaian */
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
    
    /* Tombol Utama (Hijau Emas) */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        padding: 10px 24px;
        background: linear-gradient(135deg, #047857 0%, #065F46 100%);
        color: #FFFFFF;
        border: 1px solid #D97706; /* Accent Emas Halus */
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(217,119,6,0.3);
        background: linear-gradient(135deg, #B45309 0%, #D97706 100%);
        color: #FFFFFF;
        border-color: #F59E0B;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# GATEKEEPER: HALAMAN AUTHENTICATION (LOGIN & REGISTRASI)
# ==========================================
if not st.session_state.user_logged_in:
    
    # Menggunakan rasio [1.2, 2, 1.2] agar kotak di tengah tampil sangat proporsional & elegan
    col_space1, col_form, col_space2 = st.columns([1.2, 2, 1.2])

    with col_form:
        # Header Kustom Hijau-Emas (Sekarang berada di dalam col_form yang sama dengan form)
        st.markdown("""
            <div class="header-card">
                <h1>🌿 Sistem Asesmen PROPER Hijau KLH</h1>
                <p class="header-subtitle">Silakan login atau mendaftar akun untuk mengakses sistem</p>
            </div>
        """, unsafe_allow_html=True)

        tab_login, tab_register = st.tabs(["🔒 Login", "📝 Pendaftaran Akun Baru"])

        # TAB LOGIN
        with tab_login:
            st.markdown("### Login Asesor / Perusahaan")
            email_login = st.text_input("Alamat Email", key="login_email", placeholder="nama@perusahaan.com")
            pass_login = st.text_input("Password", type="password", key="login_pass", placeholder="••••••••")

            if st.button("🔑 Login Sistem", use_container_width=True):
                if not email_login or not pass_login:
                    st.warning("Mohon isi Email dan Password!")
                else:
                    with st.spinner("Verifikasi kredensial..."):
                        success, msg, profile = login_user(email_login, pass_login)
                        if success:
                            st.session_state.user_logged_in = True
                            st.session_state.user_info = profile
                            st.success(msg)
                            st.rerun()
                        else:
                            st.error(msg)

        # TAB REGISTRASI
        with tab_register:
            st.markdown("### Form Pendaftaran Akun Baru")
            nama_reg = st.text_input("Nama Lengkap Pengguna", key="reg_nama", placeholder="Contoh: Budi Santoso")
            pt_reg = st.text_input("Nama Perusahaan / Instansi", key="reg_pt", placeholder="Contoh: PT Berkah Jaya")
            email_reg = st.text_input("Alamat Email", key="reg_email", placeholder="nama@perusahaan.com")
            pass_reg = st.text_input("Password Baru", type="password", key="reg_pass", placeholder="••••••••")

            if st.button("📩 Daftar Sekarang", use_container_width=True):
                if not nama_reg or not pt_reg or not email_reg or not pass_reg:
                    st.warning("Semua kolom registrasi wajib diisi!")
                else:
                    with st.spinner("Mendaftarkan akun..."):
                        success, msg = register_user(nama_reg, pt_reg, email_reg, pass_reg)
                        if success:
                            st.success(msg)
                        else:
                            st.error(msg)
                            
    # Footer Kustom
    st.markdown("""
        <div style="text-align: center; margin-top: 3.5rem; font-size: 0.75rem; color: #64748B; border-top: 1px solid #E2E8F0; padding-top: 1.5rem; line-height: 1.6;">
            Dikembangkan oleh <strong>Shared Value Indonesia</strong> © 2026<br>
            Platform Sistem Asesmen Kinerja Pengelolaan Lingkungan Perusahaan (PROPER Hijau).
        </div>
    """, unsafe_allow_html=True)

    st.stop() # Hentikan eksekusi di sini jika belum login


# ==========================================
# APLIKASI UTAMA (TERBUKA HANYA JIKA APPROVED)
# ==========================================

# --- HEADER APLIKASI ---
st.markdown('<div class="main-header">🌿 Asesmen - PROPER Hijau KLH</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Asisten Cerdas untuk Evaluasi Dokumen Keberlanjutan</div>', unsafe_allow_html=True)
st.markdown("---")

# --- MENU SIDEBAR: PROFIL & NAVIGASI ---
st.sidebar.title("👤 Profil Pengguna")
st.sidebar.info(f"**{st.session_state.user_info.get('nama')}**\n\n🏢 {st.session_state.user_info.get('nama_perusahaan')}")

if st.sidebar.button("🚪 Logout", use_container_width=True):
    st.session_state.user_logged_in = False
    st.session_state.user_info = None
    st.session_state.skor_tabulasi = {}
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.title("⚙️ Konfigurasi")

# Pilih Siklus Penilaian PROPER
siklus_proper = st.sidebar.selectbox(
    "🗓️ Siklus Penilaian PROPER:",
    ["2023/2024", "2024/2025", "2025/2026", "2026/2027", "2027/2028"],
    index=2,
    help="Menentukan batas kedaluwarsa dokumen dinamis (Renja, Laporan, dll)."
)

tahun_akhir = siklus_proper.split("/")[1]
st.sidebar.caption(f"📌 **Timeline Riil:** 1 Juli {int(tahun_akhir)-1} s.d. 30 Juni {tahun_akhir}")
st.sidebar.markdown("---")

# 1. Pilih Jenis Dokumen
jenis_dokumen = st.sidebar.selectbox("📂 1. Pilih Jenis Dokumen", list(DATA_PROPER.keys()))

# 2. Pilih Kategori
kategori_list = list(DATA_PROPER[jenis_dokumen].keys())
kategori = st.sidebar.selectbox("📑 2. Pilih Kategori", kategori_list)

st.sidebar.markdown("---")
st.sidebar.markdown("**🎯 3. Pilih Kriteria Penilaian:**")

kriteria_dict = DATA_PROPER[jenis_dokumen][kategori]

if not kriteria_dict:
    st.sidebar.warning("Kriteria untuk kategori ini belum tersedia.")
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
    st.sidebar.markdown(html_scores, unsafe_allow_html=True)
    st.sidebar.success(f"**TOTAL SKOR: {total_skor} / {maks_skor}**")

    # ==========================================
    # DASHBOARD UTAMA (EVALUASI)
    # ==========================================
    active_rubric = kriteria_dict[selected_no]

    st.caption(f"📍 **Modul Aktif:** {jenis_dokumen} ➔ {kategori} ➔ Kriteria {selected_no}")
    st.header(active_rubric['judul'])

    with st.expander("📖 Lihat Panduan Penilaian & Rubrik PROPER LHK", expanded=False):
        st.info(active_rubric.get('detail_ui', 'Aspek penilaian tidak tersedia.'))
        st.markdown("#### 🎯 Kriteria & Parameter Sistem")
        st.markdown(f"- **Fokus Analisis AI:** {active_rubric.get('kriteria_ai', '-')}")
        st.markdown(f"- **Skor Maksimal:** `{active_rubric.get('skor_maksimal', 0.0)}`")
        
        st.markdown("#### ⚙️ Aturan Skoring & Validasi Waktu")
        st.warning(active_rubric.get('rubrik_ai', 'Aturan skoring tidak tersedia.'))
        
        if 'tabel_html' in active_rubric and active_rubric['tabel_html'].strip() != "":
            st.markdown("---")
            st.markdown("**📋 Format Tabel Acuan PROPER:**")
            st.markdown(active_rubric['tabel_html'], unsafe_allow_html=True)

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
                    list_file_bytes = [f.read() for f in uploaded_files]
                    hasil = run_gemini_audit(list_file_bytes, active_rubric, siklus_proper)
                    skor_didapat = float(hasil.get('skor', 0.0))
                    
                    kunci_skor = f"{jenis_dokumen}_{kategori}_{selected_no}"
                    st.session_state.skor_tabulasi[kunci_skor] = skor_didapat

                    st.markdown("---")
                    st.markdown("### 📊 Hasil Analisis Asesor AI")
                    
                    col_score, col_desc = st.columns([1.5, 3])
                    
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
                    if skor_didapat == 0.0:
                        st.warning(hasil.get('alasan_penilaian', 'Alasan tidak diberikan.'))
                    else:
                        st.info(hasil.get('alasan_penilaian', 'Alasan tidak diberikan.'))

                except Exception as e:
                    st.error(f"🚨 Terjadi kesalahan teknis: {e}")