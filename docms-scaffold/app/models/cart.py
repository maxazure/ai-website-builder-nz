"""购物车模块 - Shopping Cart Module"""

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.base import BaseModel


class Cart(BaseModel):
    """
    购物车模型

    用于管理用户购物车，支持已登录用户和访客购物车
    """

    __tablename__ = "cart"

    # 用户关联
    user_id = Column(
        Integer, ForeignKey("user.id"), nullable=True, comment="关联用户ID(已登录用户)"
    )
    session_id = Column(
        String(100), nullable=True, comment="会话ID(访客用户标识)"
    )

    # 购物车状态
    is_active = Column(
        Integer, default=1, nullable=False, comment="是否活跃(0=已转换为订单,1=活跃)"
    )
    converted_to_order_id = Column(
        Integer, ForeignKey("order.id"), nullable=True, comment="转换为的订单ID"
    )

    # 金额统计
    subtotal = Column(Float, default=0.0, nullable=False, comment="商品小计")
    estimated_tax = Column(Float, default=0.0, nullable=False, comment="预估税费")
    estimated_shipping = Column(Float, default=0.0, nullable=False, comment="预估运费")
    estimated_total = Column(Float, default=0.0, nullable=False, comment="预估总额")

    # 优惠信息
    coupon_code = Column(String(50), nullable=True, comment="应用的优惠码")
    discount_amount = Column(Float, default=0.0, nullable=False, comment="折扣金额")

    # 时间信息
    last_activity_at = Column(DateTime, nullable=True, comment="最后活动时间")
    expires_at = Column(DateTime, nullable=True, comment="过期时间(访客购物车)")

    # 其他
    notes = Column(Text, nullable=True, comment="备注")

    # 关系
    user = relationship("User", backref="carts")
    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")
    converted_order = relationship("Order")

    def __repr__(self):
        return f"<Cart user_id={self.user_id} session_id={self.session_id}>"


class CartItem(BaseModel):
    """
    购物车项模型

    购物车中的单个产品项
    """

    __tablename__ = "cart_item"

    # 关联信息
    cart_id = Column(Integer, ForeignKey("cart.id"), nullable=False, comment="购物车ID")
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False, comment="产品ID")

    # 产品选项
    product_variant = Column(
        String(255), nullable=True, comment="产品规格(如:颜色=红色,尺寸=L)"
    )
    product_sku = Column(String(100), nullable=True, comment="产品SKU")

    # 数量与价格
    quantity = Column(Integer, default=1, nullable=False, comment="数量")
    unit_price = Column(Float, nullable=False, comment="单价(添加时的价格)")
    subtotal = Column(Float, nullable=False, comment="小计(单价×数量)")

    # 折扣信息
    discount_amount = Column(Float, default=0.0, nullable=False, comment="折扣金额")
    total_price = Column(Float, nullable=False, comment="总价(小计-折扣)")

    # 其他
    notes = Column(Text, nullable=True, comment="特殊要求备注")
    added_at = Column(DateTime, nullable=True, comment="添加到购物车时间")

    # 关系
    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")

    def __repr__(self):
        return f"<CartItem product_id={self.product_id} x{self.quantity}>"
