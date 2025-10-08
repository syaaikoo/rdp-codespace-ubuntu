# rdp-codespace-ubuntu

Free RDP via GitHub Codespaces (Ubuntu + XFCE4 / KDE Plasma) — tanpa ribet, langsung jalan.

<div align="center">

[![Stars](https://img.shields.io/github/stars/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/stargazers)
[![Issues](https://img.shields.io/github/issues/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/issues)
[![Forks](https://img.shields.io/github/forks/syaaikoo/rdp-codespace-ubuntu?style=for-the-badge)](https://github.com/syaaikoo/rdp-codespace-ubuntu/forks)
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-24292e?style=for-the-badge&logo=github)](https://codespaces.new/syaaikoo/rdp-codespace-ubuntu)
<a href="https://instagram.com/syaaikoo">
  <img alt="Instagram syaaikoo" src="https://img.shields.io/badge/Instagram-syaaikoo-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
</a>

<br /><br />
<img src="https://media.tenor.com/N5fU8iyU9F4AAAAi/shigure-ui-dance.gif" alt="fun animation" height="140" />
</div>

> [!WARNING]
> Ikuti panduan dengan teliti agar tidak gagal. Jangan menutup atau me-reload tab Codespace saat proses berjalan.

---

## Daftar Isi
- [Fitur](#fitur)
- [Pilihan Desktop Environment](#pilihan-desktop-environment)
- [Perbandingan XFCE4 vs KDE Plasma](#perbandingan-xfce4-vs-kde-plasma)
- [Quick Start](#quick-start)
- [Prasyarat](#prasyarat)
- [Tutorial Lengkap](#tutorial-lengkap)
  - [1) Persiapan](#1-persiapan)
  - [2) Setup Codespace](#2-setup-codespace)
  - [3) Setup Chrome Remote Desktop](#3-setup-chrome-remote-desktop)
  - [4) Jalankan Script](#4-jalankan-script)
  - [5) Login RDP](#5-login-rdp)
- [Troubleshooting](#troubleshooting)
- [Keamanan & Privasi](#keamanan--privasi)
- [FAQ](#faq)
- [Preview](#preview)
- [Roadmap / Next Update](#roadmap--next-update)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)
- [Dukungan](#dukungan)

---

## Fitur
- Gratis 100% via GitHub Codespaces  
- RAM sekitar 15 GB, CPU memadai untuk tugas berat  
- Setup otomatis, minim langkah manual  
- Pilihan Desktop Environment: XFCE4 atau KDE Plasma  
- Akses melalui Chrome Remote Desktop (web atau aplikasi Android)

---

## Quick Start
1. Buka https://github.com/features/codespaces dan pilih **New codespace** untuk repo Anda.  
2. Di Terminal Codespace:
```bash
git clone https://github.com/syaaikoo/rdp-codespace-ubuntu.git && cd rdp-codespace-ubuntu && ls
```
3. Pilih DE: jalankan salah satu `crd-xfce.py` atau `crd-kde-plasma.py`, lalu ikuti langkah Chrome Remote Desktop.
