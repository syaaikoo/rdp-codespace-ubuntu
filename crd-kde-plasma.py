#!/usr/bin/env python3
#stable_version_2.0-kde
#credit: @syaaikoo
#instagram: @syaaikoo
from __future__ import annotations
import os
import sys
import re
import platform
import shutil
import subprocess
import time
import logging
from pathlib import Path
from getpass import getpass

NAMA_APLIKASI = "rdp-kde-codespace"
DIREKTORI_VENV = Path(__file__).resolve().parent / "venv"
TANDA_REEXEC = "MC_BOOTSTRAPPED"
PAKET_PYTHON_WAJIB = ["rich", "alive-progress"]

def sedang_di_venv() -> bool:
    return (hasattr(sys, "real_prefix") or sys.prefix != sys.base_prefix)

def path_python_venv(venv_dir: Path) -> Path:
    if platform.system() == "Windows":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"

def buat_venv(venv_dir: Path) -> None:
    import venv
    builder = venv.EnvBuilder(with_pip=True, clear=False, upgrade=False)
    builder.create(venv_dir)
    py = path_python_venv(venv_dir)
    subprocess.run([str(py), "-m", "ensurepip", "--upgrade"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([str(py), "-m", "pip", "install", "--upgrade", "-q", "pip", "setuptools", "wheel"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

def pip_senyap(py: Path, packages: list[str]) -> None:
    cmd = [str(py), "-m", "pip", "install", "-q", "--disable-pip-version-check", "--no-input", *packages]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

def cek_perintah(cmds: list[str]) -> None:
    hilang = [cmd for cmd in cmds if shutil.which(cmd) is None]
    if hilang:
        console.print(Panel(
            f"[bold red]command ini tidak ditemukan di sistem: {', '.join(hilang)}[/bold red]\n"
            "wait cek semua dependensi sistem sudah terpasang apa belum.",
            title="Dependency Error"
        ))
        sys.exit(1)

def bootstrap() -> None:
    if os.environ.get(TANDA_REEXEC) == "1":
        return
    if not sedang_di_venv():
        DIREKTORI_VENV.mkdir(parents=True, exist_ok=True)
        buat_venv(DIREKTORI_VENV)
        pip_senyap(path_python_venv(DIREKTORI_VENV), PAKET_PYTHON_WAJIB)
        os.environ[TANDA_REEXEC] = "1"
        py = path_python_venv(DIREKTORI_VENV)
        os.execv(str(py), [str(py), __file__, *sys.argv[1:]])
    else:
        pip_senyap(Path(sys.executable), PAKET_PYTHON_WAJIB)

bootstrap()

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from alive_progress import alive_bar

console = Console()

def atur_logging() -> Path:
    utama = Path("/var/log") / NAMA_APLIKASI
    cadangan = Path.home() / f".{NAMA_APLIKASI}" / "logs"
    direktori_log = utama
    try:
        direktori_log.mkdir(parents=True, exist_ok=True)
        uji_file = direktori_log / ".w"
        uji_file.write_text("ok")
        uji_file.unlink(missing_ok=True)
    except Exception:
        direktori_log = cadangan
        direktori_log.mkdir(parents=True, exist_ok=True)
    file_log = direktori_log / "kde-crd.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(file_log, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    logging.info("File log: %s", str(file_log))
    return file_log

FILE_LOG = atur_logging()

def wajib_root() -> None:
    if os.geteuid() != 0:
        console.print(Panel("[bold red]woii!! nih skrip harus dijalanin pakai sudo lah atau root.[/bold red]", title="Hak Akses"))
        sys.exit(1)

def wajib_linux_apt() -> None:
    if platform.system().lower() != "linux":
        console.print(Panel("[bold red]maaf kak skrip ini cuma kompitable di vps linux.[/bold red]", title="OS"))
        sys.exit(1)
    if shutil.which("apt-get") is None:
        console.print(Panel("[bold red]perlu apt-get (Debian/Ubuntu).[/bold red]", title="Paket"))
        sys.exit(1)

def wajib_arch_amd64() -> None:
    arch = platform.machine().lower()
    if arch not in ("x86_64", "amd64"):
        console.print(Panel(f"[bold red]arsitektur kamu {arch} jadi maaf yaaa!! gak didukung. Butuh amd64/x86_64 hehehe.[/bold red]", title="Arsitektur"))
        sys.exit(1)

def jalankan_perintah(cmd: list[str], deskripsi: str = "", abaikan_error: bool = False, env_patch: dict | None = None) -> int:
    env_gabungan = os.environ.copy()
    if env_patch:
        env_gabungan.update(env_patch)
    judul = deskripsi or "running command…"
    with alive_bar(1, title=judul, spinner="dots_waves") as bar:
        try:
            proc = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=env_gabungan,
            )
            if proc.stdout:
                logging.info("CMD STDOUT (%s): %s", " ".join(cmd), proc.stdout.strip())
            if proc.stderr:
                logging.warning("CMD STDERR (%s): %s", " ".join(cmd), proc.stderr.strip())
            rc = proc.returncode
        except Exception as e:
            logging.exception("Gagal menjalankan perintah: %s", cmd)
            rc = 1
        time.sleep(0.25)
        bar()
    if rc != 0 and not abaikan_error:
        console.print(f"[bold red]Gagal:[/bold red] {deskripsi} (rc={rc}). Rinci lihat log: {FILE_LOG}")
    return rc

def apt(cmd_args: list[str], deskripsi: str) -> int:
    env = {"DEBIAN_FRONTEND": "noninteractive", "DEBIAN_PRIORITY": "critical", "APT_LISTCHANGES_FRONTEND": "none"}
    dasar = ["apt-get", "-y", "-o", "Dpkg::Use-Pty=0"]
    return jalankan_perintah(dasar + cmd_args, deskripsi=deskripsi, env_patch=env)

def validasi_username(username: str) -> bool:
    return re.fullmatch(r"[a-z_][a-z0-9_-]*", username) is not None

def pastikan_shell_bash(username: str) -> None:
    jalankan_perintah(["chsh", "-s", "/bin/bash", username], "atur shell bash", abaikan_error=True)

def tambah_sudoers(username: str) -> None:
    entri = f"{username}    ALL=(ALL:ALL) ALL\n"
    path = "/etc/sudoers"
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(entri)
        jalankan_perintah(["visudo", "-c"], "validasi /etc/sudoers", abaikan_error=False)
    except Exception:
        logging.exception("maaf gagal tambah entri ke /etc/sudoers")
        console.print(Panel(f"[bold red]maaf gagal tulis/validasi sudoers untuk {username} coba cek log yaaa!!.[/bold red]\nlihat log ini: {FILE_LOG}", title="sudoers"))
        sys.exit(1)

def buat_user(username: str, password: str) -> None:
    cek_perintah(["id", "useradd", "usermod", "chpasswd", "chsh", "visudo"])
    console.print(Panel("wait buat user sekaligus konfigurasi sudo/akses root", style="bold green", title="User"))
    jalankan_perintah(["id", "-u", username], "memeriksa user", abaikan_error=True)
    rc = jalankan_perintah(["id", "-u", username], deskripsi="cek user ada", abaikan_error=True)
    if rc != 0:
        jalankan_perintah(["useradd", "-m", username], "tambah user")
    jalankan_perintah(["usermod", "-aG", "sudo", username], "tambah ke grup sudo")
    jalankan_perintah(["bash", "-lc", f"echo '{username}:{password}' | chpasswd"], "atur password")
    pastikan_shell_bash(username)
    tambah_sudoers(username)

def pasang_dependensi() -> None:
    cek_perintah(["apt-get"])
    apt(["update"], "perbarui paket paket pendukung")
    apt(["install", "dbus-x11", "wget"], "pasang dependency dasar")

def pasang_crd() -> None:
    cek_perintah(["wget", "dpkg"])
    url = "https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb"
    deb = "chrome-remote-desktop_current_amd64.deb"
    rc_dl = jalankan_perintah(["wget", "-q", url, "-O", deb], "installing CRD")
    if rc_dl != 0 or not Path(deb).exists():
        console.print(Panel(
            "[bold red]sorry gagal unduh paket Chrome Remote Desktop.[/bold red]\n"
            "coba cek koneksi internet kamu aktif atau tidak serta url di skrip ini dapat diakses atau tidak, karna sewaktu waktu bisa berubah yaa urlnnya!!!.", title="Download Error"))
        logging.error("gagal unduh CRD dari %s", url)
        sys.exit(1)
    rc = jalankan_perintah(["dpkg", "-i", deb], "wait pasang CRD", abaikan_error=True)
    if rc != 0:
        apt(["-f", "install"], "fix dependency CRD")
    Path(deb).unlink(missing_ok=True)

def pasang_desktop() -> None:
    cek_perintah(["apt-get", "bash", "systemctl"])
    #pasang kde plamsa full
    rc_kde = apt(["install", "kde-plasma-desktop", "kde-full"], "Pasang DE KDE Plasma Full")
    if rc_kde != 0:
        console.print(Panel("[bold yellow]KDE Plasma tidak tersedia di repositori utama. Coba tambah repo universe dan update...[/bold yellow]"))
        #add repo universe
        jalankan_perintah(["add-apt-repository", "universe"], "Menambah repo universe", abaikan_error=True)
        apt(["update"], "Update repositori setelah tambah universe")
        #coba install lagi
        rc_kde2 = apt(["install", "kde-full"], "Pasang DE KDE Plasma Full (setelah tambah repo)")
        if rc_kde2 != 0:
            console.print(Panel(
                "[bold red]Gagal memasang KDE Plasma Full![/bold red]\n"
                "Paket tidak tersedia di semua repositori. Coba cek manual atau gunakan sistem yang kompatibel.",
                title="KDE Error"
            ))
            sys.exit(1)
    cmd = 'echo "exec /etc/X11/Xsession /usr/bin/startplasma-x11" > /etc/chrome-remote-desktop-session'
    jalankan_perintah(["bash", "-lc", cmd], "Mengatur sesi CRD (KDE)")
    apt(["remove", "gnome-terminal"], "hapus gnome-terminal (opsional)")
    apt(["install", "xscreensaver"], "pasang xscreensaver")
    jalankan_perintah(["systemctl", "disable", "lightdm.service"], "Menonaktifkan lightdm", abaikan_error=True)

def pasang_chrome() -> None:
    cek_perintah(["wget", "dpkg"])
    url = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
    deb = "google-chrome-stable_current_amd64.deb"
    rc_dl = jalankan_perintah(["wget", "-q", url, "-O", deb], "Mengunduh Google Chrome")
    if rc_dl != 0 or not Path(deb).exists():
        console.print(Panel(
            "[bold red]Gagal mengunduh paket Google Chrome.[/bold red]\n"
            "Pastikan koneksi internet aktif sekaligus url dapat diakses.", title="Download Error"))
        logging.error("Gagal mengunduh Chrome dari %s", url)
        sys.exit(1)
    rc = jalankan_perintah(["dpkg", "-i", deb], "pasang Google Chrome", abaikan_error=True)
    if rc != 0:
        console.print("[bold yellow]Fix dependency Chrome…[/bold yellow]")
        apt(["-f", "install"], "Fix dependency Chrome")
    Path(deb).unlink(missing_ok=True)

def daftar_crd(user: str, crp_command: str, pin: str) -> None:
    cek_perintah(["usermod", "su", "service"])
    jalankan_perintah(["usermod", "-aG", "chrome-remote-desktop", user], "Menambah user ke grup CRD", abaikan_error=True)
    jalankan_perintah(["su", "-", user, "-c", f"{crp_command} --pin={pin}"], "Registrasi host CRD")
    jalankan_perintah(["service", "chrome-remote-desktop", "start"], "Menyalakan layanan CRD")

def pasang_vscode_interaktif() -> None:
    jawaban = Prompt.ask("[bold cyan]maw sekalian pssang vsvode gak, biar nsnti gak ribet ribet setup vscode?[/bold cyan]", choices=["y", "n"], default="n")
    if jawaban.lower() != "y":
        return
    cek_perintah(["wget", "dpkg"])
    url = "https://az764295.vo.msecnd.net/stable/695af097c7bd098fbf017ce3ac85e09bbc5dda06/code_1.79.2-1686734195_amd64.deb"
    deb = Path(url).name
    rc_dl = jalankan_perintah(["wget", "-q", url, "-O", deb], "waitt unduh vscode")
    if rc_dl != 0 or not Path(deb).exists():
        console.print(Panel(
            "[bold red]ehh kok gagal unduh paket vscode.[/bold red]\n"
            "coba cek koneksi internet kalian aktif atau tidakk, sertaa cek url dalam skrip ini dapat diakses atau tidak yaa!!.", title="Download Error"))
        logging.error("Gagal mengunduh vscode dari %s", url)
        return
    rc = jalankan_perintah(["dpkg", "-i", deb], "pasang vscode", abaikan_error=True)
    if rc != 0:
        console.print("[bold yellow]Fix dependency vscode…[/bold yellow]")
        apt(["-f", "install"], "Fix dependency vscode")
    Path(deb).unlink(missing_ok=True)

def banner() -> None:
    tabel = Table(title="Installing chrome-remote-desktop (KDE Plasma)", show_lines=False, header_style="bold")
    tabel.add_column("Item", style="cyan", no_wrap=True)
    tabel.add_column("Nilai", style="green")
    tabel.add_row("OS", platform.platform())
    tabel.add_row("Python", sys.version.split()[0])
    tabel.add_row("Venv", str(DIREKTORI_VENV))
    tabel.add_row("Log", str(FILE_LOG))
    console.print(tabel)

def fitur_keep_alive() -> None:
    file_path = Path(__file__).resolve().parent / "cpu-diagnosa.txt"
    console.print(Panel(
        "[bold green]Fitur keep alive aktif![/bold green]\n"
        "skrip ini bakal nulis detail CPU ke cpu-diagnosa.txt setiap 60 detik, agar apa? yap agar sistem tidak mendeteksi kita afk alhasil dimatikan secara otomatis. cmiww.\n"
        "btw teken [bold yellow]Ctrl+C[/bold yellow] buat berhenti yaa!!.",
        title="Keep Alive"
    ))
    try:
        while True:
            with open(file_path, "a", encoding="utf-8") as f:
                waktu = time.strftime("%Y-%m-%d %H:%M:%S")
                loadavg = ""
                cpuinfo = ""
                try:
                    with open("/proc/loadavg") as lf:
                        loadavg = lf.read().strip()
                    with open("/proc/cpuinfo") as cf:
                        cpuinfo = cf.read().strip()
                except Exception as e:
                    loadavg = "N/A"
                    cpuinfo = f"Error membaca cpuinfo: {e}"
                f.write(f"=== {waktu} ===\n")
                f.write(f"Load Average: {loadavg}\n")
                f.write(f"CPU Info:\n{cpuinfo}\n\n")
            time.sleep(60)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Keep alive dihentikan oleh pengguna.[/bold yellow]")

def main() -> None:
    try:
        banner()
        wajib_linux_apt()
        wajib_arch_amd64()
        wajib_root()
        cek_perintah([
            "id", "useradd", "usermod", "chpasswd", "chsh", "visudo",
            "apt-get", "dpkg", "wget", "bash", "systemctl", "su", "service", "add-apt-repository"
        ])
        console.print(Panel("Input user untuk akses RDP", title="Konfigurasi", style="bold blue"))
        username = Prompt.ask("[bold cyan]Masukkan username (huruf kecil/angka/_/-):[/bold cyan]").strip()
        if not validasi_username(username):
            console.print(Panel("[bold red]Username tidak valid.[/bold red] Contoh valid: user-01", title="Validasi"))
            sys.exit(1)
        password = getpass("Masukkan password (disembunyikan): ").strip()
        if len(password) < 6:
            console.print(Panel("[bold red]Password minimal 6 karakter.[/bold red]", title="Validasi"))
            sys.exit(1)
        buat_user(username, password)
        console.print(Panel("Tempel perintah pendaftaran dari Google Remote Desktop (crp). Contoh: /opt/google/chrome-remote-desktop/start-host --code=\"...\" --redirect-url=\"...\" --name=\"...\"", title="CRD"))
        crp = Prompt.ask("[bold cyan]Masukkan perintah CRD (tanpa --pin):[/bold cyan]").strip()
        pin = Prompt.ask("[bold cyan]Masukkan PIN (6-12 digit):[/bold cyan]").strip()
        if not crp:
            console.print("[bold red]Perintah CRD wajib diisi.[/bold red]")
            sys.exit(1)
        if not re.fullmatch(r"\d{6,12}", pin):
            console.print("[bold red]PIN harus 6-12 digit angka.[/bold red]")
            sys.exit(1)
        console.print(Panel("pasang paket sistem sekaligus CRD…", style="bold green"))
        pasang_dependensi()
        pasang_crd()
        pasang_desktop()
        pasang_chrome()
        daftar_crd(username, crp, pin)
        console.print(Panel("nicee!! rdp kamuu berhasil dibuat nihh!.\nSekarang buka: https://remotedesktop.google.com/access \nuntuk aksesnya", style="bold green", title="Sukses"))
        pasang_vscode_interaktif()
        jawaban_keep_alive = Prompt.ask(
            "[bold cyan]Mau aktifin fitur keep alive gakk?, fungsinya buatt hindari AFK cara kerjanya tuh skrip ini bakal nulis kecepatsn cpu cpu-diagnosa.txt setiap 60 detik, inituh berfungsi bngt tauu kalok semisal kamu jalaninnya di lingkungan codespace agar menghindari di shutdown secara paksa gara gara tidak ads perubahan. cmiw!![/bold cyan]",
            choices=["y", "n"], default="n"
        )
        if jawaban_keep_alive.lower() == "y":
            fitur_keep_alive()
    except KeyboardInterrupt:
        console.print("\n[bold yellow]yahh kenapa skripnya kamu batalin kak:<.[/bold yellow]")
    except Exception as e:
        logging.exception("maaf eror dari skrip yg tak terduga")
        console.print(Panel(f"[bold red]eh terjadi error entah itu apa coba cek log:[/bold red] {e}\nLihat log disini: {FILE_LOG}", title="Error"))
        sys.exit(1)

if __name__ == "__main__":
    main()
