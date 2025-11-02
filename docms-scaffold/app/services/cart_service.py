# -*- coding: utf-8 -*-
"""Cart Service - Shopping cart management"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from app.models import Cart, CartItem


class CartService:
    """Service class for managing shopping carts"""

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, cart_id: int) -> Optional[Cart]:
        """
        Get cart by ID

        Args:
            cart_id: Cart ID

        Returns:
            Cart object or None
        """
        return (
            self.db.query(Cart)
            .options(joinedload(Cart.items).joinedload(CartItem.product))
            .filter(Cart.id == cart_id)
            .first()
        )

    def get_by_user(self, user_id: int, is_active: bool = True) -> Optional[Cart]:
        """
        Get active cart for a user

        Args:
            user_id: User ID
            is_active: Filter by active status

        Returns:
            Cart object or None
        """
        return (
            self.db.query(Cart)
            .options(joinedload(Cart.items).joinedload(CartItem.product))
            .filter(Cart.user_id == user_id, Cart.is_active == (1 if is_active else 0))
            .first()
        )

    def get_by_session(self, session_id: str, is_active: bool = True) -> Optional[Cart]:
        """
        Get active cart for a guest session

        Args:
            session_id: Session ID
            is_active: Filter by active status

        Returns:
            Cart object or None
        """
        return (
            self.db.query(Cart)
            .options(joinedload(Cart.items).joinedload(CartItem.product))
            .filter(Cart.session_id == session_id, Cart.is_active == (1 if is_active else 0))
            .first()
        )

    def get_or_create_cart(self, user_id: Optional[int] = None, session_id: Optional[str] = None) -> Cart:
        """
        Get existing cart or create a new one

        Args:
            user_id: User ID (for logged-in users)
            session_id: Session ID (for guest users)

        Returns:
            Cart object
        """
        if user_id:
            cart = self.get_by_user(user_id)
        elif session_id:
            cart = self.get_by_session(session_id)
        else:
            raise ValueError("Either user_id or session_id must be provided")

        if not cart:
            cart = Cart(
                user_id=user_id,
                session_id=session_id,
                is_active=1,
                last_activity_at=datetime.utcnow(),
            )
            self.db.add(cart)
            self.db.commit()
            self.db.refresh(cart)

        return cart

    def add_item(
        self,
        cart_id: int,
        product_id: int,
        quantity: int = 1,
        unit_price: float = 0.0,
        **kwargs,
    ) -> CartItem:
        """
        Add item to cart or update quantity if already exists

        Args:
            cart_id: Cart ID
            product_id: Product ID
            quantity: Quantity to add
            unit_price: Unit price
            **kwargs: Additional item data

        Returns:
            CartItem object
        """
        # Check if item already exists in cart
        existing_item = (
            self.db.query(CartItem)
            .filter(CartItem.cart_id == cart_id, CartItem.product_id == product_id)
            .first()
        )

        if existing_item:
            # Update quantity
            existing_item.quantity += quantity
            existing_item.subtotal = existing_item.unit_price * existing_item.quantity
            existing_item.total_price = existing_item.subtotal - existing_item.discount_amount
            self.db.commit()
            self.db.refresh(existing_item)
            item = existing_item
        else:
            # Create new cart item
            subtotal = unit_price * quantity
            item_data = {
                "cart_id": cart_id,
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": unit_price,
                "subtotal": subtotal,
                "total_price": subtotal,
                "added_at": datetime.utcnow(),
            }
            item_data.update(kwargs)

            item = CartItem(**item_data)
            self.db.add(item)
            self.db.commit()
            self.db.refresh(item)

        # Update cart totals
        self.update_cart_totals(cart_id)

        return item

    def update_item_quantity(self, item_id: int, quantity: int) -> Optional[CartItem]:
        """
        Update cart item quantity

        Args:
            item_id: Cart item ID
            quantity: New quantity

        Returns:
            Updated CartItem object or None
        """
        item = self.db.query(CartItem).filter(CartItem.id == item_id).first()
        if not item:
            return None

        if quantity <= 0:
            # Remove item if quantity is 0 or less
            self.remove_item(item_id)
            return None

        item.quantity = quantity
        item.subtotal = item.unit_price * item.quantity
        item.total_price = item.subtotal - item.discount_amount
        self.db.commit()
        self.db.refresh(item)

        # Update cart totals
        self.update_cart_totals(item.cart_id)

        return item

    def remove_item(self, item_id: int) -> bool:
        """
        Remove item from cart

        Args:
            item_id: Cart item ID

        Returns:
            True if removed successfully, False otherwise
        """
        item = self.db.query(CartItem).filter(CartItem.id == item_id).first()
        if not item:
            return False

        cart_id = item.cart_id
        self.db.delete(item)
        self.db.commit()

        # Update cart totals
        self.update_cart_totals(cart_id)

        return True

    def clear_cart(self, cart_id: int) -> bool:
        """
        Remove all items from cart

        Args:
            cart_id: Cart ID

        Returns:
            True if cleared successfully, False otherwise
        """
        cart = self.get_by_id(cart_id)
        if not cart:
            return False

        self.db.query(CartItem).filter(CartItem.cart_id == cart_id).delete()
        self.db.commit()

        # Update cart totals
        self.update_cart_totals(cart_id)

        return True

    def update_cart_totals(self, cart_id: int) -> Optional[Cart]:
        """
        Recalculate and update cart totals

        Args:
            cart_id: Cart ID

        Returns:
            Updated Cart object or None
        """
        cart = self.get_by_id(cart_id)
        if not cart:
            return None

        # Calculate subtotal from all items
        subtotal = sum(item.total_price for item in cart.items)

        # Update cart
        cart.subtotal = subtotal
        cart.estimated_total = subtotal + cart.estimated_tax + cart.estimated_shipping - cart.discount_amount
        cart.last_activity_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(cart)
        return cart

    def apply_coupon(self, cart_id: int, coupon_code: str, discount_amount: float) -> Optional[Cart]:
        """
        Apply coupon to cart

        Args:
            cart_id: Cart ID
            coupon_code: Coupon code
            discount_amount: Discount amount

        Returns:
            Updated Cart object or None
        """
        cart = self.get_by_id(cart_id)
        if not cart:
            return None

        cart.coupon_code = coupon_code
        cart.discount_amount = discount_amount
        cart.estimated_total = cart.subtotal + cart.estimated_tax + cart.estimated_shipping - discount_amount

        self.db.commit()
        self.db.refresh(cart)
        return cart

    def convert_to_order(self, cart_id: int, order_id: int) -> Optional[Cart]:
        """
        Mark cart as converted to order

        Args:
            cart_id: Cart ID
            order_id: Order ID

        Returns:
            Updated Cart object or None
        """
        cart = self.get_by_id(cart_id)
        if not cart:
            return None

        cart.is_active = 0
        cart.converted_to_order_id = order_id

        self.db.commit()
        self.db.refresh(cart)
        return cart

    def merge_carts(self, user_id: int, session_id: str) -> Optional[Cart]:
        """
        Merge guest cart with user cart when user logs in

        Args:
            user_id: User ID
            session_id: Guest session ID

        Returns:
            Merged Cart object or None
        """
        user_cart = self.get_by_user(user_id)
        guest_cart = self.get_by_session(session_id)

        if not guest_cart:
            return user_cart

        if not user_cart:
            # Just transfer the guest cart to the user
            guest_cart.user_id = user_id
            guest_cart.session_id = None
            self.db.commit()
            self.db.refresh(guest_cart)
            return guest_cart

        # Merge items from guest cart to user cart
        for item in guest_cart.items:
            self.add_item(
                cart_id=user_cart.id,
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=item.unit_price,
                product_variant=item.product_variant,
                product_sku=item.product_sku,
            )

        # Delete guest cart
        self.db.delete(guest_cart)
        self.db.commit()

        return user_cart
