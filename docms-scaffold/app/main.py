# -*- coding: utf-8 -*-
"""FastAPI Application Entry Point

Docms CMS - Green Bud Smart Technology Website
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from app.config import APP_ENV, settings
from app.middleware.error_handlers import (
    global_exception_handler,
    http_exception_handler,
)
from app.routes import frontend
from app.utils.logger import setup_logging

# 初始化日志系统
logger = setup_logging("docms", log_level="DEBUG" if settings.debug else "INFO")
logger.info(f"Starting {settings.app_name} in {APP_ENV} mode")

# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

# 注册全局异常处理器
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

# Mount static files
app.mount("/static", StaticFiles(directory=str(settings.static_dir)), name="static")


# Health check endpoint (must be registered BEFORE frontend router's catchall)
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    logger.debug("Health check endpoint accessed")
    return {"status": "ok", "app": settings.app_name}


# Include routers
app.include_router(frontend.router)
logger.info("Application routes registered")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
