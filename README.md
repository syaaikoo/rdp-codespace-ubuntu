# rdp-codespace-ubuntu

Free RDP via GitHub Codespaces (Ubuntu + XFCE4 / KDE Plasma) — tanpa ribet, langsung jalan.

<div align="center">

[![Stars](https://img.shields.io/github/stars/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/stargazers)
[![Issues](https://img.shields.io/github/issues/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/issues)
[![Forks](https://img.shields.io/github/forks/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/forks)
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-24292e?style=for-the-badge\&logo=github)](https://codespaces.new/syaaikoo/rdp-codespace-ubuntu) <a href="https://instagram.com/syaaikoo"> <img alt="Instagram syaaikoo" src="https://img.shields.io/badge/Instagram-syaaikoo-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /> </a>

<br><br> <img src="https://media.tenor.com/N5fU8iyU9F4AAAAi/shigure-ui-dance.gif" alt="fun animation" height="140">

</div>

> [!WARNING]
> Ikuti panduan dengan teliti agar tidak gagal. Jangan menutup atau me-reload tab Codespace saat proses berjalan.

---

## Daftar Isi

* [Fitur](#fitur)
* [Pilihan Desktop Environment](#pilihan-desktop-environment)
* [Perbandingan XFCE4 vs KDE Plasma](#perbandingan-xfce4-vs-kde-plasma)
* [Quick Start](#quick-start)
* [Prasyarat](#prasyarat)
* [Tutorial Lengkap](#tutorial-lengkap)

  * [1) Persiapan](#1-persiapan)
  * [2) Setup Codespace](#2-setup-codespace)
  * [3) Setup Chrome Remote Desktop](#3-setup-chrome-remote-desktop)
  * [4) Jalankan Script](#4-jalankan-script)
  * [5) Login RDP](#5-login-rdp)
* [Troubleshooting](#troubleshooting)
* [Keamanan & Privasi](#keamanan--privasi)
* [FAQ](#faq)
* [Preview](#preview)
* [Roadmap / Next Update](#roadmap--next-update)
* [Kontribusi](#kontribusi)
* [Lisensi](#lisensi)
* [Dukungan](#dukungan)

---

## Fitur

* Gratis 100% via GitHub Codespaces
* RAM sekitar 15 GB, CPU memadai untuk tugas berat
* Setup otomatis, minim langkah manual
* Pilihan Desktop Environment: XFCE4 atau KDE Plasma
* Akses melalui Chrome Remote Desktop (web atau aplikasi Android)

---

## Pilihan Desktop Environment

* **XFCE4:** ringan, cepat, hemat resource
* **KDE Plasma:** modern, kaya fitur dan visual

Script terkait:

* `crd-xfce.py` (XFCE4)
* `crd-kde-plasma.py` (KDE Plasma)

---

## Perbandingan XFCE4 vs KDE Plasma

| Aspek          | XFCE4                  | KDE Plasma                           |
| -------------- | ---------------------- | ------------------------------------ |
| Performa       | Sangat ringan          | Sedikit lebih berat                  |
| Tampilan       | Minimalis & cepat      | Modern & kaya efek                   |
| Resource       | Rendah (hemat CPU/RAM) | Lebih tinggi                         |
| Kompatibilitas | Sangat stabil          | Kadang butuh penyesuaian tambahan    |
| Cocok untuk    | Server ringan, low-end | Pengguna yang memprioritaskan visual |
| Script         | `crd-xfce.py`          | `crd-kde-plasma.py`                  |

<div align="center">
  <img src="https://media.tenor.com/IjX29sgxJVAAAAAi/sleeping-cute.gif" alt="lightweight hint" height="90">
</div>

---

## Quick Start

1. Buka [GitHub Codespaces](https://github.com/features/codespaces) dan pilih **New codespace** untuk repo Anda.
2. Di Terminal Codespace:

```bash
git clone https://github.com/syaaikoo/rdp-codespace-ubuntu.git && cd rdp-codespace-ubuntu && ls
```

3. Pilih DE: jalankan salah satu `crd-xfce.py` atau `crd-kde-plasma.py`, lalu ikuti langkah Chrome Remote Desktop.

> [!TIP]
> Pilih region Codespace terdekat untuk latensi rendah.

---

## Prasyarat

* Akun GitHub (repo dengan minimal 1 commit)
* Koneksi internet stabil
* Akun Google untuk Chrome Remote Desktop

---

## Tutorial Lengkap

### 1) Persiapan

1. Buat akun GitHub & repo baru (atau gunakan repo yang sudah ada, minimal 1 commit).
2. Buka [GitHub Codespaces](https://github.com/features/codespaces)
3. Klik **Get started for free**
4. Klik **New codespace**
5. Pilih repo Anda → set **Region** terdekat (mis. *South Asia* untuk latensi rendah)

### 2) Setup Codespace

6. Tunggu Codespace terbuka (antarmuka mirip VS Code).
7. Buka Terminal dan jalankan:

```bash
git clone https://github.com/syaaikoo/rdp-codespace-ubuntu.git \
&& cd rdp-codespace-ubuntu && ls
```

Anda akan melihat:

* `crd-xfce.py`
* `crd-kde-plasma.py`
* `auto-active.py`
* `README.md`

### 3) Setup Chrome Remote Desktop

8. Kunjungi [Chrome Remote Desktop](https://remotedesktop.google.com) (atau aplikasi di Play Store).
9. Klik menu ☰ → **Siapkan melalui SSH** → lanjutkan sampai halaman **Siapkan komputer lain**.
10. Salin perintah paling bawah (untuk Debian Linux).

> [!IMPORTANT]
> Jangan tutup tab Chrome Remote Desktop saat proses berlangsung. AuthKey dapat berubah.

### 4) Jalankan Script

11. Di Terminal Codespace, pilih Desktop Environment:

XFCE4 (ringan & cepat):

```bash
sudo python3 crd-xfce.py
```

KDE Plasma (lebih kaya visual):

```bash
sudo python3 crd-kde-plasma.py
```

12. Tempel perintah SSH dari Chrome Remote Desktop → tekan Enter → tunggu proses otomatis selesai.

13. Jalankan keep-alive agar Codespace tetap aktif:

```bash
sudo python3 auto-active.py
```

### 5) Login RDP

14. Jangan reload atau menutup tab Codespace. Biarkan tetap terbuka.
15. Kembali ke Chrome Remote Desktop / aplikasi seluler.
16. Komputer baru akan muncul → klik dan masuk dengan password default:

```
123456
```

Selesai. Anda kini memiliki akses RDP berbasis GitHub Codespaces.

---

## Troubleshooting

* **Tidak muncul perangkat di Chrome Remote Desktop**

  * Pastikan proses instalasi selesai tanpa error dan tab CRD tidak ditutup.
  * Ulangi langkah 10–13 jika AuthKey berubah.
* **Error apt atau lock**

  * Tunggu proses sebelumnya selesai, lalu jalankan ulang script.
* **`python: command not found`**

  * Gunakan `python3` dan sesuaikan script jika diperlukan: `sudo python3 crd-xfce.py`.
* **Koneksi putus setelah idle**

  * Pastikan `auto-active.py` berjalan.
* **Latensi tinggi**

  * Gunakan region Codespace terdekat; tutup aplikasi lain yang membebani jaringan.

> [!NOTE]
> Kapasitas dan kebijakan Codespaces dapat berubah sewaktu-waktu sesuai ketentuan GitHub.

---

## Keamanan & Privasi

* Ganti password default setelah berhasil login.
* Jangan menyimpan kredensial sensitif di Codespace.
* Berhati-hati saat membagikan akses CRD; gunakan akun tepercaya.
* Hapus resource yang tidak digunakan dan revoke akses bila perlu.

---

## FAQ

* **Apakah resource permanen?**

  * Codespaces bersifat sementara. Jangan mengandalkannya untuk workload produksi jangka panjang.
* **Bisa pakai DE lain?**

  * Lihat roadmap; dukungan tambahan sedang direncanakan.
* **Perlu biaya?**

  * Mengacu pada kuota free GitHub Codespaces dan kebijakan terkini GitHub.

---

## Preview

**KDE Plasma (contoh):**
![Preview KDE Plasma](https://kde.org/content/plasma-desktop/plasma-launcher.png)

**XFCE4 (contoh):**
![Preview XFCE](https://docs.vultr.com/public/doc-assets/2091/9d5e1501-4ec5-4be6-95dd-6687764039c3.png)

---

## Roadmap / Next Update

* [ ] Dukungan DE tambahan (GNOME, MATE, Cinnamon)
* [ ] Auto-reconnect lebih stabil
* [ ] Deteksi error otomatis
* [ ] UI setup via Python CLI

---

## Kontribusi

Kontribusi sangat dihargai. Ajukan issue untuk diskusi terlebih dulu, lalu buat pull request yang terfokus pada perubahan spesifik disertai deskripsi yang jelas.

---

## Lisensi

Tentukan lisensi proyek Anda di sini. Jika menggunakan MIT, tambahkan file `LICENSE` dengan teks MIT License.

---

## Dukungan

Jika repo ini bermanfaat, mohon berikan Star pada repositori ini. Terima kasih telah berkunjung.

<div align="center">
  <img src="https://c.tenor.com/Cjw0fXX7LwwAAAAC/tenor.gif" alt="thanks" height="120">
  <p>
    <a href="https://github.com/syaaikoo">
      <img alt="Pinned Repo Card" src="https://github-readme-stats.vercel.app/api/pin/?username=syaaikoo&repo=rdp-codespace-ubuntu&theme=tokyonight&hide_border=false">
    </a>
  </p>
  <b>See you, thanks for visiting this repo</b>
</div>
