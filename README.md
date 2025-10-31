# Docms NZ - AI自动化建站项目

这是一个基于Claude Code的双工作流自动化系统,包含:
1. **AI自动化建站系统** - 专为新西兰中小企业网站设计
2. **TDD自动开发工作流** - 通用的测试驱动开发自动化

## 🎯 项目简介

### AI自动化建站系统 (`/auto-website`)

根据行业提示词自动生成完整的专业网站,包括:
- ✅ 自动规划网站结构和内容
- ✅ AI生成所有网站图片(智谱AI)
- ✅ 自动开发数据库和模板
- ✅ 自动测试所有功能
- ✅ 15-30分钟完成整个网站

**适用于**: 新西兰中小企业快速建站

### TDD自动开发工作流 (`/auto-dev`)

自动化的测试驱动开发流程:
- ✅ 自动规划和实现
- ✅ TDD方法论(测试先行)
- ✅ 自动运行测试
- ✅ 自动调试和修复
- ✅ 2-10分钟完成功能开发

**适用于**: 通用软件功能开发

## 🚀 快速开始

### 前置要求

- Claude Code CLI 已安装
- Python 3.8+ 环境
- (可选) 智谱AI API密钥(用于网站图片生成)
- (可选) Chrome DevTools MCP(用于网站测试)

### 使用AI自动化建站

```bash
# 1. 配置API密钥(首次使用)
cp .claude/config/zhipu_api_key.txt.example .claude/config/zhipu_api_key.txt
# 编辑文件填入API密钥

# 2. 启动Claude Code
cd D:/projects/docmsnz
claude

# 3. 运行自动化建站
/auto-website 为新西兰的温室设备供应公司GreenHouse NZ建立网站

# 4. 等待完成(15-30分钟)
# 网站将自动生成在: D:/projects/docmsnz/{网站目录名}/
```

**详细文档**: [AI自动化建站使用指南](.claude/AI_WEBSITE_AUTOMATION_GUIDE.md)

### 使用TDD自动开发

```bash
# 1. 启动Claude Code
claude

# 2. 运行自动开发
/auto-dev 创建一个井字棋游戏,使用HTML/CSS/JavaScript

# 3. 等待完成(2-10分钟)
# 代码将自动生成并通过测试
```

**详细文档**: [TDD工作流文档](.claude/README.md)

## 📁 项目结构

```
docmsnz/
├── .claude/                           # Claude Code配置
│   ├── agents/                        # Agent配置
│   │   ├── planner.md                # TDD规划agent
│   │   ├── developer.md              # TDD开发agent
│   │   ├── tester.md                 # TDD测试agent
│   │   ├── debugger.md               # TDD调试agent
│   │   ├── website_planner.md        # 网站规划agent
│   │   ├── website_developer.md      # 网站开发agent
│   │   └── website_tester.md         # 网站测试agent
│   │
│   ├── commands/                      # Slash命令
│   │   ├── auto-dev.md               # TDD工作流命令
│   │   └── auto-website.md           # 建站工作流命令
│   │
│   ├── hooks/                         # Hook协调器
│   │   ├── workflow_dm.py            # TDD工作流DM
│   │   ├── website_dm.py             # 建站工作流DM
│   │   └── test_checker.py           # 测试检查器
│   │
│   ├── config/                        # 配置文件
│   │   ├── zhipu_api_key.txt.example # API密钥示例
│   │   └── README.md                 # 配置说明
│   │
│   ├── README.md                      # Claude Code系统说明
│   ├── QUICKSTART.md                  # 快速开始
│   ├── ARCHITECTURE.md                # TDD架构V1
│   ├── ARCHITECTURE_V2.md             # TDD架构V2
│   ├── AI_WEBSITE_AUTOMATION_GUIDE.md # 建站系统完整指南
│   └── settings.json                  # Hook配置
│
├── docms-scaffold/                    # Python Flask CMS框架
│   ├── cli/                           # CLI工具
│   │   ├── create_site.py            # 创建网站命令
│   │   └── generate_content.py       # 内容生成工具
│   ├── app/                           # 应用核心
│   ├── docms/                         # CMS引擎
│   └── README.md                      # CMS文档
│
├── 新西兰中小企业网站模板研究报告.md    # 300+行业研究
├── .gitignore                         # Git忽略规则
└── README.md                          # 本文件
```

## 📊 两个系统对比

| 特性 | AI自动化建站 | TDD自动开发 |
|------|-------------|------------|
| **命令** | `/auto-website` | `/auto-dev` |
| **用途** | 新西兰中小企业网站 | 通用软件功能 |
| **方法论** | 内容驱动 | TDD测试驱动 |
| **输出** | 完整网站 | 功能代码 |
| **时间** | 15-30分钟 | 2-10分钟 |
| **图片** | AI生成 | 无 |
| **测试** | 功能测试(MCP) | 单元测试 |
| **成本** | ~$1.50-$2.00 | ~$0.75-$3.00 |

## 🎨 生成的网站示例

使用 `/auto-website` 命令可以生成包含以下功能的完整网站:

- ✅ 响应式首页(Hero, 产品, 文章)
- ✅ 产品/服务展示(列表+详情)
- ✅ 新闻/博客功能
- ✅ 关于我们页面
- ✅ 联系表单
- ✅ 5-10个产品,完整内容
- ✅ 6-10篇文章,完整内容
- ✅ 15-20张AI生成的专业图片
- ✅ 移动端适配
- ✅ SEO优化

**技术栈**: FastAPI + SQLAlchemy + Jinja2 + SQLite

## 💰 成本估算

### AI自动化建站
- **智谱AI图片**: ¥1.50-¥2.00 (15-20张 × ¥0.10)
- **Claude API**: $0.50-$1.00 (50K-80K tokens)
- **总成本**: 约 $1.50-$2.00 或 ¥10-¥15

### TDD自动开发
- **Claude API**: $0.75-$3.00 (25K-100K tokens)
- **取决于**: 功能复杂度和调试次数

## 📚 文档索引

### AI自动化建站系统
- **完整指南**: [.claude/AI_WEBSITE_AUTOMATION_GUIDE.md](.claude/AI_WEBSITE_AUTOMATION_GUIDE.md)
- **API配置**: [.claude/config/README.md](.claude/config/README.md)
- **行业研究**: [新西兰中小企业网站模板研究报告.md](新西兰中小企业网站模板研究报告.md)
- **CMS文档**: [docms-scaffold/README.md](docms-scaffold/README.md)

### TDD自动开发工作流
- **系统说明**: [.claude/README.md](.claude/README.md)
- **快速开始**: [.claude/QUICKSTART.md](.claude/QUICKSTART.md)
- **架构V1**: [.claude/ARCHITECTURE.md](.claude/ARCHITECTURE.md)
- **架构V2**: [.claude/ARCHITECTURE_V2.md](.claude/ARCHITECTURE_V2.md)

## 🔧 配置说明

### 智谱AI API配置(建站系统需要)

```bash
# 1. 复制示例文件
cp .claude/config/zhipu_api_key.txt.example .claude/config/zhipu_api_key.txt

# 2. 获取API密钥
# 访问: https://open.bigmodel.cn/
# 注册并获取API密钥

# 3. 编辑文件填入密钥
notepad .claude/config/zhipu_api_key.txt
```

### Hook配置

所有Hook已在 `.claude/settings.json` 中配置好,无需额外设置。

## 🛠️ 开发和定制

### 修改Agent行为

编辑对应的agent配置文件:
- TDD工作流: `.claude/agents/planner.md`, `developer.md`, `tester.md`, `debugger.md`
- 建站工作流: `.claude/agents/website_planner.md`, `website_developer.md`, `website_tester.md`

### 修改Hook逻辑

编辑hook脚本:
- TDD工作流: `.claude/hooks/workflow_dm.py`
- 建站工作流: `.claude/hooks/website_dm.py`

### 添加新的行业

编辑 `新西兰中小企业网站模板研究报告.md` 添加新的行业分类和参考资料。

## 🐛 故障排除

### 建站系统问题

| 问题 | 解决方案 |
|------|---------|
| API密钥无效 | 检查 `.claude/config/zhipu_api_key.txt` |
| 图片生成失败 | 验证API余额,检查网络连接 |
| 服务器无法启动 | 运行 `pip install -r requirements.txt` |
| 测试一直失败 | 查看 `.claude/workflow/TODOS.md` 的错误详情 |

### TDD工作流问题

| 问题 | 解决方案 |
|------|---------|
| Hook不工作 | 检查 `python --version` 是否可用 |
| 工作流卡住 | 查看最后输出,手动执行下一步 |
| 测试循环不停 | 查看调试分析,可能需要人工干预 |

详细故障排除请参考各自的文档。

## 🌟 特色功能

### 新西兰本地化
- 基于300+新西兰行业研究
- 符合新西兰企业网站特点
- 本地化的内容和设计风格
- NZ域名支持

### 完全自动化
- 无需人工干预
- 自动规划、开发、测试
- 自动修复问题(最多5次)
- 自动生成报告

### 高质量输出
- 专业的内容(非Lorem Ipsum)
- AI生成的高质量图片
- TDD保证的代码质量
- 通过测试的功能

## 📈 路线图

### 即将推出
- [ ] 支持更多图片生成服务(DALL-E, Midjourney)
- [ ] 多语言网站支持
- [ ] 网站管理后台
- [ ] 在线支付集成
- [ ] SEO工具集成
- [ ] 性能监控

### 长期计划
- [ ] 更多国家/地区的行业模板
- [ ] 自定义设计系统
- [ ] AI内容管理
- [ ] 多站点管理

## 🤝 贡献

欢迎贡献:
- 报告bug和问题
- 建议新功能
- 贡献行业研究
- 优化agent配置
- 改进文档

## 📄 许可

MIT License - 自由使用、修改和分发

## 🆘 获取帮助

1. 查看相关文档([建站指南](.claude/AI_WEBSITE_AUTOMATION_GUIDE.md) 或 [TDD文档](.claude/README.md))
2. 检查故障排除部分
3. 在Claude Code中直接提问
4. 提交Issue到项目仓库

---

**开始使用:**

```bash
# 建站
/auto-website 为新西兰咖啡馆建立网站

# 开发
/auto-dev 创建一个待办事项列表应用
```

**享受AI自动化的开发体验! 🚀**
