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


### 加索引
- 从1400万条数据中检索耗时从4.27s提高到0.01s ![](../../imgs/tunning_add_index_01.png)
