# mysqldump
- link: https://zhuanlan.zhihu.com/p/269983875
```cs
-u mysql的用户 可以用空格隔开，也可以不用
-p 后面可以跟密码
-P 指定连接数据库的端口
-h 指定数据库的ip地址
// 导出school数据库中指定表的数据和结构
mysqldump -uroot -p school --tables sc_admin users > /tmp/school.sql
mysqldump -u root -p -P3306 -h 10.240.5.194 --databases school --tables sc_admin > backup.sql

//恢复 只恢复表的时候数据库一定要存在
mysql -u root -p --database db_name
source /path/to/backup.sql
```
# 使用命令行导出表数据为 CSV 文件
- 如果只需备份表的数据而不是整个表结构，你可以使用 MySQL 命令行工具导出数据为 CSV 文件
```cs
SELECT * INTO OUTFILE 'table_data.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM your_table;

```
# 使用复制表结构和数据： 另一种备份方法是创建一个新表，具有与原始表相同的结构，并将数据从原表复制到新表。这可以通过 SQL 命令完成，如下所示
```
CREATE TABLE new_table LIKE your_table;
INSERT INTO new_table SELECT * FROM your_table;
```