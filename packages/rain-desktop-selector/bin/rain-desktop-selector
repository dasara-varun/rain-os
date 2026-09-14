#!/usr/bin/env python3
"""
Rain OS Desktop Environment & Window Manager Selector
Unified GUI & CLI utility to choose, install, configure, and switch between:
  1. COSMIC Desktop (Flagship Default - Rust-based Modern Desktop)
  2. Hyprland (Dynamic Wayland Tiling Compositor & Omarchy Theming)
  3. KDE Plasma 6 (Customizable Glass Desktop Environment)
  4. GNOME Shell (Gesture-Driven Focused Shell)
  5. i3-wm (Ultra-Lightweight Keyboard Tiling WM)
  6. Sway (i3-Compatible Wayland Compositor)
  7. XFCE 4 (Classic Lightweight Modular Desktop)
  8. Niri (Scrollable-Tiling Infinite Ribbon Compositor)
  9. River WM (Dynamic Tiling Wayland Compositor)
  10. Gamescope + MangoHUD (SteamOS-Style Micro-Compositor Gaming Session)

Features:
  - --install-mode: Vertical single-column selection integrated into system installer
  - Omarchy Theme Engine: 22 signature themes
  - 4K Anime Rain Wallpaper Gallery: 12 pristine ultra-high-resolution wallpapers
  - Multi-terminal auto-detection
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

BG_COLOR = "#1e222b"
CARD_BG = "#282d37"
CARD_SELECTED = "#343d4e"
CARD_HOVER = "#323846"
TEXT_COLOR = "#f0f6fc"
TEXT_MUTED = "#9ba3af"
ACCENT_COLOR = "#e83e38"
ACCENT_HOVER = "#ff5751"
BORDER_COLOR = "#383e4c"
BORDER_ACTIVE = "#e83e38"
SUCCESS_COLOR = "#2ea043"
INFO_COLOR = "#388bfd"

DESKTOPS = [
    {
        "id": "cosmic",
        "name": "COSMIC Desktop",
        "category": "Modern Rust Desktop Environment",
        "tagline": "Rain OS Flagship Default. Written in Rust by System76. Modular, Wayland-native, high-performance.",
        "compositor": "cosmic-comp (Wayland)",
        "ram": "~380 MB",
        "app_store": "cosmic-store",
        "binary": "cosmic-session",
        "fallback_bin": "cosmic-comp",
        "session_name": "cosmic",
        "session_file": "cosmic.desktop",
        "packages": ["cosmic-session", "cosmic-store", "cosmic-terminal", "cosmic-files", "cosmic-settings"],
        "badge": "FLAGSHIP DEFAULT",
        "icon": "🚀",
        "recommended": True
    },
    {
        "id": "hyprland",
        "name": "Hyprland",
        "category": "Dynamic Wayland Tiling Compositor",
        "tagline": "Fluid animations, rounded corners, dual borders, blur, and deep Omarchy theming integration.",
        "compositor": "Hyprland (Wayland)",
        "ram": "~220 MB",
        "app_store": "cosmic-store / Flatpak",
        "binary": "Hyprland",
        "fallback_bin": "hyprland",
        "session_name": "hyprland",
        "session_file": "hyprland.desktop",
        "packages": ["hyprland", "waybar", "rofi", "swaybg", "dunst", "kitty"],
        "badge": "OMARCHY TILING",
        "icon": "⚡",
        "recommended": False
    },
    {
        "id": "plasma",
        "name": "KDE Plasma 6",
        "category": "Full Desktop Environment",
        "tagline": "Fully customizable desktop with translucent glass UI, flexible panels, and rich widget ecosystem.",
        "compositor": "KWin (Wayland / X11)",
        "ram": "~450 MB",
        "app_store": "cosmic-store / Discover",
        "binary": "startplasma-wayland",
        "fallback_bin": "startplasma-x11",
        "session_name": "plasma",
        "session_file": "plasma.desktop",
        "packages": ["plasma-desktop", "plasma-workspace", "plasma-nm", "dolphin", "konsole", "sddm"],
        "badge": "CUSTOMIZABLE DE",
        "icon": "🪟",
        "recommended": False
    },
    {
        "id": "gnome",
        "name": "GNOME Shell",
        "category": "Full Desktop Environment",
        "tagline": "Distraction-free, gesture-driven desktop shell designed for focused, keyboard-centric productivity.",
        "compositor": "Mutter (Wayland)",
        "ram": "~550 MB",
        "app_store": "cosmic-store / gnome-software",
        "binary": "gnome-shell",
        "fallback_bin": "gnome-session",
        "session_name": "gnome",
        "session_file": "gnome.desktop",
        "packages": ["gnome-shell", "gnome-control-center", "nautilus"],
        "badge": "GESTURE DRIVEN",
        "icon": "🎯",
        "recommended": False
    },
    {
        "id": "i3",
        "name": "i3-wm (Tiling)",
        "category": "Manual Tiling Window Manager",
        "tagline": "Ultra-lightweight keyboard-driven X11 tiling window manager. Instant response on any hardware.",
        "compositor": "X11 (Picom Compositor)",
        "ram": "~120 MB",
        "app_store": "pacman / Flatpak",
        "binary": "i3",
        "fallback_bin": "i3-wm",
        "session_name": "i3",
        "session_file": "i3.desktop",
        "packages": ["i3-wm", "i3status", "picom", "rofi", "kitty"],
        "badge": "ULTRA LIGHTWEIGHT",
        "icon": "⌨️",
        "recommended": False
    },
    {
        "id": "sway",
        "name": "Sway",
        "category": "i3-Compatible Wayland Compositor",
        "tagline": "Drop-in replacement for i3 on Wayland with zero tearing and smooth wlroots hardware acceleration.",
        "compositor": "wlroots (Wayland)",
        "ram": "~160 MB",
        "app_store": "cosmic-store / Flatpak",
        "binary": "sway",
        "fallback_bin": "sway",
        "session_name": "sway",
        "session_file": "sway.desktop",
        "packages": ["sway", "waybar", "rofi", "swaybg"],
        "badge": "WAYLAND TILING",
        "icon": "🌊",
        "recommended": False
    },
    {
        "id": "xfce",
        "name": "XFCE 4",
        "category": "Lightweight Desktop Environment",
        "tagline": "Classic, modular, battle-tested desktop for older hardware and minimal resource consumption.",
        "compositor": "Xfwm4 (X11)",
        "ram": "~200 MB",
        "app_store": "cosmic-store / Flatpak",
        "binary": "xfce4-session",
        "fallback_bin": "startxfce4",
        "session_name": "xfce",
        "session_file": "xfce.desktop",
        "packages": ["xfce4-session", "xfdesktop", "xfwm4", "xfce4-panel"],
        "badge": "CLASSIC MODULAR",
        "icon": "🍃",
        "recommended": False
    },
    {
        "id": "niri",
        "name": "Niri (Scrollable)",
        "category": "Scrollable-Tiling Wayland Compositor",
        "tagline": "Infinite horizontal ribbon of windows. Fluid animations and intuitive touchpad gestures.",
        "compositor": "Niri (Wayland)",
        "ram": "~180 MB",
        "app_store": "cosmic-store / Flatpak",
        "binary": "niri",
        "fallback_bin": "niri-session",
        "session_name": "niri",
        "session_file": "niri.desktop",
        "packages": ["niri", "waybar", "rofi", "swaybg", "alacritty"],
        "badge": "SCROLLABLE RIBBON",
        "icon": "📜",
        "recommended": False
    },
    {
        "id": "river",
        "name": "River WM",
        "category": "Dynamic Tiling Wayland Compositor",
        "tagline": "Flexible, dynamic tiling Wayland compositor with rich tag-based workspace management.",
        "compositor": "River (Wayland)",
        "ram": "~140 MB",
        "app_store": "cosmic-store / Flatpak",
        "binary": "river",
        "fallback_bin": "river",
        "session_name": "river",
        "session_file": "river.desktop",
        "packages": ["river", "waybar", "rofi", "swaybg", "alacritty"],
        "badge": "DYNAMIC TILING",
        "icon": "🌊",
        "recommended": False
    },
    {
        "id": "gamescope",
        "name": "Gamescope + MangoHUD",
        "category": "Gaming Micro-Compositor Session",
        "tagline": "Optimized SteamOS-style dedicated gaming session with MangoHUD telemetry and integer scaling.",
        "compositor": "Gamescope (Wayland/Xwayland)",
        "ram": "~150 MB",
        "app_store": "Steam / Flatpak",
        "binary": "gamescope",
        "fallback_bin": "mangoapp",
        "session_name": "gamescope",
        "session_file": "gamescope-wayland.desktop",
        "packages": ["gamescope", "mangohud"],
        "badge": "GAMING EDITION",
        "icon": "🎮",
        "recommended": False
    }
]

def find_asset_path(subpath):
    candidates = [
        os.path.join("/usr/share/icons/hicolor/128x128/apps", subpath),
        os.path.join("/usr/share/pixmaps", subpath),
        os.path.join("/usr/share/rain-os", subpath),
        os.path.join(os.path.dirname(__file__), "..", "..", "branding", "icons", "128x128", subpath),
        os.path.join(os.path.dirname(__file__), "..", "..", "branding", subpath),
        os.path.join(r"E:\rain os\branding\icons\128x128", subpath),
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
    if "cosmic" in comb:
        return "cosmic"
    if "hyprland" in comb:
        return "hyprland"
    if "plasma" in comb or "kde" in comb:
        return "plasma"
    if "gnome" in comb:
        return "gnome"
    if "i3" in comb:
        return "i3"
    if "sway" in comb:
        return "sway"
    if "xfce" in comb:
        return "xfce"
    try:
        procs = subprocess.check_output(["ps", "-A"], text=True)
        if "cosmic-comp" in procs or "cosmic-session" in procs: return "cosmic"
        if "Hyprland" in procs: return "hyprland"
        if "kwin" in procs: return "plasma"
        if "gnome-shell" in procs: return "gnome"
        if "i3" in procs: return "i3"
        if "sway" in procs: return "sway"
        if "xfce4-session" in procs: return "xfce"
    except Exception:
        pass
    return "cosmic"

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

def save_installation_choice(desktop_id):
    """Saves the user's desktop choice for the installer."""
    de = next((d for d in DESKTOPS if d["id"] == desktop_id), None)
    if not de:
        return False
    
    try:
        with open("/tmp/rain-install-desktop", "w", encoding="utf-8") as f:
            f.write(desktop_id)
    except Exception:
        pass
    
    try:
        os.makedirs("/etc/rain-os", exist_ok=True)
        conf_path = "/etc/rain-os/install-desktop.conf"
        content = (
            f"[Installation]\n"
            f"DesktopId={de['id']}\n"
            f"DesktopName={de['name']}\n"
            f"SessionFile={de['session_file']}\n"
            f"Compositor={de['compositor']}\n"
            f"Packages={' '.join(de['packages'])}\n"
        )
        try:
            with open(conf_path, "w", encoding="utf-8") as f:
                f.write(content)
        except PermissionError:
            subprocess.run(f"echo '{content}' | sudo tee {conf_path}", shell=True, check=False)
    except Exception:
        pass
    
    switch_default_session(de["session_name"])
    return True

def apply_omarchy_theme(theme_id):
    """Applies an Omarchy theme to Hyprland, Waybar, Rofi, Kitty, and desktop."""
    themes_dir = find_themes_dir()
    if not themes_dir:
        return False, "Themes directory not found"
    
    theme_path = os.path.join(themes_dir, theme_id)
    if not os.path.isdir(theme_path):
        return False, f"Theme '{theme_id}' not found"

    home = os.path.expanduser("~")
    hypr_conf_dir = os.path.join(home, ".config", "hypr")
    os.makedirs(hypr_conf_dir, exist_ok=True)
    src_hypr = os.path.join(theme_path, "hyprland.conf")
    if os.path.exists(src_hypr):
        shutil.copy2(src_hypr, os.path.join(hypr_conf_dir, "theme.conf"))
        subprocess.run(["hyprctl", "reload"], capture_output=True, check=False)

    waybar_dir = os.path.join(home, ".config", "waybar")
    os.makedirs(waybar_dir, exist_ok=True)
    src_waybar = os.path.join(theme_path, "waybar.css")
    if os.path.exists(src_waybar):
        shutil.copy2(src_waybar, os.path.join(waybar_dir, "style.css"))
        subprocess.run(["pkill", "-SIGUSR2", "waybar"], capture_output=True, check=False)

    rofi_dir = os.path.join(home, ".config", "rofi")
    os.makedirs(rofi_dir, exist_ok=True)
    src_rofi = os.path.join(theme_path, "rofi.rasi")
    if os.path.exists(src_rofi):
        shutil.copy2(src_rofi, os.path.join(rofi_dir, "theme.rasi"))

    try:
        state_file = os.path.join(home, ".config", "rain-os", "active_theme.json")
        os.makedirs(os.path.dirname(state_file), exist_ok=True)
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump({"active_theme": theme_id}, f, indent=2)
    except Exception:
        pass

    return True, f"Theme '{theme_id}' successfully applied across desktop components!"

def set_active_wallpaper(image_path):
    """Sets wallpaper across COSMIC, KDE Plasma, Hyprland, Sway, i3, GNOME, or XFCE."""
    if not os.path.exists(image_path):
        return False, f"File does not exist: {image_path}"
    
    home = os.path.expanduser("~")
    cosmic_bg_file = os.path.join(home, ".config", "cosmic", "com.system76.CosmicBackground", "v1", "all")
    try:
        os.makedirs(os.path.dirname(cosmic_bg_file), exist_ok=True)
        with open(cosmic_bg_file, "w", encoding="utf-8") as f:
            f.write(f'(output: "all", source: Path("{os.path.abspath(image_path)}"), filter_by_theme: false, rotation_frequency: 0, filter_method: Lanczos)')
    except Exception:
        pass

    if shutil.which("plasma-apply-wallpaperimage"):
        subprocess.run(["plasma-apply-wallpaperimage", image_path], check=False)
    
    if shutil.which("swaybg"):
        subprocess.run(["pkill", "swaybg"], check=False)
        subprocess.Popen(["swaybg", "-m", "fill", "-i", image_path])
    
    if shutil.which("feh"):
        subprocess.run(["feh", "--bg-fill", image_path], check=False)
        
    if shutil.which("gsettings"):
        uri = f"file://{os.path.abspath(image_path)}"
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri], check=False)
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", uri], check=False)

    try:
        dest = os.path.join(home, ".config", "rain-os", "current-wallpaper.jpg")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(image_path, dest)
    except Exception:
        pass

    return True, f"Wallpaper set to {os.path.basename(image_path)}"

def run_in_terminal(cmd_str, title="Rain OS"):
    """Helper to run a shell command in any available terminal emulator."""
    terminals = [
        (["cosmic-terminal", "-e", "bash", "-c", f"{cmd_str}; echo 'Finished. Press Enter.'; read"], "cosmic-terminal"),
        (["alacritty", "-e", "bash", "-c", f"{cmd_str}; echo 'Finished. Press Enter.'; read"], "alacritty"),
        (["konsole", "--new-window", "-e", "bash", "-c", f"{cmd_str}; echo 'Finished. Press Enter.'; read"], "konsole"),
        (["kitty", "bash", "-c", f"{cmd_str}; echo 'Finished. Press Enter.'; read"], "kitty"),
        (["xterm", "-title", title, "-e", "bash", "-c", f"{cmd_str}; echo 'Finished. Press Enter.'; read"], "xterm")
    ]
    for cmd, bin_name in terminals:
        if shutil.which(bin_name):
            subprocess.Popen(cmd)
            return True
    threading.Thread(target=lambda: subprocess.run(cmd_str, shell=True), daemon=True).start()
    return False

class InstallationDesktopSelectorGUI(tk.Tk):
    """
    Dedicated Installation Window Manager / Desktop Selector.
    Renders a clean, single-column vertical list of Desktop Environments.
    """
    def __init__(self):
        super().__init__()
        self.title("Rain OS System Installation — Select Desktop Environment")
        self.geometry("920x720")
        self.minsize(860, 640)
        self.configure(bg=BG_COLOR)

        self.selected_id = tk.StringVar(value="cosmic")
        self.card_frames = {}
        self.radio_widgets = {}

        self._load_branding()
        self._build_ui()

    def _load_branding(self):
        logo_path = (find_asset_path("rain-installer.png") or
                     find_asset_path("rain-desktop-selector.png") or
                     find_asset_path("rain-logo.png"))
        self.tk_logo = None
        if logo_path and os.path.exists(logo_path):
            try:
                img = Image.open(logo_path).resize((48, 48), Image.Resampling.LANCZOS)
                self.tk_logo = ImageTk.PhotoImage(img)
            except Exception:
                pass

    def _build_ui(self):
        header = tk.Frame(self, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        header.pack(fill="x", padx=20, pady=(15, 10))

        h_content = tk.Frame(header, bg=CARD_BG)
        h_content.pack(fill="x", padx=18, pady=14)

        if self.tk_logo:
            tk.Label(h_content, image=self.tk_logo, bg=CARD_BG).pack(side="left", padx=(0, 15))

        title_box = tk.Frame(h_content, bg=CARD_BG)
        title_box.pack(side="left", fill="both", expand=True)

        tk.Label(
            title_box,
            text="Choose Desktop Environment for Installation",
            font=("Segoe UI", 16, "bold"),
            fg=TEXT_COLOR,
            bg=CARD_BG
        ).pack(anchor="w")

        tk.Label(
            title_box,
            text="Displayed in vertical priority order. COSMIC Desktop is the flagship default. Select your target environment below.",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=CARD_BG
        ).pack(anchor="w", pady=(2, 0))

        body_frame = tk.Frame(self, bg=BG_COLOR)
        body_frame.pack(fill="both", expand=True, padx=20, pady=5)

        canvas = tk.Canvas(body_frame, bg=BG_COLOR, highlightthickness=0)
        scrollbar = tk.Scrollbar(body_frame, orient="vertical", command=canvas.yview)
        self.scroll_frame = tk.Frame(canvas, bg=BG_COLOR)

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas_window = canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw", width=870)
        canvas.configure(yscrollcommand=scrollbar.set)

        def _on_canvas_resize(event):
            canvas.itemconfig(canvas_window, width=event.width)
        canvas.bind("<Configure>", _on_canvas_resize)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for idx, de in enumerate(DESKTOPS):
            self._create_vertical_card(self.scroll_frame, de, idx)

        footer = tk.Frame(self, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
        footer.pack(fill="x", padx=20, pady=(10, 15))

        f_content = tk.Frame(footer, bg=CARD_BG)
        f_content.pack(fill="x", padx=18, pady=12)

        self.status_label = tk.Label(
            f_content,
            text="Selected: COSMIC Desktop (Rust Flagship Default)",
            font=("Segoe UI", 10, "bold"),
            fg=SUCCESS_COLOR,
            bg=CARD_BG
        )
        self.status_label.pack(side="left")

        btn_box = tk.Frame(f_content, bg=CARD_BG)
        btn_box.pack(side="right")

        cancel_btn = tk.Button(
            btn_box,
            text="Cancel",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg="#20252e",
            activebackground="#2c3340",
            activeforeground=TEXT_COLOR,
            relief="flat",
            padx=14,
            pady=7,
            cursor="hand2",
            command=self._on_cancel
        )
        cancel_btn.pack(side="left", padx=(0, 10))

        continue_btn = tk.Button(
            btn_box,
            text="Continue to Disk Partitioning & Installation ➜",
            font=("Segoe UI", 10, "bold"),
            fg="#ffffff",
            bg=ACCENT_COLOR,
            activebackground=ACCENT_HOVER,
            activeforeground="#ffffff",
            relief="flat",
            padx=18,
            pady=7,
            cursor="hand2",
            command=self._on_continue
        )
        continue_btn.pack(side="left")

        self._update_selection_highlight("cosmic")

    def _create_vertical_card(self, parent, de, index):
        de_id = de["id"]
        is_default = (de_id == "cosmic")

        card = tk.Frame(
            parent,
            bg=CARD_SELECTED if is_default else CARD_BG,
            highlightbackground=BORDER_ACTIVE if is_default else BORDER_COLOR,
            highlightthickness=2 if is_default else 1,
            cursor="hand2"
        )
        card.pack(fill="x", pady=5, padx=2)
        self.card_frames[de_id] = card

        inner = tk.Frame(card, bg=card.cget("bg"))
        inner.pack(fill="x", padx=16, pady=12)

        left_col = tk.Frame(inner, bg=card.cget("bg"))
        left_col.pack(side="left", padx=(0, 14))

        rb = tk.Radiobutton(
            left_col,
            variable=self.selected_id,
            value=de_id,
            bg=card.cget("bg"),
            activebackground=card.cget("bg"),
            selectcolor="#0f141c",
            command=lambda: self._on_card_click(de_id)
        )
        rb.pack(side="left")
        self.radio_widgets[de_id] = rb

        icon_lbl = tk.Label(
            left_col,
            text=de.get("icon", "📦"),
            font=("Segoe UI Emoji", 20),
            bg=card.cget("bg"),
            fg=TEXT_COLOR
        )
        icon_lbl.pack(side="left", padx=(4, 0))

        mid_col = tk.Frame(inner, bg=card.cget("bg"))
        mid_col.pack(side="left", fill="both", expand=True)

        title_row = tk.Frame(mid_col, bg=card.cget("bg"))
        title_row.pack(fill="x")

        tk.Label(
            title_row,
            text=f"{index+1}. {de['name']}",
            font=("Segoe UI", 12, "bold"),
            fg=TEXT_COLOR,
            bg=card.cget("bg")
        ).pack(side="left")

        badge_bg = ACCENT_COLOR if is_default else "#394254"
        badge_lbl = tk.Label(
            title_row,
            text=f" {de['badge']} ",
            font=("Segoe UI", 8, "bold"),
            fg="#ffffff",
            bg=badge_bg,
            padx=6,
            pady=1
        )
        badge_lbl.pack(side="left", padx=10)

        tk.Label(
            mid_col,
            text=de["tagline"],
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=card.cget("bg"),
            wraplength=580,
            justify="left"
        ).pack(anchor="w", pady=(2, 5))

        meta_row = tk.Frame(mid_col, bg=card.cget("bg"))
        meta_row.pack(fill="x")

        for pill in [
            f"🖵 {de['compositor']}",
            f"⚡ RAM: {de['ram']}",
            f"🛍️ Store: {de.get('app_store', 'cosmic-store')}"
        ]:
            tk.Label(
                meta_row,
                text=pill,
                font=("Segoe UI", 8),
                fg="#b4bcc8",
                bg="#1a1e26",
                padx=7,
                pady=2
            ).pack(side="left", padx=(0, 6))

        for widget in [card, inner, left_col, mid_col, title_row, meta_row, icon_lbl]:
            widget.bind("<Button-1>", lambda e, did=de_id: self._on_card_click(did))

    def _on_card_click(self, de_id):
        self.selected_id.set(de_id)
        self._update_selection_highlight(de_id)

    def _update_selection_highlight(self, selected_id):
        de = next((d for d in DESKTOPS if d["id"] == selected_id), DESKTOPS[0])
        self.status_label.config(text=f"Selected: {de['name']} ({de['badge']})")

        for did, c_frame in self.card_frames.items():
            is_cur = (did == selected_id)
            new_bg = CARD_SELECTED if is_cur else CARD_BG
            new_border = BORDER_ACTIVE if is_cur else BORDER_COLOR
            new_thick = 2 if is_cur else 1

            c_frame.config(bg=new_bg, highlightbackground=new_border, highlightthickness=new_thick)
            for child in c_frame.winfo_children():
                try:
                    child.config(bg=new_bg)
                    for subchild in child.winfo_children():
                        try:
                            subchild.config(bg=new_bg)
                            for ssub in subchild.winfo_children():
                                try:
                                    if not isinstance(ssub, tk.Button) and not str(ssub.cget("text")).startswith("🖵") and not str(ssub.cget("text")).startswith("⚡") and not str(ssub.cget("text")).startswith("🛍️"):
                                        ssub.config(bg=new_bg)
                                except Exception:
                                    pass
                        except Exception:
                            pass
                except Exception:
                    pass

    def _on_continue(self):
        chosen = self.selected_id.get()
        save_installation_choice(chosen)
        self.destroy()
        sys.exit(0)

    def _on_cancel(self):
        self.destroy()
        sys.exit(1)


class DesktopSelectorGUI(tk.Tk):
    """Standard Window Manager, Theme & Wallpaper Switcher."""
    def __init__(self):
        super().__init__()
        self.title("Rain OS Desktop & Window Manager Selector")
        self.geometry("960x720")
        self.minsize(880, 640)
        self.configure(bg=BG_COLOR)

        self.active_de = get_active_desktop()
        self.thumbnails = {}
        self._load_branding()
        self._build_ui()

    def _load_branding(self):
        logo_path = (find_asset_path("rain-desktop-selector.png") or
                     find_asset_path("rain-logo.png") or
                     find_asset_path("rain-logo-4k.png"))
        self.tk_logo = None
        if logo_path and os.path.exists(logo_path):
            try:
                img = Image.open(logo_path).resize((40, 40), Image.Resampling.LANCZOS)
                self.tk_logo = ImageTk.PhotoImage(img)
            except Exception:
                pass

    def _build_ui(self):
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

        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
        style.configure("TNotebook.Tab", background="#262b36", foreground=TEXT_COLOR, padding=[16, 8], font=("Segoe UI", 10, "bold"))
        style.map("TNotebook.Tab",
                  background=[("selected", ACCENT_COLOR), ("active", "#3b4354")],
                  foreground=[("selected", "#0a101a"), ("active", TEXT_COLOR)])

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=20, pady=10)

        tab_desktops = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_desktops, text="  Window Managers & Desktops  ")
        self._build_desktops_tab(tab_desktops)

        tab_themes = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_themes, text="  Omarchy Themes (22)  ")
        self._build_themes_tab(tab_themes)

        tab_wallpapers = tk.Frame(notebook, bg=BG_COLOR)
        notebook.add(tab_wallpapers, text="  4K Wallpaper Gallery (12)  ")
        self._build_wallpapers_tab(tab_wallpapers)

    def _build_desktops_tab(self, parent):
        canvas = tk.Canvas(parent, bg=BG_COLOR, highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=BG_COLOR)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas_win = canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=910)
        canvas.configure(yscrollcommand=scrollbar.set)

        def _on_c_resize(e):
            canvas.itemconfig(canvas_win, width=e.width)
        canvas.bind("<Configure>", _on_c_resize)

        def _on_wheel(e):
            canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_wheel)

        canvas.pack(side="left", fill="both", expand=True, pady=5)
        scrollbar.pack(side="right", fill="y", pady=5)

        for de in DESKTOPS:
            is_installed = is_desktop_installed(de)
            is_active = (de["id"] == self.active_de)

            card = tk.Frame(scroll_frame, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
            card.pack(fill="x", pady=6, padx=5)

            card_inner = tk.Frame(card, bg=CARD_BG)
            card_inner.pack(fill="x", padx=16, pady=14)

            left_box = tk.Frame(card_inner, bg=CARD_BG)
            left_box.pack(side="left", fill="both", expand=True)

            title_row = tk.Frame(left_box, bg=CARD_BG)
            title_row.pack(fill="x")

            tk.Label(
                title_row,
                text=f"{de.get('icon', '📦')}  {de['name']}",
                font=("Segoe UI", 13, "bold"),
                fg=TEXT_COLOR,
                bg=CARD_BG
            ).pack(side="left")

            if is_active:
                badge_text = "CURRENTLY ACTIVE"
                badge_color = SUCCESS_COLOR
            elif is_installed:
                badge_text = "INSTALLED"
                badge_color = INFO_COLOR
            else:
                badge_text = f"AVAILABLE ({de['badge']})"
                badge_color = "#3b4354"

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

            tk.Label(
                left_box,
                text=de["tagline"],
                font=("Segoe UI", 9),
                fg=TEXT_MUTED,
                bg=CARD_BG,
                wraplength=600,
                justify="left"
            ).pack(anchor="w", pady=(3, 6))

            meta_row = tk.Frame(left_box, bg=CARD_BG)
            meta_row.pack(fill="x")

            meta_info = [
                f"🖵 {de['compositor']}",
                f"⚡ Memory: {de['ram']}",
                f"🛍️ {de.get('app_store', 'cosmic-store')}"
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
                    raw_data = json.load(f)
                    if isinstance(raw_data, list):
                        for item in raw_data:
                            if isinstance(item, dict):
                                tid = item.get("id") or item.get("name")
                                if tid:
                                    themes_data[tid] = item
                    elif isinstance(raw_data, dict):
                        themes_data = raw_data
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

            left_info = tk.Frame(c_inner, bg=CARD_BG)
            left_info.pack(side="left", fill="both", expand=True)

            bg_col = colors.get("bg", colors.get("background", "#000000"))
            card_col = colors.get("card", colors.get("muted", "#111111"))
            prim_col = colors.get("primary", colors.get("foreground", "#ffffff"))
            acc_col = colors.get("accent", "#e83e38")
            border_col = colors.get("active_border", colors.get("accent", "#e83e38"))

            tk.Label(
                left_info,
                text=colors.get("name", theme_id),
                font=("Segoe UI", 11, "bold"),
                fg=TEXT_COLOR,
                bg=CARD_BG
            ).pack(anchor="w")

            tk.Label(
                left_info,
                text=f"Theme ID: {theme_id} | Accent: {acc_col} | BG: {bg_col}",
                font=("Segoe UI", 8),
                fg=TEXT_MUTED,
                bg=CARD_BG
            ).pack(anchor="w", pady=(2, 6))

            swatch_frame = tk.Frame(left_info, bg=CARD_BG)
            swatch_frame.pack(anchor="w")

            for label, color_code in [
                ("BG", bg_col),
                ("Card", card_col),
                ("Primary", prim_col),
                ("Accent", acc_col),
                ("Border", border_col)
            ]:
                s_box = tk.Frame(swatch_frame, bg=CARD_BG)
                s_box.pack(side="left", padx=(0, 10))
                tk.Frame(s_box, bg=color_code, width=24, height=16, highlightbackground="#ffffff", highlightthickness=1).pack()
                tk.Label(s_box, text=label, font=("Segoe UI", 7), fg=TEXT_MUTED, bg=CARD_BG).pack()

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
            text="12 Pristine 4K UHD Anime Rain Wallpapers (3840×2160). Select any wallpaper to set as your desktop background.",
            font=("Segoe UI", 9),
            fg=TEXT_MUTED,
            bg=BG_COLOR,
            anchor="w"
        )
        intro.pack(fill="x", padx=10, pady=(10, 5))

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

        row = 0
        col = 0
        for i, wp in enumerate(wallpapers):
            fname = os.path.basename(wp)
            meta = meta_by_name.get(fname, {})
            title = meta.get("title", f"Wallpaper #{i+1:02d}")

            w_card = tk.Frame(scroll_frame, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
            w_card.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

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
            f"Next time you login or restart display manager, {de['name']} will launch automatically."
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

        cmd = f"sudo pacman -S --needed --noconfirm {pkgs_str}"
        run_in_terminal(cmd, title=f"Installing {de['name']}")

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

def run_cli_install_mode():
    """Runs interactive vertical numbered menu in CLI mode."""
    print("\n============================================================")
    print("      Rain OS Installer - Select Desktop Environment        ")
    print("============================================================")
    print("Displayed in vertical priority order:")
    for idx, de in enumerate(DESKTOPS):
        default_tag = " [FLAGSHIP DEFAULT]" if de.get("recommended") else ""
        print(f"  [{idx+1:2d}] {de['name']:<22} ({de['compositor']:<20}) {default_tag}")
    print("============================================================")
    
    choice = input("\nEnter selection [1-10, default 1 (COSMIC)]: ").strip()
    if not choice:
        selected_de = DESKTOPS[0]
    else:
        try:
            val = int(choice)
            if 1 <= val <= len(DESKTOPS):
                selected_de = DESKTOPS[val - 1]
            else:
                selected_de = DESKTOPS[0]
        except ValueError:
            selected_de = DESKTOPS[0]

    print(f"\nConfigured {selected_de['name']} for target installation.")
    save_installation_choice(selected_de["id"])
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Rain OS Desktop Environment & Window Manager Selector")
    parser.add_argument("--install-mode", action="store_true", help="Launch in installation desktop selection mode")
    parser.add_argument("--cli", action="store_true", help="Run interactive CLI selector instead of GUI")
    parser.add_argument("--list", action="store_true", help="List all available desktop environments and status")
    parser.add_argument("--switch", type=str, metavar="WM_ID", help="Switch default session to specified WM")
    parser.add_argument("--theme", type=str, metavar="THEME_ID", help="Apply Omarchy theme")
    parser.add_argument("--wallpaper", type=str, metavar="NUM_OR_PATH", help="Set wallpaper by number or path")
    parser.add_argument("--install", type=str, metavar="WM_ID", help="Install specified desktop environment")
    parser.add_argument("--current", action="store_true", help="Print active session name")

    args = parser.parse_args()

    if args.list:
        print(f"{'ID':<12} {'NAME':<22} {'STATUS':<15} {'COMPOSITOR':<25} {'RAM':<10}")
        print("-" * 84)
        active = get_active_desktop()
        for d in DESKTOPS:
            inst = is_desktop_installed(d)
            status = "ACTIVE" if d["id"] == active else ("INSTALLED" if inst else "AVAILABLE")
            print(f"{d['id']:<12} {d['name']:<22} {status:<15} {d['compositor']:<25} {d['ram']:<10}")
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
            print("Failed to switch session.", file=sys.stderr)
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
        res = subprocess.run(f"sudo pacman -S --needed --noconfirm {pkgs}", shell=True)
        sys.exit(res.returncode)

    has_display = bool(os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY") or sys.platform.startswith("win"))

    if args.install_mode:
        if args.cli or not has_display:
            run_cli_install_mode()
        else:
            try:
                app = InstallationDesktopSelectorGUI()
                app.mainloop()
            except Exception as e:
                print(f"GUI launch failed ({e}), falling back to CLI...", file=sys.stderr)
                run_cli_install_mode()
        sys.exit(0)

    if args.cli or not has_display:
        print("Desktop Selector: No display found. Use --list, --switch <wm>, or run in a graphical session.")
        sys.exit(1)

    app = DesktopSelectorGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
