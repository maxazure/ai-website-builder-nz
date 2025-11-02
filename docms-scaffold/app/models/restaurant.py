"""餐厅订餐模块 - Restaurant Ordering Module"""

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


class MenuCategory(BaseModel):
    """
    菜单分类模型

    用于组织菜单项,如主食、饮品、甜点等
    """

    __tablename__ = "menu_category"

    # 基本信息
    name = Column(String(100), nullable=False, comment="分类名称")
    slug = Column(String(100), nullable=False, comment="分类Slug")
    description = Column(Text, nullable=True, comment="分类描述")

    # 显示控制
    sort_order = Column(Integer, default=0, nullable=False, comment="排序序号")
    is_active = Column(Boolean, default=True, nullable=False, comment="是否启用")

    # 时段限制
    available_times = Column(
        String(255), nullable=True, comment="可用时段(如:breakfast,lunch,dinner)"
    )

    # 图片
    image_media_id = Column(
        Integer, ForeignKey("media_file.id"), nullable=True, comment="分类图片ID"
    )

    # 关系
    image = relationship("MediaFile", foreign_keys=[image_media_id])

    def __repr__(self):
        return f"<MenuCategory {self.name}>"


class MenuItem(BaseModel):
    """
    菜品模型

    餐厅菜单项,包含菜品信息、价格、选项等
    """

    __tablename__ = "menu_item"

    # 基本信息
    category_id = Column(
        Integer, ForeignKey("menu_category.id"), nullable=False, comment="菜品分类ID"
    )
    name = Column(String(200), nullable=False, comment="菜品名称")
    slug = Column(String(200), nullable=False, comment="菜品Slug")
    description = Column(Text, nullable=True, comment="菜品描述")

    # 价格信息
    price = Column(Float, nullable=False, comment="价格")
    original_price = Column(Float, nullable=True, comment="原价(用于显示折扣)")

    # 图片
    image_media_id = Column(
        Integer, ForeignKey("media_file.id"), nullable=True, comment="菜品图片ID"
    )

    # 规格选项
    sizes = Column(
        String(255), nullable=True, comment="规格选项(JSON格式,如:[{'name':'小份','price':10},{'name':'大份','price':15}])"
    )
    spice_levels = Column(
        String(255), nullable=True, comment="辣度选项(如:不辣,微辣,中辣,特辣)"
    )
    customizations = Column(
        Text, nullable=True, comment="可定制选项(JSON格式,如配料、做法等)"
    )

    # 营养与过敏信息
    calories = Column(Integer, nullable=True, comment="卡路里")
    allergens = Column(
        String(255), nullable=True, comment="过敏原(如:坚果,乳制品,麸质)"
    )
    dietary_tags = Column(
        String(255), nullable=True, comment="饮食标签(如:素食,无麸质,清真)"
    )

    # 库存管理
    is_available = Column(
        Boolean, default=True, nullable=False, comment="是否可售"
    )
    stock_quantity = Column(Integer, nullable=True, comment="库存数量(null表示不限)")
    daily_limit = Column(Integer, nullable=True, comment="每日限量")
    today_sold = Column(Integer, default=0, nullable=False, comment="今日已售")

    # 推荐与标签
    is_recommended = Column(
        Boolean, default=False, nullable=False, comment="是否推荐"
    )
    is_popular = Column(Boolean, default=False, nullable=False, comment="是否热门")
    is_new = Column(Boolean, default=False, nullable=False, comment="是否新品")
    is_seasonal = Column(Boolean, default=False, nullable=False, comment="是否时令")

    # 显示控制
    sort_order = Column(Integer, default=0, nullable=False, comment="排序序号")

    # 关系
    category = relationship("MenuCategory", backref="items")
    image = relationship("MediaFile", foreign_keys=[image_media_id])

    def __repr__(self):
        return f"<MenuItem {self.name}>"


class RestaurantOrder(BaseModel):
    """
    餐厅订单模型

    管理堂食、外卖、自取订单
    """

    __tablename__ = "restaurant_order"

    # 订单基本信息
    order_number = Column(
        String(50), unique=True, nullable=False, comment="订单号(唯一标识)"
    )
    user_id = Column(
        Integer, ForeignKey("user.id"), nullable=True, comment="关联用户ID(可选)"
    )

    # 订单类型
    order_type = Column(
        Enum("dine_in", "takeaway", "delivery", name="restaurant_order_type"),
        nullable=False,
        comment="订单类型",
    )

    # 订单状态
    status = Column(
        Enum(
            "pending",
            "confirmed",
            "preparing",
            "ready",
            "delivering",
            "completed",
            "cancelled",
            name="restaurant_order_status",
        ),
        default="pending",
        nullable=False,
        comment="订单状态",
    )
    payment_status = Column(
        Enum("unpaid", "paid", "refunded", name="restaurant_payment_status"),
        default="unpaid",
        nullable=False,
        comment="支付状态",
    )

    # 客户信息
    customer_name = Column(String(100), nullable=False, comment="客户姓名")
    customer_phone = Column(String(50), nullable=False, comment="客户电话")
    customer_email = Column(String(100), nullable=True, comment="客户邮箱")

    # 堂食信息
    table_number = Column(String(20), nullable=True, comment="桌号(堂食)")
    number_of_guests = Column(Integer, nullable=True, comment="就餐人数(堂食)")

    # 外卖配送信息
    delivery_address = Column(String(500), nullable=True, comment="配送地址(外卖)")
    delivery_city = Column(String(100), nullable=True, comment="配送城市")
    delivery_postal_code = Column(String(20), nullable=True, comment="配送邮编")
    delivery_instructions = Column(Text, nullable=True, comment="配送说明")

    # 取餐信息
    pickup_time = Column(DateTime, nullable=True, comment="取餐时间(自取)")
    scheduled_time = Column(DateTime, nullable=True, comment="预定时间(堂食预订)")

    # 金额信息
    subtotal = Column(Float, default=0.0, nullable=False, comment="菜品小计")
    delivery_fee = Column(Float, default=0.0, nullable=False, comment="配送费")
    service_fee = Column(Float, default=0.0, nullable=False, comment="服务费")
    tax_amount = Column(Float, default=0.0, nullable=False, comment="税费")
    discount_amount = Column(Float, default=0.0, nullable=False, comment="折扣金额")
    tip_amount = Column(Float, default=0.0, nullable=False, comment="小费")
    total_amount = Column(Float, default=0.0, nullable=False, comment="订单总额")

    # 优惠信息
    coupon_code = Column(String(50), nullable=True, comment="优惠码")

    # 支付信息
    payment_method = Column(
        Enum("cash", "card", "online", name="restaurant_payment_method"),
        nullable=True,
        comment="支付方式",
    )
    paid_at = Column(DateTime, nullable=True, comment="支付时间")

    # 时间节点
    confirmed_at = Column(DateTime, nullable=True, comment="确认时间")
    preparing_at = Column(DateTime, nullable=True, comment="开始准备时间")
    ready_at = Column(DateTime, nullable=True, comment="准备完成时间")
    delivered_at = Column(DateTime, nullable=True, comment="送达时间")
    completed_at = Column(DateTime, nullable=True, comment="完成时间")
    cancelled_at = Column(DateTime, nullable=True, comment="取消时间")

    # 其他
    customer_notes = Column(Text, nullable=True, comment="客户备注")
    kitchen_notes = Column(Text, nullable=True, comment="厨房备注")
    cancel_reason = Column(Text, nullable=True, comment="取消原因")

    # 关系
    user = relationship("User", backref="restaurant_orders")
    items = relationship(
        "RestaurantOrderItem", back_populates="order", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<RestaurantOrder {self.order_number} ({self.order_type})>"


class RestaurantOrderItem(BaseModel):
    """
    餐厅订单项模型

    订单中的单个菜品项
    """

    __tablename__ = "restaurant_order_item"

    # 关联信息
    order_id = Column(
        Integer, ForeignKey("restaurant_order.id"), nullable=False, comment="订单ID"
    )
    menu_item_id = Column(
        Integer, ForeignKey("menu_item.id"), nullable=True, comment="菜品ID(可能已删除)"
    )

    # 菜品信息快照
    item_name = Column(String(200), nullable=False, comment="菜品名称")
    item_description = Column(Text, nullable=True, comment="菜品描述")

    # 数量与价格
    quantity = Column(Integer, default=1, nullable=False, comment="数量")
    unit_price = Column(Float, nullable=False, comment="单价")
    subtotal = Column(Float, nullable=False, comment="小计")

    # 定制选项
    size_option = Column(String(50), nullable=True, comment="规格选择(如:大份)")
    spice_level = Column(String(50), nullable=True, comment="辣度选择")
    customizations = Column(Text, nullable=True, comment="定制要求(JSON格式)")

    # 其他
    special_instructions = Column(Text, nullable=True, comment="特殊要求")

    # 关系
    order = relationship("RestaurantOrder", back_populates="items")
    menu_item = relationship("MenuItem")

    def __repr__(self):
        return f"<RestaurantOrderItem {self.item_name} x{self.quantity}>"
