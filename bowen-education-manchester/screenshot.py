#!/usr/bin/env python3
"""
Simple screenshot tool using Selenium
"""
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def take_screenshot(url, output_path="screenshot.png", width=1920, height=1080):
    """Take a screenshot of a webpage."""
    print(f"Taking screenshot of {url}...")

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'--window-size={width},{height}')

    # Initialize driver
    try:
        driver = webdriver.Chrome(options=chrome_options)

        # Load page
        driver.get(url)

        # Wait for page to load
        time.sleep(2)

        # Take screenshot
        driver.save_screenshot(output_path)
        print(f"Screenshot saved to {output_path}")

        # Clean up
        driver.quit()
        return True

    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python screenshot.py <url> [output_path]")
        sys.exit(1)

    url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "screenshot.png"

    success = take_screenshot(url, output_path)
    sys.exit(0 if success else 1)
