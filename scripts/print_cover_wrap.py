#!/usr/bin/env python3
"""
Print Cover Wrap Compositor
Assembles a full paperback/hardcover wrap from components + KDP template.

Takes a KDP cover template (PNG/PDF), front cover image, author photo,
back cover blurb, and author bio — then composites them into a single
print-ready PDF/PNG matching KDP specifications.

Usage:
    python print_cover_wrap.py parse-template ./input/kdp_template.png
    python print_cover_wrap.py calculate --pages 200 --trim-width 5.5 --trim-height 8.5
    python print_cover_wrap.py compose \
        --front ./output/book/final/cover.png \
        --pages 200 --trim-width 5.5 --trim-height 8.5 \
        --blurb "Back cover blurb text" \
        --title "Book Title" \
        --author "Author Name" \
        --output ./output/book/print/
    python print_cover_wrap.py template-overlay \
        --template ./input/kdp_template.png \
        --wrap ./output/book/print/print_cover_wrap.png \
        --output ./output/book/print/

Environment:
    Requires Pillow (pip install Pillow)
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# --- KDP Specifications ---

# Spine width formulas (inches per page)
PAPER_THICKNESS = {
    "white": 0.002252,
    "cream": 0.0025,
}

# Cover material addition to spine
COVER_ALLOWANCE = 0.06  # inches

# Bleed on all sides
BLEED = 0.125  # inches

# Safe margin from trim edge
SAFE_MARGIN = 0.25  # inches

# Spine text minimum margin from spine edge
SPINE_TEXT_MARGIN = 0.0625  # inches

# Minimum pages for spine text
MIN_PAGES_FOR_SPINE_TEXT = 79

# Barcode zone (bottom-right of back cover)
BARCODE_WIDTH = 2.0   # inches
BARCODE_HEIGHT = 1.2  # inches
BARCODE_MARGIN = 0.25  # inches from trim edges

# Print DPI
DPI = 300


def check_pil():
    if not HAS_PIL:
        print("ERROR: Pillow is required. Install with: pip install Pillow")
        sys.exit(1)


def inches_to_px(inches):
    """Convert inches to pixels at 300 DPI."""
    return int(round(inches * DPI))


def px_to_inches(px):
    """Convert pixels to inches at 300 DPI."""
    return px / DPI


def calculate_spine_width(page_count, paper_type="white"):
    """Calculate spine width in inches using KDP formula."""
    thickness = PAPER_THICKNESS.get(paper_type, PAPER_THICKNESS["white"])
    return (page_count * thickness) + COVER_ALLOWANCE


def calculate_full_cover_dimensions(trim_width, trim_height, page_count, paper_type="white"):
    """
    Calculate full wrap dimensions in inches.

    Returns dict with all measurements in inches.
    """
    spine_width = calculate_spine_width(page_count, paper_type)

    full_width = (2 * trim_width) + spine_width + (2 * BLEED)
    full_height = trim_height + (2 * BLEED)

    return {
        "trim_width": trim_width,
        "trim_height": trim_height,
        "spine_width": spine_width,
        "spine_width_inches": spine_width,
        "page_count": page_count,
        "paper_type": paper_type,
        "bleed": BLEED,
        "safe_margin": SAFE_MARGIN,
        "full_width_inches": full_width,
        "full_height_inches": full_height,
        "full_width_px": inches_to_px(full_width),
        "full_height_px": inches_to_px(full_height),
        "spine_width_px": inches_to_px(spine_width),
        "can_have_spine_text": page_count >= MIN_PAGES_FOR_SPINE_TEXT,
        # Zone positions (x coordinates in pixels, from left edge)
        "zones": {
            "back_cover": {
                "x": inches_to_px(BLEED),
                "y": inches_to_px(BLEED),
                "width": inches_to_px(trim_width),
                "height": inches_to_px(trim_height),
            },
            "spine": {
                "x": inches_to_px(BLEED + trim_width),
                "y": inches_to_px(BLEED),
                "width": inches_to_px(spine_width),
                "height": inches_to_px(trim_height),
            },
            "front_cover": {
                "x": inches_to_px(BLEED + trim_width + spine_width),
                "y": inches_to_px(BLEED),
                "width": inches_to_px(trim_width),
                "height": inches_to_px(trim_height),
            },
            "barcode": {
                "x": inches_to_px(BLEED + trim_width - BARCODE_WIDTH - BARCODE_MARGIN),
                "y": inches_to_px(BLEED + trim_height - BARCODE_HEIGHT - BARCODE_MARGIN),
                "width": inches_to_px(BARCODE_WIDTH),
                "height": inches_to_px(BARCODE_HEIGHT),
            },
        },
    }


def parse_template_image(template_path):
    """
    Parse a KDP template image to extract dimensions.
    Returns the image dimensions and estimated zones.

    NOTE: This gives pixel dimensions. For precise zone extraction,
    the user should also provide trim size and page count so we can
    calculate mathematically rather than relying on image parsing.
    """
    check_pil()
    img = Image.open(template_path)

    info = {
        "file": str(template_path),
        "width_px": img.width,
        "height_px": img.height,
        "width_inches": round(px_to_inches(img.width), 3),
        "height_inches": round(px_to_inches(img.height), 3),
        "dpi_assumed": DPI,
        "mode": img.mode,
    }

    print(json.dumps(info, indent=2))
    return info


def get_font(size, bold=False):
    """
    Try to load a good font. Falls back gracefully.
    Users can provide custom TTF files for exact matching.
    """
    # Try common system fonts
    font_candidates = []
    if bold:
        font_candidates = [
            "C:/Windows/Fonts/georgiab.ttf",   # Georgia Bold
            "C:/Windows/Fonts/timesbd.ttf",    # Times New Roman Bold
            "C:/Windows/Fonts/arialbd.ttf",    # Arial Bold
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
            "/System/Library/Fonts/Georgia Bold.ttf",
        ]
    else:
        font_candidates = [
            "C:/Windows/Fonts/georgia.ttf",    # Georgia
            "C:/Windows/Fonts/times.ttf",      # Times New Roman
            "C:/Windows/Fonts/arial.ttf",       # Arial
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "/System/Library/Fonts/Georgia.ttf",
        ]

    for font_path in font_candidates:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                continue

    # Last resort: default font
    try:
        return ImageFont.truetype("arial.ttf", size)
    except Exception:
        return ImageFont.load_default()


def wrap_text(text, font, max_width, draw):
    """Word-wrap text to fit within max_width pixels."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]

    if current_line:
        lines.append(" ".join(current_line))

    return lines


def compose_back_cover(dims, blurb_text, bio_text, author_photo_path=None,
                       bg_color=(255, 255, 255), text_color=(30, 30, 30),
                       custom_font_path=None):
    """
    Compose the back cover panel with blurb, author photo, and bio.

    Layout (top to bottom):
    - Top margin
    - Book blurb (centered, largest text area)
    - Spacer
    - Author section (photo + bio side by side)
    - Bottom margin (barcode zone reserved)
    """
    check_pil()

    zone = dims["zones"]["back_cover"]
    w, h = zone["width"], zone["height"]
    margin = inches_to_px(SAFE_MARGIN)

    back = Image.new("RGB", (w, h), bg_color)
    draw = ImageDraw.Draw(back)

    usable_w = w - (2 * margin)
    usable_top = margin
    barcode_zone = dims["zones"]["barcode"]
    # Reserve space for barcode at bottom-right
    barcode_top = barcode_zone["y"] - dims["zones"]["back_cover"]["y"]
    usable_bottom = barcode_top - inches_to_px(0.3)  # extra breathing room above barcode

    # --- Blurb section (upper 60% of usable area) ---
    blurb_area_height = int((usable_bottom - usable_top) * 0.60)
    blurb_font_size = inches_to_px(0.14)  # ~14pt at 300 DPI
    if custom_font_path:
        try:
            blurb_font = ImageFont.truetype(custom_font_path, blurb_font_size)
        except Exception:
            blurb_font = get_font(blurb_font_size)
    else:
        blurb_font = get_font(blurb_font_size)

    blurb_lines = wrap_text(blurb_text, blurb_font, usable_w, draw)

    # Calculate line height
    sample_bbox = draw.textbbox((0, 0), "Ay", font=blurb_font)
    line_height = int((sample_bbox[3] - sample_bbox[1]) * 1.5)

    # Center blurb vertically in its area
    total_blurb_height = len(blurb_lines) * line_height
    blurb_y = usable_top + max(0, (blurb_area_height - total_blurb_height) // 2)

    for line in blurb_lines:
        bbox = draw.textbbox((0, 0), line, font=blurb_font)
        line_w = bbox[2] - bbox[0]
        x = margin + (usable_w - line_w) // 2
        draw.text((x, blurb_y), line, fill=text_color, font=blurb_font)
        blurb_y += line_height

    # --- Author section (lower 35% of usable area) ---
    has_bio = bio_text and bio_text.strip()
    has_photo = author_photo_path and os.path.exists(author_photo_path)

    if not has_bio and not has_photo:
        # No author section needed — blurb gets the full space
        # Just draw barcode placeholder and return
        bc = dims["zones"]["barcode"]
        bc_x = bc["x"] - dims["zones"]["back_cover"]["x"]
        bc_y = bc["y"] - dims["zones"]["back_cover"]["y"]
        draw.rectangle(
            [bc_x, bc_y, bc_x + bc["width"], bc_y + bc["height"]],
            fill=(255, 255, 255),
            outline=(180, 180, 180),
            width=2,
        )
        placeholder_font = get_font(inches_to_px(0.08))
        draw.text(
            (bc_x + inches_to_px(0.3), bc_y + inches_to_px(0.4)),
            "BARCODE ZONE\n(KDP adds this automatically)",
            fill=(180, 180, 180),
            font=placeholder_font,
        )
        return back

    author_section_top = usable_top + blurb_area_height + inches_to_px(0.2)
    author_section_height = usable_bottom - author_section_top

    bio_font_size = inches_to_px(0.11)  # ~11pt
    if custom_font_path:
        try:
            bio_font = ImageFont.truetype(custom_font_path, bio_font_size)
        except Exception:
            bio_font = get_font(bio_font_size)
    else:
        bio_font = get_font(bio_font_size)

    if has_photo:
        # Photo on left, bio on right
        photo_size = min(inches_to_px(1.5), author_section_height)
        photo = Image.open(author_photo_path)
        photo = photo.convert("RGB")

        # Crop to square
        min_dim = min(photo.width, photo.height)
        left = (photo.width - min_dim) // 2
        top = (photo.height - min_dim) // 2
        photo = photo.crop((left, top, left + min_dim, top + min_dim))
        photo = photo.resize((photo_size, photo_size), Image.LANCZOS)

        photo_x = margin
        photo_y = author_section_top
        back.paste(photo, (photo_x, photo_y))

        # Bio text to the right of photo
        bio_x = photo_x + photo_size + inches_to_px(0.2)
        bio_max_w = usable_w - photo_size - inches_to_px(0.2)
        bio_lines = wrap_text(bio_text, bio_font, bio_max_w, draw)

        bio_line_bbox = draw.textbbox((0, 0), "Ay", font=bio_font)
        bio_line_h = int((bio_line_bbox[3] - bio_line_bbox[1]) * 1.4)

        bio_y = author_section_top
        for line in bio_lines:
            if bio_y + bio_line_h > usable_bottom:
                break
            draw.text((bio_x, bio_y), line, fill=text_color, font=bio_font)
            bio_y += bio_line_h
    else:
        # No photo — just centered bio
        bio_lines = wrap_text(bio_text, bio_font, usable_w, draw)
        bio_line_bbox = draw.textbbox((0, 0), "Ay", font=bio_font)
        bio_line_h = int((bio_line_bbox[3] - bio_line_bbox[1]) * 1.4)

        bio_y = author_section_top
        for line in bio_lines:
            if bio_y + bio_line_h > usable_bottom:
                break
            bbox = draw.textbbox((0, 0), line, font=bio_font)
            line_w = bbox[2] - bbox[0]
            x = margin + (usable_w - line_w) // 2
            draw.text((x, bio_y), line, fill=text_color, font=bio_font)
            bio_y += bio_line_h

    # --- Draw barcode placeholder ---
    bc = dims["zones"]["barcode"]
    bc_x = bc["x"] - dims["zones"]["back_cover"]["x"]
    bc_y = bc["y"] - dims["zones"]["back_cover"]["y"]
    draw.rectangle(
        [bc_x, bc_y, bc_x + bc["width"], bc_y + bc["height"]],
        fill=(255, 255, 255),
        outline=(180, 180, 180),
        width=2,
    )
    placeholder_font = get_font(inches_to_px(0.08))
    draw.text(
        (bc_x + inches_to_px(0.3), bc_y + inches_to_px(0.4)),
        "BARCODE ZONE\n(KDP adds this automatically)",
        fill=(180, 180, 180),
        font=placeholder_font,
    )

    return back


def compose_spine(dims, title, author_name, bg_color=(255, 255, 255),
                  text_color=(30, 30, 30), custom_font_path=None):
    """
    Compose the spine panel with title and author name.
    Text is rotated 90° clockwise (reads top-to-bottom when book is upright with front facing right).
    """
    check_pil()

    zone = dims["zones"]["spine"]
    w, h = zone["width"], zone["height"]
    margin = inches_to_px(SPINE_TEXT_MARGIN)

    spine = Image.new("RGB", (w, h), bg_color)

    if not dims["can_have_spine_text"]:
        # Too few pages for spine text — return blank
        return spine

    # Spine text is rotated: we compose it horizontally then rotate
    # Available width for text = spine height (since text runs along the length)
    text_length = h - (2 * inches_to_px(SAFE_MARGIN))
    text_max_height = w - (2 * margin)

    # Font size proportional to spine width, but capped
    font_size = min(int(text_max_height * 0.55), inches_to_px(0.12))
    if custom_font_path:
        try:
            title_font = ImageFont.truetype(custom_font_path, font_size)
        except Exception:
            title_font = get_font(font_size, bold=True)
    else:
        title_font = get_font(font_size, bold=True)

    author_font_size = int(font_size * 0.75)
    author_font = get_font(author_font_size)

    # Create a horizontal text image, then rotate
    # Layout: TITLE ———— AUTHOR NAME
    text_img = Image.new("RGB", (text_length, text_max_height), bg_color)
    text_draw = ImageDraw.Draw(text_img)

    # Measure
    title_bbox = text_draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    title_h = title_bbox[3] - title_bbox[1]

    author_bbox = text_draw.textbbox((0, 0), author_name, font=author_font)
    author_w = author_bbox[2] - author_bbox[0]
    author_h = author_bbox[3] - author_bbox[1]

    spacer = inches_to_px(0.3)

    # Center vertically
    total_content = title_w + spacer + author_w
    start_x = max(0, (text_length - total_content) // 2)

    title_y = (text_max_height - title_h) // 2
    author_y = (text_max_height - author_h) // 2

    text_draw.text((start_x, title_y), title, fill=text_color, font=title_font)
    text_draw.text((start_x + title_w + spacer, author_y), author_name, fill=text_color, font=author_font)

    # Rotate 90° clockwise (top of text = right side of spine = front cover side)
    rotated = text_img.rotate(-90, expand=True)

    # Center on spine
    paste_x = (w - rotated.width) // 2
    paste_y = (h - rotated.height) // 2
    spine.paste(rotated, (paste_x, paste_y))

    return spine


def compose_full_wrap(dims, front_cover_path, blurb_text, bio_text,
                      title, author_name, author_photo_path=None,
                      bg_color=(255, 255, 255), text_color=(30, 30, 30),
                      custom_font_path=None, output_dir=None):
    """
    Compose the full print cover wrap.

    Assembles: [BLEED][BACK COVER][SPINE][FRONT COVER][BLEED]
    """
    check_pil()

    full_w = dims["full_width_px"]
    full_h = dims["full_height_px"]

    # Create the full canvas
    canvas = Image.new("RGB", (full_w, full_h), bg_color)

    # --- Front cover ---
    front = Image.open(front_cover_path).convert("RGB")
    front_zone = dims["zones"]["front_cover"]
    # Resize front cover to fit the zone exactly (with bleed extension)
    front_with_bleed_w = front_zone["width"] + inches_to_px(BLEED)  # right bleed
    front_with_bleed_h = front_zone["height"] + (2 * inches_to_px(BLEED))  # top+bottom bleed

    # Scale front cover to fill the zone
    front_resized = front.resize((front_with_bleed_w, front_with_bleed_h), Image.LANCZOS)
    canvas.paste(front_resized, (front_zone["x"], 0))

    # --- Back cover ---
    back = compose_back_cover(
        dims, blurb_text, bio_text,
        author_photo_path=author_photo_path,
        bg_color=bg_color, text_color=text_color,
        custom_font_path=custom_font_path,
    )
    back_zone = dims["zones"]["back_cover"]
    canvas.paste(back, (back_zone["x"], back_zone["y"]))

    # Fill back cover bleed (left edge)
    # Extend the back cover's left edge color into the bleed area
    bleed_px = inches_to_px(BLEED)
    bleed_strip = back.crop((0, 0, 1, back.height))
    bleed_strip = bleed_strip.resize((bleed_px, back.height), Image.LANCZOS)
    canvas.paste(bleed_strip, (0, back_zone["y"]))

    # Fill top and bottom bleed for back cover
    top_strip = back.crop((0, 0, back.width, 1))
    top_strip = top_strip.resize((back.width, bleed_px), Image.LANCZOS)
    canvas.paste(top_strip, (back_zone["x"], 0))

    bottom_strip = back.crop((0, back.height - 1, back.width, back.height))
    bottom_strip = bottom_strip.resize((back.width, bleed_px), Image.LANCZOS)
    canvas.paste(bottom_strip, (back_zone["x"], back_zone["y"] + back_zone["height"]))

    # --- Spine ---
    spine = compose_spine(
        dims, title, author_name,
        bg_color=bg_color, text_color=text_color,
        custom_font_path=custom_font_path,
    )
    spine_zone = dims["zones"]["spine"]
    canvas.paste(spine, (spine_zone["x"], spine_zone["y"]))

    # Fill spine top/bottom bleed
    spine_top = spine.crop((0, 0, spine.width, 1))
    spine_top = spine_top.resize((spine.width, bleed_px), Image.LANCZOS)
    canvas.paste(spine_top, (spine_zone["x"], 0))

    spine_bottom = spine.crop((0, spine.height - 1, spine.width, spine.height))
    spine_bottom = spine_bottom.resize((spine.width, bleed_px), Image.LANCZOS)
    canvas.paste(spine_bottom, (spine_zone["x"], spine_zone["y"] + spine_zone["height"]))

    # --- Save ---
    out = Path(output_dir or ".")
    out.mkdir(parents=True, exist_ok=True)

    # Save as PNG (lossless)
    png_path = out / "print_cover_wrap.png"
    canvas.save(png_path, dpi=(DPI, DPI))
    print(f"Saved PNG: {png_path} ({full_w}x{full_h}px, {DPI} DPI)")

    # Save as PDF
    pdf_path = out / "print_cover_wrap.pdf"
    canvas.save(pdf_path, "PDF", resolution=DPI)
    print(f"Saved PDF: {pdf_path}")

    # Save dimensions metadata
    meta_path = out / "print_cover_metadata.json"
    meta = {
        "dimensions": {
            "full_width_inches": dims["full_width_inches"],
            "full_height_inches": dims["full_height_inches"],
            "full_width_px": full_w,
            "full_height_px": full_h,
            "trim_width": dims["trim_width"],
            "trim_height": dims["trim_height"],
            "spine_width_inches": round(dims["spine_width_inches"] if "spine_width_inches" in dims else calculate_spine_width(dims["page_count"], dims["paper_type"]), 4),
            "page_count": dims["page_count"],
            "paper_type": dims["paper_type"],
            "dpi": DPI,
        },
        "content": {
            "title": title,
            "author": author_name,
            "has_author_photo": author_photo_path is not None,
            "has_spine_text": dims["can_have_spine_text"],
        },
        "files": {
            "png": str(png_path),
            "pdf": str(pdf_path),
            "front_cover_source": str(front_cover_path),
        },
    }
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"Saved metadata: {meta_path}")

    return str(png_path), str(pdf_path)


def main():
    parser = argparse.ArgumentParser(description="Print Cover Wrap Compositor")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # --- parse-template ---
    parse_p = subparsers.add_parser("parse-template", help="Parse a KDP template image for dimensions")
    parse_p.add_argument("template", help="Path to KDP template PNG/PDF")

    # --- calculate ---
    calc_p = subparsers.add_parser("calculate", help="Calculate full cover dimensions from trim size + page count")
    calc_p.add_argument("--trim-width", type=float, required=True, help="Trim width in inches (e.g., 6)")
    calc_p.add_argument("--trim-height", type=float, required=True, help="Trim height in inches (e.g., 9)")
    calc_p.add_argument("--pages", type=int, required=True, help="Total page count")
    calc_p.add_argument("--paper", choices=["white", "cream"], default="white", help="Paper type")

    # --- compose ---
    comp_p = subparsers.add_parser("compose", help="Compose the full print cover wrap")
    comp_p.add_argument("--trim-width", type=float, required=True, help="Trim width in inches")
    comp_p.add_argument("--trim-height", type=float, required=True, help="Trim height in inches")
    comp_p.add_argument("--pages", type=int, required=True, help="Total page count")
    comp_p.add_argument("--paper", choices=["white", "cream"], default="white", help="Paper type")
    comp_p.add_argument("--front", required=True, help="Path to front cover image")
    comp_p.add_argument("--title", required=True, help="Book title (for spine)")
    comp_p.add_argument("--author", required=True, help="Author name (for spine)")
    comp_p.add_argument("--blurb", required=True, help="Back cover blurb text")
    comp_p.add_argument("--bio", default="", help="Author bio text (optional)")
    comp_p.add_argument("--author-photo", help="Path to author photo (optional)")
    comp_p.add_argument("--bg-color", default="255,255,255", help="Background RGB, e.g., '255,248,240'")
    comp_p.add_argument("--text-color", default="30,30,30", help="Text RGB, e.g., '30,30,30'")
    comp_p.add_argument("--font", help="Path to custom TTF font file")
    comp_p.add_argument("--output", "-o", default="./output/print/", help="Output directory")

    # --- template-overlay ---
    overlay_p = subparsers.add_parser("template-overlay", help="Overlay KDP template guides on composed wrap for verification")
    overlay_p.add_argument("--wrap", required=True, help="Path to composed wrap image")
    overlay_p.add_argument("--template", required=True, help="Path to KDP template PNG")
    overlay_p.add_argument("--output", "-o", help="Output path for overlay image")

    args = parser.parse_args()

    if args.command == "parse-template":
        parse_template_image(args.template)

    elif args.command == "calculate":
        dims = calculate_full_cover_dimensions(
            args.trim_width, args.trim_height, args.pages, args.paper
        )
        print(json.dumps(dims, indent=2))

    elif args.command == "compose":
        bg = tuple(int(x) for x in args.bg_color.split(","))
        tc = tuple(int(x) for x in args.text_color.split(","))

        dims = calculate_full_cover_dimensions(
            args.trim_width, args.trim_height, args.pages, args.paper
        )

        compose_full_wrap(
            dims=dims,
            front_cover_path=args.front,
            blurb_text=args.blurb,
            bio_text=args.bio,
            title=args.title,
            author_name=args.author,
            author_photo_path=args.author_photo,
            bg_color=bg,
            text_color=tc,
            custom_font_path=args.font,
            output_dir=args.output,
        )

    elif args.command == "template-overlay":
        check_pil()
        wrap = Image.open(args.wrap).convert("RGBA")
        template = Image.open(args.template).convert("RGBA")

        # Resize template to match wrap if needed
        if template.size != wrap.size:
            template = template.resize(wrap.size, Image.LANCZOS)

        # Blend
        overlay = Image.blend(wrap, template, alpha=0.3)
        out_path = args.output or str(Path(args.wrap).parent / "template_overlay.png")
        overlay.save(out_path)
        print(f"Saved template overlay: {out_path}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
