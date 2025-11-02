"""图片画廊模块 - Image Gallery Module"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.base import BaseModel


class Gallery(BaseModel):
    """
    画廊/相册模型

    用于组织和管理图片集合,如企业环境、产品图片、活动照片等
    """

    __tablename__ = "gallery"

    # 基本信息
    title = Column(String(200), nullable=False, comment="画廊标题")
    slug = Column(String(200), nullable=False, comment="画廊Slug")
    description = Column(Text, nullable=True, comment="画廊描述")

    # 分类
    category = Column(String(100), nullable=True, comment="画廊分类")
    tags = Column(String(255), nullable=True, comment="标签(逗号分隔)")

    # 封面图片
    cover_media_id = Column(
        Integer, ForeignKey("media_file.id"), nullable=True, comment="封面图片ID"
    )

    # 展示模式
    display_mode = Column(
        String(50),
        nullable=True,
        default="grid",
        comment="展示模式(grid=网格,masonry=瀑布流,slider=轮播)",
    )

    # 显示控制
    is_featured = Column(Boolean, default=False, nullable=False, comment="是否推荐")
    is_public = Column(Boolean, default=True, nullable=False, comment="是否公开")
    sort_order = Column(Integer, default=0, nullable=False, comment="排序序号")

    # 访问控制
    allow_download = Column(
        Boolean, default=False, nullable=False, comment="是否允许下载图片"
    )
    watermark_enabled = Column(
        Boolean, default=False, nullable=False, comment="是否启用水印"
    )

    # SEO
    seo_title = Column(String(200), nullable=True, comment="SEO标题")
    seo_description = Column(Text, nullable=True, comment="SEO描述")

    # 统计
    view_count = Column(Integer, default=0, nullable=False, comment="浏览次数")
    image_count = Column(Integer, default=0, nullable=False, comment="图片数量")

    # 其他
    notes = Column(Text, nullable=True, comment="备注")

    # 关系
    cover_media = relationship("MediaFile", foreign_keys=[cover_media_id])
    images = relationship(
        "GalleryImage", back_populates="gallery", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Gallery {self.title}>"


class GalleryImage(BaseModel):
    """
    画廊图片模型

    画廊中的单张图片
    """

    __tablename__ = "gallery_image"

    # 关联信息
    gallery_id = Column(
        Integer, ForeignKey("gallery.id"), nullable=False, comment="画廊ID"
    )
    media_id = Column(
        Integer, ForeignKey("media_file.id"), nullable=False, comment="图片文件ID"
    )

    # 图片信息
    title = Column(String(200), nullable=True, comment="图片标题")
    caption = Column(Text, nullable=True, comment="图片说明")
    alt_text = Column(String(255), nullable=True, comment="图片Alt文本(SEO)")

    # 分类与标签
    tags = Column(String(255), nullable=True, comment="标签(逗号分隔)")

    # 排序
    sort_order = Column(Integer, default=0, nullable=False, comment="排序序号")

    # 显示控制
    is_visible = Column(Boolean, default=True, nullable=False, comment="是否可见")
    is_featured = Column(Boolean, default=False, nullable=False, comment="是否精选")

    # 链接
    link_url = Column(String(500), nullable=True, comment="点击图片跳转链接")
    link_target = Column(
        String(20), nullable=True, default="_self", comment="链接打开方式(_self/_blank)"
    )

    # 统计
    view_count = Column(Integer, default=0, nullable=False, comment="浏览次数")
    download_count = Column(Integer, default=0, nullable=False, comment="下载次数")

    # 其他
    notes = Column(Text, nullable=True, comment="备注")

    # 关系
    gallery = relationship("Gallery", back_populates="images")
    media = relationship("MediaFile")

    def __repr__(self):
        return f"<GalleryImage {self.title or 'Untitled'}>"
