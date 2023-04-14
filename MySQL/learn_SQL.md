### 子查询
- link：https://blog.csdn.net/qq_44111805/article/details/124680208
- ` select * from emp where sal>(select sal from emp where empno=100013) ;` 查看比100013号员工工资高的行
### select
- help select
- select_expr
  - 列或者表达式或者*; 有多表时可以 tbl_A.*
  - 表达式 是mysql函数如 AVG/count : https://www.runoob.com/mysql/mysql-functions.html
    - count() 返回查询的记录总数 `select id, count(*) as address_count from tbl_b group by id AS tbl_new;` 返回tbl_b的行数, 并生成一个两列名分别为id, address_count(表示tbl_b中id的个数)的新表, 新表名为tbl_new 用在查询中; 需要靠id分组, 要不只有一行

### insert
- 插入行
```
insert into #列名不需要加双引号
```
### union
  - UNION 用于把来自多个 SELECT 语句的结果组合到一个结果集合中
  - 多个 SELECT 语句中，对应的列应该具有相同的字段属性，且第一个 SELECT 语句中被使用的字段名称也被用于结果的字段名称
  - 当使用 UNION 时，MySQL 会把结果集中重复的记录删掉; 而使用 UNION ALL ，MySQL 会把所有的记录返回，且效率高于 UNION
   
### group by
- link:https://www.jianshu.com/p/8f35129dd2ab
- group by col_name 子句会根据给定的数据列col_name的每个成员对查询结果进行分组
- select 子句中必须只有分组列和列函数，(否则会报错，因为其他列不一定会只有一个结果，即一个分组后一个col_name可能会对应多个别的值)，列函数对每个分组返回一个值
```
select sal,deptno from emp group by sal;
ERROR 1055 (42000): Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'go.emp.deptno' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```

### sorted by 
  - link: https://www.cnblogs.com/Guhongying/p/10541979.html
  - SELECT * FROM stu ORDER BY Sno DESC; desc 只作用于前面的一个列， 降序排列； asc是升序，默认
  - 

### top/limit MySQL不支持top
```
mysql 语法
select * from tbl_name [limit 5 offset 4]前4个不要往后排5个
top语法
SELECT TOP 2 * FROM Persons 头两条
SELECT TOP 2 percent * FROM Persons 结果的2%
```

### like
- 模糊查询 like not like
- 不会区分大小写了 like "Ab" 也能查到ab
- 占位符
  - % 任意个字符
  - _ 一个字符
  - [abc] 字符a或者字符b或者字符c
  - [!abc] 除字符a或者字符b或者字符c的任意字符
  - `select * from user where name like ‘_[AB]%’` # 查找name第二个字符为A或者B的用户信息。

### 连接 join
- 连接是SQL的核心
- 全连接应该也属于外连接吧? -------------no
![各种连接结果](https://www.runoob.com/wp-content/uploads/2019/01/sql-join.png)
![连接分类](https://images2018.cnblogs.com/blog/592892/201804/592892-20180423145538091-1111373527.png)
- link
  - https://www.cnblogs.com/wanglijun/p/8916790.html
  - 图中带颜色的表是代表在该表在结果中出现, 而不是结果中相关表的内容是不是为空
- cross join 笛卡尔积/ 交叉连接
  ```
  select * from tbl_A cross join tbl_B; # 显示的交叉连接
  select * from tbl_A, tbl_B;# 隐式的交叉连接, 没有关键字
  select * from tbl_A join tbl_B; ON为空时也是同样效果;
  ```
- 内联接
  - 取交集
  - 等价写法 inner join; straight_join; join; 还有where写法
  ```
  select <select_list> from tableA [as] A] join/inner join/straight_join tblB B on condition;
  ```
- 外连接
  - 取并集
  - 分为左连接(左外连接)/(右连接(右外链接)/完整外连接(全连接) 三种
  - 左连接
    - 取左边的表的全部，右边的表按条件，符合的显示，不符合则显示null
    - left outer join 与 left join 等价，一般写成left join
    - 可以根据where 右表为空去排除交集 注意使用is 而不是=
    `select * from tbl_A a left join tbl_B b on a.id=b.id where b.id is null(NULL)`
    - 连接多个表
    ```
    select a.xx ... 
    from a 
    join b on xxx
    join c on xxx
    ```
  
  - 右连接
    - 取右表的全部, 左表按条件, 符合的显示, 不符合显示NULL
    - right outer join 与 right join等价，一般写成right join

  - 全连接（Full outer join）
    - 全外连接是在结果中除了显示满足连接的条件的行外，还显示了join两侧表中所有满足检索条件的行
    - full outer join 等价 full join (oracle, DB2支持)
    `select * from tbl_A full outer join tbl_B on a.id=b.id;`
    - MySQL本身不支持full join（全连接），但可以通过union来实现
    ```
    select * from Person as a left join Profession as b on a.id=b.id 
    union
    select * from Person a right join Profession b on a.id=b.id;
    # 排除交集应该在union的两表上都加那个条件
    select * from Person as a left join Profession as b on a.id=b.id where a.id is null or b.id is null 
    union 
    select * from Person as a right join Profession b on a.id=b.id where a.id is null or b.id is null;
    ```

# other
### 比较操作符
- =,>,>=,<,<=和between

### 排序规则 collate 创建表时使用
  - link
    - https://www.cnblogs.com/binjoy/articles/2638708.html
  - 使用
    - `collate collation_name`
      - `CityName nvarchar(10)collate chinese_prc_ci_as null`
    - 参数collate_name是应用于表达式、列定义或数据库定义的排序规则的名称。collation_name 可以只是指定的 Windows_collation_name 或 SQL_collation_name。

### SQL中占位符拼接符（纯SQL语句中好像没有）
- link：https://www.cnblogs.com/xdyixia/p/7844984.html
- PreparedStatement是用来执行SQL查询语句的API之一, 用于执行参数化查询；这里会用到占位符和拼接符
- #{}表示一个占位符号，通过#{}把parameterType 传入的内容通过preparedStatement向占位符中设置值，自动进行java类型和jdbc类型转换，#{}可以有效防止sql注入。

# SQL
- where 中带括号是什么意思:`select * from Person where id = 1;`
- 子查询(表子查询)
  - `select * from (select * from Person where age>10) as a;`
  - 查询user对象, 以及每个id拥有的address个数
    ```
    SELECT users.*, adr_count.address_count FROM users LEFT OUTER JOIN
    (SELECT user_id, count(*) AS address_count
        FROM addresses GROUP BY user_id) AS adr_count
    ON users.id=adr_count.user_id
    ```
- 这个[...]是什么意思? `INSERT INTO users (name, fullname, nickname) VALUES (?, ?, ?)[...] ('jack', 'Jack Bean', 'gjffdd')` # 有语法错误, 应该是省略的意思/可能是格式化字符串的?(不是) --------------no
```
MariaDB [test]> insert into Person(age, name) values (?, ?)[...](18, "haha");
# syntax error
insert into tbl_name(col_name, ...) 这种可以
```