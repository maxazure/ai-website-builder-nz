# Bowen Education Group Website Requirements

## 用户输入

博文集团（Bowen Group）位于英国曼彻斯特的教育集团网站

**核心定位**: 面向家长/学生/合作方的"品牌与合作窗口"

**主要功能需求**:
1. 集团实力与新闻展示（与英国政府、国内高校合作）
2. 中文学校与补习中心的课程体系（不走线上招生，仅咨询）
3. 国际象棋/羽毛球俱乐部的比赛/课程/相册
4. 政府项目（HAF、公园活动等）成果展示
5. 活动系统（中国新年、进校园、寻根之旅、Easter访华）
6. 表单系统（咨询、报名、意向登记）
7. 图集系统（活动照片、俱乐部照片）

## 行业分析

- **识别行业**: 教育培训（Education & Training）
- **地点**: Manchester, UK
- **业务类型**: 综合教育集团（中文学校 + 补习中心 + 俱乐部 + 文化推广）
- **预设方案**: education
- **额外需求**:
  - 活动系统 (event) ✓ 已包含在 education 预设
  - 图集系统 (gallery) ✓ 需要添加
  - 表单系统 (contact) ✓ 基础模块已包含
  - 新闻博客 (post) ✓ 已包含在 education 预设
  - 团队展示 (team) ✓ 已包含在 education 预设
  - 课程展示 (product 作为课程) ✓ 已包含在 education 预设
  - 文件下载 (file_download) ✓ 已包含在 education 预设

## 最终模块方案

### 预设: education

**基础模块** (education 预设):
- `post` - 博文新闻、政府项目报道
- `team` - 教师团队、管理团队
- `product` - 课程展示（中文学校课程、补习课程、俱乐部课程）
- `faq` - 常见问题
- `user` - 用户系统（可选，暂不启用）
- `booking` - 在线咨询预约
- `event` - 活动系统（比赛、文化活动、寻根之旅等）
- `video` - 教学视频、活动视频
- `file_download` - 资料下载、课程表、赛程等

**额外添加模块**:
- `gallery` - 图片画廊（俱乐部照片、活动照片）
- `comment` - 评论系统（可选）
- `newsletter` - 邮件订阅（可选）

### 总模块数: 11 个核心模块

## 项目信息

- **项目名称**: bowen-education-manchester
- **项目路径**: /home/maxazure/projects/ai-website-builder-nz/workspace/bowen-education-manchester
- **公司名称**: Bowen Education Group / 博文集团
- **公司英文名**: Bowen Group
- **地址**: 1/F, 2A Curzon Road, Sale, Manchester, M33 7DR
- **电话**: (0044) 0161-6672668
- **邮箱**: info@boweneducation.org
- **参考网站**: https://www.boweneducation.org/about-us/

## 核心栏目规划

### 1. 首页 (Home)
- Hero 轮播（政府项目、重要活动、合作背书）
- 集团简介区块
- 课程概览卡片
- 俱乐部入口
- 最新新闻/活动
- 合作伙伴 Logo 带
- 联系表单与地图

### 2. 博文集团 (About)
- 集团发展历程
- 理念："中西融汇，博学致远"
- 管理团队
- 合作单位

### 3. 博文新闻 (News/Post)
- 新闻列表（活动报道、合作签约、媒体报道）
- 新闻详情页

### 4. 中文学校 (Chinese School)
- 学校简介 (team 模块展示教师)
- 课程设置 (product 模块)
  - 启蒙班
  - 中级班
  - 精英班
  - GCSE 普通话
  - 粤语课程
- 中英文兴趣班 (product 模块)
- 学期日期（单页）
- 报名咨询 (booking 模块)
- PTA 家长教师协会（单页）

### 5. 补习中心 (Tuition Centre)
- 课程介绍 (product 模块)
  - GCSE 数学、物理、化学、英语
  - A-Level 课程

### 6. 国际象棋俱乐部 (Chess Club)
- 俱乐部介绍
- 我们的比赛 (event 模块)
- Information for Players (外链到 ECF)
- 相册 (gallery 模块)

### 7. 羽毛球俱乐部 (Badminton Club)
- 俱乐部介绍
- 赛事 (event 模块)
- 训练时间表（单页）
- 精彩瞬间 (gallery 模块)

### 8. 政府项目 (Government Programmes)
- HAF 项目 (post 模块作为项目报道)
- 公园活动 (post 模块)

### 9. 博文活动 (Events)
- 中国新年庆典 (event 模块)
- 中国文化进校园 (event 模块)
- 寻根之旅 (event 模块)
- 河南大学合作（单页）
- Easter 访华计划 (event 模块)

### 10. 联系我们 (Contact)
- 联系表单 (contact 模块)
- 地图
- 联系信息

## 核心 KPI

- 合作线索（邮箱/表单提交）≥ 每月 10 条
- 俱乐部报名/咨询转化 ≥ 每月 20 次
- 活动页访问量 ≥ 每月 500 PV
- 关键词覆盖：Manchester Chinese School, Mandarin Classes, HSK/YCT, ECF chess club, Badminton club Manchester

## 特殊需求

1. **表单系统**: 咨询/赛事报名/意向登记（含 GDPR 合规）
2. **活动系统**: 列表、分类、过去/未来筛选、iCal 下载
3. **图集系统**: 灯箱预览、按活动关联
4. **多语言**: 中英文切换（Phase 2 手动添加）
5. **Schema.org**: Organization, School, Course, Event, NewsArticle
6. **SEO**: 自定义标题/描述/OG 图
7. **隐私合规**: GDPR、Cookie Banner、隐私政策
8. **性能**: LCP ≤ 2.5s、CLS ≤ 0.1、无障碍性
9. **分析**: GA4 + 事件追踪

## URL 规范

- `/` - 首页
- `/about/` - 博文集团
- `/news/` - 博文新闻列表
- `/news/{slug}/` - 新闻详情
- `/school/` - 中文学校
- `/school/curriculum/` - 课程设置
- `/school/term-dates/` - 学期日期
- `/school/pta/` - PTA
- `/tuition/` - 补习中心
- `/chess/` - 国际象棋俱乐部
- `/chess/events/` - 比赛列表
- `/badminton/` - 羽毛球俱乐部
- `/badminton/schedule/` - 训练时间表
- `/badminton/gallery/` - 精彩瞬间
- `/programmes/` - 政府项目
- `/programmes/haf/` - HAF 项目
- `/programmes/parks/` - 公园活动
- `/events/` - 博文活动
- `/events/{slug}/` - 活动详情
- `/contact/` - 联系我们

## Phase 1 使用的预设

**预设**: education
**命令**: `python create_project_modular.py bowen-education-manchester --preset education`

生成后将包含以下模块：
- post
- team
- product
- faq
- user (可选暂不启用)
- booking
- event
- video
- file_download

**Phase 2 需手动添加**:
- gallery 模块
- 复杂的 URL 路由结构
- 多语言支持
- GDPR 合规功能
- Schema.org 标记
