"""通讯订阅模块 - Newsletter Module"""

from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String, Text
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class NewsletterSubscriber(BaseModel):
    """
    通讯订阅者模型

    用于收集用户邮箱并管理邮件订阅、发送定期通讯、促销信息等
    """

    __tablename__ = "newsletter_subscriber"

    # 基本信息
    email = Column(String(100), unique=True, nullable=False, comment="订阅邮箱")
    first_name = Column(String(50), nullable=True, comment="名字")
    last_name = Column(String(50), nullable=True, comment="姓氏")

    # 订阅状态
    status = Column(
        Enum("pending", "active", "unsubscribed", "bounced", name="subscriber_status"),
        default="pending",
        nullable=False,
        comment="订阅状态",
    )
    is_verified = Column(Boolean, default=False, nullable=False, comment="是否已验证")

    # 订阅管理
    subscription_source = Column(
        String(100), nullable=True, comment="订阅来源(页面/弹窗/活动等)"
    )
    subscription_ip = Column(String(50), nullable=True, comment="订阅时IP地址")
    subscribed_at = Column(DateTime, nullable=True, comment="订阅时间")
    unsubscribed_at = Column(DateTime, nullable=True, comment="取消订阅时间")
    unsubscribe_reason = Column(Text, nullable=True, comment="取消订阅原因")

    # 分组管理
    group_tags = Column(
        String(255), nullable=True, comment="订阅分组标签(逗号分隔,如:vip,promotion)"
    )

    # 邮件统计
    total_emails_sent = Column(
        Integer, default=0, nullable=False, comment="已发送邮件总数"
    )
    total_emails_opened = Column(
        Integer, default=0, nullable=False, comment="已打开邮件总数"
    )
    total_links_clicked = Column(
        Integer, default=0, nullable=False, comment="已点击链接总数"
    )
    last_email_sent_at = Column(DateTime, nullable=True, comment="最后发送邮件时间")
    last_email_opened_at = Column(DateTime, nullable=True, comment="最后打开邮件时间")

    # 偏好设置
    preferred_language = Column(
        String(10), nullable=True, default="en", comment="首选语言"
    )
    email_frequency = Column(
        Enum("daily", "weekly", "monthly", name="email_frequency"),
        default="weekly",
        nullable=False,
        comment="邮件频率",
    )

    # 其他
    notes = Column(Text, nullable=True, comment="管理员备注")
    bounce_count = Column(Integer, default=0, nullable=False, comment="退信次数")
    complaint_count = Column(Integer, default=0, nullable=False, comment="投诉次数")

    def __repr__(self):
        return f"<NewsletterSubscriber {self.email} ({self.status})>"


class NewsletterCampaign(BaseModel):
    """
    邮件营销活动模型

    用于管理邮件发送活动、模板、统计等
    """

    __tablename__ = "newsletter_campaign"

    # 基本信息
    name = Column(String(200), nullable=False, comment="活动名称")
    subject = Column(String(200), nullable=False, comment="邮件主题")
    preview_text = Column(String(255), nullable=True, comment="预览文本")

    # 内容
    content_html = Column(Text, nullable=False, comment="邮件内容HTML")
    content_text = Column(Text, nullable=True, comment="纯文本内容")

    # 发送设置
    status = Column(
        Enum("draft", "scheduled", "sending", "sent", "cancelled", name="campaign_status"),
        default="draft",
        nullable=False,
        comment="活动状态",
    )
    scheduled_at = Column(DateTime, nullable=True, comment="计划发送时间")
    sent_at = Column(DateTime, nullable=True, comment="实际发送时间")

    # 目标受众
    target_groups = Column(
        String(255), nullable=True, comment="目标分组(逗号分隔)"
    )
    target_all = Column(
        Boolean, default=False, nullable=False, comment="是否发送给所有订阅者"
    )

    # 发送统计
    total_recipients = Column(Integer, default=0, nullable=False, comment="收件人总数")
    total_sent = Column(Integer, default=0, nullable=False, comment="成功发送数")
    total_failed = Column(Integer, default=0, nullable=False, comment="发送失败数")
    total_opened = Column(Integer, default=0, nullable=False, comment="打开数")
    total_clicked = Column(Integer, default=0, nullable=False, comment="点击数")
    total_unsubscribed = Column(Integer, default=0, nullable=False, comment="取消订阅数")
    total_bounced = Column(Integer, default=0, nullable=False, comment="退信数")

    # 发件人信息
    from_name = Column(String(100), nullable=True, comment="发件人名称")
    from_email = Column(String(100), nullable=True, comment="发件人邮箱")
    reply_to_email = Column(String(100), nullable=True, comment="回复邮箱")

    # 其他
    notes = Column(Text, nullable=True, comment="活动备注")

    def __repr__(self):
        return f"<NewsletterCampaign {self.name} ({self.status})>"
