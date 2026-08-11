import os
import json
import urllib.request
import urllib.error

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