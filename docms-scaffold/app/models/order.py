"""订单管理模块 - Order Management Module"""

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.base import BaseModel


class Order(BaseModel):
    """
    订单模型

    用于管理电商订单、从接收订单到配送完成的全流程追踪
    """

    __tablename__ = "order"

    # 订单基本信息
    order_number = Column(
        String(50), unique=True, nullable=False, comment="订单号(唯一标识)"
    )
    user_id = Column(
        Integer, ForeignKey("user.id"), nullable=True, comment="关联用户ID(可选,支持游客)"
    )

    # 订单状态
    status = Column(
        Enum(
            "pending",
            "confirmed",
            "processing",
            "shipped",
            "delivered",
            "cancelled",
            "refunded",
            name="order_status",
        ),
        default="pending",
        nullable=False,
        comment="订单状态",
    )
    payment_status = Column(
        Enum("unpaid", "paid", "partial", "refunded", name="payment_status"),
        default="unpaid",
        nullable=False,
        comment="支付状态",
    )

    # 客户信息
    customer_email = Column(String(100), nullable=False, comment="客户邮箱")
    customer_phone = Column(String(50), nullable=True, comment="客户电话")
    customer_name = Column(String(100), nullable=False, comment="客户姓名")

    # 配送信息
    shipping_address_line1 = Column(String(255), nullable=False, comment="配送地址行1")
    shipping_address_line2 = Column(String(255), nullable=True, comment="配送地址行2")
    shipping_city = Column(String(100), nullable=False, comment="配送城市")
    shipping_state = Column(String(100), nullable=True, comment="配送州/省")
    shipping_postal_code = Column(String(20), nullable=False, comment="配送邮编")
    shipping_country = Column(
        String(100), nullable=False, default="New Zealand", comment="配送国家"
    )

    # 账单信息
    billing_address_line1 = Column(String(255), nullable=True, comment="账单地址行1")
    billing_address_line2 = Column(String(255), nullable=True, comment="账单地址行2")
    billing_city = Column(String(100), nullable=True, comment="账单城市")
    billing_state = Column(String(100), nullable=True, comment="账单州/省")
    billing_postal_code = Column(String(20), nullable=True, comment="账单邮编")
    billing_country = Column(String(100), nullable=True, comment="账单国家")
    billing_same_as_shipping = Column(
        Boolean, default=True, nullable=False, comment="账单地址是否与配送地址相同"
    )

    # 金额信息
    subtotal = Column(Float, default=0.0, nullable=False, comment="商品小计")
    shipping_fee = Column(Float, default=0.0, nullable=False, comment="运费")
    tax_amount = Column(Float, default=0.0, nullable=False, comment="税费")
    discount_amount = Column(Float, default=0.0, nullable=False, comment="折扣金额")
    total_amount = Column(Float, default=0.0, nullable=False, comment="订单总额")
    paid_amount = Column(Float, default=0.0, nullable=False, comment="已支付金额")

    # 优惠信息
    coupon_code = Column(String(50), nullable=True, comment="优惠码")
    coupon_discount = Column(Float, default=0.0, nullable=False, comment="优惠码折扣金额")

    # 配送方式
    shipping_method = Column(
        Enum("standard", "express", "pickup", name="shipping_method"),
        default="standard",
        nullable=False,
        comment="配送方式",
    )
    shipping_carrier = Column(String(100), nullable=True, comment="物流公司")
    tracking_number = Column(String(100), nullable=True, comment="物流追踪号")
    tracking_url = Column(String(255), nullable=True, comment="物流追踪链接")

    # 支付信息
    payment_method = Column(
        Enum("credit_card", "paypal", "bank_transfer", "cash", name="payment_method"),
        nullable=True,
        comment="支付方式",
    )
    payment_transaction_id = Column(String(100), nullable=True, comment="支付交易ID")
    paid_at = Column(DateTime, nullable=True, comment="支付时间")

    # 时间节点
    confirmed_at = Column(DateTime, nullable=True, comment="确认时间")
    shipped_at = Column(DateTime, nullable=True, comment="发货时间")
    delivered_at = Column(DateTime, nullable=True, comment="送达时间")
    cancelled_at = Column(DateTime, nullable=True, comment="取消时间")

    # 其他
    customer_notes = Column(Text, nullable=True, comment="客户备注")
    admin_notes = Column(Text, nullable=True, comment="管理员备注")
    cancel_reason = Column(Text, nullable=True, comment="取消原因")
    refund_reason = Column(Text, nullable=True, comment="退款原因")
    ip_address = Column(String(50), nullable=True, comment="下单IP地址")

    # 关系
    user = relationship("User", backref="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order {self.order_number} ({self.status})>"


class OrderItem(BaseModel):
    """
    订单项模型

    订单中的单个产品项
    """

    __tablename__ = "order_item"

    # 关联信息
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False, comment="订单ID")
    product_id = Column(
        Integer, ForeignKey("product.id"), nullable=True, comment="产品ID(可能已删除)"
    )

    # 产品信息快照(保存下单时的产品信息)
    product_name = Column(String(200), nullable=False, comment="产品名称")
    product_sku = Column(String(100), nullable=True, comment="产品SKU")
    product_variant = Column(String(255), nullable=True, comment="产品规格(如:颜色,尺寸)")

    # 数量与价格
    quantity = Column(Integer, default=1, nullable=False, comment="购买数量")
    unit_price = Column(Float, nullable=False, comment="单价")
    subtotal = Column(Float, nullable=False, comment="小计(单价×数量)")
    discount_amount = Column(Float, default=0.0, nullable=False, comment="折扣金额")
    total_price = Column(Float, nullable=False, comment="总价(小计-折扣)")

    # 其他
    notes = Column(Text, nullable=True, comment="备注")

    # 关系
    order = relationship("Order", back_populates="items")
    product = relationship("Product")

    def __repr__(self):
        return f"<OrderItem {self.product_name} x{self.quantity}>"
