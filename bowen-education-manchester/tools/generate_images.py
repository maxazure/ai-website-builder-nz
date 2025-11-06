#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Image Generation Tool using Zhipu AI CogView-3-Flash
智谱AI CogView-3-Flash图片生成工具
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Dict

import requests


class ZhipuImageGenerator:
    """Zhipu AI CogView-3 Image Generator"""

    API_URL = "https://open.bigmodel.cn/api/paas/v4/images/generations"

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("ZHIPU_KEY environment variable is required")
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def generate_image(self, prompt: str, filename: str, output_dir: Path) -> Dict:
        """Generate a single image"""
        output_path = output_dir / filename

        # Skip if file already exists
        if output_path.exists():
            return {
                "success": True,
                "filename": filename,
                "message": "Skipped (already exists)",
                "skipped": True
            }

        payload = {
            "model": "cogview-3-flash",
            "prompt": prompt,
            "size": "1024x1024"
        }

        try:
            response = requests.post(
                self.API_URL,
                headers=self.headers,
                json=payload,
                timeout=60
            )

            if response.status_code != 200:
                return {
                    "success": False,
                    "filename": filename,
                    "message": f"API error: {response.status_code}"
                }

            result = response.json()

            if "data" not in result or not result["data"]:
                return {
                    "success": False,
                    "filename": filename,
                    "message": "No image data in response"
                }

            image_url = result["data"][0]["url"]

            # Download image
            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()

            # Save image
            output_dir.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(img_response.content)

            return {
                "success": True,
                "filename": filename,
                "message": "Generated successfully",
                "path": str(output_path)
            }

        except Exception as e:
            return {
                "success": False,
                "filename": filename,
                "message": f"Error: {str(e)}"
            }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    api_key = os.getenv("ZHIPU_KEY")
    if not api_key:
        print("Error: ZHIPU_KEY not set")
        sys.exit(1)

    # Load config
    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    output_dir = Path(config["output_dir"])
    images = config["images"]

    print(f"Total images: {len(images)}")

    generator = ZhipuImageGenerator(api_key)

    # Sort by priority
    priority_order = {"high": 0, "medium": 1, "low": 2}
    sorted_images = sorted(
        images,
        key=lambda x: priority_order.get(x.get("priority", "medium"), 1)
    )

    results = {"total": len(images), "success": 0, "failed": 0, "skipped": 0}

    for i, img_config in enumerate(sorted_images, 1):
        filename = img_config["filename"]
        prompt = img_config["prompt"]
        priority = img_config.get("priority", "medium")

        print(f"[{i}/{len(images)}] {filename} ({priority})")

        result = generator.generate_image(prompt, filename, output_dir)

        if result["success"]:
            if result.get("skipped"):
                results["skipped"] += 1
                print(f"  Skipped")
            else:
                results["success"] += 1
                print(f"  Success")
        else:
            results["failed"] += 1
            print(f"  Failed: {result['message']}")

        # Rate limiting
        if i < len(images) and not result.get("skipped"):
            time.sleep(2)

    print(f"\nSummary: {results['success']} success, {results['skipped']} skipped, {results['failed']} failed")


if __name__ == "__main__":
    main()
