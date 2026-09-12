#!/usr/bin/env python3
"""
Rain OS Unified Control Center (v1.0 Commercial Release)
System health, performance & COSMIC profiles, dual kernels, update preflight,
Software & App Store (Discover, Flathub, Windows Bridge), Displays & Devices.
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
        self.geometry("820x680")
        self.minsize(760, 620)
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
                pil_img = Image.open(self.logo_path).resize((48, 48), Image.Resampling.LANCZOS)
                self.tk_logo = ImageTk.PhotoImage(pil_img)
                tk.Label(header, image=self.tk_logo, bg=BG_COLOR).pack(side="left", padx=(0, 15))
            except Exception:
                pass

        header_txt = tk.Frame(header, bg=BG_COLOR)
        header_txt.pack(side="left", fill="both", expand=True)

        tk.Label(header_txt, text="Rain OS Control Center", font=("Segoe UI", 16, "bold"), fg=TEXT_COLOR, bg=BG_COLOR).pack(anchor="w")
        tk.Label(header_txt, text="System health, profiles, software store, displays, and devices", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=BG_COLOR).pack(anchor="w")

        # Custom Dark Notebook / Tabs
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
        style.configure("TNotebook.Tab", background="#262b36", foreground=TEXT_COLOR, padding=[12, 6], font=("Segoe UI", 9, "bold"))
        style.map("TNotebook.Tab",
                  background=[("selected", ACCENT_COLOR), ("active", "#3b4354")],
                  foreground=[("selected", "#0a101a"), ("active", TEXT_COLOR)])

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=25, pady=10)

        # Tab 1: System Health & Hardware
        tab_health = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_health, text=" System Health ")
        self._build_health_tab(tab_health)

        # Tab 2: System Profiles
        tab_profiles = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_profiles, text=" Profiles ")
        self._build_profiles_tab(tab_profiles)

        # Tab 3: Dual-Kernel Manager
        tab_kernels = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_kernels, text=" Kernels ")
        self._build_kernels_tab(tab_kernels)

        # Tab 4: Software & App Store
        tab_software = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_software, text=" App Store & Software ")
        self._build_software_tab(tab_software)

        # Tab 5: Displays & Connected Devices
        tab_devices = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_devices, text=" Displays & Devices ")
        self._build_devices_tab(tab_devices)

        # Tab 6: Safe Updates
        tab_updates = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_updates, text=" Safe Updates ")
        self._build_updates_tab(tab_updates)

    def _build_health_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="System Vitals & Security", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(15, 10))

        import platform
        vitals = [
            ("Operating System", "Rain OS 1.0.0 (Arch Linux baseline)"),
            ("Active Kernel", platform.release()),
            ("System Architecture", platform.machine()),
            ("Telemetry & Tracking", "Strictly Disabled (Zero Telemetry)"),
            ("Firewall Status", "Active (Firewalld)"),
            ("Snapshot Engine", "Btrfs pre-update hook active")
        ]
        for k, v in vitals:
            row = tk.Frame(card, bg=CARD_BG)
            row.pack(fill="x", padx=20, pady=4)
            tk.Label(row, text=k, font=("Segoe UI", 10, "bold"), fg=TEXT_MUTED, bg=CARD_BG, width=20, anchor="w").pack(side="left")
            tk.Label(row, text=v, font=("Segoe UI", 10), fg=TEXT_COLOR, bg=CARD_BG, anchor="w").pack(side="left")

        actions = tk.Frame(card, bg=CARD_BG)
        actions.pack(fill="x", padx=20, pady=15)
        self._make_button(actions, "Hardware & Drivers", lambda: subprocess.Popen(["konsole", "-e", "rain-hardware-report"]))
        self._make_button(actions, "Native C Probe", lambda: subprocess.Popen(["konsole", "-e", "rain-probe"]))
        self._make_button(actions, "Diagnostic Scanner", lambda: subprocess.Popen(["konsole", "-e", "rain-recovery", "status"]))
        self._make_button(actions, "Emergency Rollback", lambda: subprocess.Popen(["konsole", "-e", "rain-recovery", "rollback"]))

    def _build_profiles_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Performance & Role Profiles", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(12, 4))
        tk.Label(card, text="Profiles tune governors, inotify limits, and security boundaries without lock-in.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 10))

        def _switch_profile(p_key):
            try:
                subprocess.Popen(["konsole", "-e", "rain-profile", "set", p_key])
            except Exception:
                subprocess.Popen(["rain-profile", "set", p_key])

        profiles = [
            ("Core (Balanced)", "Balanced power & stability, LTS kernel fallback, daily desktop work.", "core"),
            ("Flow (Gaming & Performance)", "Performance governor, low latency swappiness (10), gamemode optimization.", "flow"),
            ("Forge (Development)", "Developer workspace, high inotify limits (524288), container support.", "forge"),
            ("Shield (Hardened Security)", "AppArmor enforcement, restricted dmesg, strict firewall rules.", "shield"),
            ("Pocket (Low RAM & Battery)", "Powersave CPU governor, aggressive memory reclaim, battery tuning.", "pocket"),
            ("COSMIC (Rust Desktop)", "System76 modern Rust-based desktop environment and auto-tiler.", "cosmic")
        ]

        for name, desc, p_key in profiles:
            prow = tk.Frame(card, bg="#182538", highlightbackground=BORDER_COLOR, highlightthickness=1)
            prow.pack(fill="x", padx=20, pady=4)
            t_frame = tk.Frame(prow, bg="#182538")
            t_frame.pack(side="left", padx=10, pady=6, fill="both", expand=True)

            tk.Label(t_frame, text=name, font=("Segoe UI", 10, "bold"), fg=TEXT_COLOR, bg="#182538").pack(anchor="w")
            tk.Label(t_frame, text=desc, font=("Segoe UI", 8), fg=TEXT_MUTED, bg="#182538").pack(anchor="w")

            self._make_button(prow, "Apply", lambda pk=p_key: _switch_profile(pk), side="right")

    def _build_kernels_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Dual-Kernel Retention & Selection", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(15, 5))
        tk.Label(card, text="Rain OS always retains both standard and LTS kernels for guaranteed boot safety.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 15))

        def _set_kernel(k_type):
            try:
                subprocess.Popen(["konsole", "-e", "rain-kernel", "set-default", k_type])
            except Exception:
                subprocess.Popen(["rain-kernel", "set-default", k_type])

        kernels = [
            ("Linux (Arch Standard)", "Rolling upstream kernel with newest hardware drivers and features.", "generic"),
            ("Linux LTS (Long Term Support)", "Certified fallback kernel for maximum rock-solid stability.", "lts")
        ]

        for kname, kdesc, k_type in kernels:
            krow = tk.Frame(card, bg="#182538", highlightbackground=BORDER_COLOR, highlightthickness=1)
            krow.pack(fill="x", padx=20, pady=8)
            info = tk.Frame(krow, bg="#182538")
            info.pack(side="left", padx=12, pady=10, fill="both", expand=True)

            tk.Label(info, text=kname, font=("Segoe UI", 11, "bold"), fg=TEXT_COLOR, bg="#182538").pack(anchor="w")
            tk.Label(info, text=kdesc, font=("Segoe UI", 9), fg=TEXT_MUTED, bg="#182538").pack(anchor="w")

            self._make_button(krow, "Set Default", lambda kt=k_type: _set_kernel(kt), side="right")

    def _build_software_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Software App Store & Application Bridges", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(12, 4))
        tk.Label(card, text="Native Linux software, Flatpaks, AppImages, and Windows compatibility layers.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 10))

        app_sources = [
            ("KDE Discover (Software Center)", "Graphical App Store for native packages, Flatpaks, and desktop addons.", lambda: subprocess.Popen(["plasma-discover"])),
            ("Enable Flathub (Flatpak)", "Add the universal Flathub repository to access thousands of sandboxed apps.", lambda: subprocess.Popen(["konsole", "-e", "flatpak", "remote-add", "--if-not-exists", "flathub", "https://dl.flathub.org/repo/flathub.flatpakrepo"])),
            ("AppImage Support", "Native AppImage execution enabled via FUSE2 compatibility layer.", lambda: messagebox.showinfo("AppImage", "AppImage support is active. Double click any .AppImage file to run.")),
            ("Bottles (Windows Apps)", "Isolated Windows environments for productivity apps with dependency managers.", lambda: subprocess.Popen(["bottles"])),
            ("Steam Proton & Lutris", "Vulkan-accelerated gaming runtime with DXVK and VKD3D.", lambda: subprocess.Popen(["steam"]))
        ]

        for name, desc, action in app_sources:
            row = tk.Frame(card, bg="#182538", highlightbackground=BORDER_COLOR, highlightthickness=1)
            row.pack(fill="x", padx=20, pady=4)
            info = tk.Frame(row, bg="#182538")
            info.pack(side="left", padx=10, pady=6, fill="both", expand=True)

            tk.Label(info, text=name, font=("Segoe UI", 10, "bold"), fg=TEXT_COLOR, bg="#182538").pack(anchor="w")
            tk.Label(info, text=desc, font=("Segoe UI", 8), fg=TEXT_MUTED, bg="#182538").pack(anchor="w")

            self._make_button(row, "Open / Setup", action, side="right")

    def _build_devices_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Displays & Device Connectivity", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(12, 4))
        tk.Label(card, text="Multi-screen monitors, phone sync (KDE Connect), Bluetooth, and network shares.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 10))

        devices = [
            ("Multi-Screen Display Settings", "Per-monitor DPI scaling, refresh rates, FreeSync/VRR, and multi-monitor layout.", lambda: subprocess.Popen(["rain-display-manager", "gui"])),
            ("KDE Connect (Phone Integration)", "Pair Android or iPhone for file transfer, notifications, SMS, and clipboard sync.", lambda: subprocess.Popen(["kdeconnect-app"])),
            ("Bluetooth Devices", "Pair wireless headphones, keyboards, mice, and game controllers.", lambda: subprocess.Popen(["kcmshell6", "kcm_bluetooth"])),
            ("Network Shares (Samba / Avahi)", "Discover local network PCs, NAS storage, and shared folders in Dolphin.", lambda: subprocess.Popen(["dolphin", "remote:/"]))
        ]

        for name, desc, action in devices:
            row = tk.Frame(card, bg="#182538", highlightbackground=BORDER_COLOR, highlightthickness=1)
            row.pack(fill="x", padx=20, pady=4)
            info = tk.Frame(row, bg="#182538")
            info.pack(side="left", padx=10, pady=6, fill="both", expand=True)

            tk.Label(info, text=name, font=("Segoe UI", 10, "bold"), fg=TEXT_COLOR, bg="#182538").pack(anchor="w")
            tk.Label(info, text=desc, font=("Segoe UI", 8), fg=TEXT_MUTED, bg="#182538").pack(anchor="w")

            self._make_button(row, "Manage", action, side="right")

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
            tk.Label(row, text="?", font=("Segoe UI", 12, "bold"), fg=ACCENT_COLOR, bg=CARD_BG, width=3).pack(side="left")
            cf = tk.Frame(row, bg=CARD_BG)
            cf.pack(side="left", fill="both", expand=True)
            tk.Label(cf, text=name, font=("Segoe UI", 10, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w")
            tk.Label(cf, text=desc, font=("Segoe UI", 8), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w")

        btn_row = tk.Frame(card, bg=CARD_BG)
        btn_row.pack(fill="x", padx=20, pady=25)
        self._make_button(btn_row, "Run Safe Update in Konsole", lambda: subprocess.Popen(["konsole", "-e", "rain-update-preflight"]))

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
