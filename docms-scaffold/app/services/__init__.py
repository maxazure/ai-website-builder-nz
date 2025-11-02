# -*- coding: utf-8 -*-
"""Services Module"""

# 原有服务
from app.services.post_service import PostService
from app.services.product_service import ProductService
from app.services.site_service import SiteService

# 基础内容模块服务
from app.services.team_service import TeamService
from app.services.portfolio_service import PortfolioService
from app.services.faq_service import FAQService

# 交互功能模块服务
from app.services.comment_service import CommentService, ReviewService
from app.services.user_service import UserService
from app.services.newsletter_service import NewsletterService

# 电商交易模块服务
from app.services.cart_service import CartService
from app.services.order_service import OrderService

# 预约与服务模块服务
from app.services.booking_service import BookingService
from app.services.restaurant_service import RestaurantService
from app.services.event_service import EventService

# 多媒体与资源模块服务
from app.services.gallery_service import GalleryService
from app.services.video_service import VideoService
from app.services.file_download_service import FileDownloadService

__all__ = [
    # 原有服务
    "PostService",
    "ProductService",
    "SiteService",
    # 基础内容模块
    "TeamService",
    "PortfolioService",
    "FAQService",
    # 交互功能模块
    "CommentService",
    "ReviewService",
    "UserService",
    "NewsletterService",
    # 电商交易模块
    "CartService",
    "OrderService",
    # 预约与服务模块
    "BookingService",
    "RestaurantService",
    "EventService",
    # 多媒体与资源模块
    "GalleryService",
    "VideoService",
    "FileDownloadService",
]
