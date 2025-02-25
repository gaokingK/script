## 一些排错sql
```sql
-- 查看引擎状态
show engine innodb status \G;  -- mysql命令行中
show engine innodb status; --dbeaver中
-- 1. 终止某个进程
kill 1548965;

-- 1. 查看正在执行的sql进程 id列是thread_id 
-- 命令输出解析：https://blog.csdn.net/p656456564545/article/details/53169565
show processlist;
select * from performance_schema.processlist where DB = "vt_db"; -- 可用这个代替

-- 2.查看事务
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX;
-- 3. 查看锁 <8.0用上面
select * from information_schema.innodb_locks;
select * from performance_schema.data_locks;
-- 4. 查看锁等待 <8.0用上面
SELECT * FROM INFORMATION_SCHEMA.INNODB_LOCK_WAITS; 
select * from performance_schema.data_lock_waits;

-- 5.查看当前有那些表是打开的
show open tables from vt_db;

-- 6. 检查是否有其他事务锁定表：
SELECT * FROM performance_schema.data_locks;

-- 7.检查当前用户是否有 ALTER 权限
SHOW GRANTS;

-- 检查锁定情况：
SHOW OPEN TABLES WHERE In_use > 0;
-- 检查表状态：
SHOW TABLE STATUS LIKE 'acl_rule';
```

### ERROR 1418 (HY000):
- link: https://blog.csdn.net/weixin_42613018/article/details/113274821
- 解决方法是在客户端上执行SET GLOBAL log_bin_trust_function_creators = 1;

### ERROR 执行修改表字段属性sql会一直执行中，不结束
- alter table acl_rule modify source_port varchar(512) not null comment '源cidr port',  modify dest_port varchar(512) not null comment '目标cidr port';
- 执行完上面数据后会一直不结束，并且表中其他查询会一直阻塞
- 解决办法
```sql
-- 查看事务
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX;
-- kill 其中的 trx_mysql_thread_id
```
