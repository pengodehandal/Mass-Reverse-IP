# Mass Reverse IP Lookup 🚀

Yo, welcome to **Mass Reverse IP Lookup**! Tools kece buat kalian yang pengen ngecek website-website yang ada di balik IP atau domain. Dengan menggunakan API dari [WebScan] (https://api.webscan.cc/), kalian bisa cari tau domain apa aja yang share server yang sama dengan domain yang kalian input. 

Tools ini juga punya fitur **multi-threading**, jadi proses lookup bisa jauh lebih cepat. Biar ga nunggu lama! 😎

## Fitur 🔥

- **Reverse IP Lookup**: Cek domain-domain yang ada di balik satu IP atau domain.
- **Multi-threading**: Proses lookup bisa berjalan lebih cepet dengan maksimal 30 thread.
- **Error handling**: Kalo ada error atau domain gak valid, langsung di-skip, biar ga ngabisin waktu.
- **Save Results**: Semua domain yang ketemu disimpan otomatis ke dalam file teks, jadi bisa digunakan lagi.
- **Custom Threads**: Kamu bisa custom jumlah threads sesuai kebutuhan! Maksimal 30 thread biar proses cepat.

## Prasyarat ⚙️

Sebelum kalian mulai, pastiin dulu hal-hal ini:

- Python 3.6+ udah terinstall di komputer kalian.
- Koneksi internet yang stabil, biar ga gangguan pas proses.
  
## Cara Install 💻

1. **Clone repository ini atau download**:

   ```bash
   git clone https://github.com/pengodehandal/Mass-Reverse-IP.git
   cd Mass-Reverse-IP
   pip install -r requirements.txt
   python3 rev.py
   

   
