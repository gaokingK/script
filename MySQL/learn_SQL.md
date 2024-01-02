### 注意
- 实在找不到问题的sql报错可以试着是不是某个变量是关键字，比如rank
- 空有两种，一种是null，一种是字符串的空
  - 判空 要用is null 不能用=null
  - trim(column)=''
### 子查询
- link：https://blog.csdn.net/qq_44111805/article/details/124680208
- ` select * from emp where sal>(select sal from emp where empno=100013) ;` 查看比100013号员工工资高的行
- 子查询必须在括号内
### sql语法规范
- https://help.aliyun.com/zh/dataworks/user-guide/sql-coding-guidelines-and-specifications
### SQL 中主要关键字的执行顺序
```
from
on
join
where
group by
having
select
distinct
union
order by 默认升序
limit offset
# 因此一个显而易见的SQL优化的方案是，当两张表的数据量比较大又需要连接查询时, 应该使用on, 而不是where, 因为后者会在内存中先生成一张数据量比较大的笛卡尔积表，增加了内存的开销。
```
- 有没有一个地方能看帮助中synatx的名词的意思?
  - http://www.jooq.org/doc/3.1/manual/sql-building/sql-statements/select-statement/implicit-join/
- `help select `的syntax中 为啥么是from table_references 而不是tbl_name
  - 并不一定从已有表中查询, 当进行子查询,链接查询时, 就是从一个查询结果中去查询,这时就是reference
### select
- help select
- select_expr
  - 列或者表达式或者*; 有多表时可以 tbl_A.*
  - 表达式 是mysql函数如 AVG/count : https://www.runoob.com/mysql/mysql-functions.html
    - count() 返回查询的记录总数 `select id, count(*) as address_count from tbl_b group by id AS tbl_new;` 返回tbl_b的行数, 并生成一个两列名分别为id, address_count(表示tbl_b中id的个数)的新表, 新表名为tbl_new 用在查询中; 需要靠id分组, 要不只有一行

### update
- 更新一个值：`UPDATE coupon_pool SET serialno = '20170319010010'  WHERE id = 10;`
- 更新多个值:`UPDATE coupon_pool SET serialno = '20170319010010' , name = '名字10'  WHERE id = 10;`
- delete 不能来自删除来自同一个表的,你需要一个子表 :可以这样写 DELETE FROM Person WHERE id NOT IN ( select *from (SELECT MIN(id) as id FROM Person GROUP BY email ) as a )
- DELETE p1 FROM Person p1, Person p2 WHERE p1.Email = p2.Email AND p1.Id > p2.Id
  - a. 从驱动表（左表）取出N条记录；
  - b. 拿着这N条记录，依次到被驱动表（右表）查找满足WHERE条件的记录；如果有满足条件的，就删除

作者：😼吴腾跃
链接：https://leetcode.cn/problems/delete-duplicate-emails/solutions/219860/dui-guan-fang-ti-jie-zhong-delete-he-de-jie-shi-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### insert
- 插入行
```
insert into #列名不需要加双引号
```
### delete
DELETE FROM table_name WHERE condition;
### in # exists
- 使用 IN 和 EXISTS 子句时，注意它们之间的差异。IN 用于比较一个值是否在子查询返回的结果集中，而 EXISTS 用于检查子查询是否返回了任何行。
- 简单使用方法 `select * from tbl_1 where col_1 in ("value1", "value2",...)`
- 从表中比较`select * from tbl_1 where col_1 in (select )`
- 多列比较必须加括号，顺序可以不对应 但数量和列一定要对应（查询子句中有salary，departmentId，必须要用salary，departmentId来比较）`select  name as Employee, salary from Employee where (salary, departmentId) in (select max(salary), departmentId from Employee group by departmentId) `

### union
  - UNION 用于把来自多个 SELECT 语句的结果组合到一个结果集合中
  - 多个 SELECT 语句中，对应的列应该具有相同的字段属性，且第一个 SELECT 语句中被使用的字段名称也被用于结果的字段名称
  - 当使用 UNION 时，MySQL 会把结果集中重复的记录删掉; 而使用 UNION ALL ，MySQL 会把所有的记录返回，且效率高于 UNION

### order by
- 默认升序 ascending 
- 降序 SELECT * FROM Products ORDER BY ProductName DESC;
- 子查询一个数据的时候，order 慢与 min函数（也可能给值得类型有关系）

### distinct 去重
- select distinct name from A
- select id, distinct name from A;   --会提示错误，因为distinct必须放在开头
- select distinct name， id 是根据name+id来去重的，如果name相同，id不同，distinct会认为两个是不同的，可以使用`select *, count(distinct name) from table group by name`

### group by
- link:https://www.jianshu.com/p/8f35129dd2ab
- group by col_name 子句会根据给定的数据列col_name的每个成员对查询结果进行分组（比如group by col_a, 就类似把col_a 为value_A的化为一块，value_B的化为一块）
- select 子句中必须只有分组列， 如果含有其他列必修对其他列使用列函数，(否则会报错，因为其他列不一定会只有一个结果，即一个分组后一个col_name可能会对应多个别的值)，列函数对每个分组返回一个值； 其他列可以使用*代替
```
select sal,deptno from emp group by sal;
ERROR 1055 (42000): Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'go.emp.deptno' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```
- select sum(dept_no) from dept_manager group by dept_no; 结果列中全为0，因为通过dept_no分组后的列中就没有dept_no了，但是可以count(dept_no)

### having
- https://www.runoob.com/sql/sql-having.html
- where子句中无法使用聚合函数，having子句可以让我们筛选分组后的数据
- where 和having之后都是筛选条件，但是有区别的：
  - where在group by前， having在group by 之后
  - 聚合函数（avg、sum、max、min、count），不能作为条件放在where之后，但可以放在having之后
```sql
//现在我们想要查找总访问量大于 200 的网站，并且 alexa 排名小于 200。
SELECT Websites.name, SUM(access_log.count) AS nums FROM Websites
INNER JOIN access_log
ON Websites.id=access_log.site_id
WHERE Websites.alexa < 200 
GROUP BY Websites.name
HAVING SUM(access_log.count) > 200;
// 好像不能使用列，必须要用列的聚合函数
select count(dept_no) as a from dept_manager group by dept_no having a>2
// 可以用列的，见group by
select email from Person group by email having count(email) > 1;
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
- limit 不支持运算 不能使用 limit 5-1 ；必须set N=5-1 然后再limit N
### like
- 模糊查询 like not like
- 不会区分大小写了 like "Ab" 也能查到ab
- 占位符
  - % 任意个字符
  - _ 一个字符
  - [abc] 字符a或者字符b或者字符c
  - [!abc] 除字符a或者字符b或者字符c的任意字符
  - `select * from user where name like ‘_[AB]%’` # 查找name第二个字符为A或者B的用户信息。

### on
- 在 SQL 中，ON 子句用于指定连接两个表时的条件。他用于过滤连接的结果，只使两个表中满足条件的行返回。
- ON 子句和笛卡尔积（Cartesian product）是相关的，但它们不是完全相同的概念。笛卡尔积返回的结果是两个表中所有行之间所有可能的组合。（笛卡尔积发生在没有指定连接条件，或者没有适当的连接条件）
```sql
// dept_manger有24行，departments有9行
select count(*) from dept_manager a join departments b on a.dept_no=b.dept_no; //返回24
select count(*) from dept_manager join departments; //返回216=9*24
```
- JOIN 关键字用于表示连接操作。ON 关键字用于指定连接条件，即在两个表中相互匹配的列。连接条件通常是两个表之间的相等关系，但也可以是其他条件，具体取决于你的需求。通常是一起使用的但也可分开`SELECT * FROM table1 JOIN table2 USING (column_name);`
### 自连接
- 把自己的表连接到直接的表
- `select a.name as "Employee"  from Employee as a join Employee as b on a.managerId = b.id where a.salary > b.salary`
### 连接 # join
- 连接是SQL的核心
- 全连接应该也属于外连接吧? -------------no
![各种连接结果](https://www.runoob.com/wp-content/uploads/2019/01/sql-join.png)
![连接分类](https://images2018.cnblogs.com/blog/592892/201804/592892-20180423145538091-1111373527.png)
- link
  - https://www.cnblogs.com/wanglijun/p/8916790.html
  - 圆圈代表表，一个圆圈全部有颜色代表所有行都在结果中，两个园圈重合的代表都满足连接条件的行，图中带颜色的表是代表该表在结果中出现, 而不是结果中相关表的内容是不是为空
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
  select xxx from tbl_name1, tbl_name2 where tbl_name1.col=tbl_name2.col
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
- 一个表使用两次
```sql
select a.score as score, 
(select count(distinct b.score) from Scores b where b.score >= a.score) as 'Rank' 
from Scores a 
order by a.score Desc
# 另外一个
select a.name as "Employee"  from Employee as a join Employee as b on a.managerId = b.id where a.salary > b.salary
```
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