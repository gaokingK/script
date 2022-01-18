# 准备和使用
### 产品和版本选择
  - link
    - 产品:https://blog.csdn.net/chw0629/article/details/106206272
    - 版本:
  - 一共有四个产品
    - MySQL Community Server 社区版本，开源免费，但不提供官方技术支持
    - MySQL Enterprise Edition 企业版本，需付费，可以试用30天。
    - MySQL Cluster 集群版，开源免费。可将几个MySQL Server封装成一个Server。要先把mysql装上
    - MySQL Workbench（GUITOOL）一款专为MySQL设计的ER/数据库建模工具。它是著名的数据库设计工具DBDesigner4的继任者。
  - mysql-server主要的三个版本 5.6/5,7/8.0
    - 使用5.7
### 连接服务器
- 添加用户:
  - link:https://www.runoob.com/mysql/mysql-administration.html
  - 可以设置用户名和密码, 以及用户可以进行的操作如(select/insert等)
- 检查服务是否启动`ps -ef | grep mysqld`
- 启动服务器 `cd /usr/bin;sudo  ./mysqld_safe &` # 好像加&不行, 不加可以 
- 关闭服务器 `cd /usr/bin; ./mysqladmin -u root -p shutdown`
- mysql
  - -p 怎么把命令跟在-p后面而不是回车后再输入? --------------------no
  - -u user_name # 某些用户有密码,这时要加-p 不加连不进去
  - 后面可以直接跟要使用的数据库吗?
  - mysql -u root -p # 示例
- 提示符
```s
MariaDB [(none)]> # none 是当前使用数据库的名字
```
### 寻找帮助
- help contents 按目录查看
- help create database;
- Mycli 是一个 MySQL，MariaDB 和 Percona 命令行客户端，具有自动补全、智能补全、别名支持、页面调整和语法高亮功能。
### 管理MySQL
- link: https://www.runoob.com/mysql/mysql-administration.html
- show databases;
  - information_schema/mysql以及 performance_schema是系统数据库
- use database_name;
- create database database_name;
- drop database database_name;
- show tables; 使用该命令前需要使用 use 命令来选择要操作的数据库。
  
- show COLUMNS FROM 数据表:显示数据表的属性
- show INDEX FROM 数据表: 显示数据表的详细索引信息，包括PRIMARY KEY（主键）。
- SHOW TABLE STATUS [FROM db_name] [LIKE 'pattern'] \G: 
  - 命令各项的意思可以 help show table status
    - update_time InnoDBy 引擎是Null, InnoDB 在其系统表空间中存储多个表，数据文件时间戳不适用, 
    - Update_time displays a timestamp value for the last UPDATE, INSERT, or DELETE performed on InnoDB tables that are not partitioned? 
  - 该命令将输出Mysql数据库管理系统的性能及统计信息。
  - \G;   # 加上 \G，查询结果按列打印
  ```s
  mysql> SHOW TABLE STATUS  FROM RUNOOB;   # 显示数据库 RUNOOB 中所有表的信息
  mysql> SHOW TABLE STATUS from RUNOOB LIKE 'runoob%';     # 表名以runoob开头的表的信息
  mysql> SHOW TABLE STATUS from RUNOOB LIKE 'runoob%'\G;   # 加上 \G，查询结果按列打印
  ```

# 简单命令
### 表 
- 创建表 help create table;
```
create table table_name
(
column1 data_type[(data_length)],
... 
# 最后一个不能加,号了
# varchar() 必须带括号,而且其中必须有值
)
# create table Person (Id int, age int, name varchar(255) );
```
- 修改表 help alter table;
```
# 修改列属性使用modify
alter table Person modify Id int not null auto_increment unique key comment 'id号'; 数据类型需要重新声明? 原本为空的设置为非空后会自动赋值
# 修改列名 怎么只修改列名,而不传入属性-------------no
alter table tbl_name change old_name new_name 随便一个属性;

# 自增, 自增属性必须为key, 且一个表中自增只有一个;
# 删除自增属性,
 alter table Profession modify id int(11), drop primary key;
```
- SHOW [FULL] COLUMNS FROM tbl_name [FROM db_name] [like_or_where] 等价于desc tbl_name
- 插入行
```
insert into 
```
### sorted by 
  - link: https://www.cnblogs.com/Guhongying/p/10541979.html
  - SELECT * FROM stu ORDER BY Sno DESC; desc 只作用于前面的一个列， 降序排列； asc是升序，默认
  - 
### select
- help select
- select_expr
  - 列或者表达式或者*; 有多表时可以 tbl_A.*
  - 表达式 是mysql函数如 AVG/count : https://www.runoob.com/mysql/mysql-functions.html
    - count() 返回查询的记录总数 `select id, count(*) as address_count from tbl_b group by id AS tbl_new;` 返回tbl_b的行数, 并生成一个两列名分别为id, address_count(表示tbl_b中id的个数)的新表, 新表名为tbl_new 用在查询中; 需要靠id分组, 要不只有一行
### insert
```
insert into 列名不需要加双引号
```
### update
```
```
### union
  - UNION 用于把来自多个 SELECT 语句的结果组合到一个结果集合中
  - 多个 SELECT 语句中，对应的列应该具有相同的字段属性，且第一个 SELECT 语句中被使用的字段名称也被用于结果的字段名称
  - 当使用 UNION 时，MySQL 会把结果集中重复的记录删掉; 而使用 UNION ALL ，MySQL 会把所有的记录返回，且效率高于 UNION

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

# 共识
- col_name (column name); tbl_name(table_name)\

# 其他
### MySql Innodb引擎 SQL中使用悲观锁
- MySQL默认使用autocommit模式, 即执行一个更新操作后, MySql会立刻将结果进行提交; 若使用悲观锁, 需要关闭`set autocommit=0`
- 使用 select…for update 锁数据，需要注意锁的级别，MySQL InnoDB 默认行级锁。行级锁都是基于索引的，如果一条 SQL 语句用不到索引是不会使用行级锁的，会使用表级锁把整张表锁住，这点需要注意。

```
// 比较典型的悲观锁策略: 修改前, 先使用for update 加锁, 然后再进行修改.
如果发生并发，同一时间只有一个线程可以开启事务并获得 id=1 的锁，其它的事务必须等本次事务提交之后才能执行。 
//0. 开始事务
begin;
//1. 查询商品库存信息
select quantity from items where id=1 for update;
//2. 修改商品库存为2
update items set quantity=2 where id=1;
//3. 提交事务
commit;
```
### MySQL InnoDB 行记录格式（ROW_FORMAT）
- link
  - https://blog.csdn.net/uiuan00/article/details/103166724
- 行记录格式 文件格式
  - 文件格式
    - Antelope 和 Barracuda
    - Antelope: 先前未命名的，原始的InnoDB文件格式。它支持两种行格式：COMPACT 和 REDUNDANT。MySQL5.6的默认文件格式。可以与早期的版本保持最大的兼容性。但不支持 Barracuda 文件格式。
    - Barracuda: 新的文件格式。它支持InnoDB的所有行格式，包括新的行格式：COMPRESSED 和 DYNAMIC。与这两个新的行格式相关的功能包括：InnoDB表的压缩，长列数据的页外存储和索引建前缀最大长度为3072字节。


  - 行格式 compact redundant DYNAMIC COMPRESSED
    - 在 msyql 5.7.9 及以后版本，默认行格式由innodb_default_row_format变量决定，它的默认值是DYNAMIC，也可以在 create table 的时候指定ROW_FORMAT=DYNAMIC。用户可以通过命令 SHOW TABLE STATUS LIKE'table_name' 来查看当前表使用的行格式，其中 row_format 列表示当前所使用的行记录结构类型。
    - 一个表的行格式决定了它的物理存储,进而会影响查询和DML(Data Manipulation Language 数据操作语言)操作的性能


### 数据类型
- help create table 中data type中查看所有的
- 整型 bigint、int、mediumint、smallint 和 tinyint的取值范围
  - link: https://www.cnblogs.com/wayne173/p/3747477.html
  - 从小到大是 tinyint/smallint/mediumint/int/bight

- decimal
  - decimal(10, 4) 一共能存10位数字，小数部分最多有4位。（多的化会四舍五入后把多出来的扔掉）
  - 定义了zerofill后，插入负数会报错
### 连接 join
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
# 问题
- SQL 中主要关键字的执行顺序
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
order by
# 因此一个显而易见的SQL优化的方案是，当两张表的数据量比较大又需要连接查询时, 应该使用on, 而不是where, 因为后者会在内存中先生成一张数据量比较大的笛卡尔积表，增加了内存的开销。
```
- 有没有一个地方能看帮助中synatx的名词的意思?
  - http://www.jooq.org/doc/3.1/manual/sql-building/sql-statements/select-statement/implicit-join/
- `help select `的syntax中 为啥么是from table_references 而不是tbl_name
  - 并不一定从已有表中查询, 当进行子查询,链接查询时, 就是从一个查询结果中去查询,这时就是reference
- create database test-test;
```
MariaDB [ccnet-db]> create database test-test;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '-test' at line 1
# 为什么会报错呢?
help create database;
# https://dev.mysql.com/doc/refman/8.0/en/identifiers.html
Rules for permissible database names are given in Section 9.2, “Schema Object Names”. 
# 因为不加反引号,只能使用[0-9,a-z,A-Z$_]
# 加反引号可以使用 ASCII: U+0001 .. U+007F, 除了Extended: U+0080 .. U+FFFF
use database_name 时可以不用加
```
- InnoDB partitioned(InnoDB 分区)?
- help join?
  - 帮助中给出的synatx是属于select/update/delete语句中table_reference部分的
  - 至于table_factor/join_table是什么意思?
- implicit join是什么?
  - http://www.jooq.org/doc/3.1/manual/sql-building/sql-statements/select-statement/implicit-join/
