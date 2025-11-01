# -*- coding: utf-8 -*-
"""
brownsbay-language-school.nz - Application Entry Point

启动命令:
    python app.py

或使用 uvicorn:
    uvicorn app:app --reload --host 0.0.0.0 --port 8000
"""

from pathlib import Path

from app.main import create_app
from app.config import SiteConfig

# 加载站点配置
config = SiteConfig.from_yaml(Path(__file__).parent / "site.yaml")

# 创建应用实例
app = create_app(site_config=config)

if __name__ == "__main__":
    import uvicorn

    # 不使用 reload 模式时直接传递 app 对象
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level=config.log_level.lower()
    )
