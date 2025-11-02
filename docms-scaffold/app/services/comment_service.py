# -*- coding: utf-8 -*-
"""Comment Service - Comments and reviews management"""

from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.models import Comment, Review


class CommentService:
    """Service class for managing comments"""

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        skip: int = 0,
        limit: int = 100,
        commentable_type: Optional[str] = None,
        commentable_id: Optional[int] = None,
        status: str = "approved",
    ) -> List[Comment]:
        """
        Get all comments with optional filters

        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            commentable_type: Filter by commentable type
            commentable_id: Filter by commentable ID
            status: Filter by status

        Returns:
            List of Comment objects
        """
        query = self.db.query(Comment).options(joinedload(Comment.user)).filter(Comment.status == status)

        if commentable_type:
            query = query.filter(Comment.commentable_type == commentable_type)

        if commentable_id:
            query = query.filter(Comment.commentable_id == commentable_id)

        return query.order_by(Comment.created_at.desc()).offset(skip).limit(limit).all()

    def get_by_id(self, comment_id: int) -> Optional[Comment]:
        """
        Get comment by ID

        Args:
            comment_id: Comment ID

        Returns:
            Comment object or None
        """
        return (
            self.db.query(Comment)
            .options(joinedload(Comment.user), joinedload(Comment.replies))
            .filter(Comment.id == comment_id)
            .first()
        )

    def get_for_item(
        self, commentable_type: str, commentable_id: int, status: str = "approved"
    ) -> List[Comment]:
        """
        Get comments for a specific item

        Args:
            commentable_type: Type of the commentable item
            commentable_id: ID of the commentable item
            status: Filter by status

        Returns:
            List of Comment objects
        """
        return (
            self.db.query(Comment)
            .options(joinedload(Comment.user))
            .filter(
                Comment.commentable_type == commentable_type,
                Comment.commentable_id == commentable_id,
                Comment.status == status,
                Comment.parent_id == None,  # Only top-level comments
            )
            .order_by(Comment.created_at.desc())
            .all()
        )

    def create(self, comment_data: dict) -> Comment:
        """
        Create a new comment

        Args:
            comment_data: Dictionary containing comment data

        Returns:
            Created Comment object
        """
        comment = Comment(**comment_data)
        self.db.add(comment)
        self.db.commit()
        self.db.refresh(comment)
        return comment

    def update(self, comment_id: int, comment_data: dict) -> Optional[Comment]:
        """
        Update comment

        Args:
            comment_id: Comment ID
            comment_data: Dictionary containing updated data

        Returns:
            Updated Comment object or None
        """
        comment = self.get_by_id(comment_id)
        if not comment:
            return None

        for key, value in comment_data.items():
            if hasattr(comment, key):
                setattr(comment, key, value)

        self.db.commit()
        self.db.refresh(comment)
        return comment

    def delete(self, comment_id: int) -> bool:
        """
        Delete comment

        Args:
            comment_id: Comment ID

        Returns:
            True if deleted successfully, False otherwise
        """
        comment = self.get_by_id(comment_id)
        if not comment:
            return False

        self.db.delete(comment)
        self.db.commit()
        return True

    def approve(self, comment_id: int) -> Optional[Comment]:
        """
        Approve a pending comment

        Args:
            comment_id: Comment ID

        Returns:
            Approved Comment object or None
        """
        return self.update(comment_id, {"status": "approved"})

    def mark_as_spam(self, comment_id: int) -> Optional[Comment]:
        """
        Mark comment as spam

        Args:
            comment_id: Comment ID

        Returns:
            Updated Comment object or None
        """
        return self.update(comment_id, {"status": "spam"})


class ReviewService:
    """Service class for managing reviews"""

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        skip: int = 0,
        limit: int = 100,
        reviewable_type: Optional[str] = None,
        reviewable_id: Optional[int] = None,
        status: str = "approved",
    ) -> List[Review]:
        """
        Get all reviews with optional filters

        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            reviewable_type: Filter by reviewable type
            reviewable_id: Filter by reviewable ID
            status: Filter by status

        Returns:
            List of Review objects
        """
        query = self.db.query(Review).options(joinedload(Review.user)).filter(Review.status == status)

        if reviewable_type:
            query = query.filter(Review.reviewable_type == reviewable_type)

        if reviewable_id:
            query = query.filter(Review.reviewable_id == reviewable_id)

        return query.order_by(Review.created_at.desc()).offset(skip).limit(limit).all()

    def get_by_id(self, review_id: int) -> Optional[Review]:
        """
        Get review by ID

        Args:
            review_id: Review ID

        Returns:
            Review object or None
        """
        return self.db.query(Review).options(joinedload(Review.user)).filter(Review.id == review_id).first()

    def get_for_item(self, reviewable_type: str, reviewable_id: int, status: str = "approved") -> List[Review]:
        """
        Get reviews for a specific item

        Args:
            reviewable_type: Type of the reviewable item
            reviewable_id: ID of the reviewable item
            status: Filter by status

        Returns:
            List of Review objects
        """
        return (
            self.db.query(Review)
            .options(joinedload(Review.user))
            .filter(
                Review.reviewable_type == reviewable_type,
                Review.reviewable_id == reviewable_id,
                Review.status == status,
            )
            .order_by(Review.created_at.desc())
            .all()
        )

    def get_featured(self, limit: int = 5, status: str = "approved") -> List[Review]:
        """
        Get featured reviews

        Args:
            limit: Maximum number of reviews to return
            status: Filter by status

        Returns:
            List of featured Review objects
        """
        return (
            self.db.query(Review)
            .options(joinedload(Review.user))
            .filter(Review.is_featured == True, Review.status == status)
            .order_by(Review.created_at.desc())
            .limit(limit)
            .all()
        )

    def create(self, review_data: dict) -> Review:
        """
        Create a new review

        Args:
            review_data: Dictionary containing review data

        Returns:
            Created Review object
        """
        review = Review(**review_data)
        self.db.add(review)
        self.db.commit()
        self.db.refresh(review)
        return review

    def update(self, review_id: int, review_data: dict) -> Optional[Review]:
        """
        Update review

        Args:
            review_id: Review ID
            review_data: Dictionary containing updated data

        Returns:
            Updated Review object or None
        """
        review = self.get_by_id(review_id)
        if not review:
            return None

        for key, value in review_data.items():
            if hasattr(review, key):
                setattr(review, key, value)

        self.db.commit()
        self.db.refresh(review)
        return review

    def delete(self, review_id: int) -> bool:
        """
        Delete review

        Args:
            review_id: Review ID

        Returns:
            True if deleted successfully, False otherwise
        """
        review = self.get_by_id(review_id)
        if not review:
            return False

        self.db.delete(review)
        self.db.commit()
        return True

    def approve(self, review_id: int) -> Optional[Review]:
        """
        Approve a pending review

        Args:
            review_id: Review ID

        Returns:
            Approved Review object or None
        """
        return self.update(review_id, {"status": "approved"})

    def get_average_rating(self, reviewable_type: str, reviewable_id: int) -> float:
        """
        Get average rating for an item

        Args:
            reviewable_type: Type of the reviewable item
            reviewable_id: ID of the reviewable item

        Returns:
            Average rating
        """
        from sqlalchemy import func

        result = (
            self.db.query(func.avg(Review.overall_rating))
            .filter(
                Review.reviewable_type == reviewable_type,
                Review.reviewable_id == reviewable_id,
                Review.status == "approved",
            )
            .scalar()
        )

        return float(result) if result else 0.0
