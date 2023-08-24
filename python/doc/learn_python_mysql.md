# TO
- 什么是池化，池化带来的改变，怎么实现
# 池化 https://blog.csdn.net/qq_42956653/article/details/126062269
- 池化技术就是把需要用的东西放在一个池里，当用的时候从这里取，用完了可以还到池里面去。以此来省去这个对象的创建流程。
- 池化技术能够减少资源对象的创建次数，提高程序的响应性能，特别是在高并发的场景下这种提升会更加明显，所以池化技术相当于一层缓冲。使用池化技术缓存的资源对象有如下共同特点：
    对象创建时间长
    对象创建需要大量资源；
    对象创建后可被重复使用
- 像 线程池，内存池，请求池，对象池，连接池 都具备以上的共同特点。
## 数据库连接池
- 什么是数据库连接池
    - 数据库连接池是程序启动时建立足够数量的数据库连接，并将这些连接统一管理起来组成一个连接池，程序动态的从池中取连接与归还连接。
    - 创建数据库连接相对来说是比较耗时的，不仅有三次握手，还有mysql的三次认证过程。所以在程序启动时就创建多个连接统一管理，可以提高程序的响应性能。

- 为什么使用数据库连接池
    - 资源复用：由于数据库的连接得到的复用，避免频繁的创建和销毁连接的性能开销。在减少系统消耗的基础上，另一方面也增进了系统运行环境的平稳性（减少内存碎片以及数据库临时进程/线程的数量）。
    - 更快的系统响应速度：数据库连接池在初始化后，往往已经创建了若干数据库连接置于池中备用。此时连接的初始化工作均已完成。对于业务请求处理而言，直接利用现有可用连接，避免了从数据库连接初始化和释放过程的开销，从而缩减了系统整体响应时间。
    - 统一的连接管理，避免数据库连接泄露：在较为完备的数据库连接池实现中，可根据预先的连接占用超时设定，强制收回被占用连接。从而避免了常规数据库连接操作中可能出现的资源泄露。
## code
- PyMySQL
```
pip3 install PyMySQL
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()
```
- DBUtils是一套Python数据库连接池包，并允许对非线程安全的数据库接口进行线程安全包装。DBUtils来自Webware for Python。
- DBUtils提供两种外部接口：
    - PersistentDB ：提供线程专用的数据库连接，并自动管理连接。
    - PooledDB ：提供线程间可共享的数据库连接，并自动管理连接。
- 链接不需要关闭



```
from dbutils.pooled_db import PooledDB, SharedDBConnection
class MysqlConnector(object):
    def __init__(self, database_conf):
        self.POOL = PooledDB(
            creator=pymysql,
            maxconnections=10,  # 连接池的最大连接数
            maxcached=10,
            maxshared=10,
            blocking=True,
            setsession=[],
            host=database_conf.get("host"),
            port=int(database_conf.get("port", 3306)),
            user=database_conf.get("username", "exporter"),
            password=database_conf.get("password", "Exporter12#$"),
            database=database_conf.get("database_name", "qdam"),
            charset='utf8',
        )

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def connect(self):
        conn = self.POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    def connect_close(self, conn, cursor):
        cursor.close()
        conn.close()

    def fetch_all(self, sql, args=None):
        conn, cursor = self.connect()
        if args is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, args)
        record_list = cursor.fetchall()
        return record_list

    def fetch_one(self, sql, args):
        conn, cursor = self.connect()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        return result

    def insert(self, sql, args):
        conn, cursor = self.connect()
        row = cursor.execute(sql, args)
        conn.commit()
        self.connect_close(conn, cursor)
        return row
```