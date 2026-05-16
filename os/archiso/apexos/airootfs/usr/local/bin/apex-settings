#!/usr/bin/env python3
"""Apex Postavke — Windows-slične postavke sustava."""

from __future__ import annotations

import os
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk


def run(cmd: list[str]) -> None:
    try:
        subprocess.Popen(cmd, start_new_session=True)
    except FileNotFoundError:
        messagebox.showerror("Apex Postavke", f"Nije pronađeno: {cmd[0]}")


class ApexSettings(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Apex Postavke")
        self.geometry("480x420")
        self.minsize(420, 380)
        self.configure(bg="#0a0e14")

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#121820")
        style.configure("TLabel", background="#121820", foreground="#e8eef7")
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#3b9eff")
        style.configure("TButton", padding=10)

        frame = ttk.Frame(self, padding=16)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Apex Postavke", style="Header.TLabel").pack(anchor="w")
        ttk.Label(
            frame,
            text="Upravljanje sustavom, zvukom i ažuriranjima.",
        ).pack(anchor="w", pady=(0, 12))

        buttons = [
            ("🖥 Sve postavke sustava", self.open_system_settings),
            ("📁 Explorer (datoteke)", self.open_explorer),
            ("🔊 Zvuk i pojačavanje", self.open_sound),
            ("⬆ Apex Update", self.open_update),
            ("🛒 Apex Store", self.open_store),
            ("🌐 Mreža (Wi‑Fi)", self.open_network),
        ]
        for text, cmd in buttons:
            ttk.Button(frame, text=text, command=cmd).pack(fill=tk.X, pady=4)

        ttk.Label(
            frame,
            text="Pojačavanje zvuka: u Zvuku povuci klizač iznad 100% ili uključi EasyEffects.",
            wraplength=400,
        ).pack(anchor="w", pady=(12, 0))

    def open_system_settings(self) -> None:
        for cmd in (["systemsettings"], ["systemsettings5"]):
            try:
                run([cmd[0]])
                return
            except Exception:
                pass
        messagebox.showinfo("Apex Postavke", "Otvori izbornik Start → System Settings.")

    def open_explorer(self) -> None:
        run(["dolphin"])

    def open_sound(self) -> None:
        run(["/usr/local/bin/apex-audio-boost"])

    def open_update(self) -> None:
        run(["/usr/local/bin/apex-update"])

    def open_store(self) -> None:
        run(["/usr/local/bin/apex-store"])

    def open_network(self) -> None:
        run(["nm-connection-editor"])


def main() -> None:
    ApexSettings().mainloop()


if __name__ == "__main__":
    main()
