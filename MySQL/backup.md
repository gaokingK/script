# mysqldump
- link: https://zhuanlan.zhihu.com/p/269983875
```cs
-u mysql的用户 可以用空格隔开，也可以不用
-p 后面可以跟密码 也可以不跟，会提示输入,如果跟密码 -pywPT\!@34(1是要紧跟-p,2是!前要加转义) 
-P 指定连接数据库的端口
-h 指定数据库的ip地址
- --databases 后面跟数据库名，也可以不用这个，直接把数据库名放在mysqldump后面，还可以用--database
- --tables 后面跟表名，也可以用--table
// 导出school数据库中指定表的数据和结构
mysqldump -uroot -p school --tables sc_admin users > /tmp/school.sql
mysqldump -u root -p -P3306 -h 10.240.5.194 --databases school --tables sc_admin > backup.sql

//恢复 只恢复表的时候数据库一定要存在
mysql -u root -p --database db_name
source /path/to/backup.sql
```
# 使用命令行导出表数据为 CSV 文件
- https://www.navicat.com.cn/company/aboutus/blog/497-%E5%B0%86-mysql-%E8%A1%A8%E5%AF%BC%E5%87%BA%E5%88%B0-csv
- 如果只需备份表的数据而不是整个表结构，你可以使用 MySQL 命令行工具导出数据为 CSV 文件
```cs
SELECT * INTO OUTFILE 'table_data.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM your_table;

(SELECT 'id',"base_url","domain_count", "ipv6_count", "ipv4_count", "ipv6_precent","create_time")
UNION
(SELECT * INTO OUTFILE 'C:\\Users\\Farben\\Documents\\t_url_dns_res.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM t_url_dns_res);

(SELECT 'id',"base_url","url", "domain", "is_ipv6", "ipv6","ipv6_precent","create_time")
UNION
(SELECT * INTO OUTFILE 'C:\\Users\\Farben\\Documents\\t_url_dns_res_detail.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM t_url_dns_res_detail);
```
# 解决ERROR 1290 (HY000): The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
- link：https://softwareg.com.au/blogs/windows-security/how-to-disable-secure-file-priv-mysql-windows
- 
# 使用复制表结构和数据： 另一种备份方法是创建一个新表，具有与原始表相同的结构，并将数据从原表复制到新表。这可以通过 SQL 命令完成，如下所示
```
CREATE TABLE new_table LIKE your_table;
INSERT INTO new_table SELECT * FROM your_table;
```
