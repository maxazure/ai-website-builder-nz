#!/usr/bin/env python3
"""
使用 Selenium 截取网站首页
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import sys

# Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

# 设置显示
import os
os.environ['DISPLAY'] = ':99'

try:
    # 初始化 WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # 访问页面
    print("正在访问页面...")
    driver.get('http://192.168.31.205:8002/')

    # 等待页面加载
    time.sleep(3)

    # 获取页面标题
    print(f"页面标题: {driver.title}")

    # 截图
    screenshot_path = 'homepage_screenshot.png'
    driver.save_screenshot(screenshot_path)
    print(f"截图已保存: {screenshot_path}")

    # 检查导航栏
    nav_links = driver.find_elements('css selector', '.nav-link')
    print(f"\n找到 {len(nav_links)} 个导航链接")

    for i, link in enumerate(nav_links[:5], 1):
        classes = link.get_attribute('class')
        text = link.text.strip()
        print(f"{i}. {text}: class='{classes}'")

    driver.quit()
    print("\n✓ 截图完成！")

except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
