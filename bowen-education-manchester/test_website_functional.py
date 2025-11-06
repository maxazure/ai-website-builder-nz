#!/usr/bin/env python3
"""
网站功能测试脚本 - Bowen Education Group
自动化测试所有关键页面和功能
"""

import sys
import requests
from datetime import datetime
from pathlib import Path

# ANSI颜色代码
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

# 测试结果统计
test_results = {
    "passed": 0,
    "failed": 0,
    "warnings": 0,
    "total": 0
}

BASE_URL = "http://192.168.31.205:8002"

def print_header(text):
    """打印测试标题"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'=' * 70}")
    print(f"{text}")
    print(f"{'=' * 70}{Colors.END}\n")

def test_pass(message):
    """测试通过"""
    test_results["passed"] += 1
    test_results["total"] += 1
    print(f"{Colors.GREEN}✓{Colors.END} {message}")

def test_fail(message):
    """测试失败"""
    test_results["failed"] += 1
    test_results["total"] += 1
    print(f"{Colors.RED}✗{Colors.END} {message}")

def test_warning(message):
    """测试警告"""
    test_results["warnings"] += 1
    print(f"{Colors.YELLOW}⚠{Colors.END} {message}")

def test_page_accessibility():
    """测试页面可访问性"""
    print_header("测试1: 页面可访问性测试")

    pages = [
        ("/", "首页"),
        ("/about", "关于页"),
        ("/contact", "联系页"),
    ]

    for path, name in pages:
        try:
            url = f"{BASE_URL}{path}"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                test_pass(f"{name} ({path}) - HTTP 200 OK")
            else:
                test_fail(f"{name} ({path}) - HTTP {response.status_code}")

        except requests.exceptions.RequestException as e:
            test_fail(f"{name} ({path}) - 无法访问: {str(e)}")

def test_page_content():
    """测试页面内容"""
    print_header("测试2: 页面内容完整性测试")

    # 测试首页内容
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        content = response.text

        required_elements = [
            ("<!DOCTYPE html>", "HTML5 DOCTYPE"),
            ("<title>", "页面标题"),
            ("Bowen Education Group", "公司名称"),
            ("博文集团", "中文名称"),
            ("<section", "页面sections"),
            ("</footer>", "页脚"),
        ]

        for element, description in required_elements:
            if element in content:
                test_pass(f"首页包含: {description}")
            else:
                test_fail(f"首页缺少: {description}")

    except Exception as e:
        test_fail(f"首页内容检查失败: {str(e)}")

    # 测试关于页内容
    try:
        response = requests.get(f"{BASE_URL}/about", timeout=5)
        content = response.text

        required_elements = [
            ("About Us", "英文标题"),
            ("关于我们", "中文标题"),
            ("Mission", "使命部分"),
            ("Vision", "愿景部分"),
            ("Our Team", "团队部分"),
        ]

        for element, description in required_elements:
            if element in content:
                test_pass(f"关于页包含: {description}")
            else:
                test_fail(f"关于页缺少: {description}")

    except Exception as e:
        test_fail(f"关于页内容检查失败: {str(e)}")

    # 测试联系页内容
    try:
        response = requests.get(f"{BASE_URL}/contact", timeout=5)
        content = response.text

        required_elements = [
            ("Contact Us", "英文标题"),
            ("联系我们", "中文标题"),
            ("<form", "联系表单"),
            ("0161 969 3071", "电话号码"),
            ("Sale, Manchester", "地址"),
        ]

        for element, description in required_elements:
            if element in content:
                test_pass(f"联系页包含: {description}")
            else:
                test_fail(f"联系页缺少: {description}")

    except Exception as e:
        test_fail(f"联系页内容检查失败: {str(e)}")

def test_bilingual_support():
    """测试双语支持"""
    print_header("测试3: 双语内容支持测试")

    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        content = response.text

        # 检查中文字符
        chinese_chars = ["博文", "中文", "教育", "学校", "关于", "联系"]
        chinese_count = sum(1 for char in chinese_chars if char in content)

        if chinese_count >= 4:
            test_pass(f"首页包含中文内容 ({chinese_count}/6 关键词)")
        else:
            test_warning(f"首页中文内容较少 ({chinese_count}/6 关键词)")

        # 检查字体支持
        if "Noto Sans SC" in content or "font-chinese" in content:
            test_pass("页面包含中文字体支持")
        else:
            test_warning("页面可能缺少中文字体定义")

    except Exception as e:
        test_fail(f"双语支持检查失败: {str(e)}")

def test_static_resources():
    """测试静态资源加载"""
    print_header("测试4: 静态资源加载测试")

    resources = [
        ("/static/css/main.css", "主CSS样式表"),
        ("/static/images/hero-chinese-school.jpg", "首页Hero图片"),
        ("/static/images/course-gcse-chinese.jpg", "课程图片"),
    ]

    for path, name in resources:
        try:
            url = f"{BASE_URL}{path}"
            response = requests.head(url, timeout=5)

            if response.status_code == 200:
                test_pass(f"{name} - 可访问")
            elif response.status_code == 404:
                test_fail(f"{name} - 404 Not Found")
            else:
                test_warning(f"{name} - HTTP {response.status_code}")

        except requests.exceptions.RequestException as e:
            test_fail(f"{name} - 无法访问: {str(e)}")

def test_responsive_headers():
    """测试响应头"""
    print_header("测试5: HTTP响应头测试")

    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        headers = response.headers

        if 'text/html' in headers.get('content-type', ''):
            test_pass("Content-Type 正确 (text/html)")
        else:
            test_fail(f"Content-Type 错误: {headers.get('content-type')}")

        if headers.get('server'):
            test_pass(f"服务器类型: {headers.get('server')}")

        content_length = headers.get('content-length', 'unknown')
        if content_length != 'unknown':
            size_kb = int(content_length) / 1024
            if size_kb < 500:
                test_pass(f"页面大小合理: {size_kb:.2f} KB")
            else:
                test_warning(f"页面较大: {size_kb:.2f} KB")

    except Exception as e:
        test_fail(f"响应头检查失败: {str(e)}")

def test_meta_tags():
    """测试 meta 标签"""
    print_header("测试6: SEO Meta标签测试")

    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        content = response.text

        meta_tags = [
            ('<meta name="description"', "description meta标签"),
            ('<meta name="keywords"', "keywords meta标签"),
            ('<meta property="og:', "Open Graph标签"),
            ('<meta name="twitter:', "Twitter Card标签"),
            ('<meta name="viewport"', "viewport meta标签"),
        ]

        for tag, description in meta_tags:
            if tag in content:
                test_pass(f"包含 {description}")
            else:
                test_warning(f"缺少 {description}")

    except Exception as e:
        test_fail(f"Meta标签检查失败: {str(e)}")

def test_navigation():
    """测试导航链接"""
    print_header("测试7: 导航系统测试")

    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        content = response.text

        # 检查导航链接
        nav_links = [
            'href="/about"',
            'href="/contact"',
        ]

        for link in nav_links:
            if link in content:
                test_pass(f"导航包含: {link}")
            else:
                test_warning(f"导航可能缺少: {link}")

        # 检查footer链接
        if '<footer' in content:
            test_pass("页面包含footer")
        else:
            test_fail("页面缺少footer")

    except Exception as e:
        test_fail(f"导航测试失败: {str(e)}")

def test_forms():
    """测试表单"""
    print_header("测试8: 表单功能测试")

    try:
        response = requests.get(f"{BASE_URL}/contact", timeout=5)
        content = response.text

        form_elements = [
            ('<form', "表单标签"),
            ('name="name"', "姓名字段"),
            ('name="email"', "邮箱字段"),
            ('name="message"', "留言字段"),
            ('type="submit"', "提交按钮"),
            ('action="/contact/submit"', "表单action"),
        ]

        for element, description in form_elements:
            if element in content:
                test_pass(f"表单包含: {description}")
            else:
                test_fail(f"表单缺少: {description}")

        # 测试表单提交（仅验证端点存在，不实际提交）
        test_warning("表单提交功能需要手动测试")

    except Exception as e:
        test_fail(f"表单测试失败: {str(e)}")

def test_performance():
    """测试性能"""
    print_header("测试9: 页面加载性能测试")

    pages = [
        ("/", "首页"),
        ("/about", "关于页"),
        ("/contact", "联系页"),
    ]

    for path, name in pages:
        try:
            url = f"{BASE_URL}{path}"
            import time
            start_time = time.time()
            response = requests.get(url, timeout=10)
            load_time = time.time() - start_time

            if load_time < 1.0:
                test_pass(f"{name} 加载时间: {load_time:.3f}秒 (优秀)")
            elif load_time < 3.0:
                test_pass(f"{name} 加载时间: {load_time:.3f}秒 (良好)")
            else:
                test_warning(f"{name} 加载时间: {load_time:.3f}秒 (较慢)")

        except Exception as e:
            test_fail(f"{name} 性能测试失败: {str(e)}")

def test_error_pages():
    """测试错误页面"""
    print_header("测试10: 错误处理测试")

    try:
        # 测试404页面
        response = requests.get(f"{BASE_URL}/nonexistent-page", timeout=5)
        if response.status_code == 404:
            test_pass("404错误页面正常返回")
            if "404" in response.text or "Not Found" in response.text:
                test_pass("404页面包含错误提示")
            else:
                test_warning("404页面可能缺少用户友好的错误提示")
        else:
            test_warning(f"不存在的页面返回: HTTP {response.status_code}")

    except Exception as e:
        test_fail(f"错误页面测试失败: {str(e)}")

def generate_test_report():
    """生成测试报告"""
    print_header("测试报告")

    total = test_results["total"]
    passed = test_results["passed"]
    failed = test_results["failed"]
    warnings = test_results["warnings"]

    success_rate = (passed / total * 100) if total > 0 else 0

    print(f"测试总数: {total}")
    print(f"{Colors.GREEN}通过: {passed}{Colors.END}")
    print(f"{Colors.RED}失败: {failed}{Colors.END}")
    print(f"{Colors.YELLOW}警告: {warnings}{Colors.END}")
    print(f"\n成功率: {Colors.BOLD}{success_rate:.1f}%{Colors.END}")

    if failed == 0:
        print(f"\n{Colors.GREEN}{Colors.BOLD}✓ 所有关键测试通过！{Colors.END}")
    elif failed < 5:
        print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠ 有少量测试失败，建议修复{Colors.END}")
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}✗ 多项测试失败，需要立即修复{Colors.END}")

    # 保存报告到文件
    report_path = Path("WEBSITE_TEST_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# 网站功能测试报告\n\n")
        f.write(f"**项目**: Bowen Education Group 博文集团网站\n")
        f.write(f"**测试时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**测试URL**: {BASE_URL}\n\n")
        f.write(f"## 测试结果摘要\n\n")
        f.write(f"- 测试总数: {total}\n")
        f.write(f"- ✓ 通过: {passed}\n")
        f.write(f"- ✗ 失败: {failed}\n")
        f.write(f"- ⚠ 警告: {warnings}\n")
        f.write(f"- 成功率: {success_rate:.1f}%\n\n")
        f.write(f"## 测试详情\n\n")
        f.write(f"详细测试结果请查看终端输出。\n\n")
        f.write(f"## 测试覆盖范围\n\n")
        f.write(f"1. ✓ 页面可访问性测试\n")
        f.write(f"2. ✓ 页面内容完整性测试\n")
        f.write(f"3. ✓ 双语内容支持测试\n")
        f.write(f"4. ✓ 静态资源加载测试\n")
        f.write(f"5. ✓ HTTP响应头测试\n")
        f.write(f"6. ✓ SEO Meta标签测试\n")
        f.write(f"7. ✓ 导航系统测试\n")
        f.write(f"8. ✓ 表单功能测试\n")
        f.write(f"9. ✓ 页面加载性能测试\n")
        f.write(f"10. ✓ 错误处理测试\n\n")

        if failed == 0:
            f.write(f"## 结论\n\n")
            f.write(f"✅ **所有关键功能测试通过**\n\n")
            f.write(f"网站已通过全面的功能测试，所有关键功能正常运行。\n")
        else:
            f.write(f"## 需要修复的问题\n\n")
            f.write(f"请查看上述测试失败的项目并进行修复。\n")

    print(f"\n{Colors.BLUE}测试报告已保存到: {report_path}{Colors.END}")

def main():
    """主函数"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("=" * 70)
    print("  Bowen Education Group 网站功能测试")
    print("  Website Functional Testing")
    print("=" * 70)
    print(f"{Colors.END}")
    print(f"测试URL: {BASE_URL}")
    print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # 执行所有测试
    test_page_accessibility()
    test_page_content()
    test_bilingual_support()
    test_static_resources()
    test_responsive_headers()
    test_meta_tags()
    test_navigation()
    test_forms()
    test_performance()
    test_error_pages()

    # 生成报告
    generate_test_report()

    # 返回退出码
    if test_results["failed"] > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
