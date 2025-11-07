PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('21fd3e69434b');
CREATE TABLE booking_service (
	name VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	description TEXT, 
	duration_minutes INTEGER NOT NULL, 
	price FLOAT, 
	buffer_time_minutes INTEGER NOT NULL, 
	max_capacity INTEGER NOT NULL, 
	allow_waitlist BOOLEAN NOT NULL, 
	min_advance_hours INTEGER NOT NULL, 
	max_advance_days INTEGER NOT NULL, 
	allow_cancel_hours INTEGER NOT NULL, 
	working_days VARCHAR(100), 
	working_start_time TIME, 
	working_end_time TIME, 
	is_active BOOLEAN NOT NULL, 
	sort_order INTEGER NOT NULL, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO booking_service VALUES('Free Trial Class (Chinese School)','trial-class-chinese','Book a free 45-minute trial class for your child to experience our Chinese School programme',45,0.0,15,8,1,24,30,24,NULL,NULL,NULL,1,1,NULL,1,'2025-11-04 21:58:23.631751','2025-11-04 21:58:23.631756');
INSERT INTO booking_service VALUES('Parent Consultation','parent-consultation','One-on-one consultation with our education team to discuss your child''s learning needs',30,0.0,10,1,0,48,14,48,NULL,NULL,NULL,1,2,NULL,2,'2025-11-04 21:58:23.631757','2025-11-04 21:58:23.631758');
CREATE TABLE faq (
	category VARCHAR(100), 
	question VARCHAR(500) NOT NULL, 
	answer TEXT NOT NULL, 
	sort_order INTEGER NOT NULL, 
	is_visible BOOLEAN NOT NULL, 
	is_pinned BOOLEAN NOT NULL, 
	view_count INTEGER NOT NULL, 
	helpful_count INTEGER NOT NULL, 
	unhelpful_count INTEGER NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO faq VALUES('Enrolment','How do I enroll my child in Chinese School?','<p>You can enroll your child by filling out our online registration form or visiting our centre in person. We offer a free trial class so your child can experience our teaching approach before committing to a term.</p>',1,1,1,0,0,0,1,'2025-11-04 21:58:23.546012','2025-11-04 21:58:23.546016');
INSERT INTO faq VALUES('Courses','What is the difference between HSK and YCT examinations?','<p>HSK (Hanyu Shuiping Kaoshi) is the standardized Chinese proficiency test for adults, while YCT (Youth Chinese Test) is designed specifically for young learners aged 15 and under. YCT has a more age-appropriate vocabulary and testing format.</p>',2,1,0,0,0,0,2,'2025-11-04 21:58:23.546018','2025-11-04 21:58:23.546019');
INSERT INTO faq VALUES('Fees & Payment','What are your fees and payment terms?','<p>Our fees are charged per term (12 weeks). Payment is due at the start of each term. We accept bank transfer, card payments, and cash. Sibling discounts of 10% are available for families enrolling multiple children.</p>',3,1,0,0,0,0,3,'2025-11-04 21:58:23.546021','2025-11-04 21:58:23.546022');
CREATE TABLE faq_category (
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	description TEXT, 
	icon VARCHAR(50), 
	sort_order INTEGER NOT NULL, 
	is_visible BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (slug)
);
INSERT INTO faq_category VALUES('Enrolment','enrolment',NULL,NULL,1,1,1,'2025-11-04 21:58:23.525812','2025-11-04 21:58:23.525816');
INSERT INTO faq_category VALUES('Courses','courses',NULL,NULL,2,1,2,'2025-11-04 21:58:23.525818','2025-11-04 21:58:23.525818');
INSERT INTO faq_category VALUES('Fees & Payment','fees-payment',NULL,NULL,3,1,3,'2025-11-04 21:58:23.525819','2025-11-04 21:58:23.525820');
INSERT INTO faq_category VALUES('Facilities','facilities',NULL,NULL,4,1,4,'2025-11-04 21:58:23.525820','2025-11-04 21:58:23.525821');
CREATE TABLE file_category (
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	description TEXT, 
	parent_id INTEGER, 
	icon_class VARCHAR(50), 
	sort_order INTEGER NOT NULL, 
	is_visible BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_id) REFERENCES file_category (id)
);
INSERT INTO file_category VALUES('Enrolment Forms','enrolment',NULL,NULL,NULL,1,1,1,'2025-11-04 21:58:23.608652','2025-11-04 21:58:23.608657');
INSERT INTO file_category VALUES('Course Materials','course-materials',NULL,NULL,NULL,2,1,2,'2025-11-04 21:58:23.608659','2025-11-04 21:58:23.608660');
INSERT INTO file_category VALUES('Policies','policies',NULL,NULL,NULL,3,1,3,'2025-11-04 21:58:23.608661','2025-11-04 21:58:23.608661');
CREATE TABLE media_file (
	filename_original VARCHAR(255) NOT NULL, 
	mime_type VARCHAR(100) NOT NULL, 
	size_bytes INTEGER NOT NULL, 
	width INTEGER, 
	height INTEGER, 
	path_original VARCHAR(500) NOT NULL, 
	path_medium VARCHAR(500), 
	path_thumb VARCHAR(500), 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO media_file VALUES('course-a-level-chinese.jpg','image/jpeg',114733,NULL,NULL,'/static/images/course-a-level-chinese.jpg','/static/images/course-a-level-chinese.jpg','/static/images/course-a-level-chinese.jpg',1,'2025-11-04 22:53:59.654814','2025-11-04 22:53:59.654818');
INSERT INTO media_file VALUES('course-cantonese.jpg','image/jpeg',125491,NULL,NULL,'/static/images/course-cantonese.jpg','/static/images/course-cantonese.jpg','/static/images/course-cantonese.jpg',2,'2025-11-04 22:53:59.654818','2025-11-04 22:53:59.654819');
INSERT INTO media_file VALUES('course-foundation-mandarin.jpg','image/jpeg',129900,NULL,NULL,'/static/images/course-foundation-mandarin.jpg','/static/images/course-foundation-mandarin.jpg','/static/images/course-foundation-mandarin.jpg',3,'2025-11-04 22:53:59.654819','2025-11-04 22:53:59.654821');
INSERT INTO media_file VALUES('course-gcse-chinese.jpg','image/jpeg',115996,NULL,NULL,'/static/images/course-gcse-chinese.jpg','/static/images/course-gcse-chinese.jpg','/static/images/course-gcse-chinese.jpg',4,'2025-11-04 22:53:59.654822','2025-11-04 22:53:59.654823');
INSERT INTO media_file VALUES('course-hsk-level-3.jpg','image/jpeg',112926,NULL,NULL,'/static/images/course-hsk-level-3.jpg','/static/images/course-hsk-level-3.jpg','/static/images/course-hsk-level-3.jpg',5,'2025-11-04 22:53:59.654823','2025-11-04 22:53:59.654824');
INSERT INTO media_file VALUES('hero-chess-club.jpg','image/jpeg',121566,NULL,NULL,'/static/images/hero-chess-club.jpg','/static/images/hero-chess-club.jpg','/static/images/hero-chess-club.jpg',6,'2025-11-04 22:53:59.654824','2025-11-04 22:53:59.654824');
INSERT INTO media_file VALUES('hero-chinese-new-year.jpg','image/jpeg',206766,NULL,NULL,'/static/images/hero-chinese-new-year.jpg','/static/images/hero-chinese-new-year.jpg','/static/images/hero-chinese-new-year.jpg',7,'2025-11-04 22:53:59.654825','2025-11-04 22:53:59.654825');
INSERT INTO media_file VALUES('hero-chinese-school.jpg','image/jpeg',110187,NULL,NULL,'/static/images/hero-chinese-school.jpg','/static/images/hero-chinese-school.jpg','/static/images/hero-chinese-school.jpg',8,'2025-11-04 22:53:59.654825','2025-11-04 22:53:59.654826');
INSERT INTO media_file VALUES('hero-haf-programme.jpg','image/jpeg',119878,NULL,NULL,'/static/images/hero-haf-programme.jpg','/static/images/hero-haf-programme.jpg','/static/images/hero-haf-programme.jpg',9,'2025-11-04 22:53:59.654826','2025-11-04 22:53:59.654826');
INSERT INTO media_file VALUES('hero-henan-university.jpg','image/jpeg',107905,NULL,NULL,'/static/images/hero-henan-university.jpg','/static/images/hero-henan-university.jpg','/static/images/hero-henan-university.jpg',10,'2025-11-04 22:53:59.654827','2025-11-04 22:53:59.654827');
INSERT INTO media_file VALUES('henan-university-partnership.jpg','image/jpeg',84714,NULL,NULL,'/static/images/news/henan-university-partnership.jpg','/static/images/news/henan-university-partnership.jpg','/static/images/news/henan-university-partnership.jpg',11,'2025-11-05 10:38:18','2025-11-05 10:38:18');
INSERT INTO media_file VALUES('2024-autumn-term-enrollment.jpg','image/jpeg',119053,NULL,NULL,'/static/images/news/2024-autumn-term-enrollment.jpg','/static/images/news/2024-autumn-term-enrollment.jpg','/static/images/news/2024-autumn-term-enrollment.jpg',12,'2025-11-05 10:38:18','2025-11-05 10:38:18');
INSERT INTO media_file VALUES('haf-programme-success-2024.jpg','image/jpeg',103873,NULL,NULL,'/static/images/news/haf-programme-success-2024.jpg','/static/images/news/haf-programme-success-2024.jpg','/static/images/news/haf-programme-success-2024.jpg',13,'2025-11-05 10:38:18','2025-11-05 10:38:18');
INSERT INTO media_file VALUES('chess-club-tournament-achievements.jpg','image/jpeg',135090,NULL,NULL,'/static/images/news/chess-club-tournament-achievements.jpg','/static/images/news/chess-club-tournament-achievements.jpg','/static/images/news/chess-club-tournament-achievements.jpg',14,'2025-11-05 10:38:18','2025-11-05 10:38:18');
INSERT INTO media_file VALUES('news-hero-background.jpg','image/jpeg',85797,NULL,NULL,'/static/images/news/news-hero-background.jpg','/static/images/news/news-hero-background.jpg','/static/images/news/news-hero-background.jpg',15,'2025-11-05 10:38:18','2025-11-05 10:38:18');
CREATE TABLE newsletter_campaign (
	name VARCHAR(200) NOT NULL, 
	subject VARCHAR(200) NOT NULL, 
	preview_text VARCHAR(255), 
	content_html TEXT NOT NULL, 
	content_text TEXT, 
	status VARCHAR(9) NOT NULL, 
	scheduled_at DATETIME, 
	sent_at DATETIME, 
	target_groups VARCHAR(255), 
	target_all BOOLEAN NOT NULL, 
	total_recipients INTEGER NOT NULL, 
	total_sent INTEGER NOT NULL, 
	total_failed INTEGER NOT NULL, 
	total_opened INTEGER NOT NULL, 
	total_clicked INTEGER NOT NULL, 
	total_unsubscribed INTEGER NOT NULL, 
	total_bounced INTEGER NOT NULL, 
	from_name VARCHAR(100), 
	from_email VARCHAR(100), 
	reply_to_email VARCHAR(100), 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE newsletter_subscriber (
	email VARCHAR(100) NOT NULL, 
	first_name VARCHAR(50), 
	last_name VARCHAR(50), 
	status VARCHAR(12) NOT NULL, 
	is_verified BOOLEAN NOT NULL, 
	subscription_source VARCHAR(100), 
	subscription_ip VARCHAR(50), 
	subscribed_at DATETIME, 
	unsubscribed_at DATETIME, 
	unsubscribe_reason TEXT, 
	group_tags VARCHAR(255), 
	total_emails_sent INTEGER NOT NULL, 
	total_emails_opened INTEGER NOT NULL, 
	total_links_clicked INTEGER NOT NULL, 
	last_email_sent_at DATETIME, 
	last_email_opened_at DATETIME, 
	preferred_language VARCHAR(10), 
	email_frequency VARCHAR(7) NOT NULL, 
	notes TEXT, 
	bounce_count INTEGER NOT NULL, 
	complaint_count INTEGER NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
CREATE TABLE portfolio_category (
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	description TEXT, 
	sort_order INTEGER NOT NULL, 
	is_visible BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (slug)
);
CREATE TABLE site_column (
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	column_type VARCHAR(11) NOT NULL, 
	parent_id INTEGER, 
	icon VARCHAR(50), 
	sort_order INTEGER NOT NULL, 
	show_in_nav BOOLEAN NOT NULL, 
	is_enabled BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, menu_location VARCHAR(20) NOT NULL DEFAULT 'header', 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_id) REFERENCES site_column (id), 
	UNIQUE (slug)
);
INSERT INTO site_column VALUES('首页','home','CUSTOM',NULL,NULL,1,1,1,1,'2025-11-04 21:58:23.384980','2025-11-05 02:27:06.860060','HEADER');
INSERT INTO site_column VALUES('博文集团','about','SINGLE_PAGE',NULL,NULL,2,1,1,2,'2025-11-04 21:58:23.384983','2025-11-04 21:58:23.384983','HEADER');
INSERT INTO site_column VALUES('中文学校','school','CUSTOM',NULL,NULL,4,1,1,3,'2025-11-04 21:58:23.384984','2025-11-05 06:02:28.491805','HEADER');
INSERT INTO site_column VALUES('补习中心','tuition','PRODUCT',NULL,NULL,5,1,1,4,'2025-11-04 21:58:23.384984','2025-11-05 02:27:32.968280','HEADER');
INSERT INTO site_column VALUES('国际象棋俱乐部','chess','CUSTOM',NULL,NULL,6,1,1,5,'2025-11-04 21:58:23.384985','2025-11-05 02:27:32.968280','HEADER');
INSERT INTO site_column VALUES('政府项目','programmes','CUSTOM',NULL,NULL,8,1,1,6,'2025-11-04 21:58:23.384985','2025-11-05 02:27:32.968281','HEADER');
INSERT INTO site_column VALUES('博文活动','events','CUSTOM',NULL,NULL,9,1,1,7,'2025-11-04 21:58:23.384986','2025-11-05 02:27:32.968283','HEADER');
INSERT INTO site_column VALUES('博文新闻','news','POST',NULL,NULL,3,1,1,8,'2025-11-04 21:58:23.384986','2025-11-05 02:27:32.968284','HEADER');
INSERT INTO site_column VALUES('图库','gallery','CUSTOM',NULL,NULL,9,0,1,9,'2025-11-04 21:58:23.384987','2025-11-05 01:10:21.172421','FOOTER');
INSERT INTO site_column VALUES('常见问题','faq','CUSTOM',NULL,NULL,10,0,1,10,'2025-11-04 21:58:23.384987','2025-11-05 01:10:21.172423','FOOTER');
INSERT INTO site_column VALUES('联系我们','contact','SINGLE_PAGE',NULL,NULL,10,1,1,11,'2025-11-04 21:58:23.384988','2025-11-05 01:09:49.165359','HEADER');
INSERT INTO site_column VALUES('羽毛球俱乐部','badminton','CUSTOM',NULL,NULL,7,1,1,12,'2025-11-05 01:09:49.166605','2025-11-05 02:27:32.968284','HEADER');
INSERT INTO site_column VALUES('课程设置','school-curriculum','PRODUCT',3,NULL,1,0,1,13,'2025-11-05 06:02:28.512109','2025-11-05 06:02:28.512112','HEADER');
INSERT INTO site_column VALUES('学期日期','school-term-dates','SINGLE_PAGE',3,NULL,2,0,1,14,'2025-11-05 06:02:28.513188','2025-11-05 06:02:28.513190','HEADER');
INSERT INTO site_column VALUES('PTA家长教师协会','school-pta','SINGLE_PAGE',3,NULL,3,0,1,15,'2025-11-05 06:02:28.513956','2025-11-05 06:02:28.513957','HEADER');
INSERT INTO site_column VALUES('我们的比赛','chess-competitions','POST',5,NULL,1,0,1,16,'2025-11-05 06:02:28.514732','2025-11-05 06:02:28.514733','HEADER');
INSERT INTO site_column VALUES('棋手信息','chess-players','SINGLE_PAGE',5,NULL,2,0,1,17,'2025-11-05 06:02:28.515467','2025-11-05 06:02:28.515468','HEADER');
INSERT INTO site_column VALUES('相册','chess-gallery','CUSTOM',5,NULL,3,0,1,18,'2025-11-05 06:02:28.516193','2025-11-05 06:02:28.516195','HEADER');
INSERT INTO site_column VALUES('赛事活动','badminton-events','POST',12,NULL,1,0,1,19,'2025-11-05 06:02:28.516923','2025-11-05 06:02:28.516924','HEADER');
INSERT INTO site_column VALUES('训练时间表','badminton-schedule','SINGLE_PAGE',12,NULL,2,0,1,20,'2025-11-05 06:02:28.517638','2025-11-05 06:02:28.517639','HEADER');
INSERT INTO site_column VALUES('精彩瞬间','badminton-gallery','CUSTOM',12,NULL,3,0,1,21,'2025-11-05 06:02:28.518324','2025-11-05 06:02:28.518325','HEADER');
INSERT INTO site_column VALUES('HAF项目','programmes-haf','SINGLE_PAGE',6,NULL,1,0,1,22,'2025-11-05 06:02:28.519031','2025-11-05 06:02:28.519033','HEADER');
INSERT INTO site_column VALUES('公园活动','programmes-parks','POST',6,NULL,2,0,1,23,'2025-11-05 06:02:28.519708','2025-11-05 06:02:28.519709','HEADER');
INSERT INTO site_column VALUES('河南大学合作','events-henan','SINGLE_PAGE',7,NULL,1,0,1,24,'2025-11-05 06:02:28.520273','2025-11-05 06:02:28.520274','HEADER');
CREATE TABLE site_setting (
	setting_key VARCHAR(100) NOT NULL, 
	value_text TEXT NOT NULL, 
	value_type VARCHAR(6) NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (setting_key)
);
INSERT INTO site_setting VALUES('site_name','Bowen Education Group','string',1,'2025-11-04 21:58:23.365500','2025-11-04 21:58:23.365503');
INSERT INTO site_setting VALUES('site_name_chinese','博文集团','string',2,'2025-11-04 21:58:23.365504','2025-11-04 21:58:23.365504');
INSERT INTO site_setting VALUES('tagline','Bridging East and West Through Education','string',3,'2025-11-04 21:58:23.365505','2025-11-04 21:58:23.365507');
INSERT INTO site_setting VALUES('tagline_chinese','中西融汇，博学致远','string',4,'2025-11-04 21:58:23.365508','2025-11-04 21:58:23.365508');
INSERT INTO site_setting VALUES('company_phone','+44 (0)161 6672668','string',5,'2025-11-04 21:58:23.365509','2025-11-04 21:58:23.365509');
INSERT INTO site_setting VALUES('company_email','info@boweneducation.org','string',6,'2025-11-04 21:58:23.365509','2025-11-04 21:58:23.365510');
INSERT INTO site_setting VALUES('company_address','1/F, 2A Curzon Road, Sale, Manchester, M33 7DR, UK','string',7,'2025-11-04 21:58:23.365510','2025-11-04 21:58:23.365510');
INSERT INTO site_setting VALUES('company_wechat','bowenedu_uk','string',8,'2025-11-04 21:58:23.365511','2025-11-04 21:58:23.365511');
INSERT INTO site_setting VALUES('founded_year','2018','string',9,'2025-11-04 21:58:23.365511','2025-11-04 21:58:23.365511');
INSERT INTO site_setting VALUES('business_hours','Monday - Friday: 9:00 - 17:00, Saturday - Sunday: 10:00 - 16:00','string',10,'2025-11-04 21:58:23.365512','2025-11-04 21:58:23.365512');
INSERT INTO site_setting VALUES('mission','To provide high-quality Chinese language education and cultural enrichment programmes that bridge Eastern and Western educational traditions, empowering students to succeed in a globalised world.','string',11,'2025-11-04 21:58:23.365512','2025-11-04 21:58:23.365513');
INSERT INTO site_setting VALUES('vision','To be the leading Chinese education provider in Greater Manchester, recognised for academic excellence, cultural authenticity, and community impact.','string',12,'2025-11-04 21:58:23.365513','2025-11-04 21:58:23.365513');
INSERT INTO site_setting VALUES('about_description','Bowen Education Group is a registered educational institution in Manchester, UK, offering comprehensive Chinese language programmes from Foundation to A-Level, academic tutoring, chess club, badminton club, and government-funded community programmes.','string',13,'2025-11-04 21:58:23.365513','2025-11-04 21:58:23.365514');
CREATE TABLE user (
	username VARCHAR(100) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
	phone VARCHAR(50), 
	password_hash VARCHAR(255) NOT NULL, 
	first_name VARCHAR(50), 
	last_name VARCHAR(50), 
	display_name VARCHAR(100), 
	bio TEXT, 
	avatar_url VARCHAR(255), 
	date_of_birth DATETIME, 
	gender VARCHAR(17), 
	address_line1 VARCHAR(255), 
	address_line2 VARCHAR(255), 
	city VARCHAR(100), 
	state VARCHAR(100), 
	postal_code VARCHAR(20), 
	country VARCHAR(100), 
	role VARCHAR(6) NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	is_verified BOOLEAN NOT NULL, 
	is_staff BOOLEAN NOT NULL, 
	membership_level VARCHAR(8) NOT NULL, 
	membership_expires_at DATETIME, 
	points INTEGER NOT NULL, 
	total_earned_points INTEGER NOT NULL, 
	last_login_at DATETIME, 
	last_login_ip VARCHAR(50), 
	login_count INTEGER NOT NULL, 
	failed_login_attempts INTEGER NOT NULL, 
	locked_until DATETIME, 
	email_notifications BOOLEAN NOT NULL, 
	sms_notifications BOOLEAN NOT NULL, 
	marketing_emails BOOLEAN NOT NULL, 
	facebook_id VARCHAR(100), 
	google_id VARCHAR(100), 
	linkedin_id VARCHAR(100), 
	notes TEXT, 
	email_verified_at DATETIME, 
	phone_verified_at DATETIME, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (username)
);
CREATE TABLE video_category (
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	description TEXT, 
	parent_id INTEGER, 
	sort_order INTEGER NOT NULL, 
	is_visible BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_id) REFERENCES video_category (id)
);
INSERT INTO video_category VALUES('Student Performances','performances','',NULL,1,1,1,'2025-11-04 21:58:23.566413','2025-11-04 21:58:23.566418');
INSERT INTO video_category VALUES('Cultural Events','cultural-events','',NULL,2,1,2,'2025-11-04 21:58:23.566420','2025-11-04 21:58:23.566421');
INSERT INTO video_category VALUES('Teaching Resources','teaching-resources','',NULL,3,1,3,'2025-11-04 21:58:23.566421','2025-11-04 21:58:23.566422');
CREATE TABLE comment (
	commentable_type VARCHAR(50) NOT NULL, 
	commentable_id INTEGER NOT NULL, 
	author_name VARCHAR(100) NOT NULL, 
	author_email VARCHAR(100) NOT NULL, 
	author_website VARCHAR(255), 
	user_id INTEGER, 
	content TEXT NOT NULL, 
	rating INTEGER, 
	parent_id INTEGER, 
	status VARCHAR(8) NOT NULL, 
	is_featured BOOLEAN NOT NULL, 
	admin_reply TEXT, 
	replied_at DATETIME, 
	helpful_count INTEGER NOT NULL, 
	report_count INTEGER NOT NULL, 
	ip_address VARCHAR(45), 
	user_agent VARCHAR(500), 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_id) REFERENCES comment (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);
CREATE TABLE custom_field_def (
	module_type VARCHAR(7) NOT NULL, 
	column_id INTEGER, 
	field_key VARCHAR(100) NOT NULL, 
	label VARCHAR(100) NOT NULL, 
	input_type VARCHAR(11) NOT NULL, 
	required BOOLEAN NOT NULL, 
	sort_order INTEGER NOT NULL, 
	min_value FLOAT, 
	max_value FLOAT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(column_id) REFERENCES site_column (id)
);
CREATE TABLE event (
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	description TEXT NOT NULL, 
	summary TEXT, 
	event_type VARCHAR(10) NOT NULL, 
	start_datetime DATETIME NOT NULL, 
	end_datetime DATETIME NOT NULL, 
	timezone VARCHAR(50), 
	registration_deadline DATETIME, 
	location_type VARCHAR(8) NOT NULL, 
	venue_name VARCHAR(200), 
	venue_address VARCHAR(500), 
	venue_city VARCHAR(100), 
	venue_postal_code VARCHAR(20), 
	online_meeting_url VARCHAR(500), 
	online_meeting_password VARCHAR(100), 
	max_attendees INTEGER, 
	current_attendees INTEGER NOT NULL, 
	allow_waitlist BOOLEAN NOT NULL, 
	waitlist_count INTEGER NOT NULL, 
	is_free BOOLEAN NOT NULL, 
	ticket_price FLOAT, 
	early_bird_price FLOAT, 
	early_bird_deadline DATETIME, 
	cover_media_id INTEGER, 
	status VARCHAR(9) NOT NULL, 
	is_featured BOOLEAN NOT NULL, 
	is_public BOOLEAN NOT NULL, 
	organizer_name VARCHAR(200), 
	organizer_email VARCHAR(100), 
	organizer_phone VARCHAR(50), 
	contact_person VARCHAR(100), 
	agenda TEXT, 
	speakers TEXT, 
	materials_url VARCHAR(500), 
	seo_title VARCHAR(200), 
	seo_description TEXT, 
	tags VARCHAR(255), 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cover_media_id) REFERENCES media_file (id)
);
INSERT INTO event VALUES('Chinese New Year Celebration 2025','chinese-new-year-2025','Join us for our annual Chinese New Year celebration featuring traditional performances, calligraphy workshops, dumpling making, and lion dance!','Annual Chinese New Year celebration with performances and cultural activities','cultural','2025-02-10 14:00:00.000000','2025-02-10 17:00:00.000000','Pacific/Auckland',NULL,'physical','Manchester Community Centre','123 Main Street','Manchester','M1 1AA',NULL,NULL,200,0,1,0,0,5.0,NULL,NULL,NULL,'published',1,1,'Bowen Education Group','info@boweneducation.org',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,'2025-11-04 21:58:23.507544','2025-11-04 21:58:23.507548');
INSERT INTO event VALUES('HSK Level 3 Mock Examination','hsk-3-mock-exam','Full mock examination for HSK Level 3 students including listening, reading, and writing sections. Get familiarized with exam format and timing.','Practice HSK Level 3 exam under real conditions','exam','2025-03-15 10:00:00.000000','2025-03-15 12:00:00.000000','Pacific/Auckland',NULL,'physical','Bowen Education Centre','1/F, 2A Curzon Road, Sale','Manchester','M33 7DR',NULL,NULL,40,0,0,0,1,NULL,NULL,NULL,NULL,'published',0,0,'Bowen Education Group','info@boweneducation.org',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2,'2025-11-04 21:58:23.507550','2025-11-04 21:58:23.507550');
CREATE TABLE file_download (
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	description TEXT, 
	category_id INTEGER, 
	file_media_id INTEGER NOT NULL, 
	file_name VARCHAR(255) NOT NULL, 
	file_extension VARCHAR(20), 
	file_size_kb INTEGER, 
	file_type VARCHAR(5) NOT NULL, 
	version VARCHAR(50), 
	is_latest BOOLEAN NOT NULL, 
	previous_version_id INTEGER, 
	thumbnail_media_id INTEGER, 
	access_level VARCHAR(12) NOT NULL, 
	requires_login BOOLEAN NOT NULL, 
	allowed_roles VARCHAR(255), 
	download_limit_per_user INTEGER, 
	link_expiry_days INTEGER, 
	is_featured BOOLEAN NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	status VARCHAR(9) NOT NULL, 
	sort_order INTEGER NOT NULL, 
	tags VARCHAR(255), 
	download_count INTEGER NOT NULL, 
	view_count INTEGER NOT NULL, 
	last_downloaded_at DATETIME, 
	usage_instructions TEXT, 
	system_requirements TEXT, 
	release_notes TEXT, 
	seo_title VARCHAR(200), 
	seo_description TEXT, 
	author VARCHAR(100), 
	published_date DATETIME, 
	last_updated_date DATETIME, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES file_category (id), 
	FOREIGN KEY(file_media_id) REFERENCES media_file (id), 
	FOREIGN KEY(previous_version_id) REFERENCES file_download (id), 
	FOREIGN KEY(thumbnail_media_id) REFERENCES media_file (id)
);
CREATE TABLE gallery (
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	description TEXT, 
	category VARCHAR(100), 
	tags VARCHAR(255), 
	cover_media_id INTEGER, 
	display_mode VARCHAR(50), 
	is_featured BOOLEAN NOT NULL, 
	is_public BOOLEAN NOT NULL, 
	sort_order INTEGER NOT NULL, 
	allow_download BOOLEAN NOT NULL, 
	watermark_enabled BOOLEAN NOT NULL, 
	seo_title VARCHAR(200), 
	seo_description TEXT, 
	view_count INTEGER NOT NULL, 
	image_count INTEGER NOT NULL, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cover_media_id) REFERENCES media_file (id)
);
CREATE TABLE menu_category (
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	description TEXT, 
	sort_order INTEGER NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	available_times VARCHAR(255), 
	image_media_id INTEGER, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(image_media_id) REFERENCES media_file (id)
);
CREATE TABLE IF NOT EXISTS "order" (
	order_number VARCHAR(50) NOT NULL, 
	user_id INTEGER, 
	status VARCHAR(10) NOT NULL, 
	payment_status VARCHAR(8) NOT NULL, 
	customer_email VARCHAR(100) NOT NULL, 
	customer_phone VARCHAR(50), 
	customer_name VARCHAR(100) NOT NULL, 
	shipping_address_line1 VARCHAR(255) NOT NULL, 
	shipping_address_line2 VARCHAR(255), 
	shipping_city VARCHAR(100) NOT NULL, 
	shipping_state VARCHAR(100), 
	shipping_postal_code VARCHAR(20) NOT NULL, 
	shipping_country VARCHAR(100) NOT NULL, 
	billing_address_line1 VARCHAR(255), 
	billing_address_line2 VARCHAR(255), 
	billing_city VARCHAR(100), 
	billing_state VARCHAR(100), 
	billing_postal_code VARCHAR(20), 
	billing_country VARCHAR(100), 
	billing_same_as_shipping BOOLEAN NOT NULL, 
	subtotal FLOAT NOT NULL, 
	shipping_fee FLOAT NOT NULL, 
	tax_amount FLOAT NOT NULL, 
	discount_amount FLOAT NOT NULL, 
	total_amount FLOAT NOT NULL, 
	paid_amount FLOAT NOT NULL, 
	coupon_code VARCHAR(50), 
	coupon_discount FLOAT NOT NULL, 
	shipping_method VARCHAR(8) NOT NULL, 
	shipping_carrier VARCHAR(100), 
	tracking_number VARCHAR(100), 
	tracking_url VARCHAR(255), 
	payment_method VARCHAR(13), 
	payment_transaction_id VARCHAR(100), 
	paid_at DATETIME, 
	confirmed_at DATETIME, 
	shipped_at DATETIME, 
	delivered_at DATETIME, 
	cancelled_at DATETIME, 
	customer_notes TEXT, 
	admin_notes TEXT, 
	cancel_reason TEXT, 
	refund_reason TEXT, 
	ip_address VARCHAR(50), 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	UNIQUE (order_number)
);
CREATE TABLE portfolio (
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	subtitle VARCHAR(300), 
	cover_media_id INTEGER, 
	summary TEXT, 
	background TEXT, 
	challenge TEXT, 
	solution TEXT, 
	result TEXT, 
	content_html TEXT, 
	client_name VARCHAR(200), 
	client_logo_media_id INTEGER, 
	is_client_anonymous BOOLEAN NOT NULL, 
	project_date DATE, 
	project_duration VARCHAR(100), 
	project_url VARCHAR(500), 
	tags VARCHAR(500), 
	is_featured BOOLEAN NOT NULL, 
	sort_order INTEGER NOT NULL, 
	status VARCHAR(9) NOT NULL, 
	seo_title VARCHAR(200), 
	seo_description TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_logo_media_id) REFERENCES media_file (id), 
	FOREIGN KEY(cover_media_id) REFERENCES media_file (id), 
	UNIQUE (slug)
);
CREATE TABLE post (
	column_id INTEGER NOT NULL, 
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	summary TEXT, 
	cover_media_id INTEGER, 
	content_html TEXT NOT NULL, 
	is_recommended BOOLEAN NOT NULL, 
	status VARCHAR(9) NOT NULL, 
	seo_title VARCHAR(200), 
	seo_description TEXT, 
	published_at DATETIME, 
	is_approved INTEGER NOT NULL, 
	admin_reply TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(column_id) REFERENCES site_column (id), 
	FOREIGN KEY(cover_media_id) REFERENCES media_file (id)
);
INSERT INTO post VALUES(8,'博文集团与河南大学建立战略合作伙伴关系','henan-university-partnership','博文教育集团正式与中国河南大学签署战略合作协议，共同推进中英教育文化交流项目，为曼彻斯特华裔青少年提供寻根之旅机会。',11,'<h2>合作背景</h2><p>2024年3月，博文教育集团与河南大学在郑州正式签署战略合作协议。此次合作标志着博文集团在推动中英教育文化交流方面迈出了重要一步。河南大学作为中国百年名校，在汉语国际教育和文化传播领域具有深厚的学术积淀和丰富的教学资源。</p><h2>合作内容</h2><p>本次战略合作涵盖多个领域：</p><ul><li><strong>师资交流项目</strong>：河南大学将定期派遣优秀汉语教师来曼彻斯特进行短期教学交流。</li><li><strong>学生交流计划</strong>：每年组织博文学校学生赴河南大学参加短期文化体验营。</li><li><strong>课程资源共享</strong>：河南大学将向博文集团提供优质的教学资源。</li><li><strong>学术研究合作</strong>：双方将在海外华文教育研究领域开展合作。</li></ul><h2>寻根之旅</h2><p>作为合作的重要组成部分，博文集团每年将组织"寻根之旅"活动。</p><h2>报名咨询</h2><p>邮箱：china-trip@boweneducation.org<br>电话：0161 xxx xxxx</p>',0,'published','博文集团与河南大学建立战略合作伙伴关系','博文教育集团正式与中国河南大学签署战略合作协议。','2024-03-15 10:00:00',1,NULL,1,'2025-11-05 10:23:43','2025-11-05 10:23:43');
INSERT INTO post VALUES(8,'2024年秋季学期招生现已开放','2024-autumn-term-enrollment','博文中文学校2024年秋季学期招生全面启动，提供从基础班到A-Level的全方位中文课程，GCSE通过率保持100%。',12,'<h2>招生公告</h2><p>博文中文学校2024年秋季学期招生现已全面启动！</p><h2>课程设置</h2><h3>1. 基础中文班（5-7岁）</h3><ul><li>上课时间：每周六 10:00-11:00</li><li>学费：£180/学期（12周）</li></ul><h3>2. GCSE中文班（14-16岁）</h3><ul><li>课程特色：历年通过率100%</li></ul><h2>新生优惠</h2><p>首月学费九折优惠。</p>',1,'published','2024年秋季学期招生现已开放','博文中文学校2024年秋季学期招生全面启动。','2024-02-20 09:00:00',1,NULL,2,'2025-11-05 10:23:43','2025-11-05 10:23:43');
INSERT INTO post VALUES(8,'2024年HAF项目圆满结束，惠及200余名儿童','haf-programme-success-2024','博文集团作为Trafford Council官方合作伙伴，成功举办2024年暑期HAF项目，为200多名儿童提供免费活动和健康餐食。',13,'<h2>项目概况</h2><p>2024年暑期，博文教育集团成功举办了为期四周的假期活动，惠及200余名儿童。</p><h2>项目亮点</h2><ul><li>中华文化体验活动</li><li>体育运动项目</li></ul><h2>项目成果</h2><ul><li>参与儿童：206名</li><li>家长满意度：98%</li></ul>',0,'published','2024年HAF项目圆满结束','博文集团成功举办2024年暑期HAF项目。','2024-08-25 14:30:00',1,NULL,3,'2025-11-05 10:23:43','2025-11-05 10:23:43');
INSERT INTO post VALUES(8,'博文国际象棋俱乐部在曼彻斯特地区赛事中斩获佳绩','chess-club-tournament-achievements','博文国际象棋俱乐部学员在2024年春季曼彻斯特青少年锦标赛中表现出色，3名学员分别获得各组别冠军。',14,'<h2>赛事背景</h2><p>2024年3月16-17日，曼彻斯特青少年国际象棋锦标赛举行。</p><h2>博文俱乐部战绩</h2><ul><li><strong>U10组冠军</strong>：王思远</li><li><strong>U12组冠军</strong>：李明轩</li><li><strong>U14组冠军</strong>：张雨涵</li></ul><h2>ECF等级分提升</h2><ul><li>5名学员首次获得ECF等级分</li><li>12名学员等级分提升100分以上</li></ul>',0,'published','博文国际象棋俱乐部斩获佳绩','3名学员获得冠军。','2024-03-20 16:00:00',1,NULL,4,'2025-11-05 10:23:43','2025-11-05 10:23:43');
CREATE TABLE post_category (
	column_id INTEGER NOT NULL, 
	parent_id INTEGER, 
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	sort_order INTEGER NOT NULL, 
	is_visible BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(column_id) REFERENCES site_column (id), 
	FOREIGN KEY(parent_id) REFERENCES post_category (id)
);
INSERT INTO post_category VALUES(8,NULL,'School News','school-news',1,1,1,'2025-11-04 21:58:23.467552','2025-11-04 21:58:23.467557');
INSERT INTO post_category VALUES(8,NULL,'Events','events',2,1,2,'2025-11-04 21:58:23.467558','2025-11-04 21:58:23.467559');
INSERT INTO post_category VALUES(8,NULL,'Student Success','student-success',3,1,3,'2025-11-04 21:58:23.467560','2025-11-04 21:58:23.467560');
CREATE TABLE product (
	column_id INTEGER NOT NULL, 
	name VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	summary TEXT, 
	description_html TEXT NOT NULL, 
	cover_media_id INTEGER, 
	price_text VARCHAR(100), 
	availability_status VARCHAR(12) NOT NULL, 
	is_recommended BOOLEAN NOT NULL, 
	status VARCHAR(7) NOT NULL, 
	seo_title VARCHAR(200), 
	seo_description TEXT, 
	published_at DATETIME, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(column_id) REFERENCES site_column (id), 
	FOREIGN KEY(cover_media_id) REFERENCES media_file (id)
);
INSERT INTO product VALUES(3,'Foundation Mandarin (Ages 5-7)','foundation-mandarin','Playful introduction to Mandarin for young learners through songs, games, and stories','<p>Our Foundation Mandarin programme is designed for children aged 5-7 who are just beginning their Chinese language journey...</p>',NULL,'£180 per term','in_stock',1,'online',NULL,NULL,'2025-11-04 21:58:23.426108',1,'2025-11-04 21:58:23.428883','2025-11-04 21:58:23.428885');
INSERT INTO product VALUES(3,'GCSE Chinese (Ages 14-16)','gcse-chinese','Comprehensive GCSE Chinese preparation aligned with AQA/Edexcel specifications','<p>Our GCSE Chinese programme provides comprehensive preparation for the AQA or Edexcel GCSE Chinese examinations...</p>',NULL,'£240 per term','in_stock',1,'online',NULL,NULL,'2025-11-04 21:58:23.426114',2,'2025-11-04 21:58:23.428885','2025-11-04 21:58:23.428886');
INSERT INTO product VALUES(3,'A-Level Chinese (Ages 16-18)','a-level-chinese','Advanced Chinese language and literature course for university-bound students','<p>Our A-Level Chinese programme offers advanced study of Chinese language and literature...</p>',NULL,'£280 per term','in_stock',1,'online',NULL,NULL,'2025-11-04 21:58:23.426116',3,'2025-11-04 21:58:23.428886','2025-11-04 21:58:23.428886');
INSERT INTO product VALUES(3,'HSK Level 3 Preparation','hsk-level-3','Targeted preparation for the HSK Level 3 examination with mock tests','<p>Our HSK Level 3 preparation course is designed to help students pass the HSK Level 3 examination...</p>',NULL,'£200 per term','in_stock',0,'online',NULL,NULL,'2025-11-04 21:58:23.426118',4,'2025-11-04 21:58:23.428887','2025-11-04 21:58:23.428887');
INSERT INTO product VALUES(3,'Cantonese Language Course','cantonese-language','Preserve your Cantonese heritage with our authentic language programme','<p>Our Cantonese language course helps students maintain and develop their Cantonese language skills...</p>',NULL,'£180 per term','in_stock',0,'online',NULL,NULL,'2025-11-04 21:58:23.426120',5,'2025-11-04 21:58:23.428887','2025-11-04 21:58:23.428888');
INSERT INTO product VALUES(4,'GCSE Mathematics Tutoring','gcse-mathematics','Expert GCSE Maths tutoring with focus on problem-solving and exam technique','<p>Our GCSE Mathematics tutoring provides comprehensive support for students preparing for their GCSE exams...</p>',NULL,'£30 per hour','in_stock',1,'online',NULL,NULL,'2025-11-04 21:58:23.426715',6,'2025-11-04 21:58:23.428888','2025-11-04 21:58:23.428888');
INSERT INTO product VALUES(4,'A-Level Physics Tutoring','a-level-physics','One-to-one A-Level Physics tutoring from experienced educators','<p>Our A-Level Physics tutoring provides personalized support for students studying A-Level Physics...</p>',NULL,'£35 per hour','in_stock',0,'online',NULL,NULL,'2025-11-04 21:58:23.426720',7,'2025-11-04 21:58:23.428889','2025-11-04 21:58:23.428889');
CREATE TABLE product_category (
	column_id INTEGER NOT NULL, 
	parent_id INTEGER, 
	name VARCHAR(100) NOT NULL, 
	slug VARCHAR(100) NOT NULL, 
	sort_order INTEGER NOT NULL, 
	is_visible BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(column_id) REFERENCES site_column (id), 
	FOREIGN KEY(parent_id) REFERENCES product_category (id)
);
INSERT INTO product_category VALUES(3,NULL,'Chinese Language Courses','chinese-language',1,1,1,'2025-11-04 21:58:23.406291','2025-11-04 21:58:23.406293');
INSERT INTO product_category VALUES(4,NULL,'Academic Tutoring','academic-tutoring',2,1,2,'2025-11-04 21:58:23.406294','2025-11-04 21:58:23.406294');
INSERT INTO product_category VALUES(3,NULL,'Exam Preparation','exam-preparation',3,1,3,'2025-11-04 21:58:23.406294','2025-11-04 21:58:23.406295');
INSERT INTO product_category VALUES(3,NULL,'Adult Classes','adult-classes',4,1,4,'2025-11-04 21:58:23.406295','2025-11-04 21:58:23.406295');
CREATE TABLE restaurant_order (
	order_number VARCHAR(50) NOT NULL, 
	user_id INTEGER, 
	order_type VARCHAR(8) NOT NULL, 
	status VARCHAR(10) NOT NULL, 
	payment_status VARCHAR(8) NOT NULL, 
	customer_name VARCHAR(100) NOT NULL, 
	customer_phone VARCHAR(50) NOT NULL, 
	customer_email VARCHAR(100), 
	table_number VARCHAR(20), 
	number_of_guests INTEGER, 
	delivery_address VARCHAR(500), 
	delivery_city VARCHAR(100), 
	delivery_postal_code VARCHAR(20), 
	delivery_instructions TEXT, 
	pickup_time DATETIME, 
	scheduled_time DATETIME, 
	subtotal FLOAT NOT NULL, 
	delivery_fee FLOAT NOT NULL, 
	service_fee FLOAT NOT NULL, 
	tax_amount FLOAT NOT NULL, 
	discount_amount FLOAT NOT NULL, 
	tip_amount FLOAT NOT NULL, 
	total_amount FLOAT NOT NULL, 
	coupon_code VARCHAR(50), 
	payment_method VARCHAR(6), 
	paid_at DATETIME, 
	confirmed_at DATETIME, 
	preparing_at DATETIME, 
	ready_at DATETIME, 
	delivered_at DATETIME, 
	completed_at DATETIME, 
	cancelled_at DATETIME, 
	customer_notes TEXT, 
	kitchen_notes TEXT, 
	cancel_reason TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	UNIQUE (order_number)
);
CREATE TABLE single_page (
	column_id INTEGER NOT NULL, 
	title VARCHAR(200) NOT NULL, 
	subtitle VARCHAR(300), 
	content_html TEXT NOT NULL, 
	hero_media_id INTEGER, 
	seo_title VARCHAR(200), 
	seo_description TEXT, 
	status VARCHAR(9) NOT NULL, 
	published_at DATETIME, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(column_id) REFERENCES site_column (id), 
	FOREIGN KEY(hero_media_id) REFERENCES media_file (id), 
	UNIQUE (column_id)
);
INSERT INTO single_page VALUES(2,'About Us','Learn about Bowen Education Group','<p>Welcome to Bowen Education Group - Manchester''s premier Chinese language school.</p>',NULL,NULL,NULL,'published','2025-11-04 22:59:06.623365',1,'2025-11-04 22:59:06.625733','2025-11-04 22:59:06.625736');
INSERT INTO single_page VALUES(11,'Contact Us','Get in touch with us','<p>We''re here to help! Contact us for more information about our courses.</p>',NULL,NULL,NULL,'published','2025-11-04 22:59:06.623533',2,'2025-11-04 22:59:06.625736','2025-11-04 22:59:06.625737');
INSERT INTO single_page VALUES(3,'中文学校','Manchester Chinese School','<div class="container"><h2>中文学校</h2><p>博文中文学校为不同年龄段的学生提供优质的中文教育服务。</p><p>课程内容正在建设中，敬请期待。</p></div>',NULL,'中文学校 - 博文集团','博文中文学校提供启蒙班、中级班、精英班、GCSE普通话等课程','published','2025-11-05 02:22:26.641503',3,'2025-11-05 02:22:26.647020','2025-11-05 02:22:26.647022');
INSERT INTO single_page VALUES(4,'补习中心','Tuition Centre','<div class="container"><h2>补习中心</h2><p>博文补习中心提供GCSE和A-Level各科目的专业辅导。</p><p>课程内容正在建设中，敬请期待。</p></div>',NULL,'补习中心 - 博文集团','提供GCSE数学、物理、化学、英语和A-Level课程辅导','published','2025-11-05 02:22:26.642242',4,'2025-11-05 02:22:26.647023','2025-11-05 02:22:26.647023');
INSERT INTO single_page VALUES(5,'国际象棋俱乐部','Chess Club','<div class="container"><h2>国际象棋俱乐部</h2><p>博文国际象棋俱乐部为学生提供专业的国际象棋培训和比赛机会。</p><p>详细内容正在建设中，敬请期待。</p></div>',NULL,'国际象棋俱乐部 - 博文集团','专业的国际象棋培训和比赛','published','2025-11-05 02:22:26.642839',5,'2025-11-05 02:22:26.647023','2025-11-05 02:22:26.647026');
INSERT INTO single_page VALUES(6,'政府项目','Government Programmes','<div class="container"><h2>政府项目</h2><p>博文集团参与多项政府合作项目，包括HAF项目和公园活动等。</p><p>详细内容正在建设中，敬请期待。</p></div>',NULL,'政府项目 - 博文集团','HAF项目、公园活动等政府合作项目','published','2025-11-05 02:22:26.643443',6,'2025-11-05 02:22:26.647026','2025-11-05 02:22:26.647027');
INSERT INTO single_page VALUES(7,'博文活动','Events','<div class="container"><h2>博文活动</h2><p>博文集团定期举办各类文化活动，包括中国新年庆典、文化进校园、寻根之旅等。</p><p>详细内容正在建设中，敬请期待。</p></div>',NULL,'博文活动 - 博文集团','中国新年庆典、文化进校园、寻根之旅等文化活动','published','2025-11-05 02:22:26.643996',7,'2025-11-05 02:22:26.647028','2025-11-05 02:22:26.647028');
INSERT INTO single_page VALUES(8,'博文新闻','News','<div class="container"><h2>博文新闻</h2><p>了解博文集团的最新动态、活动报道和合作消息。</p><p>详细内容正在建设中，敬请期待。</p></div>',NULL,'博文新闻 - 博文集团','博文集团最新动态、活动报道和合作消息','published','2025-11-05 02:22:26.644552',8,'2025-11-05 02:22:26.647028','2025-11-05 02:22:26.647029');
INSERT INTO single_page VALUES(12,'羽毛球俱乐部','Badminton Club','<div class="container"><h2>羽毛球俱乐部</h2><p>博文羽毛球俱乐部为学生提供专业的羽毛球训练和比赛机会。</p><p>详细内容正在建设中，敬请期待。</p></div>',NULL,'羽毛球俱乐部 - 博文集团','专业的羽毛球训练和比赛','published','2025-11-05 02:22:26.645107',9,'2025-11-05 02:22:26.647029','2025-11-05 02:22:26.647029');
INSERT INTO single_page VALUES(14,'学期日期','Term Dates',replace('\n                <h2>2024-2025学年学期安排</h2>\n\n                <h3>秋季学期 Autumn Term</h3>\n                <ul>\n                    <li><strong>开学日期：</strong>2024年9月7日</li>\n                    <li><strong>期中假期：</strong>2024年10月26日 - 11月3日</li>\n                    <li><strong>学期结束：</strong>2024年12月21日</li>\n                </ul>\n\n                <h3>春季学期 Spring Term</h3>\n                <ul>\n                    <li><strong>开学日期：</strong>2025年1月6日</li>\n                    <li><strong>期中假期：</strong>2025年2月15日 - 2月23日</li>\n                    <li><strong>学期结束：</strong>2025年4月4日</li>\n                </ul>\n\n                <h3>夏季学期 Summer Term</h3>\n                <ul>\n                    <li><strong>开学日期：</strong>2025年4月21日</li>\n                    <li><strong>期中假期：</strong>2025年5月24日 - 6月1日</li>\n                    <li><strong>学期结束：</strong>2025年7月18日</li>\n                </ul>\n\n                <div class="alert alert-info mt-4">\n                    <p><strong>注意事项：</strong></p>\n                    <ul>\n                        <li>所有课程均在周六上午进行</li>\n                        <li>法定假日不上课</li>\n                        <li>如遇特殊情况需要调整，学校将提前通知</li>\n                    </ul>\n                </div>\n            ','\n',char(10)),NULL,'学期日期 - 博文中文学校','查看博文中文学校2024-2025学年的完整学期安排和重要日期','published','2025-11-05 06:06:15.023817',10,'2025-11-05 06:06:15.026300','2025-11-05 06:06:15.026303');
INSERT INTO single_page VALUES(15,'PTA家长教师协会','Parent-Teacher Association',replace('\n                <h2>关于我们的PTA</h2>\n                <p>博文中文学校家长教师协会（PTA）是一个由家长和教师组成的志愿组织，致力于促进家校合作，为学生创造更好的学习环境。</p>\n\n                <h3>我们的使命</h3>\n                <ul>\n                    <li>促进家长与学校之间的沟通与合作</li>\n                    <li>组织各类文化活动和社交活动</li>\n                    <li>为学校筹集资金，改善教学设施</li>\n                    <li>支持学校的教育项目和倡议</li>\n                </ul>\n\n                <h3>如何参与</h3>\n                <p>我们欢迎所有家长和教师加入PTA。您可以通过以下方式参与：</p>\n                <ul>\n                    <li>参加每学期的PTA会议</li>\n                    <li>协助组织学校活动</li>\n                    <li>担任PTA委员会成员</li>\n                    <li>提供您的专业技能和建议</li>\n                </ul>\n\n                <h3>联系我们</h3>\n                <p>如有任何问题或建议，请通过学校邮箱 <a href="mailto:info@boweneducation.org">info@boweneducation.org</a> 联系我们，或在家长微信群中与我们互动。</p>\n            ','\n',char(10)),NULL,'PTA家长教师协会 - 博文中文学校','加入博文中文学校PTA，与学校携手共同促进孩子的成长和发展','published','2025-11-05 06:06:15.027576',11,'2025-11-05 06:06:15.027993','2025-11-05 06:06:15.027995');
INSERT INTO single_page VALUES(17,'棋手信息','Information for Players',replace('\n                <h2>棋手注册与认证</h2>\n                <p>博文国际象棋俱乐部与英格兰国际象棋联合会（English Chess Federation, ECF）合作，为棋手提供正规的等级认证服务。</p>\n\n                <h3>ECF会员注册</h3>\n                <ul>\n                    <li>所有希望参加正式比赛的棋手需要注册ECF会员</li>\n                    <li>会员可以获得官方等级分（ECF Rating）</li>\n                    <li>青少年会员享有优惠价格</li>\n                </ul>\n\n                <h3>等级分体系</h3>\n                <p>ECF采用国际通用的等级分系统，根据比赛表现动态调整。等级分分为：</p>\n                <ul>\n                    <li><strong>初级：</strong>0-1000</li>\n                    <li><strong>中级：</strong>1000-1600</li>\n                    <li><strong>高级：</strong>1600-2000</li>\n                    <li><strong>专家：</strong>2000+</li>\n                </ul>\n\n                <h3>相关链接</h3>\n                <ul>\n                    <li><a href="https://www.englishchess.org.uk/" target="_blank">English Chess Federation 官网</a></li>\n                    <li><a href="https://www.englishchess.org.uk/ecf-membership/" target="_blank">ECF会员注册</a></li>\n                    <li><a href="https://www.englishchess.org.uk/rating-lists/" target="_blank">查询等级分</a></li>\n                </ul>\n\n                <p class="mt-4"><strong>如需协助注册或有任何疑问，请联系俱乐部教练。</strong></p>\n            ','\n',char(10)),NULL,'棋手信息 - 博文国际象棋俱乐部','了解ECF会员注册、等级分体系和相关信息','published','2025-11-05 06:06:15.028710',12,'2025-11-05 06:06:15.029066','2025-11-05 06:06:15.029068');
INSERT INTO single_page VALUES(20,'训练时间表','Training Schedule',replace('\n                <h2>训练时间安排</h2>\n\n                <h3>常规训练</h3>\n                <div class="table-responsive">\n                    <table class="table">\n                        <thead>\n                            <tr>\n                                <th>日期</th>\n                                <th>时间</th>\n                                <th>级别</th>\n                                <th>地点</th>\n                            </tr>\n                        </thead>\n                        <tbody>\n                            <tr>\n                                <td>每周六</td>\n                                <td>10:00 - 12:00</td>\n                                <td>初级班</td>\n                                <td>Sale Sports Centre</td>\n                            </tr>\n                            <tr>\n                                <td>每周六</td>\n                                <td>14:00 - 16:00</td>\n                                <td>中级班</td>\n                                <td>Sale Sports Centre</td>\n                            </tr>\n                            <tr>\n                                <td>每周日</td>\n                                <td>10:00 - 12:00</td>\n                                <td>高级班</td>\n                                <td>Sale Sports Centre</td>\n                            </tr>\n                            <tr>\n                                <td>每周日</td>\n                                <td>14:00 - 17:00</td>\n                                <td>竞技训练</td>\n                                <td>Sale Sports Centre</td>\n                            </tr>\n                        </tbody>\n                    </table>\n                </div>\n\n                <h3>训练内容</h3>\n                <ul>\n                    <li><strong>初级班：</strong>基础技术教学，包括握拍、步法、基本击球</li>\n                    <li><strong>中级班：</strong>技术提升，战术训练，双打配合</li>\n                    <li><strong>高级班：</strong>高级技战术，体能训练，心理素质培养</li>\n                    <li><strong>竞技训练：</strong>针对比赛的专项训练和实战演练</li>\n                </ul>\n\n                <h3>训练地点</h3>\n                <p>\n                    <strong>Sale Sports Centre</strong><br>\n                    Sale Road, Sale, Manchester M33 3SL<br>\n                    <a href="https://goo.gl/maps/example" target="_blank">查看地图</a>\n                </p>\n\n                <div class="alert alert-info mt-4">\n                    <p><strong>注意事项：</strong></p>\n                    <ul>\n                        <li>请提前10分钟到场热身</li>\n                        <li>自备球拍和运动装备</li>\n                        <li>如遇场馆维护或特殊情况，将提前通知</li>\n                    </ul>\n                </div>\n            ','\n',char(10)),NULL,'训练时间表 - 博文羽毛球俱乐部','查看博文羽毛球俱乐部的完整训练时间表和地点信息','published','2025-11-05 06:06:15.029792',13,'2025-11-05 06:06:15.030153','2025-11-05 06:06:15.030155');
INSERT INTO single_page VALUES(22,'HAF项目','Holiday Activities and Food Programme',replace('\n                <h2>关于HAF项目</h2>\n                <p>Holiday Activities and Food (HAF) 项目是英国政府资助的一项重要社区项目，旨在在学校假期期间为符合条件的儿童提供健康食品和有趣的活动。博文集团积极参与该项目，为当地社区的孩子们提供丰富多彩的假期活动。</p>\n\n                <h3>项目目标</h3>\n                <ul>\n                    <li>为符合条件的儿童提供免费的健康餐食</li>\n                    <li>组织各类教育和娱乐活动</li>\n                    <li>促进儿童的身心健康发展</li>\n                    <li>支持家庭减轻假期照看负担</li>\n                </ul>\n\n                <h3>活动内容</h3>\n                <p>我们的HAF项目包括：</p>\n                <ul>\n                    <li>中华文化体验活动（书法、剪纸、中国结等）</li>\n                    <li>体育运动（羽毛球、国际象棋等）</li>\n                    <li>艺术创作和手工制作</li>\n                    <li>团队游戏和户外活动</li>\n                    <li>每日提供健康午餐和小食</li>\n                </ul>\n\n                <h3>参与资格</h3>\n                <p>该项目面向5-16岁符合以下条件的儿童：</p>\n                <ul>\n                    <li>有资格享受免费校餐（Free School Meals）</li>\n                    <li>居住在Trafford地区</li>\n                </ul>\n\n                <h3>如何报名</h3>\n                <p>HAF项目通常在以下假期期间举办：</p>\n                <ul>\n                    <li>复活节假期（2周）</li>\n                    <li>暑假（4周）</li>\n                    <li>圣诞假期（1周）</li>\n                </ul>\n                <p>具体报名方式和时间将通过学校和社区渠道公布。如有疑问，请联系我们。</p>\n\n                <div class="alert alert-success mt-4">\n                    <p><strong>项目优势：</strong></p>\n                    <ul>\n                        <li>完全免费，包括所有活动和餐食</li>\n                        <li>专业教练和工作人员指导</li>\n                        <li>安全友好的环境</li>\n                        <li>结识新朋友，学习新技能</li>\n                    </ul>\n                </div>\n            ','\n',char(10)),NULL,'HAF项目 - 博文集团政府项目','了解博文集团参与的HAF假期活动和食品项目，为儿童提供免费健康餐食和丰富活动','published','2025-11-05 06:06:15.030825',14,'2025-11-05 06:06:15.031153','2025-11-05 06:06:15.031154');
INSERT INTO single_page VALUES(24,'河南大学合作','Cooperation with Henan University',replace('\n                <h2>河南大学合作项目</h2>\n                <p>博文集团与中国河南大学建立了长期战略合作伙伴关系，共同推动中英教育文化交流。</p>\n\n                <h3>合作内容</h3>\n                <ul>\n                    <li><strong>师资交流：</strong>河南大学定期派遣优秀教师到英国进行文化交流和教学支持</li>\n                    <li><strong>学生交流：</strong>组织学生互访活动，促进两国青少年的友谊和了解</li>\n                    <li><strong>文化活动：</strong>联合举办各类中华文化推广活动和学术研讨</li>\n                    <li><strong>资源共享：</strong>共享教学资源和研究成果</li>\n                </ul>\n\n                <h3>寻根之旅</h3>\n                <p>作为合作项目的重要组成部分，我们每年组织"寻根之旅"活动，带领在英国长大的华裔青少年回到中国，深入了解中华文化：</p>\n                <ul>\n                    <li>参观河南大学校园，体验中国大学生活</li>\n                    <li>游览历史文化名城，了解中国历史</li>\n                    <li>与中国学生交流，建立国际友谊</li>\n                    <li>参加文化体验活动（茶道、武术、传统工艺等）</li>\n                </ul>\n\n                <h3>Easter访华计划</h3>\n                <p>每年复活节期间，我们组织为期两周的访华活动：</p>\n                <ul>\n                    <li><strong>日期：</strong>每年复活节假期</li>\n                    <li><strong>对象：</strong>12-18岁学生</li>\n                    <li><strong>行程：</strong>河南（开封、郑州、洛阳）+ 北京</li>\n                    <li><strong>住宿：</strong>大学宿舍和精选酒店</li>\n                    <li><strong>陪同：</strong>专业领队和河南大学志愿者</li>\n                </ul>\n\n                <div class="alert alert-info mt-4">\n                    <p><strong>报名咨询：</strong></p>\n                    <p>如对河南大学合作项目或访华活动感兴趣，请联系我们获取详细信息和报名方式。</p>\n                    <p>邮箱：<a href="mailto:info@boweneducation.org">info@boweneducation.org</a></p>\n                </div>\n            ','\n',char(10)),NULL,'河南大学合作 - 博文集团','了解博文集团与河南大学的合作项目，包括寻根之旅和Easter访华计划','published','2025-11-05 06:06:15.031772',15,'2025-11-05 06:06:15.031992','2025-11-05 06:06:15.031993');
CREATE TABLE team_member (
	name VARCHAR(100) NOT NULL, 
	title VARCHAR(100), 
	department VARCHAR(100), 
	photo_media_id INTEGER, 
	bio TEXT, 
	qualifications TEXT, 
	specialties VARCHAR(500), 
	email VARCHAR(100), 
	phone VARCHAR(50), 
	linkedin VARCHAR(255), 
	twitter VARCHAR(255), 
	sort_order INTEGER NOT NULL, 
	is_featured BOOLEAN NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(photo_media_id) REFERENCES media_file (id)
);
INSERT INTO team_member VALUES('Dr. Bowen Zhang','Founder & Director','Leadership',NULL,'Dr. Bowen Zhang founded Bowen Education Group in 2018 with a vision to bridge Eastern and Western educational traditions. With a PhD in Education from the University of Manchester and over 15 years of teaching experience, Dr. Zhang has developed innovative Chinese language curricula that have helped hundreds of students achieve fluency and cultural competence.','PhD in Education (University of Manchester), MA in Chinese Linguistics (Peking University), QTS (UK)','Chinese Language Education, Curriculum Development, Educational Leadership','bowen.zhang@boweneducation.org',NULL,NULL,NULL,1,1,1,1,'2025-11-04 21:58:23.446958','2025-11-04 21:58:23.446961');
INSERT INTO team_member VALUES('Miss Emily Chen','Head of Chinese School','Chinese School',NULL,'Miss Emily Chen leads our Chinese School with passion and expertise. A native Mandarin speaker with over 10 years of teaching experience, Emily holds a Master''s degree in Teaching Chinese as a Foreign Language and is certified by Hanban (Confucius Institute Headquarters).','MA in TCFL (Beijing Language and Culture University), Hanban Certified Chinese Teacher','Mandarin Teaching, YCT/HSK Preparation, Children''s Language Development','emily.chen@boweneducation.org',NULL,NULL,NULL,2,1,1,2,'2025-11-04 21:58:23.446962','2025-11-04 21:58:23.446963');
INSERT INTO team_member VALUES('Mr. James Wilson','Head of Tuition Centre','Tuition Centre',NULL,'Mr. James Wilson brings extensive experience in British secondary education to his role as Head of Tuition Centre. With 12 years of teaching experience in Manchester schools and a track record of helping students achieve top grades, James specializes in GCSE and A-Level exam preparation.','BSc Mathematics (University of Cambridge), PGCE Secondary Mathematics, QTS','GCSE/A-Level Mathematics, Physics, Exam Technique','james.wilson@boweneducation.org',NULL,NULL,NULL,3,1,1,3,'2025-11-04 21:58:23.446963','2025-11-04 21:58:23.446964');
CREATE TABLE video (
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	description TEXT, 
	category_id INTEGER, 
	video_source VARCHAR(8) NOT NULL, 
	video_media_id INTEGER, 
	youtube_id VARCHAR(100), 
	vimeo_id VARCHAR(100), 
	external_url VARCHAR(500), 
	thumbnail_media_id INTEGER, 
	duration_seconds INTEGER, 
	resolution VARCHAR(20), 
	file_size_mb INTEGER, 
	autoplay BOOLEAN NOT NULL, 
	loop BOOLEAN NOT NULL, 
	muted BOOLEAN NOT NULL, 
	controls BOOLEAN NOT NULL, 
	has_subtitles BOOLEAN NOT NULL, 
	subtitle_url VARCHAR(500), 
	is_featured BOOLEAN NOT NULL, 
	is_public BOOLEAN NOT NULL, 
	status VARCHAR(9) NOT NULL, 
	sort_order INTEGER NOT NULL, 
	tags VARCHAR(255), 
	view_count INTEGER NOT NULL, 
	like_count INTEGER NOT NULL, 
	share_count INTEGER NOT NULL, 
	seo_title VARCHAR(200), 
	seo_description TEXT, 
	embed_code TEXT, 
	allow_embed BOOLEAN NOT NULL, 
	requires_login BOOLEAN NOT NULL, 
	allowed_roles VARCHAR(255), 
	notes TEXT, 
	published_at VARCHAR(200), 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES video_category (id), 
	FOREIGN KEY(thumbnail_media_id) REFERENCES media_file (id), 
	FOREIGN KEY(video_media_id) REFERENCES media_file (id)
);
INSERT INTO video VALUES('Chinese New Year 2024 Highlights','cny-2024-highlights','Highlights from our spectacular Chinese New Year 2024 celebration featuring student performances and cultural activities.',1,'youtube',NULL,'example1',NULL,NULL,NULL,180,NULL,NULL,0,0,0,1,0,NULL,1,1,'published',1,NULL,0,0,0,NULL,NULL,NULL,1,0,NULL,NULL,NULL,1,'2025-11-04 21:58:23.591021','2025-11-04 21:58:23.591024');
INSERT INTO video VALUES('Student Dragon Dance Performance','dragon-dance-performance','Our talented students perform a traditional Chinese dragon dance at the Manchester Chinese Cultural Festival.',1,'youtube',NULL,'example2',NULL,NULL,NULL,240,NULL,NULL,0,0,0,1,0,NULL,0,1,'published',2,NULL,0,0,0,NULL,NULL,NULL,1,0,NULL,NULL,NULL,2,'2025-11-04 21:58:23.591025','2025-11-04 21:58:23.591025');
CREATE TABLE video_playlist (
	title VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	description TEXT, 
	cover_media_id INTEGER, 
	is_featured BOOLEAN NOT NULL, 
	is_public BOOLEAN NOT NULL, 
	sort_order INTEGER NOT NULL, 
	video_count INTEGER NOT NULL, 
	total_duration_seconds INTEGER NOT NULL, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cover_media_id) REFERENCES media_file (id)
);
CREATE TABLE booking (
	user_id INTEGER, 
	service_id INTEGER NOT NULL, 
	staff_id INTEGER, 
	booking_number VARCHAR(50) NOT NULL, 
	booking_date DATETIME NOT NULL, 
	duration_minutes INTEGER NOT NULL, 
	end_datetime DATETIME, 
	customer_name VARCHAR(100) NOT NULL, 
	customer_email VARCHAR(100) NOT NULL, 
	customer_phone VARCHAR(50) NOT NULL, 
	status VARCHAR(9) NOT NULL, 
	confirmation_method VARCHAR(6) NOT NULL, 
	price FLOAT, 
	payment_status VARCHAR(8) NOT NULL, 
	payment_method VARCHAR(50), 
	paid_at DATETIME, 
	confirmed_at DATETIME, 
	cancelled_at DATETIME, 
	completed_at DATETIME, 
	reminder_sent_at DATETIME, 
	reminder_count INTEGER NOT NULL, 
	customer_notes TEXT, 
	admin_notes TEXT, 
	cancel_reason TEXT, 
	source VARCHAR(50), 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(service_id) REFERENCES booking_service (id), 
	FOREIGN KEY(staff_id) REFERENCES team_member (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	UNIQUE (booking_number)
);
CREATE TABLE booking_time_slot (
	service_id INTEGER NOT NULL, 
	staff_id INTEGER, 
	date DATETIME NOT NULL, 
	start_time TIME NOT NULL, 
	end_time TIME NOT NULL, 
	is_available BOOLEAN NOT NULL, 
	available_slots INTEGER NOT NULL, 
	booked_slots INTEGER NOT NULL, 
	is_special BOOLEAN NOT NULL, 
	special_price FLOAT, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(service_id) REFERENCES booking_service (id), 
	FOREIGN KEY(staff_id) REFERENCES team_member (id)
);
CREATE TABLE cart (
	user_id INTEGER, 
	session_id VARCHAR(100), 
	is_active INTEGER NOT NULL, 
	converted_to_order_id INTEGER, 
	subtotal FLOAT NOT NULL, 
	estimated_tax FLOAT NOT NULL, 
	estimated_shipping FLOAT NOT NULL, 
	estimated_total FLOAT NOT NULL, 
	coupon_code VARCHAR(50), 
	discount_amount FLOAT NOT NULL, 
	last_activity_at DATETIME, 
	expires_at DATETIME, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(converted_to_order_id) REFERENCES "order" (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);
CREATE TABLE contact_message (
	name VARCHAR(100) NOT NULL, 
	contact_info VARCHAR(200) NOT NULL, 
	message_text TEXT NOT NULL, 
	product_id INTEGER, 
	source_page_url VARCHAR(500), 
	status VARCHAR(7) NOT NULL, 
	handled_at DATETIME, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);
CREATE TABLE custom_field_option (
	field_id INTEGER NOT NULL, 
	value VARCHAR(100) NOT NULL, 
	label VARCHAR(100) NOT NULL, 
	sort_order INTEGER NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(field_id) REFERENCES custom_field_def (id)
);
CREATE TABLE event_registration (
	event_id INTEGER NOT NULL, 
	user_id INTEGER, 
	registration_number VARCHAR(50) NOT NULL, 
	attendee_name VARCHAR(100) NOT NULL, 
	attendee_email VARCHAR(100) NOT NULL, 
	attendee_phone VARCHAR(50), 
	company VARCHAR(200), 
	job_title VARCHAR(100), 
	status VARCHAR(9) NOT NULL, 
	ticket_type VARCHAR(10) NOT NULL, 
	ticket_price FLOAT NOT NULL, 
	payment_status VARCHAR(8) NOT NULL, 
	payment_method VARCHAR(50), 
	payment_transaction_id VARCHAR(100), 
	paid_at DATETIME, 
	registered_at DATETIME, 
	confirmed_at DATETIME, 
	checked_in_at DATETIME, 
	cancelled_at DATETIME, 
	check_in_code VARCHAR(100), 
	is_checked_in BOOLEAN NOT NULL, 
	check_in_method VARCHAR(50), 
	dietary_requirements TEXT, 
	special_needs TEXT, 
	how_heard VARCHAR(100), 
	custom_fields TEXT, 
	notes TEXT, 
	admin_notes TEXT, 
	cancel_reason TEXT, 
	confirmation_email_sent BOOLEAN NOT NULL, 
	reminder_email_sent BOOLEAN NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(event_id) REFERENCES event (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	UNIQUE (registration_number)
);
CREATE TABLE event_ticket_type (
	event_id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	description TEXT, 
	price FLOAT NOT NULL, 
	quantity INTEGER, 
	sold_count INTEGER NOT NULL, 
	sale_start_time DATETIME, 
	sale_end_time DATETIME, 
	is_active BOOLEAN NOT NULL, 
	sort_order INTEGER NOT NULL, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(event_id) REFERENCES event (id)
);
CREATE TABLE file_download_log (
	file_id INTEGER NOT NULL, 
	user_id INTEGER, 
	ip_address VARCHAR(50), 
	user_agent VARCHAR(500), 
	referrer VARCHAR(500), 
	download_status VARCHAR(9) NOT NULL, 
	error_message TEXT, 
	downloaded_at DATETIME, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(file_id) REFERENCES file_download (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);
CREATE TABLE gallery_image (
	gallery_id INTEGER NOT NULL, 
	media_id INTEGER NOT NULL, 
	title VARCHAR(200), 
	caption TEXT, 
	alt_text VARCHAR(255), 
	tags VARCHAR(255), 
	sort_order INTEGER NOT NULL, 
	is_visible BOOLEAN NOT NULL, 
	is_featured BOOLEAN NOT NULL, 
	link_url VARCHAR(500), 
	link_target VARCHAR(20), 
	view_count INTEGER NOT NULL, 
	download_count INTEGER NOT NULL, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(gallery_id) REFERENCES gallery (id), 
	FOREIGN KEY(media_id) REFERENCES media_file (id)
);
CREATE TABLE menu_item (
	category_id INTEGER NOT NULL, 
	name VARCHAR(200) NOT NULL, 
	slug VARCHAR(200) NOT NULL, 
	description TEXT, 
	price FLOAT NOT NULL, 
	original_price FLOAT, 
	image_media_id INTEGER, 
	sizes VARCHAR(255), 
	spice_levels VARCHAR(255), 
	customizations TEXT, 
	calories INTEGER, 
	allergens VARCHAR(255), 
	dietary_tags VARCHAR(255), 
	is_available BOOLEAN NOT NULL, 
	stock_quantity INTEGER, 
	daily_limit INTEGER, 
	today_sold INTEGER NOT NULL, 
	is_recommended BOOLEAN NOT NULL, 
	is_popular BOOLEAN NOT NULL, 
	is_new BOOLEAN NOT NULL, 
	is_seasonal BOOLEAN NOT NULL, 
	sort_order INTEGER NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES menu_category (id), 
	FOREIGN KEY(image_media_id) REFERENCES media_file (id)
);
CREATE TABLE order_item (
	order_id INTEGER NOT NULL, 
	product_id INTEGER, 
	product_name VARCHAR(200) NOT NULL, 
	product_sku VARCHAR(100), 
	product_variant VARCHAR(255), 
	quantity INTEGER NOT NULL, 
	unit_price FLOAT NOT NULL, 
	subtotal FLOAT NOT NULL, 
	discount_amount FLOAT NOT NULL, 
	total_price FLOAT NOT NULL, 
	notes TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(order_id) REFERENCES "order" (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);
CREATE TABLE portfolio_category_link (
	portfolio_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (portfolio_id, category_id), 
	FOREIGN KEY(category_id) REFERENCES portfolio_category (id), 
	FOREIGN KEY(portfolio_id) REFERENCES portfolio (id)
);
CREATE TABLE portfolio_image (
	portfolio_id INTEGER NOT NULL, 
	media_id INTEGER NOT NULL, 
	caption VARCHAR(500), 
	sort_order INTEGER NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(media_id) REFERENCES media_file (id), 
	FOREIGN KEY(portfolio_id) REFERENCES portfolio (id)
);
CREATE TABLE post_category_link (
	post_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (post_id, category_id), 
	FOREIGN KEY(category_id) REFERENCES post_category (id), 
	FOREIGN KEY(post_id) REFERENCES post (id)
);
CREATE TABLE product_category_link (
	product_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (product_id, category_id), 
	FOREIGN KEY(category_id) REFERENCES product_category (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);
CREATE TABLE product_custom_field_value (
	product_id INTEGER NOT NULL, 
	field_id INTEGER NOT NULL, 
	value_text TEXT NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(field_id) REFERENCES custom_field_def (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);
CREATE TABLE review (
	reviewable_type VARCHAR(50) NOT NULL, 
	reviewable_id INTEGER NOT NULL, 
	reviewer_name VARCHAR(100) NOT NULL, 
	reviewer_email VARCHAR(100) NOT NULL, 
	reviewer_photo VARCHAR(500), 
	user_id INTEGER, 
	title VARCHAR(200), 
	content TEXT NOT NULL, 
	overall_rating INTEGER NOT NULL, 
	quality_rating INTEGER, 
	service_rating INTEGER, 
	value_rating INTEGER, 
	is_verified_purchase BOOLEAN NOT NULL, 
	order_id INTEGER, 
	status VARCHAR(8) NOT NULL, 
	is_featured BOOLEAN NOT NULL, 
	helpful_count INTEGER NOT NULL, 
	unhelpful_count INTEGER NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(order_id) REFERENCES "order" (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);
CREATE TABLE video_playlist_link (
	playlist_id INTEGER NOT NULL, 
	video_id INTEGER NOT NULL, 
	sort_order INTEGER NOT NULL, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(playlist_id) REFERENCES video_playlist (id), 
	FOREIGN KEY(video_id) REFERENCES video (id)
);
CREATE TABLE cart_item (
	cart_id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	product_variant VARCHAR(255), 
	product_sku VARCHAR(100), 
	quantity INTEGER NOT NULL, 
	unit_price FLOAT NOT NULL, 
	subtotal FLOAT NOT NULL, 
	discount_amount FLOAT NOT NULL, 
	total_price FLOAT NOT NULL, 
	notes TEXT, 
	added_at DATETIME, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cart_id) REFERENCES cart (id), 
	FOREIGN KEY(product_id) REFERENCES product (id)
);
CREATE TABLE restaurant_order_item (
	order_id INTEGER NOT NULL, 
	menu_item_id INTEGER, 
	item_name VARCHAR(200) NOT NULL, 
	item_description TEXT, 
	quantity INTEGER NOT NULL, 
	unit_price FLOAT NOT NULL, 
	subtotal FLOAT NOT NULL, 
	size_option VARCHAR(50), 
	spice_level VARCHAR(50), 
	customizations TEXT, 
	special_instructions TEXT, 
	id INTEGER NOT NULL, 
	created_at DATETIME NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(menu_item_id) REFERENCES menu_item (id), 
	FOREIGN KEY(order_id) REFERENCES restaurant_order (id)
);
CREATE INDEX idx_site_column_menu_location ON site_column(menu_location);
COMMIT;
