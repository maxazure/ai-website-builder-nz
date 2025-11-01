# brownsbay-language-school.nz

基于 Docms CMS 创建的企业官网

## 快速开始

### 1. 安装依赖

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 2. 配置站点

编辑 `site.yaml` 文件，配置站点基本信息。

### 3. 生成内容（使用 LLM）

```bash
python -m cli.generate_content
```

按照提示输入公司信息，LLM 将自动生成：
- 数据库内容（产品、文章、栏目等）
- 页面模板（HTML）

### 4. 初始化数据库

```bash
alembic upgrade head
sqlite3 instance/database.db < seed_data.sql
```

### 5. 启动服务器

```bash
python app.py
```

访问 http://localhost:8000

## 目录结构

```
brownsbay-language-school.nz/
├── app/                    # 核心应用代码
├── docms/                  # Docms 引擎
├── instance/               # 站点实例数据
│   ├── database.db        # SQLite 数据库
│   └── media/             # 媒体文件
├── templates/              # 模板文件
│   ├── base.html
│   ├── home.html
│   └── static/
├── migrations/             # 数据库迁移
├── app.py                  # 应用入口
└── site.yaml              # 站点配置
```

## 自定义

### 修改模板

编辑 `templates/` 目录下的 HTML 文件。

### 修改样式

编辑 `templates/static/css/main.css`。

### 添加内容

通过数据库或使用 LLM 生成工具添加产品、文章等内容。

## 部署

参考 [Docms 部署文档](https://github.com/your-repo/docms-scaffold)

---

Powered by [Docms CMS](https://github.com/your-repo/docms-scaffold)
