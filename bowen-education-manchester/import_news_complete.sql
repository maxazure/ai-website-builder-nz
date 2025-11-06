-- Import 4 news articles
-- 导入4篇新闻

-- Article 1: Henan University Partnership
INSERT OR IGNORE INTO post (
    column_id, title, slug, summary, content_html, 
    status, is_recommended, published_at, 
    seo_title, seo_description, created_at, updated_at
) VALUES (
    8,
    '博文集团与河南大学建立战略合作伙伴关系',
    'henan-university-partnership',
    '博文教育集团正式与中国河南大学签署战略合作协议，共同推进中英教育文化交流项目，为曼彻斯特华裔青少年提供寻根之旅机会。',
    '<h2>合作背景</h2><p>2024年3月，博文教育集团与河南大学在郑州正式签署战略合作协议。此次合作标志着博文集团在推动中英教育文化交流方面迈出了重要一步。河南大学作为中国百年名校，在汉语国际教育和文化传播领域具有深厚的学术积淀和丰富的教学资源。</p><h2>合作内容</h2><p>本次战略合作涵盖多个领域：</p><ul><li><strong>师资交流项目</strong>：河南大学将定期派遣优秀汉语教师来曼彻斯特进行短期教学交流。</li><li><strong>学生交流计划</strong>：每年组织博文学校学生赴河南大学参加短期文化体验营。</li><li><strong>课程资源共享</strong>：河南大学将向博文集团提供优质的教学资源。</li><li><strong>学术研究合作</strong>：双方将在海外华文教育研究领域开展合作。</li></ul><h2>寻根之旅</h2><p>作为合作的重要组成部分，博文集团每年将组织"寻根之旅"活动。</p><h2>报名咨询</h2><p>邮箱：china-trip@boweneducation.org<br>电话：0161 xxx xxxx</p>',
    'published',
    0,
    '2024-03-15 10:00:00',
    '博文集团与河南大学建立战略合作伙伴关系',
    '博文教育集团正式与中国河南大学签署战略合作协议，共同推进中英教育文化交流项目。',
    datetime('now'),
    datetime('now')
);

-- Article 2: Autumn Term Enrollment
INSERT OR IGNORE INTO post (
    column_id, title, slug, summary, content_html,
    status, is_recommended, published_at,
    seo_title, seo_description, created_at, updated_at
) VALUES (
    8,
    '2024年秋季学期招生现已开放',
    '2024-autumn-term-enrollment',
    '博文中文学校2024年秋季学期招生全面启动，提供从基础班到A-Level的全方位中文课程，GCSE通过率保持100%。新生可享受首月学费九折优惠。',
    '<h2>招生公告</h2><p>博文中文学校2024年秋季学期招生现已全面启动！作为曼彻斯特地区领先的中文教育机构，我们致力于为5-18岁的学生提供高质量的中文教育。</p><h2>课程设置</h2><h3>1. 基础中文班（5-7岁）</h3><ul><li>上课时间：每周六 10:00-11:00</li><li>学费：£180/学期（12周）</li><li>班级人数：8-12人小班教学</li></ul><h3>2. GCSE中文班（14-16岁）</h3><ul><li>上课时间：每周六 14:00-16:00</li><li>学费：£360/学期（12周）</li><li>课程特色：针对GCSE Chinese考试的专项训练，历年通过率100%</li></ul><h2>新生优惠</h2><p>现在报名秋季学期课程，新生可享受首月学费九折优惠。</p><h2>报名方式</h2><p>电话：0161 xxx xxxx<br>邮箱：admissions@boweneducation.org</p>',
    'published',
    1,
    '2024-02-20 09:00:00',
    '2024年秋季学期招生现已开放',
    '博文中文学校2024年秋季学期招生全面启动，GCSE通过率保持100%。',
    datetime('now'),
    datetime('now')
);

-- Article 3: HAF Programme Success
INSERT OR IGNORE INTO post (
    column_id, title, slug, summary, content_html,
    status, is_recommended, published_at,
    seo_title, seo_description, created_at, updated_at
) VALUES (
    8,
    '2024年HAF项目圆满结束，惠及200余名儿童',
    'haf-programme-success-2024',
    '博文集团作为Trafford Council官方合作伙伴，成功举办2024年暑期HAF项目，为200多名符合条件的儿童提供免费活动和健康餐食，获得家长和社区高度评价。',
    '<h2>项目概况</h2><p>2024年暑期，博文教育集团作为Trafford Council的官方HAF（Holiday Activities and Food）项目合作伙伴，成功举办了为期四周的假期活动。本次项目共惠及200余名5-16岁的儿童。</p><h2>什么是HAF项目？</h2><p>HAF项目是英国政府资助的重要社区项目，旨在为符合免费校餐资格的儿童在学校假期期间提供免费健康营养的餐食和多样化的教育娱乐活动。</p><h2>2024暑期项目亮点</h2><h3>1. 中华文化体验活动</h3><ul><li>书法课：学习基本笔画和简单汉字书写</li><li>剪纸工艺：制作传统中国剪纸作品</li><li>中国结编织：学习基础编织技法</li></ul><h3>2. 体育运动项目</h3><ul><li>羽毛球训练：由专业教练指导基础技术</li><li>国际象棋课程：培养逻辑思维</li></ul><h2>项目成果</h2><ul><li>参与儿童：206名</li><li>活动天数：20天（4周）</li><li>提供餐食：超过4,000份</li><li>家长满意度：98%</li></ul><h2>联系方式</h2><p>邮箱：haf@boweneducation.org<br>电话：0161 xxx xxxx</p>',
    'published',
    0,
    '2024-08-25 14:30:00',
    '2024年HAF项目圆满结束，惠及200余名儿童',
    '博文集团成功举办2024年暑期HAF项目，获得家长和社区高度评价。',
    datetime('now'),
    datetime('now')
);

-- Article 4: Chess Tournament Success
INSERT OR IGNORE INTO post (
    column_id, title, slug, summary, content_html,
    status, is_recommended, published_at,
    seo_title, seo_description, created_at, updated_at
) VALUES (
    8,
    '博文国际象棋俱乐部在曼彻斯特地区赛事中斩获佳绩',
    'chess-club-tournament-achievements',
    '博文国际象棋俱乐部学员在2024年春季曼彻斯特青少年锦标赛中表现出色，3名学员分别获得各组别冠军，多人晋升ECF等级分。',
    '<h2>赛事背景</h2><p>2024年3月16-17日，曼彻斯特青少年国际象棋锦标赛在Sale Leisure Centre举行。比赛分为U8、U10、U12、U14和U16五个组别，采用瑞士制7轮赛制。</p><h2>博文俱乐部战绩</h2><p>博文国际象棋俱乐部共派出28名学员参赛，取得了骄人战绩。</p><h3>冠军获得者</h3><ul><li><strong>U10组冠军</strong>：王思远（7战全胜）</li><li><strong>U12组冠军</strong>：李明轩（6胜1和）</li><li><strong>U14组冠军</strong>：张雨涵（6胜1负）</li></ul><h2>ECF等级分提升</h2><p>根据比赛成绩，多名博文学员的ECF等级分将获得显著提升：</p><ul><li>5名学员首次获得ECF等级分</li><li>12名学员等级分提升100分以上</li><li>3名学员等级分突破1000分大关</li></ul><h2>关于博文国际象棋俱乐部</h2><p>博文国际象棋俱乐部成立于2018年，是English Chess Federation (ECF)的正式会员俱乐部。</p><h3>训练时间</h3><ul><li>每周六：14:00-16:00（初级和中级）</li><li>每周六：16:00-18:00（高级和竞赛）</li></ul><h2>联系方式</h2><p>邮箱：chess@boweneducation.org<br>电话：0161 xxx xxxx<br>地点：Sale Sports Centre, Manchester</p>',
    'published',
    0,
    '2024-03-20 16:00:00',
    '博文国际象棋俱乐部在曼彻斯特地区赛事中斩获佳绩',
    '博文国际象棋俱乐部学员在2024年春季锦标赛中表现出色，3名学员获得冠军。',
    datetime('now'),
    datetime('now')
);

SELECT '✅ 成功导入 ' || COUNT(*) || ' 篇新闻' FROM post WHERE column_id = 8;
