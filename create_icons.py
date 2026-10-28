"""
Run this script ONCE to generate the 3 icon sizes needed by the Chrome extension.
Requirements: pip install Pillow

Usage:
    python create_icons.py
"""
from PIL import Image
import os
import shutil

# Source icon (the generated one)
SOURCE_PATHS = [
    r"C:\Users\Mayur Meghna\.gemini\antigravity\brain\59c8304e-8706-410f-afe1-d114b01273f4\extension_icon_1775761331202.png",
]

# Extension icons output directory
OUT_DIR = r"C:\Users\Mayur Meghna\Desktop\Career Autheticity extension\extension\icons"
os.makedirs(OUT_DIR, exist_ok=True)

SIZES = [16, 48, 128]

source = None
for p in SOURCE_PATHS:
    if os.path.exists(p):
        source = p
        break

if not source:
    print("❌ Could not find source icon. Make sure the generated icon exists.")
    exit(1)

img = Image.open(source).convert("RGBA")

for size in SIZES:
    out_path = os.path.join(OUT_DIR, f"icon{size}.png")
    resized  = img.resize((size, size), Image.LANCZOS)
    resized.save(out_path, "PNG")
    print(f"✅ Created {out_path}")

print(f"\n🎉 All icons created in {OUT_DIR}")
