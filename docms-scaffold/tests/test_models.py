# -*- coding: utf-8 -*-
"""模型层测试

测试数据库模型的创建、关系等
"""

import pytest
from datetime import datetime

from app.models.site import SiteColumn, SiteSetting, ColumnType
from app.models.product import Product, ProductCategory


def test_create_site_column(db_session):
    """测试创建栏目"""
    column = SiteColumn(
        name="测试栏目",
        slug="test-column",
        column_type=ColumnType.PRODUCT,
        is_enabled=True,
        show_in_nav=True,
        sort_order=1
    )

    db_session.add(column)
    db_session.commit()
    db_session.refresh(column)

    # 验证
    assert column.id is not None
    assert column.name == "测试栏目"
    assert column.slug == "test-column"
    assert column.created_at is not None
    assert isinstance(column.created_at, datetime)


def test_create_product(db_session, sample_column):
    """测试创建产品"""
    product = Product(
        column_id=sample_column.id,
        name="智能水培设备",
        slug="smart-hydroponic",
        description_html="<p>测试产品</p>",
        status="online"
    )

    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    # 验证
    assert product.id is not None
    assert product.name == "智能水培设备"
    assert product.slug == "smart-hydroponic"
    assert product.column_id == sample_column.id
    assert product.created_at is not None


def test_product_category_relationship(db_session, sample_column):
    """测试产品和分类的关系"""
    # 创建分类
    category = ProductCategory(
        column_id=sample_column.id,
        name="家用设备",
        slug="home-devices",
        sort_order=1
    )
    db_session.add(category)

    # 创建产品
    product = Product(
        column_id=sample_column.id,
        name="家用水培机",
        slug="home-hydroponic",
        description_html="<p>测试</p>",
        status="online"
    )

    # 关联分类
    product.categories.append(category)

    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    # 验证关系
    assert len(product.categories) == 1
    assert product.categories[0].name == "家用设备"
    assert product.categories[0].slug == "home-devices"


def test_site_setting_creation(db_session):
    """测试站点配置创建"""
    setting = SiteSetting(
        setting_key="company_name",
        value_text="测试公司"
    )

    db_session.add(setting)
    db_session.commit()
    db_session.refresh(setting)

    # 验证
    assert setting.id is not None
    assert setting.setting_key == "company_name"
    assert setting.value_text == "测试公司"
    assert setting.created_at is not None


def test_product_timestamps(db_session, sample_column):
    """测试时间戳自动更新"""
    product = Product(
        column_id=sample_column.id,
        name="测试产品",
        slug="test-product",
        description_html="<p>测试</p>",
        status="online"
    )

    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    created_at = product.created_at
    updated_at = product.updated_at

    # 验证创建时间
    assert created_at is not None
    assert updated_at is not None

    # 更新产品
    product.name = "更新后的产品"
    db_session.commit()
    db_session.refresh(product)

    # 验证更新时间变化
    assert product.updated_at > updated_at
    assert product.created_at == created_at  # 创建时间不变
