# -*- coding: utf-8 -*-
"""服务层测试

测试业务逻辑层的功能是否正确
"""

import pytest
from app.services import product_service, post_service, site_service
from app.models.post import Post
from app.models.site import SiteColumn, ColumnType


def test_get_products_returns_only_online(db_session, sample_column, sample_products):
    """测试只返回上线的产品"""
    products = product_service.get_products(db_session, status="online")

    # 验证所有返回的产品都是 online 状态
    assert all(p.status == "online" for p in products)

    # 10个产品中有5个是 online (偶数ID)
    assert len(products) == 5


def test_get_products_with_limit(db_session, sample_column, sample_products):
    """测试限制返回数量"""
    products = product_service.get_products(db_session, limit=3)

    assert len(products) <= 3


def test_get_product_by_slug(db_session, sample_column, sample_products):
    """测试通过 slug 获取产品"""
    # 获取一个在线产品
    online_product = [p for p in sample_products if p.status == "online"][0]

    product = product_service.get_product_by_slug(db_session, online_product.slug)

    assert product is not None
    assert product.slug == online_product.slug
    assert product.name == online_product.name


def test_get_product_by_slug_not_found(db_session):
    """测试获取不存在的产品"""
    product = product_service.get_product_by_slug(db_session, "nonexistent-slug")

    assert product is None


def test_get_recommended_products(db_session, sample_column, sample_products):
    """测试获取推荐产品"""
    products = product_service.get_products(
        db_session,
        is_recommended=True
    )

    # 验证所有返回的产品都是推荐的
    assert all(p.is_recommended for p in products)

    # 10个产品中ID能被3整除的是推荐产品: 3, 6, 9
    # 但只有偶数ID是online状态: 2, 4, 6, 8, 10
    # 因此只有产品6既是推荐的又是在线的
    assert len(products) == 1
    assert products[0].name == "测试产品 6"


def test_get_product_count(db_session, sample_column, sample_products):
    """测试获取产品总数"""
    # 所有在线产品
    count = product_service.get_product_count(
        db_session,
        column_id=sample_column.id,
        status="online"
    )

    assert count == 5  # 10个产品中有5个是 online


def test_get_column_by_slug(db_session, sample_column):
    """测试通过 slug 获取栏目"""
    column = site_service.get_column_by_slug(db_session, sample_column.slug)

    assert column is not None
    assert column.slug == sample_column.slug
    assert column.name == sample_column.name


def test_get_site_setting(db_session, sample_site_settings):
    """测试获取站点配置"""
    phone = site_service.get_site_setting(db_session, "phone")

    assert phone == "400-123-4567"


def test_get_all_site_settings(db_session, sample_site_settings):
    """测试获取所有站点配置"""
    settings = site_service.get_all_site_settings(db_session)

    assert isinstance(settings, dict)
    assert "phone" in settings
    assert "email" in settings
    assert settings["phone"] == "400-123-4567"


# ===== Post Service Tests =====

@pytest.fixture
def sample_post_column(db_session):
    """创建示例文章栏目"""
    column = SiteColumn(
        name="新闻资讯",
        slug="news",
        column_type=ColumnType.POST,
        is_enabled=True,
        show_in_nav=True,
        sort_order=2
    )
    db_session.add(column)
    db_session.commit()
    db_session.refresh(column)
    return column


@pytest.fixture
def sample_posts(db_session, sample_post_column):
    """创建示例文章"""
    posts = [
        Post(
            column_id=sample_post_column.id,
            title=f"测试文章 {i}",
            slug=f"test-post-{i}",
            summary=f"这是测试文章 {i} 的摘要",
            content_html=f"<p>测试文章 {i} 的内容</p>",
            status="published" if i % 2 == 0 else "draft",
            is_recommended=(i % 3 == 0)
        )
        for i in range(1, 11)
    ]

    for post in posts:
        db_session.add(post)

    db_session.commit()

    for post in posts:
        db_session.refresh(post)

    return posts


def test_get_posts_returns_only_published(db_session, sample_post_column, sample_posts):
    """测试只返回已发布的文章"""
    posts = post_service.get_posts(db_session, status="published")

    # 验证所有返回的文章都是 published 状态
    assert all(p.status == "published" for p in posts)

    # 10篇文章中有5篇是 published (偶数ID)
    assert len(posts) == 5


def test_get_posts_with_limit(db_session, sample_post_column, sample_posts):
    """测试限制返回数量"""
    posts = post_service.get_posts(db_session, limit=3)

    assert len(posts) <= 3


def test_get_post_by_slug(db_session, sample_post_column, sample_posts):
    """测试通过 slug 获取文章"""
    # 获取一个已发布文章
    published_post = [p for p in sample_posts if p.status == "published"][0]

    post = post_service.get_post_by_slug(db_session, published_post.slug)

    assert post is not None
    assert post.slug == published_post.slug
    assert post.title == published_post.title


def test_get_post_by_slug_not_found(db_session):
    """测试获取不存在的文章"""
    post = post_service.get_post_by_slug(db_session, "nonexistent-slug")

    assert post is None


def test_get_recommended_posts(db_session, sample_post_column, sample_posts):
    """测试获取推荐文章"""
    posts = post_service.get_posts(
        db_session,
        is_recommended=True,
        status="published"
    )

    # 验证所有返回的文章都是推荐的
    assert all(p.is_recommended for p in posts)

    # 10篇文章中ID能被3整除的是推荐文章: 3, 6, 9
    # 但只有偶数ID是published状态: 2, 4, 6, 8, 10
    # 因此只有文章6既是推荐的又是已发布的
    assert len(posts) == 1
    assert posts[0].title == "测试文章 6"


def test_get_post_count(db_session, sample_post_column, sample_posts):
    """测试获取文章总数"""
    count = post_service.get_post_count(
        db_session,
        column_id=sample_post_column.id,
        status="published"
    )

    assert count == 5  # 10篇文章中有5篇是 published


# ===== Navigation and Settings Tests =====

def test_get_navigation_only_enabled(db_session):
    """测试只获取启用的导航栏目"""
    # 创建多个栏目，部分禁用
    columns = [
        SiteColumn(name="产品", slug="products", column_type=ColumnType.PRODUCT,
                   is_enabled=True, show_in_nav=True, sort_order=1),
        SiteColumn(name="新闻", slug="news", column_type=ColumnType.POST,
                   is_enabled=True, show_in_nav=True, sort_order=2),
        SiteColumn(name="隐藏栏目", slug="hidden", column_type=ColumnType.POST,
                   is_enabled=False, show_in_nav=True, sort_order=3),
        SiteColumn(name="不显示在导航", slug="no-nav", column_type=ColumnType.POST,
                   is_enabled=True, show_in_nav=False, sort_order=4),
    ]

    for col in columns:
        db_session.add(col)

    db_session.commit()

    # 获取导航
    nav = site_service.get_navigation(db_session)

    # 只应该返回 enabled=True 且 show_in_nav=True 的栏目
    assert len(nav) == 2
    assert all(col.is_enabled for col in nav)
    assert all(col.show_in_nav for col in nav)


def test_get_navigation_sorted(db_session):
    """测试导航按排序顺序返回"""
    columns = [
        SiteColumn(name="第三", slug="third", column_type=ColumnType.PRODUCT,
                   is_enabled=True, show_in_nav=True, sort_order=3),
        SiteColumn(name="第一", slug="first", column_type=ColumnType.POST,
                   is_enabled=True, show_in_nav=True, sort_order=1),
        SiteColumn(name="第二", slug="second", column_type=ColumnType.POST,
                   is_enabled=True, show_in_nav=True, sort_order=2),
    ]

    for col in columns:
        db_session.add(col)

    db_session.commit()

    nav = site_service.get_navigation(db_session)

    # 验证排序
    assert nav[0].name == "第一"
    assert nav[1].name == "第二"
    assert nav[2].name == "第三"


def test_get_site_setting_nonexistent(db_session):
    """测试获取不存在的站点配置"""
    value = site_service.get_site_setting(db_session, "nonexistent_key")

    assert value is None


# ===== Product Category Tests =====

@pytest.fixture
def sample_product_categories(db_session, sample_column):
    """创建示例产品分类"""
    from app.models.product import ProductCategory

    categories = [
        ProductCategory(
            column_id=sample_column.id,
            name=f"分类 {i}",
            slug=f"category-{i}",
            is_visible=(i % 2 == 0),
            sort_order=i
        )
        for i in range(1, 6)
    ]

    for cat in categories:
        db_session.add(cat)

    db_session.commit()

    for cat in categories:
        db_session.refresh(cat)

    return categories


def test_get_product_categories_visible_only(db_session, sample_column, sample_product_categories):
    """测试只获取可见的产品分类"""
    categories = product_service.get_product_categories(
        db_session,
        column_id=sample_column.id,
        visible_only=True
    )

    # 只返回可见的分类
    assert all(cat.is_visible for cat in categories)
    assert len(categories) == 2  # 5个分类中有2个是可见的 (偶数ID: 2, 4)


def test_get_product_categories_all(db_session, sample_column, sample_product_categories):
    """测试获取所有产品分类（包括不可见）"""
    categories = product_service.get_product_categories(
        db_session,
        column_id=sample_column.id,
        visible_only=False
    )

    assert len(categories) == 5


def test_get_product_categories_sorted(db_session, sample_column, sample_product_categories):
    """测试分类按排序顺序返回"""
    categories = product_service.get_product_categories(
        db_session,
        column_id=sample_column.id,
        visible_only=False
    )

    # 验证排序
    for i, cat in enumerate(categories, start=1):
        assert cat.slug == f"category-{i}"
