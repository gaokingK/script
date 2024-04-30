# 函数
- [所有函数](https://www.w3schools.com/sql/func_mysql_floor.asp)
- https://docs.aws.amazon.com/zh_cn/redshift/latest/dg/r_DATE_TRUNC.html
- 如果某些函数的值会出现在结果列当中，可以使用As来为这个列重命名，如果没有AS，这个列名就是这个函数的语句
- 函数分为标准SQL函数、特定数据库系统，例如 MySQL、PostgreSQL、Oracle 等，它们可能提供了自己的时间处理函数
  
# 日期函数
### CURDATE() # NOW()
- 要查询在今天凌晨后更新的数据，你可以使用MySQL的CURDATE()和NOW()函数来获取日期时间，并结合BETWEEN子句进行选择
```sql
SELECT *
FROM your_table_name
WHERE your_timestamp_column BETWEEN CURDATE() AND NOW();
-- 这个查询会返回在今天凌晨00:00:00 之后和当前时间之前更新的所有记录。如果你只关心从凌晨到现在的记录，那么CURDATE()会返回当天的日期（没有时间部分），而NOW()则返回当前的精确时间。
```
### datediff() 
- datediff(日期1, 日期2)：得到的结果是日期1与日期2相差的天数。如果日期1比日期2大，结果为正；如果日期1比日期2小，结果为负。
### 同一月的时间可以直接加减，但上个月末是这个月月初的前一天，但差值不是1
### TIMESTAMPDIFF和TIMESTAMPADD
- https://blog.csdn.net/zmxiangde_88/article/details/8011661
- 计算时间的
- TIMESTAMPDIFF(interval,datetime_expr1,datetime_expr2)。 datetime_expr2 - datetime_expr1 结果的单位由interval 参数给出
- select TIMESTAMPDIFF(day,'2012-08-24','2012-08-30'); // 1
- select TIMESTAMPDIFF(day,from_date,to_date) from dept_manager; // 必须是日期格式的，且日期有效不能2012-08-32
- select TIMESTAMPDIFF(day,'120831','2012-08-30'); 这样也是可以的

### DATE_TRUNC
- https://docs.aws.amazon.com/zh_cn/redshift/latest/dg/r_DATE_TRUNC.html 
- 根据你指定的单位截断表达式
- 如果传入的单位是year， 将输入时间戳截断至一年的第一天。 SELECT DATE_TRUNC('year', TIMESTAMP '20200430 04:05:06.789'); 2020-01-01 00:00:00	
### date_add() date_sub() 
date_add(x, num) 计算日期x加num天后的日期  
date_sub()
add_months()：月份相加，内是完整日期格式，不完整可以计算，但返回是完整日期格式的值
month_between()
```sql
select update_time, date_add(update_time, 10) as calc_time from tbl_name
update_time calc_time
2023-10-24 14:56:83 2023-10-14 14:56:83
```
### 查看变量 SELECT FLOOR(25.75);
### ifnull(value, b) 
- 如果value不为null，返回value，否则返回b
- `select ifnull((select max(b) from tbl_name), 222 )` # 如果是一个表达式，应该是一个子查询的形式，，并且只能返回一行一列
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
### floor 
- 向下取整
- `select floor(__time to minute), count(*) from tbl_name where xxx group by floor(__time to minute)`
### keywhen
### distinct
- select distinct col_name from tbl_name
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


### dense_rank() over()和# rank() over() # row_number
- 用来看排名 
- rank 是跳次排序 1,1,1,4, dense_rank是不跳次排序1,1,1,2, row_number是顺序1,2,3,4
- 注意逗号分隔
- over() 子句指定如何对窗口函数rank() 的表行进行分区和排序
```sql
RANK() OVER (
    PARTITION BY <expression>[{,<expression>...}]
    ORDER BY <expression> [ASC|DESC], [{,<expression>...}]
) 
select score, dense_rank() over(order by score desc) as "rank" from Scores; # 相同的分数排名相同，不占用排名
| score | Rank |
| ----- | ---- |
| 4     | 1    |
| 4     | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.5   | 4    |
select score, rank() over(order by score desc) as "rank" from Scores; # 相同的分数虽然排名相同，但是占用排名
| score | Rank |
| ----- | ---- |
| 4     | 1    |
| 4     | 1    |
| 3.85  | 3    |
| 3.65  | 4    |
| 3.65  | 4    |
| 3.5   | 6    |
```
### 窗口函数 #PARTITION BY # 开窗函数
- link:https://www.cnblogs.com/cjsblog/p/16743807.html
- 一句话概述就是可以结合函数，然后把parttion子句写在over函数内来为每一个结果行添加一个列，列的值就是函数的值
- 写在select后
- 窗口函数对一组查询行执行类似聚合的操作。不同之处在于聚合操作将查询行分组到单个结果行，而窗口函数为每个查询行产生一个结果:
    - 函数求值发生的行称为当前行
    - 与发生函数求值的当前行相关的查询行组成了当前行的窗口
- 窗口操作不会将一组查询行折叠到单个输出行。相反，它们为每一行生成一个结果。
- 窗口函数只允许在查询列表和 ORDER BY 子句中使用。
- 查询结果行由 FROM 子句确定，在 WHERE、GROUP BY 和 HAVING 处理之后，窗口执行发生在 ORDER BY、LIMIT 和 SELECT DISTINCT 之前。
```sql
RANK() OVER (
    PARTITION BY <expression>[{,<expression>...}]
    ORDER BY <expression> [ASC|DESC], [{,<expression>...}]
) 

select emp_no,salary,
    sum(salary) over(partition by emp_no) as per_emp_total_salary, 
    sum(salary) over() as total_salary 
from (select * from salaries limit 0, 20) salaries;
+--------+--------+----------------------+--------------+
| emp_no | salary | per_emp_total_salary | total_salary |
+--------+--------+----------------------+--------------+
|  10001 |  60117 |              1281612 |      1480883 |
|  10001 |  62102 |              1281612 |      1480883 |
|  10001 |  66074 |              1281612 |      1480883 |
|  10001 |  66596 |              1281612 |      1480883 |
|  10001 |  66961 |              1281612 |      1480883 |
|  10001 |  71046 |              1281612 |      1480883 |
|  10001 |  74333 |              1281612 |      1480883 |
|  10001 |  75286 |              1281612 |      1480883 |
|  10001 |  75994 |              1281612 |      1480883 |
|  10001 |  76884 |              1281612 |      1480883 |
|  10001 |  80013 |              1281612 |      1480883 |
|  10001 |  81025 |              1281612 |      1480883 |
|  10001 |  81097 |              1281612 |      1480883 |
|  10001 |  84917 |              1281612 |      1480883 |
|  10001 |  85112 |              1281612 |      1480883 |
|  10001 |  85097 |              1281612 |      1480883 |
|  10001 |  88958 |              1281612 |      1480883 |
|  10002 |  65828 |               199271 |      1480883 |
|  10002 |  65909 |               199271 |      1480883 |
|  10002 |  67534 |               199271 |      1480883 |
+--------+--------+----------------------+--------------+
- 第一个 OVER 子句是空的，它将整个查询行集视为一个分区。窗口函数因此产生一个全局和，但对每一行都这样做。
- 第二个 OVER 子句按 manufacturer 划分行，产生每个分区（每个manufacturer）的总和。该函数为每个分区行生成此总和 
```
- OVER子句被允许用于许多聚合函数，因此，这些聚合函数可以用作窗口函数或非窗口函数，具体取决于是否存在 OVER 子句：
AVG()
BIT_AND()
BIT_OR()
BIT_XOR()
COUNT()
JSON_ARRAYAGG()
JSON_OBJECTAGG()
MAX()
MIN()
STDDEV_POP(), STDDEV(), STD()
STDDEV_SAMP()
SUM()
VAR_POP(), VARIANCE()
VAR_SAMP()
- 只能作为窗口函数使用的非聚合函数 对于这些，OVER子句是必须的
CUME_DIST()
DENSE_RANK()
FIRST_VALUE()
LAG()
LAST_VALUE()
LEAD()
NTH_VALUE()
NTILE()
PERCENT_RANK()
RANK()
ROW_NUMBER()

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