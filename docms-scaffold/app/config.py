"""应用配置管理"""

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 项目根目录
BASE_DIR = Path(__file__).parent.parent

# 数据库配置
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./docms.db")

# 应用配置
APP_NAME = os.getenv("APP_NAME", "Docms CMS")
APP_ENV = os.getenv("APP_ENV", "development")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# 站点配置
SITE_NAME = os.getenv("SITE_NAME", "绿芽智能科技")
SITE_TITLE = os.getenv("SITE_TITLE", "智能水培设备领导者")
SITE_DESCRIPTION = os.getenv("SITE_DESCRIPTION", "专业的智能水培设备研发、生产与销售")

# 主题配置 - 已设置为绿色科技主题
ACTIVE_THEME = os.getenv("ACTIVE_THEME", "green-tech")

# 静态文件路径
TEMPLATE_DIR = BASE_DIR / "templates" / ACTIVE_THEME
STATIC_DIR = TEMPLATE_DIR / "static"
MEDIA_DIR = STATIC_DIR / "media" / "uploads"

# 确保媒体目录存在
MEDIA_DIR.mkdir(parents=True, exist_ok=True)


class Settings:
    """应用设置类"""

    def __init__(self):
        self.database_url = DATABASE_URL
        self.app_name = APP_NAME
        self.debug = DEBUG
        self.site_name = SITE_NAME
        self.site_title = SITE_TITLE
        self.site_description = SITE_DESCRIPTION
        self.static_dir = STATIC_DIR
        self.media_dir = MEDIA_DIR
        self.template_dir = TEMPLATE_DIR

    def get_site_settings(self) -> dict[str, Any]:
        """获取站点设置字典"""
        return {
            "site_name": self.site_name,
            "site_title": self.site_title,
            "site_description": self.site_description,
        }


# 创建全局设置实例
settings = Settings()
