# 🚀 rdp-codespace-ubuntu
**Free RDP via GitHub Codespaces (Ubuntu) – tanpa ribet, langsung jalan!**  

Hanya dengan membuat repo GitHub (bahkan cukup README aja), kamu bisa dapetin **Remote Desktop gratis** dengan spesifikasi **dewa (RAM 15GB)** 

> ⚠️ **PENTING**: Ikuti tutorial ini dengan benar biar nggak gagal dapet RDP.  

---

## ✨ Fitur
- ✅ Gratis 100% via GitHub Codespaces  
- ✅ RAM 15GB (powerful banget 🚀)  
- ✅ Setup super gampang (full otomatis)  
- ✅ Bisa diakses lewat [Chrome Remote Desktop](https://remotedesktop.google.com) atau aplikasinya di HP  

---

## 📋 Tutorial Lengkap

### 1. Persiapan
1. Buat akun GitHub & bikin repo baru (atau pakai yang sudah ada, asal ada minimal 1 commit).  
2. Buka 👉 [https://github.com/features/codespaces](https://github.com/features/codespaces)  
3. Klik **Get started for free**  
4. Klik **New codespace**  
5. Pilih repo kamu tadi → **Region** pilih server terdekat (misalnya *South Asia* biar low ping ⚡).  

---

### 2. Setup Codespace
6. Tunggu Codespace terbuka → tampilannya mirip **VSCode**.  
7. Buka **Terminal** lalu jalankan perintah berikut:  

   ```bash
   git clone https://github.com/syaaikoo/rdp-codespace-ubuntu.git    && cd rdp-codespace-ubuntu && ls
   ```

   📂 Kamu bakal lihat 3 file:  
   - `main.py`  
   - `auto-active.py`  
   - `README.md`

---

### 3. Setup Chrome Remote Desktop
8. Buka [Chrome Remote Desktop](https://remotedesktop.google.com) (atau install app di Play Store).  
9. Klik menu **☰** (pojok kiri atas) → pilih **Siapkan melalui SSH** → lanjut terus sampai muncul halaman **Siapkan komputer lain**.  
10. Copy perintah paling bawah (yang untuk Debian Linux).  
    > ⚠️ **Jangan tutup tab Chrome Remote Desktop!** Kalau ditutup, AuthKey bisa berubah.  

---

### 4. Jalankan Script
11. Balik ke terminal Codespace → jalankan:  

   ```bash
   sudo python main.py
   ```

12. Paste perintah SSH yang tadi kamu copy → tekan **Enter** → tunggu proses otomatis sampai selesai.  
13. Setelah itu jalankan script auto-keepalive biar Codespace nggak disconnect:  

   ```bash
   sudo python auto-active.py
   ```

---

### 5. Login RDP
14. **Jangan reload tab Codespace!** Biarkan tetap terbuka.  
15. Balik ke [Chrome Remote Desktop](https://remotedesktop.google.com) / aplikasi HP.  
16. Akan muncul komputer baru → klik dan masuk dengan password default:  

   ```
   123456
   ```

   🎉 Boom! Sekarang kamu punya **RDP gratis dengan RAM 15GB** siap dipakai.  

---

## 📦 Rencana Update
- [ ] Support desktop environment lain: KDE Plasma, GNOME, Cinnamon, dll  
- [ ] Auto-reconnect lebih stabil  
- [ ] UI setup lebih simpel  

---

## 🖼️ Preview
> Tampilan kurang lebih akan seperti ini setelah berhasil setup:  

![RDP Codespace Preview](https://i.ibb.co/bsxnpp1/codespace-rdp-preview.png)  

---

## ❤️ Support
Kalau tutorial ini bermanfaat, jangan lupa kasih **⭐ star** di repo ini biar makin semangat update 🚀  
