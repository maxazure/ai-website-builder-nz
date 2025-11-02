# -*- coding: utf-8 -*-
"""Site Service - Site columns, settings, single pages"""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models import SinglePage, SiteColumn, SiteSetting
from app.utils.cache import cache_navigation, cache_settings


@cache_navigation
def get_navigation(db: Session) -> List[SiteColumn]:
    """
    Get navigation menu items (cached for 10 minutes)

    Returns:
        List of enabled columns that should appear in navigation
    """
    return (
        db.query(SiteColumn)
        .filter(SiteColumn.is_enabled == True, SiteColumn.show_in_nav == True)
        .order_by(SiteColumn.sort_order)
        .all()
    )


def get_column_by_slug(db: Session, slug: str) -> Optional[SiteColumn]:
    """
    Get column by slug

    Args:
        db: Database session
        slug: Column slug

    Returns:
        SiteColumn object or None
    """
    return (
        db.query(SiteColumn)
        .filter(SiteColumn.slug == slug, SiteColumn.is_enabled == True)
        .first()
    )


def get_single_page(db: Session, column_id: int) -> Optional[SinglePage]:
    """
    Get single page by column ID

    Args:
        db: Database session
        column_id: Column ID

    Returns:
        SinglePage object or None
    """
    return (
        db.query(SinglePage)
        .filter(SinglePage.column_id == column_id, SinglePage.status == "published")
        .first()
    )


@cache_settings
def get_site_setting(db: Session, key: str) -> Optional[str]:
    """
    Get site setting value by key (cached for 10 minutes)

    Args:
        db: Database session
        key: Setting key

    Returns:
        Setting value or None
    """
    setting = db.query(SiteSetting).filter(SiteSetting.setting_key == key).first()
    return setting.value_text if setting else None


@cache_settings
def get_all_site_settings(db: Session) -> dict:
    """
    Get all site settings as a dictionary (cached for 10 minutes)

    Args:
        db: Database session

    Returns:
        Dictionary of settings {key: value}
    """
    settings = db.query(SiteSetting).all()
    return {s.setting_key: s.value_text for s in settings}
