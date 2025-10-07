#!/usr/bin/env python3
import time
import psutil
import itertools
import os

log_file = "diagnosa.txt"
dummy_file = "keepalive.txt"

def log_to_file(msg: str):
    with open(log_file, "a") as f:
        f.write(msg + "\n")

def keepalive_file():
    with open(dummy_file, "w") as f:
        f.write(f"keepalive {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

def clear_terminal():
    os.system("clear" if os.name == "posix" else "cls")

def monitor_mode():
    spinner = itertools.cycle(["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"])
    clear_terminal()
    print("✮⋆˙ auto-active monitor mode... (ctrl+c buat berhenti)\n")
    while True:
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        freq = psutil.cpu_freq()
        if freq:
            log_line = f"{now} | cpu: {freq.current:.2f} mhz"
        else:
            log_line = f"{now} | cpu: tidak ditemukan"
        log_to_file(log_line)
        spin = next(spinner)
        print(f"\r{spin} {log_line}", end="", flush=True)
        time.sleep(60)

def keepalive_mode():
    clear_terminal()
    print("⋆.˚🦋༘⋆ auto-active keepalive mode... (ctrl+c buat berhenti)\n")
    while True:
        keepalive_file()
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"\r⏳ keepalive update {now}", end="", flush=True)
        time.sleep(60)

if __name__ == "__main__":
    mode = input("pilih mode dulu (1=monitor, 2=keepalive): ").strip()
    try:
        if mode == "2":
            keepalive_mode()
        else:
            monitor_mode()
    except KeyboardInterrupt:
        print("\n❌ auto-active dihentikan manual.")
