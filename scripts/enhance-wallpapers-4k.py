#!/usr/bin/env python3
"""
Rain OS 4K Wallpaper Enhancement and Purification Pipeline
- Eliminates all white divider edge cuts, fringes, and seams
- Inpaints and removes all overlay text, slogans, and watermarks
- Applies bilateral denoising, Lanczos 4K UHD (3840x2160) upscaling,
  multi-scale unsharp masking, and cinematic Urban Rain color grading
"""
import os
import glob
import json
import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

TARGET_W = 3840
TARGET_H = 2160

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
OUT_DIR = os.path.join(ROOT_DIR, 'branding', 'wallpapers')
os.makedirs(OUT_DIR, exist_ok=True)

USER_UPLOAD_DIR = r'C:\Users\DELL\.gemini\antigravity\brain\0cc99af3-734f-4db7-afd1-b318800c1db3\.user_uploaded'
IMG1_PATH = os.path.join(USER_UPLOAD_DIR, 'media_1789216794998.jpg')
IMG2_PATH = os.path.join(USER_UPLOAD_DIR, 'media_1789216802532.jpg')
IMG3_PATH = os.path.join(USER_UPLOAD_DIR, 'media_1789216808742.jpg')

# Precise bounding boxes with 4px safety inward margins to completely eliminate divider lines
# Sheet 1: 4 rows x 5 cols
s1_boxes = [
    (4, 4, 183, 140), (195, 4, 391, 140), (403, 4, 600, 140), (612, 4, 828, 140), (840, 4, 1020, 140),
    (4, 151, 172, 284), (184, 151, 386, 284), (398, 151, 607, 284), (619, 151, 826, 284), (837, 151, 1020, 284),
    (4, 296, 194, 418), (206, 296, 396, 418), (409, 296, 594, 418), (606, 296, 819, 418), (830, 296, 1020, 418),
    (4, 429, 202, 572), (214, 429, 390, 572), (402, 429, 566, 572), (577, 429, 804, 572), (815, 429, 1020, 572)
]

# Sheet 2: 4 rows x 5 cols (Dividers at x: 219, 403, 619, 804 | y: 143, 287, 430)
s2_boxes = [
    (4, 4, 214, 138), (225, 4, 398, 138), (409, 4, 614, 138), (625, 4, 798, 138), (809, 4, 1020, 138),
    (4, 148, 214, 282), (225, 148, 398, 282), (409, 148, 614, 282), (625, 148, 798, 282), (809, 148, 1020, 282),
    (4, 293, 214, 424), (225, 293, 398, 424), (409, 293, 614, 424), (625, 293, 798, 424), (809, 293, 1020, 424),
    (4, 435, 214, 572), (225, 435, 398, 572), (409, 435, 614, 572), (625, 435, 798, 572), (809, 435, 1020, 572)
]

# Sheet 3: 4 rows x 4 cols (Dividers at x: 256, 511, 767 | y: 144, 288, 424)
s3_boxes = [
    (4, 4, 250, 139), (262, 4, 506, 139), (518, 4, 762, 139), (774, 4, 1020, 139),
    (4, 149, 161, 283), (173, 149, 506, 283), (518, 149, 762, 283), (774, 149, 1020, 283),
    (4, 293, 250, 419), (262, 293, 506, 419), (518, 293, 762, 419), (774, 293, 1020, 419),
    (4, 429, 250, 572), (262, 429, 506, 572), (518, 429, 762, 572), (774, 429, 1020, 572)
]

# Text regions dictionary: frame_number -> list of (y1_pct, y2_pct, x1_pct, x2_pct, threshold)
TEXT_OVERLAYS = {
    # Sheet 1
    2: [(0.25, 0.45, 0.45, 0.95, 100)],            # Subway sign
    6: [(0.70, 0.95, 0.05, 0.55, 70)],             # 'Found myself in the rain'
    8: [(0.10, 0.55, 0.05, 0.45, 70)],             # 'Different Skies Same Thoughts'
    10: [(0.15, 0.60, 0.70, 0.98, 80)],            # 'Music Rain You'
    11: [(0.15, 0.65, 0.05, 0.45, 75)],            # 'Same Songs Different Feelings'
    13: [(0.65, 0.95, 0.60, 0.98, 60)],            # 'it will be okay'
    14: [(0.25, 0.70, 0.05, 0.35, 75)],            # 'Good Music Better Days' poster
    15: [(0.10, 0.65, 0.70, 0.98, 65)],            # 'A Quieter Internet A Kinder World'
    19: [(0.10, 0.35, 0.65, 0.95, 110)],           # Highway overhead sign
    
    # Sheet 2
    21: [(0.12, 0.65, 0.05, 0.45, 65)],            # 'Some Peace in the Rain' billboard
    22: [(0.25, 0.45, 0.45, 0.95, 100)],           # Subway sign
    23: [(0.45, 0.75, 0.05, 0.30, 80)],            # Monitor text
    25: [(0.10, 0.65, 0.65, 0.98, 70)],            # 'Same Place Different Mindset'
    26: [(0.70, 0.95, 0.05, 0.55, 70)],            # 'Found myself in the rain'
    27: [(0.15, 0.65, 0.05, 0.45, 75)],            # 'Same Songs Different Feelings'
    28: [(0.10, 0.55, 0.05, 0.45, 70)],            # 'Different Skies Same Thoughts'
    30: [(0.45, 0.85, 0.05, 0.45, 75)],            # 'Better Things Ahead'
    31: [(0.15, 0.55, 0.60, 0.98, 75)],            # 'it will be okay'
    33: [(0.20, 0.65, 0.70, 0.98, 75)],            # 'Music Rain You'
    34: [(0.10, 0.65, 0.05, 0.40, 70)],            # 'A Quieter Internet A Kinder World'
    35: [(0.45, 0.85, 0.02, 0.30, 70)],            # 'Built for Calmer Tomorrows'
    36: [(0.10, 0.35, 0.65, 0.95, 110)],           # Overhead highway sign
    
    # Sheet 3
    41: [(0.15, 0.75, 0.05, 0.35, 45)],            # 'A Calmer Brighter You' poster
    43: [(0.45, 0.85, 0.75, 0.98, 70)],            # 'Same Space Different Mindset'
    44: [(0.25, 0.65, 0.80, 0.98, 70)],            # 'Lost But Here'
    46: [(0.35, 0.70, 0.70, 0.95, 70)],            # 'Better Things Ahead'
    47: [(0.10, 0.55, 0.75, 0.98, 70)],            # 'Rain Coffee Ideas Progress'
    48: [(0.10, 0.55, 0.75, 0.98, 70)],            # 'Different Skies Same Dreams'
    49: [(0.10, 0.65, 0.05, 0.40, 65)],            # 'Some Peace in the Rain'
    50: [(0.10, 0.55, 0.05, 0.35, 70)],            # 'Music Feels Different Here'
    51: [(0.50, 0.85, 0.05, 0.35, 70)],            # 'A Quieter Mind'
    52: [(0.15, 0.65, 0.75, 0.98, 70)],            # 'Higher Wetter Brighter'
    53: [(0.40, 0.80, 0.05, 0.35, 60), (0.40, 0.80, 0.40, 0.65, 60)], # 'Still Here Still Growing'
    54: [(0.10, 0.60, 0.05, 0.35, 70)],            # 'Same Rain Different Story'
    55: [(0.10, 0.60, 0.02, 0.35, 70)],            # 'Good Ideas Rain at Night'
    56: [(0.15, 0.80, 0.75, 0.98, 45)]             # 'Create a Calmer Tomorrow' poster
}

def clean_edges(img_bgr, threshold=165):
    """Shaves off any outer border row/col containing bright divider pixels."""
    h, w = img_bgr.shape[:2]
    top = 0
    while top < 8 and np.mean(img_bgr[top, :, :] > threshold) > 0.08:
        top += 1
    bottom = h
    while bottom > h - 8 and np.mean(img_bgr[bottom-1, :, :] > threshold) > 0.08:
        bottom -= 1
    left = 0
    while left < 8 and np.mean(img_bgr[:, left, :] > threshold) > 0.08:
        left += 1
    right = w
    while right > w - 8 and np.mean(img_bgr[:, right-1, :] > threshold) > 0.08:
        right -= 1
    return img_bgr[top:bottom, left:right]

def inpaint_text(img_bgr, frame_num):
    """Inpaints text overlays within specified sub-regions."""
    if frame_num not in TEXT_OVERLAYS:
        return img_bgr
    
    h, w = img_bgr.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)
    
    for (y1_p, y2_p, x1_p, x2_p, thresh_val) in TEXT_OVERLAYS[frame_num]:
        y1, y2 = int(y1_p * h), int(y2_p * h)
        x1, x2 = int(x1_p * w), int(x2_p * w)
        y1, y2 = max(0, y1), min(h, y2)
        x1, x2 = max(0, x1), min(w, x2)
        
        reg = img_bgr[y1:y2, x1:x2]
        gray = cv2.cvtColor(reg, cv2.COLOR_BGR2GRAY)
        mask_sub = (gray > thresh_val).astype(np.uint8) * 255
        
        # Dilate mask to cover font anti-aliasing
        kernel = np.ones((3, 3), np.uint8)
        mask_sub = cv2.dilate(mask_sub, kernel, iterations=1)
        mask[y1:y2, x1:x2] = mask_sub
    
    if (mask > 0).sum() > 0:
        return cv2.inpaint(img_bgr, mask, inpaintRadius=4, flags=cv2.INPAINT_TELEA)
    return img_bgr

def enhance_to_4k(img_bgr):
    """Multi-stage 4K enhancement pipeline."""
    # 1. Bilateral filter to smooth compression artifacts while retaining sharp edges
    filtered = cv2.bilateralFilter(img_bgr, d=5, sigmaColor=32, sigmaSpace=32)
    
    # 2. Convert BGR to RGB PIL Image
    img_rgb = cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    
    # 3. High-grade Lanczos upscale to native 4K UHD (3840x2160)
    res = pil_img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    
    # 4. Multi-scale unsharp masking for razor-sharp rain droplets and neon reflections
    res = res.filter(ImageFilter.UnsharpMask(radius=2.0, percent=135, threshold=2))
    res = res.filter(ImageFilter.UnsharpMask(radius=4.5, percent=50, threshold=3))
    
    # 5. Cinematic Rain Color Grading: rich blacks, glowing neons, subtle saturation
    res = ImageEnhance.Contrast(res).enhance(1.06)
    res = ImageEnhance.Color(res).enhance(1.10)
    res = ImageEnhance.Sharpness(res).enhance(1.12)
    
    return res

def process_all():
    im1 = cv2.imread(IMG1_PATH)
    im2 = cv2.imread(IMG2_PATH)
    im3 = cv2.imread(IMG3_PATH)
    
    all_jobs = []
    for b in s1_boxes: all_jobs.append((im1, b))
    for b in s2_boxes: all_jobs.append((im2, b))
    for b in s3_boxes: all_jobs.append((im3, b))
    
    manifest = []
    print(f'Starting processing of {len(all_jobs)} 4K UHD wallpapers...')
    
    for idx, (sheet_img, box) in enumerate(all_jobs, 1):
        x1, y1, x2, y2 = box
        crop = sheet_img[y1:y2, x1:x2]
        
        # Step 1: Shave any divider fringe
        cleaned = clean_edges(crop)
        
        # Step 2: Inpaint text overlays / watermarks
        inpainted = inpaint_text(cleaned, idx)
        
        # Step 3: Enhance to 4K UHD
        enhanced_4k = enhance_to_4k(inpainted)
        
        # Step 4: Save wallpaper
        fname = f'rain-wallpaper-{idx:02d}.jpg'
        fpath = os.path.join(OUT_DIR, fname)
        enhanced_4k.save(fpath, 'JPEG', quality=96, subsampling=0)
        
        fsize = os.path.getsize(fpath)
        manifest.append({
            'id': f'rain-{idx:02d}',
            'filename': fname,
            'title': f'Urban Rain #{idx:02d}',
            'resolution': '3840x2160',
            'aspect_ratio': '16:9',
            'size_bytes': fsize
        })
        print(f'Processed [{idx:02d}/56] {fname} ({round(fsize/1024/1024, 2)} MB)')
        
    # Write manifest
    with open(os.path.join(OUT_DIR, 'wallpapers.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
        
    # Set flagship default wallpaper: Frame 21 (Tokyo neon balcony with umbrella)
    hero_src = os.path.join(OUT_DIR, 'rain-wallpaper-21.jpg')
    hero_dest = os.path.join(ROOT_DIR, 'branding', 'rain-wallpaper-4k.jpg')
    if os.path.exists(hero_src):
        import shutil
        shutil.copy2(hero_src, hero_dest)
        print('Updated branding/rain-wallpaper-4k.jpg to enhanced Frame 21!')

if __name__ == '__main__':
    process_all()
