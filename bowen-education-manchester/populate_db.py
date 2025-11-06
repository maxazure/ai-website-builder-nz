#!/usr/bin/env python3
"""
Populate database with Bowen Education Group seed data
"""
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Add app to path
sys.path.insert(0, str(Path(__file__).parent))

from app.database import SessionLocal
from app.models import (
    SiteSetting,
    SiteColumn,
    ColumnType,
    Product,
    ProductCategory,
    ProductCategoryLink,
    Post,
    PostCategory,
    PostCategoryLink,
    TeamMember,
    Event,
    EventTicketType,
    FAQ,
    FAQCategory,
    Video,
    VideoCategory,
    FileCategory,
    FileDownload,
    BookingService,
    ContactMessage,
)


def populate_site_settings(db):
    """Populate site settings (key-value pairs)"""
    settings = [
        ("site_name", "Bowen Education Group", "string"),
        ("site_name_chinese", "博文集团", "string"),
        ("tagline", "Bridging East and West Through Education", "string"),
        ("tagline_chinese", "中西融汇，博学致远", "string"),
        ("company_phone", "+44 (0)161 6672668", "string"),
        ("company_email", "info@boweneducation.org", "string"),
        ("company_address", "1/F, 2A Curzon Road, Sale, Manchester, M33 7DR, UK", "string"),
        ("company_wechat", "bowenedu_uk", "string"),
        ("founded_year", "2018", "string"),
        ("business_hours", "Monday - Friday: 9:00 - 17:00, Saturday - Sunday: 10:00 - 16:00", "string"),
        ("mission", "To provide high-quality Chinese language education and cultural enrichment programmes that bridge Eastern and Western educational traditions, empowering students to succeed in a globalised world.", "string"),
        ("vision", "To be the leading Chinese education provider in Greater Manchester, recognised for academic excellence, cultural authenticity, and community impact.", "string"),
        ("about_description", "Bowen Education Group is a registered educational institution in Manchester, UK, offering comprehensive Chinese language programmes from Foundation to A-Level, academic tutoring, chess club, badminton club, and government-funded community programmes.", "string"),
    ]

    for key, value, value_type in settings:
        setting = SiteSetting(
            setting_key=key,
            value_text=value,
            value_type=value_type
        )
        db.add(setting)

    db.commit()
    print(f"✓ Added {len(settings)} site settings")


def populate_site_columns(db):
    """Populate site navigation structure"""
    columns = [
        # Top level navigation
        {"name": "Home", "slug": "home", "type": ColumnType.SINGLE_PAGE, "sort": 1},
        {"name": "About Us", "slug": "about", "type": ColumnType.SINGLE_PAGE, "sort": 2},
        {"name": "Chinese School", "slug": "school", "type": ColumnType.PRODUCT, "sort": 3},
        {"name": "Tuition Centre", "slug": "tuition", "type": ColumnType.PRODUCT, "sort": 4},
        {"name": "Clubs & Activities", "slug": "clubs", "type": ColumnType.CUSTOM, "sort": 5},
        {"name": "Community Programmes", "slug": "programmes", "type": ColumnType.CUSTOM, "sort": 6},
        {"name": "Events", "slug": "events", "type": ColumnType.CUSTOM, "sort": 7},
        {"name": "News & Resources", "slug": "news", "type": ColumnType.POST, "sort": 8},
        {"name": "Gallery", "slug": "gallery", "type": ColumnType.CUSTOM, "sort": 9},
        {"name": "FAQ", "slug": "faq", "type": ColumnType.CUSTOM, "sort": 10},
        {"name": "Contact", "slug": "contact", "type": ColumnType.SINGLE_PAGE, "sort": 11},
    ]

    for col_data in columns:
        column = SiteColumn(
            name=col_data["name"],
            slug=col_data["slug"],
            column_type=col_data["type"],
            sort_order=col_data["sort"],
            show_in_nav=True,
            is_enabled=True
        )
        db.add(column)

    db.commit()
    print(f"✓ Added {len(columns)} site columns")

    # Return columns for foreign key references
    return {col.slug: col for col in db.query(SiteColumn).all()}


def populate_product_categories(db, columns):
    """Populate course categories"""
    school_col = columns.get("school")
    tuition_col = columns.get("tuition")

    categories = [
        {"name": "Chinese Language Courses", "slug": "chinese-language", "column_id": school_col.id if school_col else None, "sort": 1},
        {"name": "Academic Tutoring", "slug": "academic-tutoring", "column_id": tuition_col.id if tuition_col else None, "sort": 2},
        {"name": "Exam Preparation", "slug": "exam-preparation", "column_id": school_col.id if school_col else None, "sort": 3},
        {"name": "Adult Classes", "slug": "adult-classes", "column_id": school_col.id if school_col else None, "sort": 4},
    ]

    for cat_data in categories:
        category = ProductCategory(
            column_id=cat_data["column_id"],
            name=cat_data["name"],
            slug=cat_data["slug"],
            sort_order=cat_data["sort"],
            is_visible=True
        )
        db.add(category)

    db.commit()
    print(f"✓ Added {len(categories)} product categories")

    return {cat.slug: cat for cat in db.query(ProductCategory).all()}


def populate_products(db, columns, categories):
    """Populate courses/products"""
    school_col = columns.get("school")
    tuition_col = columns.get("tuition")

    products = [
        # Chinese School Courses
        {
            "column_id": school_col.id if school_col else None,
            "name": "Foundation Mandarin (Ages 5-7)",
            "slug": "foundation-mandarin",
            "summary": "Playful introduction to Mandarin for young learners through songs, games, and stories",
            "description_html": "<p>Our Foundation Mandarin programme is designed for children aged 5-7 who are just beginning their Chinese language journey...</p>",
            "price_text": "£180 per term",
            "availability_status": "in_stock",
            "is_recommended": True,
            "status": "published",
            "published_at": datetime.now(),
        },
        {
            "column_id": school_col.id if school_col else None,
            "name": "GCSE Chinese (Ages 14-16)",
            "slug": "gcse-chinese",
            "summary": "Comprehensive GCSE Chinese preparation aligned with AQA/Edexcel specifications",
            "description_html": "<p>Our GCSE Chinese programme provides comprehensive preparation for the AQA or Edexcel GCSE Chinese examinations...</p>",
            "price_text": "£240 per term",
            "availability_status": "in_stock",
            "is_recommended": True,
            "status": "published",
            "published_at": datetime.now(),
        },
        {
            "column_id": school_col.id if school_col else None,
            "name": "A-Level Chinese (Ages 16-18)",
            "slug": "a-level-chinese",
            "summary": "Advanced Chinese language and literature course for university-bound students",
            "description_html": "<p>Our A-Level Chinese programme offers advanced study of Chinese language and literature...</p>",
            "price_text": "£280 per term",
            "availability_status": "in_stock",
            "is_recommended": True,
            "status": "published",
            "published_at": datetime.now(),
        },
        {
            "column_id": school_col.id if school_col else None,
            "name": "HSK Level 3 Preparation",
            "slug": "hsk-level-3",
            "summary": "Targeted preparation for the HSK Level 3 examination with mock tests",
            "description_html": "<p>Our HSK Level 3 preparation course is designed to help students pass the HSK Level 3 examination...</p>",
            "price_text": "£200 per term",
            "availability_status": "in_stock",
            "is_recommended": False,
            "status": "published",
            "published_at": datetime.now(),
        },
        {
            "column_id": school_col.id if school_col else None,
            "name": "Cantonese Language Course",
            "slug": "cantonese-language",
            "summary": "Preserve your Cantonese heritage with our authentic language programme",
            "description_html": "<p>Our Cantonese language course helps students maintain and develop their Cantonese language skills...</p>",
            "price_text": "£180 per term",
            "availability_status": "in_stock",
            "is_recommended": False,
            "status": "published",
            "published_at": datetime.now(),
        },
        # Tuition Centre Courses
        {
            "column_id": tuition_col.id if tuition_col else None,
            "name": "GCSE Mathematics Tutoring",
            "slug": "gcse-mathematics",
            "summary": "Expert GCSE Maths tutoring with focus on problem-solving and exam technique",
            "description_html": "<p>Our GCSE Mathematics tutoring provides comprehensive support for students preparing for their GCSE exams...</p>",
            "price_text": "£30 per hour",
            "availability_status": "in_stock",
            "is_recommended": True,
            "status": "published",
            "published_at": datetime.now(),
        },
        {
            "column_id": tuition_col.id if tuition_col else None,
            "name": "A-Level Physics Tutoring",
            "slug": "a-level-physics",
            "summary": "One-to-one A-Level Physics tutoring from experienced educators",
            "description_html": "<p>Our A-Level Physics tutoring provides personalized support for students studying A-Level Physics...</p>",
            "price_text": "£35 per hour",
            "availability_status": "in_stock",
            "is_recommended": False,
            "status": "published",
            "published_at": datetime.now(),
        },
    ]

    for prod_data in products:
        product = Product(**prod_data)
        db.add(product)

    db.commit()
    print(f"✓ Added {len(products)} products/courses")


def populate_team(db):
    """Populate team members"""
    team_members = [
        {
            "name": "Dr. Bowen Zhang",
            "title": "Founder & Director",
            "department": "Leadership",
            "email": "bowen.zhang@boweneducation.org",
            "bio": "Dr. Bowen Zhang founded Bowen Education Group in 2018 with a vision to bridge Eastern and Western educational traditions. With a PhD in Education from the University of Manchester and over 15 years of teaching experience, Dr. Zhang has developed innovative Chinese language curricula that have helped hundreds of students achieve fluency and cultural competence.",
            "qualifications": "PhD in Education (University of Manchester), MA in Chinese Linguistics (Peking University), QTS (UK)",
            "specialties": "Chinese Language Education, Curriculum Development, Educational Leadership",
            "is_featured": True,
            "is_active": True,
            "sort_order": 1,
        },
        {
            "name": "Miss Emily Chen",
            "title": "Head of Chinese School",
            "department": "Chinese School",
            "email": "emily.chen@boweneducation.org",
            "bio": "Miss Emily Chen leads our Chinese School with passion and expertise. A native Mandarin speaker with over 10 years of teaching experience, Emily holds a Master's degree in Teaching Chinese as a Foreign Language and is certified by Hanban (Confucius Institute Headquarters).",
            "qualifications": "MA in TCFL (Beijing Language and Culture University), Hanban Certified Chinese Teacher",
            "specialties": "Mandarin Teaching, YCT/HSK Preparation, Children's Language Development",
            "is_featured": True,
            "is_active": True,
            "sort_order": 2,
        },
        {
            "name": "Mr. James Wilson",
            "title": "Head of Tuition Centre",
            "department": "Tuition Centre",
            "email": "james.wilson@boweneducation.org",
            "bio": "Mr. James Wilson brings extensive experience in British secondary education to his role as Head of Tuition Centre. With 12 years of teaching experience in Manchester schools and a track record of helping students achieve top grades, James specializes in GCSE and A-Level exam preparation.",
            "qualifications": "BSc Mathematics (University of Cambridge), PGCE Secondary Mathematics, QTS",
            "specialties": "GCSE/A-Level Mathematics, Physics, Exam Technique",
            "is_featured": True,
            "is_active": True,
            "sort_order": 3,
        },
    ]

    for member_data in team_members:
        member = TeamMember(**member_data)
        db.add(member)

    db.commit()
    print(f"✓ Added {len(team_members)} team members")


def populate_posts(db, columns):
    """Populate blog posts/news articles"""
    news_col = columns.get("news")

    # Create post categories first
    categories = [
        {"name": "School News", "slug": "school-news", "column_id": news_col.id if news_col else None, "sort": 1},
        {"name": "Events", "slug": "events", "column_id": news_col.id if news_col else None, "sort": 2},
        {"name": "Student Success", "slug": "student-success", "column_id": news_col.id if news_col else None, "sort": 3},
    ]

    for cat_data in categories:
        category = PostCategory(
            column_id=cat_data["column_id"],
            name=cat_data["name"],
            slug=cat_data["slug"],
            sort_order=cat_data["sort"],
            is_visible=True
        )
        db.add(category)

    db.commit()

    posts = [
        {
            "column_id": news_col.id if news_col else None,
            "title": "Bowen Education Partners with Henan University",
            "slug": "henan-university-partnership",
            "summary": "Exciting new partnership brings authentic Chinese teaching resources to Manchester",
            "content_html": "<p>We are thrilled to announce our strategic partnership with Henan University, one of China's leading institutions for teacher training...</p>",
            "is_recommended": True,
            "is_approved": True,
            "status": "published",
            "published_at": datetime.now() - timedelta(days=7),
        },
        {
            "column_id": news_col.id if news_col else None,
            "title": "100% Pass Rate in GCSE Chinese 2024",
            "slug": "gcse-results-2024",
            "summary": "Our students achieve outstanding results with 100% pass rate and 85% achieving grades 7-9",
            "content_html": "<p>We are incredibly proud to announce that our GCSE Chinese students achieved a 100% pass rate in the 2024 examinations...</p>",
            "is_recommended": True,
            "is_approved": True,
            "status": "published",
            "published_at": datetime.now() - timedelta(days=14),
        },
    ]

    for post_data in posts:
        post = Post(**post_data)
        db.add(post)

    db.commit()
    print(f"✓ Added {len(posts)} news posts")


def populate_events(db):
    """Populate events"""
    events = [
        {
            "title": "Chinese New Year Celebration 2025",
            "slug": "chinese-new-year-2025",
            "description": "Join us for our annual Chinese New Year celebration featuring traditional performances, calligraphy workshops, dumpling making, and lion dance!",
            "summary": "Annual Chinese New Year celebration with performances and cultural activities",
            "event_type": "cultural",
            "start_datetime": datetime(2025, 2, 10, 14, 0),
            "end_datetime": datetime(2025, 2, 10, 17, 0),
            "location_type": "physical",
            "venue_name": "Manchester Community Centre",
            "venue_address": "123 Main Street",
            "venue_city": "Manchester",
            "venue_postal_code": "M1 1AA",
            "max_attendees": 200,
            "current_attendees": 0,
            "allow_waitlist": True,
            "waitlist_count": 0,
            "is_free": False,
            "ticket_price": 5.0,
            "is_featured": True,
            "is_public": True,
            "status": "published",
            "organizer_name": "Bowen Education Group",
            "organizer_email": "info@boweneducation.org",
        },
        {
            "title": "HSK Level 3 Mock Examination",
            "slug": "hsk-3-mock-exam",
            "description": "Full mock examination for HSK Level 3 students including listening, reading, and writing sections. Get familiarized with exam format and timing.",
            "summary": "Practice HSK Level 3 exam under real conditions",
            "event_type": "exam",
            "start_datetime": datetime(2025, 3, 15, 10, 0),
            "end_datetime": datetime(2025, 3, 15, 12, 0),
            "location_type": "physical",
            "venue_name": "Bowen Education Centre",
            "venue_address": "1/F, 2A Curzon Road, Sale",
            "venue_city": "Manchester",
            "venue_postal_code": "M33 7DR",
            "max_attendees": 40,
            "current_attendees": 0,
            "allow_waitlist": False,
            "waitlist_count": 0,
            "is_free": True,
            "is_featured": False,
            "is_public": False,
            "status": "published",
            "organizer_name": "Bowen Education Group",
            "organizer_email": "info@boweneducation.org",
        },
    ]

    for event_data in events:
        event = Event(**event_data)
        db.add(event)

    db.commit()
    print(f"✓ Added {len(events)} events")


def populate_faqs(db):
    """Populate FAQs"""
    # Create FAQ categories first
    categories = [
        {"name": "Enrolment", "slug": "enrolment", "sort": 1},
        {"name": "Courses", "slug": "courses", "sort": 2},
        {"name": "Fees & Payment", "slug": "fees-payment", "sort": 3},
        {"name": "Facilities", "slug": "facilities", "sort": 4},
    ]

    for cat_data in categories:
        category = FAQCategory(
            name=cat_data["name"],
            slug=cat_data["slug"],
            sort_order=cat_data["sort"],
            is_visible=True
        )
        db.add(category)

    db.commit()

    faqs = [
        {
            "category": "Enrolment",
            "question": "How do I enroll my child in Chinese School?",
            "answer": "<p>You can enroll your child by filling out our online registration form or visiting our centre in person. We offer a free trial class so your child can experience our teaching approach before committing to a term.</p>",
            "sort_order": 1,
            "is_visible": True,
            "is_pinned": True,
        },
        {
            "category": "Courses",
            "question": "What is the difference between HSK and YCT examinations?",
            "answer": "<p>HSK (Hanyu Shuiping Kaoshi) is the standardized Chinese proficiency test for adults, while YCT (Youth Chinese Test) is designed specifically for young learners aged 15 and under. YCT has a more age-appropriate vocabulary and testing format.</p>",
            "sort_order": 2,
            "is_visible": True,
            "is_pinned": False,
        },
        {
            "category": "Fees & Payment",
            "question": "What are your fees and payment terms?",
            "answer": "<p>Our fees are charged per term (12 weeks). Payment is due at the start of each term. We accept bank transfer, card payments, and cash. Sibling discounts of 10% are available for families enrolling multiple children.</p>",
            "sort_order": 3,
            "is_visible": True,
            "is_pinned": False,
        },
    ]

    for faq_data in faqs:
        faq = FAQ(**faq_data)
        db.add(faq)

    db.commit()
    print(f"✓ Added {len(faqs)} FAQs")


def populate_videos(db):
    """Populate videos"""
    # Create video categories first
    categories = [
        {"name": "Student Performances", "slug": "performances", "sort": 1},
        {"name": "Cultural Events", "slug": "cultural-events", "sort": 2},
        {"name": "Teaching Resources", "slug": "teaching-resources", "sort": 3},
    ]

    for cat_data in categories:
        category = VideoCategory(
            name=cat_data["name"],
            slug=cat_data["slug"],
            description="",
            sort_order=cat_data["sort"],
            is_visible=True
        )
        db.add(category)

    db.commit()

    # Get first category for videos
    perf_category = db.query(VideoCategory).filter_by(slug="performances").first()

    videos = [
        {
            "title": "Chinese New Year 2024 Highlights",
            "slug": "cny-2024-highlights",
            "description": "Highlights from our spectacular Chinese New Year 2024 celebration featuring student performances and cultural activities.",
            "category_id": perf_category.id if perf_category else None,
            "video_source": "youtube",
            "youtube_id": "example1",
            "duration_seconds": 180,
            "autoplay": False,
            "loop": False,
            "muted": False,
            "controls": True,
            "has_subtitles": False,
            "is_featured": True,
            "is_public": True,
            "status": "published",
            "sort_order": 1,
            "view_count": 0,
            "like_count": 0,
            "share_count": 0,
            "allow_embed": True,
            "requires_login": False,
        },
        {
            "title": "Student Dragon Dance Performance",
            "slug": "dragon-dance-performance",
            "description": "Our talented students perform a traditional Chinese dragon dance at the Manchester Chinese Cultural Festival.",
            "category_id": perf_category.id if perf_category else None,
            "video_source": "youtube",
            "youtube_id": "example2",
            "duration_seconds": 240,
            "autoplay": False,
            "loop": False,
            "muted": False,
            "controls": True,
            "has_subtitles": False,
            "is_featured": False,
            "is_public": True,
            "status": "published",
            "sort_order": 2,
            "view_count": 0,
            "like_count": 0,
            "share_count": 0,
            "allow_embed": True,
            "requires_login": False,
        },
    ]

    for video_data in videos:
        video = Video(**video_data)
        db.add(video)

    db.commit()
    print(f"✓ Added {len(videos)} videos")


def populate_file_downloads(db):
    """Populate downloadable files"""
    # Create file categories first
    categories = [
        {"name": "Enrolment Forms", "slug": "enrolment", "sort": 1},
        {"name": "Course Materials", "slug": "course-materials", "sort": 2},
        {"name": "Policies", "slug": "policies", "sort": 3},
    ]

    for cat_data in categories:
        category = FileCategory(
            name=cat_data["name"],
            slug=cat_data["slug"],
            sort_order=cat_data["sort"],
            is_visible=True
        )
        db.add(category)

    db.commit()
    print(f"✓ Added {len(categories)} file categories")

    # Note: Skipping file downloads for now as they require actual media files
    # These will be added later when media files are uploaded


def populate_booking_services(db):
    """Populate booking services"""
    services = [
        {
            "name": "Free Trial Class (Chinese School)",
            "slug": "trial-class-chinese",
            "description": "Book a free 45-minute trial class for your child to experience our Chinese School programme",
            "duration_minutes": 45,
            "price": 0.0,
            "buffer_time_minutes": 15,
            "max_capacity": 8,
            "allow_waitlist": True,
            "min_advance_hours": 24,
            "max_advance_days": 30,
            "allow_cancel_hours": 24,
            "is_active": True,
            "sort_order": 1,
        },
        {
            "name": "Parent Consultation",
            "slug": "parent-consultation",
            "description": "One-on-one consultation with our education team to discuss your child's learning needs",
            "duration_minutes": 30,
            "price": 0.0,
            "buffer_time_minutes": 10,
            "max_capacity": 1,
            "allow_waitlist": False,
            "min_advance_hours": 48,
            "max_advance_days": 14,
            "allow_cancel_hours": 48,
            "is_active": True,
            "sort_order": 2,
        },
    ]

    for service_data in services:
        service = BookingService(**service_data)
        db.add(service)

    db.commit()
    print(f"✓ Added {len(services)} booking services")


def main():
    """Main function to populate all data"""
    print("=" * 60)
    print("Bowen Education Group - Database Population Script")
    print("=" * 60)
    print()

    db = SessionLocal()

    try:
        print("Populating database with seed data...\n")

        populate_site_settings(db)
        columns = populate_site_columns(db)
        categories = populate_product_categories(db, columns)
        populate_products(db, columns, categories)
        populate_team(db)
        populate_posts(db, columns)
        populate_events(db)
        populate_faqs(db)
        populate_videos(db)
        populate_file_downloads(db)
        populate_booking_services(db)

        print()
        print("=" * 60)
        print("✅ Database population completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error populating database: {e}")
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    main()
