"""案例展示模块 - Portfolio/Case Study Module"""

from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.base import BaseModel


class PortfolioCategory(BaseModel):
    """
    案例分类模型
    """

    __tablename__ = "portfolio_category"

    name = Column(String(100), nullable=False, comment="分类名称")
    slug = Column(String(100), unique=True, nullable=False, comment="分类Slug")
    description = Column(Text, nullable=True, comment="分类描述")
    sort_order = Column(Integer, default=0, nullable=False, comment="排序序号")
    is_visible = Column(Boolean, default=True, nullable=False, comment="是否可见")


class Portfolio(BaseModel):
    """
    案例展示模型

    展示企业完成的项目案例、成功案例、作品集等
    """

    __tablename__ = "portfolio"

    title = Column(String(200), nullable=False, comment="案例标题")
    slug = Column(String(200), unique=True, nullable=False, comment="案例Slug")
    subtitle = Column(String(300), nullable=True, comment="副标题")

    # 封面图
    cover_media_id = Column(
        Integer, ForeignKey("media_file.id"), nullable=True, comment="封面图ID"
    )

    # 案例详情
    summary = Column(Text, nullable=True, comment="案例摘要")
    background = Column(Text, nullable=True, comment="项目背景")
    challenge = Column(Text, nullable=True, comment="面临挑战")
    solution = Column(Text, nullable=True, comment="解决方案")
    result = Column(Text, nullable=True, comment="项目成果")
    content_html = Column(Text, nullable=True, comment="详细内容HTML")

    # 客户信息
    client_name = Column(String(200), nullable=True, comment="客户名称")
    client_logo_media_id = Column(
        Integer, ForeignKey("media_file.id"), nullable=True, comment="客户Logo ID"
    )
    is_client_anonymous = Column(
        Boolean, default=False, nullable=False, comment="客户是否匿名"
    )

    # 项目信息
    project_date = Column(Date, nullable=True, comment="项目日期")
    project_duration = Column(String(100), nullable=True, comment="项目时长")
    project_url = Column(String(500), nullable=True, comment="项目链接")

    # 标签
    tags = Column(String(500), nullable=True, comment="标签（逗号分隔）")

    # 展示控制
    is_featured = Column(Boolean, default=False, nullable=False, comment="是否推荐")
    sort_order = Column(Integer, default=0, nullable=False, comment="排序序号")
    status = Column(
        Enum("draft", "published", "archived", name="portfolio_status"),
        default="draft",
        nullable=False,
        comment="状态",
    )

    # SEO
    seo_title = Column(String(200), nullable=True, comment="SEO标题")
    seo_description = Column(Text, nullable=True, comment="SEO描述")

    # 关系
    cover_media = relationship("MediaFile", foreign_keys=[cover_media_id])
    client_logo = relationship("MediaFile", foreign_keys=[client_logo_media_id])
    categories = relationship(
        "PortfolioCategory",
        secondary="portfolio_category_link",
        backref="portfolios",
    )


class PortfolioCategoryLink(Base):
    """
    案例与分类的多对多关联表
    """

    __tablename__ = "portfolio_category_link"

    portfolio_id = Column(
        Integer, ForeignKey("portfolio.id"), primary_key=True, comment="案例ID"
    )
    category_id = Column(
        Integer, ForeignKey("portfolio_category.id"), primary_key=True, comment="分类ID"
    )


class PortfolioImage(BaseModel):
    """
    案例图片模型

    一个案例可以有多张图片
    """

    __tablename__ = "portfolio_image"

    portfolio_id = Column(
        Integer, ForeignKey("portfolio.id"), nullable=False, comment="关联案例ID"
    )
    media_id = Column(
        Integer, ForeignKey("media_file.id"), nullable=False, comment="图片ID"
    )
    caption = Column(String(500), nullable=True, comment="图片说明")
    sort_order = Column(Integer, default=0, nullable=False, comment="排序序号")

    # 关系
    portfolio = relationship("Portfolio", backref="images")
    media = relationship("MediaFile")
