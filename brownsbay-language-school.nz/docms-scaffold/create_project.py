#!/usr/bin/env python3
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

    print(f"创建项目: {project_name}")
    print(f"目标路径: {project_path}")

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

    print(f"项目 '{project_name}' 创建完成!")
    print(f"位置: {project_path}")
    print("\n下一步:")
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
        print("提示: 记得创建虚拟环境:")
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
