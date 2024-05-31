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
- 事务分为显示事务和隐式事务，显示事务是由关键字声明的事务
## 隐式事务
- 当我们使用alter user、create  user、drop user、grant、rename user、revoke、set password等语句时也会隐式提交前面语句所属的事务。
- 事务控制或关于锁定的语句
- 当我们在一个事务还没提交或回滚时就又使用start transaction或begin语句开启一个事务，会隐式提交上一个事务。
- 当前的autocommit如果为off，此时如果我们手动将其修改为on也会隐式提交前面语句所在的事务。
- 使用lock tables、unlock  tables等关于锁定的语句也会隐式提交前边语句所属事务。
- 加载数据的语句 使用load data语句来批量往数据库中导入数据时也会隐式提交前边的事务。
- 关于mysql复制的一些语句 使用start  slave、stop slave、reset slave、change master to等语句时。
- 其他一些语句 使用 analyze table, cache index , check table , flush , load index into cache , optimize table , repair table , reset等语句也会隐式提交事务。
## 事务的四大特征（ACID）
- 原子性(atomicity)：事务是最小单位，不可再分
- 一致性(consistency)：执行事务前后，数据保持一致，多个事务对同一个数据读取的结果是相同的；
- 隔离性(isolation)：并发访问数据库时，一个用户的事务不被其他事务所干扰，各并发事务之间数据库是独立的；
- 持久性(durability)：是事务的保证，事务终结的标志(一个事务被提交之后。它对数据库中数据的改变是持久的，即使数据库发生故障也不应该对其有任何影响。)

## 关于事务的关键字
- START TRANSACTION 或 BEGIN 开始一个新事务。begin和start trancation的区别是后者后面可以跟修饰符
    - read only，表示当前事务是一个只读事务，也就是属于该事物的数据库操作只能读取数据而不能修改数据。
    - 补充：只读事务中只是不允许修改那些其他事务也能访问到的数据表中的数据，而对于临时表来说（我们使用create temporary table创建的表），由于他们只能在当前会话中可见，所以只读事务是可以对临时表进行增删改操作的。
    - read write，表示当前事务是一个读写事务，也就是属于该事物的数据库操作既可以读取数据，也可以修改数据。（读写和只读只能出现一个）
    - with consistent snapshot ，启动一致性读。
    - 默认是读写模式

- COMMIT 提交当前事务，使得所有自上一个COMMIT或START TRANSACTION语句以来进行的修改成为持久的。
- ROLLBACK 回滚当前事务，撤销自上一个BEGIN或START TRANSACTION以来所有的修改。
- 对于不支持事务的存储引擎（如MyISAM），START TRANSACTION、COMMIT和ROLLBACK语句被数据库接受（为了兼容性），但它们并不会执行任何操作
- 事务中如果同时出现COMMIT和ROLLBACK，实际执行的将是这两个命令中先到达的一个


### 如果事务中不写commit和rollback，事务会提交吗
- 在大多数数据库系统中，如果在事务中没有明确执行COMMIT或ROLLBACK指令，那么事务不会自动提交。当对话结束或连接关闭时，大多数数据库系统会自动执行ROLLBACK操作，以撤销在事务中执行的所有操作，确保数据的一致性不受到未完成事务的影响。
### autocommit
- MySQL中有一个叫做autocommit的模式。当autocommit模式被设置为true（这是默认设置）时，每个单独的SQL语句会被视为一个事务并在执行完成后立刻自动提交。这意味着，你可能不需要明确写COMMIT语句就完成了数据提交。
- 如果你开始了事务（即使用了START TRANSACTION或BEGIN），那么autocommit模式会被临时关闭，直到你明确调用COMMIT或ROLLBACK指令,如果你没有调用COMMIT或ROLLBACK而直接结束对话或关闭连接，那么数据库系统通常会回滚那个事务中的所有操作。
- 在关闭autocommit模式后，你需要显式使用COMMIT命令来提交你的事务。如果只是执行了SQL操作后没有提交，那么执行的操作只会在数据库连接的会话内有效，一旦会话结束或连接被关闭，所有未提交的操作都会被撤销。
### 如果事务中开启autocommit会怎么样
- 在事务中开启autocommit会导致一些可能与你预期不同的行为。这是因为autocommit模式的行为和显式事务（即通过START TRANSACTION或BEGIN命令启动的事务）的行为是相对的。
- 当你使用START TRANSACTION或BEGIN命令开始一个事务时，无论autocommit设置为什么值，MySQL都会将其视为一个显式事务，autocommit模式会暂时被忽略，直到事务结束（通过COMMIT或ROLLBACK）。在这个事务中，所做的修改不会被自动提交，而是等待你显式执行COMMIT或ROLLBACK。
- 如果你在事务中试图通过SET autocommit = 1;来开启autocommit模式，该设置对当前事务没有影响，当前事务仍需显式提交。但是，一旦当前事务通过COMMIT或ROLLBACK结束，后续的单独SQL指令将会立即自动提交。
- 对于简单的单一操作或不需要事务保证的场景，让autocommit保持开启（默认设置）是合适的，因为它简化了操作

### 标准SQL并不支持在事务中直接使用IF语句这样的流程控制结构。
如果需要，将这些逻辑放入到存储过程中，例如：
```sql
DELIMITER //

CREATE PROCEDURE example_procedure()
BEGIN
    START TRANSACTION;
    
    UPDATE tbl_name1 SET col_1 = value;

    IF 3 > 2 THEN
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END //

DELIMITER ;
# 然后调用这个存储过程：CALL example_procedure();
```
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
  - 设置完成后，所有新建的会话将使用这个隔离级别，但这不会影响已经存在的会话
  - 改变事务的隔离级别应谨慎进行，因为不同的隔离级别会直接影响数据库的并发性能和数据一致性。
  - 一般情况下，应用程序开发过程并不常改动数据库的隔离级别，而是选择符合其业务需要的默认隔离级别。
  - 选择合适的隔离级别可以在保证数据一致性和提高并发性能间找到一个平衡点
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
