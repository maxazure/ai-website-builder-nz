# Docms Scaffold - 模块化网站生成系统

## 🎯 快速开始

### 使用预设方案（推荐）

```bash
# 企业官网
python create_project_modular.py my-website --preset corporate

# 电商网站
python create_project_modular.py my-shop --preset ecommerce

# 教育培训
python create_project_modular.py my-school --preset education

# 餐厅/咖啡馆
python create_project_modular.py my-restaurant --preset restaurant
```

### 自定义模块

```bash
# 手动指定模块
python create_project_modular.py my-site --modules team,portfolio,product,faq

# 交互式选择
python create_project_modular.py my-site --interactive
```

### 查看可用选项

```bash
# 列出所有预设方案
python create_project_modular.py --list-presets

# 列出所有可用模块
python create_project_modular.py --list-modules

# 查看帮助
python create_project_modular.py --help
```

---

## 📦 8个预设方案

| 方案 | 适用场景 | 包含模块数 |
|------|---------|-----------|
| **corporate** | 企业官网 | 10个 |
| **ecommerce** | 电商网站 | 12个 |
| **education** | 教育培训 | 13个 |
| **restaurant** | 餐厅/咖啡馆 | 9个 |
| **medical** | 医疗/诊所 | 11个 |
| **service** | 专业服务 | 11个 |
| **minimal** | 最小化配置 | 4个（仅核心） |
| **full** | 完整配置 | 24个（全部） |

---

## 🧩 20个核心模块

### 基础内容模块
- `post` - 新闻/博客
- `team` - 团队展示
- `portfolio` - 案例展示
- `product` - 产品/服务
- `custom_field` - 自定义字段
- `faq` - 常见问题

### 交互功能模块
- `comment` - 评论/评价
- `user` - 用户/会员
- `newsletter` - 通讯订阅

### 电商交易模块
- `cart` - 购物车
- `order` - 订单管理

### 预约与服务模块
- `booking` - 在线预约
- `restaurant` - 餐厅订餐
- `event` - 活动报名

### 多媒体与资源模块
- `gallery` - 图片画廊
- `video` - 视频展示
- `file_download` - 文件下载

---

## 🔧 系统组成

### 核心文件

```
docms-scaffold/
├── modules_config.yaml          # 模块配置文件
├── module_manager.py             # 模块管理器
├── create_project_modular.py    # 模块化生成器（新）
└── create_project.py             # 原始生成器（仍可用）
```

### 工作原理

1. **读取配置** - 从 `modules_config.yaml` 加载模块定义
2. **解析依赖** - 自动解析模块间的依赖关系
3. **复制文件** - 只复制选择的模块文件
4. **生成导入** - 动态生成 `__init__.py` 文件
5. **创建项目** - 生成轻量化的项目结构

---

## ✨ 核心优势

### 传统方式 vs 模块化方式

| 对比项 | 传统方式 | 模块化方式 |
|--------|---------|-----------|
| 生成内容 | 所有模块 | 按需选择 |
| 项目大小 | ~500KB | ~50-300KB |
| 数据库表 | 51个表 | 10-40个表 |
| 维护复杂度 | 高 | 低 |
| 启动速度 | 慢 | 快 |

### 主要特性

✅ **智能依赖解析** - 自动包含所需的依赖模块
✅ **8个预设方案** - 覆盖常见行业需求
✅ **灵活自定义** - 支持手动选择任意模块组合
✅ **交互式界面** - 友好的命令行交互
✅ **向后兼容** - 原有的 create_project.py 仍可使用

---

## 📝 使用示例

### 示例1: 创建公司官网

```bash
python create_project_modular.py acme-corp --preset corporate
cd acme-corp
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
alembic upgrade head
python app.py
```

包含功能：
- ✓ 新闻发布
- ✓ 团队展示
- ✓ 案例展示
- ✓ 产品/服务
- ✓ 常见问题
- ✓ 图片画廊
- ✓ 联系表单

### 示例2: 创建电商网站

```bash
python create_project_modular.py my-shop --preset ecommerce
```

包含功能：
- ✓ 产品管理
- ✓ 购物车
- ✓ 订单管理
- ✓ 用户系统
- ✓ 评论评价
- ✓ 邮件订阅

### 示例3: 自定义博客网站

```bash
python create_project_modular.py my-blog --modules post,comment,user,newsletter
```

只包含博客所需的模块，项目更轻量。

---

## 🔍 模块依赖关系

某些模块依赖其他模块。系统会自动解析并包含依赖。

**示例**: 选择 `order` 时自动包含：
- `order` → `cart` → `product` → `media`
- `order` → `user`
- `product` → `custom_field`

查看完整依赖关系：
```bash
python create_project_modular.py --list-modules
```

---

## 📚 完整文档

详细文档位于 `tools/` 目录：

- **模块化网站生成使用指南.md** - 完整使用指南
- **Docms网站系统20个核心模块说明文档.md** - 各模块详细说明

---

## 🆚 新旧对比

### 使用旧版生成器（生成所有模块）

```bash
python create_project.py my-website
```

生成结果：
- 📦 所有 51 个数据库表
- 📦 所有 26 个模型文件
- 📦 所有 14 个服务文件
- 📦 所有 50+ 个 Schema

### 使用新版生成器（按需生成）

```bash
python create_project_modular.py my-website --preset corporate
```

生成结果：
- 📦 约 20 个数据库表
- 📦 约 10 个模型文件
- 📦 约 6 个服务文件
- 📦 约 20 个 Schema

**项目大小减少 60%+，维护更简单！**

---

## 💡 最佳实践

### ✅ 推荐做法

1. **项目初期确定好模块** - 避免后期频繁修改
2. **使用预设方案** - 快速开始，涵盖常见需求
3. **查看 enabled_modules.txt** - 了解项目使用了哪些模块
4. **利用依赖自动解析** - 不用手动指定所有依赖

### ❌ 不推荐做法

1. ~~生成后再频繁添加/删除模块~~ - 需要手动操作
2. ~~使用 full 方案~~ - 除非真的需要所有功能
3. ~~禁用依赖模块~~ - 会导致功能异常

---

## 🎓 教程

### 第一次使用？

```bash
# 1. 查看可用方案
python create_project_modular.py --list-presets

# 2. 选择合适的方案
python create_project_modular.py my-site --preset corporate

# 3. 进入项目并初始化
cd my-site
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head

# 4. 启动开发服务器
python app.py
```

### 不确定选哪些模块？

```bash
# 使用交互式模式
python create_project_modular.py my-site --interactive

# 系统会引导你：
# 1. 选择预设方案 或 自定义
# 2. 按类别选择模块
# 3. 自动解析依赖
# 4. 生成项目
```

---

## 📞 获取帮助

```bash
# 命令行帮助
python create_project_modular.py --help

# 查看所有预设方案
python create_project_modular.py --list-presets

# 查看所有模块
python create_project_modular.py --list-modules
```

查看完整文档：
- `tools/模块化网站生成使用指南.md`
- `tools/Docms网站系统20个核心模块说明文档.md`

---

## 🚀 开始使用

**推荐**: 根据你的行业选择预设方案

```bash
# 企业官网
python create_project_modular.py my-company --preset corporate

# 在线商城
python create_project_modular.py my-shop --preset ecommerce

# 培训机构
python create_project_modular.py my-school --preset education

# 餐厅网站
python create_project_modular.py my-restaurant --preset restaurant

# 诊所网站
python create_project_modular.py my-clinic --preset medical

# 律师事务所
python create_project_modular.py law-firm --preset service
```

**灵活使用**: 自定义模块组合

```bash
python create_project_modular.py my-site --modules module1,module2,module3
```

**探索模式**: 交互式选择

```bash
python create_project_modular.py my-site --interactive
```

---

**🎉 享受模块化开发带来的便利！**
