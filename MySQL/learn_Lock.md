# MySQL锁 中各种锁的表现
# 问题
- 为什么排他锁造成的锁表按照死锁 section提供的办法查不到
# 总结：
- 在MySQL中，使用锁机制和并发调度来实现，来实现绝对的事务隔离机制。锁分为悲观锁和乐观锁；悲观锁的实现方式有两种，在MySQL中，常使用第二种方法；而乐观锁分为共享锁和排他锁，这两种锁MySQL都有相应的实现。也只有借助底层来实现才能保证数据访问时的排他性。除此之外，行锁和表锁是共享锁和排他锁在使用时根据是否会在SQL中使用索引的不同而产生的不同粒度。
## 乐观锁
- 乐观锁假设数据一般情况不会造成冲突，所以在数据进行提交更新的时候，才会正式对数据的冲突与否进行检测，如果冲突，则返回给用户异常信息，让用户决定如何去做。
- 乐观锁适用于读多写少的场景，这样可以提高程序的吞吐量。
### 乐观锁的实现
- 版本号控制 实现(可以解决ABA问题) 最常见的实现方式
  - 一般是在数据表中加上一个数据版本号 version 字段，表示数据被修改的次数。当数据被修改时，version 值会 +1。当线程 A 要更新数据时，在读取数据的同时也会读取 version 值，在提交更新时，若刚才读取到的 version 值与当前数据库中的 version 值相等时才更新，否则重试更新操作，直到更新成功。

## 悲观锁(Pessimistic Concurrency Control)
- 之所以叫做悲观锁，是因为这是一种对数据的修改持有悲观态度的并发控制方式。总是假设最坏的情况，每次读取数据的时候都默认其他线程会更改数据。
- 进行每次操作时都要通过获取锁才能进行对相同数据的操作，这点跟java中synchronized很 相似，共享锁（读锁）和排它锁（写锁）是悲观锁的不同的实现
### 悲观锁的实现
- 悲观锁主要实现分为共享锁和排他锁：两种数据库都实现了
## 共享锁【shared locks】
- 又称为读锁，简称 S 锁。顾名思义，所有的事务只能对其进行读操作不能写操作，加上共享锁后，其他事务只能再加共享锁。
#### 使用共享锁
```
# 关闭autocommit
set autocommit=0
# 打开第一个查询窗口A
begin;/begin work;/start transaction;(三者选一就可以)
SELECT * from TABLE where id = 1 lock in share mode;
# 第二个个查询窗口B中，对id为1的数据进行更新
updateTABLE set name="www.souyunku.com" where id =1;
# 如果A 一直不commit，B操作界面进入了卡顿状态，过了超时间，提示错误信息
# 如果A在超时前，执行commit，B更新语句就会成功。
# B加上共享锁后，也提示错误信息
[Err] 1064 - You have an error in your SQL syntax; check the manual thatcorresponds to your MySQL server version for the right syntax to use near 'lockin share mode' at line 1
```
- 在查询语句后面增加LOCK IN SHARE MODE，Mysql会对查询结果中的每行都加共享锁，当没有其他线程对查询结果集中的任何一行使用排他锁时，可以成功申请共享锁，否则会被阻塞。其他线程(不加排他锁）也可以读取使用了共享锁的表，而且这些线程读取的是同一个版本的数据。
- 加上共享锁后，对于update,insert,delete语句会自动加排它锁。
- 读取为什么要加读锁呢：防止数据在被读取的时候被别的线程加上写锁
## 排他锁【exclusive locks】
- 又称为写锁，简称 X 锁。若事务1对数据对象A加上X锁，事务1可以读A也可以修改A，其他事务不能再对A加任何锁，直到事物1释放A上的锁。这保证了其他事务在事物1释放A上的锁之前不能再读取和修改A。排它锁会阻塞所有的排它锁和共享锁
#### 使用排他锁
```
select * from tbl_name where condition for update
```
在需要执行的语句后面加上for update就可以了;
- 加上排他锁后，别人不能读了？别人能读，但不能加锁读
  
## 行锁
- 给某一行加上锁，也就是一条记录加上锁。行级锁都是基于索引的，如果一条SQL语句用不到索引是不会使用行级锁的，会使用表级锁。
- 行锁也分为排他锁和共享锁（前面的例子中就是行锁的排他锁和共享锁）
- 前面的例子中，使用到了id， id已经设置了主键。就也相当于索引。执行加锁时，会将id这个索引为1的记录加上锁，那么这个锁就是行锁。
- 如果用到了索引，也用到了没有索引的字段，那么会锁表还是锁行呢？-------------no
```
# tbl_a 没有主键
# 窗口A中 （autocommit已经关闭）
select * from tbl_a where id=1 lock in share mode;
# 窗口B（autocommit=1）
update test set value=2 where id=2; # 会等待，说明表已经被锁了

# tbl_a id 为key
# 窗口A中 
select * from tbl_a where id=1 lock in share mode;
# 窗口B（autocommit=1）
update test set value=2 where id=2; # 完成
update test set value=2 where id=1; # wait 锁行了

# tbl_a id 为key
# 窗口A中 
select * from tbl_a where value=1 lock in share mode; # 查询到的是id=1 # select id where value=1也会锁表
# 窗口B（autocommit=1）
update test set value=2 where id=2; # wait 锁表了
```
- 行级锁的缺点是需要请求大量的锁资源，速度慢，内存消耗大。

## 表锁  
- Innodb引擎即支持行锁，也支持表锁，他们都由sql的 查询语句触发，区别是通过索引检索数据，InnoDB才使用行级锁，否则就使用表锁
- 行级锁都是基于索引的，如果一条SQL语句用不到索引是不会使用行级锁的，会使用表级锁。
- 要特别注意InnoDB行锁的这一特性，不然的话，可能导致大量的锁冲突，从而影响并发性能。

## 死锁
- 所谓的死锁是在两个或多个进程在执行过程中，因为争夺资源而造成互相等待的一种现象。如果没有外力作用，将一直互相等待下去。
- 死锁会造成系统开销，事务由于死锁回滚会取消事务执行的所有工作。
### MySQL中解除死锁的两种办法
- link: https://www.cnblogs.com/jpfss/p/9203679.html
# 第一种
```
# 查询是否锁表
show open tables where in_use > 0; 
# show open tables from database_name; https://www.cnblogs.com/jpfss/p/9203679.html
# 2.查询进程（如果您有SUPER权限，您可以看到所有线程。否则，您只能看到您自己的线程）
show processlist; # info里是sql命令
# 杀死进程id（就是上面命令的id列）
kill id
```
# 第二种
```
# 查看当前的事务
select * from infomation_schema.innodb_trx;
# 查看当前锁定的事务 为什么关闭autocommit后当前事务查不到？
SELECT * FROM INFORMATION_SCHEMA.INNODB_LOCKS;
# 查看当前等锁的事务 # 在另一个窗口打开，进行sql， 这个窗口查询。
select * from information_schema.innodb_lock_waits;
kill id
```
- 如果系统资源充足，进程的资源请求都能够得到满足，死锁出现的可能性就很低，否则就会因争夺有限的资源而陷入死锁。其次，进程运行推进顺序与速度不同，也可能产生死锁。
### 死锁产生的4个条件
  - 互斥条件： 一个资源一次只能被一个进程使用
  - 请求与保持条件： 一个进程因等待资源而阻塞时， 对已获得的资源不释放
  - 不剥夺条件： 一个进程已获得的资源，只能自己释放，别人不能剥夺
  - 循环等待条件：若干个进程形成首位相接的等待资源状态。
- 死锁不能完全避免，但可以是死锁的数量降至最低。这样可以增加事务的吞吐量并减少系统开销
### 降低死锁的办法
  - 按同一顺序访问资源
  - 避免事务中的用户交互
  - 保持事务简短并在一个批处理中（一个程序中？）
  - 使用低隔离级别
  - 使用绑定链接

### 绑定链接
- link：
  - https://bbs.csdn.net/topics/50417887
  - https://help.gnome.org/users/gda-browser/stable/virtual-connections.html.zh_CN
- 连接绑定功能是一个可以 "联合" 几个连接 并/或输入数据集到一个单一连接，与使用普通连接几乎一样
- 示例
```
# 准备
create table tb(id int);
# 开始对比
# 不使用绑定连接的测试
# (a窗口)
begin tran;
insert tb values(100);
# (b window)
begin tran;
update tb set a=50; # 此时的执行结果是产生的阻塞,b窗口的处理要等a窗口的处理完成后才能进行下一步

# 使用绑定连接的测试
# (a窗口)
declare @bind_token varchar(255); # 声明一个临时变量
begin tran;
execute sp_getbindtoken @bind_token output;
print @bind_token #记下这个结果,后面要用到
insert tb values(100)
# 开始一个新窗口(b窗口),写上如下代码并执行(不会产生阻塞)
begin tran
update tb set a=50
rollback tran
# 回a窗口执行
select * from tb # 此会话中的活动事务已由另外一个会话提交或终止。
```


- 采用的保守策略，为数据处理的安全提供了保证。但是在效率方面，处理加锁的机制会让数据库产生额外的开销，还有增加产生死锁的机会。
- 另外还会降低并行性，一个事务如果锁定了某行数据，其他事务就必须等待该事务处理完才可以处理那行数据。
- 悲观锁的实现
  - 需要借助数据库的锁机制
  - 在修改前就尝试去对该记录加上排他锁, 如果加锁失败, 具体响应需要开发者根据实际情况决定是等待还是抛出异常
- 悲观锁的应用
  - SQL中使用悲观锁

- 乐观锁和悲观锁的选择
  - 响应效率: 乐观锁的响应速度高, 且未加锁,效率高
  - 冲突频率: 冲突频率高适合用悲观锁, 因为乐观锁需要多次重试才能成功,代价大
  - 重试代价: 重试代价大的话选择悲观锁,其失败的概率低
  - 乐观锁如果有人在你之前更新了，你的更新应当是被拒绝的，可以让用户从新操作。悲观锁则会等待前一个更新完成。这也是区别
  - 随着三高(高并发, 高可用, 高性能)提出, 悲观锁已经越来越少的应用到生产中了, 特别是并发量大的场景中
### 调度
- CFS 绝对公平算法
### 问题
- 悲观锁,乐观锁会产生死锁吗?
- CAS 在某些情况下能保证原子性吗?
  - A检查完后准备修改,但此刻B把数据改了
  - 比较并交换这个操作, 不是原子性, 即使是底层代码(汇编)也不是(因为可能被其他cpu给打断)
- 语言提供的锁操作是依赖操作系统提供的,操作系统依赖汇编, 汇编有许多种方式, 可以锁缓存, 锁总线(硬件方面, 拉高北桥电平信号)
- 高并发环境下锁粒度把控是一门重要的学问。选择一个好的锁，在保证数据安全的情况下，可以大大提升吞吐率，进而提升性能。
