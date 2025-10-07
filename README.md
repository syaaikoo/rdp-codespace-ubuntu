# rdp-codespace-ubuntu
**Free RDP via GitHub Codespaces (Ubuntu + XFCE4 / KDE Plasma) – tanpa ribet, langsung jalan!**  

<img>https://media.tenor.com/N5fU8iyU9F4AAAAi/shigure-ui-dance.gif</img>

Hanya dengan membuat repo GitHub (bahkan cukup README aja), kamu bisa dapetin **Remote Desktop gratis** dengan spesifikasi **dewa (RAM 15GB)**   

> ⚠️ **PENTING**: Ikuti tutorial ini dengan benar biar enggak gagal.  

---

## ✨ Fitur
- ✅ Gratis 100% via GitHub Codespaces  
- ✅ RAM 15GB lupa spek cpu nya intinya (powerful banget 🚀)  
- ✅ Setup super gampang (full otomatis)  
- ✅ Pilihan Desktop Environment: **XFCE4** atau **KDE Plasma**  
- ✅ Bisa diakses lewat [Chrome Remote Desktop](https://remotedesktop.google.com) atau aplikasinya di HP  

---

## 🧠 Perbandingan XFCE4 vs KDE Plasma

| Aspek | XFCE4 | KDE Plasma |
|-------|--------|-------------|
|  Performa | Super ringan | Sedikit lebih berat |
|  Tampilan | Minimalis & cepat | Modern & kaya efek |
|  Resource | Rendah (hemat CPU/RAM) | Tinggi (lebih berat) |
|  Kompatibilitas | Sangat stabil | Kadang butuh tweak tambahan |
|  Cocok untuk | Server ringan, low-end | PC/laptop kuat, user estetis |
|  Script | `crd-xfce.py` | `crd-kde-plasma.py` |

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
   git clone https://github.com/syaaikoo/rdp-codespace-ubuntu.git && cd rdp-codespace-ubuntu && ls
   ```

   📂 Kamu bakal lihat beberapa file:  
   - `crd-xfce.py`  
   - `crd-kde-plasma.py`  
   - `auto-active.py`  
   - `README.md`

---

### 3. Setup Chrome Remote Desktop
8. Buka [Chrome Remote Desktop](https://remotedesktop.google.com) (atau install app di Play Store).  
9. Klik menu **☰** (pojok kiri atas) → pilih **Siapkan melalui SSH** → lanjut terus sampai muncul halaman **Siapkan komputer lain**.  
10. Copy perintah paling bawah (yang untuk Debian Linux).  
    > ⚠️ **Jangan hapus tab Chrome Remote Desktop!** Kalau dihapus, AuthKey bisa berubah.  

---

### 4. Jalankan Script
11. Balik ke terminal Codespace → jalankan sesuai environment yang kamu mau:  

   Untuk **XFCE4 (ringan & cepat):**
   ```bash
   sudo python crd-xfce.py
   ```

   Untuk **KDE Plasma (tampilan keren):**
   ```bash
   sudo python crd-kde-plasma.py
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

   Dan yapp! sekarang kmuu udahh punya **RDP gratis dengan RAM 15GB** siap dipakai apapun itu.  

---

## 📦 Next Update
- [ ] Support tambahan desktop environment (GNOME, MATE, Cinnamon)  
- [ ] Auto-reconnect lebih stabil  
- [ ] Deteksi error otomatis  
- [ ] UI setup via python cli  

---

## 🖼️ Preview
> Tampilan jika kalian memilih **KDE-PLASMA** kurang lebih akan seperti ini setelah berhasil setup:  

![RDP Codespace Preview xfce](https://kde.org/content/plasma-desktop/plasma-launcher.png)

> Tampilan jika kalian memilih **XFCE4** kurang lebih akan seperti ini setelah berhasil setup:  

![RDP Codespace Preview xfce](https://docs.vultr.com/public/doc-assets/2091/9d5e1501-4ec5-4be6-95dd-6687764039c3.png)

---

## ❤️ Support
Kalau tutorial dan script repo ini bermanfaat, tolong jangan lupa kasih **⭐ star** 
di repo ini biar airaaa makin semangat update ehehehe!!!!  

---

Made with 💻 by **©AiraaCheisyaa**
<div align="center">  
  <img src="https://media.tenor.com/eeur7VuCbmkAAAAj/anime-rikka.gif" width="220"/>  
  <br>  
  <b>see youu, thanks for visiting my repositori</b>  
</div>
