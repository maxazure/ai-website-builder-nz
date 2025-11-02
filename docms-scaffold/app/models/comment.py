"""评论/评价系统模块 - Comment & Review Module"""

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Comment(BaseModel):
    """
    评论模型

    支持对文章、产品、案例等内容的评论和评价
    """

    __tablename__ = "comment"

    # 评论对象（多态关联）
    commentable_type = Column(
        String(50), nullable=False, comment="评论对象类型（post/product/portfolio等）"
    )
    commentable_id = Column(Integer, nullable=False, comment="评论对象ID")

    # 评论者信息
    author_name = Column(String(100), nullable=False, comment="评论者姓名")
    author_email = Column(String(100), nullable=False, comment="评论者邮箱")
    author_website = Column(String(255), nullable=True, comment="评论者网站")
    user_id = Column(
        Integer, ForeignKey("user.id"), nullable=True, comment="关联用户ID（如已登录）"
    )

    # 评论内容
    content = Column(Text, nullable=False, comment="评论内容")
    rating = Column(Integer, nullable=True, comment="评分（1-5星）")

    # 回复关系
    parent_id = Column(
        Integer, ForeignKey("comment.id"), nullable=True, comment="父评论ID（用于回复）"
    )

    # 审核和管理
    status = Column(
        Enum("pending", "approved", "spam", "trash", name="comment_status"),
        default="pending",
        nullable=False,
        comment="状态",
    )
    is_featured = Column(Boolean, default=False, nullable=False, comment="是否精选")

    # 管理员回复
    admin_reply = Column(Text, nullable=True, comment="管理员回复内容")
    replied_at = Column(DateTime, nullable=True, comment="回复时间")

    # 统计
    helpful_count = Column(Integer, default=0, nullable=False, comment="有用次数")
    report_count = Column(Integer, default=0, nullable=False, comment="举报次数")

    # IP和用户代理
    ip_address = Column(String(45), nullable=True, comment="IP地址")
    user_agent = Column(String(500), nullable=True, comment="用户代理")

    # 关系
    parent = relationship("Comment", remote_side="Comment.id", backref="replies")
    user = relationship("User", backref="comments", foreign_keys=[user_id])


class Review(BaseModel):
    """
    评价模型

    专门用于产品/服务评价，比评论更结构化
    """

    __tablename__ = "review"

    # 评价对象
    reviewable_type = Column(
        String(50), nullable=False, comment="评价对象类型（product/service等）"
    )
    reviewable_id = Column(Integer, nullable=False, comment="评价对象ID")

    # 评价者信息
    reviewer_name = Column(String(100), nullable=False, comment="评价者姓名")
    reviewer_email = Column(String(100), nullable=False, comment="评价者邮箱")
    reviewer_photo = Column(String(500), nullable=True, comment="评价者头像")
    user_id = Column(
        Integer, ForeignKey("user.id"), nullable=True, comment="关联用户ID"
    )

    # 评价内容
    title = Column(String(200), nullable=True, comment="评价标题")
    content = Column(Text, nullable=False, comment="评价内容")

    # 评分维度
    overall_rating = Column(Integer, nullable=False, comment="总体评分（1-5星）")
    quality_rating = Column(Integer, nullable=True, comment="质量评分")
    service_rating = Column(Integer, nullable=True, comment="服务评分")
    value_rating = Column(Integer, nullable=True, comment="性价比评分")

    # 验证购买
    is_verified_purchase = Column(
        Boolean, default=False, nullable=False, comment="是否验证购买"
    )
    order_id = Column(Integer, ForeignKey("order.id"), nullable=True, comment="关联订单ID")

    # 审核
    status = Column(
        Enum("pending", "approved", "rejected", name="review_status"),
        default="pending",
        nullable=False,
        comment="状态",
    )
    is_featured = Column(Boolean, default=False, nullable=False, comment="是否精选")

    # 统计
    helpful_count = Column(Integer, default=0, nullable=False, comment="有用次数")
    unhelpful_count = Column(Integer, default=0, nullable=False, comment="无用次数")

    # 关系
    user = relationship("User", backref="reviews", foreign_keys=[user_id])
