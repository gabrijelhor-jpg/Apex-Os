#!/usr/bin/env python3
"""Apex Update — ažuriranje sustava (paketi + provjera nove verzije Apex OS)."""

from __future__ import annotations

import json
import os
import subprocess
import threading
import tkinter as tk
import urllib.error
import urllib.request
from tkinter import messagebox, scrolledtext, ttk

APEX_RELEASE = "/etc/apex-release"
DEFAULT_VERSION_URL = "https://raw.githubusercontent.com/apex-os/apex-os/main/os/apex-version.json"


def read_apex_version() -> str:
    if os.path.isfile(APEX_RELEASE):
        with open(APEX_RELEASE, encoding="utf-8") as f:
            for line in f:
                if line.startswith("APEX_VERSION="):
                    return line.split("=", 1)[1].strip().strip('"')
    return "1.0"


def read_update_url() -> str:
    if os.path.isfile(APEX_RELEASE):
        with open(APEX_RELEASE, encoding="utf-8") as f:
            for line in f:
                if line.startswith("APEX_UPDATE_URL="):
                    return line.split("=", 1)[1].strip().strip('"')
    return DEFAULT_VERSION_URL


def fetch_remote_version() -> dict | None:
    url = read_update_url()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Apex-Update/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
        return None


def run_as_root(args: list[str]) -> subprocess.CompletedProcess[str]:
    if os.path.isfile("/usr/bin/pkexec"):
        return subprocess.run(["pkexec"] + args, capture_output=True, text=True)
    return subprocess.run(["sudo"] + args, capture_output=True, text=True)


class ApexUpdateApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Apex Update")
        self.geometry("560x440")
        self.minsize(480, 360)
        self.configure(bg="#0a0e14")

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#121820")
        style.configure("TLabel", background="#121820", foreground="#e8eef7")
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#3b9eff")

        frame = ttk.Frame(self, padding=12)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Apex Update", style="Header.TLabel").pack(anchor="w")
        local = read_apex_version()
        self.status = ttk.Label(frame, text=f"Tvoja verzija Apex OS: {local}")
        self.status.pack(anchor="w", pady=4)
        self.remote_label = ttk.Label(frame, text="Provjera novih verzija…")
        self.remote_label.pack(anchor="w", pady=(0, 8))

        btn_row = ttk.Frame(frame)
        btn_row.pack(fill=tk.X, pady=4)
        self.check_btn = ttk.Button(btn_row, text="Provjeri ažuriranja", command=self.check_updates_thread)
        self.check_btn.pack(side=tk.LEFT, padx=(0, 8))
        self.upgrade_btn = ttk.Button(btn_row, text="Instaliraj ažuriranja", command=self.install_updates_thread)
        self.upgrade_btn.pack(side=tk.LEFT)
        self.upgrade_btn.state(["disabled"])

        ttk.Label(
            frame,
            text="Za ažuriranje treba internet. Ažurira programe i sustav (pacman).",
        ).pack(anchor="w")

        self.log = scrolledtext.ScrolledText(
            frame, height=14, bg="#0a0e14", fg="#e8eef7", insertbackground="#e8eef7"
        )
        self.log.pack(fill=tk.BOTH, expand=True, pady=8)

        threading.Thread(target=self._check_remote_version, daemon=True).start()

    def log_line(self, text: str) -> None:
        self.log.insert(tk.END, text + "\n")
        self.log.see(tk.END)

    def _check_remote_version(self) -> None:
        data = fetch_remote_version()
        local = read_apex_version()

        def ui() -> None:
            if not data:
                self.remote_label.configure(
                    text="Nije moguće provjeriti novu verziju online (nema mreže ili URL nije postavljen)."
                )
                return
            remote = str(data.get("version", ""))
            notes = data.get("notes", "")
            if remote and _version_gt(remote, local):
                self.remote_label.configure(
                    text=f"Dostupna novija verzija Apex OS: {remote}. {notes}"
                )
            else:
                self.remote_label.configure(text=f"Apex OS je ažuran ({local}). Paketi se provjeravaju zasebno.")

        self.after(0, ui)

    def check_updates_thread(self) -> None:
        self.check_btn.state(["disabled"])
        threading.Thread(target=self._check_updates, daemon=True).start()

    def _check_updates(self) -> None:
        self.after(0, lambda: self.log_line("Sinkroniziram repozitorije…"))
        sync = run_as_root(["pacman", "-Sy"])
        if sync.returncode != 0:
            self.after(0, lambda: self.log_line(sync.stderr or "Greška pri pacman -Sy"))
            self.after(0, lambda: self.check_btn.state(["!disabled"]))
            return

        result = subprocess.run(["pacman", "-Qu"], capture_output=True, text=True)
        out = result.stdout.strip()

        def done() -> None:
            if out:
                self.log_line("Dostupna ažuriranja paketa:\n" + out)
                self.upgrade_btn.state(["!disabled"])
            else:
                self.log_line("Nema novih ažuriranja paketa.")
                self.upgrade_btn.state(["disabled"])
            self.check_btn.state(["!disabled"])

        self.after(0, done)

    def install_updates_thread(self) -> None:
        if not messagebox.askyesno(
            "Apex Update",
            "Instalirati sva dostupna ažuriranja?\n\nLozinka administratora može biti potrebna.",
        ):
            return
        self.upgrade_btn.state(["disabled"])
        threading.Thread(target=self._install_updates, daemon=True).start()

    def _install_updates(self) -> None:
        self.after(0, lambda: self.log_line("Instaliram ažuriranja (pacman -Syu)…"))
        proc = run_as_root(["pacman", "-Syu", "--noconfirm"])
        text = (proc.stdout or "") + (proc.stderr or "")

        def done() -> None:
            self.log_line(text or "Gotovo.")
            if proc.returncode == 0:
                messagebox.showinfo("Apex Update", "Ažuriranje završeno. Restart se preporučuje.")
            else:
                messagebox.showerror("Apex Update", "Ažuriranje nije u potpunosti uspjelo. Pogledaj log.")
            self.upgrade_btn.state(["!disabled"])

        self.after(0, done)


def _version_gt(a: str, b: str) -> bool:
    def parts(v: str) -> list[int]:
        return [int(x) for x in v.split(".") if x.isdigit()]

    pa, pb = parts(a), parts(b)
    return pa > pb


def main() -> None:
    ApexUpdateApp().mainloop()


if __name__ == "__main__":
    main()
