#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docms Project Generator (Modular Version)

使用 scaffold 创建新项目，支持模块化选择
"""

import os
import shutil
import sys
import argparse
from pathlib import Path
from datetime import datetime
from module_manager import ModuleManager


def create_project(
    project_name: str,
    project_path: str = None,
    preset: str = None,
    modules: list = None,
    interactive: bool = False
):
    """
    创建新项目

    Args:
        project_name: 项目名称
        project_path: 项目路径
        preset: 预设方案名称
        modules: 自定义模块列表
        interactive: 是否交互式选择模块
    """

    if project_path is None:
        project_path = Path.cwd() / project_name
    else:
        project_path = Path(project_path)

    scaffold_dir = Path(__file__).parent

    print(f"创建项目: {project_name}")
    print(f"目标路径: {project_path}")

    # 初始化模块管理器
    manager = ModuleManager()

    # 确定启用的模块
    if interactive:
        selected_modules = _interactive_select_modules(manager)
    elif preset:
        print(f"使用预设方案: {preset}")
        selected_modules = manager.get_preset_modules(preset)
    elif modules:
        selected_modules = modules
    else:
        # 默认使用 corporate 方案
        print("使用默认方案: corporate (企业官网)")
        selected_modules = manager.get_preset_modules("corporate")

    # 解析依赖
    enabled_modules = manager.resolve_dependencies(selected_modules)
    print(f"\n启用的模块 ({len(enabled_modules)}个):")
    for module in sorted(enabled_modules):
        module_info = manager.all_modules.get(module, {})
        display_name = module_info.get("display_name", module)
        print(f"  ✓ {module:15} - {display_name}")

    # 创建项目目录
    project_path.mkdir(parents=True, exist_ok=True)

    # 复制基础文件（不包括 models/services/schemas）
    _copy_base_files(scaffold_dir, project_path)

    # 根据模块复制对应文件
    _copy_module_files(scaffold_dir, project_path, manager, enabled_modules)

    # 生成 __init__.py 文件
    _generate_init_files(project_path, manager, enabled_modules)

    # 处理模板文件
    _process_templates(project_path, project_name)

    # 创建初始目录
    _create_initial_directories(project_path)

    # 生成模块配置文件（保存项目使用的模块列表）
    _save_project_modules(project_path, enabled_modules)

    print(f"\n✅ 项目 '{project_name}' 创建完成!")
    print(f"📁 位置: {project_path}")
    print("\n📋 下一步:")
    print(f"   cd {project_path}")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # Linux/Mac")
    print("   # 或 venv\\Scripts\\activate  # Windows")
    print("   pip install -r requirements.txt")
    print("   alembic upgrade head")
    print("   python app.py")


def _interactive_select_modules(manager: ModuleManager) -> list:
    """交互式选择模块"""
    print("\n=== 模块选择 ===")
    print("\n可用预设方案:")

    presets = manager.list_presets()
    for i, preset in enumerate(presets, 1):
        print(f"  {i}. {preset['display_name']:15} - {preset['description']}")

    print(f"  {len(presets)+1}. 自定义选择")

    choice = input(f"\n请选择 (1-{len(presets)+1}): ").strip()

    try:
        choice_num = int(choice)
        if 1 <= choice_num <= len(presets):
            preset = presets[choice_num - 1]
            print(f"\n已选择: {preset['display_name']}")
            return preset["modules"]
    except ValueError:
        pass

    # 自定义选择
    print("\n=== 自定义模块选择 ===")
    categories = manager.list_available_modules()

    selected = []

    for cat_name, modules in categories.items():
        if cat_name == "核心模块（必需）":
            continue  # 核心模块自动包含

        print(f"\n{cat_name}:")
        for module in modules:
            deps = module.get("dependencies", [])
            deps_str = f" [需要: {', '.join(deps)}]" if deps else ""
            print(f"  {module['name']:15} - {module['display_name']:12} - {module['description']}{deps_str}")

        selected_input = input(f"请输入要启用的模块（逗号分隔，留空跳过）: ").strip()
        if selected_input:
            selected.extend([m.strip() for m in selected_input.split(",")])

    return selected


def _copy_base_files(scaffold_dir: Path, project_path: Path):
    """复制基础文件和目录"""
    print("\n📦 复制基础文件...")

    # 需要跳过的文件和目录
    skip_items = {
        "create_project.py",
        "create_project_modular.py",
        "module_manager.py",
        "modules_config.yaml",
        "README.md",
        "__pycache__"
    }

    # 需要特殊处理的目录
    special_dirs = {"app"}

    for item in scaffold_dir.iterdir():
        if item.name in skip_items:
            continue

        target = project_path / item.name

        if item.is_dir():
            if item.name in special_dirs:
                # 特殊处理 app 目录
                _copy_app_dir(item, target)
            else:
                # 直接复制其他目录
                if target.exists():
                    shutil.rmtree(target)
                shutil.copytree(item, target)
                print(f"  ✓ {item.name}/")
        else:
            shutil.copy2(item, target)
            print(f"  ✓ {item.name}")


def _copy_app_dir(source_app: Path, target_app: Path):
    """复制 app 目录（但跳过 models/services/schemas 目录内容）"""
    skip_content_dirs = {"models", "services", "schemas"}

    target_app.mkdir(parents=True, exist_ok=True)

    for item in source_app.iterdir():
        target = target_app / item.name

        if item.is_dir():
            if item.name in skip_content_dirs:
                # 只创建目录，不复制内容
                target.mkdir(parents=True, exist_ok=True)
                print(f"  ✓ app/{item.name}/ (空目录)")
            else:
                if target.exists():
                    shutil.rmtree(target)
                shutil.copytree(item, target)
                print(f"  ✓ app/{item.name}/")
        else:
            shutil.copy2(item, target)
            print(f"  ✓ app/{item.name}")


def _copy_module_files(
    scaffold_dir: Path,
    project_path: Path,
    manager: ModuleManager,
    enabled_modules: set
):
    """根据启用的模块复制对应文件"""
    print("\n📦 复制模块文件...")

    files_to_copy = manager.get_files_to_copy(enabled_modules)

    for file_type, file_list in files_to_copy.items():
        source_dir = scaffold_dir / "app" / file_type
        target_dir = project_path / "app" / file_type

        for file_name in file_list:
            source_file = source_dir / file_name
            target_file = target_dir / file_name

            if source_file.exists():
                shutil.copy2(source_file, target_file)
                print(f"  ✓ app/{file_type}/{file_name}")
            else:
                print(f"  ⚠ 文件不存在: app/{file_type}/{file_name}")

    # 特殊处理 schemas.py（如果需要的话）
    if "schemas.py" in [f if isinstance(f, str) else f.get("key") for files in [
        m.get("files", {}).get("schemas", [])
        for m in manager.all_modules.values()
    ] for f in files]:
        source_schemas = scaffold_dir / "app" / "schemas" / "schemas.py"
        target_schemas = project_path / "app" / "schemas" / "schemas.py"
        if source_schemas.exists():
            shutil.copy2(source_schemas, target_schemas)
            print(f"  ✓ app/schemas/schemas.py")


def _generate_init_files(project_path: Path, manager: ModuleManager, enabled_modules: set):
    """生成 __init__.py 文件"""
    print("\n📝 生成 __init__.py 文件...")

    # 生成 models/__init__.py
    models_init = project_path / "app" / "models" / "__init__.py"
    models_content = manager.generate_models_init(enabled_modules)
    models_init.write_text(models_content, encoding="utf-8")
    print("  ✓ app/models/__init__.py")

    # 生成 services/__init__.py
    services_init = project_path / "app" / "services" / "__init__.py"
    services_content = manager.generate_services_init(enabled_modules)
    services_init.write_text(services_content, encoding="utf-8")
    print("  ✓ app/services/__init__.py")

    # 生成 schemas/__init__.py
    schemas_init = project_path / "app" / "schemas" / "__init__.py"
    schemas_content = manager.generate_schemas_init(enabled_modules)
    schemas_init.write_text(schemas_content, encoding="utf-8")
    print("  ✓ app/schemas/__init__.py")


def _process_templates(project_path: Path, project_name: str):
    """处理模板文件，替换占位符"""
    print("\n🔧 处理模板文件...")

    placeholders = {
        "{{PROJECT_NAME}}": project_name.title(),
        "{{PROJECT_SLUG}}": project_name.lower().replace(" ", "-"),
        "{{SITE_NAME}}": project_name.title(),
        "{{SITE_DESCRIPTION}}": f"A professional website for {project_name.title()}",
        "{{SITE_URL}}": "https://example.com",
        "{{COMPANY_NAME}}": project_name.title(),
        "{{CONTACT_EMAIL}}": f"info@{project_name.lower().replace(' ', '')}.com",
        "{{CONTACT_PHONE}}": "+64 9 123 4567",  # NZ phone format
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
            template_file.unlink()
            print(f"  ✓ config/{template_file.stem}")

    # 处理应用配置文件
    config_file = project_path / "app" / "config.py"
    if config_file.exists():
        content = config_file.read_text(encoding='utf-8')
        for placeholder, value in placeholders.items():
            content = content.replace(placeholder, value)
        config_file.write_text(content, encoding='utf-8')
        print(f"  ✓ app/config.py")


def _create_initial_directories(project_path: Path):
    """创建初始目录"""
    directories = [
        "instance",
        "instance/media",
        "logs"
    ]

    for directory in directories:
        (project_path / directory).mkdir(parents=True, exist_ok=True)
        gitkeep = project_path / directory / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text("")


def _save_project_modules(project_path: Path, enabled_modules: set):
    """保存项目使用的模块列表"""
    modules_file = project_path / "enabled_modules.txt"
    content = "# Enabled Modules for this project\n"
    content += "# Generated by create_project_modular.py\n\n"
    content += "\n".join(sorted(enabled_modules))
    modules_file.write_text(content, encoding="utf-8")
    print(f"\n  ✓ enabled_modules.txt (记录已启用模块)")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Docms Project Generator - 模块化版本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 使用默认方案（企业官网）
  python create_project_modular.py my-website

  # 使用预设方案
  python create_project_modular.py my-website --preset ecommerce

  # 自定义模块
  python create_project_modular.py my-website --modules team,portfolio,product

  # 交互式选择
  python create_project_modular.py my-website --interactive

可用预设方案:
  - corporate      企业官网
  - ecommerce      电商网站
  - education      教育培训
  - restaurant     餐厅/咖啡馆
  - medical        医疗/诊所
  - service        专业服务
  - minimal        最小化配置
  - full           完整配置
        """
    )

    parser.add_argument("project_name", help="项目名称")
    parser.add_argument("project_path", nargs="?", help="项目路径（可选）")
    parser.add_argument("--preset", "-p", help="预设方案名称")
    parser.add_argument("--modules", "-m", help="自定义模块列表（逗号分隔）")
    parser.add_argument("--interactive", "-i", action="store_true", help="交互式选择模块")
    parser.add_argument("--list-presets", action="store_true", help="列出所有预设方案")
    parser.add_argument("--list-modules", action="store_true", help="列出所有可用模块")

    args = parser.parse_args()

    # 列出预设方案
    if args.list_presets:
        manager = ModuleManager()
        print("\n=== 可用预设方案 ===\n")
        for preset in manager.list_presets():
            print(f"{preset['name']:12} | {preset['display_name']:15} | {preset['description']}")
            print(f"  模块: {', '.join(preset['modules'])}\n")
        return

    # 列出所有模块
    if args.list_modules:
        manager = ModuleManager()
        print("\n=== 可用模块 ===\n")
        categories = manager.list_available_modules()
        for cat_name, modules in categories.items():
            print(f"{cat_name}:")
            for module in modules:
                deps = module.get("dependencies", [])
                deps_str = f" [依赖: {', '.join(deps)}]" if deps else ""
                print(f"  {module['name']:15} | {module['display_name']:12} | {module['description']}{deps_str}")
            print()
        return

    # 创建项目
    modules_list = args.modules.split(",") if args.modules else None

    create_project(
        project_name=args.project_name,
        project_path=args.project_path,
        preset=args.preset,
        modules=modules_list,
        interactive=args.interactive
    )


if __name__ == "__main__":
    main()
