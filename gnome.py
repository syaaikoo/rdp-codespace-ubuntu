#!/usr/bin/env python3
import os
import subprocess
import textwrap
import sys
import pwd

def log(msg, status="INFO"):
    colors = {
        "INFO": "\033[94m[INFO]\033[0m",
        "OK": "\033[92m[OK]\033[0m",
        "WARN": "\033[93m[WARN]\033[0m",
        "ERROR": "\033[91m[ERROR]\033[0m"
    }
    print("{} {}".format(colors.get(status, "[?]"), msg))

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
        log("Perintah gagal: {} -> {}".format(' '.join(cmd), e), "ERROR")
        if check:
            sys.exit(1)
        return None, str(e)

CRD_SSH_Code = input("masukin google crd tadi yang kamu salin : ").strip()
Pin = input("masukin pin minimal 6 digit (default 123456): ").strip() or "123456"

if len(Pin) < 6:
    log("pin minimal 6 digit astagfirullah!", "ERROR")
    sys.exit(1)

if os.geteuid() != 0:
    log("jalanin script ini pakai sudo!", "ERROR")
    sys.exit(1)

os.environ["DEBIAN_FRONTEND"] = "noninteractive"

SUDO_USER = os.environ.get('SUDO_USER') or None
if not SUDO_USER:
    for uname in os.listdir('/home'):
        if uname not in ('root',):
            SUDO_USER = uname
            break
if not SUDO_USER:
    SUDO_USER = 'nobody'

def uid_gid_of(user):
    try:
        pw = pwd.getpwnam(user)
        return pw.pw_uid, pw.pw_gid
    except KeyError:
        return None, None

def ensure_pulse_pipe_sink(user=SUDO_USER):
    uid, gid = uid_gid_of(user)
    pulse_dir = f"/tmp/chrome_remote_desktop_audio_{user}"
    fifo_path = os.path.join(pulse_dir, 'fifo_output')
    try:
        os.makedirs(pulse_dir, exist_ok=True)
        if uid is not None:
            os.chown(pulse_dir, uid, gid)
        os.chmod(pulse_dir, 0o770)
        log(f"pulse dir ready: {pulse_dir}", "OK")
    except Exception as e:
        log(f"gagal bikin pulse dir {pulse_dir}: {e}", "WARN")
    if not os.path.exists(fifo_path):
        try:
            os.mkfifo(fifo_path)
            if uid is not None:
                os.chown(fifo_path, uid, gid)
            os.chmod(fifo_path, 0o660)
            log(f"fifo dibuat: {fifo_path}", "OK")
        except Exception as e:
            log(f"gagal buat fifo {fifo_path}: {e}", "ERROR")
            return False
    else:
        log(f"fifo sudah ada: {fifo_path}", "INFO")
    try:
        os.makedirs('/etc/pulse/default.pa.d', exist_ok=True)
        conf_path = '/etc/pulse/default.pa.d/chrome-remote-desktop.conf'
        conf_content = f"load-module module-pipe-sink sink_name=chrome_remote_desktop_session file={fifo_path} rate=48000 channels=2 format=s16le\n"
        with open(conf_path, 'w') as f:
            f.write(conf_content)
        log(f"wrote {conf_path}", "OK")
    except Exception as e:
        log(f"gagal tulis conf default.pa.d: {e}", "WARN")
    pactl_bin = subprocess.run(['which', 'pactl'], stdout=subprocess.PIPE, text=True).stdout.strip()
    if pactl_bin:
        load_cmd = ['pactl', 'load-module', 'module-pipe-sink', f'sink_name=chrome_remote_desktop_session', f'file={fifo_path}', 'rate=48000', 'channels=2', 'format=s16le']
        out, err = run_cmd(load_cmd, check=False, capture=True, as_user=user)
        if out:
            log(f"module-pipe-sink dimuat (mod id): {out}", "OK")
        else:
            log(f"gagal load module via pactl: {err}", "WARN")
    else:
        log("pactl tidak ditemukan, dilewati", "INFO")
    return True

class CRDRootGNOME:
    def __init__(self):
        self.install_requirements()
        self.install_crd()
        self.install_gnome()
        self.ensure_run_user_for_root()
        self.configure_crd_session()
        ensure_pulse_pipe_sink()
        self.finish()

    @staticmethod
    def install_requirements():
        log("update repository & install dependency dasar...")
        run_cmd(["apt", "update", "-y"])
        run_cmd(["apt", "install", "-y", "wget", "curl", "sudo", "lsb-release", "pulseaudio", "pactl", "dbus-x11"], check=False)
        log("dependency dasar terpasang", "OK")

    @staticmethod
    def install_crd():
        log("install chrome remote desktop...")
        run_cmd(["wget", "-q", "https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "chrome-remote-desktop_current_amd64.deb"], check=False)
        run_cmd(["apt", "install", "-y", "--fix-broken"]) 
        log("chrome remote desktop udah terpasang", "OK")

    @staticmethod
    def install_gnome():
        log("install gnome full...")
        run_cmd(["apt", "install", "-y", "gnome-session", "gnome-shell", "gnome-terminal", "gdm3"], check=False)
        log("gnome desktop sudah terpasang", "OK")

    @staticmethod
    def ensure_run_user_for_root():
        run_user_dir = "/run/user/0"
        if not os.path.exists(run_user_dir):
            os.makedirs(run_user_dir, exist_ok=True)
            os.chown(run_user_dir, 0, 0)
            os.chmod(run_user_dir, 0o700)
            log("folder /run/user/0 dibuat", "OK")
        else:
            log("/run/user/0 udah ada", "INFO")

    @staticmethod
    def configure_crd_session():
        log("menulis /etc/chrome-remote-desktop-session (gnome)...")
        session_script = textwrap.dedent("""\
        #!/bin/bash
        export XDG_RUNTIME_DIR=/run/user/0
        if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
          eval $(dbus-launch --sh-syntax --exit-with-session)
        fi
        export CHROME_RDP_FIFO_DIR=/tmp/chrome_remote_desktop_audio_$SUDO_USER
        export PULSE_RUNTIME_PATH=$CHROME_RDP_FIFO_DIR
        exec gnome-session
        """)
        with open('/etc/chrome-remote-desktop-session', 'w') as f:
            f.write(session_script)
        os.chmod('/etc/chrome-remote-desktop-session', 0o755)
        log("session gnome ditulis", "OK")

    @staticmethod
    def finish():
        log("restart dbus & chrome-remote-desktop...")
        os.system("service dbus restart || true")
        os.system("service chrome-remote-desktop restart || true")
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
    CRDRootGNOME()
