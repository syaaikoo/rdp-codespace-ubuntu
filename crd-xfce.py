# script by airaacheisyaa
#instagram: @syaaikoo
# dilarang keras menyalahgunakan, segala resiko ditanggung sendiri ya kocak
#!/usr/bin/env python3
import os
import subprocess
import textwrap
import sys
#utility
def log(msg, status="INFO"):
    colors = {
        "INFO": "\033[94m[INFO]\033[0m",
        "OK": "\033[92m[OK]\033[0m",
        "WARN": "\033[93m[WARN]\033[0m",
        "ERROR": "\033[91m[ERROR]\033[0m"
    }
    print(f"{colors.get(status, '[?]')} {msg}")

def run_cmd(cmd, check=True):
    try:
        subprocess.run(cmd, check=check)
    except subprocess.CalledProcessError as e:
        log(f"Perintah gagal: {' '.join(cmd)}", "ERROR")
        sys.exit(1)

#input
CRD_SSH_Code = input("masukin google crd tadi yang kamu salin : ").strip()
Pin = input("masukin pin minimal 6 digit (default 123456): ").strip() or "123456"
if os.geteuid() != 0:
    log("si kocakk udah dibilangin jalanin nih script pakai sudo!", "ERROR")
    sys.exit(1)

if CRD_SSH_Code == "":
    log("woii auth code dari google crd wajib diisi!", "ERROR")
    sys.exit(1)

if len(Pin) < 6:
    log("pin minimal 6 digit astagfirullah!", "ERROR")
    sys.exit(1)

os.environ["DEBIAN_FRONTEND"] = "noninteractive"

#mainclas
class CRDRootXFCE:
    def __init__(self):
        self.install_requirements()
        self.install_crd()
        self.install_xfce()
        self.ensure_run_user_for_root()
        self.configure_crd_session()
        self.finish()

    @staticmethod
    def install_requirements():
        log("sabar update repository & menginstall dependency dasar dasar dulu...")
        run_cmd(["apt", "update", "-y"])
        run_cmd(["apt", "install", "-y", "wget", "curl", "sudo", "lsb-release"])
        log("Dependency dasar terpasang", "OK")

    @staticmethod
    def install_crd():
        log("waitt install chrome remote desktop...")
        run_cmd(["wget", "-q", "https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "chrome-remote-desktop_current_amd64.deb"], check=False)
        run_cmd(["apt", "install", "-y", "--fix-broken"])
        log("nice chrome remote desktop udah terpasang", "OK")

    @staticmethod
    def install_xfce():
        log("tunggu sebentar sedang menginstall xfce4 full...")
        run_cmd(["apt", "install", "-y", "xfce4", "xfce4-goodies", "dbus-x11", "dbus-user-session", "pulseaudio"])
        log("xfce4 full sudah terpasang", "OK")

    @staticmethod
    def ensure_run_user_for_root():
        run_user_dir = "/run/user/0"
        if not os.path.exists(run_user_dir):
            os.makedirs(run_user_dir, exist_ok=True)
            os.chown(run_user_dir, 0, 0)
            os.chmod(run_user_dir, 0o700)
            log("Folder /run/user/0 dibuat untuk session user", "OK")
        else:
            log("/run/user/0 udah ada", "INFO")

    @staticmethod
    def configure_crd_session():
        log("membuat /etc/chrome-remote-desktop-session (xfce user session)...")
        session_script = textwrap.dedent("""\
        #!/bin/bash
        export XDG_RUNTIME_DIR=/run/user/0
        if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
          eval $(dbus-launch --sh-syntax --exit-with-session)
        fi
        exec /usr/bin/startxfce4
        """)
        with open('/etc/chrome-remote-desktop-session', 'w') as f:
            f.write(session_script)
        os.chmod('/etc/chrome-remote-desktop-session', 0o755)
        log("session xfce user ditulis", "OK")

    @staticmethod
    def finish():
        log("restart service dbus & chrome-remote-desktop...")
        os.system("systemctl daemon-reload || true")
        os.system("service dbus restart || true")
        os.system("service chrome-remote-desktop restart || true")

        if CRD_SSH_Code:
            log("jalankan host-setup chrome remote desktop...")
            os.system(f"{CRD_SSH_Code} --pin={Pin}")
        else:
            log("auth code CRD gak ada, dilewati", "WARN")

        print("\n\033[92m✅ RDP XFCE4 siap diakses via Chrome Remote Desktop!\033[0m")
        print("CATATAN: kalok CRD gk muncul, tunggu 1-5 menit karna lagi booting.")
        print("kalo tetap gak muncul, ketikin: sudo service chrome-remote-desktop restart")
      
#eksekusi
if __name__ == "__main__":
    CRDRootXFCE()
