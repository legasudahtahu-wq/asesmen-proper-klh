# kriteria_data.py

DATA_PROPER = {
    "DRKPL": {
        "Pengembangan Masyarakat": {
            1: {
                "no": 1,
                "judul": "1. Status Kegiatan Pemberdayaan Masyarakat",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Status Kegiatan Pemberdayaan Masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Pastikan tabel mencakup data hingga Tahun N berjalan. Cari tabel yang menjelaskan status kegiatan pemberdayaan masyarakat selama 4 tahun terakhir (Tahun N-4 s.d Tahun N berjalan). Tabel tersebut HARUS memiliki kolom klasifikasi kegiatan (seperti: karikatif, infrastruktur, penguatan kapasitas, pemberdayaan). Berikan Skor 2.0 jika tabel data lengkap 4 tahun berturut-turut beserta klasifikasinya. Berikan Skor 0.0 jika data kurang dari 4 tahun atau klasifikasi tidak ada.",
                "detail_ui": "**Pertanyaan Verbatim PROPER:**\n> \"Menjelaskan status kegiatan pemberdayaan masyarakat yang dilakukan selama 4 tahun terakhir dengan mengisi tabel sebagai berikut: Keterangan: klasifikasi kegiatan berupa 1) karikatif; 2) infrastruktur; 3) penguatan kapasitas; 4) pemberdayaan\"\n\n**Aturan Evaluasi Sistem:** Sistem akan memindai dokumen untuk mencari keberadaan tabel yang memuat daftar program, klasifikasinya, dan rekam jejak selama 4 tahun terakhir (Tahun N-4 s.d Tahun N).",
                "tabel_html": "<div style=\"overflow-x:auto;\"><table style=\"width:100%; border: 1px solid #ddd; border-collapse: collapse; text-align: center; font-size: 14px; background-color: white;\"><tr style=\"background-color: #f8f9fa;\"><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">No</th><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">Program</th><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">Klasifikasi</th><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">Lokasi</th><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">Satuan</th><th colspan=\"5\" style=\"border: 1px solid #ddd; padding: 10px;\">Hasil Absolut</th></tr><tr style=\"background-color: #f8f9fa;\"><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N-4</th><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N-3</th><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N-2</th><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N-1</th><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N</th></tr><tr><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">1</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888;\">...</td></tr></table></div><br>"
            },
            2: {
                "no": 2,
                "judul": "2. Hasil Absolut Kegiatan Pemberdayaan Masyarakat",
                "skor_maksimal": 4.0,
                "kriteria_ai": "Hasil Absolut Kegiatan Pemberdayaan Masyarakat",
                "rubrik_ai": "Evaluasi kelengkapan 5 SYARAT MUTLAK ini di dalam dokumen:\na. Ada deskripsi kegiatan/program.\nb. Ada tabel hasil absolut yang berisi indikator spesifik.\nc. Tersedia data paling sedikit 4 tahun terakhir.\nd. Tersedia data pada tahun ke-N (Tahun Penilaian yang berjalan).\ne. Menampilkan data anggaran.\nATURAN KETAT: Berikan Skor 4.0 HANYA JIKA KELIMA SYARAT (a-e) TERPENUHI SECARA BERSAMAAN. Berikan Skor 0.0 jika ada SALAH SATU SAJA syarat yang tidak lengkap.",
                "detail_ui": "**Pertanyaan Verbatim PROPER:**\n> \"Menjelaskan hasil absolut kegiatan pemberdayaan masyarakat, yang terdiri dari: a. Memberikan deskripsi kegiatan. b. Mengisi tabel absolut. c. Tersedia data paling sedikit 4 tahun. d. Tersedia data pada tahun ke-N. e. Menampilkan anggaran kegiatan\"\n\n**Aturan Evaluasi Sistem:** Sistem akan memeriksa kelengkapan **kelima syarat (a sampai e)** tersebut secara ketat, khususnya keberadaan data pada tahun penilaian (Tahun N).",
                "tabel_html": "<div style=\"overflow-x:auto;\"><table style=\"width:100%; border: 1px solid #ddd; border-collapse: collapse; text-align: left; font-size: 14px; background-color: white;\"><tr style=\"background-color: #f8f9fa; text-align: center;\"><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">No</th><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">Program</th><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">Indikator</th><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">Deskripsi Indikator</th><th rowspan=\"2\" style=\"border: 1px solid #ddd; padding: 10px;\">Satuan</th><th colspan=\"5\" style=\"border: 1px solid #ddd; padding: 10px;\">Hasil Absolut</th></tr><tr style=\"background-color: #f8f9fa; text-align: center;\"><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N-4</th><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N-3</th><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N-2</th><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N-1</th><th style=\"border: 1px solid #ddd; padding: 8px;\">Thn N</th></tr><tr><td rowspan=\"5\" style=\"border: 1px solid #ddd; padding: 8px; text-align: center; vertical-align: top;\">1</td><td rowspan=\"5\" style=\"border: 1px solid #ddd; padding: 8px; font-weight: bold; text-align: center; vertical-align: top;\">Program A</td><td style=\"border: 1px solid #ddd; padding: 8px;\">Masalah lingkungan yang diselesaikan</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td></tr><tr><td style=\"border: 1px solid #ddd; padding: 8px;\">Masalah sosial yang diselesaikan</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td></tr><tr><td style=\"border: 1px solid #ddd; padding: 8px;\">Jumlah penerima manfaat</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td></tr><tr><td style=\"border: 1px solid #ddd; padding: 8px;\">Jumlah peningkatan pendapatan</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td></tr><tr><td style=\"border: 1px solid #ddd; padding: 8px;\">Jumlah kelembagaan baru yang terbentuk</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td><td style=\"border: 1px solid #ddd; padding: 8px; color:#888; text-align:center;\">...</td></tr></table></div><br>"
            },
            3: {
                "no": 3,
                "judul": "3. Sertifikasi / Penghargaan Pemberdayaan Masyarakat",
                "skor_maksimal": 1.5,
                "kriteria_ai": "Sertifikasi atau Penghargaan Pemberdayaan Masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Pastikan sertifikat penghargaan ini diterbitkan sesuai masa tahun penilaian.\n- Berikan Skor 1.5 jika terdapat bukti penghargaan tingkat Nasional atau Internasional.\n- Berikan Skor 0.5 jika hanya terdapat bukti penghargaan tingkat Lokal, Regional, atau Provinsi.\n- Berikan Skor 0.0 jika usang atau tidak ada.",
                "detail_ui": "**Pertanyaan Verbatim PROPER:**\n> \"Memiliki penghargaan di bidang pemberdayaan masyarakat di tingkat:\n> a) Nasional; dan\n> b) Internasional.\"\n\n**Aturan Evaluasi Sistem:** Sistem akan memindai seluruh dokumen untuk mencari rekam jejak, sertifikat, atau sebutan pencapaian/penghargaan spesifik di bidang pemberdayaan masyarakat beserta tingkatannya yang relevan dengan masa penilaian.",
                "tabel_html": "" 
            },
            4: {
                "no": 4,
                "judul": "4. Inovasi Sosial Pemberdayaan Masyarakat",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Inovasi Sosial Pemberdayaan Masyarakat",
                "rubrik_ai": "Evaluasi apakah program pemberdayaan masyarakat memiliki INOVASI dengan 3 SYARAT MUTLAK berikut:\n a. Ada deskripsi teknis inovasi yang menonjolkan unsur kebaruan.\n b. Ada bukti bahwa inovasi tersebut menyebabkan perbaikan lingkungan secara KUANTITATIF (angka riil).\n c. Ada deskripsi nilai tambah (value) yang disebabkan oleh inovasi berupa salah satu dari: i. Perubahan rantai nilai; ii. Penambahan kualitas layanan produk/jasa; atau iii. Perubahan perilaku.\nATURAN KETAT: Berikan Skor 2.0 HANYA JIKA KETIGA SYARAT (a, b, c) terpenuhi. Berikan Skor 0.0 jika ada salah satu syarat saja yang tidak lengkap/tidak kuantitatif.",
                "detail_ui": "**Pertanyaan Verbatim PROPER:**\n> \"Memiliki program/kegiatan pemberdayaan masyarakat dengan ketentuan:\n> a. Mendeskripsikan secara singkat dan teknis inovasi yang dilakukan dengan mengutamakan unsur kebaruan\n> b. Dapat menunjukan bahwa hasil inovasi menyebabkan terjadinya perbaikan lingkungan (secara kuantitatif)\n> c. Dapat mendeskripsikan nilai tambah (value) yang disebabkan oleh inovasi pada tingkat sistem/sub sistem/komponen: i. Perubahan rantai nilai; ii. Penambahan kualitas layanan produk/jasa; dan iii. Perubahan perilaku.\"\n\n**Aturan Evaluasi Sistem:** Sistem akan memverifikasi 3 komponen (Kebaruan teknis, Hitungan perbaikan lingkungan kuantitatif, dan Bukti nilai tambah).",
                "tabel_html": "" 
            },
            5: {
                "no": 5,
                "judul": "5. Paten / Hak Cipta / Kekayaan Intelektual",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Paten Teknologi Pengembangan Masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Tahun paten/sertifikat terbit HARUS SESUAI dengan masa penilaian.\nEvaluasi PATEN atau HAKI: \na. Terkait teknologi di bidang pemberdayaan/pengembangan masyarakat. \nb. Dikeluarkan oleh pihak berwenang resmi di Indonesia (misal: DJKI Kementerian Hukum dan HAM). \nATURAN KETAT: Berikan Skor 3.0 HANYA JIKA ketiga syarat terpenuhi. Berikan Skor 0.0 jika tidak ditemukan atau tahunnya kedaluwarsa.",
                "detail_ui": "**Pertanyaan Verbatim PROPER:**\n> \"Paten. Teknologi di bidang pengembangan masyakarat telah memperoleh paten dari pihak yang berwenang.\"\n\n**Aturan Evaluasi Sistem:** Sistem akan memindai dokumen untuk mencari sertifikat, nomor registrasi Paten, atau HAKI dari DJKI Kemenkumham RI yang terkait langsung dengan program Comdev dan dicatatkan pada tahun penilaian berjalan.",
                "tabel_html": "" 
            }
        }
    },
    
    "Dokumen Lengkap": {
        "Pemberdayaan Masyarakat": {
            "1.a": {
                "no": "1.a",
                "judul": "1.a Kebijakan Tertulis Pengembangan Masyarakat",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Kebijakan Tertulis Pengembangan Masyarakat / CSR",
                "rubrik_ai": "Cari bukti dokumen berupa kebijakan tertulis (seperti SK Direksi, Peraturan Perusahaan, SOP) mengenai pengembangan masyarakat/CSR. CATATAN: Dokumen kebijakan bersifat statis, tahun berapapun dokumen diterbitkan tetap VALID selama masih berlaku.\nATURAN SKORING:\n- Skor 2.0 jika ditemukan bukti kebijakan tertulis tersebut dengan jelas.\n- Skor 0.0 jika tidak ditemukan.",
                "detail_ui": "**Aspek Penilaian:** Kebijakan Pengembangan Masyarakat",
                "tabel_html": "" 
            },
            "1.b": {
                "no": "1.b",
                "judul": "1.b Sistem Tata Kelola Pengembangan Masyarakat",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Sistem Tata Kelola Program Pengembangan Masyarakat / CSR",
                "rubrik_ai": "Cari bukti dokumen 'Sistem Tata Kelola' khusus untuk program Pengembangan Masyarakat/CSR (SOP, Instruksi Kerja, dll). CATATAN: Dokumen statis, tahun berapapun diterbitkan tetap VALID.\nATURAN SKORING:\n- Skor 1.0 jika dokumen tata kelola Comdev tersedia.\n- Skor 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Kebijakan Pengembangan Masyarakat",
                "tabel_html": "" 
            },
            "2.1": {
                "no": "2.1",
                "judul": "2.1 Struktur dan Tanggung Jawab Pengembangan Masyarakat",
                "skor_maksimal": 5.0,
                "kriteria_ai": "Struktur Organisasi dan Fungsi Khusus Pengembangan Masyarakat (CSR)",
                "rubrik_ai": "Cari bukti dokumen bagan struktur organisasi atau Job Description yang menunjukkan divisi/tim khusus untuk CSR. Dokumen bersifat statis.\nATURAN SKORING (Rentang 0.0 - 5.0): Skor penuh jika struktur eksklusif menangani Comdev. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Struktur dan Tanggung Jawab",
                "tabel_html": "" 
            },
            "2.2": {
                "no": "2.2",
                "judul": "2.2 Kualifikasi SDM Pengembangan Masyarakat",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Kualifikasi Pendidikan dan Pelatihan SDM (CDO) Pengembangan Masyarakat",
                "rubrik_ai": "Cari bukti dokumen kualifikasi SDM (CDO) seperti CV, matriks, atau sertifikat pelatihan.\nATURAN SKORING (Rentang 0.0 - 3.0): Skor penuh jika pendidikan S1/pelatihan relevan. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Struktur dan Tanggung Jawab",
                "tabel_html": "" 
            },
            "2.3": {
                "no": "2.3",
                "judul": "2.3 Rasio SDM Pengembangan Masyarakat",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Rasio Jumlah SDM Pengembangan Masyarakat Terhadap Total SDM Unit",
                "rubrik_ai": "Cari bukti persentase/rasio spesifik jumlah personel tim CSR dibandingkan total karyawan unit. Beri skor 0.5 jika ada, 0.0 jika tidak.",
                "detail_ui": "**Aspek Penilaian:** Struktur dan Tanggung Jawab",
                "tabel_html": "" 
            },
            "3.1": {
                "no": "3.1",
                "judul": "3.1 Realisasi Dana Pengembangan Masyarakat",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Realisasi Dana Pelaksanaan Pengembangan Masyarakat (3 Tahun Berturut-turut)",
                "rubrik_ai": "Cari laporan/tabel realisasi pengeluaran khusus CSR yang tercatat '3 Tahun Berturut-turut' mundur dari tahun penilaian.\nATURAN SKORING (Rentang 0.0 - 2.0): Skor 2.0 jika lengkap 3 tahun berturut-turut. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Alokasi Dana Pengembangan Masyarakat",
                "tabel_html": "" 
            },
            "3.2": {
                "no": "3.2",
                "judul": "3.2 Perbandingan Dana Pengembangan Masyarakat dengan Laba",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Perbandingan Dana CSR Tahun Berjalan dengan Laba Unit Tahun Sebelumnya",
                "rubrik_ai": "Cari bukti rasio perbandingan Dana CSR Tahun N dengan Laba Bersih Tahun N-1. Skor penuh jika persentase perbandingan ditampilkan.",
                "detail_ui": "**Aspek Penilaian:** Alokasi Dana Pengembangan Masyarakat",
                "tabel_html": "" 
            },
            "4.1.1": {
                "no": "4.1.1",
                "judul": "4.1.1 Dokumen Pemetaan Sosial (Maksimal 4 Tahun Terakhir)",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Keberadaan dan Tahun Dokumen Pemetaan Sosial (Social Mapping)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial ini. Jika usianya LEBIH DARI 4 TAHUN ditarik mundur dari tahun penilaian (Misal dokumen 2019 untuk audit 2025/2026), WAJIB BERI SKOR 0.0. Jika tahunnya valid (maks 4 tahun terakhir), beri skor 0.5.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.2": {
                "no": "4.1.2",
                "judul": "4.1.2 Pembaruan (Update) Pemetaan Sosial 1 Tahun Terakhir",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Pembaruan (Update) Dokumen Pemetaan Sosial (Social Mapping) 1 Tahun Terakhir",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Cari bukti adendum/update laporan Pemetaan Sosial. Beri skor 0.5 HANYA JIKA ada bukti pembaruan data yang dilakukan DALAM 1 TAHUN TERAKHIR dari tahun penilaian berjalan. Jika usang, skor 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.a": {
                "no": "4.1.3.a",
                "judul": "4.1.3.a Substansi Pemetaan Sosial: Aktor dan Jaringan",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Pemetaan Aktor dan Jaringan Hubungan Antaraktor",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid (maks 4 tahun), beri skor 1.0 JIKA memuat identifikasi aktor dan jaringan. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.b": {
                "no": "4.1.3.b",
                "judul": "4.1.3.b Substansi Pemetaan Sosial: Posisi dan Peranan Sosial",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Deskripsi Posisi dan Peranan Sosial Aktor",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid, beri skor 1.0 JIKA merinci posisi dan peranan sosial aktor. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.c": {
                "no": "4.1.3.c",
                "judul": "4.1.3.c Substansi Pemetaan Sosial: Analisis Kekuatan dan Kepentingan Aktor",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Analisis Derajat Kekuatan (Power) dan Kepentingan (Interest) Aktor",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid, beri skor 1.0 JIKA memuat kuadran/analisis kekuatan dan kepentingan aktor. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.d": {
                "no": "4.1.3.d",
                "judul": "4.1.3.d Substansi Pemetaan Sosial: Identifikasi Forum Kepentingan Publik",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Identifikasi Mekanisme atau Forum Pembahasan Kepentingan Publik",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid, beri skor 1.0 JIKA mengidentifikasi forum publik lokal. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.e": {
                "no": "4.1.3.e",
                "judul": "4.1.3.e Substansi Pemetaan Sosial: Potensi Penghidupan Berkelanjutan",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Deskripsi Potensi Penghidupan Berkelanjutan (5 Asset)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid, beri skor 1.0 JIKA memuat potensi 5 aset penghidupan. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.f": {
                "no": "4.1.3.f",
                "judul": "4.1.3.f Substansi Pemetaan Sosial: Analisis Kebutuhan Masyarakat",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Analisis Kebutuhan Masyarakat untuk Mendukung Penghidupan Berkelanjutan",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid, beri skor 1.0 JIKA memuat analisis kebutuhan masyarakat. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.g": {
                "no": "4.1.3.g",
                "judul": "4.1.3.g Substansi Pemetaan Sosial: Jenis Kerentanan dan Kelompok Rentan",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Deskripsi Jenis-Jenis Kerentanan (Vulnerability) dan Kelompok Rentan",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid, beri skor 1.0 JIKA mendeskripsikan jenis kerentanan/kelompok rentan. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.h": {
                "no": "4.1.3.h",
                "judul": "4.1.3.h Substansi Pemetaan Sosial: Deskripsi Masalah Sosial",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Deskripsi Masalah Sosial di Masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid, beri skor 1.0 JIKA memuat deskripsi masalah sosial. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.1.3.i": {
                "no": "4.1.3.i",
                "judul": "4.1.3.i Substansi Pemetaan Sosial: Rekomendasi Program Pengembangan Masyarakat",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Rekomendasi Program Pengembangan Masyarakat (Comdev)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun dokumen Pemetaan Sosial. Jika usianya LEBIH DARI 4 TAHUN dari tahun audit, SKOR WAJIB 0.0 MESKIPUN ISINYA ADA. \nJika tahun valid, beri skor 1.0 JIKA memuat rekomendasi program. Jika tidak, 0.0.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Pemetaan Sosial",
                "tabel_html": "" 
            },
            "4.2.1": {
                "no": "4.2.1",
                "judul": "4.2.1 Pelibatan Pihak Terkait dalam Penyusunan Renstra",
                "skor_maksimal": 1.5,
                "kriteria_ai": "Pelibatan Pihak Terkait dalam Penyusunan Rencana Strategis (Renstra) Comdev",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Pastikan Renstra yang diunggah berlaku/beririsan dengan tahun penilaian. Cari bukti (notulensi/daftar hadir) pelibatan masyarakat. Beri skor 1.5 jika valid. 0.0 jika usang atau tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Renstra Comdev",
                "tabel_html": "" 
            },
            "4.2.2.a": {
                "no": "4.2.2.a",
                "judul": "4.2.2.a Substansi Renstra: Visi, Misi, dan Tujuan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Visi, Misi, dan Tujuan Pengembangan Masyarakat dalam Renstra",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Pastikan rentang tahun berlakunya Renstra mencakup tahun penilaian berjalan. JIKA RENSTRA KEDALUWARSA, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika memuat Visi, Misi, dan Tujuan.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Renstra Comdev",
                "tabel_html": "" 
            },
            "4.2.2.b": {
                "no": "4.2.2.b",
                "judul": "4.2.2.b Substansi Renstra: Analisis Isu Strategis",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Analisis Isu Strategis Pengembangan Masyarakat dalam Renstra",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Pastikan rentang tahun berlakunya Renstra mencakup tahun penilaian berjalan. JIKA RENSTRA KEDALUWARSA, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika memuat Analisis Isu Strategis.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Renstra Comdev",
                "tabel_html": "" 
            },
            "4.2.2.c": {
                "no": "4.2.2.c",
                "judul": "4.2.2.c Substansi Renstra: Program Jangka Panjang yang Dirinci Program Tahunan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Program Jangka Panjang (Multiyears) yang Dirinci Program Tahunan dalam Renstra",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa rentang waktu Renstra. JIKA RENSTRA KEDALUWARSA/TIDAK MENG-COVER TAHUN PENILAIAN, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika program jangka panjang dirinci tahunan.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Renstra Comdev",
                "tabel_html": "" 
            },
            "4.2.2.d": {
                "no": "4.2.2.d",
                "judul": "4.2.2.d Substansi Renstra: Indikator Program yang Terukur",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Indikator Program yang Terukur dalam Renstra",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: JIKA RENSTRA KEDALUWARSA, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika mencantumkan indikator program.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Renstra Comdev",
                "tabel_html": "" 
            },
            "4.2.2.e": {
                "no": "4.2.2.e",
                "judul": "4.2.2.e Substansi Renstra: Kebutuhan Anggaran Pembiayaan Program",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Kebutuhan Anggaran untuk Pembiayaan Program dalam Renstra",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: JIKA RENSTRA KEDALUWARSA, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika memuat proyeksi kebutuhan anggaran.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Renstra Comdev",
                "tabel_html": "" 
            },
            "4.2.2.f": {
                "no": "4.2.2.f",
                "judul": "4.2.2.f Substansi Renstra: Target Sasaran Program",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Target Sasaran Program (Individu, Kelompok, Organisasi) dalam Renstra",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: JIKA RENSTRA KEDALUWARSA, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika memuat target sasaran.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Renstra Comdev",
                "tabel_html": "" 
            },
            "4.2.2.g": {
                "no": "4.2.2.g",
                "judul": "4.2.2.g Substansi Renstra: Program Menjawab Kebutuhan Kelompok Rentan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Program Menjawab Kebutuhan Kelompok Rentan dalam Renstra",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: JIKA RENSTRA KEDALUWARSA, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika menjawab kebutuhan kelompok rentan.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Substansi Renstra Comdev",
                "tabel_html": "" 
            },
            "4.3.1": {
                "no": "4.3.1",
                "judul": "4.3.1 Pelibatan Pihak Terkait dalam Penyusunan Renja Tahunan",
                "skor_maksimal": 1.5,
                "kriteria_ai": "Pelibatan Pihak Terkait (Masyarakat/Pemerintah/Perusahaan Lain) dalam Penyusunan Rencana Kerja (Renja) Tahunan",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen Rencana Kerja (Renja) Tahunan HARUS mencantumkan tahun yang relevan dengan masa/tahun penilaian berjalan. Jika dokumen usang/berbeda tahun, SKOR WAJIB 0.0. Jika valid, skor 1.5 jika terbukti melibatkan masyarakat/stakeholder.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Renja Tahunan",
                "tabel_html": "" 
            },
            "4.3.2": {
                "no": "4.3.2",
                "judul": "4.3.2 Penjabaran Program menjadi Kegiatan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Penjabaran Program Menjadi Kegiatan-Kegiatan Spesifik dalam Renja",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun Renja. Jika usang, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika merinci program menjadi kegiatan spesifik.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Renja Tahunan",
                "tabel_html": "" 
            },
            "4.3.3": {
                "no": "4.3.3",
                "judul": "4.3.3 Indikator Kegiatan yang Terukur dalam Renja",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Indikator Kegiatan yang Terukur",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun Renja. Jika usang, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika mencantumkan indikator capaian terukur.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Renja Tahunan",
                "tabel_html": "" 
            },
            "4.3.4": {
                "no": "4.3.4",
                "judul": "4.3.4 Jadwal Pelaksanaan Kegiatan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Jadwal Waktu Pelaksanaan Kegiatan (Timeline/Gantt Chart)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun Renja. Jika usang, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika memuat matriks waktu pelaksanaan.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Renja Tahunan",
                "tabel_html": "" 
            },
            "4.3.5": {
                "no": "4.3.5",
                "judul": "4.3.5 Anggaran Masing-masing Kegiatan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Anggaran Masing-masing Kegiatan dalam Renja",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun Renja. Jika usang, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika merinci alokasi anggaran per kegiatan.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Renja Tahunan",
                "tabel_html": "" 
            },
            "4.3.6": {
                "no": "4.3.6",
                "judul": "4.3.6 Target Sasaran Kegiatan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Target Sasaran Kegiatan (Individu, Kelompok, Organisasi) dalam Renja",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Periksa tahun Renja. Jika usang, SKOR WAJIB 0.0. Jika valid, beri skor 0.5 jika menyebutkan target sasaran spesifik.",
                "detail_ui": "**Aspek Penilaian:** Perencanaan - Renja Tahunan",
                "tabel_html": "" 
            },
            "5.1": {
                "no": "5.1",
                "judul": "5.1 Kesesuaian Implementasi dengan Pemetaan Sosial",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Kesesuaian Implementasi Program/Kegiatan dengan Pemetaan Sosial (Social Mapping)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen Laporan Pelaksanaan/Implementasi HARUS merupakan laporan untuk tahun penilaian berjalan. Evaluasi keselarasan (*traceability*) antara program yang dilaporkan dengan rekomendasi di dokumen Pemetaan Sosial. Skor 2.0 jika selaras/merujuk eksplisit. Skor 0.0 jika laporan usang/beda tahun, atau implementasi melenceng dari Pemetaan Sosial.",
                "detail_ui": "**Aspek Penilaian:** Implementasi",
                "tabel_html": "" 
            },
            "5.2": {
                "no": "5.2",
                "judul": "5.2 Inovasi Sosial Hasil Program Pengembangan Masyarakat",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Inovasi Sosial yang Dihasilkan dari Program/Kegiatan Pengembangan Masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Laporan pelaksanaan HARUS sesuai tahun penilaian berjalan. Cari klaim Inovasi Sosial. Beri skor 3.0 jika ada. 0.0 jika tidak ada atau laporan usang.",
                "detail_ui": "**Aspek Penilaian:** Implementasi",
                "tabel_html": "" 
            },
            "5.3": {
                "no": "5.3",
                "judul": "5.3 Laporan Pelaksanaan Program",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Ketersediaan Laporan Pelaksanaan Program (Implementasi)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Cari dokumen 'Laporan Pelaksanaan Program'. Pastikan tahun laporan tersebut sesuai dengan tahun penilaian PROPER berjalan. Berikan skor 2.0 jika laporan realisasi/implementasi tahun terkait tersedia utuh. 0.0 jika tidak ada laporan, atau hanya mengunggah laporan tahun lampau yang kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Implementasi",
                "tabel_html": "" 
            },
            "5.4.1": {
                "no": "5.4.1",
                "judul": "5.4.1 Kesesuaian Implementasi dengan Renja: Program dan Kegiatan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Kesesuaian Implementasi Program dan Kegiatan dengan Rencana Kerja (Renja)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Laporan Implementasi dan Renja HARUS untuk tahun yang sama (tahun penilaian berjalan). Bandingkan keduanya. Beri skor 0.5 jika nama program/kegiatan selaras. 0.0 jika usang atau tidak selaras.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Kesesuaian dengan Renja",
                "tabel_html": "" 
            },
            "5.4.2": {
                "no": "5.4.2",
                "judul": "5.4.2 Kesesuaian Implementasi dengan Renja: Indikator Kegiatan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Kesesuaian Capaian Indikator Kegiatan dengan Rencana Kerja (Renja)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Berlaku hanya untuk dokumen tahun penilaian. Beri skor 0.5 jika capaian implementasi mencapai indikator Renja. 0.0 jika usang/tidak.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Kesesuaian dengan Renja",
                "tabel_html": "" 
            },
            "5.4.3": {
                "no": "5.4.3",
                "judul": "5.4.3 Kesesuaian Implementasi dengan Renja: Jadwal Pelaksanaan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Kesesuaian Jadwal Pelaksanaan Riil dengan Rencana Kerja (Renja)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Berlaku hanya untuk dokumen tahun penilaian. Beri skor 0.5 jika waktu implementasi sesuai jadwal Renja. 0.0 jika usang/tidak.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Kesesuaian dengan Renja",
                "tabel_html": "" 
            },
            "5.4.4": {
                "no": "5.4.4",
                "judul": "5.4.4 Kesesuaian Implementasi dengan Renja: Anggaran Kegiatan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Kesesuaian Realisasi Anggaran dengan Rencana Kerja (Renja)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Berlaku hanya untuk dokumen tahun penilaian. Beri skor 0.5 jika penyerapan anggaran sesuai Renja. 0.0 jika usang/tidak.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Kesesuaian dengan Renja",
                "tabel_html": "" 
            },
            "5.4.5": {
                "no": "5.4.5",
                "judul": "5.4.5 Kesesuaian Implementasi dengan Renja: Target Sasaran",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Kesesuaian Capaian Target Sasaran dengan Rencana Kerja (Renja)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Berlaku hanya untuk dokumen tahun penilaian. Beri skor 0.5 jika penerima manfaat tepat sasaran. 0.0 jika usang/tidak.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Kesesuaian dengan Renja",
                "tabel_html": "" 
            },
            "5.5": {
                "no": "5.5",
                "judul": "5.5 Partisipasi Pihak Terkait dalam Implementasi",
                "skor_maksimal": 1.5,
                "kriteria_ai": "Partisipasi Pihak-Pihak Terkait dalam Pelaksanaan Program dan Kegiatan",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Laporan HARUS untuk tahun penilaian berjalan. Cari bukti nyata partisipasi masyarakat. Skor max 1.5 jika ada. 0.0 jika usang atau nihil.",
                "detail_ui": "**Aspek Penilaian:** Implementasi",
                "tabel_html": "" 
            },
            "5.6": {
                "no": "5.6",
                "judul": "5.6 Implementasi Kegiatan yang Tidak Direncanakan",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Pelaporan Implementasi Program/Kegiatan yang Tidak Direncanakan (Insidental)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Laporan HARUS untuk tahun penilaian berjalan. Beri skor 2.0 jika perusahaan melaporkan program insidental secara transparan. 0.0 jika usang atau tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Implementasi",
                "tabel_html": "" 
            },
            "5.7.1": {
                "no": "5.7.1",
                "judul": "5.7.1 Hasil Program: Pengentasan Warga Miskin",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Jumlah dan Persentase Pengentasan Warga Miskin (Outcome)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen HARUS untuk tahun penilaian berjalan. Cari capaian pengentasan warga miskin. Skor 2.0 jika ada bukti, 0.0 jika usang atau nihil.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Hasil Program",
                "tabel_html": "" 
            },
            "5.7.2": {
                "no": "5.7.2",
                "judul": "5.7.2 Hasil Program: Peningkatan Pendapatan",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Peningkatan Pendapatan Warga Sasaran (Outcome)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen HARUS untuk tahun penilaian berjalan. Cari data peningkatkan income warga. Skor 2.0 jika ada, 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Hasil Program",
                "tabel_html": "" 
            },
            "5.7.3": {
                "no": "5.7.3",
                "judul": "5.7.3 Hasil Program: Kebijakan Pemerintah",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Jumlah Kebijakan Pemerintah Merespon Program (Outcome Kelembagaan)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen HARUS untuk tahun penilaian berjalan. Cari bukti terbitnya kebijakan/Perdes sebagai respon program. Skor 2.0 jika ada, 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Hasil Program",
                "tabel_html": "" 
            },
            "5.7.4": {
                "no": "5.7.4",
                "judul": "5.7.4 Hasil Program: Kontribusi Pelestarian Lingkungan",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Kontribusi Program Terhadap Pelestarian Lingkungan (Outcome Lingkungan)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen HARUS untuk tahun penilaian berjalan. Cari capaian lingkungan dari program Comdev. Skor 2.0 jika ada, 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Hasil Program",
                "tabel_html": "" 
            },
            "5.7.5": {
                "no": "5.7.5",
                "judul": "5.7.5 Hasil Program: Local Hero dan Regenerasinya",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Keberadaan Local Hero (Tokoh Penggerak Lokal) dan Proses Regenerasinya",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen HARUS untuk tahun penilaian berjalan. Beri skor 2.0 jika ada profil Local Hero & pembinaannya. 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Implementasi - Hasil Program",
                "tabel_html": "" 
            },
            "6.1": {
                "no": "6.1",
                "judul": "6.1 Sistem Tata Kelola Monitoring dan Evaluasi",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Sistem Tata Kelola Monitoring dan Evaluasi Pengembangan Masyarakat",
                "rubrik_ai": "Cari SOP tentang Monitoring & Evaluasi CSR. CATATAN: Sebagai dokumen statis, SOP TIDAK TERIKAT BATASAN TAHUN. Skor 1.0 jika SOP monev ada, 0.0 jika tidak.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi",
                "tabel_html": "" 
            },
            "6.2": {
                "no": "6.2",
                "judul": "6.2 Partisipasi Pihak Terkait dalam Monitoring dan Evaluasi",
                "skor_maksimal": 1.5,
                "kriteria_ai": "Partisipasi Pihak Terkait dalam Pelaksanaan Monitoring dan Evaluasi (Monev)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Pada laporan Evaluasi TAHUN BERJALAN, pastikan terdapat partisipasi masyarakat/pihak luar dalam memberi feedback. Skor 1.5 jika ada. SKOR 0.0 JIKA LAPORAN USANG atau monev sepihak.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi",
                "tabel_html": "" 
            },
            "6.3": {
                "no": "6.3",
                "judul": "6.3 Pengesahan Dokumen Evaluasi oleh Pimpinan Tertinggi",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Dokumen Evaluasi Disahkan oleh Pimpinan Tertinggi Unit",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Laporan Evaluasi yang diunggah harus mencantumkan tanda tangan/pengesahan pimpinan untuk TAHUN PENILAIAN TERSEBUT. Skor 2.0 jika disahkan, 0.0 jika usang/tidak disahkan.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi",
                "tabel_html": "" 
            },
            "6.4": {
                "no": "6.4",
                "judul": "6.4 Bukti Tertulis Proses dan Hasil Monitoring Berkala",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Bukti Tertulis Proses dan Hasil Monitoring Berkala",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Cari bukti logbook monitoring bulanan/triwulanan di TAHUN BERJALAN. Skor 0.5 jika ada, 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi",
                "tabel_html": "" 
            },
            "6.5": {
                "no": "6.5",
                "judul": "6.5 Bukti Perbaikan Program berdasarkan Hasil Monev",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Bukti Perbaikan Program dan Kegiatan Berdasarkan Hasil Monev",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Harus laporan TAHUN BERJALAN. Beri skor 0.5 jika ditemukan tindakan korektif program berdasarkan evaluasi sebelumnya. 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi",
                "tabel_html": "" 
            },
            "6.6": {
                "no": "6.6",
                "judul": "6.6 Indeks Kepuasan Masyarakat (IKM)",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Indeks Kepuasan Masyarakat (IKM) Program Pengembangan Masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Pastikan laporan Survei (IKM) yang diunggah mewakili sentimen pada rentang TAHUN PENILAIAN BERJALAN. Skor 1.0 jika hasil survei ada. SKOR 0.0 JIKA USANG/nihil.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi",
                "tabel_html": "" 
            },
            "6.7": {
                "no": "6.7",
                "judul": "6.7 Pembentukan dan Keberlanjutan Institusi Lokal",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Lahirnya dan Berkembangnya Institusi Ekonomi/Sosial Baru di Masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dalam laporan TAHUN BERJALAN, beri skor 0.5 jika dibuktikan berdirinya/berlanjutnya kelembagaan warga (Koperasi, dll). 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi - Keberlanjutan Program",
                "tabel_html": "" 
            },
            "6.8": {
                "no": "6.8",
                "judul": "6.8 Penerapan Pengetahuan/Keterampilan oleh Kelompok Sasaran",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Kelompok Sasaran Menerapkan Pengetahuan/Keterampilan Hasil Program",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Laporan TAHUN BERJALAN harus membuktikan kelompok warga mempraktikkan ilmu. 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi - Hasil Program",
                "tabel_html": "" 
            },
            "6.9": {
                "no": "6.9",
                "judul": "6.9 Penyebarluasan Pengetahuan/Keterampilan kepada Pihak Lain",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Kelompok Sasaran Mampu Menyebarluaskan Pengetahuan/Keterampilan kepada Pihak Lain",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dalam laporan TAHUN BERJALAN, beri skor 0.5 jika kelompok sasaran terbukti mengajarkan kembali ilmunya (multiplier effect). 0.0 jika usang/nihil.",
                "detail_ui": "**Aspek Penilaian:** Monitoring dan Evaluasi - Hasil Program",
                "tabel_html": "" 
            },
            "7.1": {
                "no": "7.1",
                "judul": "7.1 Memiliki Dokumen Stakeholder Engagement",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Ketersediaan Dokumen Stakeholder Engagement",
                "rubrik_ai": "SYARAT MUTLAK HARD-GATE: JIKA DOKUMEN BERUPA CV ATAU DOKUMEN ACAK = SKOR 0.0. Cari bukti bahwa perusahaan memiliki dokumen formal 'Pemetaan Pemangku Kepentingan' atau 'Stakeholder Engagement'. Beri skor 3.0 jika dokumen tersebut ada dan merujuk pada perusahaan yang dinilai. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Pelibatan Pemangku Kepentingan (Stakeholder Engagement)\n**Kriteria Verbatim:** 7.1. Memiliki dokumen stakeholder engagement.\n\n**Aturan Evaluasi Sistem:** Memverifikasi ketersediaan dokumen induk *Stakeholder Engagement* secara fisik sebelum membedah isinya di sub-kriteria selanjutnya.",
                "tabel_html": "" 
            },
            "7.1.1": {
                "no": "7.1.1",
                "judul": "7.1.1 Cakupan Aktor Pemangku Kepentingan (Pemerintah, Perusahaan, Masyarakat Sipil)",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Dokumen Stakeholder Engagement yang Mencakup 3 Pilar Aktor Utama (Pemerintah, Perusahaan, Organisasi Masyarakat Sipil)",
                "rubrik_ai": "SYARAT MUTLAK: Verifikasi ketat jenis dokumen. JIKA DOKUMEN BERUPA CV INDIVIDU, LANGSUNG SKOR 0.0. Jika valid, pastikan tahun relevan. Skor 3.0 jika aktor dari 3 pilar (Public, Private, Civil Society) dipetakan. 0.0 jika tidak.",
                "detail_ui": "**Aspek Penilaian:** Pelibatan Pemangku Kepentingan (Stakeholder Engagement)",
                "tabel_html": "" 
            },
            "7.1.2": {
                "no": "7.1.2",
                "judul": "7.1.2 Cakupan Wilayah Pemangku Kepentingan",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Cakupan Wilayah Pemangku Kepentingan yang Dijangkau",
                "rubrik_ai": "SYARAT MUTLAK: JIKA CV/DOKUMEN ACAK = SKOR 0.0. Skor 3.0 jika peta stakeholder merinci level jangkauan wilayah (Desa s/d Nasional). 0.0 jika tidak.",
                "detail_ui": "**Aspek Penilaian:** Pelibatan Pemangku Kepentingan (Stakeholder Engagement)",
                "tabel_html": "" 
            },
            "7.1.3": {
                "no": "7.1.3",
                "judul": "7.1.3 Cakupan Tema Stakeholder Engagement",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Cakupan Tema Stakeholder Engagement (Lingkungan, Sosial, Ekonomi)",
                "rubrik_ai": "SYARAT MUTLAK: JIKA CV/DOKUMEN ACAK = SKOR 0.0. Skor 3.0 jika tema engagement merangkum 3 pilar: Ekonomi, Sosial, Lingkungan. 0.0 jika tidak.",
                "detail_ui": "**Aspek Penilaian:** Pelibatan Pemangku Kepentingan (Stakeholder Engagement)",
                "tabel_html": "" 
            },
            "7.1.4": {
                "no": "7.1.4",
                "judul": "7.1.4 Pendekatan Relasi Pemangku Kepentingan",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Pendekatan Relasi Pemangku Kepentingan (Komunikasi, Konsultasi, Dialog, Kemitraan)",
                "rubrik_ai": "SYARAT MUTLAK: JIKA CV/DOKUMEN ACAK = SKOR 0.0. Skor 3.0 jika dokumen menjelaskan level pendekatan relasi (seperti: Kemitraan). 0.0 jika tidak.",
                "detail_ui": "**Aspek Penilaian:** Pelibatan Pemangku Kepentingan (Stakeholder Engagement)",
                "tabel_html": "" 
            },
            "7.1.5": {
                "no": "7.1.5",
                "judul": "7.1.5 Program Perwujudan Stakeholder Engagement",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Program/Kegiatan Perwujudan Stakeholder Engagement",
                "rubrik_ai": "SYARAT MUTLAK: JIKA CV/DOKUMEN ACAK = SKOR 0.0. Skor 3.0 jika hasil pemetaan tersebut menghasilkan Action Plan/Program nyata. 0.0 jika hanya analisis kertas.",
                "detail_ui": "**Aspek Penilaian:** Pelibatan Pemangku Kepentingan (Stakeholder Engagement)",
                "tabel_html": "" 
            },
            "7.1.6": {
                "no": "7.1.6",
                "judul": "7.1.6 Hasil Akhir (Outcome) Stakeholder Engagement",
                "skor_maksimal": 3.0,
                "kriteria_ai": "Hasil (Outcome) dari Pelaksanaan Stakeholder Engagement",
                "rubrik_ai": "SYARAT MUTLAK: JIKA CV/DOKUMEN ACAK = SKOR 0.0. Skor 3.0 jika dokumen melaporkan dampak positif/resolusi nyata dari engagement (misal MoU terbentuk). 0.0 jika nihil.",
                "detail_ui": "**Aspek Penilaian:** Pelibatan Pemangku Kepentingan (Stakeholder Engagement)",
                "tabel_html": "" 
            },
            "7.2.1": {
                "no": "7.2.1",
                "judul": "7.2.1 Adanya Serikat Pekerja",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Eksistensi Serikat Pekerja / Serikat Buruh di Lingkungan Internal Perusahaan",
                "rubrik_ai": "SYARAT MUTLAK: Verifikasi ini laporan perusahaan/PKB (BUKAN CV). Skor 1.0 jika memuat deklarasi sah keberadaan Serikat Pekerja internal. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Hubungan Kerja Internal",
                "tabel_html": "" 
            },
            "7.2.2": {
                "no": "7.2.2",
                "judul": "7.2.2 Memiliki Perjanjian Kerja Bersama (PKB)",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Kepemilikan Perjanjian Kerja Bersama (PKB) antara Manajemen dan Serikat Pekerja",
                "rubrik_ai": "SYARAT MUTLAK: Dokumen harus PKB/pelaporan internal (BUKAN CV). Skor 1.0 jika terbukti memiliki PKB bipartit. 0.0 jika hanya Peraturan Perusahaan sepihak.",
                "detail_ui": "**Aspek Penilaian:** Hubungan Kerja Internal",
                "tabel_html": "" 
            },
            "7.2.3": {
                "no": "7.2.3",
                "judul": "7.2.3 Tata Kelola Penyelesaian Perselisihan Hubungan Kerja",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Sistem Tata Kelola Penyelesaian Perselisihan Hubungan Industrial / Kerja",
                "rubrik_ai": "SYARAT MUTLAK: Cek dokumen sah. Skor 1.0 jika dokumen mengatur mekanisme penanganan keluhan (Grievance) bagi pekerja. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Hubungan Kerja Internal",
                "tabel_html": "" 
            },
            "7.2.4": {
                "no": "7.2.4",
                "judul": "7.2.4 Catatan Perselisihan Hubungan Kerja 2 Tahun Terakhir",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Keberadaan Catatan/Rekapitulasi Perselisihan Hubungan Kerja 2 Tahun Terakhir",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Cari logbook perselisihan dalam rentang 2 TAHUN TERAKHIR dari tahun penilaian. Catatan 'Zero Dispute' tertulis dinilai valid. Skor 0.5 jika transparan disajikan. 0.0 jika usang/disembunyikan.",
                "detail_ui": "**Aspek Penilaian:** Hubungan Kerja Internal",
                "tabel_html": "" 
            },
            "7.2.5": {
                "no": "7.2.5",
                "judul": "7.2.5 Penurunan Perselisihan Hubungan Kerja 2 Tahun Terakhir",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Tren Penurunan Kasus Perselisihan Hubungan Kerja dalam 2 Tahun Terakhir",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Analisis tren data 2 TAHUN TERAKHIR. Skor 0.5 jika jumlah perselisihan menurun, ATAU berhasil menahan status 0 (nihil) konflik. Skor 0.0 jika usang/kasus naik.",
                "detail_ui": "**Aspek Penilaian:** Hubungan Kerja Internal",
                "tabel_html": "" 
            },
            "7.3.1": {
                "no": "7.3.1",
                "judul": "7.3.1 Tata Kelola Penyelesaian Konflik Eksternal (Masyarakat/Pemerintah)",
                "skor_maksimal": 1.0,
                "kriteria_ai": "Sistem Tata Kelola Penyelesaian Konflik dengan Pihak Eksternal",
                "rubrik_ai": "SYARAT MUTLAK: Dokumen resmi perusahaan. Cari SOP Keluhan Eksternal. Skor 1.0 jika saluran pengaduan konflik eksternal tersedia tertulis. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Hubungan Eksternal",
                "tabel_html": "" 
            },
            "7.3.2": {
                "no": "7.3.2",
                "judul": "7.3.2 Catatan Konflik Eksternal 2 Tahun Terakhir",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Keberadaan Catatan/Rekam Jejak Konflik Eksternal 2 Tahun Terakhir",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Cari logbook keluhan eksternal 2 TAHUN TERAKHIR. Klaim 'Zero Conflict' dinilai valid. Skor 0.5 jika tercatat baik. 0.0 jika usang/tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Hubungan Eksternal",
                "tabel_html": "" 
            },
            "7.3.3": {
                "no": "7.3.3",
                "judul": "7.3.3 Penurunan Konflik Eksternal 2 Tahun Terakhir",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Tren Penurunan Kasus Konflik Eksternal dalam 2 Tahun Terakhir",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Analisis tren pengaduan warga 2 TAHUN TERAKHIR. Skor 0.5 jika terbukti menurun ATAU stagnan di titik nol kasus. Skor 0.0 jika usang/konflik naik.",
                "detail_ui": "**Aspek Penilaian:** Hubungan Eksternal",
                "tabel_html": "" 
            },
            "8.1.1": {
                "no": "8.1.1",
                "judul": "8.1.1 Diseminasi Best Practice melalui Jurnal Internasional/Buku Ber-ISBN",
                "skor_maksimal": 4.0,
                "kriteria_ai": "Praktek Pengelolaan Lingkungan/Masyarakat Terbaik di-Diseminasi melalui Jurnal Ilmiah Internasional atau Buku Ber-ISBN (3 Tahun Terakhir)",
                "rubrik_ai": "SYARAT MUTLAK KETAT: JIKA BUKAN TENTANG PERUSAHAAN (misal CV pribadi) = SKOR 0.0. Jurnal Internasional/Buku ISBN tersebut HARUS membahas *best practice* CSR perusahaan DAN diterbitkan MAKSIMAL 3 TAHUN ditarik mundur dari tahun audit. (Skor max 4.0).",
                "detail_ui": "**Aspek Penilaian:** Publikasi dan Penghargaan",
                "tabel_html": "" 
            },
            "8.1.2": {
                "no": "8.1.2",
                "judul": "8.1.2 Diseminasi Best Practice melalui Jurnal Ilmiah Nasional",
                "skor_maksimal": 2.0,
                "kriteria_ai": "Praktek Pengelolaan Lingkungan/Masyarakat Terbaik di-Diseminasi melalui Jurnal Ilmiah Nasional (3 Tahun Terakhir)",
                "rubrik_ai": "SYARAT MUTLAK KETAT: JIKA BUKAN TENTANG PERUSAHAAN (CV pribadi) = SKOR 0.0. Jurnal Ilmiah Nasional (SINTA, dll) HARUS terkait program CSR perusahaan DAN diterbitkan MAKSIMAL 3 TAHUN ditarik mundur dari tahun audit. (Skor max 2.0).",
                "detail_ui": "**Aspek Penilaian:** Publikasi dan Penghargaan",
                "tabel_html": "" 
            },
            "8.1.3": {
                "no": "8.1.3",
                "judul": "8.1.3 Penghargaan Bidang Pengembangan Masyarakat",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Perolehan Penghargaan Bidang Pengembangan Masyarakat dari Pemerintah/LSM",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Penghargaan HARUS didapatkan PADA TAHUN PENILAIAN BERJALAN. Penghargaan harus jelas untuk pilar Pengembangan Masyarakat (Comdev). Skor 0.5 jika valid. 0.0 jika penghargaan kedaluwarsa atau bukan untuk Comdev.",
                "detail_ui": "**Aspek Penilaian:** Publikasi dan Penghargaan\n**Catatan Validasi Waktu:** Piagam penghargaan akan diperiksa masa berlakunya agar relevan dengan tahun audit berjalan.",
                "tabel_html": "" 
            }
        },
"Tanggap Kebencanaan": {
            "1.1.1": {
                "no": "1.1.1",
                "judul": "1.1.1 Analisa Risiko dan Pemetaan Kerentanan Bencana",
                "skor_maksimal": 0.05,
                "kriteria_ai": "Analisa Risiko, Pemetaan Daerah Rawan Bencana, dan Pemetaan Kerentanan",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen Analisa Risiko/Pemetaan Daerah Rawan Bencana maksimal berumur 4 TAHUN TERAKHIR dari tahun penilaian. Jika usang (lebih dari 4 tahun), SKOR WAJIB 0.0. Jika valid, dokumen HARUS mencakup pemetaan kerentanan secara holistik di 4 aspek: 1) Fisik, 2) Ekonomi, 3) Sosial, dan 4) Lingkungan. Beri skor 0.05 jika analisis ini ada dan mencakup keempat aspek tersebut. 0.0 jika tidak lengkap/usang.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Pencegahan Bencana",
                "tabel_html": ""
            },
            "1.1.2": {
                "no": "1.1.2",
                "judul": "1.1.2 Pedoman / Prosedur Internal Penanganan Bencana",
                "skor_maksimal": 0.05,
                "kriteria_ai": "Pedoman, Standar, atau Prosedur (SOP) Penanganan Bencana",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Pedoman, Standar, atau SOP Penanganan Bencana ini TIDAK LAGI DIANGGAP STATIS. Usia dokumen maksimal 4 TAHUN TERAKHIR dari tahun penilaian. Jika usang, SKOR WAJIB 0.0. Jika valid, beri skor 0.05 jika SOP/Pedoman ini tertulis eksplisit. 0.0 jika tidak ditemukan atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Pencegahan Bencana",
                "tabel_html": ""
            },
            "1.1.3": {
                "no": "1.1.3",
                "judul": "1.1.3 Organisasi / Satuan Gugus Tugas Bencana",
                "skor_maksimal": 0.05,
                "kriteria_ai": "Pembentukan Satuan Gugus Tugas Bencana dan Keterlibatan dalam Forum Masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: SK Pembentukan Satgas/Gugus Tugas Bencana dan bukti keterlibatannya maksimal berumur 4 TAHUN TERAKHIR dari tahun penilaian. Jika usang, SKOR WAJIB 0.0. Jika valid, harus ada bukti SK Satgas internal DAN bukti satgas ini terlibat aktif memperkuat unit sosial masyarakat. Beri skor 0.05 jika lengkap. 0.0 jika tidak lengkap.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Pencegahan Bencana",
                "tabel_html": ""
            },
            "1.2.1": {
                "no": "1.2.1",
                "judul": "1.2.1 Pembuatan dan Penempatan Tanda Peringatan Rawan Bencana",
                "skor_maksimal": 0.05,
                "kriteria_ai": "Pembuatan dan penempatan tanda-tanda peringatan, bahaya, atau larangan di daerah rawan bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti dokumen (foto/laporan) maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.05 jika terdapat bukti perusahaan membuat/menempatkan tanda peringatan bahaya/larangan di daerah rawan bencana. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Mitigasi Bencana",
                "tabel_html": ""
            },
            "1.2.2": {
                "no": "1.2.2",
                "judul": "1.2.2 Pelatihan Dasar Kebencanaan bagi Staf Perusahaan",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Pelatihan dasar kebencanaan bagi staf perusahaan yang bertugas menangani bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti pelatihan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat bukti pelaksanaan pelatihan dasar kebencanaan untuk staf penanganan bencana. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Mitigasi Bencana",
                "tabel_html": ""
            },
            "1.2.3": {
                "no": "1.2.3",
                "judul": "1.2.3 Bantuan Relokasi Penduduk dari Daerah Rawan Bencana",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Membantu instansi pemerintah atau masyarakat dalam pemindahan penduduk dari daerah rawan ke aman.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti keterlibatan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat bukti dokumentasi perusahaan membantu pemindahan/relokasi penduduk ke daerah aman. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Mitigasi Bencana",
                "tabel_html": ""
            },
            "1.2.4": {
                "no": "1.2.4",
                "judul": "1.2.4 Bantuan Penyuluhan dan Peningkatan Kewaspadaan Masyarakat",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Membantu pemerintah dalam penyuluhan dan peningkatan kewaspadaan masyarakat terhadap bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti penyuluhan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika perusahaan terbukti melakukan penyuluhan/sosialisasi kewaspadaan bencana kepada masyarakat. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Mitigasi Bencana",
                "tabel_html": ""
            },
            "1.2.5": {
                "no": "1.2.5",
                "judul": "1.2.5 Perencanaan Daerah Penampungan Sementara dan Jalur Evakuasi",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Keterlibatan dalam perencanaan daerah penampungan sementara dan jalur evakuasi bencana di masyarakat.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen perencanaan/peta evakuasi maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika perusahaan terbukti ikut menyusun peta/perencanaan jalur evakuasi dan titik kumpul di masyarakat. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Mitigasi Bencana",
                "tabel_html": ""
            },
            "1.2.6": {
                "no": "1.2.6",
                "judul": "1.2.6 Pembuatan Bangunan Struktur Pencegah/Pengurang Dampak Bencana",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Pembuatan bangunan struktur (tanggul, dam, dll) untuk mencegah dan mengurangi dampak bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti pembangunan/pemeliharaan infrastruktur mitigasi maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika ada bukti fisik pembangunan struktur mitigasi bencana. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Mitigasi Bencana",
                "tabel_html": ""
            },
            "1.3.1": {
                "no": "1.3.1",
                "judul": "1.3.1 Pengaktifan Pos-Pos Siaga Bencana",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Membantu masyarakat Pengaktifan pos-pos siaga bencana dengan segenap unsur pendukungnya.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti laporan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat bukti keterlibatan perusahaan membantu masyarakat mengaktifkan pos-pos siaga bencana. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Kesiapsiagaan",
                "tabel_html": ""
            },
            "1.3.2": {
                "no": "1.3.2",
                "judul": "1.3.2 Pelatihan / Simulasi / Gladi Siaga Bencana",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Pelatihan siaga / simulasi / gladi / teknis bagi setiap sektor Penanggulangan bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti laporan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat bukti pelatihan/simulasi/gladi teknis untuk sektor penanggulangan bencana. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Kesiapsiagaan",
                "tabel_html": ""
            },
            "1.3.3": {
                "no": "1.3.3",
                "judul": "1.3.3 Inventarisasi Sumber Daya Pendukung Kedaruratan",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Inventarisasi sumber daya pendukung kedaruratan",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti laporan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat dokumen inventarisasi sumber daya pendukung kedaruratan. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Kesiapsiagaan",
                "tabel_html": ""
            },
            "1.3.4": {
                "no": "1.3.4",
                "judul": "1.3.4 Penyiapan Dukungan dan Mobilisasi Sumber Daya / Logistik",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Penyiapan dukungan dan mobilisasi sumberdaya/logistik.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti laporan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat bukti penyiapan dukungan dan logistik kebencanaan. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Kesiapsiagaan",
                "tabel_html": ""
            },
            "1.3.5": {
                "no": "1.3.5",
                "judul": "1.3.5 Penyiapan Sistem Informasi dan Komunikasi Terpadu",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Penyiapan sistem informasi dan komunikasi yang cepat dan terpadu guna mendukung tugas kebencanaan.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti laporan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat bukti penyiapan sistem informasi dan komunikasi terpadu. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Kesiapsiagaan",
                "tabel_html": ""
            },
            "1.3.6": {
                "no": "1.3.6",
                "judul": "1.3.6 Pemasangan Sistem Peringatan Dini (Early Warning System)",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Penyiapan dan pemasangan instrument sistem peringatan dini (early warning).",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti laporan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat bukti penyiapan/pemasangan instrumen peringatan dini. 0.0 jika tidak ada atau kedaluwarsa.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Kesiapsiagaan",
                "tabel_html": ""
            },
            "1.3.7": {
                "no": "1.3.7",
                "judul": "1.3.7 Penyusunan Rencana Kontinjensi (Contingency Plan)",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Penyusunan rencana kontinjensi (contingency plan)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen rencana kontinjensi maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika perusahaan memiliki/menyusun contingency plan. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Kesiapsiagaan",
                "tabel_html": ""
            },
            "1.3.8": {
                "no": "1.3.8",
                "judul": "1.3.8 Mobilisasi Sumber Daya Personil dan Sarana Peralatan",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Mobilisasi sumber daya (personil dan prasarana/sarana peralatan)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Bukti laporan maksimal berumur 4 TAHUN TERAKHIR. Beri skor 0.1 jika terdapat bukti mobilisasi personil dan prasarana/sarana. 0.0 jika tidak ada.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Program Kesiapsiagaan",
                "tabel_html": ""
            },
            "1.4.1": {
                "no": "1.4.1",
                "judul": "1.4.1 Pengkajian Cepat Lokasi, Kerusakan, dan Sumber Daya",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Pengkajian secara cepat dan tepat terhadap lokasi, kerusakan, kerugian, dan sumberdaya saat tanggap darurat.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Laporan pengkajian darurat HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika kejadian/bencana adalah masa lampau di luar tahun audit, SKOR WAJIB 0.0. Jika valid tahunnya, beri skor 0.1 jika ada kajian cepat kerusakan/kerugian. 0.0 jika tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Tanggap Darurat",
                "tabel_html": ""
            },
            "1.4.2": {
                "no": "1.4.2",
                "judul": "1.4.2 Penentuan Status Keadaan Darurat Bencana",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Penentuan status keadaan darurat bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Laporan HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika kejadian lampau di luar tahun audit, SKOR WAJIB 0.0. Jika valid, beri skor 0.1 jika ada penentuan status darurat. 0.0 jika tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Tanggap Darurat",
                "tabel_html": ""
            },
            "1.4.3": {
                "no": "1.4.3",
                "judul": "1.4.3 Penyelamatan dan Evakuasi Masyarakat",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Penyelamatan dan evakuasi masyarakat terkena bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Evakuasi HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika kejadian lampau di luar tahun audit, SKOR WAJIB 0.0. Jika valid, beri skor 0.1 jika ada bukti evakuasi/penyelamatan korban. 0.0 jika tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Tanggap Darurat",
                "tabel_html": ""
            },
            "1.4.4": {
                "no": "1.4.4",
                "judul": "1.4.4 Pemenuhan Kebutuhan Dasar Korban Bencana",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Pemenuhan kebutuhan dasar bagi masyarakat terdampak bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Penyaluran bantuan logistik/kebutuhan dasar HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika laporan bencana lampau, SKOR WAJIB 0.0. Jika valid, beri skor 0.1. 0.0 jika tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Tanggap Darurat",
                "tabel_html": ""
            },
            "1.4.5": {
                "no": "1.4.5",
                "judul": "1.4.5 Perlindungan Terhadap Kelompok Rentan",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Perlindungan terhadap kelompok rentan saat tanggap darurat bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Perlindungan HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika kejadian lampau, SKOR WAJIB 0.0. Jika valid, beri skor 0.1 jika memprioritaskan kelompok rentan. 0.0 jika tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Tanggap Darurat",
                "tabel_html": ""
            },
            "1.4.6": {
                "no": "1.4.6",
                "judul": "1.4.6 Pemulihan Segera Prasarana dan Sarana Vital",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Pemulihan dengan segera prasarana dan sarana vital pascabencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Pemulihan darurat HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika kejadian lampau, SKOR WAJIB 0.0. Jika valid, beri skor 0.1. 0.0 jika tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Tanggap Darurat",
                "tabel_html": ""
            },
            "1.5.1": {
                "no": "1.5.1",
                "judul": "1.5.1 Pembangunan Kembali Prasarana, Sarana, dan Pelayanan Publik",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Pembangunan kembali prasarana dan sarana serta pelayanan publik pascabencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Pelaksanaan pembangunan HARUS terjadi/berlanjut pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika proyek lampau di luar siklus audit, SKOR WAJIB 0.0. Beri skor 0.1 jika valid dan terbukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Pemulihan Pascabencana",
                "tabel_html": ""
            },
            "1.5.2": {
                "no": "1.5.2",
                "judul": "1.5.2 Pembangkitan Kembali Kehidupan Sosial Budaya Masyarakat",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Pembangkitan kembali kehidupan sosial budaya masyarakat pascabencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Rehabilitasi sosial HARUS terjadi/berlanjut pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika kejadian lampau di luar siklus audit, SKOR WAJIB 0.0. Beri skor 0.1 jika valid dan terbukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Pemulihan Pascabencana",
                "tabel_html": ""
            },
            "1.5.3": {
                "no": "1.5.3",
                "judul": "1.5.3 Penerapan Rancang Bangun Tepat dan Peralatan Tahan Bencana",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Penerapan rancang bangun yang tepat dan penggunaan peralatan yang lebih baik dan tahan bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Proses rancang bangun HARUS terjadi/berlanjut pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika proyek lampau di luar siklus audit, SKOR WAJIB 0.0. Beri skor 0.1 jika valid dan terbukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Pemulihan Pascabencana",
                "tabel_html": ""
            },
            "1.5.4": {
                "no": "1.5.4",
                "judul": "1.5.4 Partisipasi dan Peran Serta Lembaga serta Organisasi",
                "skor_maksimal": 0.1,
                "kriteria_ai": "Partisipasi dan peran serta lembaga dan organisasi dalam upaya pemulihan.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Kemitraan pemulihan HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Jika kejadian lampau di luar siklus audit, SKOR WAJIB 0.0. Beri skor 0.1 jika valid dan terbukti.",
                "detail_ui": "**Aspek Penilaian:** Keterlibatan Perusahaan - Pemulihan Pascabencana",
                "tabel_html": ""
            },
            "2.1": {
                "no": "2.1",
                "judul": "2.1 Jangkauan Program Tanggap Kebencanaan",
                "skor_maksimal": 2.5,
                "kriteria_ai": "Tingkat jangkauan wilayah program tanggap bencana perusahaan (Lokal hingga Internasional)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Bencana/Krisis yang ditangani HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Evaluasi jangkauan tertinggi (Internasional=2.5, Nasional=2.0, Provinsi=1.5, Daerah=1.0, Lokal=0.5). Skor 0.0 jika usang atau tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Jangkauan Program Perusahaan",
                "tabel_html": ""
            },
            "3.1": {
                "no": "3.1",
                "judul": "3.1 Model Kemitraan Tanggap Kebencanaan",
                "skor_maksimal": 2.5,
                "kriteria_ai": "Model Kemitraan yang dikembangkan perusahaan dalam penanggulangan bencana.",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Kemitraan tanggap bencana HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Skor proporsional berjenjang hingga 2.5 (Bantuan Internasional). Skor 0.0 jika kejadian lampau atau tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Model Kemitraan",
                "tabel_html": ""
            },
            "4.1": {
                "no": "4.1",
                "judul": "4.1 Analisa Risiko dengan Prinsip REA",
                "skor_maksimal": 1.5,
                "kriteria_ai": "Analisa resiko dan kerentanan menggunakan prinsip Rapid Environmental Impact Assessment in Disaster (REA)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK: Dokumen analisa maksimal berumur 4 TAHUN TERAKHIR dari tahun penilaian. Beri skor 1.5 jika terdapat bukti analisis menggunakan prinsip REA. 0.0 jika tidak ada atau usang.",
                "detail_ui": "**Aspek Penilaian:** Perbaikan Terus Menerus",
                "tabel_html": ""
            },
            "4.2": {
                "no": "4.2",
                "judul": "4.2 Pemanfaatan Hasil Analisa untuk Program Pemberdayaan",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Hasil analisa resiko digunakan sebagai perbaikan dan penyusunan program pemberdayaan masyarakat",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Pelaksanaan perbaikan program HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Beri skor 0.5 jika hasil analisa digunakan sebagai dasar perbaikan program. 0.0 jika kejadian lampau atau tidak terbukti.",
                "detail_ui": "**Aspek Penilaian:** Perbaikan Terus Menerus",
                "tabel_html": ""
            },
            "4.3": {
                "no": "4.3",
                "judul": "4.3 Pelibatan Masyarakat Binaan Lama dan Baru",
                "skor_maksimal": 2.5,
                "kriteria_ai": "Melibatkan masyarakat binaan existing dan masyarakat binaan baru dalam penanggulangan bencana",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Pelibatan masyarakat HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Beri skor 2.5 jika menggerakkan binaan lama dan baru di daerah bencana. 0.0 jika kejadian lampau atau tidak terbukti.",
                "detail_ui": "**Aspek Penilaian:** Perbaikan Terus Menerus",
                "tabel_html": ""
            },
            "4.4": {
                "no": "4.4",
                "judul": "4.4 Program Pemberdayaan Jangka Panjang di Daerah Bencana",
                "skor_maksimal": 2.5,
                "kriteria_ai": "Program pemberdayaan bersifat jangka panjang (infrastruktur, sosial-budaya, rancang bangun tahan bencana)",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Laporan program pemberdayaan HARUS terjadi/berjalan pada SIKLUS TAHUN PENILAIAN BERJALAN. Beri skor 2.5 jika mencakup prasarana, sosial budaya, dan rancang bangun. 0.0 jika tidak utuh atau lampau.",
                "detail_ui": "**Aspek Penilaian:** Perbaikan Terus Menerus",
                "tabel_html": ""
            },
            "5.1": {
                "no": "5.1",
                "judul": "5.1 Komitmen Internal: Tidak Ada PHK Saat Bencana",
                "skor_maksimal": 0.5,
                "kriteria_ai": "Komitmen perusahaan untuk tidak melakukan PHK (Pemutusan Hubungan Kerja) terhadap karyawan tetap dan outsourcing saat terdampak bencana",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Peristiwa/Krisis HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Beri skor 0.5 jika ada deklarasi/bukti komitmen tidak mem-PHK karyawan saat terdampak bencana. 0.0 jika kejadian lampau atau tidak ada bukti.",
                "detail_ui": "**Aspek Penilaian:** Komitmen Internal",
                "tabel_html": ""
            },
          "6.1": {
                "no": "6.1",
                "judul": "6.1 Tingkat Partisipasi Penanganan Bencana",
                "skor_maksimal": 10.0,
                "kriteria_ai": "Tingkat partisipasi berdasarkan jumlah penerima manfaat, luas area, dan tingkat kesulitan",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Penanganan Bencana HARUS terjadi pada SIKLUS TAHUN PENILAIAN BERJALAN. Evaluasi kelengkapan data jumlah korban, luas area, dan kesulitan. Beri skor proporsional maksimal 10.0 jika laporan sangat rinci dan masif. 0.0 jika tidak terbukti atau merupakan bencana lampau.",
                "detail_ui": "**Aspek Penilaian:** Tingkat Partisipasi Penanganan Bencana\n**Kriteria Verbatim:** Tingkat partisipasi perusahaan yang ditentukan berdasarkan: a. Jumlah orang yang mendapatkan bantuan; b. Luas area yang mendapatkan bantuan; c. Tingkat kesulitan terhadap: 1. akses menuju lokasi penanganan bencana; dan 2. koordinasi dengan mitra di lokasi penanganan bencana. Masuk ke dalam penilaian: 10% tertinggi hingga 10% terendah.",
                "tabel_html": ""
            }
        },
        "Inovasi Sosial": {
            "1": {
                "no": "1",
                "judul": "1. Kebaruan (Novelty) Inovasi Sosial",
                "skor_maksimal": 5.0,
                "kriteria_ai": "Unsur kebaruan (baru di sektor/kawasan tersebut, aplikasi cara baru) dan orisinalitas (keunikan) program",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Dokumen Inovasi Sosial HARUS relevan dan diajukan pada SIKLUS TAHUN PENILAIAN BERJALAN. Evaluasi klaim program. Beri skor penuh 5.0 JIKA dokumen secara eksplisit membuktikan program memiliki unsur KEBARUAN (metode/hal baru yang belum pernah diterapkan di kawasan/sektor tersebut) DAN memiliki unsur orisinalitas/keunikan. JIKA program terdeteksi hanya sebagai CSR reguler (Business as Usual) tanpa unsur kebaruan yang jelas, SKOR WAJIB 0.0.",
                "detail_ui": "**Aspek Penilaian:** Inovasi Sosial - Kebaruan\n**Kriteria Verbatim:** a. merupakan hal baru yang diterapkan di sektor tersebut di kawasan tersebut atau di aplikasikan dengan cara atau hal-hal yang baru; b. Memiliki unsur orisinal dan unik.",
                "tabel_html": ""
            },
            "2": {
                "no": "2",
                "judul": "2. Unsur Core Competency (Kompetensi Inti)",
                "skor_maksimal": 6.0,
                "kriteria_ai": "Transfer pengetahuan/keterampilan core competency, berbasis dampak daur hidup (LCA), dan responsif krisis",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Dokumen HARUS relevan dengan SIKLUS TAHUN PENILAIAN BERJALAN. Evaluasi 3 elemen mutlak: a) Adanya transfer pengetahuan/keterampilan inti (core competency) perusahaan kepada masyarakat; b) Program dikembangkan secara ilmiah berbasis hasil analisis dampak daur hidup (Life Cycle Assessment / LCA); c) Inovasi memiliki sensitivitas dan responsif menjadi solusi saat kondisi krisis/bencana di masyarakat. Beri skor penuh 6.0 jika ketiga unsur ini terbukti eksplisit. 0.0 jika hanya CSR biasa (tidak ada transfer core competency atau tidak berbasis LCA).",
                "detail_ui": "**Aspek Penilaian:** Inovasi Sosial - Core Competency\n**Kriteria Verbatim:** a. Transfer pengetahuan atau keterampilan core competency; b. Dikembangkan berdasarkan hasil analisis intepretasi penilaian dampak daur hidup; c. Memiliki unsur sensitifitas dan daya rensponsif terhadap kondisi krisis di masyarakat akibat bencana.",
                "tabel_html": ""
            },
            "3": {
                "no": "3",
                "judul": "3. Status Inovasi Sosial (Keberlanjutan, Scaling/Replikasi, Perubahan Sistemik)",
                "skor_maksimal": 9.0,
                "kriteria_ai": "Status pencapaian inovasi sosial yang mencakup keberlanjutan, perluasan skala/replikasi, dan perubahan sistemik",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Dokumen evaluasi/laporan HARUS terjadi dan relevan pada SIKLUS TAHUN PENILAIAN BERJALAN. Evaluasi kelengkapan 3 elemen transformasi: a) Keberlanjutan (bukti kemandirian program tanpa kebergantungan absolut pada perusahaan); b) Scaling/Replikasi (bukti inovasi diperluas dampaknya atau diduplikasi ke lokasi/kelompok lain); c) Perubahan Sistemik (bukti adanya perubahan kebijakan/peraturan lokal, pergeseran norma sosial, atau perubahan struktur rantai pasok ekonomi secara permanen). Beri skor penuh 9.0 JIKA KETIGA elemen ini terbukti secara eksplisit dan saling mendukung. JIKA gagal membuktikan salah satu elemen (misal: belum ada perubahan sistemik/replikasi), SKOR WAJIB 0.0.",
                "detail_ui": "**Aspek Penilaian:** Inovasi Sosial - Status Inovasi\n**Kriteria Verbatim:** a. Keberlanjutan; b. Scalling / Replikasi; c. Perubahan Sistemik.",
                "tabel_html": ""
            },
            "4": {
                "no": "4",
                "judul": "4. Efektifitas Inovasi Sosial (Menggunakan SROI)",
                "skor_maksimal": 10.0,
                "kriteria_ai": "Pengukuran efektifitas penyelesaian masalah sosial menggunakan metode SROI yang kredibel dan transparan",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Dokumen Kajian/Laporan SROI HARUS diajukan untuk SIKLUS TAHUN PENILAIAN BERJALAN. PERINGATAN KETAT: Jangan berikan skor hanya karena menemukan kata 'SROI' atau rasio angka. Dokumen HARUS membuktikan secara efektif penyelesaian masalah sosial melalui metodologi SROI yang utuh. Sistem WAJIB memverifikasi kehadiran 6 komponen penyusun kredibilitas kajian/pelaksana SROI di dalam dokumen: 1) Pengalaman, 2) Transparansi (asumsi dan proksi keuangan dijelaskan), 3) Kualitas, 4) Kompetensi, 5) Keahlian tertentu/Spesialis, dan 6) Reputasi. Beri skor PENUH 10.0 HANYA JIKA evaluasi menggunakan alat ukur SROI secara nyata dan memenuhi keenam komponen tersebut. JIKA alat ukurnya bukan SROI, atau metodologinya tidak transparan/tidak memenuhi ke-6 komponen, atau dokumen usang, SKOR WAJIB 0.0.",
                "detail_ui": "**Aspek Penilaian:** Inovasi Sosial - Efektifitas\n**Kriteria Verbatim:** Efektifitas (menggunakan SROI sebagai alat ukur): Efektif menyelesaikan masalah/ kebutuhan sosial. Komponen Penyusun: Pengalaman, Transparansi, Kualitas, Kompetensi, Memiliki keahlian tertentu (spesialis), Reputasi.",
                "tabel_html": ""
            },
            "5": {
                "no": "5",
                "judul": "5. Menjawab Kebutuhan & Meningkatkan Kapasitas Sosial (SROI)",
                "skor_maksimal": 20.0,
                "kriteria_ai": "Penyelesaian masalah sosial dan peningkatan kapasitas masyarakat yang diukur dengan 5 tahapan komprehensif SROI",
                "rubrik_ai": "SYARAT WAKTU MUTLAK KETAT: Dokumen Laporan SROI HARUS relevan untuk SIKLUS TAHUN PENILAIAN BERJALAN. Kriteria ini berbobot sangat masif (20 poin). AI WAJIB memverifikasi secara ketat ketersediaan 5 (lima) komponen penyusun laporan SROI di dalam dokumen: 1) Ruang lingkup dan identifikasi stakeholder; 2) Pemetaan outcome dari setiap stakeholder; 3) Penetapan indikator dan nilai (proxy keuangan) dari setiap outcome; 4) Fiksasi dampak (memperhitungkan deadweight, attribution, drop-off, displacement); 5) Perhitungan akhir rasio SROI. Selain itu, narasi laporan harus membuktikan adanya peningkatan kapasitas masyarakat (menciptakan peran/hubungan baru, mengembangkan kemampuan/aset). Beri skor PENUH 20.0 HANYA JIKA kelima tahapan metodologi SROI ini terpampang nyata, lengkap, dan membuktikan penyelesaian masalah sosial. SKOR WAJIB 0.0 jika ada SATU SAJA komponen laporan yang dihilangkan, metodologinya cacat, atau dokumennya usang.",
                "detail_ui": "**Aspek Penilaian:** Inovasi Sosial - Menjawab Kebutuhan & Meningkatkan Kapasitas Sosial\n**Kriteria Verbatim:** Dapat menyelesaikan kebutuhan/permasalahan sosial, meningkatkan kapasitas masyarakat untuk bertindak antara lain dengan menciptakan peran dan hubungan baru, mengembangkan aset dan kemampuan dan/atau menggunakan aset dan sumberdaya dengan lebih baik. Komponen Laporan: Ruang lingkup dan identifikasi stakeholder, Pemetaan outcome, Penetapan indikator dan nilai, Fiksasi dampak, Perhitungan SROI.",
                "tabel_html": ""
            },
            "6": {
                "no": "6",
                "judul": "6. Penilaian Dewan Pertimbangan PROPER (Hak Prerogatif)",
                "skor_maksimal": 50.0,
                "kriteria_ai": "Penilaian subjektif dan holistik dari Dewan Pertimbangan PROPER LHK terkait efektivitas dan dampak inovasi sosial",
                "rubrik_ai": "SYARAT MUTLAK KETAT (HAK PREROGATIF DEWAN): Kriteria ini bernilai 50 poin dan murni merupakan wewenang Dewan Pertimbangan PROPER (bukan ranah self-assessment perusahaan). PERINGATAN UNTUK AI: JANGAN PERNAH memberikan skor 50.0 jika dokumen yang diunggah hanya berupa laporan/klaim sepihak dari perusahaan. Berikan skor 50.0 HANYA JIKA dokumen yang diunggah adalah BUKTI RESMI (Surat Keputusan, Berita Acara, Lembar Penilaian Resmi, atau Pengumuman dari KLHK/Dewan Pertimbangan PROPER) pada siklus tahun berjalan yang secara eksplisit menyatakan bahwa inovasi sosial perusahaan dinilai 'Sesuai' dan mendapatkan poin ini. Jika tidak ada bukti legal dari pemerintah/DP PROPER, SKOR WAJIB 0.0, dan berikan catatan evaluasi: 'Penilaian ini menunggu keputusan mutlak dari sidang Dewan Pertimbangan PROPER'.",
                "detail_ui": "**Aspek Penilaian:** Inovasi Sosial - Penilaian Dewan Pertimbangan\n**Kriteria Verbatim:** Penilaian dewan pertimbangan Proper mengenai efektifitas inovasi sosial, kemampuan inovasi menjawab kebutuhan sosial dan kemampuan inovasi meningkatkan kapasitas sosial. \n\n⚠️ **CATATAN SISTEM:** Poin ini adalah hak prerogatif Dewan Pertimbangan LHK saat tahap presentasi kandidat. AI tidak akan memberikan skor pada tahap *self-assessment* mandiri kecuali terdapat bukti rekam jejak penilaian resmi dari KLHK.",
                "tabel_html": ""
            }
        }

    }
}