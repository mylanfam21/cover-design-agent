#!/usr/bin/env python3
"""
Nano Banana API Wrapper
Calls Google AI Studio's Gemini image generation (Nano Banana) via REST API.

Usage:
    python nano_banana_api.py --prompt "Your cover prompt" --output ./output/
    python nano_banana_api.py --prompt "Your cover prompt" --output ./output/ --model gemini-2.5-flash-image
    python nano_banana_api.py --prompt "Your cover prompt" --output ./output/ --count 4

Environment:
    GOOGLE_AI_API_KEY - Your Google AI Studio API key (required)
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path
from urllib import request, error


# Available models (update as Google releases new ones)
MODELS = {
    "nano-banana-pro": "gemini-3-pro-image-preview",
    "nano-banana-flash": "gemini-2.5-flash-image",
    "imagen4": "imagen-4.0-generate-001",
    "imagen4-fast": "imagen-4.0-fast-generate-001",
    "imagen4-ultra": "imagen-4.0-ultra-generate-001",
}

DEFAULT_MODEL = "gemini-2.5-flash-image"

API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"


def get_api_key():
    """Get API key from environment variable."""
    key = os.environ.get("GOOGLE_AI_API_KEY")
    if not key:
        print("ERROR: GOOGLE_AI_API_KEY environment variable not set.")
        print("Set it with: export GOOGLE_AI_API_KEY=your_key_here")
        sys.exit(1)
    return key


def generate_with_gemini(prompt, model=DEFAULT_MODEL, api_key=None):
    """
    Generate images using Gemini's native image generation (generateContent endpoint).
    Works with gemini-2.5-flash-image, gemini-3-pro-image-preview, etc.
    """
    url = f"{API_BASE}/{model}:generateContent"

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "temperature": 1.0,
        },
    }

    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers=headers, method="POST")

    try:
        with request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result
    except error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"API Error {e.code}: {error_body}")
        return None
    except error.URLError as e:
        print(f"Connection Error: {e.reason}")
        return None


def generate_with_imagen(prompt, model="imagen-4.0-generate-001", count=4,
                          aspect_ratio="3:4", api_key=None):
    """
    Generate images using Imagen's dedicated endpoint (:predict).
    Works with imagen-4.0-generate-001, imagen-4.0-fast-generate-001, etc.
    """
    url = f"{API_BASE}/{model}:predict"

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    }

    payload = {
        "instances": [
            {"prompt": prompt}
        ],
        "parameters": {
            "sampleCount": min(count, 4),
            "aspectRatio": aspect_ratio,
        },
    }

    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers=headers, method="POST")

    try:
        with request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result
    except error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"API Error {e.code}: {error_body}")
        return None
    except error.URLError as e:
        print(f"Connection Error: {e.reason}")
        return None


def extract_images_gemini(response):
    """Extract base64 image data from Gemini generateContent response."""
    images = []
    if not response or "candidates" not in response:
        return images

    for candidate in response["candidates"]:
        if "content" not in candidate:
            continue
        for part in candidate["content"].get("parts", []):
            if "inlineData" in part:
                images.append({
                    "data": part["inlineData"]["data"],
                    "mime_type": part["inlineData"]["mimeType"],
                })
            elif "text" in part:
                # Gemini may return text alongside images
                print(f"Model note: {part['text'][:200]}")
    return images


def extract_images_imagen(response):
    """Extract base64 image data from Imagen predict response."""
    images = []
    if not response or "predictions" not in response:
        return images

    for prediction in response["predictions"]:
        if "bytesBase64Encoded" in prediction:
            images.append({
                "data": prediction["bytesBase64Encoded"],
                "mime_type": prediction.get("mimeType", "image/png"),
            })
    return images


def save_images(images, output_dir, prefix="cover"):
    """Save base64 images to files."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    saved = []
    timestamp = int(time.time())

    for i, img in enumerate(images):
        ext = "png" if "png" in img["mime_type"] else "jpg"
        filename = f"{prefix}_{timestamp}_{i+1}.{ext}"
        filepath = output_path / filename

        with open(filepath, "wb") as f:
            f.write(base64.b64decode(img["data"]))

        saved.append(str(filepath))
        print(f"Saved: {filepath}")

    return saved


def generate_cover(prompt, output_dir="./output", model=DEFAULT_MODEL,
                    count=4, aspect_ratio="3:4", prefix="cover"):
    """
    Main generation function. Detects model type and uses appropriate endpoint.

    Args:
        prompt: The cover generation prompt
        output_dir: Directory to save generated images
        model: Model name or alias (see MODELS dict)
        count: Number of images to generate (Imagen only, max 4)
        aspect_ratio: Aspect ratio (Imagen only)
        prefix: Filename prefix for saved images

    Returns:
        List of saved file paths
    """
    api_key = get_api_key()

    # Resolve model aliases
    if model in MODELS:
        model = MODELS[model]

    print(f"Model: {model}")
    print(f"Prompt: {prompt[:100]}...")
    print(f"Output: {output_dir}")
    print()

    # Determine which endpoint to use based on model name
    is_imagen = model.startswith("imagen")

    if is_imagen:
        print(f"Using Imagen endpoint (:predict), generating {count} images...")
        response = generate_with_imagen(
            prompt, model=model, count=count,
            aspect_ratio=aspect_ratio, api_key=api_key
        )
        images = extract_images_imagen(response)
    else:
        print("Using Gemini native endpoint (:generateContent)...")
        # Gemini generates one image per call, so loop for multiple
        images = []
        for i in range(count):
            print(f"  Generating image {i+1}/{count}...")
            response = generate_with_gemini(prompt, model=model, api_key=api_key)
            batch = extract_images_gemini(response)
            images.extend(batch)
            if i < count - 1:
                time.sleep(1)  # Brief pause between calls

    if not images:
        print("ERROR: No images were generated. Check the API response above.")
        return []

    print(f"\nGenerated {len(images)} image(s). Saving...")
    saved = save_images(images, output_dir, prefix=prefix)
    print(f"Done. {len(saved)} image(s) saved to {output_dir}")
    return saved


def main():
    parser = argparse.ArgumentParser(description="Generate book covers via Nano Banana API")
    parser.add_argument("--prompt", "-p", required=True, help="The cover generation prompt")
    parser.add_argument("--output", "-o", default="./output", help="Output directory")
    parser.add_argument("--model", "-m", default=DEFAULT_MODEL,
                        help=f"Model to use. Aliases: {', '.join(MODELS.keys())}. "
                             f"Or use full model name. Default: {DEFAULT_MODEL}")
    parser.add_argument("--count", "-c", type=int, default=4,
                        help="Number of images to generate (default: 4)")
    parser.add_argument("--aspect-ratio", "-a", default="3:4",
                        help="Aspect ratio for Imagen models (default: 3:4 for book covers)")
    parser.add_argument("--prefix", default="cover",
                        help="Filename prefix (default: cover)")

    args = parser.parse_args()
    generate_cover(
        prompt=args.prompt,
        output_dir=args.output,
        model=args.model,
        count=args.count,
        aspect_ratio=args.aspect_ratio,
        prefix=args.prefix,
    )


if __name__ == "__main__":
    main()
