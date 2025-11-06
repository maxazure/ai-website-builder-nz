# CLI 工具使用确认文档

**日期**: 2025-11-04
**更新内容**: 确认和规范 Coder 和 Asset Maker 使用的 CLI 工具

---

## 1. Coder Agent - 使用 docms-scaffold CLI ✅

### CLI 工具
**文件**: `docms-scaffold/create_project_modular.py`

### 使用方式
```bash
cd docms-scaffold
python create_project_modular.py {project_name} --preset {preset}
```

### 功能
- 创建模块化项目骨架
- 支持预设方案 (corporate, blog, ecommerce, portfolio, etc.)
- 自动解析模块依赖
- 复制对应的 models, services, schemas 文件
- 生成 __init__.py 文件

### 预设方案
- `corporate`: 企业官网
- `blog`: 博客网站
- `ecommerce`: 电商网站
- `portfolio`: 作品展示
- `restaurant`: 餐厅网站
- 等...

### 在 coder.md 中的体现
```bash
# 核心任务 - 1. 调用docms-scaffold CLI生成骨架
cd docms-scaffold
python create_project_modular.py {project_name} --preset {preset}
cd ../{project_name}
```

---

## 2. Asset Maker Agent - 使用 tools/generate_images.py ✅

### CLI 工具
**文件**: `tools/generate_images.py`

### 使用方式
```bash
python tools/generate_images.py --config images.json
```

### 功能
- 批量图片生成
- 使用 Zhipu AI CogView-3-Flash API
- 从 JSON 配置文件读取图片清单
- 按优先级生成 (high → medium → low)
- 自动下载并保存
- 跳过已存在文件
- 2秒间隔防止API限流

### 环境变量
```bash
export ZHIPU_KEY='your-api-key'
```

### 配置文件格式 (images.json)
```json
{
  "output_dir": "templates/static/images",
  "images": [
    {
      "filename": "hero-banner.jpg",
      "prompt": "Beautiful modern office space with natural lighting...",
      "priority": "high"
    },
    {
      "filename": "product-1.jpg",
      "prompt": "Professional IT services equipment on desk...",
      "priority": "medium"
    }
  ]
}
```

### Asset Maker 工作流
1. **解析输入**: 读取 ASSET_MANIFEST.md、CONTENT_DATA.json、DESIGN_SYSTEM.json
2. **生成配置**: 创建 images.json，融入设计系统风格
3. **调用CLI**: `python tools/generate_images.py --config images.json`
4. **生成报告**: 解析CLI输出，生成 ASSET_REPORT.md

### 设计系统集成
Asset Maker 会从 DESIGN_SYSTEM.json 提取：
- 主色调 (primary color)
- 风格关键词 (modern, professional, clean, etc.)
- 将这些融入图片生成提示词中，确保图片风格与网站设计一致

---

## 3. 更新的文件清单

### Agent 定义
- ✅ `.claude/agents/asset_maker.md` - 更新为使用 tools/generate_images.py

### 配置文件
- ✅ `.claude/settings.json` - 环境变量从 ZHIPU_API_KEY 改为 ZHIPU_KEY

### 文档
- ✅ `.claude/ARCHITECTURE.md` - 明确两个 agent 使用的 CLI 工具
- ✅ `.claude/AGENT_SUMMARY.md` - 更新工具说明和环境变量

---

## 4. 环境变量统一

所有文档和配置现已统一使用：
- `ZHIPU_KEY` (匹配 tools/generate_images.py 中的实际使用)

---

## 5. 优势

### Coder 使用 CLI
- ✅ 复用成熟的模块化脚手架
- ✅ 自动处理模块依赖
- ✅ 减少 agent 复杂度
- ✅ 提高项目结构一致性

### Asset Maker 使用 CLI
- ✅ 复用已测试的图片生成工具
- ✅ 统一的API调用和错误处理
- ✅ 自动限流和重试
- ✅ Agent 只需专注于配置文件生成和报告整理

---

**状态**: ✅ 全部确认和更新完成
