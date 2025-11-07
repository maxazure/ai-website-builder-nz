# 数据库恢复指南

本目录包含 Bowen Education Manchester 网站的数据库备份和恢复脚本。

## 文件说明

- `database_backup.sql` - 完整的数据库备份文件（包含表结构和所有数据）
- `restore_database.sh` - Bash 恢复脚本
- `restore_database.py` - Python 恢复脚本（推荐使用，功能更完善）

## 快速使用

### 方法一：使用 Bash 脚本（Linux/Mac）

```bash
cd bowen-education-manchester
./restore_database.sh
```

或者指定目标数据库路径：

```bash
./restore_database.sh /path/to/database.db
```

### 方法二：使用 Python 脚本（跨平台）

```bash
cd bowen-education-manchester
python restore_database.py
```

或者指定目标数据库路径：

```bash
python restore_database.py /path/to/database.db
```

## 功能特点

✓ **自动备份** - 恢复前自动备份现有数据库
✓ **安全确认** - 覆盖前需要用户确认
✓ **完整性验证** - 恢复后自动验证数据库
✓ **详细日志** - 彩色输出，清晰展示恢复过程

## 数据库信息

数据库包含以下表（共 40+ 张表）：

- **用户和权限**: user
- **内容管理**: post, post_category, single_page, comment
- **产品和订单**: product, product_category, order, order_item, cart, cart_item
- **预订系统**: booking, booking_service, booking_time_slot
- **活动管理**: event, event_registration, event_ticket_type
- **文件和媒体**: media_file, file_download, gallery, gallery_image, video
- **餐厅**: restaurant_order, restaurant_order_item, menu_item, menu_category
- **作品集**: portfolio, portfolio_category, portfolio_image
- **团队和评价**: team_member, review
- **常见问题**: faq, faq_category
- **联系和订阅**: contact_message, newsletter_subscriber, newsletter_campaign
- **网站设置**: site_setting, site_column
- 以及更多...

## 注意事项

⚠️ **重要提醒**：
- 恢复操作会**覆盖**目标数据库的所有现有数据
- 脚本会在覆盖前自动创建带时间戳的备份
- 确保在生产环境使用前先在测试环境验证
- 建议定期备份数据库

## 手动恢复（可选）

如果不想使用脚本，也可以手动恢复：

```bash
# 删除旧数据库（可选，先备份！）
rm instance/database.db

# 导入备份
sqlite3 instance/database.db < database_backup.sql
```

## 故障排除

### 问题：权限不足
```bash
chmod +x restore_database.sh
chmod +x restore_database.py
```

### 问题：找不到 sqlite3
**Ubuntu/Debian:**
```bash
sudo apt-get install sqlite3
```

**Mac:**
```bash
brew install sqlite3
```

### 问题：Python 脚本运行失败
确保使用 Python 3:
```bash
python3 restore_database.py
```

## 创建新备份

如果需要重新创建备份文件：

```bash
sqlite3 instance/database.db .dump > database_backup.sql
```
