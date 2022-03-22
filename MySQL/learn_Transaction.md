# link
- [MySQL——事务(Transaction)详解](https://blog.csdn.net/w_linux/article/details/79666086)
- [MYSQL隔离级别 通俗理解 + MYSQL、ORACLE默认事务隔离级别](https://www.cnblogs.com/personsiglewine/p/11507866.html)
- [MySql查询正在进行中的事务](https://blog.csdn.net/ffzhihua/article/details/103703497)
- [MySql查询正在进行中的事务](https://www.cnblogs.com/grey-wolf/p/7479549.html)
# 问题
- InnoDB默认的REPEATABLE-READ并不会在性能上有任何损失。 为什么？
- 回读是什么？
# 事务的一些概念
## 定义
- 事务是一个不可再分的单元；通常和一个完整的业务对应(例如银行账户转账业务，该业务就是一个最小的工作单元)
- 一个完整的业务需要批量的DML(insert、update、delete)语句共同联合完成
    ```
    update t_act set balance=400 where actno=1;
    update t_act set balance=200 where actno=2;

     ```
- 以上两个DML语句必须同时成功或者同时失败。最小单元不可再分，当第一条DML语句执行成功后，并不能将底层数据库中的第一个账户的数据修改，只是将操作记录了一下；这个记录是在内存中完成的；当第二条DML语句执行成功后，和底层数据库文件中的数据完成同步。若第二条DML语句执行失败，则清空所有的历史操作记录，要完成以上的功能必须借助事务
  
## 事务的四大特征（ACID）
- 原子性(atomicity)：事务是最小单位，不可再分
- 一致性(consistency)：执行事务前后，数据保持一致，多个事务对同一个数据读取的结果是相同的；
- 隔离性(isolation)：并发访问数据库时，一个用户的事务不被其他事务所干扰，各并发事务之间数据库是独立的；
- 持久性(durability)：是事务的保证，事务终结的标志(一个事务被提交之后。它对数据库中数据的改变是持久的，即使数据库发生故障也不应该对其有任何影响。)

## 关于事务的关键字
    - begin; commit; rollback; close

## 脏读、不可重复读、幻读
- 脏读：事务A更新（不是提交）的数据被事务B读了，然后事务A又rollback了。（事务B读到的数据就是错误的）
- 不可从复读：事务A两次查询的数据不一样， 因为在两次查询中间事务B更新了A已读的数据
- 幻读：事务A两次查询中查到的数据条数不同（不可重复读是某条数据的内容不同，这个是个数不同）， 第一次读了5条，然后事务B又插入了两条，A第二次读就会读到7条。

## 事务的隔离级别
- 读未提交
- 读已提交：允许读取并发事务已提交的数据
- 可重复读：对同一字段的多次读取结果是一致的，除非是事务本身修改的数据。但不能避免幻读。（可能是只允许读取并发事务新插入的？）
- 可串行化：最高隔离级别，所有事务之间依次逐个执行

- mysql 默认采用的 可从复读 隔离级别；
- 查看隔离级别：
  - `select @@tx_isolation;` # 当前事务
  - `select @@global.tx_isolation;` # 全局
- 设置隔离级别
  - `set [session] transaction isolation level read committed;`# 当前事务
  - `set global transaction isolation level read committed;`# 全局
- 事务隔离机制的实现基于锁机制和并发调度。
  - 其中并发调度使用的是MVVC（多版本并发控制），通过保存修改的旧版本信息来支持并发一致性读和回滚等特性。
  - 事务的隔离级别越低， 事务请求的锁就越少；但InnoDB默认的REPEATABLE-READ并不会在性能上有任何损失
- InnoDB存储引擎在 分布式事务 的情况下一般会用到SERIALIZABLE(可串行化)隔离级别。

## 查询正在进行的事务
- link：
  - https://blog.csdn.net/ffzhihua/article/details/103703497
```
# 查看引擎的相关信息
show engine innodb status;
# 查看锁表
select * from information_schema.innodb_locks;
查看事务相关信息
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX; # 这个只能查询此刻正在进行中的事务，已经完成的是查不到的

# mysql 5.6，查看更具体的信息：
SELECT a.trx_id, a.trx_state, a.trx_started, a.trx_query, b.ID, b.USER, b.DB, b.COMMAND, b.TIME, b.STATE, b.INFO, c.PROCESSLIST_USER, c.PROCESSLIST_HOST, c.PROCESSLIST_DB, d.SQL_TEXT FROM information_schema.INNODB_TRX a LEFT JOIN information_schema.PROCESSLIST b ON a.trx_mysql_thread_id = b.id AND b.COMMAND = 'Sleep' LEFT JOIN PERFORMANCE_SCHEMA.threads c ON b.id = c.PROCESSLIST_ID LEFT JOIN PERFORMANCE_SCHEMA.events_statements_current d ON d.THREAD_ID = c.THREAD_ID;

# 针对mysql 5.5，查看更具体的信息：
SELECT a.trx_id, a.trx_state, a.trx_started, a.trx_query, b.ID, b. USER, b. HOST, b.DB, b.COMMAND, b.TIME, b.STATE, b.INFO FROM information_schema.INNODB_TRX a LEFT JOIN information_schema.PROCESSLIST b ON a.trx_mysql_thread_id = b.id WHERE b.COMMAND = 'Sleep';
```