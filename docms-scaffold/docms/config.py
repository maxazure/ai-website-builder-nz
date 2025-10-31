# -*- coding: utf-8 -*-
"""Docms Configuration

站点配置管理，支持从 YAML 文件加载
"""

from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


class SiteConfig(BaseModel):
    """站点配置"""

    # 基本信息
    site_name: str = "Docms Site"
    site_description: str = "A website powered by Docms"
    site_url: str = "http://localhost:8000"

    # 路径配置
    base_dir: Path = Field(default_factory=lambda: Path.cwd())
    template_dir: Path = Field(default_factory=lambda: Path.cwd() / "templates")
    static_dir: Path = Field(default_factory=lambda: Path.cwd() / "templates" / "static")
    media_dir: Path = Field(default_factory=lambda: Path.cwd() / "instance" / "media")

    # 数据库配置
    database_url: str = "sqlite:///./instance/database.db"

    # 主题配置
    theme: str = "default"
    available_themes: list[str] = ["default"]

    # 日志配置
    log_level: str = "INFO"

    # 缓存配置
    enable_cache: bool = True
    cache_ttl: int = 300  # 5 分钟

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_yaml(cls, yaml_path: Path) -> "SiteConfig":
        """从 YAML 文件加载配置"""
        import yaml

        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # 转换路径字符串为 Path 对象
        if "base_dir" in data:
            data["base_dir"] = Path(data["base_dir"])
        if "template_dir" in data:
            data["template_dir"] = Path(data["template_dir"])
        if "static_dir" in data:
            data["static_dir"] = Path(data["static_dir"])
        if "media_dir" in data:
            data["media_dir"] = Path(data["media_dir"])

        return cls(**data)

    def save_yaml(self, yaml_path: Path):
        """保存配置到 YAML 文件"""
        import yaml

        data = self.model_dump()
        # 转换 Path 对象为字符串
        for key in ["base_dir", "template_dir", "static_dir", "media_dir"]:
            if key in data:
                data[key] = str(data[key])

        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True, default_flow_style=False)
