- 从磁盘取数据是最影响性能的
- 一般的应用系统，读写比例在10:1左右，而且插入操作和一般的更新操作很少出现性能问题，在生产环境中，我们遇到最多的，也是最容易出问题的，还是一些复杂的查询操作，因此对查询语句的优化显然是重中之重

### 细微的
- 从磁盘取数据是最影响性能的
- 一般的应用系统，读写比例在10:1左右，而且插入操作和一般的更新操作很少出现性能问题，在生产环境中，我们遇到最多的，也是最容易出问题的，还是一些复杂的查询操作，因此对查询语句的优化显然是重中之重
### MySQL的@与@@区别
  - link： https://www.cnblogs.com/qlqwjy/p/8470722.html
  - @x 是 用户自定义的变量  (User variables are written as @var_name)
  - @@x 是 global或session变量  (@@global  @@session )
  - 查看全局变量: `select @@var_name`
  - 设置全局变量值:
      `mysql> SET @t1=0, @t2=0, @t3=0;`
      `mysql> SELECT @t1:=(@t2:=1)+@t3:=4,@t1,@t2,@t3;`

- 查询的时候设置临时变量 tmp
  - `mysql> SELECT @t1:=(@t2:=1)+@t3:=4,@t1,@t2,@t3;`# t2=1, t3=4, t1=t3+t4; 查询t1、t2、t3
### schema、catalog分别指的是什么？
- 在关系型数据库中，分三级：database.schema.table 即一个数据库下面可以包含多个schema，一个schema下可以包含多个数据库对象，比如表、存储过程、触发器等。但并非所有数据库都实现了schema这一层，比如mysql直接把schema和database等效了，PostgreSQL、Oracle、SQL server等的schema也含义不太相同。
- 关系型数据库中没有catalog的概念。但在一些其它地方（特别是大数据领域的一些组件）有catalog的概念，也是用来做层级划分的，一般是这样的层级关系：catalog.database.table。
### delimiter 语句
- link：https://blog.csdn.net/muyangjun/article/details/123548056
- `delimiter //`主要作用就是把语句界定符由默认值`；`变为 `//`, 这样就能使程序体中的；界定符被传到服务器解释而不是mysql客户端
### 每张表大约要存多少条数据
- link：https://juejin.cn/post/7165689453124517896
- 很多人都说单张表的数据行最好不要超过2000万或者2GB，但其实2000万这个数据并不固定，盲目的以这个数字为标准，可能导致系统性能的大幅下降.实际情况下由于每张表的字段数量不同，字段所占的空间不同等原因，他们在最佳性能下可以存放的数据量也就不同.
- 当B+树的层数保持在4层以下时，会有不错的性能。那么上面说的大约能存放多少数据就可以根据页格式信息和索引字段长度计算出叶子节点的数量，再根据每条数据的大小计算出每个叶子节点里能存放多少条数据。把结果相乘就得出来了。
- 页大小默认为16KB时，每个页大约有15KB的空间可用，可以存储1000个int值，那么就有1000*1000个叶子节点 每条数据长度为7KB的情况下，每个叶子节点里有两条数据，这样大约就是1000*1000*2=200万条数据。
### Mysql海量数据表的快速生成（1000万条记录）
- link：https://blog.csdn.net/qq_40530040/article/details/107623254
```
CREATE TABLE dept( /*部门表*/
deptno MEDIUMINT   UNSIGNED  NOT NULL  DEFAULT 0,
dname VARCHAR(20)  NOT NULL  DEFAULT "",
loc VARCHAR(13) NOT NULL DEFAULT ""
) ;
#创建表EMP雇员
CREATE TABLE emp
(empno  MEDIUMINT UNSIGNED  NOT NULL  DEFAULT 0, /*编号*/
ename VARCHAR(20) NOT NULL DEFAULT "", /*名字*/
job VARCHAR(9) NOT NULL DEFAULT "",/*工作*/
mgr MEDIUMINT UNSIGNED NOT NULL DEFAULT 0,/*上级编号*/
hiredate DATE NOT NULL,/*入职时间*/
sal DECIMAL(7,2)  NOT NULL,/*薪水*/
comm DECIMAL(7,2) NOT NULL,/*红利*/
deptno MEDIUMINT UNSIGNED NOT NULL DEFAULT 0 /*部门编号*/
) ;
#工资级别表
CREATE TABLE salgrade
(
grade MEDIUMINT UNSIGNED NOT NULL DEFAULT 0,
losal DECIMAL(17,2)  NOT NULL,
hisal DECIMAL(17,2)  NOT NULL
);
#测试数据
INSERT INTO salgrade VALUES (1,700,1200);
INSERT INTO salgrade VALUES (2,1201,1400);
INSERT INTO salgrade VALUES (3,1401,2000);
INSERT INTO salgrade VALUES (4,2001,3000);
INSERT INTO salgrade VALUES (5,3001,9999);

#创建一个函数，名字 rand_string，可以随机返回我指定的个数字符串
delimiter $$ 
create function rand_string(n INT)
returns varchar(255) #该函数会返回一个字符串
begin
#定义了一个变量 chars_str， 类型  varchar(100)
#默认给 chars_str 初始值   'abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'
 declare chars_str varchar(100) default 'abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ'; 
 declare return_str varchar(255) default '';
 declare i int default 0; 
 while i < n 
 do
    # concat 函数 : 连接函数mysql函数
   set return_str =concat(return_str,substring(chars_str,floor(1+rand()*52),1));
   set i = i + 1;
   end while;
  return return_str;
  end $$

#这里我们又自定了一个函数,返回一个随机的部门号
create function rand_num( )
returns int(5)
begin
declare i int default 0;
set i = floor(10+rand()*500);
return i;
end $$

#创建一个存储过程， 可以添加雇员
create procedure insert_emp(in start int(10),in max_num int(10))
begin
declare i int default 0;
#set autocommit =0 把autocommit设置成0
 #autocommit = 0 含义: 不要自动提交
 set autocommit = 0; #默认不提交sql语句
 repeat
 set i = i + 1;
 #通过前面写的函数随机产生字符串和部门编号，然后加入到emp表
 insert into emp values ((start+i) ,rand_string(6),'SALESMAN',0001,curdate(),2000,400,rand_num());
  until i = max_num
 end repeat;
 #commit整体提交所有sql语句，提高效率
   commit;
 end $$

 # 执行 call insert_emp(100001,8000000)$$ (9 min 54.45 sec)
```
### SQL的生命周期？
- 应用服务器和数据库服务器建立连接
- 服务器进程拿到请求sql
- 解析并生成执行计划、执行
- 把数据读取到内存中进行逻辑处理
- 关闭步骤一中的连接，然后把数据发送到客户端
- 关闭连接，释放资源
### 对索引的理解
- learn_index 什么是索引
### 
