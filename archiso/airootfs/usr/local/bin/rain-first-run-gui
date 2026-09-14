#!/usr/bin/env python3
"""
Rain OS Welcome & First-Run Graphical Assistant (v1.1.0)
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
    threading.Thread(target=lambda: subprocess.run(cmd_list), daemon=True).start()
    return False

class RainWelcomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to Rain OS")
        self.geometry("740x660")
        self.minsize(700, 600)
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

        possible_paths = [
            "/usr/share/icons/hicolor/128x128/apps/rain-welcome.png",
            "/usr/share/pixmaps/rain-welcome.png",
            "/usr/share/pixmaps/rain-os.png",
            "/usr/share/icons/hicolor/256x256/apps/rain-os.png",
            os.path.join(os.path.dirname(__file__), "..", "..", "branding", "icons", "128x128", "rain-welcome.png"),
            os.path.join(os.path.dirname(__file__), "..", "..", "branding", "rain-logo.png"),
        ]
        if repo_b:
            possible_paths.extend([
                os.path.join(repo_b, "icons", "128x128", "rain-welcome.png"),
                os.path.join(repo_b, "rain-logo.png")
            ])
        self.logo_path = None
        for p in possible_paths:
            if os.path.exists(p):
                self.logo_path = p
                break

    def _build_ui(self):
        header_frame = tk.Frame(self, bg=BG_COLOR)
        header_frame.pack(fill="x", padx=30, pady=(20, 10))

        if self.logo_path:
            try:
                pil_img = Image.open(self.logo_path).resize((72, 72), Image.Resampling.LANCZOS)
                self.tk_logo = ImageTk.PhotoImage(pil_img)
                logo_label = tk.Label(header_frame, image=self.tk_logo, bg=BG_COLOR)
                logo_label.pack(side="left", padx=(0, 20))
            except Exception:
                pass

        title_box = tk.Frame(header_frame, bg=BG_COLOR)
        title_box.pack(side="left", fill="both", expand=True)

        title_label = tk.Label(
            title_box,
            text="Rain OS 1.1.0 (Core)",
            font=("Segoe UI", 20, "bold"),
            fg=TEXT_COLOR,
            bg=BG_COLOR,
            anchor="w"
        )
        title_label.pack(fill="x")

        subtitle_label = tk.Label(
            title_box,
            text="Shelter from complexity, without hiding the system.",
            font=("Segoe UI", 11, "italic"),
            fg=ACCENT_COLOR,
            bg=BG_COLOR,
            anchor="w"
        )
        subtitle_label.pack(fill="x", pady=(3, 0))

        divider = tk.Frame(self, bg=BORDER_COLOR, height=1)
        divider.pack(fill="x", padx=30, pady=10)

        body = tk.Frame(self, bg=BG_COLOR)
        body.pack(fill="both", expand=True, padx=30, pady=10)

        left_card = tk.Frame(body, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        left_card.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=5)

        card_title = tk.Label(
            left_card,
            text="System Baseline",
            font=("Segoe UI", 12, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_BG
        )
        card_title.pack(anchor="w", padx=15, pady=(15, 10))

        specs = self._get_specs()
        for label, val in specs:
            row = tk.Frame(left_card, bg=CARD_BG)
            row.pack(fill="x", padx=15, pady=4)
            lbl = tk.Label(row, text=label, font=("Segoe UI", 10, "bold"), fg=TEXT_MUTED, bg=CARD_BG, width=15, anchor="w")
            lbl.pack(side="left")
            val_lbl = tk.Label(row, text=val, font=("Segoe UI", 10), fg=TEXT_COLOR, bg=CARD_BG, anchor="w")
            val_lbl.pack(side="left", fill="x", expand=True)

        right_card = tk.Frame(body, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        right_card.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=5)

        actions_title = tk.Label(
            right_card,
            text="Quick Launch",
            font=("Segoe UI", 12, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_BG
        )
        actions_title.pack(anchor="w", padx=15, pady=(15, 10))

        self._create_btn(right_card, "🚀  Install Rain OS to Disk", self._run_installer, highlight=True)
        self._create_btn(right_card, "🖵  Desktop & WM Selector", self._run_desktop_selector)
        self._create_btn(right_card, "⚙️  Rain Control Center", self._run_control_center)
        self._create_btn(right_card, "🛍️  Rain App Store (COSMIC)", self._run_app_store)
        self._create_btn(right_card, "🖥️  Hardware & Driver Wizard", self._run_hardware_wizard)
        self._create_btn(right_card, "🛡️  System Recovery & Health", self._run_recovery)
        self._create_btn(right_card, "🔄  Update Safety Preflight", self._run_preflight)
        self._create_btn(right_card, "📖  Rain Learning Hub (Lessons)", self._run_learning_hub)

        footer = tk.Frame(self, bg=BG_COLOR)
        footer.pack(fill="x", padx=30, pady=(10, 20))

        status_text = "Rain OS Core  •  Zero Telemetry  •  Arch Linux Baseline  •  GPL-3.0"
        status_lbl = tk.Label(footer, text=status_text, font=("Segoe UI", 9), fg=TEXT_MUTED, bg=BG_COLOR)
        status_lbl.pack(side="left")

        quit_btn = tk.Button(
            footer,
            text="Close",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=CARD_BG,
            activebackground=BORDER_COLOR,
            activeforeground=TEXT_COLOR,
            bd=0,
            padx=12,
            pady=4,
            command=self.destroy
        )
        quit_btn.pack(side="right")

    def _create_btn(self, parent, text, cmd, highlight=False):
        bg = ACCENT_COLOR if highlight else "#1b293e"
        fg = "#ffffff" if highlight else TEXT_COLOR
        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold" if highlight else "normal"),
            bg=bg,
            fg=fg,
            activebackground=ACCENT_HOVER if highlight else "#283b56",
            activeforeground="#ffffff" if highlight else TEXT_COLOR,
            bd=0,
            anchor="w",
            padx=15,
            pady=6,
            cursor="hand2",
            command=cmd
        )
        btn.pack(fill="x", padx=15, pady=4)

    def _get_specs(self):
        import platform
        uname = platform.uname()
        kernel = uname.release
        arch = uname.machine

        cpu = uname.processor or "Generic x86_64"
        if sys.platform.startswith("linux"):
            try:
                with open("/proc/cpuinfo") as f:
                    for line in f:
                        if "model name" in line:
                            cpu = line.split(":")[1].strip()
                            break
            except Exception:
                pass

        mem = "Available"
        if sys.platform.startswith("linux"):
            try:
                with open("/proc/meminfo") as f:
                    for line in f:
                        if "MemTotal" in line:
                            kb = int(line.split()[1])
                            mem = f"{round(kb / (1024 * 1024), 1)} GB"
                            break
            except Exception:
                pass

        return [
            ("Distribution:", "Rain OS 1.1.0"),
            ("Default Desktop:", "COSMIC (Rust)"),
            ("Active Profile:", "Core (Standard)"),
            ("Kernel:", kernel),
            ("Architecture:", arch),
            ("Processor:", cpu[:24] + ("..." if len(cpu) > 24 else "")),
            ("Memory:", mem),
            ("Telemetry:", "Disabled (Zero Telemetry)")
        ]

    def _run_installer(self):
        paths = ["/usr/local/bin/rain-install-launcher", "/usr/bin/calamares", "/usr/bin/archinstall"]
        for p in paths:
            if os.path.exists(p):
                subprocess.Popen([p])
                return
        messagebox.showinfo("Installer", "Rain OS installer ready. Run '/usr/local/bin/rain-install-launcher' in terminal.")

    def _run_desktop_selector(self):
        if shutil.which("rain-desktop-selector"):
            subprocess.Popen(["rain-desktop-selector"])
        else:
            messagebox.showinfo("Desktop Selector", "Run 'rain-desktop-selector' in terminal.")

    def _run_control_center(self):
        if shutil.which("rain-control-center"):
            subprocess.Popen(["rain-control-center"])
        else:
            messagebox.showinfo("Control Center", "Run 'rain-control-center' in terminal.")

    def _run_app_store(self):
        stores = ["cosmic-store", "plasma-discover", "bauh", "gnome-software"]
        for s in stores:
            if shutil.which(s):
                subprocess.Popen([s])
                return
        messagebox.showinfo("App Store", "Launch App Store: cosmic-store or use pacman / flatpak.")

    def _run_hardware_wizard(self):
        run_in_terminal(["rain-hardware-report"], "Hardware Report")

    def _run_recovery(self):
        run_in_terminal(["rain-recovery", "status"], "System Recovery")

    def _run_preflight(self):
        run_in_terminal(["rain-update-preflight"], "Update Preflight")

    def _run_learning_hub(self):
        if shutil.which("rain-guide-launcher"):
            subprocess.Popen(["rain-guide-launcher"])
        else:
            run_in_terminal(["rain-guide"], "Rain Learning Hub")

if __name__ == "__main__":
    app = RainWelcomeApp()
    app.mainloop()
