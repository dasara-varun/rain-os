#!/usr/bin/env python3
"""
Rain OS Welcome & First-Run Graphical Assistant
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

class RainWelcomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to Rain OS")
        self.geometry("720x640")
        self.minsize(680, 580)
        self.configure(bg=BG_COLOR)

        self._find_logo()
        self._build_ui()

    def _find_logo(self):
        possible_paths = [
            "/usr/share/pixmaps/rain-os.png",
            "/usr/share/icons/hicolor/256x256/apps/rain-os.png",
            os.path.join(os.path.dirname(__file__), "..", "..", "branding", "rain-logo.png"),
            os.path.join(os.path.dirname(__file__), "rain-logo.png"),
            r"E:\rain os\branding\rain-logo.png"
        ]
        self.logo_path = None
        for p in possible_paths:
            if os.path.exists(p):
                self.logo_path = p
                break

    def _build_ui(self):
        # Header Container
        header_frame = tk.Frame(self, bg=BG_COLOR)
        header_frame.pack(fill="x", padx=30, pady=(20, 10))

        # Logo
        if self.logo_path:
            try:
                pil_img = Image.open(self.logo_path).resize((80, 80), Image.Resampling.LANCZOS)
                self.tk_logo = ImageTk.PhotoImage(pil_img)
                logo_label = tk.Label(header_frame, image=self.tk_logo, bg=BG_COLOR)
                logo_label.pack(side="left", padx=(0, 20))
            except Exception:
                pass

        # Title & Subtitle
        title_box = tk.Frame(header_frame, bg=BG_COLOR)
        title_box.pack(side="left", fill="both", expand=True)

        title_label = tk.Label(
            title_box,
            text="Rain OS 1.0.0 (Core)",
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

        # Divider
        divider = tk.Frame(self, bg=BORDER_COLOR, height=1)
        divider.pack(fill="x", padx=30, pady=10)

        # Main Body (2 Columns: System Info & Quick Actions)
        body = tk.Frame(self, bg=BG_COLOR)
        body.pack(fill="both", expand=True, padx=30, pady=10)

        # Left Column: Hardware / System Specs Card
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
            lbl = tk.Label(row, text=label, font=("Segoe UI", 10, "bold"), fg=TEXT_MUTED, bg=CARD_BG, width=14, anchor="w")
            lbl.pack(side="left")
            val_lbl = tk.Label(row, text=val, font=("Segoe UI", 10), fg=TEXT_COLOR, bg=CARD_BG, anchor="w")
            val_lbl.pack(side="left", fill="x", expand=True)

        # Right Column: Action Buttons
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
        self._create_btn(right_card, "⚙️  Rain Control Center", self._run_control_center)
        self._create_btn(right_card, "🖥️  Hardware & Driver Wizard", self._run_hardware_wizard)
        self._create_btn(right_card, "🛡️  System Recovery & Health", self._run_recovery)
        self._create_btn(right_card, "🔄  Update Safety Preflight", self._run_preflight)
        self._create_btn(right_card, "📖  Rain Learning Hub (Lessons)", self._run_learning_hub)

        # Footer Status Bar
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
        fg = "#0a101a" if highlight else TEXT_COLOR
        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold" if highlight else "normal"),
            bg=bg,
            fg=fg,
            activebackground=ACCENT_HOVER if highlight else "#283b56",
            activeforeground="#0a101a" if highlight else TEXT_COLOR,
            bd=0,
            anchor="w",
            padx=15,
            pady=8,
            cursor="hand2",
            command=cmd
        )
        btn.pack(fill="x", padx=15, pady=6)

    def _get_specs(self):
        import platform
        uname = platform.uname()
        kernel = uname.release
        arch = uname.machine

        # CPU info
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

        # Memory info
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
            ("Distribution:", "Rain OS 1.0.0"),
            ("Active Profile:", "Core (Standard)"),
            ("Kernel:", kernel),
            ("Architecture:", arch),
            ("Processor:", cpu[:26] + ("..." if len(cpu) > 26 else "")),
            ("Memory:", mem),
            ("Telemetry:", "Disabled (Private)")
        ]

    def _run_installer(self):
        paths = ["/usr/local/bin/rain-install-launcher", "/usr/bin/calamares", "/usr/bin/archinstall"]
        for p in paths:
            if os.path.exists(p):
                subprocess.Popen([p])
                return
        messagebox.showinfo("Installer", "Rain OS installer ready. Run '/usr/local/bin/rain-install-launcher' in terminal.")

    def _run_control_center(self):
        cmd = ["rain-control-center"] if os.path.exists("/usr/bin/rain-control-center") else ["python3", "-m", "rain_control_center"]
        try:
            subprocess.Popen(cmd)
        except Exception:
            messagebox.showinfo("Control Center", "Launching Rain Control Center...")

    def _run_hardware_wizard(self):
        paths = ["/usr/local/bin/rain-hardware-report", "/usr/bin/rain-hardware-report"]
        found = None
        for p in paths:
            if os.path.exists(p):
                found = p
                break
        if found:
            try:
                subprocess.Popen(["konsole", "-e", found])
            except Exception:
                subprocess.Popen([found])
        else:
            messagebox.showinfo("Hardware Wizard", "Run 'rain-hardware-report' in terminal.")

    def _run_recovery(self):
        try:
            subprocess.Popen(["konsole", "-e", "rain-recovery", "status"])
        except Exception:
            messagebox.showinfo("Recovery", "Run 'rain-recovery status' in terminal.")

    def _run_preflight(self):
        try:
            subprocess.Popen(["konsole", "-e", "rain-update-preflight"])
        except Exception:
            messagebox.showinfo("Preflight", "Run 'rain-update-preflight' in terminal.")

    def _run_learning_hub(self):
        try:
            subprocess.Popen(["konsole", "-e", "rain-guide"])
        except Exception:
            messagebox.showinfo("Learning Hub", "Run 'rain-guide' in terminal.")

if __name__ == "__main__":
    app = RainWelcomeApp()
    app.mainloop()
