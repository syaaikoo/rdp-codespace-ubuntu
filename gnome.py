# script by airaacheisyaa
# instagram: @syaaikoo
# dilarang keras menyalahgunakan, segala resiko ditanggung sendiri ya kocak
#!/usr/bin/env python3
import os
import subprocess
import textwrap
import sys

def log(msg, status="INFO"):
    colors = {
        "INFO": "\033[94m[INFO]\033[0m",
        "OK": "\033[92m[OK]\033[0m",
        "WARN": "\033[93m[WARN]\033[0m",
        "ERROR": "\033[91m[ERROR]\033[0m"
    }
    print(f"{colors.get(status, '[?]')} {msg}")

def run_cmd(cmd, check=True, capture=False, as_user=None):
    if as_user and os.geteuid() == 0 and as_user != 'root':
        cmd = ['sudo', '-u', as_user] + cmd
    try:
        if capture:
            r = subprocess.run(cmd, check=check, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return r.stdout.strip(), r.stderr.strip()
        else:
            subprocess.run(cmd, check=check)
            return None, None
    except subprocess.CalledProcessError as e:
        if capture:
            return getattr(e, 'stdout', ''), getattr(e, 'stderr', str(e))
        log(f"Perintah gagal: {' '.join(cmd)} -> {e}", "ERROR")
        if check:
            sys.exit(1)
        return None, str(e)

# Input
CRD_SSH_Code = input("masukin google crd tadi yang kamu salin : ").strip()
Pin = input("masukin pin minimal 6 digit (default 123456): ").strip() or "123456"

if len(Pin) < 6:
    log("pin minimal 6 digit astagfirullah!", "ERROR")
    sys.exit(1)

if os.geteuid() != 0:
    log("si kocakk udah dibilangin jalanin nih script pakai sudo!", "ERROR")
    sys.exit(1)

os.environ["DEBIAN_FRONTEND"] = "noninteractive"

SUDO_USER = os.environ.get('SUDO_USER') or "nobody"

class CRDRootGNOME_NoSystemd:
    def __init__(self):
        self.install_requirements()
        self.install_crd()
        self.install_gnome()
        self.configure_crd_session()
        self.finish()

    @staticmethod
    def install_requirements():
        log("update repository & install dependency dasar...")
        run_cmd(["apt-get", "update", "-y"])
        run_cmd(["apt-get", "install", "-y", "wget", "curl", "sudo", "lsb-release", "pulseaudio", "dbus-x11"], check=False)
        log("dependency dasar terpasang", "OK")

    @staticmethod
    def install_crd():
        log("install chrome remote desktop...")
        run_cmd(["wget", "-q", "https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "chrome-remote-desktop_current_amd64.deb"], check=False)
        run_cmd(["apt-get", "install", "-y", "--fix-broken"]) 
        log("chrome remote desktop udah terpasang", "OK")

    @staticmethod
    def install_gnome():
        log("install GNOME minimal (desktop & dependencies)...")
        run_cmd(["apt-get", "install", "-y", "ubuntu-desktop-minimal", "dbus-user-session"], check=False)
        log("GNOME desktop sudah terpasang", "OK")

    @staticmethod
    def configure_crd_session():
        log("menulis /etc/chrome-remote-desktop-session (gnome user session)...")
        session_script = textwrap.dedent("""\
        #!/bin/bash
        export XDG_RUNTIME_DIR=/run/user/0
        if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
          eval $(dbus-launch --sh-syntax --exit-with-session)
        fi
        exec /usr/bin/gnome-session --session=ubuntu
        """)
        with open('/etc/chrome-remote-desktop-session', 'w') as f:
            f.write(session_script)
        os.chmod('/etc/chrome-remote-desktop-session', 0o755)
        log("session GNOME user ditulis", "OK")

    @staticmethod
    def finish():
        log("restart service dbus & chrome-remote-desktop (tanpa systemd)...")

        # restart service dengan cara lama (SysVinit style)
        os.system("service dbus restart || /etc/init.d/dbus restart || true")
        os.system("service chrome-remote-desktop restart || /etc/init.d/chrome-remote-desktop restart || true")

        if CRD_SSH_Code:
            log("jalankan host-setup chrome remote desktop...")
            if SUDO_USER and SUDO_USER != 'nobody':
                os.system(f"sudo -u {SUDO_USER} {CRD_SSH_Code} --pin={Pin}")
            else:
                os.system(f"{CRD_SSH_Code} --pin={Pin}")
        else:
            log("auth code CRD gak ada, dilewati", "WARN")

        print("\n\033[92m✅ RDP GNOME siap diakses via Chrome Remote Desktop!\033[0m")
        print("CATATAN: kalau CRD gk muncul, tunggu 1-5 menit karna lagi booting.")
        print("kalo tetap gak muncul, ketikin: service chrome-remote-desktop restart")

if __name__ == "__main__":
    CRDRootGNOME_NoSystemd()
