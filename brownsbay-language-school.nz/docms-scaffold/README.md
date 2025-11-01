# Docms Scaffold

Docms CMS 项目模板，用于快速创建新的网站项目。

## 快速开始

### 1. 使用 Scaffold 创建新项目

```bash
python create_project.py my-new-website
```

### 2. 进入项目目录

```bash
cd my-new-website
```

### 3. 设置虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

### 5. 初始化数据库

```bash
# 如果有 Alembic 迁移
alembic upgrade head

# 导入初始数据（可选）
sqlite3 instance/database.db < config/seed_data.sql
```

### 6. 启动应用

```bash
python app.py
```

## 项目结构

```
your-project/
├── app.py                    # 应用入口
├── site.yaml                 # 站点配置
├── requirements.txt          # Python 依赖
├── alembic.ini              # 数据库迁移配置
├── app/                     # 应用代码
│   ├── main.py             # 应用工厂
│   ├── config.py           # 配置管理
│   ├── models/             # 数据模型
│   ├── routes/             # 路由处理
│   ├── services/           # 业务逻辑
│   ├── utils/              # 工具函数
│   └── ...
├── templates/              # HTML 模板
├── migrations/             # 数据库迁移
├── instance/               # 运行时数据
└── logs/                   # 日志文件
```

## 自定义模板

### 修改站点配置

编辑 `site.yaml` 文件来配置你的网站:

```yaml
site_name: "Your Website Name"
site_description: "Your website description"
site_url: "https://yourwebsite.com"
```

### 自定义模板

在 `templates/` 目录中创建你的 HTML 模板文件。

### 添加数据模型

在 `app/models/` 目录中定义你的数据模型。

### 创建路由

在 `app/routes/` 目录中添加你的路由处理。

## 开发指南

### 添加新页面

1. 在 `templates/` 中创建模板文件
2. 在 `app/routes/frontend.py` 中添加路由
3. 在 `site.yaml` 中配置栏目

### 数据库迁移

```bash
# 创建新的迁移
alembic revision --autogenerate -m "描述变更"

# 应用迁移
alembic upgrade head

# 回滚迁移
alembic downgrade -1
```

### 部署

```bash
# 生产环境启动
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 文档

- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 文档](https://docs.sqlalchemy.org/)
- [Jinja2 文档](https://jinja.palletsprojects.com/)

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

---

创建时间: 2025-11-02 11:06:19
版本: 1.0.0
