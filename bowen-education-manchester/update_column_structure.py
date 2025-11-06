#!/usr/bin/env python3
"""
更新栏目结构，添加多级栏目
按照 REQUIREMENTS.md 的设计添加子栏目
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.site import SiteColumn, ColumnType

# 数据库连接
DATABASE_URL = "sqlite:///instance/database.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_subcolumns():
    """添加子栏目"""

    # 获取父栏目
    school = session.query(SiteColumn).filter_by(slug='school').first()
    chess = session.query(SiteColumn).filter_by(slug='chess').first()
    badminton = session.query(SiteColumn).filter_by(slug='badminton').first()
    programmes = session.query(SiteColumn).filter_by(slug='programmes').first()
    events = session.query(SiteColumn).filter_by(slug='events').first()

    # 子栏目配置
    subcolumns = [
        # 中文学校子栏目
        {
            'name': '课程设置',
            'slug': 'school-curriculum',
            'column_type': ColumnType.PRODUCT,
            'parent_id': school.id if school else None,
            'sort_order': 1,
            'show_in_nav': False,  # 不在顶级导航显示
        },
        {
            'name': '学期日期',
            'slug': 'school-term-dates',
            'column_type': ColumnType.SINGLE_PAGE,
            'parent_id': school.id if school else None,
            'sort_order': 2,
            'show_in_nav': False,
        },
        {
            'name': 'PTA家长教师协会',
            'slug': 'school-pta',
            'column_type': ColumnType.SINGLE_PAGE,
            'parent_id': school.id if school else None,
            'sort_order': 3,
            'show_in_nav': False,
        },

        # 国际象棋俱乐部子栏目
        {
            'name': '我们的比赛',
            'slug': 'chess-competitions',
            'column_type': ColumnType.POST,
            'parent_id': chess.id if chess else None,
            'sort_order': 1,
            'show_in_nav': False,
        },
        {
            'name': '棋手信息',
            'slug': 'chess-players',
            'column_type': ColumnType.SINGLE_PAGE,
            'parent_id': chess.id if chess else None,
            'sort_order': 2,
            'show_in_nav': False,
        },
        {
            'name': '相册',
            'slug': 'chess-gallery',
            'column_type': ColumnType.CUSTOM,
            'parent_id': chess.id if chess else None,
            'sort_order': 3,
            'show_in_nav': False,
        },

        # 羽毛球俱乐部子栏目
        {
            'name': '赛事活动',
            'slug': 'badminton-events',
            'column_type': ColumnType.POST,
            'parent_id': badminton.id if badminton else None,
            'sort_order': 1,
            'show_in_nav': False,
        },
        {
            'name': '训练时间表',
            'slug': 'badminton-schedule',
            'column_type': ColumnType.SINGLE_PAGE,
            'parent_id': badminton.id if badminton else None,
            'sort_order': 2,
            'show_in_nav': False,
        },
        {
            'name': '精彩瞬间',
            'slug': 'badminton-gallery',
            'column_type': ColumnType.CUSTOM,
            'parent_id': badminton.id if badminton else None,
            'sort_order': 3,
            'show_in_nav': False,
        },

        # 政府项目子栏目
        {
            'name': 'HAF项目',
            'slug': 'programmes-haf',
            'column_type': ColumnType.SINGLE_PAGE,
            'parent_id': programmes.id if programmes else None,
            'sort_order': 1,
            'show_in_nav': False,
        },
        {
            'name': '公园活动',
            'slug': 'programmes-parks',
            'column_type': ColumnType.POST,
            'parent_id': programmes.id if programmes else None,
            'sort_order': 2,
            'show_in_nav': False,
        },

        # 博文活动子栏目
        {
            'name': '河南大学合作',
            'slug': 'events-henan',
            'column_type': ColumnType.SINGLE_PAGE,
            'parent_id': events.id if events else None,
            'sort_order': 1,
            'show_in_nav': False,
        },
    ]

    # 添加子栏目
    for col_data in subcolumns:
        # 检查是否已存在
        existing = session.query(SiteColumn).filter_by(slug=col_data['slug']).first()
        if existing:
            print(f"跳过已存在的栏目: {col_data['name']} ({col_data['slug']})")
            continue

        column = SiteColumn(**col_data)
        session.add(column)
        print(f"添加子栏目: {col_data['name']} ({col_data['slug']}) -> parent_id={col_data['parent_id']}")

    session.commit()
    print("\n子栏目添加完成！")

def update_parent_column_types():
    """更新父栏目类型，使其支持子栏目"""

    # 有子栏目的父栏目应该改为 CUSTOM 类型，这样可以有自定义的landing page
    updates = [
        ('school', ColumnType.CUSTOM),  # 中文学校改为CUSTOM，做landing page
        ('chess', ColumnType.CUSTOM),   # 保持CUSTOM
        ('badminton', ColumnType.CUSTOM),  # 保持CUSTOM
        ('programmes', ColumnType.CUSTOM),  # 保持CUSTOM
        ('events', ColumnType.CUSTOM),  # 保持CUSTOM
    ]

    for slug, new_type in updates:
        column = session.query(SiteColumn).filter_by(slug=slug).first()
        if column and column.column_type != new_type:
            old_type = column.column_type
            column.column_type = new_type
            print(f"更新栏目类型: {column.name} ({slug}) {old_type} -> {new_type}")

    session.commit()
    print("\n父栏目类型更新完成！")

def display_structure():
    """显示当前栏目结构"""
    print("\n=== 当前栏目结构 ===\n")

    # 获取所有一级栏目
    top_columns = session.query(SiteColumn).filter_by(parent_id=None).order_by(SiteColumn.sort_order).all()

    for col in top_columns:
        nav_status = "✓" if col.show_in_nav else "✗"
        print(f"{nav_status} {col.name} (/{col.slug}/) - {col.column_type.value}")

        # 获取子栏目
        children = session.query(SiteColumn).filter_by(parent_id=col.id).order_by(SiteColumn.sort_order).all()
        for child in children:
            child_nav_status = "✓" if child.show_in_nav else "✗"
            print(f"  {child_nav_status} └─ {child.name} (/{child.slug}/) - {child.column_type.value}")

if __name__ == "__main__":
    print("开始更新栏目结构...\n")

    # 1. 更新父栏目类型
    update_parent_column_types()

    # 2. 添加子栏目
    add_subcolumns()

    # 3. 显示最终结构
    display_structure()

    session.close()
