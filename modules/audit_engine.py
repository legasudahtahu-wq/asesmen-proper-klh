import os
import json
import urllib.request
import urllib.error
import io
import re
import base64

# Memuat file .env (Sangat penting agar kunci rahasia terbaca)
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

def get_live_free_models(api_key):
    url = "https://openrouter.ai/api/v1/models"
    if not api_key:
        return ["google/gemini-2.0-flash-lite-preview-02-05:free"]
    
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            free_models = [m.get('id') for m in data.get('data', []) if m.get('id', '').endswith(':free')]
            
            vision_models = [m for m in free_models if any(x in m.lower() for x in ['gemini', 'pixtral', 'llama-3.2-90b', 'qwen'])]
            others = [m for m in free_models if m not in vision_models]
            
            combined = vision_models + others
            return combined if combined else ["google/gemini-2.0-flash-lite-preview-02-05:free"]
    except Exception:
        return ["google/gemini-2.0-flash-lite-preview-02-05:free"]

# === PENAMBAHAN PARAMETER KE-3 (siklus_proper) DI SINI ===
def run_gemini_audit(list_file_bytes, rubric_data, siklus_proper="2025/2026"):
    # Memanggil kunci dari brankas rahasia (.env atau sistem server)
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY") 

    # --- Kalkulasi Tahun untuk Jangkar Waktu Audit ---
    try:
        tahun_akhir = int(siklus_proper.split("/")[1])
    except Exception:
        tahun_akhir = 2026
    tahun_awal = tahun_akhir - 1

    pdf_text = ""
    base64_images = []

    # Memproses BANYAK FILE sekaligus
    for idx, f_bytes in enumerate(list_file_bytes):
        doc_text = ""
        # 1. BACA TEKS MURNI
        if HAS_PYPDF:
            try:
                reader = pypdf.PdfReader(io.BytesIO(f_bytes))
                max_pages = min(len(reader.pages), 60) 
                for i in range(max_pages):
                    extracted = reader.pages[i].extract_text()
                    if extracted: doc_text += f"\n=== [DOKUMEN {idx+1} | HALAMAN {i+1}] ===\n" + extracted
            except Exception:
                pass

        pdf_text += doc_text
        
        # 2. BACA DOKUMEN SCAN (Jika khusus file INI tidak ada teksnya)
        if len(doc_text.strip()) < 100 and HAS_FITZ:
            try:
                pdf_doc = fitz.open(stream=f_bytes, filetype="pdf")
                max_img_pages = min(len(pdf_doc), 25) 
                for i in range(max_img_pages):
                    page = pdf_doc.load_page(i)
                    pix = page.get_pixmap(matrix=fitz.Matrix(0.6, 0.6)) 
                    img_bytes = pix.tobytes("jpeg")
                    base64_img = base64.b64encode(img_bytes).decode('utf-8')
                    base64_images.append(base64_img)
            except Exception:
                pass

    pdf_text = clean_text_for_json(pdf_text)
    safe_pdf_text = pdf_text[:200000]

    # === UPDATE: PROMPT DENGAN JANGKAR WAKTU & HARD-GATE ===
    single_prompt = f"""Anda adalah Auditor Ahli PROPER Kementerian Lingkungan Hidup dan Kehutanan (KLHK) RI.
Tugas Anda adalah menilai secara obyektif dan kritis dokumen bukti perusahaan berdasarkan kriteria PROPER.
(Terdapat {len(list_file_bytes)} dokumen bukti yang dilampirkan. Gabungkan informasi dari seluruh dokumen).

==================================================
JANGKAR WAKTU AUDIT PROPER (MUTLAK):
- Siklus Penilaian PROPER Aktif: TAHUN {siklus_proper}
- Periode Operasional Riil (Tahun N): 1 Juli {tahun_awal} s.d. 30 Juni {tahun_akhir}
- Tahun Acuan Perhitungan Mundur (N): {tahun_akhir}
==================================================

ATURAN EVALUASI & VALIDASI WAKTU:
1. HARD-GATE VALIDATION (VALIDASI JENIS DOKUMEN):
   - Periksa judul, halaman sampul, dan konteks umum dokumen. 
   - JIKA DOKUMEN YANG DIUNGGAH BERUPA CV INDIVIDU, PROFIL PRIBADI, KUITANSI, TUGAS KULIAH, ATAU DOKUMEN ACAK TIDAK RELEVAN LAINNYA, LANGSUNG BERIKAN SKOR 0.0 TANPA DITAWAR.
2. KESESUAIAN TAHUN/PERIODE SESUAI LOGIKA PROPER:
   - Dokumen Statis (Kebijakan Tertulis, SOP, PKB): Diterima tahun berapapun selama tidak ada keterangan dicabut/diganti.
   - Dokumen Pemetaan Sosial (Maksimal 4 Tahun Terakhir): Wajib diterbitkan antara tahun {tahun_akhir - 4} s.d. {tahun_akhir}.
   - Publikasi Jurnal / Buku ISBN (Maksimal 3 Tahun Terakhir): Wajib terbit antara tahun {tahun_akhir - 3} s.d. {tahun_akhir} DAN harus membahas program CSR perusahaan (bukan karya pribadi).
   - Dokumen Dinamis Mutlak (Renja, Laporan Implementasi, Monev, IKM, Pengesahan Pimpinan): HARUS mencakup periode aktivitas/penilaian {siklus_proper} (Semester 2-{tahun_awal} s.d. Semester 1-{tahun_akhir}). Dokumen tahun usang/lampau = SKOR 0.0.

KRITERIA YANG DIEVALUASI:
Kriteria #{rubric_data['no']}: {rubric_data['kriteria_ai']}
Skor Maksimal Kriteria Ini: {rubric_data['skor_maksimal']}

RUBRIK PENILAIAN & ATURAN SKORING:
{rubric_data['rubrik_ai']}

DOKUMEN TEKS BUKTI PERUSAHAAN:
{safe_pdf_text}

OUTPUT WAJIB (1 Object JSON Murni tanpa format markdown tambahan):
{{
  "no": "{rubric_data['no']}",
  "kriteria": "{rubric_data['kriteria_ai']}",
  "skor": <float_skor_didapat>,
  "skor_maksimal": {rubric_data['skor_maksimal']},
  "bukti_dokumen": "<Sebutkan nama dokumen/halaman bukti tersebut ditemukan>",
  "alasan_penilaian": "<Jelaskan rinci alasan skor, sebutkan kesesuaian tahun dan isi substansinya>"
}}"""

    # 3. SUSUN PAKET
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
            "alasan_penilaian": "API Key OpenRouter tidak ditemukan di dalam sistem. Pastikan file .env sudah diatur dengan benar."
        })

    models_to_try = get_live_free_models(openrouter_api_key)[:15]
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
            "HTTP-Referer": "http://localhost", 
            "X-Title": "PROPER AI"
        }
        req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=json_data, headers=headers, method="POST")

        try:
            with urllib.request.urlopen(req) as response:
                res_body = response.read().decode('utf-8')
                res_json = json.loads(res_body)
                raw_text = res_json['choices'][0]['message']['content'].strip()

                if "```json" in raw_text: raw_text = raw_text.split("```json")[1].split("```")[0]
                elif "```" in raw_text: raw_text = raw_text.split("```")[1].split("```")[0]

                parsed = json.loads(raw_text.strip())
                if isinstance(parsed, list) and len(parsed) > 0: parsed = parsed[0]
                
                via_text = f"(Via {model_name} - Multi-File / Vision Mode 👁️)" if base64_images else f"(Via {model_name} - Multi-File)"

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
            last_error = f"Model {model_name} Error: {str(e)}"
            continue

    return UniversalSmartDict({
        "skor": 0.0,
        "bukti_dokumen": "Gagal terhubung.",
        "alasan_penilaian": f"Semua model dicoba namun gagal/menolak. Error terakhir: {last_error}"
    })