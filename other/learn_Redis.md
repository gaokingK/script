## 帮助
- [中文翻译](http://doc.redisfans.com/index.html)
- [redis-py-cluster](https://redis-py-cluster.readthedocs.io/en/2.1.0/) python操作redis cluster
## 概念
- 6.0以后可以通过更改设置文件支持多线程
- 每秒8万
## 名词
- EYS
- SMEMBERS
- full iteration ：以 0 作为游标开始一次新的迭代， 一直调用 SCAN 命令， 直到命令返回游标 0 ， 我们称这个过程为一次完整遍历。
- ex px 与 nx xx 改动set命令的行为
  - EX second ：设置键的过期时间为 second 秒。 SET key value EX second 效果等同于 SETEX key second value 。
  - PX millisecond ：设置键的过期时间为 millisecond 毫秒。 SET key value PX millisecond 效果等同于 PSETEX key millisecond value 。
  - NX ：只在键不存在时，才对键进行设置操作。 SET key value NX 效果等同于 SETNX key value 。
  - XX ：只在键已经存在时，才对键进行设置操作。
## 问题
- scan 命令中的count参数限定的是服务器单次遍历的字典槽位数量(约等于), 那么这个槽的数据是什么呢?
    这个槽是不是Redis集群中的slot? 不是, 因为如果上面说的“字典槽”的数量是集群中的slot，又知道集群中的slot数量是16384，那么遍历16384个槽之后，必然能遍历出来所有的key信息; 
    但正如图所示![查询图](https://img2018.cnblogs.com/blog/380271/201905/380271-20190531145102592-604451924.png)
    当遍历的字典槽的数量20000的时候，游标依旧没有走完遍历结果，因此这个字典槽并不等于集群中的slot的概念。

- redis 怎么持久化
- 数据库是怎么建立?
- 如何查询某种数据类型的所有值?
- 如何查询快要过期的key?
- 多客户端对Redis的连接并不存在竞争关系?

## [数据类型](https://www.runoob.com/redis/redis-data-types.html)
- string 指的是单个单个的键值对 `set get del`
- hash 是键值对的集合 `hmset hash_name key1 value1 ...` `hget`
- list 列表 只有一个值是字符串的集合
- set 集合 和列表差不多，但是值是唯一的
- zset 有序集合 根据权值排序

### 对键的命令
- 上面的数据类型的是键 值 的形式，只不过值的类型不同
- EXISTS key 检查给定 key 是否存在。
- type key 查看key的类型，然后使用对应的命令查看值

### string
- link
  - https://blog.csdn.net/qq_40399646/article/details/108906116#t21
- API
  - get key_name
    - 返回 key 的值，如果 key 不存在时，返回 nil。 如果 key 不是字符串类型，那么返回一个错误。
  - setnx(Set if No eXist)
    - setnx key_name value :成功返回1, 失败返回0
  - setex key_name timeout value
    - 为指定的key设置值(会覆盖), 并设置过期时间, 设置成功返回OK
  - getrange key_name start end
    - 切割指定key中字符串[start, end]
  - mset/msetnx key1 value1 [key2 value2...]
    - Msetnx 命令用于所有给定 key 都不存在时，同时设置一个或多个 key-value 对(原子操作)
  - setbit key_name offset
    - 对 key 所储存的字符串值，设置或清除指定偏移量上的位(bit)
  - getbit key_name offset
    - 对 key 所储存的字符串值，获取指定偏移量上的位(bit)
    - 字符串值指定偏移量上的位(bit，0 或 1 )。当偏移量 OFFSET 比字符串值的长度大，或者 key 不存在时，返回 0 。
  - decr/incr keyname; decrby/incrby key_name amount 
    - 将 key 中储存的数字值减一/加一; 减去/加上amount。
    - key不存在, 先初始化为0,再执行操作
    - 值包含错误的类型,或者不能表示为数字, 返回错误
    - 值限制在64位(bit)标识之内
  - incrbyfloat key_name float_amout
    - 为 key 中所储存的值加上指定的浮点数增量值. 没有decrbyfloat
  - strlen key_name
    - 字符串值的长度。 当 key 不存在时，返回 0, 数值也能返回 105返回3
  - strrange key_name offset value 
    - 对key的value, 从offset开始, 使用value覆盖
  - append keyname new_value
    - Redis Append 命令用于为指定的 key 追加值。如果 key 已经存在并且是一个字符串， APPEND 命令将 value 追加到 key 原来的值的末尾。
  - mget
    - 一个包含所有给定 key 的值的列表。
- 应用场景
  - 单值缓存
    - 如商品库存 key=商品id, value=库存数量
  - 对象缓存
    - set 存储用户信息，key=user:id value=json格式数据, 某个属性, 并不是对象的数据
    - mset 批量存取, 数据不断变化的应用场景
  - 分布式锁
    - setnx setex
  - 计数器
    - incr/decr; incrby/decrby; incrbyfloat
  - 共享session
    - 于负载均衡的考虑，分布式服务会将用户信息的访问均衡到不同服务器上. 如果服务器间的session是独立的话, 用户刷新一次访问可能会需要重新登录(如果到了另外一台服务器上时)，为避免这个问题可以用redis将用户session集中管理，在这种模式下只要保证redis的高可用和扩展性的，每次获取用户更新或查询登录信息都直接从redis中集中获取。
  - 限速
    - 可以限制获取某个数据的速度
  - 分布式系统全局序列号
    - 一般数据库表的主键用自增长序列号，假如系统压力大，后端做了分库分表，数据库自带的auto_increment就不适用了，可以使用redis的自增，由于Redis为单进程单线程模式， 采用队列模式将并发访问变成串行访问，且多客户端对Redis的连接并不存在竞争关系 
      - incrby orderid 1000 让每个机器一次拿1000个,自己慢慢用,防止 incr order 这样redis压力大
## 从简单命令学起

### 全局
- flushall 清空数据库
### scan
- link:
  - 简单: https://www.cnblogs.com/wy123/p/10955153.html
  - 详细: https://blog.csdn.net/qq_40399646/article/details/109034331
- SCAN cursor [MATCH pattern] [COUNT count]
  - 返回一个包含两个元素的数组
  ```r
  127.0.0.1:6379> scan 0 match k* count 10 # 从0开始迭代键名以key开头的
  1) "11" # 这个元素是用于进行下一次迭代的新游标
  2) 1) "k8" # 这个第二个元素是一个数组, 包含了所有被迭代的元素
     1) "k11"
     2) "k4"
     3) "k10"
     4) "k5"
     5) "k3"

  ```
  - cursor :游标
    - 游标参数被设置为 0 时， 服务器将开始一次新的迭代; 而当服务器向用户返回值为 0 的游标时， 表示迭代已结束
    - 使用错误的游标: 传入间断的（broken）、负数、超出范围或者其他非正常的游标来执行增量式迭代并不会造成服务器崩溃， 但可能会让命令产生未定义的行为。未定义行为指的是， 增量式命令对返回值所做的保证可能会不再为真
    
  - Match :匹配key名称的匹配模式 glob 风格的模式参数
    - MATCH功能对元素的模式匹配工作是在命令从数据集中取出元素后和向客户端返回元素前的这段时间内进行的， 所以如果被迭代的数据集中只有少量元素和模式相匹配， 那么迭代命令或许会在多次执行中都不返回任何元素。
    
  - count: 指定从数据库中的多少个数据中查找; 默认值为10
    - count 20中的20并不是代表输出符合条件的key，而是限定服务器单次遍历的字典槽位数量(约等于); 在key个数为10W个的情况下，一次遍历20w个字典槽，肯定能完全遍历出来符合pattern的所有key
    - 在迭代一个编码为整数集合（intset，一个只由整数值构成的小集合）、 或者编码为压缩列表（ziplist，由不同值构成的一个小哈希或者一个小有序集合）时， 增量式迭代命令通常会无视 COUNT 选项指定的值， 在第一次迭代就将数据集包含的所有元素都返回给用户。
    - 数据集比较大时，如果没有使用MATCH 选项, 那么命令返回的元素数量通常和 COUNT 选项指定的一样， 或者比 COUNT 选项指定的数量稍多一些。
  
- SCAN命令是一个基于游标的迭代器。这意味着命令每次被调用都需要使用上一次这个调用返回的游标作为该次调用的游标参数，以此来延续之前的迭代过程。
    - 包括sscan/hscan/zscan 都支持增量式迭代, 它们每次执行都只会返回少量元素，所以这些命令可以用于生产环境，而不会出现像 EYS 或者 SMEMBERS 命令带来的可能会阻塞服务器的问题。
  

- scan的时间复杂度
> 起始版本：2.8.0
时间复杂度：O(1) for every call. O(N) for a complete iteration, including enough command calls for the cursor to return back to 0. N is the number of elements inside the collection.


- scan命令的保证
  - 从集合遍历的元素可能重复, 处理重复的工作应该交给应用程序负责

- 在巨大的数据量的情况下, 类似于查找符合某种规则的key的信息有两种方式:
  - **keys** 简单粗暴, 由于Redis单线程这一特性, keys命令是以阻塞的方式执行的, keys是以遍历的方式实现的, 复杂度是O(n), 库中的key越多, 查找实现的代价越大,产生的阻塞时间越长
  - **scan** 以非阻塞的方式实现key值的查找, 绝大数情况下是可以替代keys命令的, 可选性更强


-  并发执行多个迭代
  - 在同一时间， 可以有任意多个客户端对同一数据集进行迭代， 客户端每次执行迭代都需要传入一个游标， 并在迭代执行之后获得一个新的游标， 而这个游标就包含了迭代的所有状态， 因此， 服务器无须为迭代记录任何状态。


## other
- 以下写入100000条key***：value***格式的测试数据（ps：用pipline的话,1w一笔，每一笔在秒级完成）
```python
import redis, sys, datatime
def create_testdata():
    r = redis.StrictRedis(host='***.***.***.***', port=***, db=0, password='***')
    counter = 0
    with r.pipeline(transaction=False) as p:
        for i in range(0, 100000):
            p.set('key' + str(i), "value" + str(i))
            counter = counter + 1
            if (counter == 10000):
                p.execute()
                counter = 0
                print("set by pipline loop")
```


