# AI Website Builder - 新架构说明

## 架构概览

```
┌─────────────────────────────────────────────────────────────┐
│              Orchestrator (总控编排器)                       │
│  ・有向状态机 (FSM)                                         │
│  ・队列管理、超时控制、重试机制、回滚策略                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────── 8个专门化Agents ───────────────────────┐
│                                                              │
│  [1] Architect         → 产品规划、IA设计、内容框架          │
│  [2] Content Manager   → 生成实际内容数据                   │
│  [3] Schema Designer   → 数据库模型设计                     │
│  [4] Design System     → 视觉设计系统（颜色、字体、风格）    │
│  [5] Asset Maker       → AI图片生成(Zhipu AI)              │
│  [6] Coder             → 代码生成、模板填充                 │
│  [7] Tester            → 功能测试、质量验证                 │
│  [8] SEO Polisher      → SEO优化、内容润色                 │
│                                                              │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────── 共享设施层 ──────────────────────────────┐
│  ・Tools: scaffold CLI, Git, Chrome DevTools MCP            │
│  ・Memory: 行业模板KB、组件片段库、提示词库                  │
│  ・Artifacts: /workspace/{site_slug}/ 工件存储               │
└──────────────────────────────────────────────────────────────┘
```

---

## 文件结构

```
.claude/
├── commands/
│   └── auto-website.md              # Orchestrator总控编排器 ✅ 已完成
│
├── agents/
│   ├── architect.md                 # [1] 产品规划专家 ✅ 已完成
│   ├── content_manager.md           # [2] 内容生成专家 ✅ 已完成
│   ├── schema_designer.md           # [3] 数据库模型设计师 ✅ 已完成
│   ├── design_system.md             # [4] 设计系统专家 ✅ 已完成
│   ├── asset_maker.md               # [5] 静态资源生成器 ✅ 已完成
│   ├── coder.md                     # [6] 代码生成与开发 ✅ 已完成
│   ├── tester.md                    # [7] 测试与验证 ✅ 已完成
│   └── seo_polisher.md              # [8] SEO内容润色 ✅ 已完成
│
├── backup/                          # 旧版本备份
│   ├── website_planner_old.md
│   ├── website_developer_old.md
│   └── website_tester_old.md
│
├── hooks/
│   ├── test_checker.py
│   ├── website_dm.py
│   └── workflow_dm.py
│
└── settings.json                    # 配置文件 🔄 需更新
```

---

## Agent职责划分

### 1. Architect (产品规划专家)
**原**: website_planner
**新职责**:
- 行业研究与分析
- 信息架构(IA)设计
- 页面蓝图规划
- 内容策略制定
- 资产清单生成

**输入**:
- project_metadata (项目元数据)
- user_input (用户需求)
- industry_kb (行业知识库)
- modules_config.yaml

**输出**:
- REQUIREMENTS.md (需求文档)
- IA_DESIGN.md (信息架构)
- PAGE_BLUEPRINT.md (页面蓝图)
- CONTENT_PLAN.md (内容计划)
- ASSET_MANIFEST.md (资产清单)

**工具**: Read, Grep, Glob, WebSearch, WebFetch, Write

---

### 2. Content Manager (内容生成专家)
**原**: 无 (新增)
**职责**:
- 解析内容需求
- 生成实际的网站内容数据
- 确保新西兰本地化
- 生成结构化JSON数据

**输入**:
- CONTENT_PLAN.md (内容计划框架)
- IA_DESIGN.md (信息架构)
- PAGE_BLUEPRINT.md (页面蓝图)
- REQUIREMENTS.md (需求文档)
- PROJECT_METADATA.json

**输出**:
- CONTENT_DATA.json (完整的结构化内容数据)
- CONTENT_GENERATION_REPORT.md (内容生成报告)

**工具**: Read, Write, WebSearch, WebFetch, Grep, Glob

---

### 3. Schema Designer (数据库模型设计师)
**原**: 无 (新增)
**职责**:
- 从IA设计推导数据实体
- 设计数据库schema
- 规划表关系和外键
- 设计seed data结构

**输入**:
- IA_DESIGN.md
- CONTENT_DATA.json (实际内容数据)
- enabled_modules.txt
- modules_config.yaml

**输出**:
- DATABASE_SCHEMA.md (schema设计)
- SEED_DATA_SPEC.md (seed数据规格)
- db_tables.json (机器可读表结构)

**工具**: Read, Write, Grep, Glob

---

### 4. Design System (设计系统专家)
**原**: 无 (新增)
**职责**:
- 行业风格研究
- 设计颜色调色板
- 设计字体系统
- 定义间距系统
- 设计组件样式规范
- 生成CSS设计令牌

**输入**:
- CONTENT_DATA.json (了解业务内容)
- REQUIREMENTS.md
- IA_DESIGN.md
- PROJECT_METADATA.json (行业信息)

**输出**:
- DESIGN_SYSTEM.json (完整设计系统规范)
- DESIGN_TOKENS.css (CSS变量定义)
- COMPONENT_SPECS.md (组件设计规范)
- DESIGN_REPORT.md (设计决策说明)

**工具**: Read, Write, WebSearch, WebFetch, Grep, Glob

---

### 5. Asset Maker (静态资源生成器)
**原**: 无 (原在planner中)
**职责**:
- 解析asset manifest和内容数据
- 生成images.json配置文件
- 调用tools/generate_images.py批量生成图片
- 生成资产报告

**输入**:
- ASSET_MANIFEST.md
- CONTENT_DATA.json (提取image_prompt)
- DESIGN_SYSTEM.json (获取颜色和风格指导)
- project_directory

**输出**:
- images.json (图片生成配置)
- templates/static/images/*.jpg (所有图片)
- ASSET_REPORT.md (生成报告)

**工具**: Read, Write, Bash, WebFetch
**CLI**: tools/generate_images.py
**环境变量**: ZHIPU_KEY

---

### 6. Coder (代码生成与开发)
**原**: website_developer
**新职责**:
- 调用docms-scaffold CLI生成骨架
- 生成模块化seed_data.sql
- 创建Jinja2模板
- 生成CSS/JS
- 创建app.py、config.py
- 数据库初始化
- 启动dev server
- (Debug模式) 修复测试失败问题

**输入**:
- DATABASE_SCHEMA.md
- SEED_DATA_SPEC.md
- CONTENT_DATA.json (实际内容数据)
- DESIGN_SYSTEM.json (设计系统规范)
- DESIGN_TOKENS.css (CSS变量)
- ASSET_REPORT.md
- enabled_modules.txt

**输出**:
- {project}/  (完整项目代码)
- seed_data.sql
- templates/*.html
- app.py, config.py

**工具**: Read, Write, Edit, Bash, Grep, Glob
**CLI**: docms-scaffold/create_project_modular.py

---

### 7. Tester (测试与验证)
**原**: website_tester
**新职责**:
- 使用Chrome DevTools MCP测试
- 验证所有页面可访问
- 检查图片加载(无404)
- 检查链接有效性
- 测试移动响应式
- 检查JS控制台错误

**输入**:
- project_directory
- website_url (http://localhost:8000)
- REQUIREMENTS.md
- ASSET_MANIFEST.md

**输出**:
- TEST_REPORT.md (测试报告)
- screenshots/*.png (截图)

**工具**: Bash, Read, Grep, Glob
**MCP**: Chrome DevTools

---

### 8. SEO Polisher (SEO内容润色)
**原**: 无 (新增)
**职责**:
- 为所有页面添加meta tags
- 生成sitemap.xml
- 生成robots.txt
- 添加schema.org结构化数据
- 添加Open Graph tags
- 生成favicon
- 检查WCAG无障碍性

**输入**:
- project_directory
- CONTENT_DATA.json
- templates/*.html

**输出**:
- meta_tags.json
- sitemap.xml
- robots.txt
- favicon.ico
- SEO_REPORT.md

**工具**: Read, Write, Edit, Grep, Glob

---

---

## 工作流程

### Phase 0: INIT (初始化)
- 解析用户需求
- 匹配预设方案
- 创建workspace
- 初始化FSM

### Phase 1: PLANNING (Architect)
- 行业研究
- IA设计
- 内容规划框架
- 资产清单

### Phase 2: CONTENT_GENERATION (Content Manager)
- 生成实际内容数据
- 公司信息、产品、团队、文章
- 新西兰本地化
- 输出 CONTENT_DATA.json

### Phase 3: SCHEMA_DESIGN (Schema Designer)
- 数据库设计
- seed data规格

### Phase 4: DESIGN_SYSTEM (Design System)
- 行业风格研究
- 颜色调色板设计
- 字体系统设计
- 间距系统定义
- 组件样式规范
- 输出设计令牌

### Phase 5: ASSET_GENERATION (Asset Maker)
- AI图片生成（基于设计系统风格）
- 资产报告

### Phase 6: CODE_GENERATION (Coder)
- scaffold生成
- SQL生成（使用CONTENT_DATA.json）
- 模板生成（使用DESIGN_TOKENS.css）
- 数据库初始化

### Phase 7: TESTING (Tester)
- 功能测试
- 质量验证
- 如失败→DEBUG_LOOP

### Phase 8: SEO_OPTIMIZATION (SEO Polisher)
- SEO优化
- meta tags
- sitemap

### Phase 9: COMPLETED
- 交付报告
- 项目总结

---

## 状态机特性

### 超时控制
```yaml
PLANNING: 300s
CONTENT_GENERATION: 240s
SCHEMA_DESIGN: 180s
DESIGN_SYSTEM: 200s
ASSET_GENERATION: 600s
CODE_GENERATION: 300s
TESTING: 300s
SEO_OPTIMIZATION: 180s
```

### 重试机制
```yaml
PLANNING: max_retries=2
CONTENT_GENERATION: max_retries=2
SCHEMA_DESIGN: max_retries=2
DESIGN_SYSTEM: max_retries=2
ASSET_GENERATION: max_retries=3 (non-blocking)
CODE_GENERATION: max_retries=2
DEBUG_LOOP: max_iterations=3
SEO_OPTIMIZATION: max_retries=1 (non-blocking)
```

### 回滚策略
```yaml
CONTENT_GENERATION → PLANNING
SCHEMA_DESIGN → CONTENT_GENERATION
DESIGN_SYSTEM → SCHEMA_DESIGN
CODE_GENERATION → SCHEMA_DESIGN
DEBUG_LOOP → CODE_GENERATION
```

---

## 共享设施

### 工具层 (Tools)
- **docms-scaffold CLI**: 项目脚手架生成
- **Git**: 版本控制
- **SQLite/PostgreSQL**: 数据库
- **Chrome DevTools MCP**: 自动化测试
- **Zhipu AI API**: 图片生成

### 记忆与知识 (Memory/KB)
- **行业模板知识库**: `tools/新西兰中小企业网站模板研究报告.md`
- **组件片段库**: 可复用的代码片段
- **提示词片段库**: 图片生成prompt库
- **模块配置**: `docms-scaffold/modules_config.yaml`

### 工件存储 (Artifacts)
```
/workspace/{site_slug}/
├── PROJECT_METADATA.json
├── REQUIREMENTS.md
├── IA_DESIGN.md
├── PAGE_BLUEPRINT.md
├── CONTENT_PLAN.md
├── ASSET_MANIFEST.md
├── DATABASE_SCHEMA.md
├── SEED_DATA_SPEC.md
├── ASSET_REPORT.md
├── TEST_REPORT.md
├── SEO_REPORT.md
├── DEPLOYMENT_GUIDE.md
├── PROJECT_SUMMARY.md
├── {project}/              # 生成的网站代码
│   ├── app/
│   ├── templates/
│   ├── migrations/
│   ├── seed_data.sql
│   └── ...
└── screenshots/            # 测试截图
```

---

## 配置文件

### settings.json 需要更新
```json
{
  "agents": {
    "architect": {
      "model": "sonnet",
      "tools": ["Read", "Grep", "Glob", "WebSearch", "WebFetch", "Write"],
      "timeout": 300
    },
    "schema_designer": {
      "model": "sonnet",
      "tools": ["Read", "Write", "Grep", "Glob"],
      "timeout": 180
    },
    "asset_maker": {
      "model": "sonnet",
      "tools": ["Read", "Write", "Bash", "WebFetch"],
      "timeout": 600
    },
    "coder": {
      "model": "sonnet",
      "tools": ["Read", "Write", "Edit", "Bash", "Grep", "Glob"],
      "timeout": 300
    },
    "tester": {
      "model": "sonnet",
      "tools": ["Bash", "Read", "Grep", "Glob"],
      "timeout": 300,
      "mcp_servers": ["chrome-devtools"]
    },
    "seo_polisher": {
      "model": "sonnet",
      "tools": ["Read", "Write", "Edit", "Grep", "Glob"],
      "timeout": 180
    }
  },
  "orchestrator": {
    "workspace_dir": "/workspace",
    "scaffold_path": "./docms-scaffold",
    "max_concurrent_agents": 1,
    "enable_rollback": true,
    "enable_retry": true
  }
}
```

---

## 优势

### 1. 清晰的职责分离
每个Agent有明确单一的职责,易于维护和扩展

### 2. 灵活的错误处理
- 关键步骤: 重试 + 回滚
- 非关键步骤: 跳过继续

### 3. 可追溯的工作流
每个阶段产生工件,便于调试和审查

### 4. 可扩展架构
- 未来可添加新Agent
- 未来可实现并行执行
- 未来可添加缓存层

### 5. 状态机管理
- 明确的状态转换
- 超时和重试控制
- 队列管理

---

## 下一步

1. ✅ 创建Orchestrator command
2. 🔄 创建7个Agent定义文件
3. 🔄 更新settings.json
4. ⏳ 测试端到端流程
5. ⏳ 编写使用文档

---

**创建日期**: 2025-11-04
**版本**: 2.2
**架构设计**: FSM-based Orchestrator + 8 Specialized Agents
