# -*- coding: utf-8 -*-
"""Gallery Service - Image gallery management"""

from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.models import Gallery, GalleryImage


class GalleryService:
    """Service class for managing image galleries"""

    def __init__(self, db: Session):
        self.db = db

    # Gallery management
    def get_all_galleries(
        self,
        skip: int = 0,
        limit: int = 100,
        is_public: bool = True,
        is_featured: Optional[bool] = None,
        category: Optional[str] = None,
    ) -> List[Gallery]:
        """Get all galleries with optional filters"""
        query = self.db.query(Gallery).options(joinedload(Gallery.cover_media))

        if is_public:
            query = query.filter(Gallery.is_public == is_public)

        if is_featured is not None:
            query = query.filter(Gallery.is_featured == is_featured)

        if category:
            query = query.filter(Gallery.category == category)

        return query.order_by(Gallery.sort_order.desc(), Gallery.id.desc()).offset(skip).limit(limit).all()

    def get_gallery_by_id(self, gallery_id: int) -> Optional[Gallery]:
        """Get gallery by ID"""
        return (
            self.db.query(Gallery)
            .options(
                joinedload(Gallery.cover_media),
                joinedload(Gallery.images).joinedload(GalleryImage.media),
            )
            .filter(Gallery.id == gallery_id)
            .first()
        )

    def get_gallery_by_slug(self, slug: str, is_public: bool = True) -> Optional[Gallery]:
        """Get gallery by slug"""
        query = (
            self.db.query(Gallery)
            .options(
                joinedload(Gallery.cover_media),
                joinedload(Gallery.images).joinedload(GalleryImage.media),
            )
            .filter(Gallery.slug == slug)
        )

        if is_public:
            query = query.filter(Gallery.is_public == is_public)

        return query.first()

    def get_featured_galleries(self, limit: int = 6) -> List[Gallery]:
        """Get featured galleries"""
        return (
            self.db.query(Gallery)
            .options(joinedload(Gallery.cover_media))
            .filter(Gallery.is_featured == True, Gallery.is_public == True)
            .order_by(Gallery.sort_order.desc())
            .limit(limit)
            .all()
        )

    def create_gallery(self, gallery_data: dict) -> Gallery:
        """Create a new gallery"""
        gallery = Gallery(**gallery_data)
        self.db.add(gallery)
        self.db.commit()
        self.db.refresh(gallery)
        return gallery

    def update_gallery(self, gallery_id: int, gallery_data: dict) -> Optional[Gallery]:
        """Update gallery"""
        gallery = self.get_gallery_by_id(gallery_id)
        if not gallery:
            return None

        for key, value in gallery_data.items():
            if hasattr(gallery, key) and key not in ["id", "created_at"]:
                setattr(gallery, key, value)

        self.db.commit()
        self.db.refresh(gallery)
        return gallery

    def delete_gallery(self, gallery_id: int) -> bool:
        """Delete gallery"""
        gallery = self.get_gallery_by_id(gallery_id)
        if not gallery:
            return False

        self.db.delete(gallery)
        self.db.commit()
        return True

    def increment_view_count(self, gallery_id: int) -> Optional[Gallery]:
        """Increment gallery view count"""
        gallery = self.get_gallery_by_id(gallery_id)
        if not gallery:
            return None

        gallery.view_count += 1
        self.db.commit()
        self.db.refresh(gallery)
        return gallery

    # Gallery image management
    def get_gallery_images(self, gallery_id: int, is_visible: bool = True) -> List[GalleryImage]:
        """Get images for a gallery"""
        query = (
            self.db.query(GalleryImage)
            .options(joinedload(GalleryImage.media))
            .filter(GalleryImage.gallery_id == gallery_id)
        )

        if is_visible:
            query = query.filter(GalleryImage.is_visible == is_visible)

        return query.order_by(GalleryImage.sort_order).all()

    def get_image_by_id(self, image_id: int) -> Optional[GalleryImage]:
        """Get gallery image by ID"""
        return (
            self.db.query(GalleryImage)
            .options(joinedload(GalleryImage.media))
            .filter(GalleryImage.id == image_id)
            .first()
        )

    def add_image(self, image_data: dict) -> GalleryImage:
        """Add image to gallery"""
        image = GalleryImage(**image_data)
        self.db.add(image)
        self.db.commit()
        self.db.refresh(image)

        # Update gallery image count
        gallery = self.get_gallery_by_id(image.gallery_id)
        if gallery:
            gallery.image_count = len(gallery.images)
            self.db.commit()

        return image

    def update_image(self, image_id: int, image_data: dict) -> Optional[GalleryImage]:
        """Update gallery image"""
        image = self.get_image_by_id(image_id)
        if not image:
            return None

        for key, value in image_data.items():
            if hasattr(image, key) and key not in ["id", "created_at"]:
                setattr(image, key, value)

        self.db.commit()
        self.db.refresh(image)
        return image

    def delete_image(self, image_id: int) -> bool:
        """Delete gallery image"""
        image = self.get_image_by_id(image_id)
        if not image:
            return False

        gallery_id = image.gallery_id
        self.db.delete(image)
        self.db.commit()

        # Update gallery image count
        gallery = self.get_gallery_by_id(gallery_id)
        if gallery:
            gallery.image_count = len(gallery.images)
            self.db.commit()

        return True

    def get_gallery_count(self, is_public: bool = True, category: Optional[str] = None) -> int:
        """Get total count of galleries"""
        query = self.db.query(Gallery)

        if is_public:
            query = query.filter(Gallery.is_public == is_public)

        if category:
            query = query.filter(Gallery.category == category)

        return query.count()
