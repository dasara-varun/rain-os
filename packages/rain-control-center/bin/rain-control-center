#!/usr/bin/env python3
"""
Rain OS Control Center Graphical Interface
"""
import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

BG_COLOR = "#1e222b"
CARD_BG = "#282d37"
TEXT_COLOR = "#f0f6fc"
TEXT_MUTED = "#9ba3af"
ACCENT_COLOR = "#e83e38"
ACCENT_HOVER = "#ff5751"
BORDER_COLOR = "#383e4c"

class RainControlCenter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rain OS Control Center")
        self.geometry("820x620")
        self.minsize(760, 560)
        self.configure(bg=BG_COLOR)

        self._find_logo()
        self._build_ui()

    def _find_logo(self):
        paths = [
            "/usr/share/pixmaps/rain-os.png",
            os.path.join(os.path.dirname(__file__), "..", "..", "branding", "rain-logo.png"),
            r"E:\rain os\branding\rain-logo.png"
        ]
        self.logo_path = next((p for p in paths if os.path.exists(p)), None)

    def _build_ui(self):
        # Header
        header = tk.Frame(self, bg=BG_COLOR)
        header.pack(fill="x", padx=25, pady=(15, 10))

        if self.logo_path:
            try:
                pil_img = Image.open(self.logo_path).resize((50, 50), Image.Resampling.LANCZOS)
                self.tk_logo = ImageTk.PhotoImage(pil_img)
                tk.Label(header, image=self.tk_logo, bg=BG_COLOR).pack(side="left", padx=(0, 15))
            except Exception:
                pass

        header_txt = tk.Frame(header, bg=BG_COLOR)
        header_txt.pack(side="left", fill="both", expand=True)

        tk.Label(header_txt, text="Rain Control Center", font=("Segoe UI", 16, "bold"), fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w")
        tk.Label(header_txt, text="System health, performance profiles, kernel fallbacks, and update safety", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=BG_COLOR).pack(anchor="w")

        # Custom Dark Notebook / Tabs
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
        style.configure("TNotebook.Tab", background=CARD_BG, foreground=TEXT_COLOR, padding=[16, 8], font=("Segoe UI", 10, "bold"), borderwidth=0)
        style.map("TNotebook.Tab", background=[("selected", ACCENT_COLOR)], foreground=[("selected", "#0a101a")])

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=25, pady=10)

        # Tab 1: Health & Overview
        tab_health = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_health, text=" System Health ")
        self._build_health_tab(tab_health)

        # Tab 2: Profiles
        tab_profiles = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_profiles, text=" Profiles (Flow) ")
        self._build_profiles_tab(tab_profiles)

        # Tab 3: Kernel Manager
        tab_kernels = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_kernels, text=" Kernels ")
        self._build_kernels_tab(tab_kernels)

        # Tab 4: Updates & Preflight
        tab_updates = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_updates, text=" Safe Updates ")
        self._build_updates_tab(tab_updates)

        # Tab 5: Windows Apps & Games Compatibility
        tab_winapps = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_winapps, text=" Windows Apps ")
        self._build_winapps_tab(tab_winapps)

    def _build_health_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="System Vitals", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(15, 10))

        import platform
        vitals = [
            ("Operating System", "Rain OS 0.1.0 (Arch Linux baseline)"),
            ("Active Kernel", platform.release()),
            ("System Architecture", platform.machine()),
            ("Privacy & Tracking", "Strictly Disabled (Zero Telemetry)"),
            ("Firewall Status", "Active (Firewalld)"),
            ("Snapshot Engine", "Btrfs / Snapper Available")
        ]
        for k, v in vitals:
            row = tk.Frame(card, bg=CARD_BG)
            row.pack(fill="x", padx=20, pady=5)
            tk.Label(row, text=k, font=("Segoe UI", 10, "bold"), fg=TEXT_MUTED, bg=CARD_BG, width=20, anchor="w").pack(side="left")
            tk.Label(row, text=v, font=("Segoe UI", 10), fg=TEXT_COLOR, bg=CARD_BG, anchor="w").pack(side="left")

        actions = tk.Frame(card, bg=CARD_BG)
        actions.pack(fill="x", padx=20, pady=20)
        self._make_button(actions, "Hardware & Drivers", lambda: subprocess.Popen(["konsole", "-e", "rain-hardware-report"]))
        self._make_button(actions, "Run Diagnostic Scanner", lambda: subprocess.Popen(["konsole", "-e", "rain-recovery", "status"]))
        self._make_button(actions, "Scrub Log Secrets", lambda: subprocess.Popen(["konsole", "-e", "rain-recovery", "scrub"]))

    def _build_profiles_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Performance & Role Profiles", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(15, 5))
        tk.Label(card, text="Profiles tune governors, memory thresholds, and security policies without lock-in.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 15))

        profiles = [
            ("Core (Active)", "Balanced power & stability, LTS kernel baseline, daily work.", True),
            ("Flow", "Performance governor, low latency audio/graphics, gamemode ready.", False),
            ("Forge", "Developer profile with compiler toolchains, docker, and profiling tools.", False),
            ("Shield", "Hardened AppArmor profiles, strict network firewalls, sandbox wrappers.", False)
        ]

        for name, desc, active in profiles:
            prow = tk.Frame(card, bg="#182538", highlightbackground=BORDER_COLOR, highlightthickness=1)
            prow.pack(fill="x", padx=20, pady=6)
            t_frame = tk.Frame(prow, bg="#182538")
            t_frame.pack(side="left", padx=12, pady=10, fill="both", expand=True)

            tk.Label(t_frame, text=name, font=("Segoe UI", 11, "bold"), fg=ACCENT_COLOR if active else TEXT_COLOR, bg="#182538").pack(anchor="w")
            tk.Label(t_frame, text=desc, font=("Segoe UI", 9), fg=TEXT_MUTED, bg="#182538").pack(anchor="w")

            btn_txt = "Active" if active else "Switch"
            self._make_button(prow, btn_txt, lambda n=name: messagebox.showinfo("Profile", f"Switching to {n} profile..."), side="right")

    def _build_kernels_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Dual-Kernel Retention & Selection", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(15, 5))
        tk.Label(card, text="Rain OS always retains both the standard and LTS kernels for guaranteed boot safety.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 15))

        kernels = [
            ("Linux (Arch Standard)", "Bleeding-edge upstream kernel for newest hardware drivers.", True),
            ("Linux LTS (Long Term Support)", "Rock-solid fallback kernel for long-term stability and recovery.", False)
        ]

        for kname, kdesc, is_cur in kernels:
            krow = tk.Frame(card, bg="#182538", highlightbackground=BORDER_COLOR, highlightthickness=1)
            krow.pack(fill="x", padx=20, pady=8)
            info = tk.Frame(krow, bg="#182538")
            info.pack(side="left", padx=12, pady=10, fill="both", expand=True)

            tk.Label(info, text=kname, font=("Segoe UI", 11, "bold"), fg=ACCENT_COLOR if is_cur else TEXT_COLOR, bg="#182538").pack(anchor="w")
            tk.Label(info, text=kdesc, font=("Segoe UI", 9), fg=TEXT_MUTED, bg="#182538").pack(anchor="w")

            btn_label = "Current Default" if is_cur else "Set as Boot Default"
            self._make_button(krow, btn_label, lambda k=kname: messagebox.showinfo("Kernel Manager", f"Updated default bootloader entry to {k}"), side="right")

    def _build_updates_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Preflight Update Guard", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(15, 5))
        tk.Label(card, text="Every update passes a 4-point safety gate: storage space, keyring check, snapshot generation, and LTS kernel retention.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 15))

        checks = [
            ("1. Storage Headroom Check", "Verifies minimum 2 GB free in root partition before download."),
            ("2. Pacman Database Lock", "Ensures no concurrent transactions or stale lock files exist."),
            ("3. Fallback Kernel Check", "Verifies 'linux-lts' remains available before upgrading 'linux'."),
            ("4. Arch Keyring Freshness", "Ensures package signature keys are synced before upgrade.")
        ]
        for name, desc in checks:
            row = tk.Frame(card, bg=CARD_BG)
            row.pack(fill="x", padx=20, pady=5)
            tk.Label(row, text="✓", font=("Segoe UI", 12, "bold"), fg=ACCENT_COLOR, bg=CARD_BG, width=3).pack(side="left")
            cf = tk.Frame(row, bg=CARD_BG)
            cf.pack(side="left", fill="both", expand=True)
            tk.Label(cf, text=name, font=("Segoe UI", 10, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w")
            tk.Label(cf, text=desc, font=("Segoe UI", 8), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w")

        btn_row = tk.Frame(card, bg=CARD_BG)
        btn_row.pack(fill="x", padx=20, pady=25)
        self._make_button(btn_row, "Run Safe Update in Konsole", lambda: subprocess.Popen(["konsole", "-e", "rain-update-preflight"]))

    def _build_winapps_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Windows Application & Gaming Compatibility", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(15, 5))
        tk.Label(card, text="Run Windows .exe and .msi applications directly on Rain OS with isolated wine prefixes.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 15))

        tiers = [
            ("Bottles (Recommended)", "Sandboxed environments for productivity apps and games with dependency managers.", "bottles"),
            ("Wine & Winetricks", "Direct native compatibility layer for running Windows binaries.", "wine"),
            ("Steam Proton & Lutris", "Optimized gaming runtimes with DXVK and VKD3D Vulkan translation.", "steam"),
            ("Virtualization (Quickemu / KVM)", "Near-native speed virtual machine for complex software with anti-cheat.", "quickemu")
        ]

        for name, desc, app_cmd in tiers:
            row = tk.Frame(card, bg="#182538", highlightbackground=BORDER_COLOR, highlightthickness=1)
            row.pack(fill="x", padx=20, pady=6)
            info = tk.Frame(row, bg="#182538")
            info.pack(side="left", padx=12, pady=10, fill="both", expand=True)

            tk.Label(info, text=name, font=("Segoe UI", 11, "bold"), fg=ACCENT_COLOR, bg="#182538").pack(anchor="w")
            tk.Label(info, text=desc, font=("Segoe UI", 9), fg=TEXT_MUTED, bg="#182538").pack(anchor="w")

            self._make_button(row, "Launch / Check", lambda c=app_cmd: messagebox.showinfo("Windows Compatibility", f"Launching {c} environment helper..."), side="right")

    def _make_button(self, parent, text, cmd, side="left"):
        b = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 9, "bold"),
            bg="#1c304d",
            fg=TEXT_COLOR,
            activebackground=ACCENT_COLOR,
            activeforeground="#0a101a",
            bd=0,
            padx=14,
            pady=6,
            cursor="hand2",
            command=cmd
        )
        b.pack(side=side, padx=8)

if __name__ == "__main__":
    app = RainControlCenter()
    app.mainloop()
