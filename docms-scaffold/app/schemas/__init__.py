"""
Pydantic schemas for request/response validation
"""
# 原有schemas
from app.schemas.requests import ContactFormRequest

# 新增schemas（从 schemas.py 导入）
from app.schemas.schemas import (
    # 团队模块
    TeamMemberCreate,
    TeamMemberUpdate,
    TeamMemberResponse,
    # 案例模块
    PortfolioCreate,
    PortfolioUpdate,
    PortfolioResponse,
    # FAQ模块
    FAQCreate,
    FAQUpdate,
    FAQResponse,
    # 评论模块
    CommentCreate,
    CommentUpdate,
    CommentResponse,
    ReviewCreate,
    ReviewUpdate,
    ReviewResponse,
    # 用户模块
    UserRegister,
    UserLogin,
    UserUpdate,
    UserResponse,
    # 订阅模块
    NewsletterSubscribeRequest,
    NewsletterSubscriberResponse,
    # 购物车模块
    CartItemAdd,
    CartItemResponse,
    CartResponse,
    # 订单模块
    OrderItemCreate,
    OrderCreate,
    OrderUpdate,
    OrderResponse,
    # 预约模块
    BookingCreate,
    BookingUpdate,
    BookingResponse,
    # 餐厅模块
    MenuItemCreate,
    RestaurantOrderItemCreate,
    RestaurantOrderCreate,
    RestaurantOrderResponse,
    # 活动模块
    EventCreate,
    EventRegistrationCreate,
    EventResponse,
    # 画廊模块
    GalleryCreate,
    GalleryImageCreate,
    GalleryResponse,
    # 视频模块
    VideoCreate,
    VideoUpdate,
    VideoResponse,
    # 文件模块
    FileDownloadCreate,
    FileDownloadUpdate,
    FileDownloadResponse,
)

__all__ = [
    # 原有
    "ContactFormRequest",
    # 团队
    "TeamMemberCreate",
    "TeamMemberUpdate",
    "TeamMemberResponse",
    # 案例
    "PortfolioCreate",
    "PortfolioUpdate",
    "PortfolioResponse",
    # FAQ
    "FAQCreate",
    "FAQUpdate",
    "FAQResponse",
    # 评论
    "CommentCreate",
    "CommentUpdate",
    "CommentResponse",
    "ReviewCreate",
    "ReviewUpdate",
    "ReviewResponse",
    # 用户
    "UserRegister",
    "UserLogin",
    "UserUpdate",
    "UserResponse",
    # 订阅
    "NewsletterSubscribeRequest",
    "NewsletterSubscriberResponse",
    # 购物车
    "CartItemAdd",
    "CartItemResponse",
    "CartResponse",
    # 订单
    "OrderItemCreate",
    "OrderCreate",
    "OrderUpdate",
    "OrderResponse",
    # 预约
    "BookingCreate",
    "BookingUpdate",
    "BookingResponse",
    # 餐厅
    "MenuItemCreate",
    "RestaurantOrderItemCreate",
    "RestaurantOrderCreate",
    "RestaurantOrderResponse",
    # 活动
    "EventCreate",
    "EventRegistrationCreate",
    "EventResponse",
    # 画廊
    "GalleryCreate",
    "GalleryImageCreate",
    "GalleryResponse",
    # 视频
    "VideoCreate",
    "VideoUpdate",
    "VideoResponse",
    # 文件
    "FileDownloadCreate",
    "FileDownloadUpdate",
    "FileDownloadResponse",
]
