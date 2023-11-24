# 函数
- [所有函数](https://www.w3schools.com/sql/func_mysql_floor.asp)
- https://docs.aws.amazon.com/zh_cn/redshift/latest/dg/r_DATE_TRUNC.html
- 如果某些函数的值会出现在结果列当中，可以使用As来为这个列重命名，如果没有AS，这个列名就是这个函数的语句
- 函数分为标准SQL函数、特定数据库系统，例如 MySQL、PostgreSQL、Oracle 等，它们可能提供了自己的时间处理函数
### 查看变量 SELECT FLOOR(25.75);
### round
- 此函数返回x舍入到最接近的整数。如果第二个参数，D有提供，则函数返回x四舍五入至第D位小数点。D必须是正数,如果省略D，则返回整数（无小数）
### concat
- link:https://www.yiibai.com/mysql/sql-concat-in-mysql.html
- CONCAT()函数需要一个或多个字符串参数，并将它们连接成一个字符串。CONCAT()函数需要至少一个参数，否则会引起错误。
### AS 
- 重命名结果列 `select SELECT SUM(Quantity) AS hhh2 FROM OrderDetails;`
- as关键字可以不声明`select SELECT SUM(Quantity) hhh2 FROM OrderDetails;`
### SUBSTRING 
- `SELECT SUBSTRING("SQL Tutorial", 5, 3) AS ExtractString;` # Extract a substring from a string (start at position 5, extract 3 characters) 从1开始数
### FLOOR
- `FLOOR(25.75);` # Return the largest integer value that is less than or equal to 25.75:
### rand
- `SELECT RAND();` # Return a random decimal number (no seed value - so it returns a completely random number >= 0 and <1):
### sum 
- 作用于行，多个行对应一个结果, 如果有group by ，就把group by 里的分组进行运算，如果没有groupby 就把查询的所有结果进行运算
- `select sum(col_name) from tbl_name;` 计算表某一列的所有和
    - 应该不能计算值不是数值的列
- 还可以对每行的数量和价格相乘求和
```sql
SELECT SUM(Price * Quantity)
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID;
```
### count
- link：https://www.w3schools.com/sql/sql_count.asp
- 计算满足条件的行的数量
- 计算表的总行数`select count(*) from tbl_name`
- 计算某列非空值的数量`select count(col_name) from tbl_name`
- 计算某列不重复值的数量`select count(distinct col_name) from tbl_name`
- 计算每个国家的客户数量`select count(Customer) from Order group by Country`

### case
- link:https://www.w3schools.com/sql/sql_case.asp
- 作用与行，每行都有结果
- 如果判断条件为True，就返回then后面的值，并结束case，否则继续往下执行，若是所有的case都不满足，返回else的值，若没有else，返回null
```cs
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;
# 结果
OrderID	Quantity	test
10248	12	The quantity is under 30
10248	10	The quantity is under 30
10248	5	The quantity is under 30
10249	9	The quantity is under 30
10249	40	The quantity is greater than 30
```

### TIMESTAMPDIFF和TIMESTAMPADD
- https://blog.csdn.net/zmxiangde_88/article/details/8011661
- 计算时间的
- TIMESTAMPDIFF(interval,datetime_expr1,datetime_expr2)。 结果的单位由interval 参数给出
- select TIMESTAMPDIFF(day,'2012-08-24','2012-08-30');
- select TIMESTAMPDIFF(day,from_date,to_date) from dept_manager; // 必须是日期格式的，且日期有效不能2012-08-32
- select TIMESTAMPDIFF(day,'120831','2012-08-30'); 这样也是可以的

### DATE_TRUNC
- https://docs.aws.amazon.com/zh_cn/redshift/latest/dg/r_DATE_TRUNC.html 
- 根据你指定的单位截断表达式
- 如果传入的单位是year， 将输入时间戳截断至一年的第一天。 SELECT DATE_TRUNC('year', TIMESTAMP '20200430 04:05:06.789'); 2020-01-01 00:00:00	

### 存储过程
- link:http://c.biancheng.net/view/2593.html
- 查看存储过程 `SELECT * FROM information_schema.Routines WHERE ROUTINE_NAME=存储过程名;`
- 调用存储过程 `call procedure_name(parms)`

### 存储函数
- link：http://c.biancheng.net/view/7838.html
- 调用存储函数 `call func_name(parms)`
- 查看存储过程 `SELECT * FROM information_schema.Routines WHERE ROUTINE_NAME=存储函数名;`

### 存储过程和存储函数的不同
- 存储过程没有返回值，一般用来执行操作
- 定义的关键字不同
- 调用的关键字不同

### 游标（Cursor）
- link:http://c.biancheng.net/view/7823.html
- 游标用来逐条读取查询结果集中的记录，只能像迭代器一样。