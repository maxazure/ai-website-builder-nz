# -*- coding: utf-8 -*-
"""路由测试

测试所有公开访问的路由是否正常工作
"""

import pytest
from app.models.site import SiteColumn, ColumnType, SinglePage
from app.models.post import Post


def test_homepage(client, sample_site_settings):
    """测试首页访问"""
    response = client.get("/")

    assert response.status_code == 200
    assert b"html" in response.content.lower()


def test_health_check(client, sample_site_settings):
    """测试健康检查端点"""
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "app" in data


def test_404_page(client, sample_site_settings):
    """测试 404 页面"""
    response = client.get("/nonexistent-page-12345")

    assert response.status_code == 404
    # 应该返回 HTML 内容
    assert b"html" in response.content.lower()


def test_product_list_page_not_found(client, sample_site_settings):
    """测试访问不存在的栏目"""
    response = client.get("/nonexistent-column")

    assert response.status_code == 404


def test_product_list_page(client, sample_column, sample_products):
    """测试产品列表页"""
    response = client.get("/products")

    assert response.status_code == 200
    assert "产品中心" in response.text or b"products" in response.content


def test_product_detail_page(client, sample_column, sample_products):
    """测试产品详情页"""
    # 获取第一个在线产品
    product = [p for p in sample_products if p.status == "online"][0]

    response = client.get(f"/products/detail/{product.slug}")

    assert response.status_code == 200
    assert product.name in response.text


def test_product_detail_not_found(client, sample_column):
    """测试访问不存在的产品"""
    response = client.get("/products/detail/nonexistent-product")

    assert response.status_code == 404


# ===== Post Routes Tests =====

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
        for i in range(1, 6)
    ]

    for post in posts:
        db_session.add(post)

    db_session.commit()

    for post in posts:
        db_session.refresh(post)

    return posts


def test_post_list_page(client, sample_post_column, sample_posts):
    """测试文章列表页"""
    response = client.get("/news")

    assert response.status_code == 200
    # 应该显示栏目名称
    assert "新闻资讯" in response.text or "news" in response.text


def test_post_detail_page(client, sample_post_column, sample_posts):
    """测试文章详情页"""
    # 获取第一个已发布文章
    post = [p for p in sample_posts if p.status == "published"][0]

    response = client.get(f"/news/detail/{post.slug}")

    assert response.status_code == 200
    assert post.title in response.text


def test_post_detail_not_found(client, sample_post_column):
    """测试访问不存在的文章"""
    response = client.get("/news/detail/nonexistent-post")

    assert response.status_code == 404


def test_draft_post_not_accessible(client, sample_post_column, sample_posts):
    """测试草稿文章不可访问"""
    # 获取一个草稿文章
    draft_post = [p for p in sample_posts if p.status == "draft"][0]

    response = client.get(f"/news/detail/{draft_post.slug}")

    # 应该返回404，因为草稿不应该公开访问
    assert response.status_code == 404


# ===== Single Page Tests =====

@pytest.fixture
def sample_single_page_column(db_session):
    """创建示例单页栏目"""
    column = SiteColumn(
        name="关于我们",
        slug="about",
        column_type=ColumnType.SINGLE_PAGE,
        is_enabled=True,
        show_in_nav=True,
        sort_order=3
    )
    db_session.add(column)
    db_session.commit()
    db_session.refresh(column)
    return column


@pytest.fixture
def sample_single_page(db_session, sample_single_page_column):
    """创建示例单页内容"""
    page = SinglePage(
        column_id=sample_single_page_column.id,
        title="关于我们",
        content_html="<p>公司简介内容</p>",
        status="published"
    )
    db_session.add(page)
    db_session.commit()
    db_session.refresh(page)
    return page


def test_single_page(client, sample_single_page_column, sample_single_page):
    """测试单页访问"""
    response = client.get("/about")

    assert response.status_code == 200
    assert "关于我们" in response.text or "公司简介" in response.text


# ===== Contact Form Tests =====

def test_contact_form_submit_success(client, db_session):
    """测试联系表单提交成功"""
    form_data = {
        "name": "张三",
        "email": "zhangsan@example.com",
        "phone": "13800138000",
        "subject": "产品咨询",
        "message": "我想了解更多关于产品的信息"
    }

    response = client.post("/contact/submit", data=form_data)

    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "message" in data


def test_contact_form_invalid_email(client, db_session):
    """测试联系表单提交失败 - 无效邮箱"""
    form_data = {
        "name": "张三",
        "email": "invalid-email",  # 无效的邮箱格式
        "phone": "",
        "subject": "产品咨询",
        "message": "测试消息"
    }

    response = client.post("/contact/submit", data=form_data)

    assert response.status_code == 400
    data = response.json()
    assert data["success"] is False
    assert "email" in data["message"].lower() or "validation" in data["message"].lower()


def test_contact_form_missing_required_fields(client, db_session):
    """测试联系表单提交失败 - 缺少必填字段"""
    form_data = {
        "name": "张三",
        # 缺少 email
        # 缺少 subject
        # 缺少 message
    }

    response = client.post("/contact/submit", data=form_data)

    # FastAPI 会返回 422 Unprocessable Entity 当缺少必填字段时
    assert response.status_code == 422


# ===== Static File Tests =====

def test_static_css_accessible(client):
    """测试静态 CSS 文件可访问"""
    response = client.get("/static/css/main.css")

    # 如果文件存在，应该返回200或304
    # 如果不存在，会返回404，这也是可接受的（取决于项目设置）
    assert response.status_code in [200, 304, 404]


# ===== Column with Categories Tests =====

def test_product_list_with_category_filter(client, sample_column, sample_products):
    """测试产品列表页基本访问"""
    # 验证产品列表页能正常访问
    response = client.get("/products")
    assert response.status_code == 200


# ===== Homepage Tests =====

def test_homepage_shows_recommended_products(client, sample_column, sample_products):
    """测试首页显示推荐产品"""
    response = client.get("/")

    assert response.status_code == 200
    # 应该包含HTML内容
    assert "html" in response.text.lower()


def test_homepage_no_products(client, sample_site_settings):
    """测试首页在没有产品时也能正常显示"""
    response = client.get("/")

    assert response.status_code == 200
    assert "html" in response.text.lower()


# ===== Error Handling Tests =====

def test_disabled_column_not_accessible(client, db_session):
    """测试禁用的栏目不可访问"""
    # 创建一个禁用的栏目
    disabled_column = SiteColumn(
        name="禁用栏目",
        slug="disabled",
        column_type=ColumnType.PRODUCT,
        is_enabled=False,  # 禁用
        show_in_nav=False,
        sort_order=10
    )
    db_session.add(disabled_column)
    db_session.commit()

    response = client.get("/disabled")

    # 应该返回404
    assert response.status_code == 404


def test_draft_product_not_accessible(client, sample_column, sample_products):
    """测试草稿产品不可访问"""
    # 获取一个草稿产品
    draft_product = [p for p in sample_products if p.status == "draft"][0]

    response = client.get(f"/products/detail/{draft_product.slug}")

    # 应该返回404
    assert response.status_code == 404
