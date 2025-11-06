-- ============================================================
-- SEED DATA SQL - Bowen Education Group Website
-- ============================================================
-- Version: 1.0
-- Created: 2024-11-04
-- Database: PostgreSQL (compatible with SQLite)
-- Total Records: 300+ across 20 tables
-- ============================================================

-- Disable foreign key checks for seeding (PostgreSQL)
SET session_replication_role = replica;

-- ============================================================
-- 1. SITE SETTINGS (site_setting table)
-- ============================================================

INSERT INTO site_setting (
    id, site_name, site_name_chinese, tagline, tagline_chinese,
    description, keywords, phone, email, address, postcode,
    city, region, country, latitude, longitude,
    opening_hours, facebook_url, instagram_url, twitter_url,
    wechat_qr_code, whatsapp_number, youtube_url, linkedin_url,
    google_analytics_id, meta_title, meta_description, og_image,
    footer_text, footer_about, privacy_policy_url, terms_url,
    cookie_policy_url, safeguarding_url, is_published, maintenance_mode,
    created_at, updated_at
) VALUES (
    1,
    'Bowen Education Group',
    '博文集团',
    'Bridging East and West, Learning to Go Far',
    '中西融汇，博学致远',
    'Bowen Education Group offers premium Chinese language courses, GCSE/A-Level tuition, ECF-registered chess club, badminton training, and cultural programmes in Manchester. Partnering with local councils and universities to nurture bilingual, internationally-minded students since 2020.',
    'Manchester Chinese School, Mandarin lessons Manchester, GCSE Chinese, A-Level Chinese, HSK exam, YCT exam, Chinese tuition Manchester, ECF chess club, badminton club Manchester, HAF programme, Chinese cultural activities',
    '+44 (0)161 6672668',
    'info@boweneducation.org',
    '1/F, 2A Curzon Road, Sale, Manchester, M33 7DR, United Kingdom',
    'M33 7DR',
    'Manchester',
    'Greater Manchester',
    'United Kingdom',
    '53.4239',
    '-2.3224',
    'Monday - Friday: 9:00 AM - 6:00 PM
Saturday: 9:00 AM - 5:00 PM
Sunday: 9:00 AM - 3:00 PM (Term Time Only)
Bank Holidays: Closed',
    'https://www.facebook.com/BoweneducationUK/',
    'https://www.instagram.com/boweneducation/',
    NULL,
    '/static/images/wechat-qr-code.png',
    '+447912345678',
    NULL,
    NULL,
    'G-XXXXXXXXXX',
    'Bowen Education Group | Manchester Chinese School | GCSE Tuition | Chess & Badminton Clubs',
    'Leading Manchester education provider: Chinese language school (Mandarin & Cantonese), GCSE/A-Level tuition, ECF chess club, badminton, HAF programmes. Trusted by 800+ families since 2020.',
    '/static/images/og-image-bowen-education.jpg',
    '© 2024 Bowen Education Group. All rights reserved. Registered in England and Wales.',
    'Founded in 2020, Bowen Education Group is a leading multicultural education provider in Greater Manchester. We offer Chinese language courses, GCSE/A-Level tuition, ECF chess club, badminton training, and government-partnered community programmes.',
    '/legal/privacy-policy/',
    '/legal/terms-and-conditions/',
    '/legal/cookie-policy/',
    '/legal/safeguarding-policy/',
    true,
    false,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- ============================================================
-- 2. SITE COLUMNS (site_column table) - Navigation Structure
-- ============================================================

INSERT INTO site_column (id, name, name_chinese, slug, parent_id, sort_order, is_visible, is_published, icon, created_at) VALUES
(1, 'Home', '首页', 'home', NULL, 1, true, true, 'home', CURRENT_TIMESTAMP),
(2, 'About Bowen Group', '博文集团', 'about', NULL, 2, true, true, 'info-circle', CURRENT_TIMESTAMP),
(3, 'Bowen News', '博文新闻', 'news', NULL, 3, true, true, 'newspaper', CURRENT_TIMESTAMP),
(4, 'Chinese School', '中文学校', 'school', NULL, 4, true, true, 'book', CURRENT_TIMESTAMP),
(5, 'Tuition Centre', '补习中心', 'tuition', NULL, 5, true, true, 'graduation-cap', CURRENT_TIMESTAMP),
(6, 'Chess Club', '国际象棋俱乐部', 'chess', NULL, 6, true, true, 'chess-pawn', CURRENT_TIMESTAMP),
(7, 'Badminton Club', '羽毛球俱乐部', 'badminton', NULL, 7, true, true, 'shuttlecock', CURRENT_TIMESTAMP),
(8, 'Government Programmes', '政府项目', 'programmes', NULL, 8, true, true, 'landmark', CURRENT_TIMESTAMP),
(9, 'Bowen Events', '博文活动', 'events', NULL, 9, true, true, 'calendar', CURRENT_TIMESTAMP),
(10, 'Resource Centre', '资源中心', 'resources', NULL, 10, true, true, 'folder', CURRENT_TIMESTAMP),
(11, 'Contact Us', '联系我们', 'contact', NULL, 11, true, true, 'envelope', CURRENT_TIMESTAMP);

-- ============================================================
-- 3. PRODUCT CATEGORIES (product_category table)
-- ============================================================

INSERT INTO product_category (id, name, name_chinese, slug, description, sort_order, is_published, created_at) VALUES
(1, 'Chinese School Courses', '中文学校课程', 'chinese-school', 'Comprehensive Mandarin language programmes from Foundation to A-Level', 1, true, CURRENT_TIMESTAMP),
(2, 'Tuition Centre Courses', '补习中心课程', 'tuition', 'Expert GCSE and A-Level tuition in core academic subjects', 2, true, CURRENT_TIMESTAMP),
(3, 'Chess Training', '国际象棋培训', 'chess', 'ECF registered chess training programmes', 3, true, CURRENT_TIMESTAMP),
(4, 'Badminton Training', '羽毛球培训', 'badminton', 'Professional badminton coaching for all ages', 4, true, CURRENT_TIMESTAMP);

-- ============================================================
-- 4. PRODUCTS (product table) - 22 Courses
-- ============================================================

INSERT INTO product (id, category_id, name, name_chinese, slug, summary, description, price, currency, price_unit, featured_image, is_published, is_featured, stock_status, display_order, created_at, updated_at) VALUES
-- Chinese School Courses (8 courses)
(1, 1, 'Foundation Mandarin (Ages 5-7)', '启蒙中文班（5-7岁）', 'foundation-mandarin',
'Introduction to Mandarin Chinese through play-based learning, focusing on listening, speaking, and basic character recognition. Perfect for young learners starting their Chinese language journey.',
'<h2>Course Overview</h2><p>Our Foundation Mandarin programme introduces young children aged 5-7 to the Chinese language through engaging, play-based activities. Students will learn basic vocabulary, pinyin pronunciation, simple characters, and develop confidence in speaking.</p><h3>What You''ll Learn</h3><ul><li>Basic greetings and self-introduction</li><li>Numbers 1-100, colors, animals, family members</li><li>Pinyin fundamentals and tone practice</li><li>50+ Chinese characters through stories and games</li><li>Simple conversational phrases</li></ul>',
280.00, 'GBP', 'per term (10 weeks)', '/static/images/course-foundation-mandarin.jpg', true, true, 'in_stock', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(2, 1, 'Intermediate Mandarin (Ages 8-10)', '中级中文班（8-10岁）', 'intermediate-mandarin',
'Building on foundation skills with expanded vocabulary, character writing, and reading comprehension. Prepare for YCT Level 2-3 certification.',
'<h2>Course Overview</h2><p>Intermediate Mandarin develops students'' language proficiency through structured lessons combining speaking, listening, reading, and writing practice.</p><h3>What You''ll Learn</h3><ul><li>Expanded vocabulary (500+ words)</li><li>Character writing practice (200+ characters)</li><li>Short paragraph reading</li><li>Basic grammar structures</li><li>YCT Level 2-3 exam preparation</li></ul>',
300.00, 'GBP', 'per term (10 weeks)', '/static/images/course-intermediate-mandarin.jpg', true, true, 'in_stock', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(3, 1, 'Advanced Mandarin (Ages 11-13)', '高级中文班（11-13岁）', 'advanced-mandarin',
'Advanced language training focusing on essay writing, classical texts, and preparing for GCSE Chinese. YCT Level 4 and HSK Level 3-4 preparation included.',
'<h2>Course Overview</h2><p>Advanced Mandarin prepares students for GCSE Chinese while developing sophisticated language skills through reading, writing, and cultural studies.</p>',
320.00, 'GBP', 'per term (10 weeks)', '/static/images/course-advanced-mandarin.jpg', true, true, 'in_stock', 3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(4, 1, 'GCSE Chinese (Ages 14-16)', 'GCSE中文（14-16岁）', 'gcse-chinese',
'Comprehensive GCSE Chinese preparation following Edexcel and AQA specifications. Systematic training in listening, speaking, reading, and writing with focus on examination techniques.',
'<h2>Course Overview</h2><p>Our GCSE Chinese programme follows both Edexcel (1CN0) and AQA (8673) specifications, providing comprehensive exam preparation.</p><h3>Exam Board Coverage</h3><ul><li>Edexcel GCSE Chinese (1CN0)</li><li>AQA GCSE Chinese (8673)</li><li>Both Foundation and Higher tiers</li></ul><h3>Course Content</h3><ul><li>Theme 1: Identity and culture</li><li>Theme 2: Local, national, international areas of interest</li><li>Theme 3: Current and future study and employment</li></ul><h3>Success Rate</h3><p>98% pass rate with 75% achieving grades 7-9 (2024 results)</p>',
380.00, 'GBP', 'per term (10 weeks)', '/static/images/course-gcse-chinese.jpg', true, true, 'in_stock', 4, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(5, 1, 'A-Level Chinese (Ages 16-18)', 'A-Level中文（16-18岁）', 'a-level-chinese',
'Advanced A-Level Chinese for university preparation. Focus on contemporary Chinese society, culture, literature, and advanced language proficiency.',
'<h2>Course Overview</h2><p>A-Level Chinese develops advanced proficiency required for university study and professional contexts.</p>',
420.00, 'GBP', 'per term (10 weeks)', '/static/images/course-a-level-chinese.jpg', true, true, 'in_stock', 5, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(6, 1, 'Adult Mandarin Beginner', '成人初级普通话', 'adult-mandarin-beginner',
'Mandarin for adult learners focusing on practical conversation, business contexts, and HSK Level 1-2 preparation.',
'<h2>Course Overview</h2><p>Designed for adult beginners, this course focuses on practical Mandarin for travel, business, and daily communication.</p>',
250.00, 'GBP', 'per term (8 weeks)', '/static/images/course-adult-mandarin.jpg', true, false, 'in_stock', 6, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(7, 1, 'Cantonese for Beginners', '粤语初级班', 'cantonese-beginners',
'Introduction to Cantonese language and Hong Kong culture. Focus on speaking and listening comprehension.',
'<h2>Course Overview</h2><p>Learn Cantonese, the language of Hong Kong, Guangdong, and global Cantonese communities.</p>',
280.00, 'GBP', 'per term (10 weeks)', '/static/images/course-cantonese.jpg', true, false, 'in_stock', 7, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(8, 1, 'Chinese Calligraphy Workshop', '书法工作坊', 'chinese-calligraphy',
'Traditional Chinese calligraphy instruction covering brush techniques, stroke order, and classical scripts.',
'<h2>Course Overview</h2><p>Master the art of Chinese calligraphy with expert instruction in brush handling and character aesthetics.</p>',
180.00, 'GBP', 'per term (6 weeks)', '/static/images/course-calligraphy.jpg', true, false, 'in_stock', 8, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

-- Tuition Centre Courses (8 courses)
(9, 2, 'GCSE Mathematics', 'GCSE数学', 'gcse-mathematics',
'Comprehensive GCSE Maths tuition covering Foundation and Higher tiers. Small group teaching with personalized support.',
'<h2>Course Overview</h2><p>Expert GCSE Mathematics tuition following Edexcel, AQA, and OCR specifications.</p>',
350.00, 'GBP', 'per term (10 weeks)', '/static/images/course-gcse-maths.jpg', true, true, 'in_stock', 9, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(10, 2, 'GCSE English Language', 'GCSE英语语言', 'gcse-english',
'GCSE English Language preparation focusing on reading comprehension, creative writing, and exam techniques.',
'<h2>Course Overview</h2><p>Develop English language skills for GCSE success with focus on Paper 1 (Fiction) and Paper 2 (Non-fiction).</p>',
350.00, 'GBP', 'per term (10 weeks)', '/static/images/course-gcse-english.jpg', true, true, 'in_stock', 10, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(11, 2, 'GCSE Sciences (Combined)', 'GCSE综合科学', 'gcse-sciences',
'GCSE Combined Science covering Biology, Chemistry, and Physics. Exam board: AQA/Edexcel.',
'<h2>Course Overview</h2><p>Master all three sciences with comprehensive coverage of required practicals and exam technique.</p>',
380.00, 'GBP', 'per term (10 weeks)', '/static/images/course-gcse-sciences.jpg', true, false, 'in_stock', 11, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(12, 2, 'A-Level Mathematics', 'A-Level数学', 'a-level-mathematics',
'Advanced A-Level Mathematics covering Pure, Statistics, and Mechanics modules. University preparation included.',
'<h2>Course Overview</h2><p>Comprehensive A-Level Maths tuition preparing students for top university courses.</p>',
420.00, 'GBP', 'per term (10 weeks)', '/static/images/course-a-level-maths.jpg', true, true, 'in_stock', 12, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(13, 2, 'A-Level Physics', 'A-Level物理', 'a-level-physics',
'A-Level Physics covering mechanics, electricity, waves, and modern physics. Practical work included.',
'<h2>Course Overview</h2><p>Expert A-Level Physics tuition with emphasis on problem-solving and practical skills.</p>',
420.00, 'GBP', 'per term (10 weeks)', '/static/images/course-a-level-physics.jpg', true, false, 'in_stock', 13, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(14, 2, 'A-Level Chemistry', 'A-Level化学', 'a-level-chemistry',
'A-Level Chemistry including organic, inorganic, and physical chemistry. Laboratory skills development.',
'<h2>Course Overview</h2><p>Comprehensive A-Level Chemistry preparing students for science and medical degrees.</p>',
420.00, 'GBP', 'per term (10 weeks)', '/static/images/course-a-level-chemistry.jpg', true, false, 'in_stock', 14, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(15, 2, 'A-Level Economics', 'A-Level经济学', 'a-level-economics',
'A-Level Economics covering micro and macroeconomics, with focus on essay technique and data analysis.',
'<h2>Course Overview</h2><p>Master economic theory and application for A-Level success and university preparation.</p>',
400.00, 'GBP', 'per term (10 weeks)', '/static/images/course-a-level-economics.jpg', true, false, 'in_stock', 15, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(16, 2, '11+ Entrance Exam Preparation', '11+入学考试准备', '11-plus-preparation',
'Comprehensive 11+ exam preparation for grammar school and independent school entrance.',
'<h2>Course Overview</h2><p>Prepare for 11+ exams with practice in Verbal Reasoning, Non-Verbal Reasoning, Maths, and English.</p>',
320.00, 'GBP', 'per term (10 weeks)', '/static/images/course-11-plus.jpg', true, false, 'in_stock', 16, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

-- Chess Club Courses (3 courses)
(17, 3, 'Chess Beginners (Ages 6-9)', '国际象棋初学者（6-9岁）', 'chess-beginners',
'Introduction to chess rules, basic tactics, and opening principles. ECF membership included.',
'<h2>Course Overview</h2><p>Learn chess from scratch with fun, engaging lessons covering rules, piece movement, and basic strategy.</p>',
120.00, 'GBP', 'per term (10 weeks)', '/static/images/course-chess-beginners.jpg', true, true, 'in_stock', 17, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(18, 3, 'Chess Intermediate (Ages 10-14)', '国际象棋中级（10-14岁）', 'chess-intermediate',
'Developing tactical skills, opening theory, endgame technique, and competitive play. Tournament opportunities.',
'<h2>Course Overview</h2><p>Advance your chess with tactical puzzles, opening preparation, and competitive tournament experience.</p>',
140.00, 'GBP', 'per term (10 weeks)', '/static/images/course-chess-intermediate.jpg', true, true, 'in_stock', 18, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(19, 3, 'Chess Advanced & Competition', '国际象棋高级与竞赛', 'chess-advanced',
'Advanced chess training for competitive players. ECF-rated tournaments, opening repertoire development, and strategic planning.',
'<h2>Course Overview</h2><p>Elite chess training for serious competitors aiming for county and national level play.</p>',
160.00, 'GBP', 'per term (10 weeks)', '/static/images/course-chess-advanced.jpg', true, false, 'in_stock', 19, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

-- Badminton Club Courses (3 courses)
(20, 4, 'Badminton Youth Development (Ages 8-12)', '青少年羽毛球发展（8-12岁）', 'badminton-youth',
'Youth badminton programme developing fundamental skills, footwork, and match play. Qualified coaches.',
'<h2>Course Overview</h2><p>Develop badminton skills in a fun, supportive environment with professional coaching.</p>',
150.00, 'GBP', 'per term (10 weeks)', '/static/images/course-badminton-youth.jpg', true, true, 'in_stock', 20, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(21, 4, 'Badminton Junior Squad (Ages 13-17)', '少年羽毛球队（13-17岁）', 'badminton-junior-squad',
'Competitive badminton training with tournament entry. Focus on singles and doubles tactics.',
'<h2>Course Overview</h2><p>Serious badminton training for competitive juniors with county and regional tournament opportunities.</p>',
180.00, 'GBP', 'per term (10 weeks)', '/static/images/course-badminton-junior.jpg', true, true, 'in_stock', 21, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(22, 4, 'Adult Badminton Club', '成人羽毛球俱乐部', 'badminton-adult',
'Adult badminton sessions combining coaching, drills, and social play. All abilities welcome.',
'<h2>Course Overview</h2><p>Enjoy badminton in a friendly, social environment with coaching support and regular matches.</p>',
120.00, 'GBP', 'per term (10 weeks)', '/static/images/course-badminton-adult.jpg', true, false, 'in_stock', 22, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- ============================================================
-- 5. TEAM DEPARTMENTS (team_department table)
-- ============================================================

INSERT INTO team_department (id, name, name_chinese, slug, description, sort_order, is_published, created_at) VALUES
(1, 'Management Team', '管理层', 'management', 'Executive leadership and management', 1, true, CURRENT_TIMESTAMP),
(2, 'Chinese School Teachers', '中文学校教师', 'chinese-teachers', 'Qualified Mandarin language teachers', 2, true, CURRENT_TIMESTAMP),
(3, 'Tuition Centre Tutors', '补习中心导师', 'tutors', 'GCSE and A-Level subject tutors', 3, true, CURRENT_TIMESTAMP),
(4, 'Chess Coaches', '国际象棋教练', 'chess-coaches', 'ECF registered chess coaches', 4, true, CURRENT_TIMESTAMP),
(5, 'Badminton Coaches', '羽毛球教练', 'badminton-coaches', 'Professional badminton coaches', 5, true, CURRENT_TIMESTAMP);

-- ============================================================
-- 6. TEAM MEMBERS (team_member table) - 12 Members
-- ============================================================

INSERT INTO team_member (id, department_id, name, name_chinese, slug, position, position_chinese, email, phone, photo, bio, qualifications, expertise_areas, languages, is_featured, is_published, display_order, created_at) VALUES
(1, 1, 'Dr. Bowen Zhang', '张博文博士', 'dr-bowen-zhang', 'Founder & Principal', '创始人兼校长', 'bowen.zhang@boweneducation.org', '+44 (0)161 6672668',
'/static/images/team-dr-bowen-zhang.jpg',
'Dr. Bowen Zhang is the founder and principal of Bowen Education Group. With over 20 years of experience in education, Dr. Zhang has dedicated his career to bridging Eastern and Western cultures through quality education. He holds a PhD in Education from the University of Manchester and has extensive experience in Chinese language teaching, curriculum development, and educational leadership.',
'PhD in Education, University of Manchester; MA in Chinese Language Teaching, Beijing Normal University; Advanced Certificate in Educational Leadership; Member of the Chartered Institute of Educational Assessors',
'Educational Leadership, Chinese Language Teaching, Curriculum Development, Cross-Cultural Education',
'English (Fluent), Mandarin (Native), Cantonese (Conversational)',
true, true, 1, CURRENT_TIMESTAMP),

(2, 1, 'Emily Chen', '陈晓燕', 'emily-chen', 'Academic Director', '学术总监', 'emily.chen@boweneducation.org', NULL,
'/static/images/team-emily-chen.jpg',
'Emily Chen oversees all academic programmes at Bowen Education. With over 12 years of experience teaching Mandarin to both native and non-native speakers, Emily has developed a rigorous, engaging curriculum. She specializes in GCSE and A-Level Chinese exam preparation and has helped dozens of students achieve top grades.',
'MA in Chinese Language Teaching, Beijing Language and Culture University; BA in Education, Nanjing Normal University; IPA (International Profession Accreditation for Chinese Language Teachers); 12+ years teaching experience',
'GCSE/A-Level Chinese, Curriculum Development, Teacher Training, Assessment',
'Mandarin (Native), English (Fluent), Cantonese (Basic)',
true, true, 2, CURRENT_TIMESTAMP),

(3, 1, 'David Li', '李大伟', 'david-li', 'Operations Manager', '运营经理', 'david.li@boweneducation.org', NULL,
'/static/images/team-david-li.jpg',
'David Li manages day-to-day operations, facilities, and community partnerships. His background in business administration and passion for education make him instrumental in Bowen''s growth.',
'MBA, Manchester Business School; BA in Business Administration; Project Management Professional (PMP)',
'Operations Management, Business Development, Partnership Management, Strategic Planning',
'English (Fluent), Mandarin (Native)',
true, true, 3, CURRENT_TIMESTAMP),

(4, 2, 'Miss Wang Mei-Ling', '王美玲老师', 'miss-wang-mei-ling', 'Foundation Chinese Teacher', '启蒙中文教师', 'wang.meiling@boweneducation.org', NULL,
'/static/images/team-wang-meiling.jpg',
'Miss Wang specializes in teaching young children aged 5-7 years. With a warm and nurturing teaching style, she creates an engaging learning environment where children develop a love for the Chinese language through play-based activities, songs, and storytelling.',
'BA in Primary Education, Capital Normal University Beijing; Certificate in Teaching Chinese as a Foreign Language (CTCSOL); Safeguarding and Child Protection Level 3; First Aid Certified',
'Early Childhood Education, Play-Based Learning, Mandarin Phonics (Pinyin), Chinese Character Introduction',
'Mandarin (Native), English (Fluent)',
true, true, 4, CURRENT_TIMESTAMP),

(5, 2, 'Mrs. Chen Xiao-Ying', '陈晓英老师', 'mrs-chen-xiao-ying', 'GCSE/A-Level Chinese Teacher', 'GCSE/A-Level中文教师', 'chen.xiaoying@boweneducation.org', NULL,
'/static/images/team-chen-xiaoying.jpg',
'Mrs. Chen is our lead GCSE and A-Level Chinese teacher with an outstanding track record. Her students consistently achieve grades 7-9, and she has extensive experience with both Edexcel and AQA exam boards.',
'MA in Chinese Linguistics, Beijing Normal University; PGCE (Postgraduate Certificate in Education), UK; 15+ years teaching experience; Edexcel and AQA examiner',
'GCSE Chinese, A-Level Chinese, Exam Preparation, Advanced Chinese Literature',
'Mandarin (Native), English (Fluent)',
true, true, 5, CURRENT_TIMESTAMP),

(6, 2, 'Mr. Liu Wei', '刘伟老师', 'mr-liu-wei', 'Intermediate Chinese Teacher', '中级中文教师', 'liu.wei@boweneducation.org', NULL,
'/static/images/team-liu-wei.jpg',
'Mr. Liu teaches intermediate level students (ages 8-10) and specializes in YCT exam preparation. His engaging teaching style helps students build confidence and fluency.',
'BA in Chinese Language and Literature, Fudan University; Certificate in Teaching Chinese as a Foreign Language (CTCSOL); 10+ years teaching experience',
'Intermediate Chinese, YCT Exam Preparation, Character Writing, Chinese Culture',
'Mandarin (Native), English (Fluent)',
false, true, 6, CURRENT_TIMESTAMP),

(7, 3, 'Dr. Sarah Thompson', '莎拉·汤普森博士', 'dr-sarah-thompson', 'GCSE Mathematics Tutor', 'GCSE数学导师', 'sarah.thompson@boweneducation.org', NULL,
'/static/images/team-sarah-thompson.jpg',
'Dr. Thompson is a mathematics specialist with a PhD in Mathematics Education. She has helped hundreds of students achieve top grades in GCSE and A-Level Mathematics.',
'PhD in Mathematics Education, University of Cambridge; MSc in Mathematics, Imperial College London; PGCE Mathematics; 18+ years teaching experience',
'GCSE Mathematics, A-Level Mathematics, Mathematics Pedagogy, Problem-Solving',
'English (Native), Mandarin (Basic)',
true, true, 7, CURRENT_TIMESTAMP),

(8, 3, 'Mr. James Wilson', '詹姆斯·威尔逊', 'mr-james-wilson', 'GCSE English & Science Tutor', 'GCSE英语与科学导师', 'james.wilson@boweneducation.org', NULL,
'/static/images/team-james-wilson.jpg',
'Mr. Wilson is a versatile tutor specializing in GCSE English Language and Combined Science. His clear explanations and patient approach help students excel.',
'BSc in Biology, University of Manchester; PGCE English and Science; 12+ years teaching experience',
'GCSE English Language, GCSE Combined Science, Essay Writing, Scientific Method',
'English (Native)',
false, true, 8, CURRENT_TIMESTAMP),

(9, 4, 'Mr. Alexander Petrov', '亚历山大·彼得罗夫', 'mr-alexander-petrov', 'Head Chess Coach', '首席国际象棋教练', 'alex.petrov@boweneducation.org', NULL,
'/static/images/team-alex-petrov.jpg',
'Alexander is an International Master (IM) and ECF-accredited coach with over 25 years of competitive chess experience. He has coached numerous county and national champions.',
'FIDE International Master (IM); ECF Senior Chess Coach Qualification; National Champion (Russia, 1998); 25+ years coaching experience',
'Chess Strategy, Opening Theory, Endgame Technique, Tournament Preparation',
'English (Fluent), Russian (Native), Mandarin (Basic)',
true, true, 9, CURRENT_TIMESTAMP),

(10, 4, 'Miss Emma Zhang', '张艾玛', 'miss-emma-zhang', 'Junior Chess Coach', '青少年国际象棋教练', 'emma.zhang@boweneducation.org', NULL,
'/static/images/team-emma-zhang.jpg',
'Emma is a FIDE Master specializing in coaching children aged 6-12. Her fun, encouraging approach helps young players develop both chess skills and critical thinking.',
'FIDE Master (FM); ECF Chess Coach Level 2; BA in Education; English Chess Federation County Champion',
'Junior Chess Coaching, Chess for Beginners, Tactical Puzzles, Youth Tournament Preparation',
'English (Native), Mandarin (Fluent)',
false, true, 10, CURRENT_TIMESTAMP),

(11, 5, 'Coach Michael Lee', '李明教练', 'coach-michael-lee', 'Head Badminton Coach', '首席羽毛球教练', 'michael.lee@boweneducation.org', NULL,
'/static/images/team-michael-lee.jpg',
'Coach Michael Lee is a Level 3 certified badminton coach with international playing experience. He represented Malaysia at junior international level and now dedicates his career to developing young talent.',
'Badminton England Level 3 Coach; BWF (Badminton World Federation) Certified Coach; Former Malaysian National Junior Team Member; 15+ years coaching experience',
'Competitive Badminton, Junior Development, Singles & Doubles Tactics, Tournament Strategy',
'English (Fluent), Mandarin (Native), Malay (Native)',
true, true, 11, CURRENT_TIMESTAMP),

(12, 5, 'Coach Sophie Wang', '王苏菲教练', 'coach-sophie-wang', 'Youth Badminton Coach', '青少年羽毛球教练', 'sophie.wang@boweneducation.org', NULL,
'/static/images/team-sophie-wang.jpg',
'Coach Sophie specializes in youth badminton development for ages 8-14. Her patient, encouraging style helps young players build fundamental skills and confidence.',
'Badminton England Level 2 Coach; Badminton England Youth Development Specialist; County Level Player; First Aid Certified',
'Youth Badminton Development, Fundamental Skills, Footwork Training, Match Play',
'English (Fluent), Mandarin (Native)',
false, true, 12, CURRENT_TIMESTAMP);

-- ============================================================
-- 7. POST CATEGORIES (post_category table)
-- ============================================================

INSERT INTO post_category (id, name, name_chinese, slug, description, sort_order, is_published, created_at) VALUES
(1, 'Event Reports', '活动报道', 'event-reports', 'Coverage of Bowen events and activities', 1, true, CURRENT_TIMESTAMP),
(2, 'Partnership Announcements', '合作签约', 'partnerships', 'New partnerships and collaborations', 2, true, CURRENT_TIMESTAMP),
(3, 'Media Coverage', '媒体报道', 'media', 'Press releases and media mentions', 3, true, CURRENT_TIMESTAMP),
(4, 'Student Achievements', '学生成就', 'achievements', 'Student success stories and exam results', 4, true, CURRENT_TIMESTAMP),
(5, 'Community Activities', '社区活动', 'community', 'Community programmes and welfare initiatives', 5, true, CURRENT_TIMESTAMP);

-- ============================================================
-- 8. POSTS (post table) - 15 News Articles
-- ============================================================

INSERT INTO post (id, category_id, title, title_chinese, slug, summary, content, featured_image, author_name, is_published, is_featured, published_at, views, tags, created_at, updated_at) VALUES
(1, 2, 'Bowen Education Partners with Henan University for Cultural Exchange', '博文集团与河南大学签署合作协议', 'henan-university-partnership-2024',
'Bowen Education Group is delighted to announce a strategic partnership with Henan University, one of China''s leading comprehensive universities.',
'<p>Manchester, UK - 15 October 2024 - Bowen Education Group is proud to announce a landmark partnership with Henan University, one of China''s leading comprehensive universities, to establish a cultural and educational exchange programme.</p><h2>Partnership Highlights</h2><p>This collaboration will enable:</p><ul><li>Annual student exchange programmes allowing Bowen students to experience Chinese university life</li><li>Joint teacher training workshops to share best practices in Chinese language education</li><li>Access to Henan University''s digital learning resources for our advanced students</li><li>Summer camp programmes in Henan Province for cultural immersion</li></ul><h2>Significance for Bowen Students</h2><p>Dr. Bowen Zhang, Founder and Director, commented: "This partnership represents a significant milestone in our mission to bridge East and West through education. Our students will benefit from direct exposure to authentic Chinese academic environments, enhancing their language proficiency and cultural understanding."</p>',
'/static/images/news-henan-partnership.jpg', 'Dr. Bowen Zhang', true, true, '2024-10-15 10:00:00', 342, 'partnership,university,exchange,henan', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(2, 4, 'Outstanding GCSE Results: 95% Pass Rate for Chinese Language', 'GCSE中文优异成绩：95%通过率', 'gcse-chinese-results-2024',
'Bowen Education celebrates exceptional GCSE Chinese results, with 95% of students achieving grades 4-9 and 70% achieving grades 7-9.',
'<h2>Record-Breaking Results</h2><p>We are thrilled to announce that our GCSE Chinese students have achieved outstanding results in the 2024 examinations:</p><ul><li><strong>98% pass rate</strong> (grades 4-9)</li><li><strong>75% achieved grades 7-9</strong> (equivalent to A/A*)</li><li><strong>45% achieved grade 9</strong> (the highest grade)</li><li>100% of students improved by at least one grade from their predicted grades</li></ul><h2>Success Stories</h2><p><strong>Emma Chen (Grade 9)</strong> - Emma began learning Chinese at Bowen from Year 7 and credits her success to the dedicated teaching and comprehensive exam preparation.</p>',
'/static/images/news-gcse-results-2024.jpg', 'Emily Chen', true, true, '2024-08-22 09:00:00', 456, 'gcse,results,achievements,chinese', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(3, 1, '2024 Chinese New Year Gala: A Spectacular Success', '2024中国新年联欢晚会圆满成功', 'chinese-new-year-gala-2024',
'Over 300 attendees celebrated the Year of the Dragon at Bowen''s annual Chinese New Year Gala featuring performances, cultural activities, and traditional food.',
'<p>On Saturday, 10 February 2024, Bowen Education Group hosted its biggest Chinese New Year celebration yet, welcoming over 300 students, families, and community members to celebrate the Year of the Dragon.</p><h2>Event Highlights</h2><ul><li>Traditional lion dance performance by Manchester Chinese Lion Dance Association</li><li>Student performances including songs, dances, and poetry recitation</li><li>Cultural workshops: calligraphy, paper-cutting, Chinese knot making</li><li>Traditional food tasting with dumplings, spring rolls, and Chinese tea</li><li>Lucky draw with prizes including course vouchers and Chinese gifts</li></ul>',
'/static/images/news-cny-gala-2024.jpg', 'David Li', true, true, '2024-02-12 14:00:00', 523, 'chinese new year,event,culture,community', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(4, 5, 'Bowen Launches HAF Summer Programme in Partnership with Manchester City Council', '博文与曼彻斯特市政府合作推出HAF夏季项目', 'haf-summer-programme-2024',
'Bowen Education selected to deliver Holiday Activities and Food (HAF) programme for Manchester children during summer holidays.',
'<p>Bowen Education Group has been selected by Manchester City Council to deliver a Holiday Activities and Food (HAF) programme this summer, providing free activities and healthy meals to children from low-income families.</p><h2>Programme Details</h2><p>Running for 4 weeks in July and August, the programme will offer:</p><ul><li>Daily cultural activities including Chinese language, calligraphy, martial arts</li><li>Physical activities: badminton, chess, outdoor games</li><li>Nutritious hot meals prepared daily</li><li>Arts and crafts workshops</li><li>Educational trips and visits</li></ul>',
'/static/images/news-haf-programme.jpg', 'David Li', true, false, '2024-06-15 10:00:00', 289, 'haf,government,community,summer', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(5, 4, 'Bowen Chess Club Students Win Regional Tournament', '博文国际象棋俱乐部学生赢得区域锦标赛', 'chess-regional-tournament-win-2024',
'Three Bowen Chess Club students secured top positions at the North West Regional Junior Chess Championship.',
'<p>Bowen Chess Club is celebrating after three of our students achieved outstanding results at the North West Regional Junior Chess Championship held in Liverpool on 5 October 2024.</p><h2>Results</h2><ul><li><strong>Tom Wu (age 12)</strong> - 1st Place, Under-12 Category</li><li><strong>Sarah Zhang (age 10)</strong> - 2nd Place, Under-10 Category</li><li><strong>Alex Chen (age 14)</strong> - 3rd Place, Under-14 Category</li></ul><p>All three students have qualified for the National Finals in London in December.</p>',
'/static/images/news-chess-tournament-win.jpg', 'Alexander Petrov', true, false, '2024-10-08 15:00:00', 312, 'chess,tournament,achievement,students', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(6, 1, 'Roots Journey: Bowen Students Visit Henan Province', '寻根之旅：博文学生参访河南', 'roots-journey-henan-2024',
'15 Bowen students embarked on a cultural heritage trip to Henan Province, visiting historical sites and experiencing Chinese culture firsthand.',
'<p>This summer, 15 Bowen students aged 12-16 participated in our inaugural "Roots Journey" cultural heritage trip to Henan Province, China.</p><h2>Trip Highlights</h2><ul><li>Visit to Shaolin Temple and martial arts demonstration</li><li>Tour of Longmen Grottoes (UNESCO World Heritage Site)</li><li>Chinese language immersion at Henan University</li><li>Homestay experience with local families</li><li>Kaifeng cultural tour and traditional performances</li></ul><p>The trip was a transformative experience for all participants, deepening their connection to Chinese culture and motivating continued language study.</p>',
'/static/images/news-henan-trip-2024.jpg', 'Emily Chen', true, true, '2024-08-28 12:00:00', 401, 'heritage trip,china,culture,students', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(7, 3, 'BBC Radio Manchester Features Bowen Education', 'BBC曼彻斯特电台专访博文集团', 'bbc-radio-manchester-feature',
'Dr. Bowen Zhang interviewed on BBC Radio Manchester about the importance of bilingual education.',
'<p>On 20 September 2024, Dr. Bowen Zhang was invited to BBC Radio Manchester''s morning show to discuss the growing importance of Mandarin language education in the UK.</p><p>The 20-minute interview covered topics including:</p><ul><li>The benefits of bilingual education for children</li><li>Growing demand for Mandarin in British schools</li><li>Bowen''s approach to blending Eastern and Western teaching methods</li><li>The role of Chinese community schools in cultural preservation</li></ul>',
'/static/images/news-bbc-radio-interview.jpg', 'Dr. Bowen Zhang', true, false, '2024-09-21 09:00:00', 267, 'media,bbc,interview,education', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(8, 2, 'Bowen Education Signs Partnership with Manchester Grammar School', '博文与曼彻斯特文法学校签署合作协议', 'manchester-grammar-partnership',
'Bowen Education to provide Mandarin language classes for Manchester Grammar School students starting September 2024.',
'<p>Bowen Education Group is delighted to announce a new partnership with Manchester Grammar School to deliver Mandarin language instruction as part of their expanded modern languages curriculum.</p><p>Starting in September 2024, Bowen teachers will provide weekly Mandarin classes for Years 7-11, with GCSE preparation for interested students.</p>',
'/static/images/news-mgs-partnership.jpg', 'Dr. Bowen Zhang', true, false, '2024-07-10 11:00:00', 198, 'partnership,school,education', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(9, 4, 'A-Level Chinese Students Achieve 100% Pass Rate', 'A-Level中文学生100%通过率', 'a-level-results-2024',
'All Bowen A-Level Chinese students achieved grades A*-B in summer 2024 examinations.',
'<p>Bowen Education is proud to announce outstanding A-Level Chinese results for 2024:</p><ul><li>100% pass rate (grades A*-E)</li><li>85% achieved A*-A grades</li><li>All students exceeded their predicted grades</li></ul><p>These exceptional results reflect the dedication of our students and the expertise of our teaching staff led by Mrs. Chen Xiao-Ying.</p>',
'/static/images/news-a-level-results.jpg', 'Emily Chen', true, false, '2024-08-15 10:00:00', 334, 'a-level,results,achievements', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(10, 5, 'Bowen Charity Run Raises £5,000 for Local Food Bank', '博文慈善跑为当地食品银行筹款5000英镑', 'charity-run-2024',
'Over 100 participants joined Bowen''s charity fun run, raising £5,000 for Trafford Food Bank.',
'<p>On Sunday, 5 May 2024, Bowen Education Group organized a charity fun run at Sale Water Park, with all proceeds going to Trafford Food Bank.</p><p>The event featured:</p><ul><li>5km and 10km routes around the scenic water park</li><li>Fun activities for children including face painting and games</li><li>Refreshment stalls and entertainment</li><li>Prize raffle with donations from local businesses</li></ul><p>Over 100 participants took part, including students, parents, staff, and community members, raising a total of £5,000.</p>',
'/static/images/news-charity-run-2024.jpg', 'David Li', true, false, '2024-05-06 14:00:00', 276, 'charity,community,fundraising', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(11, 1, 'Mid-Autumn Festival Celebration 2024', '2024中秋节庆祝活动', 'mid-autumn-festival-2024',
'Bowen families celebrated Mid-Autumn Festival with lantern making, mooncake tasting, and traditional performances.',
'<p>On Saturday, 14 September 2024, Bowen Education hosted a Mid-Autumn Festival celebration bringing together over 150 students and families.</p><h2>Festival Activities</h2><ul><li>Lantern making workshops</li><li>Traditional mooncake tasting</li><li>Chang''e and the Moon Rabbit storytelling</li><li>Chinese classical music performance</li><li>Mid-Autumn poetry recitation</li></ul>',
'/static/images/news-mid-autumn-2024.jpg', 'Emily Chen', true, false, '2024-09-16 12:00:00', 289, 'festival,culture,community', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(12, 4, 'Badminton Junior Squad Wins County Championship', '羽毛球少年队赢得郡锦标赛', 'badminton-county-championship',
'Bowen Badminton Club''s junior squad secured first place at the Greater Manchester Youth Badminton Championship.',
'<p>On 12 October 2024, Bowen Badminton Club''s junior squad (ages 13-17) won first place at the Greater Manchester Youth Badminton Championship.</p><p>The team, coached by Michael Lee and Sophie Wang, defeated teams from across Greater Manchester in singles, doubles, and mixed doubles events.</p>',
'/static/images/news-badminton-championship.jpg', 'Michael Lee', true, false, '2024-10-14 16:00:00', 245, 'badminton,sports,achievement', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(13, 2, 'Bowen Joins Confucius Institute Network', '博文加入孔子学院网络', 'confucius-institute-partnership',
'Bowen Education becomes affiliated teaching center with Confucius Institute for Chinese Language Teaching.',
'<p>Bowen Education Group has been recognized as an affiliated teaching center by the Confucius Institute, joining a global network of institutions promoting Chinese language and culture education.</p><p>This affiliation provides Bowen with access to teaching resources, professional development, and international collaboration opportunities.</p>',
'/static/images/news-confucius-partnership.jpg', 'Dr. Bowen Zhang', true, false, '2024-09-05 10:00:00', 198, 'partnership,confucius institute,education', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(14, 5, 'Culture Into Schools Programme Reaches 500 Students', '"文化进校园"项目惠及500名学生', 'culture-into-schools-500',
'Bowen''s Culture Into Schools programme has now reached over 500 Manchester primary school students with Chinese language and cultural workshops.',
'<p>Since launching in January 2024, Bowen Education''s "Culture Into Schools" outreach programme has delivered workshops to over 500 primary school students across 15 Manchester schools.</p><h2>Workshop Topics</h2><ul><li>Introduction to Mandarin language</li><li>Chinese calligraphy basics</li><li>Traditional Chinese stories and legends</li><li>Lunar New Year customs</li><li>Chinese music and instruments</li></ul>',
'/static/images/news-culture-into-schools.jpg', 'Emily Chen', true, false, '2024-10-25 11:00:00', 312, 'outreach,schools,culture,education', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(15, 4, 'Former Student Wins Scholarship to Oxford University', '博文毕业生获牛津大学奖学金', 'oxford-scholarship-winner',
'Bowen alumna Lisa Wang has been awarded a full scholarship to study Modern Languages at Oxford University.',
'<p>We are immensely proud to announce that Lisa Wang, a former Bowen student who completed her A-Level Chinese with us, has been awarded a full scholarship to read Modern Languages (Chinese) at Magdalen College, Oxford.</p><p>Lisa, who started learning Mandarin at Bowen at age 7, achieved A* in A-Level Chinese and A*AA in her other A-Levels. She credits Bowen teachers, particularly Mrs. Chen, for inspiring her passion for Chinese language and culture.</p>',
'/static/images/news-oxford-scholarship.jpg', 'Emily Chen', true, true, '2024-09-18 14:00:00', 487, 'scholarship,oxford,achievement,alumni', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Continue in next part due to length...

-- ============================================================
-- 9. EVENT CATEGORIES (event_category table)
-- ============================================================

INSERT INTO event_category (id, name, name_chinese, slug, description, sort_order, is_published, created_at) VALUES
(1, 'Chess Tournaments', '国际象棋比赛', 'chess-tournaments', 'Chess competitions and tournaments', 1, true, CURRENT_TIMESTAMP),
(2, 'Badminton Competitions', '羽毛球比赛', 'badminton-competitions', 'Badminton matches and tournaments', 2, true, CURRENT_TIMESTAMP),
(3, 'Cultural Festivals', '文化节庆', 'cultural-festivals', 'Chinese cultural celebration events', 3, true, CURRENT_TIMESTAMP),
(4, 'Heritage Trips', '寻根之旅', 'heritage-trips', 'Educational trips to China', 4, true, CURRENT_TIMESTAMP),
(5, 'School Workshops', '学校工作坊', 'school-workshops', 'Workshops and open days', 5, true, CURRENT_TIMESTAMP),
(6, 'Community Events', '社区活动', 'community-events', 'Community outreach and welfare events', 6, true, CURRENT_TIMESTAMP),
(7, 'Government Programmes', '政府项目', 'government-programmes', 'HAF and council-partnered programmes', 7, true, CURRENT_TIMESTAMP),
(8, 'Parent Events', '家长活动', 'parent-events', 'Parent information sessions and meetings', 8, true, CURRENT_TIMESTAMP);

-- ============================================================
-- 10. EVENTS (event table) - 10 Events
-- ============================================================

INSERT INTO event (id, category_id, title, title_chinese, slug, description, event_date, start_time, end_time, location, location_address, capacity, price, currency, registration_deadline, is_registration_open, featured_image, is_featured, is_published, status, created_at, updated_at) VALUES
(1, 3, 'Chinese New Year Gala 2025', '2025中国新年庆典', 'chinese-new-year-gala-2025',
'<h2>Welcome the Year of the Snake!</h2><p>Join Bowen Education Group for our spectacular Chinese New Year Gala 2025, celebrating the Year of the Snake (蛇年) with traditional performances, cultural activities, delicious food, and community fun for all ages.</p><h3>Event Highlights</h3><ul><li><strong>Traditional Performances:</strong> Lion dance, dragon dance, Chinese classical dance, martial arts demonstrations</li><li><strong>Student Showcase:</strong> Performances by Bowen Chinese School students (singing, instrumental, poetry recitation)</li><li><strong>Cultural Activities:</strong> Calligraphy workshop, paper-cutting, Chinese knot making, face painting</li><li><strong>Food Stalls:</strong> Traditional Chinese snacks, dumplings, spring rolls, tea service</li><li><strong>Lucky Draw:</strong> Win prizes including Bowen course vouchers, Chinese gifts, and restaurant vouchers</li><li><strong>Photo Booth:</strong> Chinese New Year themed photo opportunities with props</li></ul>',
'2025-02-08', '13:00:00', '17:00:00',
'Sale Waterside Arts Centre',
'1 Waterside Plaza, Sale, Manchester M33 7ZF',
300, 10.00, 'GBP', '2025-02-05 23:59:59', true,
'/static/images/event-chinese-new-year-2025.jpg', true, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(2, 4, 'Roots Journey to Henan 2025', '2025河南寻根之旅', 'roots-journey-henan-2025',
'<h2>Cultural Heritage Trip to Henan Province</h2><p>Join us for an unforgettable 10-day educational journey to Henan Province, the cradle of Chinese civilization. Students aged 12-18 will experience authentic Chinese culture, practice Mandarin, and visit historical sites.</p><h3>Trip Highlights</h3><ul><li>Shaolin Temple visit and martial arts demonstration</li><li>Longmen Grottoes UNESCO World Heritage Site</li><li>Henan University campus visit and language exchange</li><li>Homestay with local families (3 nights)</li><li>Kaifeng ancient capital tour</li><li>Chinese cooking class and cultural workshops</li></ul><h3>Dates</h3><p>10 days during summer holidays: 20-30 July 2025</p><h3>Price Includes</h3><ul><li>Return flights from Manchester</li><li>Accommodation (hotels and homestay)</li><li>All meals</li><li>Transportation in China</li><li>Entrance fees to all attractions</li><li>Travel insurance</li><li>English-speaking tour guide</li></ul>',
'2025-07-20', '06:00:00', '2025-07-30 22:00:00',
'Departing from Manchester Airport',
'Manchester Airport, M90 1QX',
20, 1850.00, 'GBP', '2025-05-31 23:59:59', true,
'/static/images/event-henan-trip-2025.jpg', true, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(3, 1, 'Autumn Chess Tournament 2024', '2024秋季国际象棋锦标赛', 'chess-autumn-tournament-2024',
'<h2>ECF-Rated Autumn Chess Tournament</h2><p>Bowen Chess Club hosts its annual Autumn Tournament, open to players of all ages and abilities. ECF-rated games for registered members.</p><h3>Categories</h3><ul><li>Under-10 (Unrated)</li><li>Under-12 (ECF-rated)</li><li>Under-14 (ECF-rated)</li><li>Under-18 (ECF-rated)</li><li>Adult Open (ECF-rated)</li></ul><h3>Format</h3><p>5-round Swiss system, 25 minutes per player. Trophies for 1st, 2nd, 3rd in each category.</p>',
'2024-11-29', '14:00:00', '18:00:00',
'Bowen Education Centre',
'2A Curzon Road, Sale, M33 7DR',
50, 15.00, 'GBP', '2024-11-25 23:59:59', true,
'/static/images/event-chess-tournament-autumn.jpg', true, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(4, 2, 'Manchester Inter-School Badminton Tournament', '曼彻斯特校际羽毛球锦标赛', 'inter-school-badminton-2024',
'<h2>Annual Inter-School Badminton Championship</h2><p>Bowen Badminton Club invites schools across Greater Manchester to participate in our annual inter-school badminton tournament.</p><h3>Age Groups</h3><ul><li>Under-13 Boys & Girls Singles and Doubles</li><li>Under-15 Boys & Girls Singles and Doubles</li><li>Under-17 Boys & Girls Singles and Doubles</li></ul>',
'2024-12-07', '09:00:00', '17:00:00',
'Manchester Aquatics Centre',
'2 Booth Street East, Manchester M13 9SS',
100, 12.00, 'GBP', '2024-11-30 23:59:59', true,
'/static/images/event-badminton-tournament.jpg', false, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(5, 3, 'Mid-Autumn Festival Celebration 2025', '2025中秋节庆祝活动', 'mid-autumn-festival-2025',
'<h2>Mid-Autumn Festival Family Celebration</h2><p>Celebrate the Mid-Autumn Festival (中秋节) with Bowen Education! Join us for mooncake tasting, lantern making, and traditional performances.</p><h3>Activities</h3><ul><li>Traditional mooncake tasting</li><li>DIY lantern making workshop</li><li>Chang''e and the Moon Rabbit storytelling</li><li>Chinese classical music performance</li><li>Mid-Autumn poetry recitation</li><li>Moon viewing and photography</li></ul>',
'2025-09-06', '15:00:00', '19:00:00',
'Sale Water Park',
'Rifle Road, Sale M33 2LX',
200, 8.00, 'GBP', '2025-09-03 23:59:59', false,
'/static/images/event-mid-autumn-2025.jpg', false, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(6, 7, 'HAF Summer Programme 2025', '2025 HAF夏季项目', 'haf-summer-2025',
'<h2>FREE Holiday Activities and Food Programme</h2><p>In partnership with Manchester City Council, Bowen Education offers a FREE 4-week summer programme for children aged 5-11 from eligible families.</p><h3>Programme Includes</h3><ul><li>Daily cultural activities (Chinese language, calligraphy, martial arts)</li><li>Physical activities (badminton, chess, outdoor games)</li><li>Free nutritious hot lunch and snacks every day</li><li>Arts and crafts workshops</li><li>Educational trips and visits</li></ul><h3>Eligibility</h3><p>Free for children aged 5-11 who receive benefits-related free school meals.</p>',
'2025-07-28', '09:00:00', '2025-08-22 16:00:00',
'Bowen Education Centre',
'2A Curzon Road, Sale, M33 7DR',
40, 0.00, 'GBP', '2025-07-14 23:59:59', false,
'/static/images/event-haf-summer-2025.jpg', true, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(7, 5, 'Open Day - Discover Bowen Education', '开放日 - 探索博文集团', 'open-day-autumn-2024',
'<h2>Bowen Education Open Day</h2><p>Explore our facilities, meet our teachers, and discover our programmes. Free trial lessons in Chinese, chess, and badminton!</p><h3>Schedule</h3><ul><li>10:00 AM - Welcome and information session</li><li>10:30 AM - Campus tour</li><li>11:00 AM - Free trial lessons (choose one): Chinese class, Chess workshop, Badminton session</li><li>12:00 PM - Q&A with teachers and management</li><li>12:30 PM - Light refreshments</li></ul>',
'2024-11-16', '10:00:00', '13:00:00',
'Bowen Education Centre',
'2A Curzon Road, Sale, M33 7DR',
80, 0.00, 'GBP', '2024-11-14 23:59:59', true,
'/static/images/event-open-day.jpg', false, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(8, 6, 'Bowen Charity Fun Run 2025', '2025博文慈善趣味跑', 'charity-fun-run-2025',
'<h2>Annual Charity Fun Run</h2><p>Join Bowen Education''s annual charity fun run at Sale Water Park. All proceeds go to Trafford Food Bank.</p><h3>Race Options</h3><ul><li>5km Fun Run (all ages)</li><li>10km Competitive Run</li><li>1km Kids Dash (under 8s)</li></ul><h3>Entry Includes</h3><ul><li>Race number and timing chip</li><li>Finisher''s medal</li><li>Event t-shirt</li><li>Post-race refreshments</li></ul>',
'2025-05-04', '09:00:00', '13:00:00',
'Sale Water Park',
'Rifle Road, Sale M33 2LX',
150, 18.00, 'GBP', '2025-04-25 23:59:59', false,
'/static/images/event-charity-run-2025.jpg', false, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(9, 1, 'Chess Summer Camp 2025', '2025国际象棋夏令营', 'chess-summer-camp-2025',
'<h2>Intensive Chess Summer Camp</h2><p>5-day intensive chess training camp for players aged 8-16. Improve your game with daily lessons, tactical training, and tournament practice.</p><h3>Camp Includes</h3><ul><li>5 days of expert coaching (9am-4pm)</li><li>Opening repertoire development</li><li>Tactical puzzle sessions</li><li>Endgame masterclasses</li><li>Practice tournament on final day</li><li>Lunch and snacks provided</li></ul>',
'2025-08-11', '09:00:00', '2025-08-15 16:00:00',
'Bowen Education Centre',
'2A Curzon Road, Sale, M33 7DR',
25, 220.00, 'GBP', '2025-07-25 23:59:59', false,
'/static/images/event-chess-summer-camp.jpg', false, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

(10, 8, 'Parent Information Evening: GCSE Options', '家长信息会：GCSE选课', 'parent-info-gcse-2024',
'<h2>GCSE Options Information Evening</h2><p>Information session for parents of Year 9 students considering GCSE Chinese or other subjects at Bowen Tuition Centre.</p><h3>Topics Covered</h3><ul><li>GCSE curriculum overview</li><li>Exam board options (Edexcel vs AQA)</li><li>Course structure and assessment</li><li>Our teaching methodology and success rates</li><li>Enrollment process and fees</li><li>Q&A with teachers</li></ul>',
'2024-11-21', '18:30:00', '20:00:00',
'Bowen Education Centre',
'2A Curzon Road, Sale, M33 7DR',
50, 0.00, 'GBP', '2024-11-19 23:59:59', true,
'/static/images/event-parent-info-evening.jpg', false, true, 'upcoming', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- ============================================================
-- 11. FAQ CATEGORIES (faq_category table)
-- ============================================================

INSERT INTO faq_category (id, name, name_chinese, slug, sort_order, is_published, created_at) VALUES
(1, 'Enrollment & Fees', '报名与费用', 'enrollment-fees', 1, true, CURRENT_TIMESTAMP),
(2, 'Course Information', '课程信息', 'course-info', 2, true, CURRENT_TIMESTAMP),
(3, 'Policies & Rules', '政策与规定', 'policies', 3, true, CURRENT_TIMESTAMP),
(4, 'Club FAQs', '俱乐部问题', 'clubs', 4, true, CURRENT_TIMESTAMP),
(5, 'General Questions', '一般问题', 'general', 5, true, CURRENT_TIMESTAMP);

-- ============================================================
-- 12. FAQS (faq table) - 20 Questions
-- ============================================================

INSERT INTO faq (id, category_id, question, question_chinese, answer, answer_chinese, sort_order, is_published, created_at) VALUES
(1, 1, 'How do I enroll my child at Bowen Education?', '如何为孩子报名？',
'To enroll your child, please follow these steps:
1. Browse our courses at boweneducation.org/courses
2. Select the course(s) you''re interested in
3. Complete the online enrollment form or contact us at info@boweneducation.org
4. We''ll arrange a placement assessment for Chinese courses (ages 8+)
5. Once placed, you''ll receive payment details and term dates
6. Payment confirms your child''s place

We recommend booking a free consultation first to discuss your child''s learning needs.',
'报名步骤：1. 浏览课程 2. 在线填表或联系我们 3. 中文课程需参加分班测试（8岁以上）4. 收到缴费详情 5. 缴费确认名额',
1, true, CURRENT_TIMESTAMP),

(2, 1, 'What are your course fees?', '课程费用是多少？',
'Course fees vary by programme:

Chinese School:
- Foundation (Ages 5-7): £280 per term
- Intermediate (Ages 8-10): £300 per term
- Advanced (Ages 11-13): £320 per term
- GCSE Chinese: £380 per term
- A-Level Chinese: £420 per term

Tuition Centre:
- GCSE subjects: £350 per term
- A-Level subjects: £420 per term

Clubs:
- Chess Club: £120-160 per term
- Badminton Club: £120-180 per term

Terms are 10 weeks long. Discounts available for siblings and multiple courses.',
'中文学校：£280-420/学期；补习中心：£350-420/学期；俱乐部：£120-180/学期。兄弟姐妹和多课程享优惠。',
2, true, CURRENT_TIMESTAMP),

(3, 1, 'Do you offer free trial lessons?', '提供免费试听课吗？',
'Yes! We offer free trial lessons for most of our courses. This allows your child to experience our teaching style and see if the class is a good fit before committing to enrollment.

To book a trial lesson:
1. Visit our Consultation Booking page
2. Select your preferred course and time slot
3. Fill in your details and submit

We''ll confirm your trial lesson within 24 hours. Trial lessons are subject to availability.',
'是的！我们为大多数课程提供免费试听课。请访问我们的预约页面选择课程和时间，我们将在24小时内确认。',
3, true, CURRENT_TIMESTAMP),

(4, 1, 'What is your refund policy?', '退款政策是什么？',
'Our refund policy is as follows:

- More than 4 weeks before term starts: Full refund minus £50 administrative fee
- 2-4 weeks before term starts: 50% refund
- Less than 2 weeks before term starts: No refund, but fees can be transferred to next term
- After term begins: No refunds

Special circumstances (medical, relocation) will be considered on a case-by-case basis. All refund requests must be submitted in writing to admin@boweneducation.org.',
'开学前4周以上：全额退款减£50行政费；2-4周：退50%；2周内：不退款但可转下学期；特殊情况个案处理。',
4, true, CURRENT_TIMESTAMP),

(5, 1, 'Do you offer sibling discounts?', '提供兄弟姐妹折扣吗？',
'Yes! We offer a 10% discount on the second child''s enrollment and 15% discount for three or more children from the same family.

Additionally, if one child enrolls in multiple courses, we offer a 5% discount on the second course and 10% discount on three or more courses.

Discounts are automatically applied when you enroll multiple children or courses.',
'是的！第二个孩子享10%折扣，三个或以上享15%折扣。同一孩子报读多个课程也享优惠。',
5, true, CURRENT_TIMESTAMP),

(6, 2, 'What age groups do you cater to?', '适合哪些年龄段？',
'Bowen Education offers courses for ages 5 to 18+:

- Chinese School: Ages 5-18 (Foundation to A-Level)
- Tuition Centre: Ages 14-18 (GCSE and A-Level)
- Chess Club: Ages 6-16 (Beginner to Advanced)
- Badminton Club: Ages 8+ (Youth and Adult)
- HAF Programmes: Ages 5-11 (Primary school children)

We also offer adult classes in Chinese language and calligraphy upon request.',
'中文学校：5-18岁；补习中心：14-18岁；国际象棋：6-16岁；羽毛球：8岁以上；HAF项目：5-11岁。成人中文课程接受预约。',
6, true, CURRENT_TIMESTAMP),

(7, 2, 'How many students are in each class?', '每班多少学生？',
'We maintain small class sizes to ensure personalized attention:

- Chinese School: Maximum 12 students per class (average 8-10)
- GCSE/A-Level Tuition: Maximum 8 students per class (average 5-6)
- Chess Club: Maximum 16 students per session
- Badminton Club: Maximum 20 students per session

Small class sizes allow teachers to provide individual feedback and adapt lessons to each student''s pace.',
'中文学校：最多12人（平均8-10人）；GCSE/A-Level：最多8人（平均5-6人）；国际象棋：最多16人；羽毛球：最多20人。',
7, true, CURRENT_TIMESTAMP),

(8, 2, 'What qualifications do your teachers have?', '老师资质如何？',
'All Bowen teachers are highly qualified and experienced:

Chinese Teachers:
- Native Mandarin speakers
- Bachelor''s or Master''s degrees in Education or Chinese Language Teaching
- CTCSOL (Certificate for Teachers of Chinese to Speakers of Other Languages) or equivalent
- Enhanced DBS checks
- Safeguarding training

Tuition Centre Tutors:
- Relevant subject degrees (often postgraduate level)
- PGCE (Qualified Teacher Status) or equivalent
- Years of GCSE/A-Level teaching experience
- Enhanced DBS checks

Club Coaches:
- Professional coaching qualifications (ECF for chess, Badminton England for badminton)
- Enhanced DBS checks
- First Aid certification',
'所有教师均持有相关学位、教学资格证书（如CTCSOL、PGCE）、DBS背景调查和儿童保护培训证明。中文教师为母语者。',
8, true, CURRENT_TIMESTAMP),

(9, 2, 'Do you follow the national curriculum?', '遵循国家课程大纲吗？',
'For GCSE and A-Level courses, we follow exam board specifications (Edexcel, AQA, OCR) which align with the national curriculum.

For Chinese School courses, we follow a custom curriculum developed by our Academic Director that:
- Incorporates best practices from Chinese and Western pedagogies
- Aligns with YCT and HSK international standards
- Prepares students for UK GCSE and A-Level exams
- Emphasizes practical communication skills alongside literacy

Our curriculum is regularly reviewed and updated to meet students'' needs and exam requirements.',
'GCSE和A-Level课程遵循考试委员会规范。中文学校课程采用自主开发课程，结合中西教学法，对接YCT、HSK和英国考试标准。',
9, true, CURRENT_TIMESTAMP),

(10, 2, 'What exams can my child take?', '孩子可以参加哪些考试？',
'Students at Bowen can prepare for various examinations:

Chinese Language:
- YCT (Youth Chinese Test) Levels 1-4 (ages 7-15)
- HSK (Hanyu Shuiping Kaoshi) Levels 1-6 (ages 12+)
- GCSE Chinese (Edexcel 1CN0 / AQA 8673)
- A-Level Chinese (Edexcel / AQA)

Other Subjects:
- GCSE in Mathematics, English, Sciences, Economics, etc.
- A-Level in Mathematics, Physics, Chemistry, Economics, etc.

Chess:
- ECF-rated tournaments for competitive players

We provide comprehensive exam preparation including mock exams, past papers, and exam technique training.',
'中文：YCT、HSK、GCSE、A-Level；其他科目：GCSE/A-Level数学、科学、经济等；国际象棋：ECF评级比赛。',
10, true, CURRENT_TIMESTAMP),

(11, 3, 'What is your attendance policy?', '出勤政策是什么？',
'Regular attendance is essential for learning progress. Our policy:

- Students are expected to attend all scheduled lessons
- If your child will be absent, please notify us at least 24 hours in advance via email or phone
- For Chinese School and Tuition Centre: No makeup lessons for student-caused absences
- If a teacher is absent or class is canceled by us, a makeup lesson will be scheduled or credit applied
- Persistent absences (more than 3 consecutive weeks) may result in loss of enrollment

We understand emergencies happen. Please communicate with us about any challenges affecting attendance.',
'学生应参加所有课程。缺课请提前24小时通知。学生原因缺课不补课；教师原因取消课程会安排补课或退费。连续缺课3周以上可能失去名额。',
11, true, CURRENT_TIMESTAMP),

(12, 3, 'Do you have a behavior policy?', '有行为规范吗？',
'Yes. Bowen Education maintains a positive learning environment for all students. Our behavior policy includes:

Expected Behavior:
- Respect for teachers, staff, and fellow students
- Active participation in lessons
- Completion of homework assignments
- Care for facilities and materials
- Following safety rules

Consequences:
- First incident: Verbal warning
- Second incident: Written warning to parents
- Third incident: Meeting with parents
- Serious or repeated issues: Suspension or exclusion

We work with parents to address behavior concerns early and constructively.',
'我们要求学生尊重他人、积极参与、完成作业、爱护设施。违纪处理：口头警告→书面通知家长→家长会谈→停课或开除。',
12, true, CURRENT_TIMESTAMP),

(13, 3, 'What is your safeguarding policy?', '儿童保护政策是什么？',
'Safeguarding children is our highest priority. Our comprehensive safeguarding policy includes:

- All staff undergo Enhanced DBS checks before employment
- Regular safeguarding training for all staff
- Designated Safeguarding Lead (DSL) on premises during all activities
- Clear procedures for reporting concerns
- Secure premises with controlled access
- Parent/guardian photo ID verification for child collection
- First aid trained staff on site
- Incident reporting and record keeping

Our full Safeguarding Policy is available on our website and by request. If you have any safeguarding concerns, contact our DSL immediately at safeguarding@boweneducation.org.',
'所有员工经加强DBS背景调查，定期接受儿童保护培训。有专职儿童保护负责人、安全设施、急救培训等。完整政策见官网。',
13, true, CURRENT_TIMESTAMP),

(14, 4, 'Do I need to be an ECF member to join Chess Club?', '加入国际象棋俱乐部需要ECF会员吗？',
'For casual play and beginner lessons, ECF membership is not required.

However, ECF membership (£15/year for juniors) is required if you want to:
- Participate in ECF-rated tournaments
- Earn an official ECF rating
- Qualify for regional and national competitions

We can help you register for ECF membership when you''re ready. Many of our intermediate and advanced students choose to join ECF to compete seriously.',
'休闲对弈和初学课程不需要。但参加ECF评级比赛、获得官方评级、参加区域和全国比赛需要ECF会员（青少年£15/年）。我们可协助注册。',
14, true, CURRENT_TIMESTAMP),

(15, 4, 'What equipment do I need for Badminton Club?', '羽毛球俱乐部需要什么装备？',
'For your first few sessions, we can lend you a racket and shuttlecocks. However, we recommend purchasing your own equipment:

Essential:
- Badminton racket (suitable for age/level, £30-80)
- Non-marking indoor court shoes (crucial for safety, £40-70)
- Sports clothing (shorts/skirt and t-shirt)

Recommended:
- Badminton shuttlecocks for practice
- Water bottle
- Small towel
- Extra socks

Our coaches can advise on suitable equipment for your child''s level. Some sports shops offer student discounts.',
'前几次可借用球拍和羽毛球。建议自备：羽毛球拍（£30-80）、无痕室内运动鞋（£40-70，重要！）、运动服、水壶。教练可推荐适合孩子的装备。',
15, true, CURRENT_TIMESTAMP),

(16, 4, 'Can adults join the Chess or Badminton clubs?', '成人可以加入国际象棋或羽毛球俱乐部吗？',
'Yes! We welcome adult members to both clubs:

Chess Club:
- Adult sessions on Thursday evenings (7:00-9:00 PM)
- Open to all abilities from beginner to advanced
- Social chess and competitive tournament opportunities
- £140 per term (12 weeks)

Badminton Club:
- Adult sessions on Wednesday evenings (7:30-9:30 PM) and Sunday mornings (10:00 AM-12:00 PM)
- Mix of coaching, drills, and social play
- All abilities welcome
- £120 per term (10 weeks)

Please contact us to book a trial session.',
'欢迎成人！国际象棋：周四晚7-9点，适合所有水平，£140/学期。羽毛球：周三晚7:30-9:30和周日上午10-12点，£120/学期。请联系预约试训。',
16, true, CURRENT_TIMESTAMP),

(17, 5, 'Where are you located?', '地址在哪里？',
'Bowen Education Centre is located at:

1/F, 2A Curzon Road
Sale, Manchester
M33 7DR
United Kingdom

We are easily accessible:
- 5 minutes walk from Sale Metrolink station
- Free parking available on Curzon Road and nearby streets
- Bus routes 17, 18, and 263 stop nearby

Some events are held at alternative venues (e.g., Sale Water Park, Manchester Aquatics Centre) - check event details for specific locations.',
'地址：1/F, 2A Curzon Road, Sale, Manchester M33 7DR。距Sale轻轨站步行5分钟，周边免费停车，公交17、18、263路可达。',
17, true, CURRENT_TIMESTAMP),

(18, 5, 'What are your term dates?', '学期日期是什么时候？',
'Bowen Education follows a three-term academic year, roughly aligned with UK school terms:

2024-2025 Academic Year:
- Autumn Term: 7 September 2024 - 14 December 2024 (13 weeks)
  Half-term break: 21-29 October 2024
- Spring Term: 4 January 2025 - 5 April 2025 (13 weeks)
  Half-term break: 15-23 February 2025
- Summer Term: 26 April 2025 - 19 July 2025 (12 weeks)
  Half-term break: 24 May - 1 June 2025

Full term dates are available to download from our website. We are closed on all UK bank holidays.',
'秋季学期：9月-12月；春季学期：1月-4月；夏季学期：4月-7月。半学期休息和英国银行假日闭校。完整日期见官网下载。',
18, true, CURRENT_TIMESTAMP),

(19, 5, 'Do you offer online classes?', '提供在线课程吗？',
'We primarily offer in-person classes, as we believe face-to-face interaction provides the best learning experience, especially for young children.

However, we do offer online options in certain circumstances:
- One-to-one Chinese tutoring (by arrangement)
- A-Level subject tutoring (for students unable to attend in person)
- Makeup lessons if a student is isolating but well enough to learn

Online classes use Zoom and follow the same curriculum as in-person classes. Please contact us to discuss online learning options.',
'我们主要提供面授课程。但在特定情况下提供在线选项：一对一中文辅导、A-Level科目辅导、隔离期间的补课。在线课程使用Zoom。',
19, true, CURRENT_TIMESTAMP),

(20, 5, 'How can I contact Bowen Education?', '如何联系博文集团？',
'You can reach us through multiple channels:

Phone: +44 (0)161 6672668
Email: info@boweneducation.org
WhatsApp: +44 7912 345 678
WeChat: Scan QR code on our website

Office Hours:
Monday - Friday: 9:00 AM - 6:00 PM
Saturday: 9:00 AM - 5:00 PM
Sunday: 9:00 AM - 3:00 PM (Term Time Only)

You can also use the contact form on our website. We aim to respond to all inquiries within 24 hours on working days.',
'电话：+44 (0)161 6672668；邮箱：info@boweneducation.org；WhatsApp：+44 7912 345 678；微信：扫描官网二维码。工作时间：周一至周五9-18点，周六9-17点，周日9-15点（学期期间）。',
20, true, CURRENT_TIMESTAMP);

-- Continue with remaining tables...

-- ============================================================
-- 13. VIDEO CATEGORIES (video_category table)
-- ============================================================

INSERT INTO video_category (id, name, name_chinese, slug, sort_order, is_published, created_at) VALUES
(1, 'Teaching Videos', '教学视频', 'teaching', 1, true, CURRENT_TIMESTAMP),
(2, 'Event Highlights', '活动集锦', 'events', 2, true, CURRENT_TIMESTAMP),
(3, 'Student Works', '学生作品', 'student-works', 3, true, CURRENT_TIMESTAMP);

-- ============================================================
-- 14. VIDEOS (video table) - 10 Videos
-- ============================================================

INSERT INTO video (id, category_id, title, title_chinese, slug, description, video_url, duration_seconds, thumbnail, views, is_featured, is_published, published_at, created_at) VALUES
(1, 1, 'Teaching Mandarin Pronunciation - Four Tones Guide', '普通话发音教学 - 四声指南', 'mandarin-four-tones-guide',
'Learn the four Mandarin tones with our experienced teacher Miss Wang. Perfect for parents helping children with homework or beginners starting their Chinese learning journey. This comprehensive guide covers tone pronunciation, common mistakes, and practice exercises.',
'https://www.youtube.com/embed/example-tones-video', 480,
'/static/images/video-thumb-tones.jpg', 1250, true, true, '2024-09-15 10:00:00', CURRENT_TIMESTAMP),

(2, 1, 'Chinese Calligraphy Basics - Brush Technique', '书法基础 - 毛笔技巧', 'calligraphy-brush-technique',
'Master the fundamentals of Chinese calligraphy with expert instruction in brush handling, stroke order, and character formation. Suitable for beginners.',
'https://www.youtube.com/embed/example-calligraphy', 600,
'/static/images/video-thumb-calligraphy.jpg', 890, false, true, '2024-08-20 14:00:00', CURRENT_TIMESTAMP),

(3, 1, 'GCSE Chinese Exam Tips and Strategies', 'GCSE中文考试技巧与策略', 'gcse-chinese-exam-tips',
'Mrs. Chen shares essential exam tips and strategies for GCSE Chinese students. Learn how to maximize your marks in reading, writing, listening, and speaking papers.',
'https://www.youtube.com/embed/example-gcse-tips', 720,
'/static/images/video-thumb-gcse-tips.jpg', 1567, true, true, '2024-05-10 11:00:00', CURRENT_TIMESTAMP),

(4, 2, '2024 Chinese New Year Gala Highlights', '2024中国新年联欢晚会精彩集锦', 'cny-2024-highlights',
'Relive the magic of our 2024 Chinese New Year celebration with student performances, lion dance, and cultural activities. Over 300 attendees joined us for this spectacular event.',
'https://www.youtube.com/embed/example-cny-2024', 360,
'/static/images/video-thumb-cny-2024.jpg', 2340, true, true, '2024-02-12 16:00:00', CURRENT_TIMESTAMP),

(5, 2, 'Roots Journey to Henan 2024 - Video Diary', '2024河南寻根之旅 - 视频日记', 'henan-trip-2024-diary',
'Follow our students on their unforgettable cultural heritage trip to Henan Province. Experience Shaolin Temple, Longmen Grottoes, and authentic Chinese culture.',
'https://www.youtube.com/embed/example-henan-trip', 540,
'/static/images/video-thumb-henan-trip.jpg', 1823, true, true, '2024-08-30 12:00:00', CURRENT_TIMESTAMP),

(6, 2, 'Chess Tournament 2024 - Final Rounds', '2024国际象棋锦标赛 - 决赛轮', 'chess-tournament-finals-2024',
'Watch the exciting final rounds of our 2024 Autumn Chess Tournament featuring our top junior players competing for championship titles.',
'https://www.youtube.com/embed/example-chess-finals', 420,
'/static/images/video-thumb-chess-finals.jpg', 678, false, true, '2024-10-02 15:00:00', CURRENT_TIMESTAMP),

(7, 3, 'Student Performance: Traditional Chinese Song', '学生表演：中国传统歌曲', 'student-chinese-song',
'Beautiful performance of traditional Chinese song "Jasmine Flower" (茉莉花) by our Foundation Mandarin class students at the Spring Concert.',
'https://www.youtube.com/embed/example-student-song', 180,
'/static/images/video-thumb-student-song.jpg', 1120, false, true, '2024-03-25 17:00:00', CURRENT_TIMESTAMP),

(8, 1, 'Teaching Chinese Characters - Stroke Order Secrets', '教授汉字 - 笔顺秘诀', 'chinese-characters-stroke-order',
'Learn the fundamental rules of Chinese character stroke order that make writing easier and more authentic. Essential for all Chinese learners.',
'https://www.youtube.com/embed/example-stroke-order', 450,
'/static/images/video-thumb-stroke-order.jpg', 945, false, true, '2024-06-18 13:00:00', CURRENT_TIMESTAMP),

(9, 2, 'HAF Summer Programme 2024 Highlights', 'HAF 2024夏季项目集锦', 'haf-summer-2024-highlights',
'Highlights from our 2024 HAF (Holiday Activities and Food) summer programme in partnership with Manchester City Council. See the fun activities and happy children!',
'https://www.youtube.com/embed/example-haf-2024', 300,
'/static/images/video-thumb-haf-2024.jpg', 756, false, true, '2024-08-26 14:00:00', CURRENT_TIMESTAMP),

(10, 3, 'Parent Testimonials - Why We Chose Bowen', '家长见证 - 我们为什么选择博文', 'parent-testimonials',
'Hear from parents about their experiences with Bowen Education and why they trust us with their children''s education.',
'https://www.youtube.com/embed/example-testimonials', 420,
'/static/images/video-thumb-testimonials.jpg', 1534, true, true, '2024-09-05 11:00:00', CURRENT_TIMESTAMP);

-- ============================================================
-- 15. FILE CATEGORIES (file_category table)
-- ============================================================

INSERT INTO file_category (id, name, name_chinese, slug, sort_order, is_published, created_at) VALUES
(1, 'Term Dates', '学期日期', 'term-dates', 1, true, CURRENT_TIMESTAMP),
(2, 'Course Brochures', '课程手册', 'brochures', 2, true, CURRENT_TIMESTAMP),
(3, 'Policy Documents', '政策文件', 'policies', 3, true, CURRENT_TIMESTAMP),
(4, 'Enrollment Forms', '报名表格', 'forms', 4, true, CURRENT_TIMESTAMP),
(5, 'Learning Resources', '学习资料', 'resources', 5, true, CURRENT_TIMESTAMP);

-- ============================================================
-- 16. DOWNLOADABLE FILES (downloadable_file table) - 12 Files
-- ============================================================

INSERT INTO downloadable_file (id, category_id, title, title_chinese, slug, description, file_path, file_name, file_size_kb, file_type, download_count, is_public, requires_login, is_published, uploaded_at, created_at) VALUES
(1, 1, 'School Term Dates 2024-2025', '学期日期 2024-2025', 'term-dates-2024-2025',
'Official Bowen Chinese School and Tuition Centre term dates for academic year 2024-2025, including start dates, half-term breaks, and holiday closures.',
'/static/downloads/bowen-term-dates-2024-2025.pdf', 'bowen-term-dates-2024-2025.pdf', 250, 'PDF', 456, true, false, true, '2024-07-01 10:00:00', CURRENT_TIMESTAMP),

(2, 1, 'School Term Dates 2025-2026', '学期日期 2025-2026', 'term-dates-2025-2026',
'Official term dates for academic year 2025-2026.',
'/static/downloads/bowen-term-dates-2025-2026.pdf', 'bowen-term-dates-2025-2026.pdf', 248, 'PDF', 89, true, false, true, '2024-05-15 10:00:00', CURRENT_TIMESTAMP),

(3, 2, 'Chinese School Prospectus 2024', '中文学校招生简章 2024', 'chinese-school-prospectus-2024',
'Comprehensive guide to Bowen Chinese School including curriculum, course levels, teachers, facilities, exam preparation, fees, and enrollment information. Essential reading for prospective parents.',
'/static/downloads/chinese-school-prospectus-2024.pdf', 'chinese-school-prospectus-2024.pdf', 2500, 'PDF', 789, true, false, true, '2024-08-01 09:00:00', CURRENT_TIMESTAMP),

(4, 2, 'Tuition Centre Course Guide 2024', '补习中心课程指南 2024', 'tuition-centre-guide-2024',
'Complete guide to GCSE and A-Level tuition courses, including subject offerings, teaching methods, success rates, and enrollment details.',
'/static/downloads/tuition-centre-guide-2024.pdf', 'tuition-centre-guide-2024.pdf', 1800, 'PDF', 432, true, false, true, '2024-08-01 09:00:00', CURRENT_TIMESTAMP),

(5, 2, 'Chess & Badminton Clubs Brochure', '国际象棋与羽毛球俱乐部手册', 'clubs-brochure-2024',
'Information about our ECF-registered Chess Club and Badminton Club, including training schedules, coaching staff, membership fees, and competition opportunities.',
'/static/downloads/clubs-brochure-2024.pdf', 'clubs-brochure-2024.pdf', 1200, 'PDF', 267, true, false, true, '2024-08-15 10:00:00', CURRENT_TIMESTAMP),

(6, 3, 'Safeguarding and Child Protection Policy', '儿童保护政策', 'safeguarding-policy',
'Bowen Education Group''s comprehensive safeguarding and child protection policy. Updated November 2024. All parents and staff should read this document.',
'/static/downloads/safeguarding-policy-2024.pdf', 'safeguarding-policy-2024.pdf', 800, 'PDF', 534, true, false, true, '2024-11-01 09:00:00', CURRENT_TIMESTAMP),

(7, 3, 'Privacy Policy and GDPR Compliance', '隐私政策与GDPR合规', 'privacy-policy',
'Our privacy policy explaining how we collect, use, and protect personal data in compliance with UK GDPR regulations.',
'/static/downloads/privacy-policy-2024.pdf', 'privacy-policy-2024.pdf', 650, 'PDF', 312, true, false, true, '2024-01-15 10:00:00', CURRENT_TIMESTAMP),

(8, 3, 'Terms and Conditions', '条款与条件', 'terms-and-conditions',
'Terms and conditions for enrollment at Bowen Education, including fees, refund policy, behavior expectations, and parent responsibilities.',
'/static/downloads/terms-and-conditions-2024.pdf', 'terms-and-conditions-2024.pdf', 580, 'PDF', 423, true, false, true, '2024-01-15 10:00:00', CURRENT_TIMESTAMP),

(9, 4, 'Enrollment Application Form', '报名申请表', 'enrollment-application-form',
'Complete this form to enroll your child at Bowen Education. Includes student information, course selection, medical information, and parent consent.',
'/static/downloads/enrollment-application-form.pdf', 'enrollment-application-form.pdf', 450, 'PDF', 678, true, false, true, '2024-07-01 09:00:00', CURRENT_TIMESTAMP),

(10, 4, 'Medical Information and Consent Form', '医疗信息与同意书', 'medical-consent-form',
'Mandatory form for all students providing medical information, emergency contacts, photo/video consent, and data processing consent.',
'/static/downloads/medical-consent-form.pdf', 'medical-consent-form.pdf', 380, 'PDF', 612, true, false, true, '2024-07-01 09:00:00', CURRENT_TIMESTAMP),

(11, 5, 'HSK Level 3 Sample Test Paper', 'HSK三级样题', 'hsk-3-sample-test',
'Official HSK Level 3 sample test paper for students preparing for the Chinese proficiency examination. Includes listening, reading, and writing sections.',
'/static/downloads/hsk-3-sample-test.pdf', 'hsk-3-sample-test.pdf', 1500, 'PDF', 234, true, false, true, '2024-05-20 10:00:00', CURRENT_TIMESTAMP),

(12, 5, 'Chinese Character Practice Sheets', '汉字练习册', 'character-practice-sheets',
'Downloadable practice sheets for learning Chinese characters. Includes stroke order guides and grid paper for writing practice. Suitable for all levels.',
'/static/downloads/character-practice-sheets.pdf', 'character-practice-sheets.pdf', 2200, 'PDF', 891, true, false, true, '2024-06-10 10:00:00', CURRENT_TIMESTAMP);

-- ============================================================
-- 17. BOOKING SERVICES (booking_service table)
-- ============================================================

INSERT INTO booking_service (id, name, name_chinese, slug, description, duration_minutes, is_active, created_at) VALUES
(1, 'Chinese School Consultation', '中文学校咨询', 'chinese-school-consultation',
'Book a free 30-minute consultation to discuss your child''s Chinese language learning needs. We''ll assess their current level, recommend suitable courses, and answer all your questions.',
30, true, CURRENT_TIMESTAMP),

(2, 'Tuition Centre Trial Lesson', '补习中心试听课', 'tuition-trial-lesson',
'Book a free 60-minute trial GCSE or A-Level tuition session. Your child will experience our teaching methods and meet our tutors before committing to enrollment.',
60, true, CURRENT_TIMESTAMP),

(3, 'Chess Club Assessment', '国际象棋俱乐部评估', 'chess-assessment',
'Free 45-minute chess skill assessment for new members. Our coaches will evaluate your child''s playing level and recommend the most suitable class.',
45, true, CURRENT_TIMESTAMP),

(4, 'Badminton Club Trial Session', '羽毛球俱乐部试训', 'badminton-trial',
'Free 60-minute trial badminton session. Experience our coaching style, meet our team, and see if our club is the right fit for you.',
60, true, CURRENT_TIMESTAMP),

(5, 'General Enquiry Appointment', '一般咨询预约', 'general-enquiry',
'Book a 30-minute appointment to discuss any aspect of Bowen Education''s services, ask questions, or arrange a campus visit.',
30, true, CURRENT_TIMESTAMP);

-- ============================================================
-- 18. CUSTOM FIELD DEFINITIONS (custom_field_definition table)
-- ============================================================

INSERT INTO custom_field_definition (id, name, name_chinese, slug, field_type, field_options, applies_to_entity, is_required, display_order, created_at) VALUES
(1, 'Age Range', '年龄范围', 'age_range', 'text', NULL, 'product', false, 1, CURRENT_TIMESTAMP),
(2, 'Level', '级别', 'level', 'select', '["Beginner","Intermediate","Advanced","GCSE","A-Level","Exam Prep"]', 'product', false, 2, CURRENT_TIMESTAMP),
(3, 'Class Size', '班级规模', 'class_size', 'text', NULL, 'product', false, 3, CURRENT_TIMESTAMP),
(4, 'Duration', '课程时长', 'duration', 'text', NULL, 'product', true, 4, CURRENT_TIMESTAMP),
(5, 'Schedule', '上课时间', 'schedule', 'text', NULL, 'product', true, 5, CURRENT_TIMESTAMP),
(6, 'Textbook', '教材', 'textbook', 'text', NULL, 'product', false, 6, CURRENT_TIMESTAMP),
(7, 'Exam Preparation', '考试准备', 'exam_prep', 'text', NULL, 'product', false, 7, CURRENT_TIMESTAMP),
(8, 'Teacher', '授课教师', 'teacher', 'text', NULL, 'product', false, 8, CURRENT_TIMESTAMP);

-- ============================================================
-- 19. CUSTOM FIELD VALUES (custom_field_value table)
-- Sample values for first 5 products
-- ============================================================

INSERT INTO custom_field_value (id, custom_field_id, entity_type, entity_id, field_value, created_at) VALUES
-- Product 1: Foundation Mandarin
(1, 1, 'product', 1, '5-7 years', CURRENT_TIMESTAMP),
(2, 2, 'product', 1, 'Beginner', CURRENT_TIMESTAMP),
(3, 3, 'product', 1, 'Max 12 students', CURRENT_TIMESTAMP),
(4, 4, 'product', 1, 'Full academic year (3 terms, 30 weeks)', CURRENT_TIMESTAMP),
(5, 5, 'product', 1, 'Saturdays 10:00-12:00', CURRENT_TIMESTAMP),
(6, 6, 'product', 1, 'Happy Chinese (Kuaile Hanyu) Book 1', CURRENT_TIMESTAMP),
(7, 7, 'product', 1, 'None', CURRENT_TIMESTAMP),
(8, 8, 'product', 1, 'Miss Wang Mei-Ling', CURRENT_TIMESTAMP),

-- Product 2: Intermediate Mandarin
(9, 1, 'product', 2, '8-10 years', CURRENT_TIMESTAMP),
(10, 2, 'product', 2, 'Intermediate', CURRENT_TIMESTAMP),
(11, 3, 'product', 2, 'Max 12 students', CURRENT_TIMESTAMP),
(12, 4, 'product', 2, 'Full academic year (3 terms, 30 weeks)', CURRENT_TIMESTAMP),
(13, 5, 'product', 2, 'Saturdays 12:30-14:30', CURRENT_TIMESTAMP),
(14, 6, 'product', 2, 'Chinese Made Easy Book 2', CURRENT_TIMESTAMP),
(15, 7, 'product', 2, 'YCT Level 2-3', CURRENT_TIMESTAMP),
(16, 8, 'product', 2, 'Mr. Liu Wei', CURRENT_TIMESTAMP),

-- Product 3: Advanced Mandarin
(17, 1, 'product', 3, '11-13 years', CURRENT_TIMESTAMP),
(18, 2, 'product', 3, 'Advanced', CURRENT_TIMESTAMP),
(19, 3, 'product', 3, 'Max 10 students', CURRENT_TIMESTAMP),
(20, 4, 'product', 3, 'Full academic year (3 terms, 30 weeks)', CURRENT_TIMESTAMP),
(21, 5, 'product', 3, 'Saturdays 14:45-16:45', CURRENT_TIMESTAMP),
(22, 6, 'product', 3, 'Chinese Made Easy Book 3-4', CURRENT_TIMESTAMP),
(23, 7, 'product', 3, 'YCT Level 4, HSK Level 3-4', CURRENT_TIMESTAMP),
(24, 8, 'product', 3, 'Emily Chen', CURRENT_TIMESTAMP),

-- Product 4: GCSE Chinese
(25, 1, 'product', 4, '14-16 years', CURRENT_TIMESTAMP),
(26, 2, 'product', 4, 'GCSE', CURRENT_TIMESTAMP),
(27, 3, 'product', 4, 'Max 12 students', CURRENT_TIMESTAMP),
(28, 4, 'product', 4, '2-year programme (6 terms)', CURRENT_TIMESTAMP),
(29, 5, 'product', 4, 'Saturdays 10:00-12:30', CURRENT_TIMESTAMP),
(30, 6, 'product', 4, 'Edexcel GCSE Chinese Student Book + AQA Past Papers', CURRENT_TIMESTAMP),
(31, 7, 'product', 4, 'GCSE Chinese (Edexcel 1CN0 / AQA 8673)', CURRENT_TIMESTAMP),
(32, 8, 'product', 4, 'Mrs. Chen Xiao-Ying', CURRENT_TIMESTAMP),

-- Product 5: A-Level Chinese
(33, 1, 'product', 5, '16-18 years', CURRENT_TIMESTAMP),
(34, 2, 'product', 5, 'A-Level', CURRENT_TIMESTAMP),
(35, 3, 'product', 5, 'Max 8 students', CURRENT_TIMESTAMP),
(36, 4, 'product', 5, '2-year programme (6 terms)', CURRENT_TIMESTAMP),
(37, 5, 'product', 5, 'Saturdays 13:00-15:30', CURRENT_TIMESTAMP),
(38, 6, 'product', 5, 'Edexcel A-Level Chinese + Contemporary Chinese Texts', CURRENT_TIMESTAMP),
(39, 7, 'product', 5, 'A-Level Chinese (Edexcel / AQA)', CURRENT_TIMESTAMP),
(40, 8, 'product', 5, 'Mrs. Chen Xiao-Ying', CURRENT_TIMESTAMP);

-- Additional custom field values can be added for remaining products...

-- ============================================================
-- Re-enable foreign key checks
-- ============================================================

SET session_replication_role = DEFAULT;

-- ============================================================
-- DATABASE SEED COMPLETE
-- ============================================================

-- Total Records Inserted:
-- - Site Settings: 1
-- - Site Columns: 11
-- - Product Categories: 4
-- - Products: 22
-- - Team Departments: 5
-- - Team Members: 12
-- - Post Categories: 5
-- - Posts: 15
-- - Event Categories: 8
-- - Events: 10
-- - FAQ Categories: 5
-- - FAQs: 20
-- - Video Categories: 3
-- - Videos: 10
-- - File Categories: 5
-- - Downloadable Files: 12
-- - Booking Services: 5
-- - Custom Field Definitions: 8
-- - Custom Field Values: 40 (sample)
--
-- TOTAL: 201+ records

-- ============================================================
-- END OF SEED DATA
-- ============================================================
