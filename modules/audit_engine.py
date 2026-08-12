import os
import json
import urllib.request
import urllib.error
import io
import re
import base64

# Memuat file .env jika diuji secara lokal
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    import pypdf
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

class UniversalSmartDict(dict):
    def __iter__(self): yield self
    def __getitem__(self, key):
        if isinstance(key, int): return self
        if key in self: return super().__getitem__(key)
        key_str = str(key).lower().strip()
        for k, v in self.items():
            if str(k).lower().strip() == key_str: return v
        if key_str in ['total_skor', 'skor_total']: return float(self.get('skor', 0.0))
        if key_str in ['alasan_penilaian', 'alasan']: return self.get('alasan_penilaian', 'Dievaluasi.')
        if key_str in ['bukti_dokumen', 'bukti']: return self.get('bukti_dokumen', 'Ditemukan.')
        return ""
    def get(self, key, default=None):
        try: return self[key] if self[key] != "" else default
        except: return default

def clean_text_for_json(text):
    if not text: return ""
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', text)
    return text.replace('"', "'").replace('\\', '/')

def get_fast_models():
    """Daftar model gratis terprioritas yang paling CEPAT & RINGAN"""
    return [
        "google/gemini-2.0-flash-lite-preview-02-05:free",
        "google/gemini-2.0-flash-exp:free",
        "qwen/qwen-2.5-coder-32b-instruct:free",
        "meta-llama/llama-3.1-8b-instruct:free"
    ]

def run_gemini_audit(list_file_bytes, rubric_data, siklus_proper="2025/2026"):
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY") 

    try:
        tahun_akhir = int(siklus_proper.split("/")[1])
    except Exception:
        tahun_akhir = 2026
    tahun_awal = tahun_akhir - 1

    pdf_text = ""
    base64_images = []

    # Memproses SELURUH FILE yang diunggah
    for idx, f_bytes in enumerate(list_file_bytes):
        doc_text = ""
        # 1. BACA TEKS MURNI (PyPDF)
        if HAS_PYPDF:
            try:
                reader = pypdf.PdfReader(io.BytesIO(f_bytes))
                max_pages = min(len(reader.pages), 50) 
                for i in range(max_pages):
                    extracted = reader.pages[i].extract_text()
                    if extracted: doc_text += f"\n=== [DOKUMEN {idx+1} | HALAMAN {i+1}] ===\n" + extracted
            except Exception:
                pass

        pdf_text += doc_text
        
        # 2. BACA DOKUMEN SCAN / GAMBAR (PyMuPDF / Fitz)
        if len(doc_text.strip()) < 100 and HAS_FITZ:
            try:
                pdf_doc = fitz.open(stream=f_bytes, filetype="pdf")
                max_img_pages = min(len(pdf_doc), 10) 
                for i in range(max_img_pages):
                    page = pdf_doc.load_page(i)
                    pix = page.get_pixmap(matrix=fitz.Matrix(0.5, 0.5)) 
                    img_bytes = pix.tobytes("jpeg")
                    base64_img = base64.b64encode(img_bytes).decode('utf-8')
                    base64_images.append(base64_img)
            except Exception:
                pass

    pdf_text = clean_text_for_json(pdf_text)
    safe_pdf_text = pdf_text[:100000] # Potong maksimal 100rb karakter agar super cepat

    # --- PROTEKSI PENTING: JIKA TEKS & GAMBAR KOSONG ---
    if not safe_pdf_text.strip() and not base64_images:
        return UniversalSmartDict({
            "no": rubric_data['no'],
            "skor": 0.0,
            "bukti_dokumen": "Gagal membaca isi dokumen PDF.",
            "alasan_penilaian": "⚠️ Teks dokumen tidak dapat diekstrak. Pastikan file PDF tidak dikunci password."
        })

    # PROMPT AUDIT PROPER
    single_prompt = f"""Anda adalah Auditor Ahli PROPER Kementerian Lingkungan Hidup dan Kehutanan (KLHK) RI.
Tugas Anda adalah menilai secara obyektif dan kritis dokumen bukti perusahaan berdasarkan kriteria PROPER.

JANGKAR WAKTU AUDIT PROPER:
- Siklus Penilaian: TAHUN {siklus_proper}
- Periode Operasional Riil (Tahun N): 1 Juli {tahun_awal} s.d. 30 Juni {tahun_akhir}

KRITERIA DIEVALUASI:
Kriteria #{rubric_data['no']}: {rubric_data['kriteria_ai']}
Skor Maksimal: {rubric_data['skor_maksimal']}

RUBRIK PENILAIAN:
{rubric_data['rubrik_ai']}

DOKUMEN TEKS BUKTI:
{safe_pdf_text}

OUTPUT WAJIB (Format JSON Murni):
{{
  "no": "{rubric_data['no']}",
  "kriteria": "{rubric_data['kriteria_ai']}",
  "skor": <float_skor_didapat>,
  "skor_maksimal": {rubric_data['skor_maksimal']},
  "bukti_dokumen": "<Sebutkan nama dokumen/halaman bukti>",
  "alasan_penilaian": "<Jelaskan rincian alasan skor dan kesesuaian tahunnya>"
}}"""

    content_array = [{"type": "text", "text": single_prompt}]
    for b64 in base64_images:
        content_array.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{b64}"}
        })

    if not openrouter_api_key:
        return UniversalSmartDict({
            "skor": 0.0,
            "bukti_dokumen": "Gagal terhubung.",
            "alasan_penilaian": "API Key OpenRouter tidak ditemukan di dalam sistem environment."
        })

    # Cukup ambil 3 model cepat
    models_to_try = get_fast_models()[:3]
    last_error = ""

    for model_name in models_to_try:
        payload = {
            "model": model_name,
            "messages": [{"role": "user", "content": content_array}]
        }
        json_data = json.dumps(payload).encode('utf-8')
        headers = {
            "Authorization": f"Bearer {openrouter_api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://asesmen-proper-klh.streamlit.app", 
            "X-Title": "PROPER AI"
        }
        req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=json_data, headers=headers, method="POST")

        try:
            # TIMEOUT DIPERKETAT HANYA 8 DETIK PER MODEL
            with urllib.request.urlopen(req, timeout=8) as response:
                res_body = response.read().decode('utf-8')
                res_json = json.loads(res_body)
                raw_text = res_json['choices'][0]['message']['content'].strip()

                if "```json" in raw_text: raw_text = raw_text.split("```json")[1].split("```")[0]
                elif "```" in raw_text: raw_text = raw_text.split("```")[1].split("```")[0]

                parsed = json.loads(raw_text.strip())
                if isinstance(parsed, list) and len(parsed) > 0: parsed = parsed[0]
                
                via_text = f"(Via {model_name} - Fast Mode)"

                return UniversalSmartDict({
                    "no": rubric_data['no'],
                    "skor": float(parsed.get('skor', 0.0)),
                    "bukti_dokumen": str(parsed.get('bukti_dokumen', 'Ditemukan.')),
                    "alasan_penilaian": f"{via_text}\n\n" + str(parsed.get('alasan_penilaian', 'Evaluasi selesai.'))
                })
        except urllib.error.HTTPError as e:
            last_error = f"Model {model_name} HTTP {e.code}"
            continue 
        except Exception as e:
            last_error = f"Model {model_name} Timeout/Error: {str(e)}"
            continue

    return UniversalSmartDict({
        "skor": 0.0,
        "bukti_dokumen": "Koneksi AI Lambat.",
        "alasan_penilaian": f"Layanan AI gratisan sedang mengalami antrean padat di server. {last_error}"
    })