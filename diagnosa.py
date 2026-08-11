import urllib.request
import json
import os

# Memuat file .env agar script ini bisa membaca kunci rahasia
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Mengambil Kunci API OpenRouter dari brankas (.env)
token = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

# Kita tes dengan teks yang sangat kecil dulu
payload = {
    "model": "google/gemini-2.0-flash-exp:free",
    "messages": [{"role": "user", "content": "Halo, tes koneksi. Balas dengan kata 'KONEKSI BERHASIL'."}]
}

if not token:
    print("❌ GAGAL: Kunci OPENROUTER_API_KEY tidak ditemukan di environment/file .env!")
else:
    headers = {
        "Authorization": f"Bearer {token}", 
        "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost",
        "X-Title": "Tes"
    }

    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method="POST")

    print("Mengirim request ke OpenRouter...")
    try:
        response = urllib.request.urlopen(req)
        print("\n✅ SUKSES! Balasan AI:")
        print(json.loads(response.read().decode('utf-8'))['choices'][0]['message']['content'])
    except Exception as e:
        print("\n❌ GAGAL!")
        print(f"Error Type: {e}")
        if hasattr(e, 'read'):
            print(f"Detail Pesan dari Server: {e.read().decode('utf-8')}")