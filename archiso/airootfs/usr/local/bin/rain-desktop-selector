#!/usr/bin/env python3
"""
Rain OS Desktop Environment & Window Manager Selector (CachyOS Style)
Unified GUI & CLI utility to choose, install, configure, and switch between:
  - KDE Plasma 6 (Flagship)
  - Hyprland (Dynamic Wayland Tiling Compositor)
  - GNOME (Modern Distraction-Free Shell)
  - i3-wm (Lightweight X11 Tiling Window Manager)
  - COSMIC Desktop (Rust-based Next-Gen Desktop)
  - Sway (i3-Compatible Wayland Compositor)
  - XFCE4 (Lightweight Classic Desktop)

Also features:
  - Omarchy Theme Engine: 10 signature themes adapted from omacom/omarchy
  - 4K Anime Rain Wallpaper Gallery: 12 pristine ultra-high-resolution wallpapers
"""
import os
import sys
import glob
import json
import shutil
import argparse
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Theme constants
BG_COLOR = "#1e222b"
CARD_BG = "#282d37"
CARD_HOVER = "#323846"
TEXT_COLOR = "#f0f6fc"
TEXT_MUTED = "#9ba3af"
ACCENT_COLOR = "#e83e38"
ACCENT_HOVER = "#ff5751"
BORDER_COLOR = "#383e4c"
SUCCESS_COLOR = "#2ea043"
INFO_COLOR = "#388bfd"

# Desktop environments catalog
DESKTOPS = [
    {
        "id": "plasma",
        "name": "KDE Plasma 6",
        "category": "Full Desktop Environment",
        "tagline": "Rain OS Flagship. Modern, customizable, translucent glass UI.",
        "compositor": "KWin (Wayland / X11)",
        "ram": "~450 MB",
        "binary": "startplasma-wayland",
        "fallback_bin": "startplasma-x11",
        "session_name": "plasma",
        "session_file": "plasma.desktop",
        "packages": ["plasma-desktop", "plasma-workspace", "plasma-nm", "dolphin", "konsole", "sddm"],
        "badge": "Default Flagship"
    },
    {
        "id": "hyprland",
        "name": "Hyprland",
        "category": "Dynamic Wayland Tiling Compositor",
        "tagline": "Fluid animations, rounded corners, blur, and deep Omarchy theming.",
        "compositor": "Hyprland (Wayland)",
        "ram": "~220 MB",
        "binary": "Hyprland",
        "fallback_bin": "hyprland",
        "session_name": "hyprland",
        "session_file": "hyprland.desktop",
        "packages": ["hyprland", "waybar", "rofi", "swaybg", "dunst", "kitty"],
        "badge": "Omarchy Native"
    },
    {
        "id": "gnome",
        "name": "GNOME Shell",
        "category": "Full Desktop Environment",
        "tagline": "Distraction-free, gesture-driven desktop designed for focused workflows.",
        "compositor": "Mutter (Wayland)",
        "ram": "~550 MB",
        "binary": "gnome-shell",
        "fallback_bin": "gnome-session",
        "session_name": "gnome",
        "session_file": "gnome.desktop",
        "packages": ["gnome-shell", "gnome-control-center", "nautilus"],
        "badge": "Gesture Driven"
    },
    {
        "id": "i3",
        "name": "i3-wm (Tiling)",
        "category": "Manual Tiling Window Manager",
        "tagline": "Ultra-lightweight keyboard-driven tiling WM. Maximum speed on any hardware.",
        "compositor": "X11 (Picom Compositor)",
        "ram": "~120 MB",
        "binary": "i3",
        "fallback_bin": "i3-wm",
        "session_name": "i3",
        "session_file": "i3.desktop",
        "packages": ["i3-wm", "i3status", "picom", "rofi", "kitty"],
        "badge": "Ultra Lightweight"
    },
    {
        "id": "cosmic",
        "name": "COSMIC Desktop",
        "category": "Modern Rust Desktop Environment",
        "tagline": "Next-generation desktop written in Rust by System76. Built for high performance.",
        "compositor": "cosmic-comp (Wayland)",
        "ram": "~380 MB",
        "binary": "cosmic-session",
        "fallback_bin": "cosmic-comp",
        "session_name": "cosmic",
        "session_file": "cosmic.desktop",
        "packages": ["cosmic-session"],
        "badge": "Rust Engine"
    },
    {
        "id": "sway",
        "name": "Sway",
        "category": "i3-Compatible Wayland Compositor",
        "tagline": "Drop-in replacement for i3 on Wayland. Smooth tear-free rendering.",
        "compositor": "wlroots (Wayland)",
        "ram": "~160 MB",
        "binary": "sway",
        "fallback_bin": "sway",
        "session_name": "sway",
        "session_file": "sway.desktop",
        "packages": ["sway", "waybar", "rofi", "swaybg"],
        "badge": "Wayland Tiling"
    },
    {
        "id": "xfce",
        "name": "XFCE 4",
        "category": "Lightweight Desktop Environment",
        "tagline": "Classic, modular, battle-tested desktop for older hardware and low resources.",
        "compositor": "Xfwm4 (X11)",
        "ram": "~200 MB",
        "binary": "xfce4-session",
        "fallback_bin": "startxfce4",
        "session_name": "xfce",
        "session_file": "xfce.desktop",
        "packages": ["xfce4-session", "xfdesktop", "xfwm4", "xfce4-panel"],
        "badge": "Classic Lightweight"
    },
    {
        "id": "niri",
        "name": "Niri (Scrollable)",
        "category": "Scrollable-Tiling Wayland Compositor",
        "tagline": "Infinite horizontal ribbon of windows. Fluid animations and touchpad gestures.",
        "compositor": "Niri (Wayland)",
        "ram": "~180 MB",
        "binary": "niri",
        "fallback_bin": "niri-session",
        "session_name": "niri",
        "session_file": "niri.desktop",
        "packages": ["niri", "waybar", "rofi", "swaybg", "alacritty"],
        "badge": "Scrollable Tiling"
    },
    {
        "id": "river",
        "name": "River WM",
        "category": "Dynamic Tiling Wayland Compositor",
        "tagline": "Flexible, dynamic tiling Wayland compositor with rich tag-based workspace management.",
        "compositor": "River (Wayland)",
        "ram": "~140 MB",
        "binary": "river",
        "fallback_bin": "river",
        "session_name": "river",
        "session_file": "river.desktop",
        "packages": ["river", "waybar", "rofi", "swaybg", "alacritty"],
        "badge": "Dynamic Tiling"
    },
    {
        "id": "gamescope",
        "name": "Gamescope + MangoHUD",
        "category": "Gaming Micro-Compositor Session",
        "tagline": "Optimized SteamOS-style gaming session with MangoHUD telemetry and integer scaling.",
        "compositor": "Gamescope (Wayland/Xwayland)",
        "ram": "~150 MB",
        "binary": "gamescope",
        "fallback_bin": "mangoapp",
        "session_name": "gamescope",
        "session_file": "gamescope-wayland.desktop",
        "packages": ["gamescope", "mangohud"],
        "badge": "Gaming Edition"
    }
]

def find_asset_path(subpath):
    candidates = [
        os.path.join("/usr/share/rain-os", subpath),
        os.path.join(os.path.dirname(__file__), "..", "..", "branding", subpath),
        os.path.join(r"E:\rain os\branding", subpath)
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def find_wallpaper_dir():
    candidates = [
        "/usr/share/wallpapers/rain-os",
        os.path.join(os.path.dirname(__file__), "..", "..", "branding", "wallpapers"),
        r"E:\rain os\branding\wallpapers"
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return None

def find_themes_dir():
    candidates = [
        "/usr/share/rain-os/themes",
        os.path.join(os.path.dirname(__file__), "..", "..", "branding", "themes"),
        r"E:\rain os\branding\themes"
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return None

def is_desktop_installed(de):
    for b in [de.get("binary"), de.get("fallback_bin")]:
        if b and shutil.which(b):
            return True
        if b and os.path.exists(os.path.join("/usr/bin", b)):
            return True
    session_file = de.get("session_file")
    for sdir in ["/usr/share/xsessions", "/usr/share/wayland-sessions"]:
        if session_file and os.path.exists(os.path.join(sdir, session_file)):
            return True
    return False

def get_active_desktop():
    cur = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()
    sess = os.environ.get("DESKTOP_SESSION", "").lower()
    comb = f"{cur} {sess}"
    if "plasma" in comb or "kde" in comb:
        return "plasma"
    if "hyprland" in comb:
        return "hyprland"
    if "gnome" in comb:
        return "gnome"
    if "i3" in comb:
        return "i3"
    if "cosmic" in comb:
        return "cosmic"
    if "sway" in comb:
        return "sway"
    if "xfce" in comb:
        return "xfce"
    # Process check fallback
    try:
        procs = subprocess.check_output(["ps", "-A"], text=True)
        if "Hyprland" in procs: return "hyprland"
        if "kwin" in procs: return "plasma"
        if "gnome-shell" in procs: return "gnome"
        if "i3" in procs: return "i3"
        if "sway" in procs: return "sway"
        if "xfce4-session" in procs: return "xfce"
    except Exception:
        pass
    return "plasma"

def switch_default_session(session_name):
    """Configures SDDM / display manager to boot into session_name by default."""
    try:
        os.makedirs("/etc/sddm.conf.d", exist_ok=True)
        sddm_conf = "/etc/sddm.conf.d/10-session.conf"
        content = f"[Autologin]\nSession={session_name}\n\n[General]\nDefaultSession={session_name}\n"
        try:
            with open(sddm_conf, "w", encoding="utf-8") as f:
                f.write(content)
        except PermissionError:
            subprocess.run(["sudo", "mkdir", "-p", "/etc/sddm.conf.d"], check=False)
            cmd = f"echo '{content}' | sudo tee {sddm_conf}"
            subprocess.run(cmd, shell=True, check=False)
        
        # Also configure user's ~/.dmrc
        home = os.path.expanduser("~")
        dmrc = os.path.join(home, ".dmrc")
        try:
            with open(dmrc, "w", encoding="utf-8") as f:
                f.write(f"[Desktop]\nSession={session_name}\n")
        except Exception:
            pass
        return True
    except Exception as e:
        print(f"Error configuring default session: {e}", file=sys.stderr)
        return False

def apply_omarchy_theme(theme_id):
    """Applies an Omarchy theme to Hyprland, Waybar, Rofi, Kitty, and desktop."""
    themes_dir = find_themes_dir()
    if not themes_dir:
        return False, "Themes directory not found"
    
    theme_path = os.path.join(themes_dir, theme_id)
    if not os.path.isdir(theme_path):
        return False, f"Theme '{theme_id}' not found"

    home = os.path.expanduser("~")
    # 1. Hyprland
    hypr_conf_dir = os.path.join(home, ".config", "hypr")
    os.makedirs(hypr_conf_dir, exist_ok=True)
    src_hypr = os.path.join(theme_path, "hyprland.conf")
    if os.path.exists(src_hypr):
        shutil.copy2(src_hypr, os.path.join(hypr_conf_dir, "theme.conf"))
        # Reload hyprland if active
        subprocess.run(["hyprctl", "reload"], capture_output=True, check=False)

    # 2. Waybar
    waybar_dir = os.path.join(home, ".config", "waybar")
    os.makedirs(waybar_dir, exist_ok=True)
    src_waybar = os.path.join(theme_path, "waybar.css")
    if os.path.exists(src_waybar):
        shutil.copy2(src_waybar, os.path.join(waybar_dir, "style.css"))
        subprocess.run(["pkill", "-SIGUSR2", "waybar"], capture_output=True, check=False)

    # 3. Rofi
    rofi_dir = os.path.join(home, ".config", "rofi")
    os.makedirs(rofi_dir, exist_ok=True)
    src_rofi = os.path.join(theme_path, "rofi.rasi")
    if os.path.exists(src_rofi):
        shutil.copy2(src_rofi, os.path.join(rofi_dir, "theme.rasi"))

    # Save active theme record
    try:
        state_file = os.path.join(home, ".config", "rain-os", "active_theme.json")
        os.makedirs(os.path.dirname(state_file), exist_ok=True)
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump({"active_theme": theme_id}, f, indent=2)
    except Exception:
        pass

    return True, f"Theme '{theme_id}' successfully applied across desktop components!"

def set_active_wallpaper(image_path):
    """Sets wallpaper across KDE Plasma, Hyprland, Sway, i3, GNOME, or XFCE."""
    if not os.path.exists(image_path):
        return False, f"File does not exist: {image_path}"
    
    # 1. KDE Plasma
    if shutil.which("plasma-apply-wallpaperimage"):
        subprocess.run(["plasma-apply-wallpaperimage", image_path], check=False)
    
    # 2. Sway / Hyprland (swaybg)
    if shutil.which("swaybg"):
        subprocess.run(["pkill", "swaybg"], check=False)
        subprocess.Popen(["swaybg", "-m", "fill", "-i", image_path])
    
    # 3. Feh (i3 / XFCE fallback)
    if shutil.which("feh"):
        subprocess.run(["feh", "--bg-fill", image_path], check=False)
        
    # 4. GNOME gsettings
    if shutil.which("gsettings"):
        uri = f"file://{os.path.abspath(image_path)}"
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri], check=False)
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", uri], check=False)

    # Copy to default branding location if writable
    try:
        home = os.path.expanduser("~")
        dest = os.path.join(home, ".config", "rain-os", "current-wallpaper.jpg")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(image_path, dest)
    except Exception:
        pass

    return True, f"Wallpaper set to {os.path.basename(image_path)}"


class DesktopSelectorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rain OS Desktop & Window Manager Selector")
        self.geometry("960x700")
        self.minsize(880, 620)
        self.configure(bg=BG_COLOR)

        self.active_de = get_active_desktop()
        self.thumbnails = {}
        self._load_branding()
        self._build_ui()

    def _load_branding(self):
        logo_path = find_asset_path("rain-logo.png") or find_asset_path("rain-logo-4k.png")
        self.tk_logo = None
        if logo_path and os.path.exists(logo_path):
            try:
                img = Image.open(logo_path).resize((40, 40), Image.Resampling.LANCZOS)
                self.tk_logo = ImageTk.PhotoImage(img)
            except Exception:
                pass

    def _build_ui(self):
        # Header bar
        header = tk.Frame(self, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        header.pack(fill="x", padx=20, pady=(15, 10))

        h_content = tk.Frame(header, bg=CARD_BG)
        h_content.pack(fill="x", padx=15, pady=12)

        if self.tk_logo:
            tk.Label(h_content, image=self.tk_logo, bg=CARD_BG).pack(side="left", padx=(0, 12))

        title_box = tk.Frame(h_content, bg=CARD_BG)
        title_box.pack(side="left", fill="both", expand=True)

        tk.Label(
            title_box,
            text="Desktop & Window Manager Selector",
            font=("Segoe UI", 15, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_BG
        ).pack(anchor="w")

        tk.Label(
            title_box,
            text=f"Switch seamlessly between Desktop Environments & Tiling Compositors | Active: {self.active_de.upper()}",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=CARD_BG
        ).pack(anchor="w")

        # Refresh button
        tk.Button(
            h_content,
            text="⟳ Refresh Status",
            command=self._refresh_status,
            bg="#383e4c",
            fg=TEXT_COLOR,
            activebackground="#4a5264",
            activeforeground=TEXT_COLOR,
            relief="flat",
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=6,
            cursor="hand2"
        ).pack(side="right")

        # Dark Notebook Tabs
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
        style.configure("TNotebook.Tab", background="#262b36", foreground=TEXT_COLOR, padding=[16, 8], font=("Segoe UI", 10, "bold"))
        style.map("TNotebook.Tab",
                  background=[("selected", ACCENT_COLOR), ("active", "#3b4354")],
                  foreground=[("selected", "#0a101a"), ("active", TEXT_COLOR)])

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=20, pady=10)

        # Tab 1: Desktops & Window Managers
        tab_desktops = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_desktops, text="  Window Managers & Desktops  ")
        self._build_desktops_tab(tab_desktops)

        # Tab 2: Omarchy Themes Engine
        tab_themes = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_themes, text="  Omarchy Themes (22)  ")
        self._build_themes_tab(tab_themes)

        # Tab 3: 4K Anime Wallpapers Gallery
        tab_wallpapers = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_wallpapers, text="  4K Wallpaper Gallery (12)  ")
        self._build_wallpapers_tab(tab_wallpapers)

    def _build_desktops_tab(self, parent):
        # Scrollable container
        canvas = tk.Canvas(parent, bg=BG_COLOR, highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=BG_COLOR)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=910)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, pady=5)
        scrollbar.pack(side="right", fill="y", pady=5)

        for de in DESKTOPS:
            is_installed = is_desktop_installed(de)
            is_active = (de["id"] == self.active_de)

            card = tk.Frame(scroll_frame, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
            card.pack(fill="x", pady=6, padx=5)

            card_inner = tk.Frame(card, bg=CARD_BG)
            card_inner.pack(fill="x", padx=16, pady=14)

            # Left Details
            left_box = tk.Frame(card_inner, bg=CARD_BG)
            left_box.pack(side="left", fill="both", expand=True)

            # Title Row
            title_row = tk.Frame(left_box, bg=CARD_BG)
            title_row.pack(fill="x")

            tk.Label(
                title_row,
                text=de["name"],
                font=("Segoe UI", 13, "bold"),
                fg=TEXT_COLOR,
                bg=CARD_BG
            ).pack(side="left")

            # Category / Badge
            badge_color = "#3b4354"
            if is_active:
                badge_text = "CURRENTLY ACTIVE"
                badge_color = SUCCESS_COLOR
            elif is_installed:
                badge_text = "INSTALLED"
                badge_color = INFO_COLOR
            else:
                badge_text = "AVAILABLE TO INSTALL"

            badge_lbl = tk.Label(
                title_row,
                text=f" {badge_text} ",
                font=("Segoe UI", 8, "bold"),
                fg="#ffffff",
                bg=badge_color,
                padx=6,
                pady=2
            )
            badge_lbl.pack(side="left", padx=10)

            # Subtitle / Tagline
            tk.Label(
                left_box,
                text=de["tagline"],
                font=("Segoe UI", 9),
                fg=TEXT_MUTED,
                bg=CARD_BG,
                wraplength=600,
                justify="left"
            ).pack(anchor="w", pady=(3, 6))

            # Metadata tags (Compositor, RAM, Category)
            meta_row = tk.Frame(left_box, bg=CARD_BG)
            meta_row.pack(fill="x")

            meta_info = [
                f"🖵 {de['compositor']}",
                f"⚡ Memory: {de['ram']}",
                f"📦 {de['category']}"
            ]
            for m in meta_info:
                tk.Label(
                    meta_row,
                    text=m,
                    font=("Segoe UI", 8),
                    fg="#b0b8c4",
                    bg="#1f232b",
                    padx=8,
                    pady=2
                ).pack(side="left", padx=(0, 6))

            # Right Actions
            right_box = tk.Frame(card_inner, bg=CARD_BG)
            right_box.pack(side="right", padx=(15, 0))

            if is_active:
                btn = tk.Label(
                    right_box,
                    text="✓ Active Session",
                    font=("Segoe UI", 9, "bold"),
                    fg=SUCCESS_COLOR,
                    bg="#1c2c20",
                    padx=14,
                    pady=8
                )
                btn.pack()
            elif is_installed:
                switch_btn = tk.Button(
                    right_box,
                    text="Switch to This WM",
                    font=("Segoe UI", 9, "bold"),
                    bg=INFO_COLOR,
                    fg="#ffffff",
                    activebackground="#216cdb",
                    activeforeground="#ffffff",
                    relief="flat",
                    padx=14,
                    pady=8,
                    cursor="hand2",
                    command=lambda d=de: self._on_switch_desktop(d)
                )
                switch_btn.pack()
            else:
                install_btn = tk.Button(
                    right_box,
                    text="One-Click Install",
                    font=("Segoe UI", 9, "bold"),
                    bg=ACCENT_COLOR,
                    fg="#ffffff",
                    activebackground=ACCENT_HOVER,
                    activeforeground="#ffffff",
                    relief="flat",
                    padx=14,
                    pady=8,
                    cursor="hand2",
                    command=lambda d=de: self._on_install_desktop(d)
                )
                install_btn.pack()

    def _build_themes_tab(self, parent):
        themes_dir = find_themes_dir()
        manifest_path = os.path.join(themes_dir, "themes.json") if themes_dir else None
        themes_data = {}
        if manifest_path and os.path.exists(manifest_path):
            try:
                with open(manifest_path, "r", encoding="utf-8") as f:
                    themes_data = json.load(f)
            except Exception:
                pass

        intro = tk.Label(
            parent,
            text="Signature themes ported from omacom/omarchy. Applying updates Hyprland, Waybar, Rofi, and terminal palettes.",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=BG_COLOR,
            anchor="w"
        )
        intro.pack(fill="x", padx=10, pady=(10, 5))

        # Canvas for themes
        canvas = tk.Canvas(parent, bg=BG_COLOR, highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=BG_COLOR)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=910)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, pady=5)
        scrollbar.pack(side="right", fill="y", pady=5)

        for theme_id, colors in themes_data.items():
            card = tk.Frame(scroll_frame, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
            card.pack(fill="x", pady=5, padx=5)

            c_inner = tk.Frame(card, bg=CARD_BG)
            c_inner.pack(fill="x", padx=15, pady=10)

            # Left theme title
            left_info = tk.Frame(c_inner, bg=CARD_BG)
            left_info.pack(side="left", fill="both", expand=True)

            tk.Label(
                left_info,
                text=colors.get("name", theme_id),
                font=("Segoe UI", 11, "bold"),
                fg=TEXT_COLOR,
                bg=CARD_BG
            ).pack(anchor="w")

            tk.Label(
                left_info,
                text=f"Theme ID: {theme_id} | Accent: {colors.get('accent')} | BG: {colors.get('bg')}",
                font=("Segoe UI", 8),
                fg=TEXT_MUTED,
                bg=CARD_BG
            ).pack(anchor="w", pady=(2, 6))

            # Swatches Row
            swatch_frame = tk.Frame(left_info, bg=CARD_BG)
            swatch_frame.pack(anchor="w")

            for label, color_code in [
                ("BG", colors.get("bg", "#000000")),
                ("Card", colors.get("card", "#111111")),
                ("Primary", colors.get("primary", "#ffffff")),
                ("Accent", colors.get("accent", "#e83e38")),
                ("Border", colors.get("active_border", "#e83e38"))
            ]:
                s_box = tk.Frame(swatch_frame, bg=CARD_BG)
                s_box.pack(side="left", padx=(0, 10))
                tk.Frame(s_box, bg=color_code, width=24, height=16, highlightbackground="#ffffff", highlightthickness=1).pack()
                tk.Label(s_box, text=label, font=("Segoe UI", 7), fg=TEXT_MUTED, bg=CARD_BG).pack()

            # Right Apply Button
            apply_btn = tk.Button(
                c_inner,
                text="Apply Theme",
                font=("Segoe UI", 9, "bold"),
                bg=ACCENT_COLOR,
                fg="#ffffff",
                activebackground=ACCENT_HOVER,
                activeforeground="#ffffff",
                relief="flat",
                padx=12,
                pady=6,
                cursor="hand2",
                command=lambda tid=theme_id: self._on_apply_theme(tid)
            )
            apply_btn.pack(side="right", padx=(10, 0))

    def _build_wallpapers_tab(self, parent):
        wp_dir = find_wallpaper_dir()
        wallpapers = []
        meta_by_name = {}
        if wp_dir and os.path.isdir(wp_dir):
            wallpapers = sorted(glob.glob(os.path.join(wp_dir, "rain-wallpaper-*.jpg")))
            manifest_path = os.path.join(wp_dir, "wallpapers.json")
            if os.path.exists(manifest_path):
                try:
                    with open(manifest_path, "r", encoding="utf-8") as f:
                        for entry in json.load(f):
                            meta_by_name[entry.get("filename")] = entry
                except Exception:
                    pass

        intro = tk.Label(
            parent,
            text=f"12 Pristine 4K UHD Anime Rain Wallpapers (3840×2160). Select any wallpaper to set as your desktop background.",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=BG_COLOR,
            anchor="w"
        )
        intro.pack(fill="x", padx=10, pady=(10, 5))

        # Canvas for wallpapers
        canvas = tk.Canvas(parent, bg=BG_COLOR, highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=BG_COLOR)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=910)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, pady=5)
        scrollbar.pack(side="right", fill="y", pady=5)

        # 4 columns grid
        row = 0
        col = 0
        for i, wp in enumerate(wallpapers):
            fname = os.path.basename(wp)
            meta = meta_by_name.get(fname, {})
            title = meta.get("title", f"Wallpaper #{i+1:02d}")

            w_card = tk.Frame(scroll_frame, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
            w_card.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

            # Load thumbnail
            try:
                pil_img = Image.open(wp).resize((200, 112), Image.Resampling.LANCZOS)
                tk_img = ImageTk.PhotoImage(pil_img)
                self.thumbnails[wp] = tk_img
                img_lbl = tk.Label(w_card, image=tk_img, bg=CARD_BG)
                img_lbl.pack(padx=6, pady=(6, 4))
            except Exception:
                pass

            title_lbl = tk.Label(
                w_card,
                text=title,
                font=("Segoe UI", 8, "bold"),
                fg=TEXT_COLOR,
                bg=CARD_BG
            )
            title_lbl.pack(anchor="w", padx=8)

            btn = tk.Button(
                w_card,
                text="Set Wallpaper",
                font=("Segoe UI", 8, "bold"),
                bg=ACCENT_COLOR,
                fg="#ffffff",
                activebackground=ACCENT_HOVER,
                activeforeground="#ffffff",
                relief="flat",
                pady=3,
                cursor="hand2",
                command=lambda p=wp: self._on_set_wallpaper(p)
            )
            btn.pack(fill="x", padx=6, pady=(4, 6))

            col += 1
            if col >= 4:
                col = 0
                row += 1

    def _on_switch_desktop(self, de):
        confirm = messagebox.askyesno(
            "Switch Default Desktop Session",
            f"Set {de['name']} as your default desktop session?\n\n"
            f"Next time you login or restart SDDM, {de['name']} will launch automatically."
        )
        if confirm:
            ok = switch_default_session(de["session_name"])
            if ok:
                messagebox.showinfo(
                    "Session Configured",
                    f"{de['name']} is now configured as your default session!\n\n"
                    "Log out of your current session to enter the new desktop."
                )
            else:
                messagebox.showerror("Configuration Error", "Could not configure display manager session.")

    def _on_install_desktop(self, de):
        pkgs_str = " ".join(de["packages"])
        confirm = messagebox.askyesno(
            f"Install {de['name']}",
            f"Do you want to install {de['name']} via pacman?\n\n"
            f"Packages to install:\n{pkgs_str}\n\n"
            "This will require root/sudo authentication."
        )
        if not confirm:
            return

        # Terminal launcher or background install
        cmd = f"sudo pacman -S --noconfirm {pkgs_str}"
        if shutil.which("konsole"):
            subprocess.Popen(["konsole", "-e", "bash", "-c", f"{cmd}; echo 'Installation finished. Press enter.'; read"])
        elif shutil.which("kitty"):
            subprocess.Popen(["kitty", "bash", "-c", f"{cmd}; echo 'Installation finished. Press enter.'; read"])
        elif shutil.which("xterm"):
            subprocess.Popen(["xterm", "-e", f"{cmd}"])
        else:
            threading.Thread(target=lambda: subprocess.run(cmd, shell=True), daemon=True).start()
            messagebox.showinfo("Installation Started", f"Installing {de['name']} in background.")

    def _on_apply_theme(self, theme_id):
        ok, msg = apply_omarchy_theme(theme_id)
        if ok:
            messagebox.showinfo("Omarchy Theme Applied", msg)
        else:
            messagebox.showerror("Theme Error", msg)

    def _on_set_wallpaper(self, image_path):
        ok, msg = set_active_wallpaper(image_path)
        if ok:
            messagebox.showinfo("Wallpaper Set", msg)
        else:
            messagebox.showerror("Wallpaper Error", msg)

    def _refresh_status(self):
        self.destroy()
        app = DesktopSelectorGUI()
        app.mainloop()


def main():
    parser = argparse.ArgumentParser(description="Rain OS Desktop Environment & Window Manager Selector")
    parser.add_argument("--list", action="store_true", help="List all available desktop environments and status")
    parser.add_argument("--switch", type=str, metavar="WM_ID", help="Switch default session to specified WM (plasma, hyprland, gnome, i3, cosmic, sway, xfce)")
    parser.add_argument("--theme", type=str, metavar="THEME_ID", help="Apply Omarchy theme (tokyo-night, matte-black, etc.)")
    parser.add_argument("--wallpaper", type=str, metavar="NUM_OR_PATH", help="Set wallpaper by number (e.g. 1) or image file path")
    parser.add_argument("--install", type=str, metavar="WM_ID", help="Install specified desktop environment")
    parser.add_argument("--current", action="store_true", help="Print active session name")
    parser.add_argument("--gui", action="store_true", help="Force graphical interface")

    args = parser.parse_args()

    if args.list:
        print(f"{'ID':<12} {'NAME':<20} {'STATUS':<15} {'COMPOSITOR':<25} {'RAM':<10}")
        print("-" * 82)
        active = get_active_desktop()
        for d in DESKTOPS:
            inst = is_desktop_installed(d)
            status = "ACTIVE" if d["id"] == active else ("INSTALLED" if inst else "AVAILABLE")
            print(f"{d['id']:<12} {d['name']:<20} {status:<15} {d['compositor']:<25} {d['ram']:<10}")
        sys.exit(0)

    if args.current:
        print(get_active_desktop())
        sys.exit(0)

    if args.switch:
        target = args.switch.lower()
        match = next((d for d in DESKTOPS if d["id"] == target), None)
        if not match:
            print(f"Error: Unknown desktop '{target}'. Run --list to view options.", file=sys.stderr)
            sys.exit(1)
        ok = switch_default_session(match["session_name"])
        if ok:
            print(f"Default session successfully switched to {match['name']} ({match['session_name']}).")
        else:
            print(f"Failed to switch session.", file=sys.stderr)
            sys.exit(1)
        sys.exit(0)

    if args.theme:
        ok, msg = apply_omarchy_theme(args.theme)
        print(msg)
        sys.exit(0 if ok else 1)

    if args.wallpaper:
        wp = args.wallpaper
        if wp.isdigit():
            num = int(wp)
            wp_dir = find_wallpaper_dir()
            fname = f"rain-wallpaper-{num:02d}.jpg"
            wp = os.path.join(wp_dir, fname) if wp_dir else fname
        ok, msg = set_active_wallpaper(wp)
        print(msg)
        sys.exit(0 if ok else 1)

    if args.install:
        target = args.install.lower()
        match = next((d for d in DESKTOPS if d["id"] == target), None)
        if not match:
            print(f"Error: Unknown desktop '{target}'.", file=sys.stderr)
            sys.exit(1)
        pkgs = " ".join(match["packages"])
        print(f"Installing {match['name']} ({pkgs})...")
        res = subprocess.run(f"sudo pacman -S --noconfirm {pkgs}", shell=True)
        sys.exit(res.returncode)

    # Launch GUI
    app = DesktopSelectorGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
