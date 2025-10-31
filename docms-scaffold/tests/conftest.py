# -*- coding: utf-8 -*-
"""Pytest 配置和共享 fixtures

提供测试所需的数据库会话、测试客户端等共享资源
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.database import Base, get_db
from app.utils.cache import clear_all_caches

# Import all models FIRST to register them with Base.metadata
from app.models import (
    SiteColumn, SiteSetting, SinglePage,
    Product, ProductCategory, ProductCategoryLink,
    Post, PostCategory, PostCategoryLink,
    MediaFile, ContactMessage,
    CustomFieldDef, CustomFieldOption, ProductCustomFieldValue
)

# Import app AFTER models are registered
from app.main import app


# 测试数据库 URL (使用共享内存数据库，避免每个连接创建新数据库)
# file:memdb1?mode=memory&cache=shared 允许多个连接共享同一个内存数据库
TEST_DATABASE_URL = "sqlite:///file:memdb1?mode=memory&cache=shared&uri=true"


@pytest.fixture(scope="function")
def db_engine():
    """
    创建测试数据库引擎

    每个测试函数使用独立的数据库实例
    """
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False, "uri": True},
        poolclass=None  # Disable connection pooling for testing
    )

    # 创建所有表
    Base.metadata.create_all(bind=engine)

    yield engine

    # 测试结束后删除所有表
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture(scope="function")
def db_session(db_engine):
    """
    创建数据库会话

    每个测试函数使用独立的会话
    """
    # Clear all caches before each test
    clear_all_caches()

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=db_engine
    )
    session = TestingSessionLocal()

    yield session

    session.close()

    # Clear caches after test
    clear_all_caches()


@pytest.fixture(scope="function")
def client(db_session):
    """
    创建测试客户端

    自动覆盖数据库依赖，使用测试数据库
    """
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def sample_site_settings(db_session):
    """创建示例站点配置"""
    from app.models.site import SiteSetting

    settings = [
        SiteSetting(setting_key="phone", value_text="400-123-4567"),
        SiteSetting(setting_key="email", value_text="contact@example.com"),
        SiteSetting(setting_key="address", value_text="深圳市南山区"),
    ]

    for setting in settings:
        db_session.add(setting)

    db_session.commit()

    return settings


@pytest.fixture
def sample_column(db_session):
    """创建示例栏目"""
    from app.models.site import SiteColumn, ColumnType

    column = SiteColumn(
        name="产品中心",
        slug="products",
        column_type=ColumnType.PRODUCT,
        is_enabled=True,
        show_in_nav=True,
        sort_order=1
    )

    db_session.add(column)
    db_session.commit()
    db_session.refresh(column)

    return column


@pytest.fixture
def sample_products(db_session, sample_column):
    """创建示例产品"""
    from app.models.product import Product

    products = [
        Product(
            column_id=sample_column.id,
            name=f"测试产品 {i}",
            slug=f"test-product-{i}",
            summary=f"这是测试产品 {i} 的简介",
            description_html=f"<p>测试产品 {i} 的详细描述</p>",
            status="online" if i % 2 == 0 else "draft",
            is_recommended=(i % 3 == 0)
        )
        for i in range(1, 11)
    ]

    for product in products:
        db_session.add(product)

    db_session.commit()

    for product in products:
        db_session.refresh(product)

    return products
