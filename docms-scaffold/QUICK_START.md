# Docms 脚手架 - 快速启动指南

> 5 分钟创建你的第一个企业官网

## 前置要求

- Python 3.11+
- SQLite 3
- LLM 访问（Claude、GPT-4 或其他）

## 创建你的第一个站点

### 步骤 1：创建站点（1 分钟）

```bash
# 进入脚手架目录
cd docms-python

# 创建新站点
python -m cli.create_site --name my-first-site --company "我的公司" --description "企业官网"

# 进入站点目录
cd ../my-first-site
```

你会看到：
```
🚀 创建新站点: my-first-site
📁 目标目录: D:\projects\my-first-site

📦 创建目录结构...
  ✓ instance
  ✓ templates
  ✓ migrations
  ...

✅ 站点创建成功！
```

### 步骤 2：安装依赖（2 分钟）

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate  # Windows
# 或
source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt
```

### 步骤 3：生成内容（5 分钟）

```bash
# 运行内容生成工具
python -m cli.generate_content
```

**交互式问答示例**：

```
🤖 Docms 智能内容生成器

请提供以下公司信息：

公司名称: 绿芽智能科技
所属行业: 智能水培设备
主要产品/服务: 家用水培机,商用水培系统,配套耗材
公司简介: 专注智能水培设备研发与生产的创新型企业
目标客户: 家庭用户,餐饮企业,农业公司
产品分类: 家用设备,商用设备,配套耗材
文章分类: 公司动态,技术文档,行业资讯

收集完成！

📝 生成数据库内容提示词...
  ✓ 提示词已保存到: prompts/database_prompt.txt

📝 生成模板内容提示词...
  ✓ 提示词已保存到: prompts/template_prompt.txt
```

### 步骤 4：使用 LLM 生成内容（3 分钟）

#### 4.1 生成数据库内容

1. 打开 `prompts/database_prompt.txt`
2. 复制全部内容
3. 发送给 Claude（或 GPT-4）
4. 将返回的 SQL 脚本保存为 `seed_data.sql`

**示例对话**：

```
你: [粘贴 database_prompt.txt 的内容]

Claude: 好的，我来为绿芽智能科技生成数据库填充脚本...

[返回完整的 SQL 脚本]

你: [复制 SQL 脚本，保存为 seed_data.sql]
```

#### 4.2 生成模板文件

1. 打开 `prompts/template_prompt.txt`
2. 复制全部内容
3. 发送给 Claude
4. 将返回的每个模板保存到 `templates/` 目录

**提示**：可以要求 Claude 一次性返回所有模板，然后手动分割保存。

### 步骤 5：初始化数据库（1 分钟）

```bash
# 运行数据库迁移
alembic upgrade head

# 填充数据
sqlite3 instance/database.db < seed_data.sql
```

看到类似输出即成功：
```
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> fc6845b44247, add_indexes_for_performance
```

### 步骤 6：启动服务器（立即）

```bash
python app.py
```

看到：
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345]
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
🚀 我的公司 启动成功
📁 模板目录: D:\projects\my-first-site\templates
```

### 步骤 7：访问网站

打开浏览器访问：**http://localhost:8000**

你应该能看到：
- ✅ 响应式首页
- ✅ 产品列表
- ✅ 文章列表
- ✅ 关于我们
- ✅ 联系我们

## 常见问题

### Q1: `pip install` 太慢怎么办？

使用国内镜像：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q2: SQLite 命令找不到？

**Windows**: 下载 [sqlite-tools](https://www.sqlite.org/download.html) 并添加到 PATH

**或者使用 Python**：
```bash
python -c "import sqlite3; conn = sqlite3.connect('instance/database.db'); conn.executescript(open('seed_data.sql').read()); conn.commit()"
```

### Q3: LLM 生成的 SQL 有错误？

手动编辑 `seed_data.sql` 修复错误，常见问题：
- 外键 ID 不匹配
- slug 重复
- 日期格式错误

### Q4: 模板显示不正确？

检查：
1. `templates/` 目录下是否有所有必需的模板文件
2. `site.yaml` 中的 `template_dir` 配置是否正确
3. CSS 文件是否正确生成

### Q5: 想修改样式怎么办？

编辑 `templates/static/css/main.css`，或者要求 LLM 重新生成更好的样式。

## 下一步

### 自定义内容

1. **修改站点配置**：编辑 `site.yaml`
2. **添加更多产品**：直接在数据库中插入或重新生成
3. **修改样式**：编辑 CSS 文件
4. **添加新页面**：创建新模板文件

### 部署上线

参考 [部署文档](./DEPLOYMENT.md)（即将推出）

常见部署选项：
- Railway
- Render
- DigitalOcean
- AWS EC2
- 自建服务器

### 学习更多

- [FastAPI 教程](https://fastapi.tiangolo.com/tutorial/)
- [SQLAlchemy 教程](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Jinja2 模板语法](https://jinja.palletsprojects.com/en/3.1.x/templates/)

## 性能和成本

### 时间成本
- 创建站点：1 分钟
- 安装依赖：2 分钟
- 生成内容：5 分钟（交互式）
- LLM 生成：3 分钟
- 初始化数据库：1 分钟
- **总计：12 分钟**

### Token 成本（使用 Claude 3.5 Sonnet）
- 输入 Token：~3,500
- 输出 Token：~8,000
- **总 Token：~11,500**
- **成本：~$0.15 USD**

### 服务器成本
- 开发：免费（本地）
- 小型站点：$5-10/月（Railway、Render）
- 中型站点：$20-50/月（VPS）

## 提示和技巧

### 💡 技巧 1：保存成功的提示词

如果某个提示词生成的内容很好，保存它作为模板：
```bash
cp prompts/database_prompt.txt prompts/templates/my_template.txt
```

下次只需修改公司信息部分。

### 💡 技巧 2：分批生成减少错误

先生成并验证数据库内容，确认无误后再生成模板。

### 💡 技巧 3：使用更便宜的 LLM

- Claude Haiku：更便宜但质量略低
- GPT-3.5：成本更低
- 本地 LLM：完全免费但需要强大的硬件

### 💡 技巧 4：复用模板减少成本

如果你要创建多个相似的站点（如同行业），可以：
1. 第一个站点完整生成
2. 后续站点复制模板文件
3. 只用 LLM 生成数据库内容

成本降低 50%！

## 故障排除

### 问题：数据库迁移失败

```bash
# 清理重来
rm -rf instance/database.db migrations/versions/*.py
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

### 问题：模板渲染错误

检查模板语法：
```bash
python -c "from jinja2 import Template; Template(open('templates/home.html').read())"
```

### 问题：静态文件404

确保 `site.yaml` 中的路径正确：
```yaml
static_dir: "./templates/static"
```

## 获取帮助

- GitHub Issues: [提交问题](https://github.com/your-repo/docms-scaffold/issues)
- 文档: [完整文档](./README-SCAFFOLD.md)
- 架构说明: [架构文档](./ARCHITECTURE.md)

---

**开始创建你的第一个站点吧！ 🚀**
