# -*- coding: utf-8 -*-
"""Restaurant Service - Restaurant ordering management"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.models import RestaurantOrder, RestaurantOrderItem, MenuItem, MenuCategory


class RestaurantService:
    """Service class for managing restaurant orders and menu"""

    def __init__(self, db: Session):
        self.db = db

    # Menu management
    def get_menu_categories(self, is_active: bool = True) -> List[MenuCategory]:
        """Get all menu categories"""
        query = self.db.query(MenuCategory)
        if is_active:
            query = query.filter(MenuCategory.is_active == is_active)
        return query.order_by(MenuCategory.sort_order).all()

    def get_menu_items(
        self, category_id: Optional[int] = None, is_available: bool = True
    ) -> List[MenuItem]:
        """Get menu items"""
        query = self.db.query(MenuItem).options(joinedload(MenuItem.category), joinedload(MenuItem.image))

        if category_id:
            query = query.filter(MenuItem.category_id == category_id)

        if is_available:
            query = query.filter(MenuItem.is_available == is_available)

        return query.order_by(MenuItem.sort_order).all()

    def get_menu_item_by_id(self, item_id: int) -> Optional[MenuItem]:
        """Get menu item by ID"""
        return (
            self.db.query(MenuItem)
            .options(joinedload(MenuItem.category), joinedload(MenuItem.image))
            .filter(MenuItem.id == item_id)
            .first()
        )

    # Order management
    def get_all_orders(
        self,
        skip: int = 0,
        limit: int = 100,
        status: Optional[str] = None,
        order_type: Optional[str] = None,
    ) -> List[RestaurantOrder]:
        """Get all restaurant orders"""
        query = self.db.query(RestaurantOrder).options(joinedload(RestaurantOrder.items))

        if status:
            query = query.filter(RestaurantOrder.status == status)

        if order_type:
            query = query.filter(RestaurantOrder.order_type == order_type)

        return query.order_by(RestaurantOrder.created_at.desc()).offset(skip).limit(limit).all()

    def get_order_by_id(self, order_id: int) -> Optional[RestaurantOrder]:
        """Get order by ID"""
        return (
            self.db.query(RestaurantOrder)
            .options(joinedload(RestaurantOrder.items).joinedload(RestaurantOrderItem.menu_item))
            .filter(RestaurantOrder.id == order_id)
            .first()
        )

    def get_order_by_number(self, order_number: str) -> Optional[RestaurantOrder]:
        """Get order by order number"""
        return (
            self.db.query(RestaurantOrder)
            .options(joinedload(RestaurantOrder.items))
            .filter(RestaurantOrder.order_number == order_number)
            .first()
        )

    def create_order(self, order_data: dict, items_data: List[dict]) -> RestaurantOrder:
        """Create a new restaurant order"""
        order = RestaurantOrder(**order_data)
        self.db.add(order)
        self.db.flush()

        for item_data in items_data:
            item_data["order_id"] = order.id
            item = RestaurantOrderItem(**item_data)
            self.db.add(item)

        self.db.commit()
        self.db.refresh(order)
        return order

    def update_order(self, order_id: int, order_data: dict) -> Optional[RestaurantOrder]:
        """Update order"""
        order = self.get_order_by_id(order_id)
        if not order:
            return None

        for key, value in order_data.items():
            if hasattr(order, key) and key not in ["id", "order_number", "created_at"]:
                setattr(order, key, value)

        self.db.commit()
        self.db.refresh(order)
        return order

    def update_order_status(self, order_id: int, status: str) -> Optional[RestaurantOrder]:
        """Update order status"""
        order = self.get_order_by_id(order_id)
        if not order:
            return None

        order.status = status

        now = datetime.utcnow()
        if status == "confirmed":
            order.confirmed_at = now
        elif status == "preparing":
            order.preparing_at = now
        elif status == "ready":
            order.ready_at = now
        elif status == "delivering":
            pass
        elif status == "completed":
            order.completed_at = now
        elif status == "cancelled":
            order.cancelled_at = now

        self.db.commit()
        self.db.refresh(order)
        return order

    def cancel_order(self, order_id: int, cancel_reason: Optional[str] = None) -> Optional[RestaurantOrder]:
        """Cancel an order"""
        order = self.get_order_by_id(order_id)
        if not order:
            return None

        order.status = "cancelled"
        order.cancelled_at = datetime.utcnow()
        if cancel_reason:
            order.cancel_reason = cancel_reason

        self.db.commit()
        self.db.refresh(order)
        return order

    def delete_order(self, order_id: int) -> bool:
        """Delete order"""
        order = self.get_order_by_id(order_id)
        if not order:
            return False

        self.db.delete(order)
        self.db.commit()
        return True

    def get_order_count(self, status: Optional[str] = None, order_type: Optional[str] = None) -> int:
        """Get total count of orders"""
        query = self.db.query(RestaurantOrder)

        if status:
            query = query.filter(RestaurantOrder.status == status)

        if order_type:
            query = query.filter(RestaurantOrder.order_type == order_type)

        return query.count()
