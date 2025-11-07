#!/bin/bash

# 数据库恢复脚本
# 用法: ./restore_database.sh [目标数据库路径]

set -e

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 默认目标数据库路径
DEFAULT_DB_PATH="instance/database.db"
BACKUP_SQL="database_backup.sql"

# 使用提供的路径或默认路径
TARGET_DB="${1:-$DEFAULT_DB_PATH}"

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}数据库恢复脚本${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# 检查备份文件是否存在
if [ ! -f "$BACKUP_SQL" ]; then
    echo -e "${RED}错误: 找不到备份文件 $BACKUP_SQL${NC}"
    exit 1
fi

echo -e "${YELLOW}备份文件: $BACKUP_SQL${NC}"
echo -e "${YELLOW}目标数据库: $TARGET_DB${NC}"
echo ""

# 如果目标数据库存在，先备份
if [ -f "$TARGET_DB" ]; then
    BACKUP_NAME="${TARGET_DB}.backup.$(date +%Y%m%d_%H%M%S)"
    echo -e "${YELLOW}检测到现有数据库，创建备份...${NC}"
    cp "$TARGET_DB" "$BACKUP_NAME"
    echo -e "${GREEN}已备份到: $BACKUP_NAME${NC}"
    echo ""

    # 询问用户是否继续
    read -p "是否继续恢复数据库? 这将覆盖现有数据 (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}操作已取消${NC}"
        exit 0
    fi

    # 删除现有数据库
    rm "$TARGET_DB"
fi

# 确保目标目录存在
TARGET_DIR=$(dirname "$TARGET_DB")
mkdir -p "$TARGET_DIR"

# 恢复数据库
echo -e "${GREEN}开始恢复数据库...${NC}"
sqlite3 "$TARGET_DB" < "$BACKUP_SQL"

# 验证恢复
TABLE_COUNT=$(sqlite3 "$TARGET_DB" "SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}恢复完成!${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}数据库表数量: $TABLE_COUNT${NC}"
echo ""

# 显示所有表
echo -e "${YELLOW}数据库表列表:${NC}"
sqlite3 "$TARGET_DB" ".tables"
