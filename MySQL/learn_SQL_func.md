# 函数
- [所有函数](https://www.w3schools.com/sql/func_mysql_floor.asp)
### 查看变量 SELECT FLOOR(25.75);
### round
- 此函数返回x舍入到最接近的整数。如果第二个参数，D有提供，则函数返回x四舍五入至第D位小数点。D必须是正数,如果省略D，则返回整数（无小数）
### concat
- link:https://www.yiibai.com/mysql/sql-concat-in-mysql.html
- CONCAT()函数需要一个或多个字符串参数，并将它们连接成一个字符串。CONCAT()函数需要至少一个参数，否则会引起错误。
### SUBSTRING
- `SELECT SUBSTRING("SQL Tutorial", 5, 3) AS ExtractString;` # Extract a substring from a string (start at position 5, extract 3 characters) 从1开始数
### FLOOR
- `FLOOR(25.75);` # Return the largest integer value that is less than or equal to 25.75:
### rand
- `SELECT RAND();` # Return a random decimal number (no seed value - so it returns a completely random number >= 0 and <1):
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