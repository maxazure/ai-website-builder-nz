# 站点完善指南 - Claude Code 工作手册

> 本文档指导如何使用 Claude Code 完善通过 CLI 工具生成的站点

## 文档概述

本指南面向 Claude Code，提供系统化的步骤来完善一个通过 `cli.create_site` 创建的基础站点。

**目标**: 将基础站点框架转变为功能完整、内容丰富的企业官网。

**主要工作**:
1. 生成数据库内容（产品、文章、栏目等）
2. 完善页面模板（HTML + Jinja2）
3. 优化前端样式（Tailwind CSS）
4. 实现特殊功能（表单、搜索等）

---

## 第一阶段：内容生成（Content Generation）

### 1.1 准备工作

**检查站点状态**:
```bash
cd /d/projects/<site-name>
ls -la

# 确认以下文件存在：
# - site.yaml
# - app.py
# - templates/
# - instance/
```

**了解站点信息**:
```bash
# 查看站点配置
cat site.yaml

# 记录以下信息：
# - site_name: 公司名称
# - site_description: 公司描述
# - 行业类型（从描述推断）
```

### 1.2 生成数据库填充脚本

**步骤 1: 分析需求**

根据 `site.yaml` 中的信息，确定：
- 行业类型（如：智能水培、能源、科技等）
- 产品类型（家用/商用/工业等）
- 目标客户（家庭用户/企业客户/政府机构等）

**步骤 2: 生成 SQL 脚本**

创建 `seed_data.sql`，包含以下表的数据：

#### 1. site_setting (站点配置)

```sql
-- 站点配置
DELETE FROM site_setting;

INSERT INTO site_setting (setting_key, value_text, description, created_at, updated_at) VALUES
    ('site_name', '<从 site.yaml 获取>', '站点名称', datetime('now'), datetime('now')),
    ('site_description', '<从 site.yaml 获取>', '站点描述', datetime('now'), datetime('now')),
    ('phone', '400-XXX-XXXX', '联系电话', datetime('now'), datetime('now')),
    ('email', 'contact@example.com', '联系邮箱', datetime('now'), datetime('now')),
    ('address', '<合理的地址>', '公司地址', datetime('now'), datetime('now')),
    ('about_us', '<200字左右的公司介绍>', '关于我们', datetime('now'), datetime('now')),
    ('business_hours', '周一至周五 9:00-18:00', '营业时间', datetime('now'), datetime('now')),
    ('wechat', 'company_wechat', '微信号', datetime('now'), datetime('now'));
```

**要求**:
- 电话号码格式合理（400 开头或区号）
- 邮箱格式正确
- 地址符合行业特点（如：科技园、工业区等）
- 公司介绍真实、专业，不使用 Lorem Ipsum

#### 2. site_column (栏目)

```sql
-- 栏目配置
DELETE FROM site_column;

INSERT INTO site_column (name, slug, column_type, description, is_enabled, show_in_nav, sort_order, created_at, updated_at) VALUES
    ('首页', 'home', 'CUSTOM', '网站首页', 1, 0, 0, datetime('now'), datetime('now')),
    ('产品中心', 'products', 'PRODUCT', '产品展示', 1, 1, 1, datetime('now'), datetime('now')),
    ('解决方案', 'solutions', 'POST', '解决方案', 1, 1, 2, datetime('now'), datetime('now')),
    ('新闻资讯', 'news', 'POST', '公司动态', 1, 1, 3, datetime('now'), datetime('now')),
    ('关于我们', 'about', 'SINGLE_PAGE', '公司介绍', 1, 1, 4, datetime('now'), datetime('now')),
    ('联系我们', 'contact', 'SINGLE_PAGE', '联系方式', 1, 1, 5, datetime('now'), datetime('now'));
```

**要求**:
- slug 使用小写字母和连字符
- column_type 正确：PRODUCT/POST/SINGLE_PAGE/CUSTOM
- sort_order 递增（决定导航栏顺序）
- is_enabled = 1, show_in_nav = 1（首页除外）

#### 3. product_category (产品分类)

```sql
-- 产品分类（根据行业特点创建 3-5 个）
DELETE FROM product_category;

INSERT INTO product_category (column_id, name, slug, description, is_visible, sort_order, created_at, updated_at) VALUES
    (2, '<分类1>', '<slug1>', '<分类描述>', 1, 1, datetime('now'), datetime('now')),
    (2, '<分类2>', '<slug2>', '<分类描述>', 1, 2, datetime('now'), datetime('now')),
    (2, '<分类3>', '<slug3>', '<分类描述>', 1, 3, datetime('now'), datetime('now'));
```

**示例（智能水培行业）**:
- 家用水培设备
- 商用水培系统
- 配套耗材
- 智能控制系统

**示例（能源行业）**:
- 太阳能系统
- 风能系统
- 储能设备
- 智能电网

#### 4. product (产品)

```sql
-- 产品（创建 8-12 个）
DELETE FROM product;

INSERT INTO product (column_id, name, slug, model_number, summary, description_html, price, status, is_recommended, sort_order, view_count, created_at, updated_at) VALUES
    (2, '<产品名称>', '<slug>', '<型号>',
     '<50字简介>',
     '<200-300字 HTML 描述>',
     <价格>, 'online', <0或1>, <排序>, 0,
     datetime('now'), datetime('now'));
```

**要求**:
- name: 真实的产品名称（如：智能水培机 Pro、家用太阳能板 5KW 等）
- model_number: 合理的型号（如：HP-2000、SE-5K 等）
- summary: 50 字左右，突出产品特点
- description_html: 200-300 字，使用 HTML 标签（`<p>`, `<ul>`, `<h3>` 等）
- price: 合理的价格（家用：300-3000，商用：5000-50000）
- status: 'online' 或 'draft'（至少 8 个 online）
- is_recommended: 至少 3 个产品设为 1（推荐产品）

**HTML 描述模板**:
```html
<h3>产品特点</h3>
<ul>
    <li>特点 1</li>
    <li>特点 2</li>
    <li>特点 3</li>
</ul>

<h3>技术参数</h3>
<p>尺寸：XXX</p>
<p>功率：XXX</p>
<p>容量：XXX</p>

<h3>适用场景</h3>
<p>详细说明适用场景...</p>
```

#### 5. product_category_link (产品分类关联)

```sql
-- 产品分类关联
DELETE FROM product_category_link;

INSERT INTO product_category_link (product_id, category_id) VALUES
    (1, 1),  -- 产品1 -> 分类1
    (2, 1),  -- 产品2 -> 分类1
    (3, 2);  -- 产品3 -> 分类2
```

**要求**: 每个产品至少关联 1 个分类

#### 6. post_category (文章分类)

```sql
-- 文章分类
DELETE FROM post_category;

INSERT INTO post_category (column_id, name, slug, description, is_visible, sort_order, created_at, updated_at) VALUES
    (3, '技术方案', 'tech-solutions', '技术解决方案', 1, 1, datetime('now'), datetime('now')),
    (4, '公司动态', 'company-news', '公司新闻', 1, 1, datetime('now'), datetime('now')),
    (4, '行业资讯', 'industry-news', '行业动态', 1, 2, datetime('now'), datetime('now'));
```

#### 7. post (文章)

```sql
-- 文章（创建 6-10 篇）
DELETE FROM post;

INSERT INTO post (column_id, title, slug, summary, content_html, status, is_recommended, author, view_count, created_at, updated_at) VALUES
    (3, '<文章标题>', '<slug>',
     '<100字摘要>',
     '<400-600字 HTML 内容>',
     'published', <0或1>, '<作者名>', 0,
     datetime('now'), datetime('now'));
```

**要求**:
- title: 与行业相关的标题（如：《智能水培技术在家庭中的应用》）
- summary: 100 字左右摘要
- content_html: 400-600 字，使用 `<h2>`, `<p>`, `<ul>` 等标签
- status: 'published' 或 'draft'（至少 6 篇 published）
- is_recommended: 至少 3 篇设为 1

#### 8. single_page (单页内容)

```sql
-- 单页内容
DELETE FROM single_page;

-- 关于我们
INSERT INTO single_page (column_id, title, content_html, status, created_at, updated_at) VALUES
    (5, '关于我们', '<HTML 内容>', 'published', datetime('now'), datetime('now'));

-- 联系我们
INSERT INTO single_page (column_id, title, content_html, status, created_at, updated_at) VALUES
    (6, '联系我们', '<HTML 内容>', 'published', datetime('now'), datetime('now'));
```

**关于我们内容结构**:
```html
<h2>公司简介</h2>
<p>公司介绍文字...</p>

<h2>发展历程</h2>
<ul>
    <li>2020年：成立</li>
    <li>2021年：XXX</li>
    <li>2023年：XXX</li>
</ul>

<h2>企业文化</h2>
<p>愿景、使命、价值观...</p>

<h2>团队介绍</h2>
<p>团队规模、核心成员...</p>
```

**联系我们内容结构**:
```html
<h2>联系方式</h2>
<p><strong>电话：</strong>400-XXX-XXXX</p>
<p><strong>邮箱：</strong>contact@example.com</p>
<p><strong>地址：</strong>完整地址</p>

<h2>营业时间</h2>
<p>周一至周五：9:00-18:00</p>

<h2>在线留言</h2>
<p>请填写下方表单，我们会尽快回复您。</p>
```

### 1.3 数据质量要求

**内容真实性**:
- ❌ 不要使用 "Lorem Ipsum" 或占位文本
- ✅ 生成真实、专业的内容
- ✅ 符合行业特点和专业术语

**数据完整性**:
- ✅ 所有外键关联正确
- ✅ slug 唯一且合理
- ✅ 日期时间使用 `datetime('now')`
- ✅ 所有必填字段都有值

**推荐内容**:
- 至少 3 个推荐产品（is_recommended=1）
- 至少 3 篇推荐文章（is_recommended=1）
- 推荐内容会显示在首页

---

## 第二阶段：模板开发（Template Development）

### 2.1 模板架构

**模板层次结构**:
```
templates/
├── base.html              # 基础布局（已有）
├── home.html              # 首页（需完善）
├── product_list.html      # 产品列表（需创建）
├── product_detail.html    # 产品详情（需创建）
├── post_list.html         # 文章列表（需创建）
├── post_detail.html       # 文章详情（需创建）
├── single_page.html       # 单页（需创建）
├── contact.html           # 联系我们（可选，自定义）
├── 404.html               # 404 页面（已有）
├── 500.html               # 500 页面（已有）
└── components/            # 组件目录
    ├── navigation.html    # 导航组件
    ├── footer.html        # 页脚组件
    └── product_card.html  # 产品卡片组件
```

### 2.2 base.html 完善

当前 `base.html` 是基础版本，需要完善为功能完整的布局。

**关键要素**:

#### 1. HTML Head
```jinja2
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{% block meta_description %}{{ site_settings.site_description }}{% endblock %}">
    <meta name="keywords" content="{% block meta_keywords %}{% endblock %}">
    <title>{% block title %}{{ site_settings.site_name }}{% endblock %}</title>

    <!-- Favicon -->
    <link rel="icon" href="/static/images/favicon.ico">

    <!-- CSS -->
    <link rel="stylesheet" href="/static/css/main.css">
    {% block extra_css %}{% endblock %}
</head>
```

#### 2. 导航栏
```jinja2
<nav class="navbar">
    <div class="container">
        <div class="navbar-brand">
            <a href="/" class="logo">
                <!-- 如果有 logo 图片 -->
                <!-- <img src="/static/images/logo.png" alt="{{ site_settings.site_name }}"> -->
                <span>{{ site_settings.site_name }}</span>
            </a>
        </div>

        <ul class="navbar-menu">
            {% for column in navigation %}
            <li class="navbar-item">
                <a href="/{{ column.slug }}"
                   class="navbar-link {% if request.path == '/' + column.slug %}active{% endif %}">
                    {{ column.name }}
                </a>
            </li>
            {% endfor %}
        </ul>

        <!-- 移动端菜单按钮 -->
        <button class="navbar-burger" id="navbarBurger">
            <span></span>
            <span></span>
            <span></span>
        </button>
    </div>
</nav>
```

#### 3. 主要内容区
```jinja2
<main class="main-content">
    {% block content %}{% endblock %}
</main>
```

#### 4. 页脚
```jinja2
<footer class="footer">
    <div class="container">
        <div class="footer-content">
            <div class="footer-section">
                <h3>关于我们</h3>
                <p>{{ site_settings.site_description }}</p>
            </div>

            <div class="footer-section">
                <h3>联系方式</h3>
                <p>电话：{{ site_settings.phone }}</p>
                <p>邮箱：{{ site_settings.email }}</p>
                <p>地址：{{ site_settings.address }}</p>
            </div>

            <div class="footer-section">
                <h3>快速链接</h3>
                <ul>
                    {% for column in navigation %}
                    <li><a href="/{{ column.slug }}">{{ column.name }}</a></li>
                    {% endfor %}
                </ul>
            </div>
        </div>

        <div class="footer-bottom">
            <p>&copy; 2025 {{ site_settings.site_name }}. All rights reserved.</p>
        </div>
    </div>
</footer>
```

#### 5. JavaScript
```jinja2
<!-- 移动端菜单脚本 -->
<script>
document.getElementById('navbarBurger').addEventListener('click', function() {
    document.querySelector('.navbar-menu').classList.toggle('is-active');
    this.classList.toggle('is-active');
});
</script>

{% block extra_js %}{% endblock %}
</body>
</html>
```

### 2.3 home.html 完善

首页需要展示：
1. Hero 区域（主视觉）
2. 推荐产品
3. 推荐文章/解决方案
4. 公司优势/特点
5. 联系方式

**完整模板**:
```jinja2
{% extends "base.html" %}

{% block title %}首页 - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<!-- Hero Section -->
<section class="hero">
    <div class="container">
        <div class="hero-content">
            <h1 class="hero-title">{{ site_settings.site_name }}</h1>
            <p class="hero-subtitle">{{ site_settings.site_description }}</p>
            <div class="hero-buttons">
                <a href="/products" class="btn btn-primary">查看产品</a>
                <a href="/contact" class="btn btn-secondary">联系我们</a>
            </div>
        </div>
    </div>
</section>

<!-- Featured Products -->
<section class="featured-products section">
    <div class="container">
        <h2 class="section-title">推荐产品</h2>
        <p class="section-subtitle">精选优质产品，满足您的需求</p>

        <div class="product-grid">
            {% for product in featured_products %}
            <div class="product-card">
                <div class="product-image">
                    {% if product.cover_image %}
                    <img src="{{ product.cover_image }}" alt="{{ product.name }}">
                    {% else %}
                    <div class="product-placeholder">
                        <span>{{ product.name[0] }}</span>
                    </div>
                    {% endif %}
                </div>
                <div class="product-info">
                    <h3 class="product-name">{{ product.name }}</h3>
                    <p class="product-summary">{{ product.summary }}</p>
                    {% if product.price %}
                    <p class="product-price">¥ {{ "%.2f"|format(product.price) }}</p>
                    {% endif %}
                    <a href="/products/detail/{{ product.slug }}" class="btn btn-small">了解更多 →</a>
                </div>
            </div>
            {% endfor %}
        </div>

        <div class="text-center">
            <a href="/products" class="btn btn-outline">查看全部产品</a>
        </div>
    </div>
</section>

<!-- Featured Posts -->
<section class="featured-posts section bg-light">
    <div class="container">
        <h2 class="section-title">最新资讯</h2>
        <p class="section-subtitle">了解行业动态和技术趋势</p>

        <div class="post-grid">
            {% for post in featured_posts %}
            <article class="post-card">
                <div class="post-meta">
                    <time>{{ post.created_at.strftime('%Y-%m-%d') }}</time>
                </div>
                <h3 class="post-title">
                    <a href="/news/detail/{{ post.slug }}">{{ post.title }}</a>
                </h3>
                <p class="post-summary">{{ post.summary }}</p>
                <a href="/news/detail/{{ post.slug }}" class="post-link">阅读更多 →</a>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<!-- Features / Advantages -->
<section class="features section">
    <div class="container">
        <h2 class="section-title">为什么选择我们</h2>

        <div class="feature-grid">
            <div class="feature-item">
                <div class="feature-icon">🎯</div>
                <h3>专业团队</h3>
                <p>拥有多年行业经验的专业团队</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">⚡</div>
                <h3>快速响应</h3>
                <p>7x24小时快速响应客户需求</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🔒</div>
                <h3>品质保证</h3>
                <p>严格的质量控制和售后服务</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">💡</div>
                <h3>创新技术</h3>
                <p>持续技术创新和产品升级</p>
            </div>
        </div>
    </div>
</section>

<!-- CTA Section -->
<section class="cta section">
    <div class="container">
        <div class="cta-content">
            <h2>准备好开始了吗？</h2>
            <p>立即联系我们，获取专业的解决方案</p>
            <a href="/contact" class="btn btn-large btn-primary">立即咨询</a>
        </div>
    </div>
</section>
{% endblock %}
```

### 2.4 product_list.html

```jinja2
{% extends "base.html" %}

{% block title %}{{ column.name }} - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<!-- Page Header -->
<section class="page-header">
    <div class="container">
        <h1>{{ column.name }}</h1>
        {% if column.description %}
        <p>{{ column.description }}</p>
        {% endif %}
    </div>
</section>

<!-- Products -->
<section class="products-section section">
    <div class="container">
        <div class="products-layout">
            <!-- Sidebar - Categories -->
            <aside class="products-sidebar">
                <div class="sidebar-widget">
                    <h3 class="widget-title">产品分类</h3>
                    <ul class="category-list">
                        <li>
                            <a href="/{{ column.slug }}"
                               class="{% if not current_category_id %}active{% endif %}">
                                全部产品 ({{ total }})
                            </a>
                        </li>
                        {% for category in categories %}
                        <li>
                            <a href="/{{ column.slug }}?category={{ category.id }}"
                               class="{% if current_category_id == category.id %}active{% endif %}">
                                {{ category.name }}
                            </a>
                        </li>
                        {% endfor %}
                    </ul>
                </div>
            </aside>

            <!-- Main Content -->
            <div class="products-main">
                {% if products %}
                <div class="product-grid">
                    {% for product in products %}
                    <div class="product-card">
                        <div class="product-image">
                            {% if product.cover_image %}
                            <img src="{{ product.cover_image }}" alt="{{ product.name }}">
                            {% else %}
                            <div class="product-placeholder">
                                <span>{{ product.name[0] }}</span>
                            </div>
                            {% endif %}

                            {% if product.is_recommended %}
                            <span class="badge badge-hot">推荐</span>
                            {% endif %}
                        </div>

                        <div class="product-info">
                            <h3 class="product-name">
                                <a href="/{{ column.slug }}/detail/{{ product.slug }}">
                                    {{ product.name }}
                                </a>
                            </h3>

                            {% if product.model_number %}
                            <p class="product-model">型号：{{ product.model_number }}</p>
                            {% endif %}

                            <p class="product-summary">{{ product.summary }}</p>

                            {% if product.price %}
                            <p class="product-price">¥ {{ "%.2f"|format(product.price) }}</p>
                            {% endif %}

                            <a href="/{{ column.slug }}/detail/{{ product.slug }}"
                               class="btn btn-small btn-block">
                                查看详情
                            </a>
                        </div>
                    </div>
                    {% endfor %}
                </div>
                {% else %}
                <div class="empty-state">
                    <p>暂无产品</p>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</section>
{% endblock %}
```

### 2.5 product_detail.html

```jinja2
{% extends "base.html" %}

{% block title %}{{ product.name }} - {{ site_settings.site_name }}{% endblock %}
{% block meta_description %}{{ product.summary }}{% endblock %}

{% block content %}
<!-- Breadcrumb -->
<nav class="breadcrumb">
    <div class="container">
        <a href="/">首页</a>
        <span>/</span>
        <a href="/{{ column.slug }}">{{ column.name }}</a>
        <span>/</span>
        <span>{{ product.name }}</span>
    </div>
</nav>

<!-- Product Detail -->
<section class="product-detail section">
    <div class="container">
        <div class="product-detail-layout">
            <!-- Product Images -->
            <div class="product-gallery">
                {% if product.cover_image %}
                <div class="main-image">
                    <img src="{{ product.cover_image }}" alt="{{ product.name }}">
                </div>
                {% endif %}

                {% if product.images %}
                <div class="thumbnail-images">
                    {% for image in product.images %}
                    <img src="{{ image.file_path }}" alt="{{ product.name }}">
                    {% endfor %}
                </div>
                {% endif %}
            </div>

            <!-- Product Info -->
            <div class="product-main-info">
                <h1 class="product-title">{{ product.name }}</h1>

                {% if product.model_number %}
                <p class="product-model">型号：{{ product.model_number }}</p>
                {% endif %}

                {% if product.categories %}
                <div class="product-categories">
                    分类：
                    {% for category in product.categories %}
                    <a href="/{{ column.slug }}?category={{ category.id }}">
                        {{ category.name }}
                    </a>
                    {% if not loop.last %}, {% endif %}
                    {% endfor %}
                </div>
                {% endif %}

                {% if product.price %}
                <div class="product-price-box">
                    <span class="price-label">价格：</span>
                    <span class="price-value">¥ {{ "%.2f"|format(product.price) }}</span>
                </div>
                {% endif %}

                <div class="product-summary">
                    <p>{{ product.summary }}</p>
                </div>

                <!-- Action Buttons -->
                <div class="product-actions">
                    <a href="/contact" class="btn btn-primary btn-large">立即咨询</a>
                    <a href="tel:{{ site_settings.phone }}" class="btn btn-secondary btn-large">
                        电话咨询
                    </a>
                </div>

                <!-- Share Buttons (optional) -->
                <div class="product-share">
                    <span>分享：</span>
                    <a href="#">微信</a>
                    <a href="#">微博</a>
                </div>
            </div>
        </div>

        <!-- Product Description -->
        <div class="product-description">
            <div class="tabs">
                <button class="tab-button active" data-tab="description">产品详情</button>
                <button class="tab-button" data-tab="specs">技术参数</button>
            </div>

            <div class="tab-content active" id="description">
                <div class="content-html">
                    {{ product.description_html | safe }}
                </div>
            </div>

            <div class="tab-content" id="specs">
                <table class="specs-table">
                    {% for field in product.custom_fields %}
                    <tr>
                        <td class="spec-label">{{ field.field_name }}</td>
                        <td class="spec-value">{{ field.display_value }}</td>
                    </tr>
                    {% endfor %}
                </table>
            </div>
        </div>

        <!-- Related Products -->
        {% if related_products %}
        <div class="related-products">
            <h2>相关产品</h2>
            <div class="product-grid">
                {% for related in related_products %}
                <div class="product-card">
                    <!-- Same as product list card -->
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
    </div>
</section>
{% endblock %}
```

### 2.6 post_list.html & post_detail.html

结构类似 product 模板，调整为文章相关的字段和样式。

### 2.7 single_page.html

```jinja2
{% extends "base.html" %}

{% block title %}{{ page.title }} - {{ site_settings.site_name }}{% endblock %}

{% block content %}
<section class="single-page section">
    <div class="container">
        <article class="page-content">
            <h1 class="page-title">{{ page.title }}</h1>
            <div class="page-html">
                {{ page.content_html | safe }}
            </div>
        </article>
    </div>
</section>
{% endblock %}
```

### 2.8 contact.html (自定义)

可以在 `templates/` 下创建 `contact.html`，实现带表单的联系页面。

---

## 第三阶段：样式优化（Style Enhancement）

### 3.1 CSS 架构

更新 `templates/static/css/main.css`：

```css
/* =================================
   1. CSS Variables (Design Tokens)
   ================================= */
:root {
    /* Colors */
    --color-primary: #3b82f6;
    --color-primary-dark: #2563eb;
    --color-secondary: #10b981;
    --color-accent: #f59e0b;

    --color-text: #1f2937;
    --color-text-light: #6b7280;
    --color-bg: #ffffff;
    --color-bg-light: #f3f4f6;
    --color-border: #e5e7eb;

    /* Spacing */
    --spacing-xs: 0.5rem;
    --spacing-sm: 1rem;
    --spacing-md: 1.5rem;
    --spacing-lg: 2rem;
    --spacing-xl: 3rem;

    /* Typography */
    --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-size-base: 16px;
    --line-height-base: 1.6;

    /* Radius */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;

    /* Shadow */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

/* =================================
   2. Reset & Base
   ================================= */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-sans);
    font-size: var(--font-size-base);
    line-height: var(--line-height-base);
    color: var(--color-text);
    background: var(--color-bg);
}

/* Container */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--spacing-md);
}

/* =================================
   3. Typography
   ================================= */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.3;
    margin-bottom: var(--spacing-sm);
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }

/* =================================
   4. Buttons
   ================================= */
.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: var(--radius-md);
    font-size: 1rem;
    font-weight: 500;
    text-decoration: none;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-primary {
    background: var(--color-primary);
    color: white;
}

.btn-primary:hover {
    background: var(--color-primary-dark);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

/* =================================
   5. Navigation
   ================================= */
.navbar {
    background: white;
    box-shadow: var(--shadow-sm);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: var(--spacing-sm);
    padding-bottom: var(--spacing-sm);
}

.navbar-menu {
    display: flex;
    list-style: none;
    gap: var(--spacing-lg);
}

.navbar-link {
    color: var(--color-text);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
}

.navbar-link:hover,
.navbar-link.active {
    color: var(--color-primary);
}

/* Mobile Menu */
.navbar-burger {
    display: none;
    /* Mobile styles... */
}

@media (max-width: 768px) {
    .navbar-burger {
        display: block;
    }

    .navbar-menu {
        /* Mobile menu styles... */
    }
}

/* =================================
   6. Hero Section
   ================================= */
.hero {
    background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
    color: white;
    padding: var(--spacing-xl) 0;
    text-align: center;
}

.hero-title {
    font-size: 3rem;
    margin-bottom: var(--spacing-md);
}

.hero-subtitle {
    font-size: 1.25rem;
    margin-bottom: var(--spacing-lg);
    opacity: 0.9;
}

/* =================================
   7. Product Grid
   ================================= */
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: var(--spacing-lg);
}

.product-card {
    background: white;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-lg);
    overflow: hidden;
    transition: all 0.3s;
}

.product-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

/* =================================
   8. Footer
   ================================= */
.footer {
    background: var(--color-text);
    color: white;
    padding: var(--spacing-xl) 0 var(--spacing-lg);
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-lg);
    margin-bottom: var(--spacing-lg);
}

/* =================================
   9. Responsive
   ================================= */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2rem;
    }

    .product-grid {
        grid-template-columns: 1fr;
    }
}
```

### 3.2 可选：使用 Tailwind CSS

如果想使用 Tailwind CSS：

1. 安装 Tailwind
2. 配置 `tailwind.config.js`
3. 在模板中使用 Tailwind 类名

---

## 第四阶段：功能实现（Feature Implementation）

### 4.1 联系表单

确保 `contact.html` 有表单提交功能：

```html
<form action="/contact/submit" method="POST" id="contactForm">
    <div class="form-group">
        <label for="name">姓名 *</label>
        <input type="text" id="name" name="name" required>
    </div>

    <div class="form-group">
        <label for="email">邮箱 *</label>
        <input type="email" id="email" name="email" required>
    </div>

    <div class="form-group">
        <label for="phone">电话</label>
        <input type="tel" id="phone" name="phone">
    </div>

    <div class="form-group">
        <label for="subject">主题 *</label>
        <input type="text" id="subject" name="subject" required>
    </div>

    <div class="form-group">
        <label for="message">留言 *</label>
        <textarea id="message" name="message" rows="5" required></textarea>
    </div>

    <button type="submit" class="btn btn-primary">提交</button>
</form>

<script>
document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const response = await fetch('/contact/submit', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();

    if (result.success) {
        alert('提交成功！我们会尽快回复您。');
        this.reset();
    } else {
        alert('提交失败：' + result.message);
    }
});
</script>
```

### 4.2 搜索功能（可选）

在导航栏添加搜索框。

### 4.3 图片占位符

如果产品没有图片，显示占位符：

```html
<div class="product-placeholder" style="background: #f3f4f6; width: 100%; height: 200px; display: flex; align-items: center; justify-content: center;">
    <span style="font-size: 3rem; color: #9ca3af;">{{ product.name[0] }}</span>
</div>
```

---

## 第五阶段：测试与优化（Testing & Optimization)

### 5.1 功能测试清单

- [ ] 首页加载正常
- [ ] 导航菜单正常工作
- [ ] 产品列表显示所有产品
- [ ] 产品分类筛选正常
- [ ] 产品详情页显示完整信息
- [ ] 文章列表和详情正常
- [ ] 联系表单提交成功
- [ ] 404 页面正常显示
- [ ] 移动端响应式正常

### 5.2 性能优化

- 图片使用合理尺寸
- CSS 压缩
- 减少不必要的 HTTP 请求

### 5.3 SEO 优化

- 确保每个页面有合适的 title 和 meta description
- 使用语义化 HTML 标签
- 添加 alt 属性到图片

---

## 工作流程总结

### 推荐工作顺序

1. **数据生成** (30 分钟)
   - 创建 `seed_data.sql`
   - 运行数据库迁移和填充
   - 验证数据正确性

2. **模板开发** (1-2 小时)
   - 完善 `base.html`
   - 完善 `home.html`
   - 创建 `product_list.html` 和 `product_detail.html`
   - 创建 `post_list.html` 和 `post_detail.html`
   - 创建 `single_page.html`

3. **样式优化** (1 小时)
   - 更新 `main.css`
   - 实现响应式设计
   - 调整颜色和间距

4. **功能实现** (30 分钟)
   - 完善联系表单
   - 添加交互功能

5. **测试** (30 分钟)
   - 功能测试
   - 浏览器兼容性测试
   - 移动端测试

**总计时间**: 约 3-4 小时完成一个完整的企业官网

---

## 附录：常见问题

### Q1: 如何添加新的栏目？

在 `seed_data.sql` 中添加新的 `site_column` 记录。

### Q2: 如何修改网站主色调？

修改 `main.css` 中的 `--color-primary` 变量。

### Q3: 如何添加自定义字段？

参考数据库设计文档，使用 `custom_field_def` 和 `product_custom_field_value` 表。

### Q4: 如何处理图片？

- 上传图片到 `instance/media/uploads/`
- 在数据库中存储相对路径（如：`/static/media/uploads/image.jpg`）

---

## 结语

本指南提供了完整的站点完善流程。按照这个指南，Claude Code 可以系统化地将一个基础站点框架转变为功能完整的企业官网。

关键要点：
1. **数据真实性** - 不使用占位文本
2. **模板完整性** - 覆盖所有页面类型
3. **样式一致性** - 使用设计系统
4. **功能可用性** - 所有功能都能正常工作
5. **响应式设计** - 移动端友好

**预计完成时间**: 3-4 小时/站点
**质量标准**: 专业、完整、可直接上线
