# AI自动化建站系统使用指南

这是一个基于Claude Code的AI自动化建站系统,专为新西兰中小企业网站设计。系统可以根据行业提示词自动生成完整的专业网站。

## 🎯 系统特点

- **全自动流程**: 从需求分析到网站部署,全程自动化
- **AI驱动内容**: 使用LLM生成专业内容
- **AI生成图片**: 集成智谱AI文生图,自动生成所有网站图片
- **新西兰本地化**: 基于300+新西兰行业研究,符合本地特色
- **质量保证**: 自动测试所有功能,确保无失效链接和图片
- **快速高效**: 15-30分钟完成整个网站开发

## 📋 系统组成

### 核心命令
- `/auto-website [行业描述]` - 启动自动化建站工作流

### 专门Agents
- **website_planner** - 规划网站结构、内容和图片
- **website_developer** - 开发数据库和模板
- **website_tester** - 测试网站功能

### 协调机制
- **website_dm.py** - Hook协调器,自动编排整个流程

### 资源文件
- **新西兰中小企业网站模板研究报告.md** - 300+行业参考
- **docms-scaffold/** - Python Flask CMS框架

## 🚀 快速开始

### 前置要求

1. **Claude Code CLI** 安装和配置
2. **Python 3.8+** 环境
3. **智谱AI API密钥** (用于图片生成)
4. **Chrome DevTools MCP** (用于网站测试,可选)

### 步骤1: 配置API密钥

```bash
# 复制示例配置文件
cd D:/projects/docmsnz
cp .claude/config/zhipu_api_key.txt.example .claude/config/zhipu_api_key.txt

# 编辑文件,填入你的智谱AI API密钥
# 获取API密钥: https://open.bigmodel.cn/
notepad .claude/config/zhipu_api_key.txt
```

### 步骤2: 启动自动化建站

在Claude Code中运行:

```bash
claude -p "我想为一家新西兰的温室园艺设备供应公司建立网站,公司名叫GreenHouse NZ,主营智能温室设备和配件"
```

或使用slash命令:

```
/auto-website 我想为一家新西兰的咖啡馆建立网站,公司名叫Auckland Central Cafe,提供精品咖啡和新西兰特色早午餐
```

### 步骤3: 等待自动化完成

系统将自动执行以下步骤:

1. **阶段0: 需求理解** (1分钟)
   - 解析行业类型和公司信息
   - 确定网站目录名

2. **阶段1: 创建目录** (1分钟)
   - 使用docms-scaffold创建网站结构

3. **阶段2: 网站规划** (3-5分钟)
   - 分析行业研究报告
   - 搜索新西兰参考网站
   - 规划栏目和内容
   - 设计图片生成方案
   - 创建6个规划文档

4. **阶段3: 图片生成** (5-10分钟)
   - 调用智谱AI API
   - 生成15-20张图片
   - 保存到网站目录

5. **阶段4: 网站开发** (3-5分钟)
   - 生成数据库脚本
   - 创建Jinja2模板
   - 初始化数据库
   - 启动开发服务器

6. **阶段5: 网站测试** (2-3分钟)
   - 测试所有页面
   - 检查图片和链接
   - 验证移动端响应
   - 生成测试报告

7. **阶段6: 修复循环** (如需要, 每次2-3分钟)
   - 自动修复发现的问题
   - 重新测试
   - 最多5次迭代

8. **阶段7: 完成** (1分钟)
   - 生成最终报告
   - 提供访问URL和使用说明

**总耗时**: 约15-30分钟

### 步骤4: 访问生成的网站

```bash
# 网站会保存在项目根目录
cd D:/projects/docmsnz/greenhouse.nz  # 或你的网站目录名

# 启动服务器(如果未自动启动)
python app.py

# 访问网站
# http://localhost:8000
```

## 📁 生成的网站结构

```
{网站目录名}/
├── .claude/workflow/          # 规划文档
│   ├── WEBSITE_REQUIREMENTS.md
│   ├── CONTENT_PLAN.md
│   ├── IMAGE_GENERATION_PLAN.md
│   ├── DATABASE_SCHEMA.md
│   ├── TEMPLATE_PLAN.md
│   └── TODOS.md
│
├── app/                       # 应用核心代码
├── docms/                     # CMS引擎
├── instance/
│   ├── database.db           # SQLite数据库
│   └── media/                # 媒体文件
│
├── templates/                # 模板文件
│   ├── base.html
│   ├── home.html             # 首页
│   ├── product_list.html     # 产品列表
│   ├── product_detail.html   # 产品详情
│   ├── post_list.html        # 文章列表
│   ├── post_detail.html      # 文章详情
│   ├── about.html            # 关于我们
│   ├── contact.html          # 联系我们
│   └── static/
│       ├── css/main.css      # 样式文件
│       └── images/           # AI生成的图片
│
├── seed_data.sql             # 数据库脚本
├── app.py                    # 应用入口
└── site.yaml                 # 站点配置
```

## 📝 规划文档说明

所有规划文档保存在 `.claude/workflow/` 目录:

### WEBSITE_REQUIREMENTS.md
- 行业分析和目标用户
- 功能需求和验收标准
- 参考网站分析
- 设计要求

### CONTENT_PLAN.md
- 网站设置(名称、联系方式等)
- 产品/服务详细内容(5-10个)
- 文章详细内容(6-10篇)
- 单页内容(关于我们、联系我们)

### IMAGE_GENERATION_PLAN.md
- 所有图片清单(15-20张)
- 每张图片的详细AI生成提示词
- 图片用途和尺寸要求

### DATABASE_SCHEMA.md
- 数据库表结构
- 所有数据记录规划
- 外键关系

### TEMPLATE_PLAN.md
- 7个模板文件设计
- 设计风格指南(颜色、字体、布局)
- 响应式设计要求

### TODOS.md
- 工作流进度跟踪
- 每个阶段的任务状态
- 测试结果记录

## 🎨 网站功能

生成的网站包含以下功能:

### 前台功能
- ✅ 响应式首页(Hero banner, 推荐产品, 最新文章)
- ✅ 产品/服务列表页(分类筛选)
- ✅ 产品/服务详情页(图片、描述、相关产品)
- ✅ 文章列表页(分类筛选、侧边栏)
- ✅ 文章详情页(内容、相关文章)
- ✅ 关于我们页面
- ✅ 联系我们页面(联系表单、联系信息)
- ✅ 导航菜单
- ✅ 页脚(联系信息、快捷链接)

### 技术特性
- ✅ FastAPI后端
- ✅ Jinja2模板引擎(SSR)
- ✅ SQLite数据库
- ✅ SQLAlchemy ORM
- ✅ 移动端响应式设计
- ✅ SEO优化(语义化HTML、Meta标签)
- ✅ 图片懒加载
- ✅ 现代化UI设计

### 内容特点
- ✅ 专业、真实的内容(非Lorem Ipsum)
- ✅ 新西兰本地化
- ✅ 行业特色突出
- ✅ AI生成的高质量图片
- ✅ SEO友好的URL(slug)

## 🔧 自定义和修改

### 修改网站内容

**方法1: 修改数据库**
```bash
cd {网站目录}
sqlite3 instance/database.db

# 查看产品
SELECT * FROM product;

# 修改产品
UPDATE product SET name='新产品名' WHERE id=1;

# 添加产品
INSERT INTO product (name, slug, summary, ...) VALUES (...);
```

**方法2: 修改seed_data.sql并重新导入**
```bash
# 编辑 seed_data.sql

# 重新导入
rm instance/database.db
alembic upgrade head
sqlite3 instance/database.db < seed_data.sql
```

### 修改网站样式

编辑 `templates/static/css/main.css`:
```css
:root {
  --primary-color: #your-color;  /* 修改主色调 */
  --secondary-color: #your-color;
}
```

### 修改模板布局

编辑模板文件,如 `templates/home.html`:
```html
{% extends "base.html" %}

{% block content %}
<!-- 修改首页布局 -->
{% endblock %}
```

### 添加新功能

1. 修改数据库模型: `app/models/`
2. 创建迁移: `alembic revision --autogenerate -m "add feature"`
3. 运行迁移: `alembic upgrade head`
4. 添加路由: `app/routes/`
5. 创建模板: `templates/`

## 📊 工作流程详解

### DM协调机制

系统使用 `website_dm.py` hook自动协调整个流程:

1. **监听Agent完成**: 每个agent完成后触发hook
2. **读取TODOS.md**: 判断当前进度和下一步
3. **决策下一步**: 自动选择下一个agent或操作
4. **传递指令**: 给DM明确的下一步指令

### Agent职责

**website_planner**:
- 阅读行业研究报告
- 搜索参考网站
- 规划网站结构和内容
- 创建详细的规划文档
- 设计图片生成方案

**website_developer**:
- 生成SQL数据库脚本
- 创建Jinja2模板文件
- 编写CSS样式
- 初始化数据库
- 启动开发服务器

**website_tester**:
- 使用Chrome DevTools MCP测试
- 检查所有页面加载
- 验证所有图片(无404)
- 验证所有链接(无404)
- 测试移动端响应
- 生成测试报告

### 错误处理和修复

如果测试失败:
1. Tester生成详细的失败报告
2. Hook自动调用Developer修复
3. Developer根据报告修复问题
4. Hook自动调用Tester重新测试
5. 重复最多5次,直到通过或达到上限

## 💰 成本估算

### AI服务成本

**智谱AI图片生成**:
- 单价: ~¥0.10/张
- 网站图片数: 15-20张
- 图片成本: ¥1.50-¥2.00

**Claude API**:
- Tokens消耗: 约50,000-80,000 tokens
- 成本: 约$0.50-$1.00 (Claude 3.5 Sonnet)

**总成本**: 约$1.50-$2.00 (或¥10-¥15)

### 时间成本

- 自动化流程: 15-30分钟
- 人工开发: 3-5天
- **时间节省**: 约95%

## 🐛 故障排除

### 问题1: API密钥无效

**症状**: 图片生成失败,提示API key invalid

**解决**:
1. 检查 `.claude/config/zhipu_api_key.txt` 是否存在
2. 验证API密钥是否正确
3. 检查API账户是否有余额
4. 重新生成API密钥

### 问题2: 服务器无法启动

**症状**: `python app.py` 失败

**解决**:
1. 检查是否安装了依赖: `pip install -r requirements.txt`
2. 检查是否运行了迁移: `alembic upgrade head`
3. 检查数据库是否存在: `ls instance/database.db`
4. 查看错误日志,根据提示修复

### 问题3: 图片显示404

**症状**: 网站图片无法加载

**解决**:
1. 检查图片是否已生成: `ls templates/static/images/`
2. 检查数据库中图片路径是否正确
3. 检查图片文件名是否与数据库匹配
4. 重新运行图片生成步骤

### 问题4: 测试一直失败

**症状**: 进入无限修复循环

**解决**:
1. 查看 `.claude/workflow/TODOS.md` Phase 5 的详细错误
2. 手动查看网站,确认问题
3. 如果是图片问题,检查图片生成
4. 如果是链接问题,检查数据库slug
5. 手动修复后重新测试

### 问题5: 内容不符合行业

**症状**: 生成的内容与行业不匹配

**解决**:
1. 检查输入的提示词是否清晰
2. 查看 `CONTENT_PLAN.md`,确认内容规划
3. 手动修改 `seed_data.sql` 中的内容
4. 重新导入数据库

## 📚 最佳实践

### 输入提示词

**好的提示词示例**:
```
/auto-website 我想为一家新西兰奥克兰的律师事务所建立网站,公司名叫Smith & Partners Law,专注于家庭法和商业法,服务新西兰本地客户
```

**包含以下要素**:
- ✅ 行业类型(律师事务所)
- ✅ 公司名称(Smith & Partners Law)
- ✅ 地理位置(奥克兰)
- ✅ 业务特点(家庭法、商业法)
- ✅ 目标客户(新西兰本地)

### 行业选择

选择行业时,参考 `新西兰中小企业网站模板研究报告.md` 中的分类:
- 建筑与工程
- 专业服务(法律、会计、咨询等)
- 零售与电子商务
- 餐饮与酒店
- 医疗保健
- 农业、林业与渔业
- 旅游与娱乐
- 健身与健康
- 教育与培训
- 汽车服务
- 信息技术与通信
- 艺术与创意服务
- 家庭服务
- 环境与可持续发展

### 图片生成

系统会自动为以下内容生成图片:
- Hero/Banner (1-2张)
- 产品图片 (5-10张)
- 文章配图 (6-10张)
- 背景图 (2-3张)
- 关于我们/团队 (1-2张)

如果对生成的图片不满意:
1. 查看 `IMAGE_GENERATION_PLAN.md` 中的提示词
2. 修改提示词(更具体或更简洁)
3. 重新运行图片生成步骤

## 🚀 部署上线

### 准备部署

1. **环境配置**:
```bash
# 生产环境变量
export FLASK_ENV=production
export DATABASE_URL=postgresql://...  # 如果使用PostgreSQL
```

2. **静态文件优化**:
```bash
# 压缩图片
# 合并和压缩CSS/JS
# 启用CDN
```

3. **数据库迁移**:
```bash
# 如果使用PostgreSQL
# 导出SQLite数据
# 导入PostgreSQL
```

### 部署选项

**选项1: Railway/Heroku**
- 适合小型网站
- 免费或低成本
- 简单部署

**选项2: VPS (DigitalOcean, Linode等)**
- 更多控制权
- 适合中型网站
- 需要服务器管理知识

**选项3: 新西兰本地托管**
- 更快的本地访问速度
- 符合数据主权要求
- 推荐供应商: SiteHost, VentraIP等

### 域名配置

1. 注册 `.nz` 域名
2. 配置DNS指向服务器
3. 配置SSL证书(Let's Encrypt免费)
4. 更新 `site.yaml` 中的 `site_url`

## 📞 支持和反馈

如有问题或建议:
1. 查看本指南的故障排除部分
2. 检查 `.claude/workflow/TODOS.md` 了解当前状态
3. 查看agent配置文件了解详细流程
4. 提交Issue到项目仓库

## 🎓 进阶使用

### 自定义Agent行为

修改 `.claude/agents/` 下的agent配置文件:
- `website_planner.md` - 调整规划策略
- `website_developer.md` - 调整开发流程
- `website_tester.md` - 调整测试标准

### 添加新的行业

在 `新西兰中小企业网站模板研究报告.md` 中添加新行业:
1. 添加行业描述
2. 定义典型栏目结构
3. 提供参考网站示例
4. 描述行业特点

### 集成其他服务

可以集成以下服务:
- Google Analytics - 网站分析
- Mailchimp - 邮件营销
- Stripe - 在线支付
- Twilio - 短信通知
- SendGrid - 邮件发送

## 📊 系统架构

```
用户输入提示词
    ↓
/auto-website 命令
    ↓
DM解析需求 (阶段0)
    ↓
CLI创建网站目录 (阶段1)
    ↓
website_planner agent → 规划文档 (阶段2)
    ↓ (SubagentStop hook触发)
    ↓
website_dm.py 读取TODOS.md
    ↓
DM生成图片 using Zhipu AI API (阶段3)
    ↓
website_developer agent → 数据库+模板 (阶段4)
    ↓ (SubagentStop hook触发)
    ↓
website_tester agent → 功能测试 (阶段5)
    ↓ (SubagentStop hook触发)
    ↓
Tests Pass? → Yes → 完成报告 (阶段7)
    ↓ No
    ↓
website_developer agent → 修复 (阶段6)
    ↓
website_tester agent → 重新测试
    ↓ (循环最多5次)
    ↓
完成 (PASS 或 PARTIAL)
```

## 🌟 未来改进

计划中的功能:
- [ ] 支持更多图片生成服务(DALL-E, Midjourney等)
- [ ] 多语言支持(英语/中文切换)
- [ ] 管理后台界面
- [ ] 在线支付集成
- [ ] SEO工具集成
- [ ] 性能监控面板
- [ ] A/B测试功能
- [ ] 用户评论系统
- [ ] 社交媒体集成

---

**祝您使用愉快! 🎉**

*AI自动化建站系统 v1.0*
*Powered by Claude Code + Docms CMS + 智谱AI*
