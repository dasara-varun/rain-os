import os
import math
from PIL import Image, ImageDraw, ImageFont

ICONS = [
    {
        "name": "rain-control-center",
        "bg_top": (30, 41, 59),
        "bg_bot": (15, 23, 42),
        "accent": (0, 240, 255),
        "accent_sec": (56, 189, 248),
        "symbol": "control"
    },
    {
        "name": "rain-installer",
        "bg_top": (39, 39, 42),
        "bg_bot": (24, 24, 27),
        "accent": (239, 68, 68),
        "accent_sec": (244, 114, 182),
        "symbol": "installer"
    },
    {
        "name": "rain-welcome",
        "bg_top": (30, 58, 138),
        "bg_bot": (15, 23, 42),
        "accent": (245, 158, 11),
        "accent_sec": (56, 189, 248),
        "symbol": "welcome"
    },
    {
        "name": "rain-learning-hub",
        "bg_top": (6, 78, 59),
        "bg_bot": (2, 44, 34),
        "accent": (16, 185, 129),
        "accent_sec": (52, 211, 153),
        "symbol": "learning"
    },
    {
        "name": "rain-desktop-selector",
        "bg_top": (46, 16, 101),
        "bg_bot": (24, 24, 27),
        "accent": (168, 85, 247),
        "accent_sec": (236, 72, 153),
        "symbol": "selector"
    },
    {
        "name": "rain-store",
        "bg_top": (30, 27, 75),
        "bg_bot": (15, 23, 42),
        "accent": (99, 102, 241),
        "accent_sec": (56, 189, 248),
        "symbol": "store"
    },
    {
        "name": "rain-hardware",
        "bg_top": (41, 37, 36),
        "bg_bot": (23, 23, 23),
        "accent": (249, 115, 22),
        "accent_sec": (234, 179, 8),
        "symbol": "hardware"
    },
    {
        "name": "rain-display",
        "bg_top": (12, 74, 110),
        "bg_bot": (15, 23, 42),
        "accent": (14, 165, 233),
        "accent_sec": (147, 197, 253),
        "symbol": "display"
    }
]

SIZES = [32, 48, 64, 128, 256, 512]

def draw_control(draw, s, c1, c2):
    # Circular Gauge + Tuning Sliders
    cx, cy = s / 2, s / 2
    r = s * 0.32
    # Outer arc
    draw.arc([cx - r, cy - r, cx + r, cy + r], start=140, end=40, fill=c1, width=max(2, int(s * 0.05)))
    # Inner needle
    angle = -45
    rad = math.radians(angle)
    nx = cx + (r * 0.7) * math.cos(rad)
    ny = cy + (r * 0.7) * math.sin(rad)
    draw.line([cx, cy, nx, ny], fill=(255, 255, 255), width=max(2, int(s * 0.04)))
    draw.ellipse([cx - s*0.06, cy - s*0.06, cx + s*0.06, cy + s*0.06], fill=c2)
    # Sliders below
    sy1 = cy + r * 0.45
    sy2 = cy + r * 0.75
    draw.line([cx - r*0.6, sy1, cx + r*0.6, sy1], fill=(148, 163, 184), width=max(1, int(s*0.025)))
    draw.ellipse([cx - r*0.1, sy1 - s*0.035, cx + r*0.1, sy1 + s*0.035], fill=c1)
    draw.line([cx - r*0.6, sy2, cx + r*0.6, sy2], fill=(148, 163, 184), width=max(1, int(s*0.025)))
    draw.ellipse([cx + r*0.2, sy2 - s*0.035, cx + r*0.4, sy2 + s*0.035], fill=c2)

def draw_installer(draw, s, c1, c2):
    # NVMe Drive with Downward Flash Arrow
    cx, cy = s / 2, s / 2
    # Drive body
    w, h = s * 0.55, s * 0.28
    x0, y0 = cx - w/2, cy + s*0.05
    x1, y1 = cx + w/2, y0 + h
    draw.rounded_rectangle([x0, y0, x1, y1], radius=max(2, int(s*0.04)), fill=(71, 85, 105), outline=(148, 163, 184), width=max(1, int(s*0.02)))
    # Chips on drive
    draw.rectangle([x0 + w*0.15, y0 + h*0.2, x0 + w*0.4, y0 + h*0.8], fill=(30, 41, 59))
    draw.rectangle([x0 + w*0.5, y0 + h*0.2, x0 + w*0.85, y0 + h*0.8], fill=(30, 41, 59))
    # Downward install arrow
    aw = s * 0.18
    ay_top = cy - s * 0.32
    ay_mid = cy - s * 0.05
    ay_bot = cy + s * 0.08
    # Arrow stem
    draw.rectangle([cx - aw*0.4, ay_top, cx + aw*0.4, ay_mid], fill=c1)
    # Arrow head
    draw.polygon([(cx, ay_bot), (cx - aw*1.2, ay_mid), (cx + aw*1.2, ay_mid)], fill=c1)

def draw_welcome(draw, s, c1, c2):
    # Beacon / Lighthouse with Star Compass
    cx, cy = s / 2, s / 2
    # Light rays
    r = s * 0.35
    for a in [-50, -25, 0, 25, 50]:
        rad = math.radians(a - 90)
        lx = cx + r * math.cos(rad)
        ly = cy + r * math.sin(rad)
        draw.line([cx, cy - s*0.05, lx, ly], fill=(c2[0], c2[1], c2[2], 120), width=max(1, int(s*0.02)))
    # Lighthouse tower
    tw_top, tw_bot = s * 0.12, s * 0.25
    y_top = cy - s * 0.08
    y_bot = cy + s * 0.32
    draw.polygon([
        (cx - tw_top, y_top),
        (cx + tw_top, y_top),
        (cx + tw_bot, y_bot),
        (cx - tw_bot, y_bot)
    ], fill=(241, 245, 249))
    # Stripes
    draw.polygon([(cx - tw_top*1.2, y_top + s*0.1), (cx + tw_top*1.2, y_top + s*0.1), (cx + tw_top*1.5, y_top + s*0.18), (cx - tw_top*1.5, y_top + s*0.18)], fill=c1)
    # Lantern room (glowing)
    draw.ellipse([cx - s*0.1, y_top - s*0.12, cx + s*0.1, y_top + s*0.05], fill=c1)
    draw.ellipse([cx - s*0.05, y_top - s*0.08, cx + s*0.05, y_top], fill=(255, 255, 255))

def draw_learning(draw, s, c1, c2):
    # Open Textbook with Terminal Prompt
    cx, cy = s / 2, s / 2
    w = s * 0.65
    h = s * 0.45
    y0 = cy - h/2 - s*0.02
    # Left page
    draw.rounded_rectangle([cx - w/2, y0, cx - s*0.03, y0 + h], radius=max(2, int(s*0.03)), fill=(248, 250, 252))
    # Right page
    draw.rounded_rectangle([cx + s*0.03, y0, cx + w/2, y0 + h], radius=max(2, int(s*0.03)), fill=(241, 245, 249))
    # Spine
    draw.line([cx, y0, cx, y0 + h], fill=(100, 116, 139), width=max(2, int(s*0.03)))
    # Terminal prompt '>_' on left page
    px0 = cx - w/2 + s*0.06
    py0 = y0 + s*0.08
    # '>'
    draw.line([px0, py0, px0 + s*0.07, py0 + s*0.06], fill=c1, width=max(2, int(s*0.035)))
    draw.line([px0 + s*0.07, py0 + s*0.06, px0, py0 + s*0.12], fill=c1, width=max(2, int(s*0.035)))
    # '_'
    draw.line([px0 + s*0.11, py0 + s*0.12, px0 + s*0.18, py0 + s*0.12], fill=c2, width=max(2, int(s*0.035)))
    # Text lines on right page
    for i in range(3):
        ly = y0 + s*0.09 + i * s*0.08
        draw.line([cx + s*0.08, ly, cx + w/2 - s*0.06, ly], fill=(148, 163, 184), width=max(1, int(s*0.02)))
    # Graduation cap ribbon below
    draw.line([cx - w*0.35, y0 + h + s*0.05, cx + w*0.35, y0 + h + s*0.05], fill=c1, width=max(2, int(s*0.025)))

def draw_selector(draw, s, c1, c2):
    # 2x2 Workspace Grid Matrix
    cx, cy = s / 2, s / 2
    cell = s * 0.26
    gap = s * 0.05
    coords = [
        (cx - cell - gap/2, cy - cell - gap/2, True),   # Top-Left (Active)
        (cx + gap/2, cy - cell - gap/2, False),         # Top-Right
        (cx - cell - gap/2, cy + gap/2, False),         # Bot-Left
        (cx + gap/2, cy + gap/2, False)                 # Bot-Right
    ]
    for x, y, active in coords:
        if active:
            draw.rounded_rectangle([x, y, x + cell, y + cell], radius=max(2, int(s*0.04)), fill=c1, outline=(255, 255, 255), width=max(2, int(s*0.03)))
            # Window bar
            draw.line([x + cell*0.2, y + cell*0.3, x + cell*0.8, y + cell*0.3], fill=(255, 255, 255), width=max(2, int(s*0.03)))
            draw.rectangle([x + cell*0.2, y + cell*0.5, x + cell*0.5, y + cell*0.8], fill=c2)
            draw.rectangle([x + cell*0.55, y + cell*0.5, x + cell*0.8, y + cell*0.8], fill=(255, 255, 255))
        else:
            draw.rounded_rectangle([x, y, x + cell, y + cell], radius=max(2, int(s*0.04)), fill=(51, 65, 85), outline=(100, 116, 139), width=max(1, int(s*0.02)))
            draw.line([x + cell*0.2, y + cell*0.3, x + cell*0.8, y + cell*0.3], fill=(148, 163, 184), width=max(1, int(s*0.02)))

def draw_store(draw, s, c1, c2):
    # Shopping Bag / Software Package Box with Raindrop
    cx, cy = s / 2, s / 2
    bw = s * 0.56
    bh = s * 0.52
    by0 = cy - bh/2 + s*0.06
    # Handle
    hr = s * 0.16
    draw.arc([cx - hr, by0 - hr*1.2, cx + hr, by0 + hr*0.8], start=180, end=0, fill=c2, width=max(2, int(s*0.045)))
    # Bag body
    draw.rounded_rectangle([cx - bw/2, by0, cx + bw/2, by0 + bh], radius=max(3, int(s*0.06)), fill=c1, outline=(255, 255, 255), width=max(1, int(s*0.02)))
    # Raindrop cut-out in center
    rcx, rcy = cx, by0 + bh*0.55
    rw, rh = s*0.14, s*0.2
    draw.polygon([(rcx, rcy - rh/2), (rcx - rw/2, rcy + rh/4), (rcx + rw/2, rcy + rh/4)], fill=c2)
    draw.ellipse([rcx - rw/2, rcy - rh/6, rcx + rw/2, rcy + rh/2], fill=c2)

def draw_hardware(draw, s, c1, c2):
    # Silicon CPU Die with Circuit Traces
    cx, cy = s / 2, s / 2
    die_s = s * 0.44
    draw.rounded_rectangle([cx - die_s/2, cy - die_s/2, cx + die_s/2, cy - die_s/2 + die_s], radius=max(2, int(s*0.04)), fill=(30, 41, 59), outline=c1, width=max(2, int(s*0.035)))
    # Inner core
    core_s = s * 0.22
    draw.rectangle([cx - core_s/2, cy - core_s/2, cx + core_s/2, cy + core_s/2], fill=c1)
    # CPU Pins
    pin_len = s * 0.12
    for offset in [-s*0.14, 0, s*0.14]:
        # Top & Bottom pins
        draw.line([cx + offset, cy - die_s/2, cx + offset, cy - die_s/2 - pin_len], fill=c2, width=max(2, int(s*0.03)))
        draw.line([cx + offset, cy + die_s/2, cx + offset, cy + die_s/2 + pin_len], fill=c2, width=max(2, int(s*0.03)))
        # Left & Right pins
        draw.line([cx - die_s/2, cy + offset, cx - die_s/2 - pin_len, cy + offset], fill=c2, width=max(2, int(s*0.03)))
        draw.line([cx + die_s/2, cy + offset, cx + die_s/2 + pin_len, cy + offset], fill=c2, width=max(2, int(s*0.03)))

def draw_display(draw, s, c1, c2):
    # Dual Panoramic Curved Monitors
    cx, cy = s / 2, s / 2
    mw, mh = s * 0.34, s * 0.28
    # Left monitor
    lx0, ly0 = cx - mw - s*0.03, cy - mh/2 - s*0.03
    draw.rounded_rectangle([lx0, ly0, lx0 + mw, ly0 + mh], radius=max(2, int(s*0.03)), fill=(15, 23, 42), outline=c1, width=max(2, int(s*0.03)))
    draw.rectangle([lx0 + s*0.04, ly0 + s*0.04, lx0 + mw - s*0.04, ly0 + mh - s*0.04], fill=(30, 58, 138))
    # Right monitor
    rx0, ry0 = cx + s*0.03, cy - mh/2 - s*0.03
    draw.rounded_rectangle([rx0, ry0, rx0 + mw, ry0 + mh], radius=max(2, int(s*0.03)), fill=(15, 23, 42), outline=c2, width=max(2, int(s*0.03)))
    draw.rectangle([rx0 + s*0.04, ry0 + s*0.04, rx0 + mw - s*0.04, ry0 + mh - s*0.04], fill=(14, 116, 144))
    # Shared Stand
    draw.line([cx, cy + mh/2 - s*0.03, cx, cy + mh/2 + s*0.12], fill=(148, 163, 184), width=max(2, int(s*0.04)))
    draw.line([cx - s*0.2, cy + mh/2 + s*0.12, cx + s*0.2, cy + mh/2 + s*0.12], fill=(148, 163, 184), width=max(2, int(s*0.04)))

DISPATCH = {
    "control": draw_control,
    "installer": draw_installer,
    "welcome": draw_welcome,
    "learning": draw_learning,
    "selector": draw_selector,
    "store": draw_store,
    "hardware": draw_hardware,
    "display": draw_display
}

def generate_icon(config, size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded Squircle Background
    pad = max(1, int(size * 0.05))
    rad = max(4, int(size * 0.22))
    
    # Draw vertical gradient background
    base_rect = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    rect_draw = ImageDraw.Draw(base_rect)
    rect_draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=rad, fill=config["bg_bot"], outline=(255, 255, 255, 40), width=max(1, int(size*0.02)))
    
    # Gradient overlay
    for y in range(pad, size - pad):
        factor = (y - pad) / max(1, (size - 2*pad))
        r = int(config["bg_top"][0] * (1 - factor) + config["bg_bot"][0] * factor)
        g = int(config["bg_top"][1] * (1 - factor) + config["bg_bot"][1] * factor)
        b = int(config["bg_top"][2] * (1 - factor) + config["bg_bot"][2] * factor)
        rect_draw.line([(pad, y), (size - pad, y)], fill=(r, g, b, 255))
        
    # Mask to rounded rect
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=rad, fill=255)
    
    img.paste(base_rect, (0, 0), mask)
    
    # Border
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=rad, outline=(255, 255, 255, 50), width=max(1, int(size*0.02)))
    
    # Symbol
    DISPATCH[config["symbol"]](draw, size, config["accent"], config["accent_sec"])
    return img

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dest_dirs = [
        os.path.join(repo_root, "branding", "icons"),
        os.path.join(repo_root, "archiso", "airootfs", "usr", "share", "icons", "hicolor"),
        os.path.join(repo_root, "packages", "rain-branding", "icons")
    ]
    
    for c in ICONS:
        name = c["name"]
        print(f"Generating icon: {name}...")
        for s in SIZES:
            img = generate_icon(c, s)
            
            # Save to standard hicolor dirs
            for base_dir in dest_dirs:
                if "branding\\icons" in base_dir:
                    os.makedirs(base_dir, exist_ok=True)
                    if s == 512:
                        img.save(os.path.join(base_dir, f"{name}.png"), "PNG")
                else:
                    target_dir = os.path.join(base_dir, f"{s}x{s}", "apps")
                    os.makedirs(target_dir, exist_ok=True)
                    img.save(os.path.join(target_dir, f"{name}.png"), "PNG")
                    
    print("SUCCESS: All 8 distinct application icons generated across all resolutions!")

if __name__ == "__main__":
    main()
