# 准备和使用
### 产品和版本、存储引擎
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
  - 存储引擎
    - MySQL的存储引擎有MyISAM、InnoDB
    - MyISAM是MySQL的默认数据库引擎（5.5版之前），由早期的ISAM所改良。虽然性能极佳，但却不支持事务处理
    - 
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
### 使用\s
### 寻找帮助
- help contents 按目录查看
  - 全大写的是sql的关键字，小写的是变量名，可以根据情况替换为自己需要的
  - | 代表或
  - [] 中的是可选的，如果有多个的话，一个不要都行
  - {} 中的是必须选择的参数 ADD {INDEX|KEY} 就说明add 后面必选跟INDEX或者KEY
  - () 的意思是被括号包裹的变量在sql中也要被包裹
  - (key_part,...)、(col_name,...)这种的意思就是可以出现多个
 
- help create database;
- Mycli 是一个 MySQL，MariaDB 和 Percona 命令行客户端，具有自动补全、智能补全、别名支持、页面调整和语法高亮功能。
- 帮助网站
	- https://riptutorial.com/sql/example/938/implicit-join
	- http://www.jooq.org/doc/latest/manual/sql-building/sql-statements/select-statement/implicit-join/
  - [ourmysql](http://ourmysql.com/)
  - https://help.gnome.org/users/gda-browser/stable/virtual-connections.html.zh_CN
- 技术网站
  - https://www.modb.pro/  
- mysql数据库在线测试_5个免费在线 SQL 数据库环境
  - https://blog.csdn.net/weixin_32329059/article/details/114864041

### 管理MySQL
- 查看信息：https://www.cnblogs.com/caoshousong/p/10845396.html
  - 查看当前连接数 show status like  'Threads%';
  Threads_connected ：这个数值指的是打开的连接数.
  Threads_running ：这个数值指的是激活的连接数，这个数值一般远低于connected数值.
  Threads_connected 跟show processlist结果相同，表示当前连接数。准确的来说，Threads_running是代表当前并发数
  - show processlist如果是root帐号，你能看到所有用户的当前连接。如果是其它普通帐号，只能看到自己占用的连接。
    - 等价与`select * from information_schema.processlist` 
  - `\s` 并不是一个独立的 SQL 命令，而是 MySQL 命令行客户端的一个特殊命令，用于显示当前会话（session）的状态信息。
- 允许通过远程链接
  - link: https://blog.csdn.net/weixin_52988911/article/details/120100574
  - 允许用户myuser从ip为192.168.1.6的主机连接到mysql服务器,使用mypassword作为密码`GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'192.168.0.1' IDENTIFIED BY'mypassword' WITH GRANT OPTION;`
- link: https://www.runoob.com/mysql/mysql-administration.html
- show variables like "datadir"; # 数据库存放路径
- 对数据库
  - show databases;
    - information_schema/mysql以及 performance_schema是系统数据库
  - use database_name;
  - create database database_name;
  - drop database database_name;
- 对表
- select * from information_schema.tables where table_name=tbl_name 查看该表的一些信息
- show tables; 使用该命令前需要使用 use 命令来选择要操作的数据库。
- show [FULL] COLUMNS FROM 数据表:显示数据表的属性
- show INDEX FROM 数据表: 显示数据表的详细索引信息，包括PRIMARY KEY（主键）。
- SHOW TABLE STATUS [FROM db_name] [LIKE 'pattern'] \G: 
  - 命令各项的意思可以 help show table status
    - update_time InnoDBy 引擎是Null, InnoDB 在其系统表空间中存储多个表，数据文件时间戳不适用, 
    - Update_time displays a timestamp value for the last UPDATE, INSERT, or DELETE performed on InnoDB tables that are not partitioned? 
  - 该命令将输出Mysql数据库管理系统的性能及统计信息。
  - \G;   # 加上 \G，查询结果按列打印
  ```s
  mysql> SHOW TABLE STATUS FROM RUNOOB;   # 显示数据库 RUNOOB 中所有表的信息
  mysql> SHOW TABLE STATUS from RUNOOB LIKE 'runoob%';     # 表名以runoob开头的表的信息
  mysql> SHOW TABLE STATUS from RUNOOB LIKE 'runoob%'\G;   # 加上 \G，查询结果按列打印
  ```
- 获取表的主键信息
  `SELECT TABLE_NAME,COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAMe="Person";`
  - link:https://www.cnblogs.com/zouhao/p/6651995.html
- autocommit 自动提交
  - link: https://blog.csdn.net/wx145/article/details/82740737
  - 查看autocommit
    - 查看当前会话：`show variables like 'autocommit';` 或 'select @@autocommit;'
    - 查看全局：'select @@global.autocommit;'
  - 设置 autocommit
    - 设置当前会话 `set [session] autocommit=0`
    - 设置全局 `set global autocommit=0`
  - 当autocommit为ON的情况下，并且又手动开启了事务，那么mysql会把start transaction 与 commit之间的语句当做一次事务来处理，默认并不会帮用户提交需要手动提交，如果用户不提交便退出了，那么事务将回滚。

# 表 
- ## 查看表信息
  - [descript|desc] tbl_name
  - SHOW [FULL] COLUMNS FROM tbl_name [FROM db_name] [like_or_where] 等价于`desc tbl_name`# 查看columns status
    - link:https://dev.mysql.com/doc/refman/8.0/en/show-columns.html
    - 关于Key值：
      - empty：没有索引，或者作为覆盖索引或者非唯一索引的第二列
      - PRI：主键索引或者属于多列主键索引
      - UNI：唯一索引的第一列
      - MUL：非唯一索引的第一列（允许出现重复值）
      - 如果一个列属于多个索引，按照PRI, UNI, MUL的优先级显示
 
- ## 创建表 # create help create table;
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
- 将查询结果导入到表中(表存在且表结构相同)`INSERT INTO table2 SELECT * FROM table1 WHERE condition;`
- 将查询结果导入到表中(表不存在) `CREATE TABLE school SELECT * FROM class`
- ## 重新创建表`create table tbl_name like tbl_name;`
- ## 修改表 help alter table;
```cs
# 修改列属性使用modify
alter table Person modify Id int not null auto_increment unique key comment 'id号'; 数据类型需要重新声明? 原本为空的设置为非空后会自动赋值
# 修改列名 怎么只修改列名,而不传入属性-------------no
alter table tbl_name change old_name new_name 随便一个属性;

# 自增, 自增属性必须为key, 且一个表中自增只有一个;
# 删除自增属性, 其他的属性会消失吗?
alter table Profession modify id int(11), drop primary key;
# 对表重命名
ALTER  TABLE table_name RENAME TO new_table_name
```
- ## 新建列的时候添加外键`alter table task add video_id int(11) after video_duration ,add constraint video_id foreign key (video_id) references video(id) on delete cascade on update no action;`

- ## 删除表`drop table tbl_name`
# 共识
- col_name (column name); tbl_name(table_name)\

# 其他
### 约束
- link：https://blog.csdn.net/qq_34306360/article/details/79717682
- 添加约束: `alter table task add video_id int(11) after video_duration ,add constraint video_id foreign key (video_id) references video(id) on delete cascade on update no action;`
- 可以修改 task ，但改动前、改动后的video_id都要在video存在
- 可以修改video, 但不能修改id列的值
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
  - 据类型最多可存储 38 个数字，所有数字都能够放到小数点的右边。
  - decimal(10, 4) 一共能存10位数字，小数部分最多有4位。（多的化会四舍五入后把多出来的扔掉）
  - 定义了zerofill后，插入负数会报错
- datetime
  - 不能为空
    ``` 
    mysql> update autotest set kass_pro_date="" where id =3;
    ERROR 1292 (22007): Incorrect datetime value: '' for column 'kass_pro_date' at row 1
    ```
- varchar(128)可以存多少汉字
  - 4.0版本以下，varchar(50)，指的是50字节，如果存放UTF8汉字时，只能存16个（每个汉字3字节） 
  - 5.0版本以上，varchar(50)，指的是50字符，无论存放的是数字、字母还是UTF8汉字（每个汉字3字节），都可以存放50个

- TEXT 长文本字段，能存储64kb
- blob 长文本字段， 保存的是二进制，可以用来存储图片

# 主键
- 主键是唯一的索引
  - 
- 复合主键(联合主键) 和唯一键
  - link
    - https://www.cnblogs.com/binjoy/articles/2638708.html
  - 复合主键
    - 两者是一个东西,不同叫法
    - 一个表只允许有一个主键,但一个主键可以允许由多个字段构成,这时称为复合主键
    - 使用方式`help constraint`
      ```
      CREATE TABLE product (category INT NOT NULL, id INT NOT NULL, price DECIMAL,
                            PRIMARY KEY(category, id)) ENGINE=INNODB;
      ```
    - 为什么需要复合主键
      - 为什么ID可以作为主键, 还需要复合主键呢, 因为有的表可能没有ID, 一个学生表，没有唯一能标识学生的ID，怎么办呢，学生的名字、年龄、班级都可能重复，无法使用单个字段来唯一标识
      - 这时，我们可以将多个字段设置为主键,由这多个字段联合标识唯一性，其中，某几个主键字段值出现重复是没有问题的，只要不是有多条记录的所有主键值完全一样，就不算重复。
  - 唯一键
    - 限制字段的记录不重复的, 比如docker表要把`ip, port, delete_time` `name, delete_time`做成两个唯一键
# 外键
- 新增外键
```
alter table issue_record add column uid int after id; # 新增列
alter table issue_record add constraint fk_issue_user foreign key (uid) references user(id); # 添加约束
```
# 索引
- 主键和唯一索引的区别
  - link
    - https://blog.csdn.net/weixin_38750084/article/details/84885565
    - https://www.cnblogs.com/-619569179/p/6528896.html
  - 主键是一种约束，唯一索引是一种索引，两者在本质上是不同的。
  - 主键不允许空值，唯一索引允许空值
  - 主键只允许一个，唯一索引允许多个
  - 主键产生唯一的聚集索引，唯一索引产生唯一的非聚集索引
- 索引的特点
  - 索引可以提高查询的速度。
# 问题
- 外键一定要是主键吗？
- SQL 中怎么会用到索引？

```
- create database test-test;
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
  - https://www.cybertec-postgresql.com/en/postgressql-implicit-vs-explicit-joins/#:~:text=An%20implicit%20join%20is%20the%20simplest%20way%20to,commo%20n%20way%20to%20connect%20two%20tab%20les.        --------no
  - 隐式join就是不包含join关键字, 表与表之间使用逗号分割, 在where中定义之间的关系, 可以在form后跟多个表
  - 不建议使用的原因:
    - 可能会导致cross join, 意外的得到不正确的结果, 尤其是当在查询中有很多链接的时候
    - 如果你故意使用隐私链接来完成全连接, 这不是一个清晰的句法(井盖使用Cross join去替代), 也不利于别人维护
  - 好处
  ```
  select a.name, b.name from Person a, Profession b where a.id=b.id;
  ```