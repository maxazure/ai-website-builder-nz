# -*- coding: utf-8 -*-
"""Portfolio Service - Portfolio/case study management"""

from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.models import Portfolio, PortfolioCategory
from app.utils.cache import cache_content


class PortfolioService:
    """Service class for managing portfolios and case studies"""

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        skip: int = 0,
        limit: int = 100,
        status: str = "published",
        is_featured: Optional[bool] = None,
        category_id: Optional[int] = None,
    ) -> List[Portfolio]:
        """
        Get all portfolios with optional filters

        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            status: Filter by status
            is_featured: Filter by featured status
            category_id: Filter by category ID

        Returns:
            List of Portfolio objects
        """
        query = (
            self.db.query(Portfolio)
            .options(
                joinedload(Portfolio.cover_media),
                joinedload(Portfolio.client_logo),
                joinedload(Portfolio.categories),
            )
            .filter(Portfolio.status == status)
        )

        if is_featured is not None:
            query = query.filter(Portfolio.is_featured == is_featured)

        if category_id:
            query = query.join(Portfolio.categories).filter(PortfolioCategory.id == category_id)

        return query.order_by(Portfolio.sort_order.desc(), Portfolio.id.desc()).offset(skip).limit(limit).all()

    def get_by_id(self, portfolio_id: int) -> Optional[Portfolio]:
        """
        Get portfolio by ID

        Args:
            portfolio_id: Portfolio ID

        Returns:
            Portfolio object or None
        """
        return (
            self.db.query(Portfolio)
            .options(
                joinedload(Portfolio.cover_media),
                joinedload(Portfolio.client_logo),
                joinedload(Portfolio.categories),
                joinedload(Portfolio.images),
            )
            .filter(Portfolio.id == portfolio_id)
            .first()
        )

    def get_by_slug(self, slug: str, status: str = "published") -> Optional[Portfolio]:
        """
        Get portfolio by slug

        Args:
            slug: Portfolio slug
            status: Filter by status

        Returns:
            Portfolio object or None
        """
        return (
            self.db.query(Portfolio)
            .options(
                joinedload(Portfolio.cover_media),
                joinedload(Portfolio.client_logo),
                joinedload(Portfolio.categories),
                joinedload(Portfolio.images),
            )
            .filter(Portfolio.slug == slug, Portfolio.status == status)
            .first()
        )

    def get_featured(self, limit: int = 6, status: str = "published") -> List[Portfolio]:
        """
        Get featured portfolios

        Args:
            limit: Maximum number of portfolios to return
            status: Filter by status

        Returns:
            List of featured Portfolio objects
        """
        return (
            self.db.query(Portfolio)
            .options(joinedload(Portfolio.cover_media), joinedload(Portfolio.categories))
            .filter(Portfolio.is_featured == True, Portfolio.status == status)
            .order_by(Portfolio.sort_order.desc())
            .limit(limit)
            .all()
        )

    def get_categories(self, visible_only: bool = True) -> List[PortfolioCategory]:
        """
        Get portfolio categories

        Args:
            visible_only: Only return visible categories

        Returns:
            List of PortfolioCategory objects
        """
        query = self.db.query(PortfolioCategory)

        if visible_only:
            query = query.filter(PortfolioCategory.is_visible == True)

        return query.order_by(PortfolioCategory.sort_order).all()

    def create(self, portfolio_data: dict) -> Portfolio:
        """
        Create a new portfolio

        Args:
            portfolio_data: Dictionary containing portfolio data

        Returns:
            Created Portfolio object
        """
        portfolio = Portfolio(**portfolio_data)
        self.db.add(portfolio)
        self.db.commit()
        self.db.refresh(portfolio)
        return portfolio

    def update(self, portfolio_id: int, portfolio_data: dict) -> Optional[Portfolio]:
        """
        Update portfolio

        Args:
            portfolio_id: Portfolio ID
            portfolio_data: Dictionary containing updated data

        Returns:
            Updated Portfolio object or None
        """
        portfolio = self.get_by_id(portfolio_id)
        if not portfolio:
            return None

        for key, value in portfolio_data.items():
            if hasattr(portfolio, key) and key not in ["id", "created_at", "updated_at"]:
                setattr(portfolio, key, value)

        self.db.commit()
        self.db.refresh(portfolio)
        return portfolio

    def delete(self, portfolio_id: int) -> bool:
        """
        Delete portfolio

        Args:
            portfolio_id: Portfolio ID

        Returns:
            True if deleted successfully, False otherwise
        """
        portfolio = self.get_by_id(portfolio_id)
        if not portfolio:
            return False

        self.db.delete(portfolio)
        self.db.commit()
        return True

    def get_count(self, status: str = "published", category_id: Optional[int] = None) -> int:
        """
        Get total count of portfolios

        Args:
            status: Filter by status
            category_id: Filter by category ID

        Returns:
            Count of portfolios
        """
        query = self.db.query(Portfolio).filter(Portfolio.status == status)

        if category_id:
            query = query.join(Portfolio.categories).filter(PortfolioCategory.id == category_id)

        return query.count()
