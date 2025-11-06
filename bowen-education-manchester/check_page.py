#!/usr/bin/env python3
"""
检查页面完整状态，关闭搜索覆盖层
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

os.environ['DISPLAY'] = ':99'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://192.168.31.205:8002/')
    time.sleep(3)

    # 检查是否有搜索覆盖层
    try:
        search_overlay = driver.find_element(By.ID, 'search-overlay')
        if not search_overlay.get_attribute('hidden'):
            print("⚠ 搜索覆盖层是打开的")
            # 尝试关闭它
            close_btn = driver.find_element(By.CSS_SELECTOR, '[data-action="close-search"]')
            if close_btn:
                close_btn.click()
                time.sleep(1)
                print("✓ 已关闭搜索覆盖层")
    except:
        print("✓ 搜索覆盖层正常")

    # 获取页面信息
    print(f"\n页面标题: {driver.title}")

    # 检查body背景色
    body = driver.find_element(By.TAG_NAME, 'body')
    bg_color = body.value_of_css_property('background-color')
    print(f"Body背景色: {bg_color}")

    # 检查主要区域
    try:
        hero = driver.find_element(By.CLASS_NAME, 'hero')
        print(f"✓ Hero区域存在")
        hero_display = hero.value_of_css_property('display')
        print(f"  Display: {hero_display}")
    except:
        print("✗ Hero区域不存在")

    # 检查sections
    sections = driver.find_elements(By.CLASS_NAME, 'section')
    print(f"\n找到 {len(sections)} 个section")

    # 截图
    driver.save_screenshot('homepage_full_check.png')
    print("\n✓ 截图已保存: homepage_full_check.png")

    driver.quit()

except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
