# -*- coding: utf-8 -*-
"""Create New Docms Site

用法:
    python -m cli.create_site --name my-company-site --dir ../sites/

这将创建一个新的站点目录，包含所有必要的文件和配置
"""

import argparse
import shutil
import sys
from pathlib import Path
from typing import Optional

import yaml


def create_site(
    site_name: str,
    target_dir: Optional[Path] = None,
    company_name: Optional[str] = None,
    company_description: Optional[str] = None,
) -> Path:
    """
    创建新的 Docms 站点

    Args:
        site_name: 站点名称（目录名）
        target_dir: 目标目录（默认为当前目录的父目录）
        company_name: 公司名称
        company_description: 公司描述

    Returns:
        创建的站点目录路径
    """
    # 确定目标目录
    if target_dir is None:
        target_dir = Path.cwd().parent / site_name
    else:
        target_dir = target_dir / site_name

    if target_dir.exists():
        print(f"[ERROR] 目录 {target_dir} 已存在")
        sys.exit(1)

    print(f">> 创建新站点: {site_name}")
    print(f">> 目标目录: {target_dir}")

    # 创建目录结构
    print("\n[1/7] 创建目录结构...")
    create_directory_structure(target_dir)

    # 复制核心代码
    print("\n[2/7] 复制核心代码...")
    copy_core_files(target_dir)

    # 创建配置文件
    print("\n[3/7] 创建配置文件...")
    create_config_file(
        target_dir,
        site_name=company_name or site_name,
        description=company_description or f"Website for {company_name or site_name}"
    )

    # 创建入口文件
    print("\n[4/7] 创建应用入口...")
    create_app_entry(target_dir, site_name)

    # 创建 requirements.txt
    print("\n[5/7] 创建依赖文件...")
    create_requirements(target_dir)

    # 创建基础模板
    print("\n[6/7] 创建基础模板...")
    create_base_templates(target_dir)

    # 创建 README
    print("\n[7/7] 创建 README...")
    create_readme(target_dir, site_name)

    print(f"\n[SUCCESS] 站点创建成功！")
    print(f"\n下一步:")
    print(f"1. cd {target_dir}")
    print(f"2. python -m venv venv")
    print(f"3. venv\\Scripts\\activate  (Windows) 或 source venv/bin/activate  (Linux/Mac)")
    print(f"4. pip install -r requirements.txt")
    print(f"5. python -m cli.generate_content  (使用 LLM 生成内容)")
    print(f"6. python app.py  (启动服务器)")

    return target_dir


def create_directory_structure(base_dir: Path):
    """创建目录结构"""
    dirs = [
        "instance",
        "instance/media",
        "instance/media/uploads",
        "templates",
        "templates/static",
        "templates/static/css",
        "templates/static/js",
        "templates/static/images",
        "templates/components",
        "migrations",
        "migrations/versions",
    ]

    for dir_path in dirs:
        (base_dir / dir_path).mkdir(parents=True, exist_ok=True)
        print(f"  [OK] {dir_path}")


def copy_core_files(target_dir: Path):
    """复制核心代码文件"""
    source_dir = Path(__file__).parent.parent  # docms-python 目录

    # 复制核心模块
    core_modules = ["app", "docms"]

    for module in core_modules:
        source = source_dir / module
        if source.exists():
            target = target_dir / module
            if source.is_dir():
                shutil.copytree(source, target, dirs_exist_ok=True)
                print(f"  [OK] 复制 {module}/ 目录")
            else:
                shutil.copy2(source, target)
                print(f"  [OK] 复制 {module}")

    # 复制 Alembic 配置
    alembic_ini = source_dir / "alembic.ini"
    if alembic_ini.exists():
        shutil.copy2(alembic_ini, target_dir / "alembic.ini")
        print(f"  [OK] 复制 alembic.ini")


def create_config_file(target_dir: Path, site_name: str, description: str):
    """创建站点配置文件"""
    config = {
        "site_name": site_name,
        "site_description": description,
        "site_url": "http://localhost:8000",
        "base_dir": ".",
        "template_dir": "./templates",
        "static_dir": "./templates/static",
        "media_dir": "./instance/media",
        "database_url": "sqlite:///./instance/database.db",
        "theme": "default",
        "available_themes": ["default"],
        "log_level": "INFO",
        "enable_cache": True,
        "cache_ttl": 300,
    }

    config_file = target_dir / "site.yaml"
    with open(config_file, "w", encoding="utf-8") as f:
        yaml.safe_dump(config, f, allow_unicode=True, default_flow_style=False)

    print(f"  [OK] 创建 site.yaml")


def create_app_entry(target_dir: Path, site_name: str):
    """创建应用入口文件"""
    app_code = f'''# -*- coding: utf-8 -*-
"""
{site_name} - Application Entry Point

启动命令:
    python app.py

或使用 uvicorn:
    uvicorn app:app --reload --host 0.0.0.0 --port 8000
"""

from pathlib import Path

from docms import create_app
from docms.config import SiteConfig

# 加载站点配置
config = SiteConfig.from_yaml(Path(__file__).parent / "site.yaml")

# 创建应用实例
app = create_app(site_config=config)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level=config.log_level.lower()
    )
'''

    (target_dir / "app.py").write_text(app_code, encoding="utf-8")
    print(f"  [OK] 创建 app.py")


def create_requirements(target_dir: Path):
    """创建 requirements.txt"""
    source_requirements = Path(__file__).parent.parent / "requirements.txt"

    if source_requirements.exists():
        shutil.copy2(source_requirements, target_dir / "requirements.txt")
    else:
        # 创建基础依赖列表
        requirements = """fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
alembic==1.12.1
pydantic==2.5.0
pydantic-settings==2.1.0
jinja2==3.1.2
python-multipart==0.0.6
email-validator==2.1.0
pyyaml==6.0.1
"""
        (target_dir / "requirements.txt").write_text(requirements, encoding="utf-8")

    print(f"  [OK] 创建 requirements.txt")


def create_base_templates(target_dir: Path):
    """创建基础模板文件"""
    templates_dir = target_dir / "templates"

    # base.html
    base_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{{ site_settings.site_name }}{% endblock %}</title>
    <link rel="stylesheet" href="/static/css/main.css">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- 导航栏 -->
    <nav class="navbar">
        <div class="container">
            <a href="/" class="logo">{{ site_settings.site_name }}</a>
            <ul class="nav-menu">
                {% for column in navigation %}
                <li><a href="/{{ column.slug }}">{{ column.name }}</a></li>
                {% endfor %}
            </ul>
        </div>
    </nav>

    <!-- 主要内容 -->
    <main>
        {% block content %}{% endblock %}
    </main>

    <!-- 页脚 -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 {{ site_settings.site_name }}. All rights reserved.</p>
        </div>
    </footer>

    {% block extra_js %}{% endblock %}
</body>
</html>
'''

    # home.html
    home_html = '''{% extends "base.html" %}

{% block title %}首页 - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<div class="hero">
    <div class="container">
        <h1>欢迎来到 {{ site_settings.site_name }}</h1>
        <p>{{ site_settings.site_description }}</p>
    </div>
</div>

<div class="container">
    <section class="featured-products">
        <h2>推荐产品</h2>
        <div class="product-grid">
            {% for product in featured_products %}
            <div class="product-card">
                <h3>{{ product.name }}</h3>
                <p>{{ product.summary }}</p>
                <a href="/products/detail/{{ product.slug }}">了解更多 →</a>
            </div>
            {% endfor %}
        </div>
    </section>
</div>
{% endblock %}
'''

    # 404.html
    error_404 = '''{% extends "base.html" %}

{% block title %}页面未找到{% endblock %}

{% block content %}
<div class="container">
    <div class="error-page">
        <h1>404</h1>
        <h2>页面未找到</h2>
        <p>抱歉，您访问的页面不存在。</p>
        <a href="/">返回首页</a>
    </div>
</div>
{% endblock %}
'''

    # 500.html
    error_500 = '''{% extends "base.html" %}

{% block title %}服务器错误{% endblock %}

{% block content %}
<div class="container">
    <div class="error-page">
        <h1>500</h1>
        <h2>服务器错误</h2>
        <p>抱歉，服务器遇到了问题。</p>
        <a href="/">返回首页</a>
    </div>
</div>
{% endblock %}
'''

    (templates_dir / "base.html").write_text(base_html, encoding="utf-8")
    (templates_dir / "home.html").write_text(home_html, encoding="utf-8")
    (templates_dir / "404.html").write_text(error_404, encoding="utf-8")
    (templates_dir / "500.html").write_text(error_500, encoding="utf-8")

    # 基础 CSS
    css_content = '''/* Basic Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navbar */
.navbar {
    background: #fff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    padding: 1rem 0;
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: #333;
    text-decoration: none;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-menu a {
    color: #666;
    text-decoration: none;
    transition: color 0.3s;
}

.nav-menu a:hover {
    color: #333;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 0;
    text-align: center;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

/* Product Grid */
.featured-products {
    padding: 4rem 0;
}

.featured-products h2 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 2rem;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
}

.product-card {
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 1.5rem;
    transition: transform 0.3s, box-shadow 0.3s;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.product-card h3 {
    margin-bottom: 0.5rem;
}

.product-card a {
    color: #667eea;
    text-decoration: none;
    font-weight: 500;
}

/* Footer */
.footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 4rem;
}

/* Error Pages */
.error-page {
    text-align: center;
    padding: 4rem 0;
}

.error-page h1 {
    font-size: 6rem;
    color: #667eea;
}

.error-page h2 {
    font-size: 2rem;
    margin: 1rem 0;
}

.error-page a {
    display: inline-block;
    margin-top: 2rem;
    padding: 0.75rem 2rem;
    background: #667eea;
    color: white;
    text-decoration: none;
    border-radius: 4px;
}
'''

    (templates_dir / "static" / "css" / "main.css").write_text(css_content, encoding="utf-8")

    print(f"  [OK] 创建基础模板文件")


def create_readme(target_dir: Path, site_name: str):
    """创建 README"""
    readme_content = f'''# {site_name}

基于 Docms CMS 创建的企业官网

## 快速开始

### 1. 安装依赖

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\\Scripts\\activate  # Windows

pip install -r requirements.txt
```

### 2. 配置站点

编辑 `site.yaml` 文件，配置站点基本信息。

### 3. 生成内容（使用 LLM）

```bash
python -m cli.generate_content
```

按照提示输入公司信息，LLM 将自动生成：
- 数据库内容（产品、文章、栏目等）
- 页面模板（HTML）

### 4. 初始化数据库

```bash
alembic upgrade head
sqlite3 instance/database.db < seed_data.sql
```

### 5. 启动服务器

```bash
python app.py
```

访问 http://localhost:8000

## 目录结构

```
{site_name}/
├── app/                    # 核心应用代码
├── docms/                  # Docms 引擎
├── instance/               # 站点实例数据
│   ├── database.db        # SQLite 数据库
│   └── media/             # 媒体文件
├── templates/              # 模板文件
│   ├── base.html
│   ├── home.html
│   └── static/
├── migrations/             # 数据库迁移
├── app.py                  # 应用入口
└── site.yaml              # 站点配置
```

## 自定义

### 修改模板

编辑 `templates/` 目录下的 HTML 文件。

### 修改样式

编辑 `templates/static/css/main.css`。

### 添加内容

通过数据库或使用 LLM 生成工具添加产品、文章等内容。

## 部署

参考 [Docms 部署文档](https://github.com/your-repo/docms-scaffold)

---

Powered by [Docms CMS](https://github.com/your-repo/docms-scaffold)
'''

    (target_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  [OK] 创建 README.md")


def main():
    """CLI 入口"""
    parser = argparse.ArgumentParser(description="创建新的 Docms 站点")
    parser.add_argument(
        "--name",
        required=True,
        help="站点名称（目录名）"
    )
    parser.add_argument(
        "--dir",
        type=Path,
        default=None,
        help="目标目录（默认为当前目录的父目录）"
    )
    parser.add_argument(
        "--company",
        default=None,
        help="公司名称"
    )
    parser.add_argument(
        "--description",
        default=None,
        help="公司描述"
    )

    args = parser.parse_args()

    try:
        create_site(
            site_name=args.name,
            target_dir=args.dir,
            company_name=args.company,
            company_description=args.description
        )
    except Exception as e:
        print(f"\n[ERROR] 创建失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
