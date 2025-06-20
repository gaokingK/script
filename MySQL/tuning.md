### 大表数据查询，怎么优化
1. 优化表schema、优化SQL、加索引
2. 使用缓存 Redis
3. 主从复制、读写分离
4. 垂直切分
5. 水平切分
### 练习项目和网站
- 练习网站：https://www.db-fiddle.com/f/3JSpBxVgcqL3W2AzfRNCyq/1?ref=hackernoon.com
- 分析：https://mp.weixin.qq.com/s/oPkney3KI0v5jxOVEHTbSQ
### explain
- link：
    - https://dev.mysql.com/doc/refman/5.7/en/explain-output.html#explain-extra-information
    - https://mp.weixin.qq.com/s?__biz=MzA3MTg4NjY4Mw==&mid=2457328508&idx=2&sn=0db2e532d2b2612ba1c4398af17e3d8c&chksm=88a5c948bfd2405e9065b02e8455e6e9603591952480097dea86cdf4a0142ce575fe2487196a&scene=27
    - https://juejin.cn/post/6844903545607553037
- id 序号，序号越大，越先执行;为null表示一个结果集，不需要使用他来查询，常出现在union语句中
- select_type:子查询的查询类型
    - simple：不包含子查询，union语句的
    - primary：包含子查询的最外层的查询
    - subquery：子查询
- type：链接类型
    - ALL：扫描全部的表
    - index：遍历了索引，有时候比扫描全表的效率还低
    - range：索引范围查找
    - ref：使用非唯一索引查找（至少要达到这个）
    - const：使用主键或者唯一索引，且匹配的结果只有一条记录。
- ref：表示使用列或者常量来和key列里面的值进行比较来从表中选取行
- extra：
    - link:https://blog.csdn.net/poxiaonie/article/details/77757471
    - using index 索引覆盖
    - Using filesort 使用文件排序，使用非索引列进行排序时出现，非常消耗性能，尽量优化
- key
    - NULL 
就说明是全表扫描，没有走索引。

### 加索引
- 从1400万条数据中检索耗时从4.27s提高到0.01s ![](../../imgs/tunning_add_index_01.png)

# sql调优
- 不用select * ，减少取出来的数据的大小，需要什么取什么
- 不对数据进行计算，会导致全表扫秒，即使该字段有索引
```sql
select name from user where FROM_UNIXTIME(create_time) < CURDATE();
// 应该修改为
select name from user where create_time < FROM_UNIXTIME(CURDATE());
```

# 如何正确得给线上表加字段
- http://www.jinyazhou.com/16656511239302.html#more
- `ALTER TABLE `user` ADD `age` int NOT NULL DEFAULT '0' COMMENT '年龄';` 执行这条sql的时候，会自动给表加上表锁，而且是写锁 会阻塞后续的所有读写请求，造成非常严重的后果，整个服务都有宕机的风险

# 删除大批量数据有规律时会好一点

### 慢日志
- link: https://blog.csdn.net/weixin_46575363/article/details/119779018
- 记录分析（mysqldumpslow）
  - mysqldumpslow -s t -t 10 -g ‘log’ mysql_slow.log # 显示前10条按耗时排序的记录
  - -s : 按照哪种规则排序
  - -t: 显示前几个记录
    - c: 访问计数
    - l: 锁定时间
    - r: 返回记录
    - t: 查询时间
    - al:平均锁定时间
    - ar:平均返回记录数
    - at:平均查询时间
  - -g : 有点像grep， 后跟正则

### 编写规范
- 尽量保持JOIN子句的简洁，只包含必要的关联条件。
- 使用WHERE子句来过滤记录，这样可以提高查询的灵活性和可读性。
- 考虑性能，确保使用索引优化过滤条件。
```sql
-- sql1
SELECT * FROM ticket
JOIN server_config_release_ticket_data ON server_config_release_ticket_data.ticket_id = ticket.id
JOIN server_config_release_data ON server_config_release_data.ticket_id = ticket.id AND server_config_release_data.is_activate = 1
WHERE ticket.is_deleted = 0
-- sql2
SELECT * FROM ticket
JOIN server_config_release_ticket_data ON server_config_release_ticket_data.ticket_id = ticket.id
JOIN server_config_release_data ON server_config_release_data.ticket_id = ticket.id
WHERE ticket.is_deleted = 0 AND server_config_release_data.is_activate = 1
-- 比较sql2更好
-- SQL2更好，因为它遵循了清晰的逻辑分离原则。将过滤条件放在WHERE子句中，使得查询的意图更加明确，易于理解和维护。
-- 性能：在某些数据库系统中，将过滤条件放在JOIN子句中可能会影响查询性能，因为数据库可能无法在连接过程中有效地使用索引。将过滤条件放在WHERE子句中有助于数据库优化器更好地进行查询优化。
-- 可读性：SQL2的可读性更好，因为它遵循了常见的SQL编写习惯，即先连接表，然后过滤记录。
-- 通用性：SQL2更通用，因为它允许你在不影响连接逻辑的情况下，更容易地添加或修改过滤条件。
-- 注意
-- 有个问题就是前者是只过滤server_config_release_data表中的数据，后者是过滤结果中的数据，如果是左连接的话，那么后者可能不会出现server_config_release_data为空的数据
-- 不过要是这样的话更推荐连接子查询
LEFT OUTER JOIN server_config_release_ticket_data ON server_config_release_ticket_data.ticket_id = ticket.id 
LEFT OUTER JOIN (select * from server_config_release_data where server_config_release_data.is_deleted = 0 AND server_config_release_data.is_activate = 1) as server_config_release_data ON server_config_release_data.ticket_id = ticket.id 
WHERE ticket.is_deleted = 0 AND server_config_release_ticket_data.is_deleted = 0
```



