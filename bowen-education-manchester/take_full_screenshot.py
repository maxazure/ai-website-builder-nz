#!/usr/bin/env python3
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

os.environ['DISPLAY'] = ':99'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://192.168.31.205:8002')
time.sleep(3)

# Get full page height
total_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(1920, total_height)
time.sleep(1)

driver.save_screenshot('full_page_screenshot.png')
print(f"Full page screenshot saved! Height: {total_height}px")
driver.quit()
