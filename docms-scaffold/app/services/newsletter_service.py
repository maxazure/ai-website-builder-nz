# -*- coding: utf-8 -*-
"""Newsletter Service - Newsletter subscription management"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models import NewsletterSubscriber, NewsletterCampaign


class NewsletterService:
    """Service class for managing newsletter subscriptions"""

    def __init__(self, db: Session):
        self.db = db

    def get_all_subscribers(
        self,
        skip: int = 0,
        limit: int = 100,
        status: Optional[str] = "active",
    ) -> List[NewsletterSubscriber]:
        """
        Get all newsletter subscribers

        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            status: Filter by status

        Returns:
            List of NewsletterSubscriber objects
        """
        query = self.db.query(NewsletterSubscriber)

        if status:
            query = query.filter(NewsletterSubscriber.status == status)

        return query.order_by(NewsletterSubscriber.created_at.desc()).offset(skip).limit(limit).all()

    def get_subscriber_by_id(self, subscriber_id: int) -> Optional[NewsletterSubscriber]:
        """
        Get subscriber by ID

        Args:
            subscriber_id: Subscriber ID

        Returns:
            NewsletterSubscriber object or None
        """
        return self.db.query(NewsletterSubscriber).filter(NewsletterSubscriber.id == subscriber_id).first()

    def get_subscriber_by_email(self, email: str) -> Optional[NewsletterSubscriber]:
        """
        Get subscriber by email

        Args:
            email: Email address

        Returns:
            NewsletterSubscriber object or None
        """
        return self.db.query(NewsletterSubscriber).filter(NewsletterSubscriber.email == email).first()

    def subscribe(self, email: str, **kwargs) -> Optional[NewsletterSubscriber]:
        """
        Subscribe an email to newsletter

        Args:
            email: Email address
            **kwargs: Additional subscriber data

        Returns:
            NewsletterSubscriber object or None if already subscribed
        """
        # Check if email already exists
        existing = self.get_subscriber_by_email(email)
        if existing:
            # If previously unsubscribed, reactivate
            if existing.status == "unsubscribed":
                existing.status = "active"
                existing.subscribed_at = datetime.utcnow()
                existing.unsubscribed_at = None
                self.db.commit()
                self.db.refresh(existing)
                return existing
            # Already active subscriber
            return None

        # Create new subscriber
        subscriber_data = {"email": email, "status": "active", "subscribed_at": datetime.utcnow()}
        subscriber_data.update(kwargs)

        subscriber = NewsletterSubscriber(**subscriber_data)
        self.db.add(subscriber)
        self.db.commit()
        self.db.refresh(subscriber)
        return subscriber

    def unsubscribe(self, email: str, reason: Optional[str] = None) -> Optional[NewsletterSubscriber]:
        """
        Unsubscribe an email from newsletter

        Args:
            email: Email address
            reason: Unsubscribe reason

        Returns:
            Updated NewsletterSubscriber object or None
        """
        subscriber = self.get_subscriber_by_email(email)
        if not subscriber:
            return None

        subscriber.status = "unsubscribed"
        subscriber.unsubscribed_at = datetime.utcnow()
        if reason:
            subscriber.unsubscribe_reason = reason

        self.db.commit()
        self.db.refresh(subscriber)
        return subscriber

    def verify_subscriber(self, subscriber_id: int) -> Optional[NewsletterSubscriber]:
        """
        Verify a subscriber

        Args:
            subscriber_id: Subscriber ID

        Returns:
            Updated NewsletterSubscriber object or None
        """
        subscriber = self.get_subscriber_by_id(subscriber_id)
        if not subscriber:
            return None

        subscriber.is_verified = True
        subscriber.status = "active"
        self.db.commit()
        self.db.refresh(subscriber)
        return subscriber

    def update_subscriber(self, subscriber_id: int, subscriber_data: dict) -> Optional[NewsletterSubscriber]:
        """
        Update subscriber

        Args:
            subscriber_id: Subscriber ID
            subscriber_data: Dictionary containing updated data

        Returns:
            Updated NewsletterSubscriber object or None
        """
        subscriber = self.get_subscriber_by_id(subscriber_id)
        if not subscriber:
            return None

        for key, value in subscriber_data.items():
            if hasattr(subscriber, key):
                setattr(subscriber, key, value)

        self.db.commit()
        self.db.refresh(subscriber)
        return subscriber

    def delete_subscriber(self, subscriber_id: int) -> bool:
        """
        Delete subscriber

        Args:
            subscriber_id: Subscriber ID

        Returns:
            True if deleted successfully, False otherwise
        """
        subscriber = self.get_subscriber_by_id(subscriber_id)
        if not subscriber:
            return False

        self.db.delete(subscriber)
        self.db.commit()
        return True

    def get_subscribers_count(self, status: Optional[str] = "active") -> int:
        """
        Get total count of subscribers

        Args:
            status: Filter by status

        Returns:
            Count of subscribers
        """
        query = self.db.query(NewsletterSubscriber)

        if status:
            query = query.filter(NewsletterSubscriber.status == status)

        return query.count()

    # Campaign management methods
    def get_all_campaigns(
        self, skip: int = 0, limit: int = 100, status: Optional[str] = None
    ) -> List[NewsletterCampaign]:
        """
        Get all newsletter campaigns

        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            status: Filter by status

        Returns:
            List of NewsletterCampaign objects
        """
        query = self.db.query(NewsletterCampaign)

        if status:
            query = query.filter(NewsletterCampaign.status == status)

        return query.order_by(NewsletterCampaign.created_at.desc()).offset(skip).limit(limit).all()

    def get_campaign_by_id(self, campaign_id: int) -> Optional[NewsletterCampaign]:
        """
        Get campaign by ID

        Args:
            campaign_id: Campaign ID

        Returns:
            NewsletterCampaign object or None
        """
        return self.db.query(NewsletterCampaign).filter(NewsletterCampaign.id == campaign_id).first()

    def create_campaign(self, campaign_data: dict) -> NewsletterCampaign:
        """
        Create a new newsletter campaign

        Args:
            campaign_data: Dictionary containing campaign data

        Returns:
            Created NewsletterCampaign object
        """
        campaign = NewsletterCampaign(**campaign_data)
        self.db.add(campaign)
        self.db.commit()
        self.db.refresh(campaign)
        return campaign

    def update_campaign(self, campaign_id: int, campaign_data: dict) -> Optional[NewsletterCampaign]:
        """
        Update newsletter campaign

        Args:
            campaign_id: Campaign ID
            campaign_data: Dictionary containing updated data

        Returns:
            Updated NewsletterCampaign object or None
        """
        campaign = self.get_campaign_by_id(campaign_id)
        if not campaign:
            return None

        for key, value in campaign_data.items():
            if hasattr(campaign, key):
                setattr(campaign, key, value)

        self.db.commit()
        self.db.refresh(campaign)
        return campaign

    def delete_campaign(self, campaign_id: int) -> bool:
        """
        Delete newsletter campaign

        Args:
            campaign_id: Campaign ID

        Returns:
            True if deleted successfully, False otherwise
        """
        campaign = self.get_campaign_by_id(campaign_id)
        if not campaign:
            return False

        self.db.delete(campaign)
        self.db.commit()
        return True
