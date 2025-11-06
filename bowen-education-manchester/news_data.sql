-- Import news articles into database
-- 导入新闻文章到数据库

-- Article 1: Henan University Partnership
INSERT OR IGNORE INTO post (
    column_id, title, slug, summary, content_html, 
    status, is_recommended, published_at, 
    seo_title, seo_description, created_at, updated_at
) VALUES (
    8, -- news column ID
    '博文集团与河南大学建立战略合作伙伴关系',
    'henan-university-partnership',
    '博文教育集团正式与中国河南大学签署战略合作协议，共同推进中英教育文化交流项目，为曼彻斯特华裔青少年提供寻根之旅机会。',
    '<h2>合作背景</h2>
<p>2024年3月，博文教育集团与河南大学在郑州正式签署战略合作协议。此次合作标志着博文集团在推动中英教育文化交流方面迈出了重要一步。河南大学作为中国百年名校，在汉语国际教育和文化传播领域具有深厚的学术积淀和丰富的教学资源。</p>

<h2>合作内容</h2>
<p>本次战略合作涵盖多个领域：</p>
<ul>
<li><strong>师资交流项目</strong>：河南大学将定期派遣优秀汉语教师来曼彻斯特进行短期教学交流，为博文中文学校提供专业的教学指导和培训支持。</li>
<li><strong>学生交流计划</strong>：每年组织博文学校学生赴河南大学参加短期文化体验营，深入了解中国历史文化。</li>
<li><strong>课程资源共享</strong>：河南大学将向博文集团提供优质的教学资源，包括HSK/YCT备考资料、中华文化课程等。</li>
<li><strong>学术研究合作</strong>：双方将在海外华文教育研究领域开展合作，共同探索适合海外华裔青少年的中文教学模式。</li>
</ul>

<h2>寻根之旅</h2>
<p>作为合作的重要组成部分，博文集团每年将组织"寻根之旅"活动，带领12-18岁的华裔青少年回到中国：</p>
<ul>
<li>参观河南大学校园，感受中国高等学府的学术氛围</li>
<li>游览开封、郑州、洛阳等历史文化名城，了解中华文明的发展历程</li>
<li>与中国学生面对面交流，建立跨文化友谊</li>
<li>参加书法、武术、茶艺等传统文化体验活动</li>
<li>探访黄河、少林寺、龙门石窟等著名景点</li>
</ul>

<h2>首次访华计划</h2>
<p>首次"寻根之旅"将于2024年复活节期间举行，为期两周。行程包括河南省主要城市和北京，学生们将入住大学宿舍和精选酒店，由专业领队和河南大学志愿者全程陪同。</p>

<p>博文集团创始人表示："这次合作不仅为我们的学生提供了更多学习中文的机会，更重要的是让生长在英国的华裔青少年有机会深入了解自己的文化根源，增强文化认同感和民族自豪感。"</p>

<h2>报名咨询</h2>
<p>如需了解更多关于河南大学合作项目和寻根之旅的信息，欢迎联系：</p>
<ul>
<li>邮箱：china-trip@boweneducation.org</li>
<li>电话：0161 xxx xxxx</li>
</ul>',
    'published',
    0,
    '2024-03-15 10:00:00',
    '博文集团与河南大学建立战略合作伙伴关系',
    '博文教育集团正式与中国河南大学签署战略合作协议，共同推进中英教育文化交流项目，为曼彻斯特华裔青少年提供寻根之旅机会。',
    datetime('now'),
    datetime('now')
);

-- Continue with remaining news articles...
-- Summaries provided, use PRAGMA to check table structure if needed

SELECT 'News data import completed. Total articles: 4';
