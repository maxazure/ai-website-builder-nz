#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Import news data from news_content.json to database
导入新闻数据到数据库
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.post import Post
from app.models.site import SiteColumn
from app.database import Base

# Database configuration
DATABASE_URL = "sqlite:///instance/database.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def import_news_data(json_file: str = "news_content.json"):
    """Import news data from JSON file"""
    
    # Load JSON data
    print(f"📄 Loading news data from: {json_file}")
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    articles = data["news_articles"]
    print(f"📰 Found {len(articles)} articles to import")
    print()
    
    # Create session
    db = SessionLocal()
    
    try:
        # Get news column
        news_column = db.query(SiteColumn).filter_by(slug="news").first()
        
        if not news_column:
            print("❌ Error: News column not found in database")
            print("   Please ensure the 'news' column exists in site_column table")
            return False
        
        print(f"✅ Found news column: {news_column.name} (ID: {news_column.id})")
        print()
        
        # Import each article
        success_count = 0
        skip_count = 0
        
        for i, article in enumerate(articles, 1):
            slug = article["slug"]
            
            # Check if article already exists
            existing_post = db.query(Post).filter_by(
                column_id=news_column.id,
                slug=slug
            ).first()
            
            if existing_post:
                print(f"[{i}/{len(articles)}] ⏭️  Skipped (already exists): {article['title']}")
                skip_count += 1
                continue
            
            # Parse published date
            published_at = datetime.fromisoformat(article["published_at"].replace("T", " "))
            
            # Create new post
            new_post = Post(
                column_id=news_column.id,
                title=article["title"],
                slug=slug,
                summary=article["summary"],
                content_html=article["content"],
                status="published",
                is_recommended=False,
                published_at=published_at,
                seo_title=article["title"],
                seo_description=article["summary"]
            )
            
            db.add(new_post)
            success_count += 1
            print(f"[{i}/{len(articles)}] ✅ Imported: {article['title']}")
        
        # Commit changes
        db.commit()
        
        print()
        print("=" * 60)
        print("📊 Import Summary")
        print("=" * 60)
        print(f"Total articles: {len(articles)}")
        print(f"✅ Successfully imported: {success_count}")
        print(f"⏭️  Skipped (already exists): {skip_count}")
        print()
        print("✅ All news data has been imported successfully!")
        print()
        print("Next steps:")
        print("1. Generate images: python tools/generate_images.py --config news_images.json")
        print("2. Start the server: uvicorn app.main:app --host 0.0.0.0 --port 8002")
        print("3. Visit: http://192.168.31.205:8002/news")
        
        return True
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error importing news data: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        db.close()


if __name__ == "__main__":
    import_news_data()
