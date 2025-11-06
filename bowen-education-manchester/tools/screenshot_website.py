#!/usr/bin/env python3
"""
Website Screenshot Tool
网站截图工具

Usage:
    python tools/screenshot_website.py <url> [output_file]

Example:
    python tools/screenshot_website.py http://localhost:8000
    python tools/screenshot_website.py http://192.168.31.205:8002 homepage.jpg
"""

import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from PIL import Image

def take_screenshot(url, output_file='screenshot.jpg', width=1920, height=1080, quality=85):
    """
    Take a screenshot of a website and compress to JPG

    Args:
        url: Website URL to screenshot
        output_file: Output filename (default: screenshot.jpg)
        width: Browser width in pixels (default: 1920)
        height: Browser height in pixels (default: 1080)
        quality: JPG quality 1-100 (default: 85)

    Returns:
        dict: Result with success status and message
    """
    # Set display for headless mode
    os.environ['DISPLAY'] = ':99'

    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument(f'--window-size={width},{height}')

    try:
        print(f"📸 Taking screenshot of: {url}")
        print(f"   Output: {output_file}")
        print(f"   Size: {width}x{height}")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to page
        driver.get(url)

        # Wait for page to load
        time.sleep(3)

        # Get page info
        title = driver.title
        print(f"   Title: {title}")

        # Check for overlays that might block content
        try:
            # Close search overlay if open
            search_overlay = driver.find_element(By.ID, 'search-overlay')
            if not search_overlay.get_attribute('hidden'):
                close_btn = driver.find_element(By.CSS_SELECTOR, '[data-action="close-search"]')
                close_btn.click()
                time.sleep(0.5)
                print("   ✓ Closed search overlay")
        except:
            pass

        try:
            # Close mobile menu if open
            mobile_menu = driver.find_element(By.ID, 'mobile-menu')
            if not mobile_menu.get_attribute('hidden'):
                toggle = driver.find_element(By.CSS_SELECTOR, '[data-action="toggle-mobile-menu"]')
                toggle.click()
                time.sleep(0.5)
                print("   ✓ Closed mobile menu")
        except:
            pass

        # Take screenshot to temporary PNG file
        temp_png = output_file.rsplit('.', 1)[0] + '_temp.png'
        driver.save_screenshot(temp_png)

        # Get page statistics
        try:
            nav_links = driver.find_elements(By.CSS_SELECTOR, '.nav-link')
            sections = driver.find_elements(By.CLASS_NAME, 'section')

            print(f"\n📊 Page Statistics:")
            print(f"   Navigation links: {len(nav_links)}")
            print(f"   Sections: {len(sections)}")
        except:
            pass

        driver.quit()

        # Compress to JPG
        try:
            # Ensure output file has .jpg extension
            if not output_file.lower().endswith(('.jpg', '.jpeg')):
                output_file = output_file.rsplit('.', 1)[0] + '.jpg'

            # Open PNG and convert to RGB (JPG doesn't support alpha channel)
            img = Image.open(temp_png)
            rgb_img = img.convert('RGB')

            # Get file sizes
            png_size = os.path.getsize(temp_png)

            # Save as JPG with compression
            rgb_img.save(output_file, 'JPEG', quality=quality, optimize=True)
            jpg_size = os.path.getsize(output_file)

            # Remove temporary PNG
            os.remove(temp_png)

            # Calculate compression ratio
            compression_ratio = (1 - jpg_size / png_size) * 100

            print(f"\n📦 Image Compression:")
            print(f"   Original PNG: {png_size / 1024:.1f} KB")
            print(f"   Compressed JPG: {jpg_size / 1024:.1f} KB")
            print(f"   Saved: {compression_ratio:.1f}%")
            print(f"   Quality: {quality}%")

        except Exception as e:
            print(f"\n⚠️  Compression warning: {str(e)}")
            # If compression fails, keep the PNG
            if os.path.exists(temp_png):
                os.rename(temp_png, output_file)

        print(f"\n✅ Screenshot saved successfully!")

        return {
            'success': True,
            'file': output_file,
            'title': title,
            'message': f'Screenshot saved to {output_file}'
        }

    except Exception as e:
        error_msg = f'Error taking screenshot: {str(e)}'
        print(f"\n❌ {error_msg}")
        import traceback
        traceback.print_exc()

        return {
            'success': False,
            'error': error_msg
        }


def main():
    """Main function for CLI usage"""
    if len(sys.argv) < 2:
        print("Usage: python tools/screenshot_website.py <url> [output_file]")
        print("\nExample:")
        print("  python tools/screenshot_website.py http://localhost:8000")
        print("  python tools/screenshot_website.py http://192.168.31.205:8002 homepage.jpg")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'screenshot.jpg'

    result = take_screenshot(url, output_file)

    if not result['success']:
        sys.exit(1)


if __name__ == '__main__':
    main()
