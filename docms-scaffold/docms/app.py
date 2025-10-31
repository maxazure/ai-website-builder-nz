# -*- coding: utf-8 -*-
"""Docms Application Factory

创建可配置的 FastAPI 应用实例
"""

import logging
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from docms.config import SiteConfig

logger = logging.getLogger("docms")


def create_app(
    site_config: Optional[SiteConfig] = None,
    template_dir: Optional[Path] = None,
    static_dir: Optional[Path] = None,
    database_url: Optional[str] = None,
) -> FastAPI:
    """
    创建 FastAPI 应用实例

    Args:
        site_config: 站点配置对象
        template_dir: 模板目录路径
        static_dir: 静态文件目录路径
        database_url: 数据库 URL

    Returns:
        配置好的 FastAPI 应用实例
    """
    # 使用默认配置或传入的配置
    if site_config is None:
        site_config = SiteConfig()

    # 创建 FastAPI 应用
    app = FastAPI(
        title=site_config.site_name,
        description=site_config.site_description,
        version="1.0.0",
    )

    # 存储配置到 app.state
    app.state.config = site_config
    app.state.template_dir = template_dir or site_config.template_dir
    app.state.static_dir = static_dir or site_config.static_dir
    app.state.database_url = database_url or site_config.database_url

    # 配置日志
    logging.basicConfig(
        level=getattr(logging, site_config.log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 注册路由
    register_routes(app)

    # 挂载静态文件
    if app.state.static_dir.exists():
        app.mount(
            "/static",
            StaticFiles(directory=str(app.state.static_dir)),
            name="static"
        )

    # 注册异常处理
    register_exception_handlers(app)

    # 启动事件
    @app.on_event("startup")
    async def startup_event():
        logger.info(f"🚀 {site_config.site_name} 启动成功")
        logger.info(f"📁 模板目录: {app.state.template_dir}")
        logger.info(f"📦 数据库: {app.state.database_url}")

    return app


def register_routes(app: FastAPI):
    """注册所有路由"""
    # 导入路由时需要访问 app.state，所以在这里导入
    from docms.routes import frontend, health

    # 注册路由
    app.include_router(health.router, tags=["health"])
    app.include_router(frontend.router, tags=["frontend"])


def register_exception_handlers(app: FastAPI):
    """注册异常处理器"""
    from fastapi.exceptions import HTTPException
    from fastapi.responses import HTMLResponse

    @app.exception_handler(404)
    async def not_found_handler(request: Request, exc: HTTPException):
        """404 错误处理"""
        try:
            templates = Jinja2Templates(directory=str(app.state.template_dir))
            return templates.TemplateResponse(
                "404.html",
                {"request": request},
                status_code=404
            )
        except Exception:
            return HTMLResponse(
                content="<h1>404 - Page Not Found</h1>",
                status_code=404
            )

    @app.exception_handler(500)
    async def internal_error_handler(request: Request, exc: Exception):
        """500 错误处理"""
        logger.error(f"Internal error: {exc}")
        try:
            templates = Jinja2Templates(directory=str(app.state.template_dir))
            return templates.TemplateResponse(
                "500.html",
                {"request": request},
                status_code=500
            )
        except Exception:
            return HTMLResponse(
                content="<h1>500 - Internal Server Error</h1>",
                status_code=500
            )
