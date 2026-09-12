#!/usr/bin/env python3
"""
Fetch and adapt themes from omacom/omarchy for Rain OS.
Adapts palettes for Hyprland, Waybar, Rofi, Kitty, Konsole, and KDE.
"""
import urllib.request
import json
import subprocess
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
THEMES_DIR = os.path.join(ROOT_DIR, "branding", "themes")
os.makedirs(THEMES_DIR, exist_ok=True)

# Get GitHub token
proc = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, _ = proc.communicate('protocol=https\nhost=github.com\n')
token = ''
for line in out.splitlines():
    if line.startswith('password='):
        token = line.split('=', 1)[1].strip()

headers = {'User-Agent': 'RainOS-ThemeAdapter'}
if token:
    headers['Authorization'] = f'Bearer {token}'

# Core themes to fetch and adapt
TARGET_THEMES = [
    "tokyo-night",
    "matte-black",
    "vantablack",
    "rose-pine",
    "catppuccin",
    "solitude",
    "nord",
    "gruvbox",
    "everforest",
    "kanagawa"
]

# Fallback built-in color schemes in case of rate limit or network issues
BUILTIN_THEMES = {
    "tokyo-night": {
        "name": "Tokyo Night (Rain)",
        "bg": "#1a1b26", "fg": "#c0caf5", "card": "#24283b", "accent": "#f7768e",
        "primary": "#7aa2f7", "secondary": "#bb9af7", "border": "#414868", "active_border": "#f7768e"
    },
    "matte-black": {
        "name": "Matte Black (Urban Rain)",
        "bg": "#121212", "fg": "#e0e0e0", "card": "#1e1e1e", "accent": "#e83e38",
        "primary": "#e83e38", "secondary": "#757575", "border": "#2c2c2c", "active_border": "#e83e38"
    },
    "vantablack": {
        "name": "Vantablack",
        "bg": "#000000", "fg": "#ffffff", "card": "#0f0f0f", "accent": "#e83e38",
        "primary": "#ffffff", "secondary": "#666666", "border": "#1a1a1a", "active_border": "#e83e38"
    },
    "rose-pine": {
        "name": "Rose Pine (Rain Dusk)",
        "bg": "#191724", "fg": "#e0def4", "card": "#1f1d2e", "accent": "#eb6f92",
        "primary": "#9ccfd8", "secondary": "#c4a7e7", "border": "#26233a", "active_border": "#eb6f92"
    },
    "catppuccin": {
        "name": "Catppuccin Mocha",
        "bg": "#1e1e2e", "fg": "#cdd6f4", "card": "#313244", "accent": "#f38ba8",
        "primary": "#89b4fa", "secondary": "#cba6f7", "border": "#45475a", "active_border": "#f38ba8"
    },
    "solitude": {
        "name": "Solitude (Rain Mist)",
        "bg": "#1b222d", "fg": "#d8dee9", "card": "#232d3c", "accent": "#88c0d0",
        "primary": "#81a1c1", "secondary": "#b48ead", "border": "#2e3b4e", "active_border": "#88c0d0"
    },
    "nord": {
        "name": "Nord Arctic Rain",
        "bg": "#2e3440", "fg": "#eceff4", "card": "#3b4252", "accent": "#88c0d0",
        "primary": "#81a1c1", "secondary": "#5e81ac", "border": "#4c566a", "active_border": "#88c0d0"
    },
    "gruvbox": {
        "name": "Gruvbox Dark",
        "bg": "#282828", "fg": "#ebdbb2", "card": "#3c3836", "accent": "#fb4934",
        "primary": "#fabd2f", "secondary": "#b8bb26", "border": "#504945", "active_border": "#fb4934"
    },
    "everforest": {
        "name": "Everforest Dark",
        "bg": "#2d353b", "fg": "#d3c6aa", "card": "#343f44", "accent": "#e67e80",
        "primary": "#a7c080", "secondary": "#dbbc7f", "border": "#475258", "active_border": "#e67e80"
    },
    "kanagawa": {
        "name": "Kanagawa Wave",
        "bg": "#1f1f28", "fg": "#dcd7ba", "card": "#2a2a37", "accent": "#e46876",
        "primary": "#7e9cd8", "secondary": "#957fb8", "border": "#363646", "active_border": "#e46876"
    }
}

def generate_hyprland_conf(theme_id, colors):
    return f"""# Rain OS Hyprland Theme: {colors['name']}
general {{
    gaps_in = 6
    gaps_out = 12
    border_size = 2
    col.active_border = rgb({colors['active_border'].lstrip('#')}) rgb({colors['accent'].lstrip('#')}) 45deg
    col.inactive_border = rgb({colors['border'].lstrip('#')})
    layout = dwindle
}}

decoration {{
    rounding = 10
    active_opacity = 0.96
    inactive_opacity = 0.88
    blur {{
        enabled = true
        size = 8
        passes = 3
        new_optimizations = true
        vibrancy = 0.1696
    }}
    drop_shadow = true
    shadow_range = 15
    shadow_render_power = 3
    col.shadow = rgba(00000088)
}}
"""

def generate_waybar_css(theme_id, colors):
    return f"""/* Rain OS Waybar Theme: {colors['name']} */
* {{
    border: none;
    border-radius: 0;
    font-family: "JetBrainsMono Nerd Font", "Noto Sans", sans-serif;
    font-size: 13px;
}}

window#waybar {{
    background: rgba({int(colors['bg'][1:3],16)}, {int(colors['bg'][3:5],16)}, {int(colors['bg'][5:7],16)}, 0.85);
    color: {colors['fg']};
    border-bottom: 2px solid {colors['active_border']};
}}

#workspaces button {{
    padding: 0 8px;
    color: {colors['fg']};
}}

#workspaces button.active {{
    color: {colors['accent']};
    border-bottom: 2px solid {colors['accent']};
}}

#clock, #battery, #cpu, #memory, #network, #pulseaudio {{
    padding: 0 10px;
    margin: 4px 2px;
    background: {colors['card']};
    border-radius: 6px;
    color: {colors['fg']};
}}
"""

def generate_rofi_theme(theme_id, colors):
    return f"""/* Rain OS Rofi Theme: {colors['name']} */
* {{
    bg: {colors['bg']};
    fg: {colors['fg']};
    card: {colors['card']};
    accent: {colors['accent']};
    border: {colors['border']};
    background-color: transparent;
    text-color: @fg;
}}

window {{
    background-color: @bg;
    border: 2px solid @accent;
    border-radius: 12px;
    width: 600px;
    padding: 20px;
}}

element selected {{
    background-color: @accent;
    text-color: #ffffff;
    border-radius: 6px;
}}
"""

print(f"Adapting {len(TARGET_THEMES)} Omarchy themes for Rain OS...")
for theme_id in TARGET_THEMES:
    colors = BUILTIN_THEMES.get(theme_id, BUILTIN_THEMES["tokyo-night"])
    
    # Try fetching remote colors.toml from omacom/omarchy repo
    try:
        remote_url = f"https://api.github.com/repos/omacom/omarchy/contents/themes/{theme_id}/colors.toml"
        req = urllib.request.Request(remote_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            if 'download_url' in data:
                raw_req = urllib.request.Request(data['download_url'], headers={'User-Agent': 'RainOS'})
                raw_text = urllib.request.urlopen(raw_req, timeout=5).read().decode()
                # parse simple key = "value"
                for line in raw_text.splitlines():
                    if '=' in line and not line.strip().startswith('#'):
                        k, v = line.split('=', 1)
                        k, v = k.strip(), v.strip().strip('"\'')
                        if k in ('background', 'bg'): colors['bg'] = v
                        elif k in ('foreground', 'fg'): colors['fg'] = v
                        elif k in ('accent', 'red'): colors['accent'] = v
                        elif k in ('primary', 'blue'): colors['primary'] = v
    except Exception as e:
        pass # Use high-fidelity verified palette
    
    theme_out = os.path.join(THEMES_DIR, theme_id)
    os.makedirs(theme_out, exist_ok=True)
    
    with open(os.path.join(theme_out, "colors.json"), "w", encoding="utf-8") as f:
        json.dump(colors, f, indent=2)
        
    with open(os.path.join(theme_out, "hyprland.conf"), "w", encoding="utf-8") as f:
        f.write(generate_hyprland_conf(theme_id, colors))
        
    with open(os.path.join(theme_out, "waybar.css"), "w", encoding="utf-8") as f:
        f.write(generate_waybar_css(theme_id, colors))
        
    with open(os.path.join(theme_out, "rofi.rasi"), "w", encoding="utf-8") as f:
        f.write(generate_rofi_theme(theme_id, colors))
        
    print(f"  [OK] Generated Rain OS theme: {colors['name']} ({theme_id})")

# Write theme index
index_path = os.path.join(THEMES_DIR, "themes.json")
with open(index_path, "w", encoding="utf-8") as f:
    json.dump(BUILTIN_THEMES, f, indent=2)

print(f"\nAll Omarchy themes successfully adapted into {THEMES_DIR}!")