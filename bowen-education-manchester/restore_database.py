#!/usr/bin/env python3
"""
数据库恢复脚本 - Python版本
用法: python restore_database.py [目标数据库路径]
"""

import os
import sys
import sqlite3
import shutil
from datetime import datetime
from pathlib import Path


class Colors:
    """终端颜色"""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color


def print_color(message, color=Colors.NC):
    """打印带颜色的消息"""
    print(f"{color}{message}{Colors.NC}")


def print_header(title):
    """打印标题"""
    print_color("=" * 50, Colors.GREEN)
    print_color(title, Colors.GREEN)
    print_color("=" * 50, Colors.GREEN)
    print()


def backup_existing_database(db_path):
    """备份现有数据库"""
    if not os.path.exists(db_path):
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{db_path}.backup.{timestamp}"

    print_color(f"检测到现有数据库，创建备份...", Colors.YELLOW)
    shutil.copy2(db_path, backup_path)
    print_color(f"已备份到: {backup_path}", Colors.GREEN)
    print()

    return backup_path


def restore_database(sql_file, target_db):
    """恢复数据库"""
    print_color("开始恢复数据库...", Colors.GREEN)

    # 读取 SQL 文件
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    # 连接到数据库并执行 SQL
    conn = sqlite3.connect(target_db)
    try:
        conn.executescript(sql_script)
        conn.commit()
    except Exception as e:
        print_color(f"错误: {str(e)}", Colors.RED)
        conn.close()
        if os.path.exists(target_db):
            os.remove(target_db)
        raise
    finally:
        conn.close()


def verify_database(db_path):
    """验证数据库"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 获取表数量
    cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
    table_count = cursor.fetchone()[0]

    # 获取所有表名
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cursor.fetchall()]

    conn.close()

    return table_count, tables


def main():
    """主函数"""
    # 默认配置
    default_db_path = "instance/database.db"
    backup_sql = "database_backup.sql"

    # 获取目标数据库路径
    target_db = sys.argv[1] if len(sys.argv) > 1 else default_db_path

    print_header("数据库恢复脚本")

    # 检查备份文件是否存在
    if not os.path.exists(backup_sql):
        print_color(f"错误: 找不到备份文件 {backup_sql}", Colors.RED)
        sys.exit(1)

    print_color(f"备份文件: {backup_sql}", Colors.YELLOW)
    print_color(f"目标数据库: {target_db}", Colors.YELLOW)
    print()

    # 如果目标数据库存在，先备份
    backup_path = None
    if os.path.exists(target_db):
        backup_path = backup_existing_database(target_db)

        # 询问用户是否继续
        response = input("是否继续恢复数据库? 这将覆盖现有数据 (y/N): ").strip().lower()
        if response not in ['y', 'yes']:
            print_color("操作已取消", Colors.YELLOW)
            sys.exit(0)

        # 删除现有数据库
        os.remove(target_db)

    # 确保目标目录存在
    target_dir = os.path.dirname(target_db)
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    try:
        # 恢复数据库
        restore_database(backup_sql, target_db)

        # 验证恢复
        table_count, tables = verify_database(target_db)

        print()
        print_header("恢复完成!")
        print_color(f"数据库表数量: {table_count}", Colors.GREEN)
        print()

        # 显示所有表
        print_color("数据库表列表:", Colors.YELLOW)
        for i, table in enumerate(tables, 1):
            print(f"  {i:2d}. {table}")

        print()
        print_color("✓ 数据库恢复成功!", Colors.GREEN)

    except Exception as e:
        print_color(f"恢复失败: {str(e)}", Colors.RED)

        # 如果有备份，询问是否恢复
        if backup_path and os.path.exists(backup_path):
            print()
            response = input("是否恢复之前的备份? (y/N): ").strip().lower()
            if response in ['y', 'yes']:
                shutil.copy2(backup_path, target_db)
                print_color("已恢复到备份版本", Colors.GREEN)

        sys.exit(1)


if __name__ == "__main__":
    main()
