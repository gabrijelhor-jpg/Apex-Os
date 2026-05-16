#!/usr/bin/env python3
"""Apex Store — službena trgovina aplikacija za Apex OS."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, ttk

CATALOG_PATH = os.environ.get(
    "APEX_STORE_CATALOG",
    "/usr/share/apex-store/catalog.json",
)


def load_catalog() -> list[dict]:
    paths = [
        CATALOG_PATH,
        os.path.join(os.path.dirname(__file__), "catalog.json"),
    ]
    for path in paths:
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
                return data.get("apps", [])
    return []


def is_installed(packages: list[str]) -> bool:
    for pkg in packages:
        if subprocess.call(["pacman", "-Q", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
            return False
    return True


def run_pacman(install: bool, packages: list[str]) -> bool:
    if install:
        cmd = ["pacman", "-S", "--needed", "--noconfirm", *packages]
    else:
        cmd = ["pacman", "-Rns", "--noconfirm", *packages]

    if shutil.which("pkexec"):
        full = ["pkexec"] + cmd
    else:
        full = ["sudo"] + cmd

    try:
        proc = subprocess.run(full)
        return proc.returncode == 0
    except FileNotFoundError:
        messagebox.showerror("Apex Store", "pacman nije pronađen.")
        return False


class ApexStoreApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Apex Store")
        self.geometry("720x520")
        self.minsize(600, 420)
        self.configure(bg="#0a0e14")

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#121820")
        style.configure("TLabel", background="#121820", foreground="#e8eef7")
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#3b9eff")
        style.configure("TButton", padding=8)

        self.apps = load_catalog()
        self._build_ui()
        self.refresh_list()

    def _build_ui(self) -> None:
        top = ttk.Frame(self, padding=12)
        top.pack(fill=tk.BOTH, expand=True)

        ttk.Label(top, text="Apex Store", style="Header.TLabel").pack(anchor="w")
        ttk.Label(
            top,
            text="Instaliraj i ukloni aplikacije. Za nove pakete potreban je internet.",
        ).pack(anchor="w", pady=(0, 8))

        search_row = ttk.Frame(top)
        search_row.pack(fill=tk.X, pady=(0, 8))
        ttk.Label(search_row, text="Pretraži:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self.refresh_list())
        ttk.Entry(search_row, textvariable=self.search_var).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)

        list_frame = ttk.Frame(top)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            list_frame,
            columns=("name", "category", "status"),
            show="headings",
            height=14,
        )
        self.tree.heading("name", text="Aplikacija")
        self.tree.heading("category", text="Kategorija")
        self.tree.heading("status", text="Status")
        self.tree.column("name", width=220)
        self.tree.column("category", width=120)
        self.tree.column("status", width=100)
        scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        self.detail = ttk.Label(top, text="Odaberi aplikaciju.", wraplength=640)
        self.detail.pack(anchor="w", pady=8)

        btn_row = ttk.Frame(top)
        btn_row.pack(fill=tk.X)
        self.install_btn = ttk.Button(btn_row, text="Instaliraj", command=self.install_selected)
        self.install_btn.pack(side=tk.LEFT, padx=(0, 8))
        self.remove_btn = ttk.Button(btn_row, text="Ukloni", command=self.remove_selected)
        self.remove_btn.pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(btn_row, text="Osvježi", command=self.refresh_list).pack(side=tk.LEFT)

    def _filtered_apps(self) -> list[dict]:
        q = self.search_var.get().strip().lower()
        if not q:
            return self.apps
        return [
            a
            for a in self.apps
            if q in a.get("name", "").lower() or q in a.get("description", "").lower()
        ]

    def refresh_list(self) -> None:
        self.tree.delete(*self.tree.get_children())
        for app in self._filtered_apps():
            pkgs = app.get("packages", [])
            status = "Instalirano" if is_installed(pkgs) else "Nije instalirano"
            self.tree.insert("", tk.END, iid=app["id"], values=(app["name"], app.get("category", ""), status))

    def _on_select(self, _event=None) -> None:
        app = self._selected_app()
        if not app:
            return
        self.detail.configure(text=app.get("description", ""))

    def _selected_app(self) -> dict | None:
        sel = self.tree.selection()
        if not sel:
            return None
        app_id = sel[0]
        for app in self.apps:
            if app["id"] == app_id:
                return app
        return None

    def install_selected(self) -> None:
        app = self._selected_app()
        if not app:
            messagebox.showinfo("Apex Store", "Odaberi aplikaciju s popisa.")
            return
        pkgs = app.get("packages", [])
        if is_installed(pkgs):
            messagebox.showinfo("Apex Store", f"{app['name']} je već instaliran.")
            return
        if not messagebox.askyesno("Apex Store", f"Instalirati {app['name']}?\n\nPaketi: {', '.join(pkgs)}"):
            return
        if run_pacman(True, pkgs):
            messagebox.showinfo("Apex Store", f"{app['name']} je instaliran.")
            self.refresh_list()
        else:
            messagebox.showerror("Apex Store", "Instalacija nije uspjela. Provjeri internet i lozinku.")

    def remove_selected(self) -> None:
        app = self._selected_app()
        if not app:
            messagebox.showinfo("Apex Store", "Odaberi aplikaciju s popisa.")
            return
        pkgs = app.get("packages", [])
        if not is_installed(pkgs):
            messagebox.showinfo("Apex Store", f"{app['name']} nije instaliran.")
            return
        if not messagebox.askyesno("Apex Store", f"Ukloniti {app['name']}?"):
            return
        if run_pacman(False, pkgs):
            messagebox.showinfo("Apex Store", f"{app['name']} je uklonjen.")
            self.refresh_list()
        else:
            messagebox.showerror("Apex Store", "Uklanjanje nije uspjelo.")


def main() -> None:
    if not shutil.which("pacman"):
        print("Apex Store radi samo na Apex OS / Arch Linuxu.", file=sys.stderr)
        sys.exit(1)
    app = ApexStoreApp()
    app.mainloop()


if __name__ == "__main__":
    main()
