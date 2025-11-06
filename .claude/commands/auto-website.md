---
name: auto-website
description: AI自动化建站编排器 - 基于有向状态机的智能网站生成系统
agents: architect, content_manager, schema_designer, design_system, asset_maker, coder, tester, seo_polisher
---

# /auto-website - AI全自动网站生成编排系统

## 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│              Orchestrator (总控编排器)                       │
│  ・有向状态机 (FSM)                                         │
│  ・队列管理、超时控制、重试机制、回滚策略                     │
│  ・Agent调度、状态跟踪、错误处理                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────── Agent Pipeline ─────────────────────────┐
│                                                              │
│  [1] Architect         → 产品规划、IA设计、内容框架          │
│  [2] Content Manager   → 生成实际内容数据                   │
│  [3] Schema Designer   → 数据库模型设计                     │
│  [4] Design System     → 视觉设计系统（颜色、字体、风格）    │
│  [5] Asset Maker       → AI图片生成                         │
│  [6] Coder             → 代码生成、模板填充                 │
│  [7] Tester            → 功能测试、质量验证                 │
│  [8] SEO Polisher      → SEO优化、内容润色                 │
│                                                              │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────── Shared Facilities ───────────────────────┐
│  ・Tools: scaffold CLI, Git, SQLite/PG, Chrome DevTools     │
│  ・Memory: 行业模板KB、组件片段库、提示词库                  │
│  ・Artifacts: /workspace/{site_slug}/ 工件存储               │
└──────────────────────────────────────────────────────────────┘
```

---

## 使用方法

```bash
/auto-website [行业描述和网站需求]
```

### 示例

```bash
# 企业官网
/auto-website 新西兰奥克兰IT咨询公司,需要展示团队、案例、服务

# 电商网站
/auto-website 新西兰手工艺品商城,需要购物车和订单管理

# 教育网站
/auto-website Browns Bay语言学校,需要课程、教师、在线报名和视频
```

---

## 有向状态机 (FSM) 定义

### 状态节点

```yaml
states:
  INIT:
    description: 初始化,解析需求
    timeout: 60s
    next: PLANNING
    on_error: ABORT

  PLANNING:
    description: 产品规划与IA设计
    agent: architect
    timeout: 300s
    next: CONTENT_GENERATION
    on_error: RETRY(max=2) → ABORT
    artifacts:
      - REQUIREMENTS.md
      - IA_DESIGN.md
      - PAGE_BLUEPRINT.md
      - CONTENT_PLAN.md
      - ASSET_MANIFEST.md

  CONTENT_GENERATION:
    description: 生成实际内容数据
    agent: content_manager
    timeout: 240s
    next: SCHEMA_DESIGN
    on_error: RETRY(max=2) → ROLLBACK(PLANNING)
    artifacts:
      - CONTENT_DATA.json
      - CONTENT_GENERATION_REPORT.md

  SCHEMA_DESIGN:
    description: 数据库模型设计
    agent: schema_designer
    timeout: 180s
    next: DESIGN_SYSTEM
    on_error: RETRY(max=2) → ROLLBACK(CONTENT_GENERATION)
    artifacts:
      - DATABASE_SCHEMA.md
      - SEED_DATA_SPEC.md

  DESIGN_SYSTEM:
    description: 设计系统生成
    agent: design_system
    timeout: 200s
    next: ASSET_GENERATION
    on_error: RETRY(max=2) → ROLLBACK(SCHEMA_DESIGN)
    artifacts:
      - DESIGN_SYSTEM.json
      - DESIGN_TOKENS.css
      - COMPONENT_SPECS.md
      - DESIGN_REPORT.md

  ASSET_GENERATION:
    description: AI图片生成
    agent: asset_maker
    timeout: 600s
    next: CODE_GENERATION
    on_error: RETRY(max=3) → CONTINUE  # 图片失败可继续
    artifacts:
      - /templates/static/images/*
      - ASSET_REPORT.md

  CODE_GENERATION:
    description: 代码生成与数据库初始化
    agent: coder
    timeout: 300s
    next: TESTING
    on_error: RETRY(max=2) → ROLLBACK(SCHEMA_DESIGN)
    artifacts:
      - seed_data.sql
      - templates/*.html
      - templates/static/css/main.css
      - app.py
      - config.py

  TESTING:
    description: 功能测试与质量验证
    agent: tester
    timeout: 300s
    next: SEO_OPTIMIZATION
    on_error: DEBUG_LOOP(max_iterations=3)
    artifacts:
      - TEST_REPORT.md
      - screenshots/*

  DEBUG_LOOP:
    description: 测试失败修复循环
    agents: [coder, tester]
    max_iterations: 3
    timeout_per_iteration: 300s
    success → SEO_OPTIMIZATION
    failure → ROLLBACK(CODE_GENERATION)

  SEO_OPTIMIZATION:
    description: SEO优化与内容润色
    agent: seo_polisher
    timeout: 180s
    next: COMPLETED
    on_error: RETRY(max=1) → COMPLETED  # SEO非关键,可继续
    artifacts:
      - meta_tags.json
      - sitemap.xml
      - robots.txt
      - SEO_REPORT.md

  COMPLETED:
    description: 完成交付
    next: null
    artifacts:
      - PROJECT_SUMMARY.md

  ABORT:
    description: 终止流程
    reason: 记录失败原因
    artifacts:
      - ERROR_REPORT.md
```

### 状态转换规则

```python
transitions = {
    ('INIT', 'success'): 'PLANNING',
    ('INIT', 'error'): 'ABORT',

    ('PLANNING', 'success'): 'CONTENT_GENERATION',
    ('PLANNING', 'error'): 'RETRY_PLANNING',
    ('RETRY_PLANNING', 'max_retry'): 'ABORT',

    ('CONTENT_GENERATION', 'success'): 'SCHEMA_DESIGN',
    ('CONTENT_GENERATION', 'error'): 'ROLLBACK_PLANNING',

    ('SCHEMA_DESIGN', 'success'): 'DESIGN_SYSTEM',
    ('SCHEMA_DESIGN', 'error'): 'ROLLBACK_CONTENT_GENERATION',

    ('DESIGN_SYSTEM', 'success'): 'ASSET_GENERATION',
    ('DESIGN_SYSTEM', 'error'): 'ROLLBACK_SCHEMA_DESIGN',

    ('ASSET_GENERATION', 'success'): 'CODE_GENERATION',
    ('ASSET_GENERATION', 'error'): 'CODE_GENERATION',  # 非阻塞

    ('CODE_GENERATION', 'success'): 'TESTING',
    ('CODE_GENERATION', 'error'): 'ROLLBACK_SCHEMA',

    ('TESTING', 'success'): 'SEO_OPTIMIZATION',
    ('TESTING', 'error'): 'DEBUG_LOOP',
    ('DEBUG_LOOP', 'success'): 'SEO_OPTIMIZATION',
    ('DEBUG_LOOP', 'max_iterations'): 'ROLLBACK_CODE',

    ('SEO_OPTIMIZATION', 'success'): 'COMPLETED',
    ('SEO_OPTIMIZATION', 'error'): 'COMPLETED',  # 非阻塞
}
```

---

## Orchestrator 工作流程

### Phase 0: 初始化 (INIT)

```yaml
input: 用户需求描述
actions:
  1. 解析行业关键词
  2. 匹配预设方案
  3. 生成项目元数据
  4. 创建工作目录
  5. 初始化状态机

output:
  - project_slug: string
  - industry: string
  - preset: string (corporate|ecommerce|education|...)
  - company_name: string
  - workspace: /workspace/{project_slug}/
  - state_machine: FSM instance

next_state: PLANNING
timeout: 60s
```

#### 实现细节

```python
# 伪代码示例
def phase_init(user_input: str) -> Dict:
    # 1. 提取关键信息
    keywords = extract_keywords(user_input)
    industry = match_industry(keywords)
    company_name = extract_company_name(user_input) or f"{industry}-company-nz"

    # 2. 匹配预设方案
    preset = match_preset(keywords, industry)
    # 规则：
    # - "商店|电商|购物" → ecommerce
    # - "学校|培训|教育" → education
    # - "餐厅|咖啡|食品" → restaurant
    # - "医疗|诊所|牙科" → medical
    # - 默认 → corporate

    # 3. 生成项目slug
    project_slug = slugify(company_name)

    # 4. 创建workspace
    workspace = Path(f"/workspace/{project_slug}")
    workspace.mkdir(parents=True, exist_ok=True)

    # 5. 保存项目元数据
    metadata = {
        "project_slug": project_slug,
        "company_name": company_name,
        "industry": industry,
        "preset": preset,
        "user_input": user_input,
        "created_at": datetime.now().isoformat(),
        "status": "initializing"
    }

    (workspace / "PROJECT_METADATA.json").write_text(json.dumps(metadata, indent=2))

    # 6. 初始化FSM
    fsm = StateMachine(initial_state="PLANNING", workspace=workspace)

    return {
        "success": True,
        "metadata": metadata,
        "fsm": fsm,
        "next_state": "PLANNING"
    }
```

---

### Phase 1: 产品规划 (PLANNING)

```yaml
state: PLANNING
agent: architect
timeout: 300s
retry_policy:
  max_retries: 2
  backoff: exponential

input:
  - project_metadata
  - user_input
  - industry_knowledge_base

agent_tasks:
  1. 行业研究与分析
  2. 信息架构(IA)设计
  3. 页面蓝图规划
  4. 内容策略制定
  5. 资产清单列表

output_artifacts:
  - REQUIREMENTS.md: 需求文档
  - IA_DESIGN.md: 信息架构设计
  - PAGE_BLUEPRINT.md: 页面蓝图
  - CONTENT_PLAN.md: 内容计划
  - ASSET_MANIFEST.md: 资产清单(图片、文件列表)

success_criteria:
  - 所有artifacts生成
  - IA与enabled_modules一致
  - 内容计划框架完整

on_success: → CONTENT_GENERATION
on_error: → RETRY(max=2) → ABORT
```

#### Agent调用

```python
result = invoke_agent(
    agent="architect",
    input={
        "project_directory": workspace,
        "company_name": metadata["company_name"],
        "industry": metadata["industry"],
        "preset": metadata["preset"],
        "user_input": metadata["user_input"],
        "enabled_modules_file": f"{docms_scaffold}/modules_config.yaml"
    },
    timeout=300
)

if result["success"]:
    fsm.transition_to("CONTENT_GENERATION")
else:
    if fsm.retry_count < 2:
        fsm.retry("PLANNING")
    else:
        fsm.transition_to("ABORT", reason=result["error"])
```

---

### Phase 2: 内容生成 (CONTENT_GENERATION)

```yaml
state: CONTENT_GENERATION
agent: content_manager
timeout: 240s
retry_policy:
  max_retries: 2
  on_max_retry: ROLLBACK(PLANNING)

input:
  - CONTENT_PLAN.md
  - IA_DESIGN.md
  - PAGE_BLUEPRINT.md
  - REQUIREMENTS.md
  - PROJECT_METADATA.json

agent_tasks:
  1. 解析内容需求（数量、类型）
  2. 生成公司信息内容
  3. 生成产品/服务内容
  4. 生成团队成员内容
  5. 生成文章/博客内容
  6. 生成评价、FAQ、案例等
  7. 确保新西兰本地化
  8. 输出结构化JSON数据

output_artifacts:
  - CONTENT_DATA.json: 完整的结构化内容数据
  - CONTENT_GENERATION_REPORT.md: 内容生成报告

success_criteria:
  - CONTENT_DATA.json 包含所有required字段
  - 内容数量符合 CONTENT_PLAN 要求
  - 文本质量高、专业、无错误
  - 新西兰本地化准确
  - 所有图片包含清晰的 image_prompt

on_success: → SCHEMA_DESIGN
on_error: → ROLLBACK(PLANNING)
```

#### Agent调用

```python
result = invoke_agent(
    agent="content_manager",
    input={
        "project_directory": workspace,
        "content_plan": workspace / "CONTENT_PLAN.md",
        "ia_design": workspace / "IA_DESIGN.md",
        "page_blueprint": workspace / "PAGE_BLUEPRINT.md",
        "requirements": workspace / "REQUIREMENTS.md",
        "metadata": workspace / "PROJECT_METADATA.json"
    },
    timeout=240
)

if result["success"]:
    fsm.transition_to("SCHEMA_DESIGN")
else:
    if fsm.retry_count < 2:
        fsm.retry("CONTENT_GENERATION")
    else:
        fsm.rollback("PLANNING")
```

---

### Phase 3: 数据库模型设计 (SCHEMA_DESIGN)

```yaml
state: SCHEMA_DESIGN
agent: schema_designer
timeout: 180s
retry_policy:
  max_retries: 2
  on_max_retry: ROLLBACK(CONTENT_GENERATION)

input:
  - IA_DESIGN.md
  - CONTENT_DATA.json
  - enabled_modules.txt
  - modules_config.yaml

agent_tasks:
  1. 读取enabled modules
  2. 分析IA确定数据实体
  3. 设计数据库schema
  4. 规划外键关系
  5. 设计seed data结构

output_artifacts:
  - DATABASE_SCHEMA.md: 完整schema设计
  - SEED_DATA_SPEC.md: seed数据规格
  - db_tables.json: 机器可读的表结构

success_criteria:
  - schema只包含enabled模块的表
  - 外键关系正确
  - seed data规格完整

on_success: → DESIGN_SYSTEM
on_error: → RETRY(max=2) → ROLLBACK(CONTENT_GENERATION)
```

---

### Phase 4: 设计系统 (DESIGN_SYSTEM)

```yaml
state: DESIGN_SYSTEM
agent: design_system
timeout: 200s
retry_policy:
  max_retries: 2
  on_max_retry: ROLLBACK(SCHEMA_DESIGN)

input:
  - CONTENT_DATA.json
  - REQUIREMENTS.md
  - IA_DESIGN.md
  - PROJECT_METADATA.json

agent_tasks:
  1. 行业风格研究
  2. 确定颜色调色板（primary/secondary/neutral）
  3. 设计字体系统（字号、行高、字重）
  4. 定义间距系统（基于8px grid）
  5. 设计组件样式规范
  6. 生成CSS设计令牌
  7. 输出设计系统JSON和文档

output_artifacts:
  - DESIGN_SYSTEM.json: 完整设计系统规范
  - DESIGN_TOKENS.css: CSS变量定义
  - COMPONENT_SPECS.md: 组件设计规范
  - DESIGN_REPORT.md: 设计决策说明

success_criteria:
  - 颜色系统完整（primary/secondary/neutral）
  - 字体系统包含所有必要规格
  - 间距系统基于一致的scale
  - 符合WCAG AA无障碍标准
  - 设计风格匹配行业特点

on_success: → ASSET_GENERATION
on_error: → ROLLBACK(SCHEMA_DESIGN)
```

---

### Phase 5: 静态资源生成 (ASSET_GENERATION)

```yaml
state: ASSET_GENERATION
agent: asset_maker
timeout: 600s
retry_policy:
  max_retries: 3
  non_blocking: true  # 图片生成失败不阻塞流程

input:
  - ASSET_MANIFEST.md
  - CONTENT_DATA.json
  - DESIGN_SYSTEM.json

agent_tasks:
  1. 解析ASSET_MANIFEST获取图片列表
  2. 从CONTENT_DATA.json提取image_prompt
  3. 从DESIGN_SYSTEM.json获取颜色和风格指导
  2. 按优先级排序(High → Medium → Low)
  3. 调用Zhipu AI CogView-3生成图片
  4. 下载并保存到templates/static/images/
  5. 生成asset report

output_artifacts:
  - templates/static/images/*.jpg: 所有生成的图片
  - ASSET_REPORT.md: 生成报告(成功/失败列表)

success_criteria:
  - >= 80% High优先级图片成功生成
  - 所有图片保存到正确路径

on_success: → CODE_GENERATION
on_error: → CONTINUE  # 部分失败仍然继续
```

#### 非阻塞错误处理

```python
result = invoke_agent("asset_maker", input_data, timeout=600)

if result["success_rate"] >= 0.8:  # 80%成功
    fsm.transition_to("CODE_GENERATION")
else:
    if fsm.retry_count < 3:
        fsm.retry("ASSET_GENERATION", partial_retry=True)
    else:
        # 即使失败也继续(使用占位图)
        log_warning("Asset generation partially failed, using placeholders")
        fsm.transition_to("CODE_GENERATION")
```

---

### Phase 6: 代码生成 (CODE_GENERATION)

```yaml
state: CODE_GENERATION
agent: coder
timeout: 300s
retry_policy:
  max_retries: 2
  on_max_retry: ROLLBACK(SCHEMA_DESIGN)

input:
  - DATABASE_SCHEMA.md
  - SEED_DATA_SPEC.md
  - CONTENT_DATA.json
  - DESIGN_SYSTEM.json
  - DESIGN_TOKENS.css
  - enabled_modules.txt
  - ASSET_REPORT.md

agent_tasks:
  1. 调用docms-scaffold CLI生成项目骨架
  2. 从CONTENT_DATA.json生成modular seed_data.sql
  3. 使用DESIGN_TOKENS.css生成样式
  3. 创建Jinja2模板(只针对enabled模块)
  4. 生成CSS样式
  5. 创建app.py和config.py
  6. 初始化数据库
  7. 启动dev server

output_artifacts:
  - {project}/: 完整项目代码
  - seed_data.sql: 模块化SQL
  - templates/*.html: 模板文件
  - app.py, config.py: 应用文件

success_criteria:
  - scaffold生成成功
  - 数据库初始化成功
  - 服务器启动成功(http://localhost:8000)

on_success: → TESTING
on_error: → RETRY(max=2) → ROLLBACK(SCHEMA_DESIGN)
```

---

### Phase 7: 测试验证 (TESTING)

```yaml
state: TESTING
agent: tester
timeout: 300s
retry_policy:
  on_error: DEBUG_LOOP(max_iterations=3)

input:
  - project_directory
  - website_url: http://localhost:8000
  - REQUIREMENTS.md
  - ASSET_MANIFEST.md

agent_tasks:
  1. 使用Chrome DevTools MCP打开网站
  2. 测试所有页面可访问
  3. 验证所有图片加载(无404)
  4. 验证所有链接正常(无死链)
  5. 测试移动端响应式
  6. 检查JS console错误
  7. 测试表单渲染

output_artifacts:
  - TEST_REPORT.md: 详细测试报告
  - screenshots/*.png: 测试截图

success_criteria:
  - 100% 核心页面可访问
  - >= 95% 图片加载成功
  - 无死链
  - 移动端响应正常

on_success: → SEO_OPTIMIZATION
on_error: → DEBUG_LOOP
```

#### Debug Loop (测试失败修复循环)

```yaml
state: DEBUG_LOOP
max_iterations: 3
current_iteration: 0

loop:
  1. 分析TEST_REPORT.md中的失败项
  2. 调用coder agent修复
  3. 调用tester agent重新测试
  4. 如果测试通过: → SEO_OPTIMIZATION
  5. 如果仍失败 AND iteration < 3: 继续循环
  6. 如果iteration >= 3: → ROLLBACK(CODE_GENERATION)
```

```python
def debug_loop(fsm, test_report, max_iterations=3):
    iteration = 0

    while iteration < max_iterations:
        iteration += 1

        # 1. coder修复
        fix_result = invoke_agent(
            agent="coder",
            mode="debug",
            input={
                "test_report": test_report,
                "project_directory": workspace,
                "fix_instructions": extract_failures(test_report)
            },
            timeout=300
        )

        if not fix_result["success"]:
            continue

        # 2. 重新测试
        retest_result = invoke_agent(
            agent="tester",
            input={"project_directory": workspace},
            timeout=300
        )

        if retest_result["all_tests_passed"]:
            return fsm.transition_to("SEO_OPTIMIZATION")

        test_report = retest_result["report"]

    # 超过最大迭代次数
    return fsm.transition_to("ROLLBACK", target="CODE_GENERATION")
```

---

### Phase 8: SEO优化 (SEO_OPTIMIZATION)

```yaml
state: SEO_OPTIMIZATION
agent: seo_polisher
timeout: 180s
retry_policy:
  max_retries: 1
  non_blocking: true  # SEO失败不阻塞

input:
  - project_directory
  - CONTENT_DATA.json
  - templates/*.html

agent_tasks:
  1. 为所有页面添加meta tags
  2. 生成sitemap.xml
  3. 生成robots.txt
  4. 添加schema.org结构化数据
  5. 添加Open Graph tags
  6. 生成favicon
  7. 检查无障碍性(WCAG AA)

output_artifacts:
  - meta_tags.json: meta tags配置
  - sitemap.xml: 站点地图
  - robots.txt: 爬虫规则
  - favicon.ico: 网站图标
  - SEO_REPORT.md: SEO优化报告

success_criteria:
  - 所有页面有meta description
  - sitemap.xml正确生成
  - robots.txt配置正确

on_success: → COMPLETED
on_error: → COMPLETED  # 非关键,可继续
```

---

### Phase 9: 完成交付 (COMPLETED)

```yaml
state: COMPLETED

final_actions:
  1. 汇总所有artifacts
  2. 生成PROJECT_SUMMARY.md
  3. 计算统计数据
  4. 展示交付报告

output_artifacts:
  - PROJECT_SUMMARY.md: 项目总结

display:
  - 项目统计
  - 生成文件列表
  - 访问链接
  - 下一步建议
```

#### 交付报告

```markdown
🎉 网站自动生成完成!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 项目统计
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 项目名称: {project_slug}
✅ 行业类型: {industry}
✅ 预设方案: {preset} ({N}个模块)
✅ 页面数量: {pages}
✅ 数据记录: {records}
✅ AI生成图片: {images}
✅ 总耗时: {duration}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📂 工件清单
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] 规划文档: ✅
    - REQUIREMENTS.md
    - IA_DESIGN.md
    - CONTENT_PLAN.md

[2] 技术设计: ✅
    - DATABASE_SCHEMA.md
    - SEED_DATA_SPEC.md

[3] 静态资源: ✅
    - {N}张图片
    - ASSET_REPORT.md

[4] 源代码: ✅
    - {M}个模板文件
    - seed_data.sql
    - app.py, config.py

[5] 测试报告: ✅
    - TEST_REPORT.md
    - {X}个截图

[6] SEO优化: ✅
    - sitemap.xml
    - robots.txt
    - SEO_REPORT.md

[7] 部署文档: ✅
    - DEPLOYMENT_GUIDE.md
    - docker-compose.yml
    - .env.template

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 访问信息
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
本地开发: http://localhost:8000
项目目录: /workspace/{project_slug}/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 下一步
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 访问网站并测试所有功能
2. 根据需要调整内容和样式
3. 阅读DEPLOYMENT_GUIDE.md准备部署
4. 配置域名和SSL证书
5. 部署到生产环境

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 提示
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
所有文档和代码都在 /workspace/{project_slug}/ 中
详细的部署指南请参考 DEPLOYMENT_GUIDE.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 错误处理与恢复

### 超时处理

```python
def handle_timeout(state, timeout_duration):
    log_error(f"State {state} timed out after {timeout_duration}s")

    if state in ["ASSET_GENERATION", "SEO_OPTIMIZATION"]:
        # 非关键状态,继续下一步
        return fsm.transition_to(next_state)
    else:
        # 关键状态,重试
        if fsm.retry_count < max_retries:
            return fsm.retry(state)
        else:
            return fsm.transition_to("ABORT")
```

### 回滚策略

```python
rollback_map = {
    "SCHEMA_DESIGN": "PLANNING",
    "CODE_GENERATION": "SCHEMA_DESIGN",
    "DEBUG_LOOP": "CODE_GENERATION"
}

def rollback(current_state):
    target_state = rollback_map.get(current_state)
    if target_state:
        log_info(f"Rolling back from {current_state} to {target_state}")
        # 清理当前状态的artifacts
        cleanup_artifacts(current_state)
        # 转换到目标状态
        return fsm.transition_to(target_state)
    else:
        return fsm.transition_to("ABORT")
```

### 重试机制

```python
class RetryPolicy:
    def __init__(self, max_retries=2, backoff="exponential"):
        self.max_retries = max_retries
        self.backoff = backoff
        self.attempt = 0

    def should_retry(self):
        return self.attempt < self.max_retries

    def wait_time(self):
        if self.backoff == "exponential":
            return 2 ** self.attempt  # 1s, 2s, 4s, 8s...
        elif self.backoff == "linear":
            return self.attempt * 2  # 2s, 4s, 6s...
        else:
            return 1  # constant

    def retry(self, func, *args, **kwargs):
        self.attempt += 1
        if not self.should_retry():
            raise MaxRetryExceeded()

        time.sleep(self.wait_time())
        return func(*args, **kwargs)
```

---

## 队列管理

```python
class OrchestratorQueue:
    def __init__(self):
        self.queue = []
        self.current_task = None
        self.completed = []
        self.failed = []

    def enqueue(self, task):
        self.queue.append(task)

    def dequeue(self):
        if self.queue:
            self.current_task = self.queue.pop(0)
            return self.current_task
        return None

    def mark_completed(self, task):
        self.completed.append(task)
        self.current_task = None

    def mark_failed(self, task, reason):
        task.failure_reason = reason
        self.failed.append(task)
        self.current_task = None
```

---

## 环境要求

### 必需工具
- Python 3.8+
- docms-scaffold CLI
- Chrome DevTools MCP
- Git

### API Keys
- ZHIPU_API_KEY: 智谱AI API密钥(图片生成)

### 环境变量
```bash
export ZHIPU_API_KEY="your-api-key"
export WORKSPACE_DIR="/workspace"
export DOCMS_SCAFFOLD_PATH="/path/to/docms-scaffold"
```

---

## 配置选项

### 预设方案
- **corporate**: 企业官网(10模块)
- **ecommerce**: 电商网站(12模块)
- **education**: 教育培训(13模块)
- **restaurant**: 餐厅(9模块)
- **medical**: 医疗诊所(11模块)
- **service**: 专业服务(11模块)
- **minimal**: 最小配置(4模块)
- **full**: 完整配置(24模块)

### 超时配置
```yaml
timeouts:
  PLANNING: 300s
  SCHEMA_DESIGN: 180s
  ASSET_GENERATION: 600s
  CODE_GENERATION: 300s
  TESTING: 300s
  DEBUG_LOOP: 300s per iteration
  SEO_OPTIMIZATION: 180s
```

### 重试配置
```yaml
retry_policies:
  PLANNING: {max: 2, backoff: exponential}
  SCHEMA_DESIGN: {max: 2, backoff: exponential}
  ASSET_GENERATION: {max: 3, backoff: linear, non_blocking: true}
  CODE_GENERATION: {max: 2, backoff: exponential}
  DEBUG_LOOP: {max_iterations: 3}
  SEO_OPTIMIZATION: {max: 1, non_blocking: true}
```

---

## 最佳实践

### 1. 提供详细需求
✅ "新西兰奥克兰IT咨询公司,专注云计算和网络安全,需要展示5个服务、8位团队成员、6个案例"
❌ "做一个公司网站"

### 2. 明确特殊功能
如果需要特定功能,明确提出:
- "需要在线预约系统"
- "需要会员注册登录"
- "需要视频教程展示"

### 3. 监控状态机
系统会实时输出当前状态:
```
[Orchestrator] State: PLANNING (1/8)
[Orchestrator] Agent: architect
[Orchestrator] Timeout: 300s
[Orchestrator] Progress: ████░░░░ 40%
```

### 4. 查看中间产物
每个阶段的artifacts都保存在workspace中,可随时查看

---

## 故障排除

### 问题1: Agent超时
**原因**: 网络慢或任务复杂
**解决**: 自动重试,或增加timeout配置

### 问题2: 图片生成失败
**原因**: API限流或网络问题
**解决**: 部分失败不阻塞,使用占位图

### 问题3: 测试失败循环
**原因**: 代码问题导致反复失败
**解决**: 最多3次debug循环,超过则回滚

### 问题4: 数据库初始化失败
**原因**: SQL语法错误或外键问题
**解决**: 回滚到SCHEMA_DESIGN重新生成

---

## 性能优化

### 并行执行(未来版本)
```yaml
# 部分非依赖stages可并行
parallel_stages:
  - [ASSET_GENERATION, SCHEMA_DESIGN]  # 未来可能并行
```

### 缓存机制(未来版本)
```yaml
cache:
  - industry_research: 缓存行业研究结果
  - image_prompts: 缓存相似的图片prompt
  - module_templates: 缓存常用模块模板
```

---

END OF ORCHESTRATOR COMMAND
