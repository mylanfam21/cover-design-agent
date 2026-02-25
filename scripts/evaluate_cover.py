#!/usr/bin/env python3
"""
Cover Evaluation Helper
Utilities for preparing cover images for Claude vision-based scoring.

This script handles:
- Thumbnail simulation (resizing to various sizes for testing)
- Grayscale conversion for contrast testing
- Side-by-side competitor grid creation
- Image metadata logging

The actual scoring is done by Claude's vision capabilities in conversation.
This script just prepares the images for evaluation.

Usage:
    python evaluate_cover.py thumbnail ./output/candidates/cover_001.png
    python evaluate_cover.py grayscale ./output/candidates/cover_001.png
    python evaluate_cover.py grid ./output/candidates/ --refs ./references/genre-screenshots/prayer/
    python evaluate_cover.py report ./output/candidates/
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

try:
    from PIL import Image, ImageFilter
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


def check_pil():
    if not HAS_PIL:
        print("ERROR: Pillow is required for image processing.")
        print("Install with: pip install Pillow")
        sys.exit(1)


def thumbnail_test(image_path, output_dir=None):
    """
    Create thumbnail versions at key Amazon display sizes.
    The 60px height version is the critical minimum stress test.
    """
    check_pil()

    img = Image.open(image_path)
    name = Path(image_path).stem
    out = Path(output_dir or Path(image_path).parent / "thumbnails")
    out.mkdir(parents=True, exist_ok=True)

    # Key sizes to test (width in pixels)
    sizes = {
        "50w_mobile_worst": (50, None),
        "60h_stress_test": (None, 60),
        "80w_also_bought": (80, None),
        "100w_desktop_search": (100, None),
        "150w_kindle_store": (150, None),
    }

    saved = []
    for label, (target_w, target_h) in sizes.items():
        ratio = img.width / img.height
        if target_w:
            new_w = target_w
            new_h = int(target_w / ratio)
        else:
            new_h = target_h
            new_w = int(target_h * ratio)

        thumb = img.resize((new_w, new_h), Image.LANCZOS)
        filepath = out / f"{name}_{label}.png"
        thumb.save(filepath)
        saved.append(str(filepath))
        print(f"Saved {label}: {new_w}x{new_h}px -> {filepath}")

    return saved


def grayscale_test(image_path, output_dir=None):
    """
    Convert to grayscale to test if title and contrast hold up without color.
    """
    check_pil()

    img = Image.open(image_path)
    name = Path(image_path).stem
    out = Path(output_dir or Path(image_path).parent)

    gray = img.convert("L")
    filepath = out / f"{name}_grayscale.png"
    gray.save(filepath)
    print(f"Saved grayscale: {filepath}")
    return str(filepath)


def competitor_grid(candidates_dir, refs_dir=None, output_dir=None, max_covers=10):
    """
    Create a side-by-side grid showing candidate covers next to competitor references.
    This simulates how the cover will look in Amazon search results.
    """
    check_pil()

    candidates = sorted(Path(candidates_dir).glob("*.png")) + \
                 sorted(Path(candidates_dir).glob("*.jpg"))

    refs = []
    if refs_dir and Path(refs_dir).exists():
        refs = sorted(Path(refs_dir).glob("*.png")) + \
               sorted(Path(refs_dir).glob("*.jpg"))

    if not candidates:
        print("No candidate images found.")
        return None

    # Standardize all images to same height
    target_h = 300
    images = []

    # Add some refs first (competitors)
    for ref_path in refs[:5]:
        img = Image.open(ref_path)
        ratio = img.width / img.height
        img = img.resize((int(target_h * ratio), target_h), Image.LANCZOS)
        images.append(("ref", img))

    # Add candidates
    for cand_path in candidates[:max_covers]:
        img = Image.open(cand_path)
        ratio = img.width / img.height
        img = img.resize((int(target_h * ratio), target_h), Image.LANCZOS)
        images.append(("candidate", img))

    if not images:
        print("No images to grid.")
        return None

    # Create grid
    padding = 10
    total_w = sum(img.width for _, img in images) + padding * (len(images) + 1)
    grid = Image.new("RGB", (total_w, target_h + padding * 2), (255, 255, 255))

    x = padding
    for label, img in images:
        grid.paste(img, (x, padding))
        x += img.width + padding

    out = Path(output_dir or candidates_dir)
    filepath = out / "competitor_grid.png"
    grid.save(filepath)
    print(f"Saved competitor grid ({len(images)} covers): {filepath}")
    return str(filepath)


def generate_report(candidates_dir):
    """
    List all candidate images with basic metadata for Claude to evaluate.
    """
    candidates = sorted(Path(candidates_dir).glob("*.png")) + \
                 sorted(Path(candidates_dir).glob("*.jpg"))

    # Filter out thumbnails and test images
    candidates = [c for c in candidates if not any(
        x in c.stem for x in ["thumbnail", "grayscale", "grid", "_50w", "_60h", "_80w", "_100w", "_150w"]
    )]

    report = {
        "total_candidates": len(candidates),
        "directory": str(candidates_dir),
        "images": []
    }

    for c in candidates:
        size = os.path.getsize(c)
        info = {
            "filename": c.name,
            "path": str(c),
            "size_kb": round(size / 1024, 1),
        }
        if HAS_PIL:
            img = Image.open(c)
            info["dimensions"] = f"{img.width}x{img.height}"
            info["aspect_ratio"] = round(img.width / img.height, 3)
        report["images"].append(info)

    print(json.dumps(report, indent=2))
    return report


def main():
    parser = argparse.ArgumentParser(description="Cover evaluation utilities")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Thumbnail test
    thumb_p = subparsers.add_parser("thumbnail", help="Generate thumbnail test images")
    thumb_p.add_argument("image", help="Path to cover image")
    thumb_p.add_argument("--output", "-o", help="Output directory")

    # Grayscale test
    gray_p = subparsers.add_parser("grayscale", help="Generate grayscale test image")
    gray_p.add_argument("image", help="Path to cover image")
    gray_p.add_argument("--output", "-o", help="Output directory")

    # Competitor grid
    grid_p = subparsers.add_parser("grid", help="Create competitor comparison grid")
    grid_p.add_argument("candidates", help="Directory with candidate covers")
    grid_p.add_argument("--refs", "-r", help="Directory with reference/competitor covers")
    grid_p.add_argument("--output", "-o", help="Output directory")

    # Report
    report_p = subparsers.add_parser("report", help="Generate candidate report")
    report_p.add_argument("candidates", help="Directory with candidate covers")

    args = parser.parse_args()

    if args.command == "thumbnail":
        thumbnail_test(args.image, args.output)
    elif args.command == "grayscale":
        grayscale_test(args.image, args.output)
    elif args.command == "grid":
        competitor_grid(args.candidates, args.refs, args.output)
    elif args.command == "report":
        generate_report(args.candidates)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
