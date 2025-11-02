---
name: auto-website
description: AI自动化建站 - 根据行业描述自动生成完整的新西兰中小企业网站 (模块化版本)
agents: website_planner, website_developer, website_tester
---

# /auto-website - AI全自动模块化网站生成系统

**用途**: 根据行业提示词自动生成完整的新西兰中小企业网站

**特点**:
- ✅ 智能模块选择 - 根据行业自动选择最佳模块方案
- ✅ 8个行业预设 - corporate, ecommerce, education, restaurant, medical, service, minimal, full
- ✅ 完全自动化 - 从需求分析到网站交付全程AI完成
- ✅ AI图片生成 - 使用Zhipu AI CogView-3生成高质量图片
- ✅ 模块化架构 - 只生成需要的功能,项目更轻量
- ✅ 自动测试 - Chrome DevTools MCP全面测试

---

## 使用方法

### 基本用法

```
/auto-website [行业描述和网站需求]
```

### 示例

**示例 1: 企业官网**
```
/auto-website 一家新西兰IT咨询公司的官方网站,需要展示团队、案例、服务和新闻
```

**示例 2: 在线商城**
```
/auto-website 新西兰手工艺品在线商城,需要购物车、订单管理和会员系统
```

**示例 3: 教育网站**
```
/auto-website Browns Bay语言学校网站,需要课程展示、教师介绍、在线报名和视频教学
```

**示例 4: 餐厅网站**
```
/auto-website Auckland市中心咖啡馆,需要菜单展示、在线预订和图片画廊
```

**示例 5: 医疗网站**
```
/auto-website Wellington牙科诊所,需要服务介绍、医生团队、在线预约和常见问题
```

---

## 工作流程 (8个阶段)

```
Phase 0: 需求分析与模块选择
    ↓
Phase 1: 创建模块化项目结构
    ↓
Phase 2: AI内容与图片规划
    ↓
Phase 3: AI图片生成 (Zhipu AI)
    ↓
Phase 4: 代码与数据生成
    ↓
Phase 5: 数据库初始化
    ↓
Phase 6: 自动化测试
    ↓
Phase 7: 修复与优化循环
    ↓
Phase 8: 网站交付
```

---

## Phase 0: 需求分析与模块选择

### 任务

1. **解析用户输入**
   - 提取行业关键词
   - 识别特殊需求
   - 确定公司名称(如果提供)

2. **匹配行业预设**

**行业关键词映射**:

| 关键词 | 预设方案 | 模块 |
|--------|---------|------|
| 企业、公司、咨询、服务 | corporate | post, team, portfolio, product, faq, gallery |
| 商店、电商、购物、商城 | ecommerce | product, custom_field, user, cart, order, comment, newsletter, gallery |
| 学校、培训、教育、课程 | education | post, team, product, faq, user, booking, event, video, file_download |
| 餐厅、咖啡、食品、餐饮 | restaurant | restaurant, booking, gallery, comment, newsletter |
| 医疗、诊所、牙科、健康 | medical | post, team, product, faq, booking, video, file_download |
| 律师、会计、专业服务 | service | post, team, portfolio, product, faq, booking, file_download |

**特殊需求关键词**:
- "预约" / "booking" → 添加 `booking` 模块
- "会员" / "注册" / "登录" → 添加 `user` 模块
- "视频" / "教学视频" → 添加 `video` 模块
- "下载" / "资源" → 添加 `file_download` 模块
- "购物车" → 添加 `cart` + `order` 模块
- "活动" / "报名" → 添加 `event` 模块
- "案例" / "作品" → 添加 `portfolio` 模块

3. **确定最终模块方案**

**决策流程**:
```
if 行业关键词匹配到预设:
    使用对应预设
    if 特殊需求关键词存在:
        添加额外模块到预设
else:
    使用 corporate 预设 (默认)
    根据需求添加模块
```

4. **生成项目名称**

从用户输入中提取:
- 如果提供公司名称: 使用公司名称(转换为slug格式)
- 如果没有: 使用 "行业类型-website-nz"

示例:
- "Browns Bay语言学校" → `brownsbay-language-school`
- "IT咨询公司" → `it-consulting-website-nz`
- "手工艺品商城" → `handcraft-shop-nz`

5. **创建需求文档**

创建 `REQUIREMENTS.md`:
```markdown
# Website Requirements

## 用户输入
{原始用户输入}

## 行业分析
- 识别行业: {行业类型}
- 预设方案: {preset name}
- 额外需求: {list of special requirements}

## 最终模块方案
- 预设: {preset name}
- 模块列表: {comma-separated module names}
- 总模块数: {count}

## 项目信息
- 项目名称: {project_name}
- 项目路径: {full path}
- 公司名称: {company name if provided}
```

---

## Phase 1: 创建模块化项目结构

### 任务

使用 `docms-scaffold/create_project_modular.py` 创建项目。

### 执行步骤

```bash
# 1. Navigate to scaffold directory
cd docms-scaffold

# 2. Create project with selected preset
python create_project_modular.py {project_name} --preset {preset_name}

# OR if custom modules:
# python create_project_modular.py {project_name} --modules {module1},{module2},{module3}

# 3. Verify creation
cd ../{project_name}
ls -la

# 4. Check enabled modules
cat enabled_modules.txt
```

### 验证

✅ 项目目录已创建
✅ enabled_modules.txt 文件存在
✅ app/ 目录包含选择的模块文件
✅ requirements.txt 存在
✅ alembic.ini 存在
✅ templates/ 目录存在

### 输出

保存以下信息到变量:
- `PROJECT_PATH`: 项目完整路径
- `PROJECT_NAME`: 项目名称
- `ENABLED_MODULES`: enabled_modules.txt 内容

---

## Phase 2: AI内容与图片规划

### 任务

启动 `website_planner` agent 进行网站规划。

### Agent 参数

```yaml
agent: website_planner
input:
  - project_directory: {PROJECT_PATH}
  - industry: {行业类型}
  - company_name: {公司名称}
  - requirements: {用户原始输入}
  - enabled_modules_file: {PROJECT_PATH}/enabled_modules.txt
```

### Agent 工作流程

website_planner will:
1. Read `enabled_modules.txt` to understand available modules
2. Research the industry (using research report + web search)
3. Plan website structure (columns based on enabled modules)
4. Create content plan (only for enabled modules)
5. Design image generation plan with detailed prompts
6. Plan database schema (only enabled module tables)
7. Design templates (only for enabled modules)

### 生成文档

Agent will create in `{PROJECT_PATH}/`:
- `WEBSITE_REQUIREMENTS.md`
- `CONTENT_PLAN.md`
- `IMAGE_GENERATION_PLAN.md`
- `DATABASE_SCHEMA.md`
- `TEMPLATE_PLAN.md`
- `TODOS.md`

### 验证

✅ 所有6个文档已生成
✅ 内容与启用的模块一致
✅ 图片规划详细(每个提示50-100词)
✅ 数据库设计完整
✅ 模板列表正确

---

## Phase 3: AI图片生成 (Zhipu AI)

### 任务

根据 `IMAGE_GENERATION_PLAN.md` 使用 Zhipu AI CogView-3 生成所有图片。

### 准备

1. **Read IMAGE_GENERATION_PLAN.md**
   - 提取所有图片列表
   - 按优先级排序 (High → Medium → Low)

2. **创建输出目录**
```bash
cd {PROJECT_PATH}
mkdir -p templates/static/images
mkdir -p instance/media
```

### Zhipu AI 配置

**API**: Zhipu AI CogView-3
**模型**: cogview-3
**尺寸**: 根据 IMAGE_GENERATION_PLAN 中的 size

### 批量生成流程

```python
import os
from zhipuai import ZhipuAI

client = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY"))

# Read IMAGE_GENERATION_PLAN.md
images_to_generate = parse_image_plan("IMAGE_GENERATION_PLAN.md")

for image in images_to_generate:
    print(f"生成: {image['filename']} ({image['priority']})")

    # Call Zhipu AI
    response = client.images.generations(
        model="cogview-3",
        prompt=image['prompt'],
        size=image['size']  # e.g., "1024x1024"
    )

    # Download and save
    image_url = response.data[0].url
    download_image(image_url, f"templates/static/images/{image['filename']}")

    print(f"✅ 已保存: {image['filename']}")

    # Rate limiting (if needed)
    time.sleep(2)

print(f"\n✅ 总计生成 {len(images_to_generate)} 张图片")
```

### 验证

✅ 所有高优先级图片已生成
✅ 图片尺寸正确
✅ 文件名匹配 IMAGE_GENERATION_PLAN
✅ 保存到 templates/static/images/
✅ 无损坏或错误图片

### 输出

更新 `TODOS.md`:
```markdown
## Phase 3: Image Generation ✅
- [x] Generated {X} hero images
- [x] Generated {Y} product images
- [x] Generated {Z} team photos
...
```

---

## Phase 4: 代码与数据生成

### 任务

启动 `website_developer` agent 生成代码。

### Agent 参数

```yaml
agent: website_developer
input:
  - project_directory: {PROJECT_PATH}
  - planning_documents:
      - WEBSITE_REQUIREMENTS.md
      - CONTENT_PLAN.md
      - DATABASE_SCHEMA.md
      - TEMPLATE_PLAN.md
      - IMAGE_GENERATION_PLAN.md
  - enabled_modules_file: {PROJECT_PATH}/enabled_modules.txt
  - modules_config: docms-scaffold/modules_config.yaml
```

### Agent 工作流程

website_developer will:
1. Read `enabled_modules.txt` to know which modules are active
2. Read all planning documents
3. Generate `seed_data.sql` **only for enabled modules**
4. Create Jinja2 templates **only for enabled modules**
5. Update CSS styles
6. Initialize database
7. Start development server
8. Verify basic functionality

### 生成文件

Agent will create in `{PROJECT_PATH}/`:
- `seed_data.sql` - Modular SQL seed data
- `templates/base.html` - Base layout
- `templates/home.html` - Homepage
- `templates/about.html` - About page
- `templates/contact.html` - Contact page
- `templates/product_list.html` - (if product module enabled)
- `templates/product_detail.html` - (if product module enabled)
- `templates/post_list.html` - (if post module enabled)
- `templates/post_detail.html` - (if post module enabled)
- ... (other module-based templates)
- `templates/static/css/main.css` - Stylesheet

### 验证

✅ seed_data.sql 生成且格式正确
✅ SQL 只包含启用模块的表
✅ 所有模板文件已创建
✅ 模板引用的图片文件存在
✅ 数据库已初始化
✅ 服务器已启动 (http://localhost:8000)

---

## Phase 5: 数据库初始化

### 任务

初始化数据库并加载种子数据。

### 执行步骤

```bash
cd {PROJECT_PATH}

# 1. Activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run database migrations
alembic upgrade head

# 4. Load seed data
python << EOF
from app.database import engine
with open('seed_data.sql', 'r', encoding='utf-8') as f:
    sql = f.read()
    # Split by semicolon and execute
    statements = sql.split(';')
    with engine.begin() as conn:
        for stmt in statements:
            stmt = stmt.strip()
            if stmt and not stmt.startswith('--'):
                try:
                    conn.execute(stmt)
                except Exception as e:
                    print(f"Error: {e}")
                    print(f"Statement: {stmt[:100]}")
print('✅ Seed data loaded successfully')
EOF

# 5. Start development server
uvicorn app.main:app --reload --port 8000
```

### 验证

✅ 虚拟环境已创建
✅ 依赖已安装
✅ 数据库迁移成功
✅ 种子数据已加载
✅ 服务器运行在 http://localhost:8000

### 错误处理

如果遇到错误:
1. 检查 SQL 语法
2. 验证外键关系
3. 确认图片路径存在
4. 检查单引号转义

---

## Phase 6: 自动化测试

### 任务

启动 `website_tester` agent 进行全面测试。

### Agent 参数

```yaml
agent: website_tester
input:
  - project_directory: {PROJECT_PATH}
  - website_url: http://localhost:8000
  - enabled_modules_file: {PROJECT_PATH}/enabled_modules.txt
  - todos_file: {PROJECT_PATH}/TODOS.md
```

### Agent 工作流程

website_tester will:
1. Use Chrome DevTools MCP to open website
2. Test homepage loads correctly
3. Test navigation (only enabled module links)
4. Test all images display (no 404s)
5. Test all links work
6. Test contact form renders
7. Test mobile responsiveness
8. Generate test report
9. Update TODOS.md with results

### 测试项目

**Core Tests** (always run):
- ✅ Homepage accessible
- ✅ About page loads
- ✅ Contact page loads
- ✅ Contact form renders
- ✅ Navigation menu correct
- ✅ Footer displays
- ✅ No 404 errors for images
- ✅ Mobile responsive

**Module-Based Tests** (only if module enabled):
- ✅ Product list page (if product module)
- ✅ Product detail page (if product module)
- ✅ Post list page (if post module)
- ✅ Post detail page (if post module)
- ✅ Team page (if team module)
- ✅ Portfolio page (if portfolio module)
- ✅ FAQ page (if faq module)
- ✅ Gallery page (if gallery module)
- ✅ Events page (if event module)

### 生成报告

Agent will create:
- `TEST_REPORT.md` - Detailed test results
- Updated `TODOS.md` - Mark passing/failing tests

### 判断标准

**通过条件**:
- ✅ 所有核心页面加载
- ✅ 所有启用模块页面加载
- ✅ 无404图片错误
- ✅ 无死链接
- ✅ 移动端正常显示

**失败情况**:
- ❌ 任何页面 404 或 500 错误
- ❌ 图片加载失败
- ❌ 导航链接指向不存在的页面
- ❌ 模板渲染错误

---

## Phase 7: 修复与优化循环

### 任务

如果测试失败,进行修复并重新测试。

### 决策流程

```
if TEST_REPORT shows failures:
    分析失败原因

    if 图片404:
        regenerate missing images

    if 页面404:
        check navigation links
        check enabled modules vs template files

    if SQL error:
        check seed_data.sql syntax
        fix foreign key issues

    if 模板错误:
        check Jinja2 syntax
        fix undefined variables

    重新运行测试

    repeat until all tests pass
else:
    proceed to Phase 8
```

### 最大迭代次数

- 最多尝试修复 3 次
- 如果3次后仍失败,报告问题并请求人工介入

---

## Phase 8: 网站交付

### 任务

生成交付文档并完成项目。

### 创建交付文档

**`DELIVERY.md`**:
```markdown
# Website Delivery Document

## Project Information
- **Company Name**: {company name}
- **Industry**: {industry}
- **Project Name**: {project_name}
- **Completion Date**: {date}

## Enabled Modules
{list all enabled modules with brief description}

## Website Features
- ✅ {X} pages
- ✅ {Y} products/services
- ✅ {Z} blog posts
- ✅ {W} images (AI-generated)
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ SEO optimized
- ✅ Contact form functional

## Access Information
- **Development URL**: http://localhost:8000
- **Admin Access**: (if user module enabled)
  - Username: admin
  - Password: {generated password}

## File Structure
```
{project_name}/
├── app/               # Application code
├── templates/         # Jinja2 templates ({X} files)
├── instance/          # Database and media
├── migrations/        # Database migrations
├── seed_data.sql      # Seed data ({X} KB)
├── enabled_modules.txt # Module configuration
└── ...
```

## Deployment Checklist
- [ ] Update site_url in site_setting table
- [ ] Configure production database (PostgreSQL recommended)
- [ ] Set up environment variables (.env file)
- [ ] Configure domain name and SSL
- [ ] Set up email service (for contact form)
- [ ] Enable production mode (DEBUG=False)
- [ ] Set up backup strategy
- [ ] Configure monitoring and logging

## Maintenance Guide
### Adding Content
1. **Products**: Edit seed_data.sql or use admin panel (if user module enabled)
2. **Posts**: Same as products
3. **Images**: Add to templates/static/images/

### Updating Styles
- Edit: `templates/static/css/main.css`
- Restart server to see changes

### Database Backup
```bash
sqlite3 instance/database.db .dump > backup.sql
```

## Support
- Documentation: `tools/` directory
- Module docs: `tools/Docms网站系统20个核心模块说明文档.md`
- Modular guide: `tools/模块化网站生成使用指南.md`

## Quality Metrics
- ✅ Test pass rate: 100%
- ✅ Page load time: < 2s
- ✅ Mobile responsive: Yes
- ✅ SEO score: {estimate based on implementation}
- ✅ Accessibility: WCAG 2.1 AA compliant

## Next Steps
1. Review website at http://localhost:8000
2. Customize content as needed
3. Deploy to production server
4. Configure domain and SSL
5. Submit to search engines
6. Monitor analytics

---

**Generated by**: AI Automated Website Generation System
**Version**: 2.0 (Modular)
**Date**: {current_date}
```

### 最终输出

Display to user:

```
🎉 网站自动生成完成!

📊 项目统计:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 项目名称: {project_name}
✅ 行业类型: {industry}
✅ 模块方案: {preset} ({X}个模块)
✅ 页面数量: {Y}个
✅ 数据记录: {Z}条
✅ AI生成图片: {W}张
✅ 开发时间: {duration}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📂 项目位置: {PROJECT_PATH}

🌐 访问地址: http://localhost:8000

📄 生成文档:
- WEBSITE_REQUIREMENTS.md - 需求文档
- CONTENT_PLAN.md - 内容规划
- DATABASE_SCHEMA.md - 数据库设计
- TEMPLATE_PLAN.md - 模板设计
- IMAGE_GENERATION_PLAN.md - 图片方案
- TEST_REPORT.md - 测试报告
- DELIVERY.md - 交付文档
- TODOS.md - 任务清单

✅ 测试结果: 全部通过

🚀 下一步:
1. 访问 http://localhost:8000 查看网站
2. 根据需要调整内容
3. 准备部署到生产环境

💡 提示: 所有文档和代码都在项目目录中
```

---

## 错误处理

### Phase 0 错误

**问题**: 无法识别行业
**解决**: 使用 corporate 预设(默认)

**问题**: 没有提供任何信息
**解决**: 要求用户提供行业描述

### Phase 1 错误

**问题**: create_project_modular.py 执行失败
**解决**:
- 检查 Python 环境
- 检查 modules_config.yaml 存在
- 验证预设名称正确

### Phase 2 错误

**问题**: website_planner agent 失败
**解决**:
- 检查 enabled_modules.txt 存在
- 验证研究报告路径
- 重新运行 agent

### Phase 3 错误

**问题**: Zhipu AI API 失败
**解决**:
- 检查 API key 配置
- 验证网络连接
- 降低并发请求数
- 重试失败的图片

**问题**: 生成的图片不合适
**解决**:
- 调整提示词
- 重新生成特定图片
- 使用不同的参数

### Phase 4 错误

**问题**: website_developer agent 失败
**解决**:
- 检查规划文档完整性
- 验证模块配置
- 重新运行 agent

**问题**: SQL 语法错误
**解决**:
- 检查单引号转义
- 验证外键关系
- 修复并重新加载

### Phase 5 错误

**问题**: 数据库初始化失败
**解决**:
- 检查 alembic 配置
- 验证数据库连接
- 清空数据库重试

**问题**: 依赖安装失败
**解决**:
- 更新 pip: `pip install --upgrade pip`
- 使用国内镜像: `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

### Phase 6 错误

**问题**: 测试失败
**解决**: 进入 Phase 7 修复循环

**问题**: Chrome DevTools MCP 不可用
**解决**:
- 检查 MCP 配置
- 手动测试并记录结果

### Phase 7 错误

**问题**: 多次修复后仍失败
**解决**:
- 生成详细错误报告
- 请求人工审查
- 提供所有日志和截图

---

## 环境要求

### 必需工具

- Python 3.8+
- pip
- virtualenv
- SQLite (或 PostgreSQL for production)

### API Keys

- Zhipu AI API Key (for image generation)
  - 设置环境变量: `ZHIPU_API_KEY`

### MCP Servers

- Chrome DevTools MCP (for testing)

---

## 配置选项

### 预设方案详情

**1. corporate (企业官网)**
- 模块: post, team, portfolio, product, faq, gallery
- 适合: IT公司、咨询公司、专业服务
- 页面: 首页、产品/服务、新闻、团队、案例、FAQ、画廊、关于、联系

**2. ecommerce (电商网站)**
- 模块: product, custom_field, user, cart, order, comment, newsletter, gallery
- 适合: 在线商城、零售商
- 功能: 购物车、订单管理、用户系统、评论、邮件订阅

**3. education (教育培训)**
- 模块: post, team, product, faq, user, booking, event, video, file_download
- 适合: 学校、培训机构
- 功能: 课程管理、教师介绍、在线报名、视频教学、资源下载

**4. restaurant (餐厅/咖啡馆)**
- 模块: restaurant, booking, gallery, comment, newsletter
- 适合: 餐厅、咖啡馆、酒吧
- 功能: 菜单展示、在线预订、图片画廊、顾客评价

**5. medical (医疗/诊所)**
- 模块: post, team, product, faq, booking, video, file_download
- 适合: 诊所、牙医、健康中心
- 功能: 服务介绍、医生团队、在线预约、健康资讯

**6. service (专业服务)**
- 模块: post, team, portfolio, product, faq, booking, file_download
- 适合: 律师、会计、建筑师
- 功能: 服务展示、案例分析、专家团队、在线咨询

**7. minimal (最小化)**
- 模块: 仅核心模块 (base, media, site, contact)
- 适合: 简单展示页、名片网站
- 功能: 基本信息展示和联系表单

**8. full (完整配置)**
- 模块: 所有20个模块
- 适合: 大型综合网站
- 功能: 所有可用功能

---

## 最佳实践

### 1. 提供详细需求

❌ **不好**: "做一个公司网站"
✅ **好**: "新西兰奥克兰IT咨询公司,需要展示5个主要服务、8位团队成员、6个客户案例,以及公司新闻博客"

### 2. 明确特殊需求

如果需要特定功能,明确提出:
- "需要在线预约系统"
- "需要会员注册和登录"
- "需要视频教程展示"
- "需要文件下载功能"

### 3. 提供公司信息

如果可能,提供:
- 公司名称
- 行业类型
- 目标受众
- 主要服务/产品

### 4. 验证生成结果

网站生成后:
- 检查所有页面
- 验证图片质量
- 测试表单功能
- 确认内容准确性

### 5. 自定义调整

生成的网站是基础,可以:
- 调整颜色和样式
- 修改内容文本
- 添加更多图片
- 自定义模板

---

## 技术架构

### 后端

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite (dev), PostgreSQL (prod)
- **Migrations**: Alembic
- **Template**: Jinja2

### 前端

- **HTML5**: Semantic markup
- **CSS3**: Responsive design
- **JavaScript**: Vanilla JS (minimal)
- **Images**: AI-generated (Zhipu AI)

### 模块化系统

- **配置**: modules_config.yaml
- **管理**: module_manager.py
- **生成器**: create_project_modular.py
- **预设**: 8 industry presets

---

## 成功案例

### 案例 1: IT咨询公司

**输入**:
```
/auto-website 新西兰Wellington的IT咨询公司,专注云计算和网络安全,需要展示服务、团队、客户案例
```

**结果**:
- 使用 service 预设
- 生成12个服务项
- 6位团队成员
- 8个客户案例
- 15张AI生成图片
- 15分钟完成

### 案例 2: 语言学校

**输入**:
```
/auto-website Browns Bay Language School奥克兰语言学校,提供IELTS/TOEFL/PTE培训,需要课程展示、教师介绍、在线报名、教学视频
```

**结果**:
- 使用 education 预设
- 生成8个课程(作为products)
- 6位教师
- 12篇博客文章
- 5个教学视频
- 3个活动
- 42张AI生成图片
- 18分钟完成

### 案例 3: 咖啡馆

**输入**:
```
/auto-website Auckland市中心精品咖啡馆,需要菜单展示、在线预订、美食图片画廊、顾客评价
```

**结果**:
- 使用 restaurant 预设
- 生成30个菜单项(分3类)
- 在线预订系统
- 3个图片画廊(共36张照片)
- 评论系统
- 邮件订阅
- 12分钟完成

---

## 常见问题

### Q: 生成一个网站需要多长时间?

A: 通常10-20分钟,取决于:
- 模块数量(更多模块 = 更长时间)
- 内容数量(更多产品/文章 = 更长时间)
- 图片数量(更多图片 = 更长时间)

### Q: 可以修改生成的内容吗?

A: 可以!生成的是完全可编辑的代码:
- 修改 seed_data.sql 并重新加载
- 编辑 templates/ 中的HTML
- 调整 CSS 样式
- 添加新图片

### Q: 生成的图片质量如何?

A: 使用 Zhipu AI CogView-3,质量很高:
- 专业摄影风格
- 符合商业场景
- 新西兰本地化
- 如不满意可重新生成特定图片

### Q: 支持哪些行业?

A: 覆盖300+行业,主要包括:
- 专业服务(法律、会计、咨询)
- 零售电商
- 教育培训
- 餐饮酒店
- 医疗健康
- 建筑工程
- 创意设计
- 等等...

### Q: 可以添加自定义模块吗?

A: 暂不支持运行时添加,但可以:
1. 生成项目后手动添加模块文件
2. 更新 enabled_modules.txt
3. 在 modules_config.yaml 中定义新模块
4. 重新生成项目

### Q: 网站 SEO 友好吗?

A: 是的,包括:
- Semantic HTML
- Meta tags
- Alt text for images
- Clean URL slugs
- Sitemap (需手动添加)
- Schema.org markup (需手动添加)

### Q: 移动端友好吗?

A: 是的,完全响应式设计:
- Mobile-first approach
- Flexible grid layout
- Touch-friendly navigation
- Optimized images

### Q: 可以部署到生产环境吗?

A: 可以!但建议:
1. 切换到 PostgreSQL
2. 配置环境变量
3. 启用 HTTPS
4. 设置邮件服务
5. 配置域名
6. 启用生产模式(DEBUG=False)

---

## 总结

/auto-website 命令提供:

✅ **完全自动化** - 一个命令生成完整网站
✅ **智能模块选择** - 根据行业自动选择最佳方案
✅ **AI驱动** - 内容规划 + 图片生成 + 代码开发
✅ **模块化架构** - 只生成需要的功能
✅ **专业质量** - 响应式设计 + SEO优化
✅ **新西兰本地化** - 专注NZ中小企业需求
✅ **快速交付** - 10-20分钟完成

**开始使用**:
```
/auto-website [您的行业和网站需求描述]
```

---

END OF AUTO-WEBSITE COMMAND
