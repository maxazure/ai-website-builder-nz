"""Database models module"""

# 基础模型
from app.models.base import BaseModel

# 站点核心模块
from app.models.contact import ContactMessage
from app.models.custom_field import (
    CustomFieldDef,
    CustomFieldOption,
    ProductCustomFieldValue,
)
from app.models.media import MediaFile
from app.models.post import Post, PostCategory, PostCategoryLink
from app.models.product import Product, ProductCategory, ProductCategoryLink
from app.models.site import ColumnType, SinglePage, SiteColumn, SiteSetting

# 基础内容模块
from app.models.team import TeamMember
from app.models.portfolio import (
    Portfolio,
    PortfolioCategory,
    PortfolioCategoryLink,
    PortfolioImage,
)
from app.models.faq import FAQ, FAQCategory

# 交互功能模块
from app.models.comment import Comment, Review
from app.models.user import User
from app.models.newsletter import NewsletterCampaign, NewsletterSubscriber

# 电商交易模块
from app.models.cart import Cart, CartItem
from app.models.order import Order, OrderItem

# 预约与服务模块
from app.models.booking import Booking, BookingService, BookingTimeSlot
from app.models.restaurant import (
    MenuCategory,
    MenuItem,
    RestaurantOrder,
    RestaurantOrderItem,
)
from app.models.event import Event, EventRegistration, EventTicketType

# 多媒体与资源模块
from app.models.gallery import Gallery, GalleryImage
from app.models.video import Video, VideoCategory, VideoPlaylist, VideoPlaylistLink
from app.models.file_download import FileCategory, FileDownload, FileDownloadLog

__all__ = [
    # 基础
    "BaseModel",
    # 站点核心
    "SiteColumn",
    "ColumnType",
    "SinglePage",
    "SiteSetting",
    "Post",
    "PostCategory",
    "PostCategoryLink",
    "Product",
    "ProductCategory",
    "ProductCategoryLink",
    "CustomFieldDef",
    "CustomFieldOption",
    "ProductCustomFieldValue",
    "MediaFile",
    "ContactMessage",
    # 基础内容模块
    "TeamMember",
    "Portfolio",
    "PortfolioCategory",
    "PortfolioCategoryLink",
    "PortfolioImage",
    "FAQ",
    "FAQCategory",
    # 交互功能模块
    "Comment",
    "Review",
    "User",
    "NewsletterSubscriber",
    "NewsletterCampaign",
    # 电商交易模块
    "Cart",
    "CartItem",
    "Order",
    "OrderItem",
    # 预约与服务模块
    "Booking",
    "BookingService",
    "BookingTimeSlot",
    "MenuCategory",
    "MenuItem",
    "RestaurantOrder",
    "RestaurantOrderItem",
    "Event",
    "EventRegistration",
    "EventTicketType",
    # 多媒体与资源模块
    "Gallery",
    "GalleryImage",
    "Video",
    "VideoCategory",
    "VideoPlaylist",
    "VideoPlaylistLink",
    "FileCategory",
    "FileDownload",
    "FileDownloadLog",
]
