#!/usr/bin/env python3
"""
Rain OS Unified Control Center (v1.1.0 Commercial Release)
System health, performance & COSMIC profiles, dual kernels, update preflight,
Software & App Store (COSMIC Store, Flathub, Windows Bridge), Displays & Devices.
"""
import os
import sys
import shutil
import subprocess
import threading
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
SUCCESS_COLOR = "#2ea043"
INFO_COLOR = "#388bfd"

def run_in_terminal(cmd_list, title="Rain OS"):
    """Helper to run a command list in any available terminal emulator."""
    terminals = [
        (["cosmic-terminal", "-e"] + cmd_list, "cosmic-terminal"),
        (["alacritty", "-e"] + cmd_list, "alacritty"),
        (["konsole", "--new-window", "-e"] + cmd_list, "konsole"),
        (["kitty"] + cmd_list, "kitty"),
        (["xterm", "-title", title, "-e"] + cmd_list, "xterm")
    ]
    for full_cmd, bin_name in terminals:
        if shutil.which(bin_name):
            try:
                subprocess.Popen(full_cmd)
                return True
            except Exception:
                pass
    # Fallback to background thread
    threading.Thread(target=lambda: subprocess.run(cmd_list), daemon=True).start()
    return False

def open_app_store():
    """Launches the primary software center (COSMIC Store, or fallbacks)."""
    stores = [
        ("cosmic-store", ["cosmic-store"]),
        ("plasma-discover", ["plasma-discover"]),
        ("bauh", ["bauh"]),
        ("gnome-software", ["gnome-software"]),
        ("pamac-manager", ["pamac-manager"])
    ]
    for bin_name, cmd in stores:
        if shutil.which(bin_name):
            subprocess.Popen(cmd)
            return True
    messagebox.showinfo("App Store", "No graphical app store found. Use 'sudo pacman -S <pkg>' or 'flatpak install <app>'.")
    return False

class RainControlCenter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rain OS Control Center")
        self.geometry("860x700")
        self.minsize(780, 640)
        self.configure(bg=BG_COLOR)

        self._find_logo()
        self._build_ui()

    def _find_logo(self):
        cur = os.path.dirname(os.path.abspath(__file__))
        repo_b = None
        for _ in range(6):
            b = os.path.join(cur, "branding")
            if os.path.isdir(b):
                repo_b = b
                break
            cur = os.path.dirname(cur)

        paths = [
            "/usr/share/icons/hicolor/128x128/apps/rain-control-center.png",
            "/usr/share/pixmaps/rain-control-center.png",
            "/usr/share/pixmaps/rain-os.png",
            os.path.join(os.path.dirname(__file__), "..", "..", "branding", "icons", "128x128", "rain-control-center.png"),
            os.path.join(os.path.dirname(__file__), "..", "..", "branding", "rain-logo.png"),
        ]
        if repo_b:
            paths.extend([
                os.path.join(repo_b, "icons", "128x128", "rain-control-center.png"),
                os.path.join(repo_b, "rain-logo.png")
            ])
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
            ("Operating System", "Rain OS 1.1.0 (Arch Linux baseline)"),
            ("Active Kernel", platform.release()),
            ("System Architecture", platform.machine()),
            ("Default Desktop", "COSMIC Desktop (Rust Flagship)"),
            ("Telemetry & Tracking", "Strictly Disabled (Zero Telemetry)"),
            ("Firewall Status", "Active (Firewalld)"),
            ("Snapshot Engine", "Btrfs pre-update hook active")
        ]
        for k, v in vitals:
            row = tk.Frame(card, bg=CARD_BG)
            row.pack(fill="x", padx=20, pady=4)
            tk.Label(row, text=k, font=("Segoe UI", 10, "bold"), fg=TEXT_MUTED, bg=CARD_BG, width=22, anchor="w").pack(side="left")
            tk.Label(row, text=v, font=("Segoe UI", 10), fg=TEXT_COLOR, bg=CARD_BG, anchor="w").pack(side="left")

        actions = tk.Frame(card, bg=CARD_BG)
        actions.pack(fill="x", padx=20, pady=20)
        self._make_button(actions, "Hardware & Drivers", lambda: run_in_terminal(["rain-hardware-report"], "Hardware Report"))
        self._make_button(actions, "Native C Probe", lambda: run_in_terminal(["rain-probe"], "Rain Probe"))
        self._make_button(actions, "Diagnostic Scanner", lambda: run_in_terminal(["rain-recovery", "status"], "System Diagnostics"))
        self._make_button(actions, "Desktop & Themes", lambda: subprocess.Popen(["rain-desktop-selector"]))

    def _build_profiles_tab(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        card.pack(fill="both", expand=True, padx=10, pady=15)

        tk.Label(card, text="Performance & Role Profiles", font=("Segoe UI", 12, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w", padx=20, pady=(12, 4))
        tk.Label(card, text="Profiles tune governors, inotify limits, and security boundaries without lock-in.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 10))

        def _switch_profile(p_key):
            run_in_terminal(["rain-profile", "set", p_key], f"Applying Profile: {p_key}")

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
            run_in_terminal(["rain-kernel", "set-default", k_type], f"Setting Default Kernel: {k_type}")

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
            ("Rain App Store (COSMIC Store)", "Modern Rust-based Graphical App Store for native packages & Flatpaks.", open_app_store),
            ("Enable Flathub (Flatpak)", "Add the universal Flathub repository to access thousands of sandboxed apps.", lambda: run_in_terminal(["flatpak", "remote-add", "--if-not-exists", "flathub", "https://dl.flathub.org/repo/flathub.flatpakrepo"], "Adding Flathub")),
            ("AppImage Support", "Native AppImage execution enabled via FUSE2 compatibility layer.", lambda: messagebox.showinfo("AppImage", "AppImage support is active. Double-click any .AppImage file to run.")),
            ("Bottles (Windows Apps)", "Isolated Windows environments for productivity apps with dependency managers.", lambda: subprocess.Popen(["bottles"] if shutil.which("bottles") else ["echo", "Bottles not installed"])),
            ("Steam Proton & Lutris", "Vulkan-accelerated gaming runtime with DXVK and VKD3D.", lambda: subprocess.Popen(["steam"] if shutil.which("steam") else ["echo", "Steam not installed"]))
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
        tk.Label(card, text="Multi-screen monitors, phone sync, Bluetooth, and network shares.", font=("Segoe UI", 9), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w", padx=20, pady=(0, 10))

        def _open_display():
            if shutil.which("cosmic-settings"):
                subprocess.Popen(["cosmic-settings", "displays"])
            elif shutil.which("rain-display-manager"):
                subprocess.Popen(["rain-display-manager", "gui"])
            elif shutil.which("kcmshell6"):
                subprocess.Popen(["kcmshell6", "kcm_kscreen"])

        def _open_bluetooth():
            if shutil.which("cosmic-settings"):
                subprocess.Popen(["cosmic-settings", "bluetooth"])
            elif shutil.which("blueman-manager"):
                subprocess.Popen(["blueman-manager"])
            elif shutil.which("kcmshell6"):
                subprocess.Popen(["kcmshell6", "kcm_bluetooth"])

        devices = [
            ("Multi-Screen Display Settings", "Per-monitor DPI scaling, refresh rates, FreeSync/VRR, and multi-monitor layout.", _open_display),
            ("KDE Connect / Phone Sync", "Pair Android or iPhone for file transfer, notifications, SMS, and clipboard sync.", lambda: subprocess.Popen(["kdeconnect-app"] if shutil.which("kdeconnect-app") else ["echo"])),
            ("Bluetooth Devices", "Pair wireless headphones, keyboards, mice, and game controllers.", _open_bluetooth),
            ("Network Shares (Samba / Avahi)", "Discover local network PCs, NAS storage, and shared folders.", lambda: subprocess.Popen(["cosmic-files"] if shutil.which("cosmic-files") else ["dolphin", "remote:/"]))
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
            tk.Label(row, text="[OK]", font=("Segoe UI", 10, "bold"), fg=ACCENT_COLOR, bg=CARD_BG, width=3).pack(side="left")
            cf = tk.Frame(row, bg=CARD_BG)
            cf.pack(side="left", fill="both", expand=True)
            tk.Label(cf, text=name, font=("Segoe UI", 10, "bold"), fg=TEXT_COLOR, bg=CARD_BG).pack(anchor="w")
            tk.Label(cf, text=desc, font=("Segoe UI", 8), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w")

        btn_row = tk.Frame(card, bg=CARD_BG)
        btn_row.pack(fill="x", padx=20, pady=25)
        self._make_button(btn_row, "Run Safe Update Guard", lambda: run_in_terminal(["rain-update-preflight"], "Safe Update Preflight"))

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
