# -*- coding: utf-8 -*-
"""Order Service - Order management"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.models import Order, OrderItem


class OrderService:
    """Service class for managing orders"""

    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        skip: int = 0,
        limit: int = 100,
        status: Optional[str] = None,
        user_id: Optional[int] = None,
        payment_status: Optional[str] = None,
    ) -> List[Order]:
        """
        Get all orders with optional filters

        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            status: Filter by status
            user_id: Filter by user ID
            payment_status: Filter by payment status

        Returns:
            List of Order objects
        """
        query = self.db.query(Order).options(joinedload(Order.items))

        if status:
            query = query.filter(Order.status == status)

        if user_id:
            query = query.filter(Order.user_id == user_id)

        if payment_status:
            query = query.filter(Order.payment_status == payment_status)

        return query.order_by(Order.created_at.desc()).offset(skip).limit(limit).all()

    def get_by_id(self, order_id: int) -> Optional[Order]:
        """
        Get order by ID

        Args:
            order_id: Order ID

        Returns:
            Order object or None
        """
        return (
            self.db.query(Order)
            .options(joinedload(Order.items).joinedload(OrderItem.product))
            .filter(Order.id == order_id)
            .first()
        )

    def get_by_order_number(self, order_number: str) -> Optional[Order]:
        """
        Get order by order number

        Args:
            order_number: Order number

        Returns:
            Order object or None
        """
        return (
            self.db.query(Order)
            .options(joinedload(Order.items).joinedload(OrderItem.product))
            .filter(Order.order_number == order_number)
            .first()
        )

    def get_user_orders(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Order]:
        """
        Get orders for a specific user

        Args:
            user_id: User ID
            skip: Number of records to skip
            limit: Maximum number of records to return

        Returns:
            List of Order objects
        """
        return (
            self.db.query(Order)
            .options(joinedload(Order.items))
            .filter(Order.user_id == user_id)
            .order_by(Order.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, order_data: dict, items_data: List[dict]) -> Order:
        """
        Create a new order with items

        Args:
            order_data: Dictionary containing order data
            items_data: List of dictionaries containing order item data

        Returns:
            Created Order object
        """
        # Create order
        order = Order(**order_data)
        self.db.add(order)
        self.db.flush()  # Flush to get order ID

        # Create order items
        for item_data in items_data:
            item_data["order_id"] = order.id
            item = OrderItem(**item_data)
            self.db.add(item)

        self.db.commit()
        self.db.refresh(order)
        return order

    def update(self, order_id: int, order_data: dict) -> Optional[Order]:
        """
        Update order

        Args:
            order_id: Order ID
            order_data: Dictionary containing updated data

        Returns:
            Updated Order object or None
        """
        order = self.get_by_id(order_id)
        if not order:
            return None

        for key, value in order_data.items():
            if hasattr(order, key) and key not in ["id", "order_number", "created_at"]:
                setattr(order, key, value)

        self.db.commit()
        self.db.refresh(order)
        return order

    def update_status(self, order_id: int, status: str) -> Optional[Order]:
        """
        Update order status

        Args:
            order_id: Order ID
            status: New status

        Returns:
            Updated Order object or None
        """
        order = self.get_by_id(order_id)
        if not order:
            return None

        order.status = status

        # Update timestamps based on status
        now = datetime.utcnow()
        if status == "confirmed":
            order.confirmed_at = now
        elif status == "shipped":
            order.shipped_at = now
        elif status == "delivered":
            order.delivered_at = now
        elif status == "cancelled":
            order.cancelled_at = now

        self.db.commit()
        self.db.refresh(order)
        return order

    def update_payment_status(self, order_id: int, payment_status: str, paid_amount: float = 0.0) -> Optional[Order]:
        """
        Update order payment status

        Args:
            order_id: Order ID
            payment_status: New payment status
            paid_amount: Amount paid

        Returns:
            Updated Order object or None
        """
        order = self.get_by_id(order_id)
        if not order:
            return None

        order.payment_status = payment_status
        if paid_amount > 0:
            order.paid_amount = paid_amount

        if payment_status == "paid":
            order.paid_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(order)
        return order

    def add_tracking_info(self, order_id: int, carrier: str, tracking_number: str, tracking_url: Optional[str] = None) -> Optional[Order]:
        """
        Add tracking information to order

        Args:
            order_id: Order ID
            carrier: Shipping carrier
            tracking_number: Tracking number
            tracking_url: Tracking URL

        Returns:
            Updated Order object or None
        """
        order = self.get_by_id(order_id)
        if not order:
            return None

        order.shipping_carrier = carrier
        order.tracking_number = tracking_number
        if tracking_url:
            order.tracking_url = tracking_url

        self.db.commit()
        self.db.refresh(order)
        return order

    def cancel_order(self, order_id: int, cancel_reason: Optional[str] = None) -> Optional[Order]:
        """
        Cancel an order

        Args:
            order_id: Order ID
            cancel_reason: Reason for cancellation

        Returns:
            Updated Order object or None
        """
        order = self.get_by_id(order_id)
        if not order:
            return None

        order.status = "cancelled"
        order.cancelled_at = datetime.utcnow()
        if cancel_reason:
            order.cancel_reason = cancel_reason

        self.db.commit()
        self.db.refresh(order)
        return order

    def delete(self, order_id: int) -> bool:
        """
        Delete order

        Args:
            order_id: Order ID

        Returns:
            True if deleted successfully, False otherwise
        """
        order = self.get_by_id(order_id)
        if not order:
            return False

        self.db.delete(order)
        self.db.commit()
        return True

    def get_count(
        self,
        status: Optional[str] = None,
        user_id: Optional[int] = None,
        payment_status: Optional[str] = None,
    ) -> int:
        """
        Get total count of orders

        Args:
            status: Filter by status
            user_id: Filter by user ID
            payment_status: Filter by payment status

        Returns:
            Count of orders
        """
        query = self.db.query(Order)

        if status:
            query = query.filter(Order.status == status)

        if user_id:
            query = query.filter(Order.user_id == user_id)

        if payment_status:
            query = query.filter(Order.payment_status == payment_status)

        return query.count()

    def get_revenue_stats(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> dict:
        """
        Get revenue statistics

        Args:
            start_date: Start date for stats
            end_date: End date for stats

        Returns:
            Dictionary containing revenue statistics
        """
        from sqlalchemy import func

        query = self.db.query(
            func.count(Order.id).label("order_count"),
            func.sum(Order.total_amount).label("total_revenue"),
            func.avg(Order.total_amount).label("average_order_value"),
        ).filter(Order.payment_status == "paid")

        if start_date:
            query = query.filter(Order.created_at >= start_date)

        if end_date:
            query = query.filter(Order.created_at <= end_date)

        result = query.first()

        return {
            "order_count": result.order_count or 0,
            "total_revenue": float(result.total_revenue or 0),
            "average_order_value": float(result.average_order_value or 0),
        }
