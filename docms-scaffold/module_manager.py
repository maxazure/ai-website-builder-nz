#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Docms 模块管理器

根据配置文件管理模块的启用/禁用，处理依赖关系
"""

import yaml
from pathlib import Path
from typing import List, Dict, Set, Optional


class ModuleManager:
    """模块管理器"""

    def __init__(self, config_file: str = "modules_config.yaml"):
        """初始化模块管理器"""
        self.config_file = Path(__file__).parent / config_file
        self.config = self._load_config()
        self.core_modules = {m["name"]: m for m in self.config["core_modules"]}
        self.optional_modules = {m["name"]: m for m in self.config["optional_modules"]}
        self.all_modules = {**self.core_modules, **self.optional_modules}

    def _load_config(self) -> dict:
        """加载配置文件"""
        with open(self.config_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_preset_modules(self, preset_name: str) -> List[str]:
        """获取预设方案的模块列表"""
        presets = {p["name"]: p for p in self.config.get("presets", [])}
        if preset_name not in presets:
            raise ValueError(f"未找到预设方案: {preset_name}")
        return presets[preset_name]["modules"]

    def resolve_dependencies(self, module_names: List[str]) -> Set[str]:
        """
        解析模块依赖关系

        Args:
            module_names: 用户选择的模块列表

        Returns:
            包含所有依赖的完整模块集合（包括核心模块）
        """
        # 始终包含所有核心模块
        resolved = set(self.core_modules.keys())

        # 添加用户选择的模块
        to_process = set(module_names)

        while to_process:
            module_name = to_process.pop()

            if module_name in resolved:
                continue

            if module_name not in self.all_modules:
                print(f"警告: 未知模块 '{module_name}'，已跳过")
                continue

            resolved.add(module_name)

            # 获取依赖
            module = self.all_modules[module_name]
            dependencies = module.get("dependencies", [])

            for dep in dependencies:
                if dep not in resolved:
                    to_process.add(dep)

        return resolved

    def get_files_to_copy(self, enabled_modules: Set[str]) -> Dict[str, List[str]]:
        """
        获取需要复制的文件列表

        Args:
            enabled_modules: 启用的模块集合

        Returns:
            字典，键为目录类型(models/services/schemas)，值为文件列表
        """
        files = {
            "models": [],
            "services": [],
            "schemas": []
        }

        for module_name in enabled_modules:
            if module_name not in self.all_modules:
                continue

            module = self.all_modules[module_name]
            module_files = module.get("files", {})

            for file_type in ["models", "services", "schemas"]:
                files[file_type].extend(module_files.get(file_type, []))

        # 去重
        for file_type in files:
            files[file_type] = list(set(files[file_type]))

        return files

    def get_schema_exports(self, enabled_modules: Set[str]) -> List[str]:
        """
        获取需要导出的 Schema 类列表

        Args:
            enabled_modules: 启用的模块集合

        Returns:
            Schema 类名列表
        """
        exports = []

        for module_name in enabled_modules:
            if module_name not in self.all_modules:
                continue

            module = self.all_modules[module_name]
            schema_files = module.get("files", {}).get("schemas", [])

            for schema_def in schema_files:
                if isinstance(schema_def, dict) and "exports" in schema_def:
                    exports.extend(schema_def["exports"])

        return list(set(exports))

    def generate_models_init(self, enabled_modules: Set[str]) -> str:
        """
        生成 models/__init__.py 文件内容

        Args:
            enabled_modules: 启用的模块集合

        Returns:
            Python 代码字符串
        """
        lines = ['"""Database models module"""', ""]

        # 导入基础模型
        lines.append("# 基础模型")
        lines.append("from app.models.base import BaseModel")
        lines.append("")

        # 按类别组织导入
        categories = {
            "core": "站点核心模块",
            "basic_content": "基础内容模块",
            "interaction": "交互功能模块",
            "ecommerce": "电商交易模块",
            "booking_service": "预约与服务模块",
            "multimedia": "多媒体与资源模块"
        }

        imports_by_category = {cat: [] for cat in categories}
        exports = ["BaseModel"]

        # 收集导入语句
        for module_name in enabled_modules:
            if module_name not in self.all_modules:
                continue

            module = self.all_modules[module_name]
            category = module.get("category", "core") if module_name in self.optional_modules else "core"
            model_files = module.get("files", {}).get("models", [])

            for model_file in model_files:
                module_path = f"app.models.{model_file[:-3]}"  # 移除 .py

                # 读取模型文件获取类名（简化处理，实际应解析文件）
                model_classes = self._get_model_classes(model_file)

                if model_classes:
                    import_stmt = f"from {module_path} import (\n    "
                    import_stmt += ",\n    ".join(model_classes)
                    import_stmt += ",\n)"
                    imports_by_category[category].append(import_stmt)
                    exports.extend(model_classes)

        # 生成导入部分
        for category, label in categories.items():
            if imports_by_category[category]:
                lines.append(f"# {label}")
                lines.extend(imports_by_category[category])
                lines.append("")

        # 生成 __all__
        lines.append("__all__ = [")
        for export in sorted(exports):
            lines.append(f'    "{export}",')
        lines.append("]")
        lines.append("")

        return "\n".join(lines)

    def generate_services_init(self, enabled_modules: Set[str]) -> str:
        """
        生成 services/__init__.py 文件内容

        Args:
            enabled_modules: 启用的模块集合

        Returns:
            Python 代码字符串
        """
        lines = ['# -*- coding: utf-8 -*-', '"""Services Module"""', ""]

        imports = []
        exports = []

        for module_name in enabled_modules:
            if module_name not in self.all_modules:
                continue

            module = self.all_modules[module_name]
            service_files = module.get("files", {}).get("services", [])

            for service_file in service_files:
                # 从文件名推断服务类名
                # 例如: team_service.py -> TeamService
                service_name = self._file_to_service_class(service_file)
                module_path = f"app.services.{service_file[:-3]}"

                imports.append(f"from {module_path} import {service_name}")
                exports.append(service_name)

        if imports:
            lines.extend(sorted(imports))
            lines.append("")
            lines.append("__all__ = [")
            for export in sorted(exports):
                lines.append(f'    "{export}",')
            lines.append("]")
            lines.append("")

        return "\n".join(lines)

    def generate_schemas_init(self, enabled_modules: Set[str]) -> str:
        """
        生成 schemas/__init__.py 文件内容

        Args:
            enabled_modules: 启用的模块集合

        Returns:
            Python 代码字符串
        """
        lines = [
            '"""',
            'Pydantic schemas for request/response validation',
            '"""',
            ""
        ]

        # 获取需要导出的 schema 类
        schema_exports = self.get_schema_exports(enabled_modules)

        # 检查是否有原有的 requests schema
        if "contact" in enabled_modules:
            lines.append("# 原有schemas")
            lines.append("from app.schemas.requests import ContactFormRequest")
            lines.append("")

        if schema_exports:
            lines.append("# 新增schemas（从 schemas.py 导入）")
            lines.append("from app.schemas.schemas import (")
            for export in sorted(schema_exports):
                lines.append(f"    {export},")
            lines.append(")")
            lines.append("")

        # 生成 __all__
        all_exports = []
        if "contact" in enabled_modules:
            all_exports.append("ContactFormRequest")
        all_exports.extend(schema_exports)

        lines.append("__all__ = [")
        for export in sorted(all_exports):
            lines.append(f'    "{export}",')
        lines.append("]")
        lines.append("")

        return "\n".join(lines)

    def _get_model_classes(self, model_file: str) -> List[str]:
        """从模型文件名推断模型类名"""
        # 简化映射，实际应该解析文件
        mappings = {
            "base.py": ["BaseModel"],
            "media.py": ["MediaFile"],
            "site.py": ["SiteColumn", "ColumnType", "SinglePage", "SiteSetting"],
            "contact.py": ["ContactMessage"],
            "post.py": ["Post", "PostCategory", "PostCategoryLink"],
            "team.py": ["TeamMember"],
            "portfolio.py": ["Portfolio", "PortfolioCategory", "PortfolioCategoryLink", "PortfolioImage"],
            "product.py": ["Product", "ProductCategory", "ProductCategoryLink"],
            "custom_field.py": ["CustomFieldDef", "CustomFieldOption", "ProductCustomFieldValue"],
            "faq.py": ["FAQ", "FAQCategory"],
            "comment.py": ["Comment", "Review"],
            "user.py": ["User"],
            "newsletter.py": ["NewsletterSubscriber", "NewsletterCampaign"],
            "cart.py": ["Cart", "CartItem"],
            "order.py": ["Order", "OrderItem"],
            "booking.py": ["Booking", "BookingService", "BookingTimeSlot"],
            "restaurant.py": ["MenuCategory", "MenuItem", "RestaurantOrder", "RestaurantOrderItem"],
            "event.py": ["Event", "EventRegistration", "EventTicketType"],
            "gallery.py": ["Gallery", "GalleryImage"],
            "video.py": ["Video", "VideoCategory", "VideoPlaylist", "VideoPlaylistLink"],
            "file_download.py": ["FileCategory", "FileDownload", "FileDownloadLog"],
        }
        return mappings.get(model_file, [])

    def _file_to_service_class(self, service_file: str) -> str:
        """从服务文件名推断服务类名"""
        # team_service.py -> TeamService
        # post_service.py -> PostService
        name_parts = service_file.replace("_service.py", "").split("_")
        return "".join(word.capitalize() for word in name_parts) + "Service"

    def list_available_modules(self) -> Dict[str, List[Dict]]:
        """列出所有可用模块"""
        categories = {}

        # 核心模块
        categories["核心模块（必需）"] = [
            {
                "name": m["name"],
                "display_name": m["display_name"],
                "description": m["description"]
            }
            for m in self.config["core_modules"]
        ]

        # 按类别组织可选模块
        for module in self.config["optional_modules"]:
            category = module.get("category", "other")
            cat_name = self.config["module_categories"].get(category, category)

            if cat_name not in categories:
                categories[cat_name] = []

            categories[cat_name].append({
                "name": module["name"],
                "display_name": module["display_name"],
                "description": module["description"],
                "dependencies": module.get("dependencies", [])
            })

        return categories

    def list_presets(self) -> List[Dict]:
        """列出所有预设方案"""
        return [
            {
                "name": p["name"],
                "display_name": p["display_name"],
                "description": p["description"],
                "modules": p["modules"]
            }
            for p in self.config.get("presets", [])
        ]


def main():
    """测试函数"""
    manager = ModuleManager()

    print("=== 可用模块 ===")
    categories = manager.list_available_modules()
    for cat_name, modules in categories.items():
        print(f"\n{cat_name}:")
        for module in modules:
            deps = module.get("dependencies", [])
            deps_str = f" (依赖: {', '.join(deps)})" if deps else ""
            print(f"  - {module['name']:15} | {module['display_name']:12} | {module['description']}{deps_str}")

    print("\n=== 预设方案 ===")
    presets = manager.list_presets()
    for preset in presets:
        print(f"\n{preset['name']:12} | {preset['display_name']:15} | {preset['description']}")
        print(f"  模块: {', '.join(preset['modules'])}")

    print("\n=== 测试: 教育培训方案 ===")
    modules = manager.get_preset_modules("education")
    print(f"选择的模块: {modules}")

    resolved = manager.resolve_dependencies(modules)
    print(f"包含依赖后: {sorted(resolved)}")

    files = manager.get_files_to_copy(resolved)
    print("\n需要复制的文件:")
    for file_type, file_list in files.items():
        print(f"  {file_type}: {file_list}")


if __name__ == "__main__":
    main()
