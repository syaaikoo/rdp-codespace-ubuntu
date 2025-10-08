# rdp-codespace-ubuntu

Free RDP via GitHub Codespaces (Ubuntu + XFCE4 / KDE Plasma) – tanpa ribet, langsung jalan!

<div align="center">
  
[![Stars](https://img.shields.io/github/stars/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/stargazers)
[![Issues](https://img.shields.io/github/issues/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/issues)
[![Forks](https://img.shields.io/github/forks/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/forks)
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-24292e?style=for-the-badge&logo=github)](https://codespaces.new/syaaikoo/rdp-codespace-ubuntu)
<a href="https://instagram.com/syaaikoo">
  <img src="https://img.shields.io/badge/Instagram-syaaikoo-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
</a>

<br><br>
<img src="https://media.tenor.com/N5fU8iyU9F4AAAAi/shigure-ui-dance.gif" alt="fun gif" height="140" />
</div>

> ⚠️ PENTING: Ikuti panduan dengan teliti agar tidak gagal. Jangan tutup atau reload tab Codespace saat proses berjalan.

---

## Daftar Isi
- [✨ Fitur](#-fitur)
- [🧠 Pilihan Desktop Environment](#-pilihan-desktop-environment)
- [📊 Perbandingan XFCE4 vs KDE Plasma](#-perbandingan-xfce4-vs-kde-plasma)
- [🧰 Prasyarat](#-prasyarat)
- [📋 Tutorial Lengkap](#-tutorial-lengkap)
  - [1) Persiapan](#1-persiapan)
  - [2) Setup Codespace](#2-setup-codespace)
  - [3) Setup Chrome Remote Desktop](#3-setup-chrome-remote-desktop)
  - [4) Jalankan Script](#4-jalankan-script)
  - [5) Login RDP](#5-login-rdp)
- [🖼️ Preview](#️-preview)
- [🧭 Roadmap / Next Update](#-roadmap--next-update)
- [❤️ Support](#️-support)

---

## ✨ Fitur
- ✅ Gratis 100% via GitHub Codespaces  
- ✅ RAM ±15GB, CPU powerful (cukup buat kerja berat) 🚀  
- ✅ Setup super gampang (otomatis)  
- ✅ Pilihan Desktop Environment: **XFCE4** atau **KDE Plasma**  
- ✅ Akses via [Chrome Remote Desktop](https://remotedesktop.google.com) (web/Android)

---

## 🧠 Pilihan Desktop Environment
- XFCE4 → ringan, cepat, hemat resource  
- KDE Plasma → modern, kaya fitur & visual

File script:
- `crd-xfce.py` (XFCE4)
- `crd-kde-plasma.py` (KDE Plasma)

---

## 📊 Perbandingan XFCE4 vs KDE Plasma

| Aspek            | XFCE4                   | KDE Plasma                         |
|------------------|-------------------------|------------------------------------|
| Performa         | Super ringan            | Sedikit lebih berat                |
| Tampilan         | Minimalis & cepat       | Modern & kaya efek                 |
| Resource         | Rendah (hemat CPU/RAM)  | Lebih tinggi                       |
| Kompatibilitas   | Sangat stabil           | Kadang butuh tweak tambahan        |
| Cocok untuk      | Server ringan, low-end  | Pengguna yang prioritaskan estetika|
| Script           | `crd-xfce.py`           | `crd-kde-plasma.py`                |

<div align="center">
  <img src="https://media.tenor.com/IjX29sgxJVAAAAAi/sleeping-cute.gif" alt="cute" height="90" />
</div>

---

## 🧰 Prasyarat
- Akun GitHub (dengan repo yang minimal punya 1 commit)
- Koneksi internet stabil
- Akun Google untuk Chrome Remote Desktop

---

## 📋 Tutorial Lengkap

### 1) Persiapan
1. Buat akun GitHub & repo baru (atau pakai repo yang sudah ada, asal ada minimal 1 commit).
2. Buka 👉 https://github.com/features/codespaces  
3. Klik **Get started for free**  
4. Klik **New codespace**  
5. Pilih repo kamu → tentukan **Region** terdekat (mis. South Asia untuk ping rendah ⚡)

---

### 2) Setup Codespace
6. Tunggu Codespace terbuka (tampilannya mirip VS Code).  
7. Buka Terminal dan jalankan:
```bash
git clone https://github.com/syaaikoo/rdp-codespace-ubuntu.git \
&& cd rdp-codespace-ubuntu && ls
```

Kamu akan melihat file:
- `crd-xfce.py`
- `crd-kde-plasma.py`
- `auto-active.py`
- `README.md`

---

### 3) Setup Chrome Remote Desktop
8. Buka https://remotedesktop.google.com (atau app di Play Store).  
9. Klik menu ☰ → pilih **Siapkan melalui SSH** → lanjut sampai halaman **Siapkan komputer lain**.  
10. Copy perintah paling bawah (untuk Debian Linux).

> ⚠️ Jangan tutup tab Chrome Remote Desktop saat proses! AuthKey bisa berubah.

---

### 4) Jalankan Script
11. Di terminal Codespace, pilih sesuai Desktop Environment:

Untuk XFCE4 (ringan & cepat):
```bash
sudo python crd-xfce.py
```

Untuk KDE Plasma (visual keren):
```bash
sudo python crd-kde-plasma.py
```

12. Paste perintah SSH yang tadi kamu copy dari Chrome Remote Desktop → Enter → tunggu proses otomatis sampai selesai.

13. Jalankan keep-alive agar Codespace tidak disconnect:
```bash
sudo python auto-active.py
```

---

### 5) Login RDP
14. Jangan reload/tab Codespace—biarkan tetap terbuka.  
15. Kembali ke Chrome Remote Desktop / aplikasi HP.  
16. Akan muncul komputer baru → klik dan login dengan password default:
```
123456
```

Selesai! Kamu sekarang punya **RDP gratis dengan RAM ±15GB** siap dipakai. 🎉

---

## 🖼️ Preview

> KDE Plasma (contoh):
>
> ![Preview KDE Plasma](https://kde.org/content/plasma-desktop/plasma-launcher.png)

> XFCE4 (contoh):
>
> ![Preview XFCE](https://docs.vultr.com/public/doc-assets/2091/9d5e1501-4ec5-4be6-95dd-6687764039c3.png)

---

## 🧭 Roadmap / Next Update
- [ ] Support DE tambahan (GNOME, MATE, Cinnamon)  
- [ ] Auto-reconnect lebih stabil  
- [ ] Deteksi error otomatis  
- [ ] UI setup via Python CLI  

---

## ❤️ Support
Kalau repo ini bermanfaat, jangan lupa kasih **⭐ Star** ya biar makin semangat update!  
Terima kasih sudah mampir! 🙌

<div align="center">
  <img src="https://c.tenor.com/Cjw0fXX7LwwAAAAC/tenor.gif" alt="thanks" height="120" />
  <p>
    <a href="https://github.com/syaaikoo">
      <img src="https://github-readme-stats.vercel.app/api/pin/?username=syaaikoo&repo=rdp-codespace-ubuntu&theme=tokyonight&hide_border=false" alt="Pinned Repo Card">
    </a>
  </p>
  <b>see youu, thanks for visiting my repo</b>
</div>
