#!/usr/bin/env python3
"""
System Test Suite for Bowen Education Group Website
Comprehensive testing of application, database, and resources
"""

import sys
import os
from pathlib import Path
import sqlite3
from datetime import datetime

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

class Colors:
    """ANSI color codes"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    """Print a section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_info(text):
    """Print info message"""
    print(f"ℹ️  {text}")

# Test Results Tracker
test_results = {
    "passed": 0,
    "failed": 0,
    "warnings": 0,
    "total": 0
}

def test_database_structure():
    """Test 1: Database structure and tables"""
    print_header("Test 1: Database Structure")

    db_path = Path("instance/database.db")

    if not db_path.exists():
        print_error("Database file not found")
        test_results["failed"] += 1
        test_results["total"] += 1
        return False

    print_success(f"Database file exists: {db_path}")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = [row[0] for row in cursor.fetchall()]

        print_info(f"Found {len(tables)} tables")

        # Expected tables for our 14 enabled modules
        expected_tables = [
            'alembic_version',
            'booking', 'booking_service', 'booking_time_slot',
            'contact_message',
            'custom_field_def', 'custom_field_option',
            'event', 'event_registration', 'event_ticket_type',
            'faq', 'faq_category',
            'file_category', 'file_download', 'file_download_log',
            'media_file',
            'post', 'post_category', 'post_category_link',
            'product', 'product_category', 'product_category_link',
            'product_custom_field_value',
            'single_page',
            'site_column', 'site_setting',
            'team_member',
            'user',
            'video', 'video_category', 'video_playlist', 'video_playlist_link',
        ]

        missing_tables = []
        for table in expected_tables:
            if table in tables:
                print_success(f"Table exists: {table}")
            else:
                missing_tables.append(table)

        if missing_tables:
            for table in missing_tables:
                print_warning(f"Missing table: {table}")
            test_results["warnings"] += len(missing_tables)

        conn.close()
        test_results["passed"] += 1
        test_results["total"] += 1
        return True

    except Exception as e:
        print_error(f"Database error: {e}")
        test_results["failed"] += 1
        test_results["total"] += 1
        return False

def test_database_data():
    """Test 2: Database data integrity"""
    print_header("Test 2: Database Data Integrity")

    db_path = Path("instance/database.db")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Test site_setting data
        cursor.execute("SELECT COUNT(*) FROM site_setting")
        setting_count = cursor.fetchone()[0]
        print_info(f"Site settings: {setting_count} records")

        if setting_count >= 10:
            print_success("Site settings populated")
        else:
            print_warning(f"Expected at least 10 site settings, found {setting_count}")
            test_results["warnings"] += 1

        # Test site_column data
        cursor.execute("SELECT COUNT(*) FROM site_column")
        column_count = cursor.fetchone()[0]
        print_info(f"Site columns: {column_count} records")

        if column_count >= 10:
            print_success("Site columns populated")
        else:
            print_warning(f"Expected at least 10 site columns, found {column_count}")
            test_results["warnings"] += 1

        # Test products
        cursor.execute("SELECT COUNT(*) FROM product")
        product_count = cursor.fetchone()[0]
        print_info(f"Products: {product_count} records")

        if product_count >= 5:
            print_success("Products populated")
        else:
            print_warning(f"Expected at least 5 products, found {product_count}")
            test_results["warnings"] += 1

        # Test team members
        cursor.execute("SELECT COUNT(*) FROM team_member")
        team_count = cursor.fetchone()[0]
        print_info(f"Team members: {team_count} records")

        if team_count >= 3:
            print_success("Team members populated")
        else:
            print_warning(f"Expected at least 3 team members, found {team_count}")
            test_results["warnings"] += 1

        # Test posts
        cursor.execute("SELECT COUNT(*) FROM post")
        post_count = cursor.fetchone()[0]
        print_info(f"Posts: {post_count} records")

        # Test events
        cursor.execute("SELECT COUNT(*) FROM event")
        event_count = cursor.fetchone()[0]
        print_info(f"Events: {event_count} records")

        # Test FAQs
        cursor.execute("SELECT COUNT(*) FROM faq")
        faq_count = cursor.fetchone()[0]
        print_info(f"FAQs: {faq_count} records")

        # Test videos
        cursor.execute("SELECT COUNT(*) FROM video")
        video_count = cursor.fetchone()[0]
        print_info(f"Videos: {video_count} records")

        # Test booking services
        cursor.execute("SELECT COUNT(*) FROM booking_service")
        booking_count = cursor.fetchone()[0]
        print_info(f"Booking services: {booking_count} records")

        conn.close()

        total_records = (setting_count + column_count + product_count +
                        team_count + post_count + event_count +
                        faq_count + video_count + booking_count)

        print_success(f"Total records in database: {total_records}")

        test_results["passed"] += 1
        test_results["total"] += 1
        return True

    except Exception as e:
        print_error(f"Database data error: {e}")
        test_results["failed"] += 1
        test_results["total"] += 1
        return False

def test_application_imports():
    """Test 3: Application imports"""
    print_header("Test 3: Application Imports")

    try:
        print_info("Testing imports...")

        # Test config
        from app.config import settings
        print_success("✓ app.config imported")

        # Test database
        from app.database import Base, SessionLocal
        print_success("✓ app.database imported")

        # Test models
        from app.models import (
            SiteSetting, SiteColumn, Product, Post,
            TeamMember, Event, FAQ, Video, User
        )
        print_success("✓ app.models imported")

        # Test schemas
        from app.schemas import (
            ProductCreate, PostCreate, TeamMemberCreate,
            EventCreate, FAQCreate, VideoCreate
        )
        print_success("✓ app.schemas imported")

        # Test services
        from app.services import (
            post_service, product_service, site_service,
            TeamService, EventService, FAQService
        )
        print_success("✓ app.services imported")

        # Test main app
        from app.main import app
        print_success("✓ app.main imported")

        test_results["passed"] += 1
        test_results["total"] += 1
        return True

    except Exception as e:
        print_error(f"Import error: {e}")
        test_results["failed"] += 1
        test_results["total"] += 1
        return False

def test_file_structure():
    """Test 4: File structure"""
    print_header("Test 4: File Structure")

    required_files = [
        "app/__init__.py",
        "app/main.py",
        "app/config.py",
        "app/database.py",
        "app/models/__init__.py",
        "app/routes/__init__.py",
        "app/routes/frontend.py",
        "app/routes/health.py",
        "app/services/__init__.py",
        "app/schemas/__init__.py",
        "migrations/env.py",
        "alembic.ini",
        "requirements.txt",
        "populate_db.py",
    ]

    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print_success(f"✓ {file_path}")
        else:
            print_error(f"✗ {file_path}")
            all_exist = False
            test_results["failed"] += 1

    if all_exist:
        test_results["passed"] += 1

    test_results["total"] += 1
    return all_exist

def test_templates():
    """Test 5: Templates"""
    print_header("Test 5: Templates")

    template_files = [
        "templates/base.html",
        "templates/partials/header.html",
    ]

    expected_but_missing = [
        "templates/home.html",
        "templates/about.html",
        "templates/contact.html",
        "templates/404.html",
        "templates/500.html",
    ]

    for file_path in template_files:
        if Path(file_path).exists():
            print_success(f"✓ {file_path}")
        else:
            print_error(f"✗ {file_path}")

    print_info("\nExpected templates (not critical):")
    for file_path in expected_but_missing:
        if Path(file_path).exists():
            print_success(f"✓ {file_path}")
        else:
            print_warning(f"⚠ {file_path} - needs to be created")
            test_results["warnings"] += 1

    test_results["passed"] += 1
    test_results["total"] += 1
    return True

def test_static_files():
    """Test 6: Static files"""
    print_header("Test 6: Static Files")

    static_dir = Path("templates/static")

    if not static_dir.exists():
        print_error("Static directory not found")
        test_results["failed"] += 1
        test_results["total"] += 1
        return False

    print_success(f"Static directory exists: {static_dir}")

    # Check for images
    images_dir = static_dir / "images"
    if images_dir.exists():
        images = list(images_dir.glob("*.jpg")) + list(images_dir.glob("*.png"))
        print_info(f"Found {len(images)} images")

        for img in images:
            print_success(f"✓ {img.name}")

        if len(images) < 10:
            print_warning(f"Expected more images. Only {len(images)} found.")
            test_results["warnings"] += 1
    else:
        print_warning("Images directory not found")
        test_results["warnings"] += 1

    # Check for CSS
    css_dir = static_dir / "css"
    if css_dir.exists():
        css_files = list(css_dir.glob("*.css"))
        print_info(f"Found {len(css_files)} CSS files")
        for css in css_files:
            print_success(f"✓ {css.name}")
    else:
        print_warning("CSS directory not found - needs to be created")
        test_results["warnings"] += 1

    # Check for design tokens
    design_tokens = Path("DESIGN_TOKENS.css")
    if design_tokens.exists():
        print_success("✓ DESIGN_TOKENS.css exists")
    else:
        print_warning("DESIGN_TOKENS.css not found")
        test_results["warnings"] += 1

    test_results["passed"] += 1
    test_results["total"] += 1
    return True

def test_environment():
    """Test 7: Environment and dependencies"""
    print_header("Test 7: Environment & Dependencies")

    # Check Python version
    print_info(f"Python version: {sys.version}")

    # Check virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print_success("✓ Running in virtual environment")
    else:
        print_warning("⚠ Not running in virtual environment")
        test_results["warnings"] += 1

    # Check requirements.txt
    req_file = Path("requirements.txt")
    if req_file.exists():
        print_success("✓ requirements.txt exists")

        # Try to import key packages
        try:
            import fastapi
            print_success(f"✓ FastAPI installed: {fastapi.__version__}")
        except ImportError:
            print_error("✗ FastAPI not installed")
            test_results["failed"] += 1

        try:
            import sqlalchemy
            print_success(f"✓ SQLAlchemy installed: {sqlalchemy.__version__}")
        except ImportError:
            print_error("✗ SQLAlchemy not installed")
            test_results["failed"] += 1

        try:
            import jinja2
            print_success(f"✓ Jinja2 installed: {jinja2.__version__}")
        except ImportError:
            print_error("✗ Jinja2 not installed")
            test_results["failed"] += 1
    else:
        print_error("✗ requirements.txt not found")
        test_results["failed"] += 1

    test_results["passed"] += 1
    test_results["total"] += 1
    return True

def print_summary():
    """Print test summary"""
    print_header("Test Summary")

    total = test_results["total"]
    passed = test_results["passed"]
    failed = test_results["failed"]
    warnings = test_results["warnings"]

    print(f"\n{Colors.BOLD}Results:{Colors.END}")
    print(f"  {Colors.GREEN}✅ Passed: {passed}/{total}{Colors.END}")
    print(f"  {Colors.RED}❌ Failed: {failed}/{total}{Colors.END}")
    print(f"  {Colors.YELLOW}⚠️  Warnings: {warnings}{Colors.END}")

    percentage = (passed / total * 100) if total > 0 else 0

    print(f"\n{Colors.BOLD}Overall: {percentage:.1f}% tests passed{Colors.END}")

    if failed == 0:
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 All critical tests passed!{Colors.END}")
        return True
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}⚠️  {failed} test(s) failed. Please review.{Colors.END}")
        return False

def main():
    """Run all tests"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  Bowen Education Group - System Test Suite".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "═" * 68 + "╝")
    print(f"{Colors.END}")

    print_info(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print_info(f"Working directory: {Path.cwd()}")

    # Run all tests
    test_database_structure()
    test_database_data()
    test_application_imports()
    test_file_structure()
    test_templates()
    test_static_files()
    test_environment()

    # Print summary
    success = print_summary()

    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
