#!/usr/bin/env python3
"""
Import Media Files Script
Import existing image files into the media_file table
"""

import sys
import os
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from app.database import SessionLocal
from app.models import MediaFile


def get_image_dimensions(image_path):
    """Get image dimensions (requires PIL/Pillow - optional)"""
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            return img.width, img.height
    except ImportError:
        # PIL not installed, skip dimensions
        return None, None
    except Exception as e:
        print(f"  Warning: Could not read dimensions: {e}")
        return None, None


def import_media_files():
    """Import all media files from templates/static/images/"""
    db = SessionLocal()

    try:
        # Check if media files already exist
        existing_count = db.query(MediaFile).count()
        if existing_count > 0:
            print(f"⚠️  Media files already exist in database ({existing_count} records)")
            response = input("Do you want to re-import? This will delete existing records. (y/N): ")
            if response.lower() != 'y':
                print("Import cancelled.")
                return

            # Delete existing records
            db.query(MediaFile).delete()
            db.commit()
            print(f"✓ Deleted {existing_count} existing media records")

        images_dir = Path("templates/static/images")

        if not images_dir.exists():
            print(f"❌ Error: Images directory not found: {images_dir}")
            return

        # Get all image files
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
        image_files = []
        for ext in image_extensions:
            image_files.extend(images_dir.glob(f"*{ext}"))

        if not image_files:
            print(f"❌ No image files found in {images_dir}")
            return

        print(f"\n📁 Found {len(image_files)} image files")
        print("=" * 70)

        imported_count = 0

        for image_path in sorted(image_files):
            filename = image_path.name
            file_size = image_path.stat().st_size

            # Determine MIME type
            extension = image_path.suffix.lower()
            mime_type_map = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif',
                '.webp': 'image/webp'
            }
            mime_type = mime_type_map.get(extension, 'image/jpeg')

            # Get image dimensions
            width, height = get_image_dimensions(image_path)

            # Create relative path for storage
            relative_path = f"/static/images/{filename}"

            # Create MediaFile record
            media_file = MediaFile(
                filename_original=filename,
                mime_type=mime_type,
                size_bytes=file_size,
                width=width,
                height=height,
                path_original=relative_path,
                path_medium=relative_path,  # Same as original for now
                path_thumb=relative_path     # Same as original for now
            )

            db.add(media_file)
            imported_count += 1

            # Display info
            size_kb = file_size / 1024
            dimensions = f"{width}x{height}" if width and height else "unknown"
            print(f"✓ {filename:40s} {size_kb:>6.1f} KB  {dimensions:>12s}")

        # Commit all changes
        db.commit()

        print("=" * 70)
        print(f"✅ Successfully imported {imported_count} media files")

        # Display summary
        total_size = sum(f.stat().st_size for f in image_files)
        print(f"\n📊 Summary:")
        print(f"   Total files: {imported_count}")
        print(f"   Total size: {total_size / 1024 / 1024:.2f} MB")

        # Show database records
        all_media = db.query(MediaFile).all()
        print(f"\n📋 Media files in database:")
        for media in all_media:
            print(f"   ID: {media.id:3d} | {media.filename_original}")

    except Exception as e:
        db.rollback()
        print(f"\n❌ Error during import: {e}")
        import traceback
        traceback.print_exc()

    finally:
        db.close()


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("  Media Files Import Script")
    print("  Bowen Education Group")
    print("=" * 70)

    import_media_files()

    print("\n✓ Import complete!")
