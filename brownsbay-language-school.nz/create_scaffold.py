#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docms Scaffold Generator

从现有项目中抽取可复用的框架代码，生成新的项目模板
"""

import os
import shutil
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set


class ScaffoldGenerator:
    """Scaffold 生成器类"""

    def __init__(self, source_dir: str = ".", output_dir: str = "docms-scaffold"):
        self.source_dir = Path(source_dir).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.template_placeholders = {
            "{{PROJECT_NAME}}": "New Website",
            "{{PROJECT_SLUG}}": "new-website",
            "{{SITE_NAME}}": "New Website",
            "{{SITE_DESCRIPTION}}": "A professional website built with Docms CMS",
            "{{SITE_URL}}": "https://example.com",
            "{{COMPANY_NAME}}": "Your Company",
            "{{CONTACT_EMAIL}}": "info@example.com",
            "{{CONTACT_PHONE}}": "+1 234 567 8900",
            "{{COPYRIGHT_YEAR}}": str(datetime.now().year),
            "{{DATABASE_NAME}}": "database.db"
        }

    def create_scaffold(self):
        """创建 scaffold"""
        print("开始创建 Docms Scaffold...")

        # 清理输出目录
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)

        self.output_dir.mkdir(parents=True)
        print(f"创建输出目录: {self.output_dir}")

        # 复制核心文件
        self._copy_core_files()

        # 创建模板文件
        self._create_template_files()

        # 复制并清理应用代码
        self._copy_and_clean_app()

        # 复制迁移框架
        self._copy_migration_framework()

        # 创建基础模板示例
        self._create_template_examples()

        # 创建项目创建脚本
        self._create_project_generator()

        # 创建 Scaffold 说明文档
        self._create_scaffold_readme()

        print("Scaffold 创建完成!")
        print(f"输出位置: {self.output_dir}")

    def _copy_core_files(self):
        """复制核心配置文件"""
        print("📋 复制核心配置文件...")

        # 复制 requirements.txt
        self._copy_file("requirements.txt")

        # 复制并清理 alembic.ini
        self._copy_and_clean_alembic_ini()

    def _copy_and_clean_alembic_ini(self):
        """复制并清理 alembic.ini"""
        source_file = self.source_dir / "alembic.ini"
        target_file = self.output_dir / "alembic.ini"

        if source_file.exists():
            content = source_file.read_text(encoding='utf-8')
            # 清理项目特定的路径
            content = re.sub(r'script_location = .*', 'script_location = migrations', content)
            content = re.sub(r'file_template = .*', 'file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d_%%(rev)s_%%(slug)s', content)

            target_file.write_text(content, encoding='utf-8')
            print(f"  ✓ 清理并复制: alembic.ini")

    def _create_template_files(self):
        """创建模板配置文件"""
        print("📝 创建模板配置文件...")

        config_dir = self.output_dir / "config"
        config_dir.mkdir()

        # 创建站点配置模板
        site_config_template = f"""available_themes:
- default
base_dir: .
cache_ttl: 300
database_url: sqlite:///./instance/{{{{DATABASE_NAME}}}}
enable_cache: true
log_level: INFO
media_dir: ./instance/media
site_description: {{{{SITE_DESCRIPTION}}}}
site_name: {{{{SITE_NAME}}}}
site_url: {{{{SITE_URL}}}}
static_dir: ./templates/static
template_dir: ./templates
theme: default
"""

        (config_dir / "site.yaml.template").write_text(site_config_template, encoding='utf-8')
        print("  ✓ 创建: config/site.yaml.template")

        # 创建初始数据模板
        seed_data_template = f"""-- =========================================
-- {{{{PROJECT_NAME}}}} - Database Seed Data Template
-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
-- =========================================

-- Clean existing data (optional - comment out if appending)
DELETE FROM product_category_link;
DELETE FROM post_category_link;
DELETE FROM product;
DELETE FROM post;
DELETE FROM product_category;
DELETE FROM post_category;
DELETE FROM single_page;
DELETE FROM site_column;
DELETE FROM site_setting;

-- =========================================
-- 1. SITE SETTINGS
-- =========================================
INSERT INTO site_setting (`key`, value, created_at, updated_at) VALUES
('site_name', '{{{{SITE_NAME}}}}', datetime('now'), datetime('now')),
('site_description', '{{{{SITE_DESCRIPTION}}}}', datetime('now'), datetime('now')),
('phone', '{{{{CONTACT_PHONE}}}}', datetime('now'), datetime('now')),
('email', '{{{{CONTACT_EMAIL}}}}', datetime('now'), datetime('now')),
('address', 'Your Address Here', datetime('now'), datetime('now')),
('business_hours', 'Monday-Friday 9:00am-5:00pm', datetime('now'), datetime('now')),
('copyright', '© {{{{COPYRIGHT_YEAR}}}} {{{{COMPANY_NAME}}}}. All rights reserved.', datetime('now'), datetime('now'));

-- =========================================
-- 2. SITE COLUMNS (Navigation Structure)
-- =========================================
INSERT INTO site_column (id, name, slug, type, description, is_visible, `order`, created_at, updated_at) VALUES
(1, 'Home', 'home', 'CUSTOM', 'Homepage', 1, 1, datetime('now'), datetime('now')),
(2, 'About Us', 'about', 'SINGLE_PAGE', 'About page', 1, 2, datetime('now'), datetime('now')),
(3, 'Services', 'services', 'SINGLE_PAGE', 'Services page', 1, 3, datetime('now'), datetime('now')),
(4, 'Blog', 'blog', 'POST', 'Blog posts and articles', 1, 4, datetime('now'), datetime('now')),
(5, 'Contact', 'contact', 'SINGLE_PAGE', 'Contact information and form', 1, 5, datetime('now'), datetime('now'));
"""

        (config_dir / "seed_data.sql.template").write_text(seed_data_template, encoding='utf-8')
        print("  ✓ 创建: config/seed_data.sql.template")

    def _copy_and_clean_app(self):
        """复制并清理应用代码"""
        print("🏗️ 复制并清理应用代码...")

        app_source = self.source_dir / "app"
        app_target = self.output_dir / "app"

        if app_source.exists():
            shutil.copytree(app_source, app_target)

            # 清理配置文件中的硬编码业务信息
            config_file = app_target / "config.py"
            if config_file.exists():
                self._clean_config_file(config_file)

            print("  ✓ 复制应用框架")

    def _clean_config_file(self, config_file: Path):
        """清理配置文件中的业务特定信息"""
        content = config_file.read_text(encoding='utf-8')

        # 替换硬编码的业务信息为通用模板
        content = re.sub(
            r'SITE_NAME = os\.getenv\("SITE_NAME", "[^"]+"\)',
            'SITE_NAME = os.getenv("SITE_NAME", "{{SITE_NAME}}")',
            content
        )
        content = re.sub(
            r'SITE_TITLE = os\.getenv\("SITE_TITLE", "[^"]+"\)',
            'SITE_TITLE = os.getenv("SITE_TITLE", "{{SITE_NAME}}")',
            content
        )
        content = re.sub(
            r'SITE_DESCRIPTION = os\.getenv\("SITE_DESCRIPTION", "[^"]+"\)',
            'SITE_DESCRIPTION = os.getenv("SITE_DESCRIPTION", "{{SITE_DESCRIPTION}}")',
            content
        )

        config_file.write_text(content, encoding='utf-8')
        print("    ✓ 清理配置文件")

    def _copy_migration_framework(self):
        """复制迁移框架（不包含具体的迁移文件）"""
        print("🗃️ 复制数据库迁移框架...")

        migrations_source = self.source_dir / "migrations"
        migrations_target = self.output_dir / "migrations"

        if migrations_source.exists():
            migrations_target.mkdir()

            # 复制环境配置文件
            env_file = migrations_source / "env.py"
            if env_file.exists():
                shutil.copy2(env_file, migrations_target / "env.py")

            # 创建空的版本目录
            versions_dir = migrations_target / "versions"
            versions_dir.mkdir()

            # 创建 .gitkeep 文件
            (versions_dir / ".gitkeep").write_text("")

            print("  ✓ 复制迁移框架")

    def _create_template_examples(self):
        """创建基础模板示例"""
        print("🎨 创建基础模板示例...")

        templates_dir = self.output_dir / "templates"
        templates_dir.mkdir()

        # 创建基础模板结构
        subdirs = ["components", "static/css", "static/js", "static/images"]
        for subdir in subdirs:
            (templates_dir / subdir).mkdir(parents=True)

        # 创建基础 HTML 模板
        base_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{{ site_settings.get('site_name', 'Website') }}{% endblock %}</title>
    <meta name="description" content="{% block description %}{{ site_settings.get('site_description', '') }}{% endblock %}">
    <link rel="stylesheet" href="/static/css/main.css">
</head>
<body>
    <header>
        <nav>
            <!-- Navigation will be rendered here -->
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; {{ moment().format('YYYY') }} {{ site_settings.get('site_name', 'Website') }}. All rights reserved.</p>
    </footer>

    <script src="/static/js/main.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
"""

        (templates_dir / "base.html").write_text(base_template, encoding='utf-8')

        # 创建错误页面模板
        error_404 = """{% extends "base.html" %}

{% block title %}404 - Page Not Found{% endblock %}

{% block content %}
<div class="error-page">
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for doesn't exist.</p>
    <a href="/">Return to Home</a>
</div>
{% endblock %}
"""

        (templates_dir / "404.html").write_text(error_404, encoding='utf-8')

        error_500 = """{% extends "base.html" %}

{% block title %}500 - Server Error{% endblock %}

{% block content %}
<div class="error-page">
    <h1>500 - Server Error</h1>
    <p>Something went wrong on our end. Please try again later.</p>
    <a href="/">Return to Home</a>
</div>
{% endblock %}
"""

        (templates_dir / "500.html").write_text(error_500, encoding='utf-8')

        print("  ✓ 创建基础模板示例")

    def _create_project_generator(self):
        """创建项目生成脚本"""
        print("⚙️ 创建项目生成脚本...")

        generator_script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docms Project Generator

使用 scaffold 创建新项目
"""

import os
import shutil
import sys
from pathlib import Path
from datetime import datetime


def create_project(project_name: str, project_path: str = None):
    """创建新项目"""

    if project_path is None:
        project_path = Path.cwd() / project_name
    else:
        project_path = Path(project_path)

    scaffold_dir = Path(__file__).parent

    print(f"🚀 创建项目: {project_name}")
    print(f"📍 目标路径: {project_path}")

    # 创建项目目录
    project_path.mkdir(parents=True, exist_ok=True)

    # 复制 scaffold 内容
    for item in scaffold_dir.iterdir():
        if item.name in ["create_project.py", "README.md"]:
            continue  # 跳过生成脚本和说明文档

        target = project_path / item.name

        if item.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)

    # 处理模板文件
    _process_templates(project_path, project_name)

    # 创建虚拟环境
    _create_virtual_env(project_path)

    # 创建初始目录
    _create_initial_directories(project_path)

    print(f"✅ 项目 '{project_name}' 创建完成!")
    print(f"📍 位置: {project_path}")
    print("\n📋 下一步:")
    print(f"   cd {project_path}")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # Linux/Mac")
    print("   # 或 venv\\Scripts\\activate  # Windows")
    print("   pip install -r requirements.txt")
    print("   alembic upgrade head")
    print("   python app.py")


def _process_templates(project_path: Path, project_name: str):
    """处理模板文件，替换占位符"""

    placeholders = {
        "{{PROJECT_NAME}}": project_name.title(),
        "{{PROJECT_SLUG}}": project_name.lower().replace(" ", "-"),
        "{{SITE_NAME}}": project_name.title(),
        "{{SITE_DESCRIPTION}}": f"A professional website for {project_name.title()}",
        "{{SITE_URL}}": "https://example.com",
        "{{COMPANY_NAME}}": project_name.title(),
        "{{CONTACT_EMAIL}}": f"info@{project_name.lower().replace(' ', '')}.com",
        "{{CONTACT_PHONE}}": "+1 234 567 8900",
        "{{COPYRIGHT_YEAR}}": str(datetime.now().year),
        "{{DATABASE_NAME}}": "database.db"
    }

    # 处理配置模板文件
    config_dir = project_path / "config"
    if config_dir.exists():
        for template_file in config_dir.glob("*.template"):
            target_file = config_dir / template_file.stem

            content = template_file.read_text(encoding='utf-8')
            for placeholder, value in placeholders.items():
                content = content.replace(placeholder, value)

            target_file.write_text(content, encoding='utf-8')
            template_file.unlink()  # 删除模板文件

    # 处理应用配置文件
    config_file = project_path / "app" / "config.py"
    if config_file.exists():
        content = config_file.read_text(encoding='utf-8')
        for placeholder, value in placeholders.items():
            content = content.replace(placeholder, value)
        config_file.write_text(content, encoding='utf-8')


def _create_virtual_env(project_path: Path):
    """创建虚拟环境提示"""
    venv_dir = project_path / "venv"
    if not venv_dir.exists():
        print("💡 提示: 记得创建虚拟环境:")
        print("   python -m venv venv")


def _create_initial_directories(project_path: Path):
    """创建初始目录"""
    directories = [
        "instance",
        "instance/media",
        "logs"
    ]

    for directory in directories:
        (project_path / directory).mkdir(parents=True, exist_ok=True)

    # 创建 .gitkeep 文件
    for directory in directories:
        gitkeep = project_path / directory / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text("")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python create_project.py <项目名称> [项目路径]")
        print("示例: python create_project.py my-website")
        print("示例: python create_project.py my-website /path/to/projects")
        sys.exit(1)

    project_name = sys.argv[1]
    project_path = sys.argv[2] if len(sys.argv) > 2 else None

    create_project(project_name, project_path)


if __name__ == "__main__":
    main()
'''

        (self.output_dir / "create_project.py").write_text(generator_script, encoding='utf-8')

        # 设置执行权限
        if os.name != 'nt':  # 非 Windows 系统
            os.chmod(self.output_dir / "create_project.py", 0o755)

        print("  ✓ 创建项目生成脚本")

    def _create_scaffold_readme(self):
        """创建 Scaffold 说明文档"""
        print("📖 创建 Scaffold 说明文档...")

        readme_content = f"""# Docms Scaffold

Docms CMS 项目模板，用于快速创建新的网站项目。

## 🚀 快速开始

### 1. 使用 Scaffold 创建新项目

```bash
python create_project.py my-new-website
```

### 2. 进入项目目录

```bash
cd my-new-website
```

### 3. 设置虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\\Scripts\\activate
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

### 5. 初始化数据库

```bash
# 如果有 Alembic 迁移
alembic upgrade head

# 导入初始数据（可选）
sqlite3 instance/database.db < config/seed_data.sql
```

### 6. 启动应用

```bash
python app.py
```

## 📁 项目结构

```
your-project/
├── app.py                    # 应用入口
├── site.yaml                 # 站点配置
├── requirements.txt          # Python 依赖
├── alembic.ini              # 数据库迁移配置
├── app/                     # 应用代码
│   ├── main.py             # 应用工厂
│   ├── config.py           # 配置管理
│   ├── models/             # 数据模型
│   ├── routes/             # 路由处理
│   ├── services/           # 业务逻辑
│   ├── utils/              # 工具函数
│   └── ...
├── templates/              # HTML 模板
├── migrations/             # 数据库迁移
├── instance/               # 运行时数据
└── logs/                   # 日志文件
```

## 🎨 自定义模板

### 修改站点配置

编辑 `site.yaml` 文件来配置你的网站:

```yaml
site_name: "Your Website Name"
site_description: "Your website description"
site_url: "https://yourwebsite.com"
```

### 自定义模板

在 `templates/` 目录中创建你的 HTML 模板文件。

### 添加数据模型

在 `app/models/` 目录中定义你的数据模型。

### 创建路由

在 `app/routes/` 目录中添加你的路由处理。

## 🛠️ 开发指南

### 添加新页面

1. 在 `templates/` 中创建模板文件
2. 在 `app/routes/frontend.py` 中添加路由
3. 在 `site.yaml` 中配置栏目

### 数据库迁移

```bash
# 创建新的迁移
alembic revision --autogenerate -m "描述变更"

# 应用迁移
alembic upgrade head

# 回滚迁移
alembic downgrade -1
```

### 部署

```bash
# 生产环境启动
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 📚 文档

- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 文档](https://docs.sqlalchemy.org/)
- [Jinja2 文档](https://jinja.palletsprojects.com/)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

创建时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
版本: 1.0.0
"""

        (self.output_dir / "README.md").write_text(readme_content, encoding='utf-8')
        print("  ✓ 创建说明文档")

    def _copy_file(self, filename: str):
        """复制单个文件"""
        source_file = self.source_dir / filename
        target_file = self.output_dir / filename

        if source_file.exists():
            shutil.copy2(source_file, target_file)
            print(f"  ✓ 复制: {filename}")


def main():
    """主函数"""
    generator = ScaffoldGenerator()
    generator.create_scaffold()


if __name__ == "__main__":
    main()