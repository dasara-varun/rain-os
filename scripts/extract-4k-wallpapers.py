#!/usr/bin/env python3
"""
Extract and upscale 56 individual 4K UHD wallpapers from the user's aesthetic rain contact sheets.
"""
import os
import json
from PIL import Image, ImageFilter, ImageEnhance

TARGET_W = 3840
TARGET_H = 2160

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
OUT_DIR = os.path.join(ROOT_DIR, "branding", "wallpapers")
os.makedirs(OUT_DIR, exist_ok=True)

USER_UPLOAD_DIR = r"C:\Users\DELL\.gemini\antigravity\brain\0cc99af3-734f-4db7-afd1-b318800c1db3\.user_uploaded"
IMG1 = os.path.join(USER_UPLOAD_DIR, "media_1789216794998.jpg")
IMG2 = os.path.join(USER_UPLOAD_DIR, "media_1789216802532.jpg")
IMG3 = os.path.join(USER_UPLOAD_DIR, "media_1789216808742.jpg")

# Define exact frame bounding boxes (x1, y1, x2, y2) without white divider lines
# Image 1 frames (4 rows x 5 cols)
im1_boxes = [
    # Row 0 (y: 0..144)
    (0, 0, 187, 144), (191, 0, 395, 144), (399, 0, 604, 144), (608, 0, 832, 144), (836, 0, 1024, 144),
    # Row 1 (y: 147..288)
    (0, 147, 176, 288), (180, 147, 390, 288), (394, 147, 611, 288), (615, 147, 830, 288), (833, 147, 1024, 288),
    # Row 2 (y: 292..422)
    (0, 292, 198, 422), (202, 292, 400, 422), (405, 292, 598, 422), (602, 292, 823, 422), (826, 292, 1024, 422),
    # Row 3 (y: 425..576)
    (0, 425, 206, 576), (210, 425, 394, 576), (398, 425, 570, 576), (573, 425, 808, 576), (811, 425, 1024, 576)
]

# Image 2 frames (4 rows x 5 cols)
# Dividers at x: 219, 403, 619, 804 | y: 143, 287, 430
im2_boxes = [
    # Row 0
    (0, 0, 218, 141), (221, 0, 402, 141), (405, 0, 618, 141), (621, 0, 802, 141), (805, 0, 1024, 141),
    # Row 1
    (0, 144, 218, 286), (221, 144, 402, 286), (405, 144, 618, 286), (621, 144, 802, 286), (805, 144, 1024, 286),
    # Row 2
    (0, 289, 218, 428), (221, 289, 402, 428), (405, 289, 618, 428), (621, 289, 802, 428), (805, 289, 1024, 428),
    # Row 3
    (0, 431, 218, 576), (221, 431, 402, 576), (405, 431, 618, 576), (621, 431, 802, 576), (805, 431, 1024, 576)
]

# Image 3 frames (4 rows x 4 cols, row 1 has wide frame in middle)
im3_boxes = [
    # Row 0 (y: 0..143)
    (0, 0, 254, 143), (257, 0, 510, 143), (513, 0, 766, 143), (769, 0, 1024, 143),
    # Row 1 (y: 145..287)
    (0, 145, 165, 287), (168, 145, 510, 287), (513, 145, 766, 287), (769, 145, 1024, 287),
    # Row 2 (y: 289..422)
    (0, 289, 254, 422), (257, 289, 510, 422), (513, 289, 766, 422), (769, 289, 1024, 422),
    # Row 3 (y: 425..576)
    (0, 425, 254, 576), (257, 425, 510, 576), (513, 425, 766, 576), (769, 425, 1024, 576)
]

titles = [
    # Image 1 (20)
    "Rain Headphone Memories", "Rainy Subway Platform", "Umbrella Neon Reflection", "City Window Cat Silhouette", "Night Skyline Balcony",
    "Red Lantern Rainy Alley", "Train Window Raindrop Thoughts", "Dusk Skyline Silhouette", "Under the Rain Together", "Music in the Rain",
    "Neon Tower Rain Reflection", "Torii Gate Rainy Walk", "It Will Be Okay", "Lofi Coffee by the Window", "A Quieter Kinder World",
    "Lofi Midnight Beats", "Falling Star Rain Sky", "Rain on Face Solitude", "Rainy Mountain Highway Drive", "Crimson Sunset Rooftop",
    
    # Image 2 (20)
    "Peace in the Rain", "Midnight Station Rain", "Lofi Desk Neon Cityscape", "Crimson River Twilight", "Quiet Window Glow",
    "Umbrella in Tokyo Alley", "Same Songs Different Feelings", "Dusk Rooftop Solitude", "Cliff Glass House Rain", "Better Things Ahead Neon",
    "Pier Rain Lantern", "Twilight Train Crossing", "Neon Cat Music Night", "Moonlight Expressway Trails", "Calmer Tomorrows Glass Hall",
    "Midnight Sports Car in Rain", "Mountain Path Fog Sunset", "Raindrops on Warm Cafe Window", "Tokyo Alleyway Glow", "Sakura Blossom Rainy Rooftop",
    
    # Image 3 (16)
    "Calmer Brighter You", "Suspended Villa Rain", "Rain Always With You", "Lost But Here Gateway",
    "Neon Rain Pavements", "Panoramic Hearth Rain Lounge", "Purple Tokyo Tower Balcony", "Overpass Sunset Bridge",
    "Some Peace in the Rain Rooftop", "Music Feels Different Here", "Architectural Glass Stairway", "Higher Wetter Brighter Arc",
    "Infinity Pool Night Skyline", "Full Moon Skyscraper Silhouette", "Good Ideas Rain at Night", "Create a Calmer Tomorrow"
]

all_sources = [
    (IMG1, im1_boxes),
    (IMG2, im2_boxes),
    (IMG3, im3_boxes)
]

def upscale_frame(crop_img):
    # Scale to 16:9 3840x2160
    # First resize with high-grade Lanczos
    res = crop_img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    
    # Subtle enhancement: slight contrast boost (1.05) and sharpening
    enhancer = ImageEnhance.Contrast(res)
    res = enhancer.enhance(1.04)
    
    # Subtle unsharp mask to crisp edges
    res = res.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=2))
    return res

wallpapers_manifest = []
global_idx = 1

for src_path, boxes in all_sources:
    if not os.path.exists(src_path):
        print(f"Warning: {src_path} not found!")
        continue
    src_img = Image.open(src_path)
    print(f"Processing source: {os.path.basename(src_path)} ({len(boxes)} frames)...")
    
    for box in boxes:
        cropped = src_img.crop(box)
        upscaled = upscale_frame(cropped)
        
        filename = f"rain-wallpaper-{global_idx:02d}.jpg"
        filepath = os.path.join(OUT_DIR, filename)
        upscaled.save(filepath, "JPEG", quality=94, optimize=True)
        
        title = titles[global_idx - 1] if global_idx - 1 < len(titles) else f"Rain OS Scene {global_idx}"
        wallpapers_manifest.append({
            "id": global_idx,
            "filename": filename,
            "title": title,
            "resolution": f"{TARGET_W}x{TARGET_H}",
            "palette": "Urban Rain / Tokyo Night"
        })
        
        # Also select Wallpaper 01 or Wallpaper 21 as the primary default 4K wallpaper
        if global_idx == 21: # Peace in the Rain (Iconic Tokyo Neon)
            hero_path = os.path.join(ROOT_DIR, "branding", "rain-wallpaper-4k.jpg")
            upscaled.save(hero_path, "JPEG", quality=96, optimize=True)
            print(f"  -> Set default 4K wallpaper to: {title}")
            
        global_idx += 1

# Save manifest
manifest_path = os.path.join(OUT_DIR, "wallpapers.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(wallpapers_manifest, f, indent=2)

print(f"\nSuccessfully generated {len(wallpapers_manifest)} 4K UHD wallpapers in {OUT_DIR}!")