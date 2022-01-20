# 问题
- Can't reconnect until invalid transaction is rolled back
    ```
    Session = sessionmaker(bind=engine, autoflush=True, autocommit=False)
    # 在python console 中运行，ctrl + c， 再运行；重复几次就会出出错，放到模块中就不会出错
    for i in range(100000):
        print(f"index: {i}, total: {len(session.query(User).filter_by(id=1).all())}")
    ```
    - link：
      - 原因：https://www.cnblogs.com/kaerxifa/p/11887127.html
    - 解决： 重启flask shell 就好了(auto_commit=True也可)
    - 避免： 每个web请求完了session.close/rollback把链接还到pool
        ```
        try:
            order = User.query.filter_by(user_id=1).first()
        except InvalidRequestError:
            db.session.rollback()
        ```

    - 原因是从pool拿的connect 没有以session.commit/rollback/close的某一种放回pool里。connection的transaction就没有完结（rollback or commit）；而不知什么原因（recycle or timeout了）你的connection又死掉了，sqlalchemy就尝试重新连接。 而由于transaction还没有完结，就无法重新连接。
# Engine
Engine 是SQLAlchemy 应用的入口. 是数据库及其DBAPI的大本营, 通过连接池和Dialect传送到SQLAlchemy应用, 描述如何去和特定的数据库/DBAPI集合进行对话.![总体架构](https://docs.sqlalchemy.org/en/13/_images/sqla_engine_arch.png)
引擎同时引用方言和池，它们一起解释 DBAPI 的模块功能以及数据库的行为。
- ## link:
  - https://docs.sqlalchemy.org/en/13/core/engines.html#mysql
- ## 问题
  - dialect是指什么?
    - 是不同的database需要不同的url吗? 不是， 可以说是关键字
- ## 创建一个Engine仅仅需要调用create_engine()
    ```
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase') # 此时即使是错误的链接也不会报错
    engine.connect()# 如果有错误是会返回错误的,无错误返回一个connection obj
    ```
  - 上面的engine创建了一个为PostgreSQL量身定做的Dialect对象, 以及一个Pool对象, 当接受到第一次连接请求时, 会在Localhost:5432上建立一个DBAPI连接. 注意在在调用 Engine.connect() 方法或者依赖该方法的操作(如Engine.execute(其依赖engine.connect))之前，Engine 及其底层 Pool 不会建立第一个实际的 DBAPI 连接.Engine 和 Pool 可以说是有lazy initialization行为
  - Engine创建后就能直接被用来和database交互, 或者被传递给Session对象来和ORM一起工作. 本文档具有一些 关于Engine配置的细节. 下一章节[working with Engines and Connections] 详细描述了如何使用Engine以及类似API的使用,通常用于非 ORM 应用程序。

- ## 对各种各样数据库的支持
  - SQLAlchemy 包括了各种各样后端的方言实现. 大多数常见数据库的方言被包括在SQLAlchemy里, 少数的数据库需要单独安装其他的dialect. 
- ## 数据库 Urls
  - create_engine基于Url返回一个Engine object. Urls遵循RFC-1738, 通常包括username/pasword/hostname/database_name和其他配置的关键字参数. 某些情况下能接受文件路径, 还能使用data source name 替换host和database.典型的数据库Url:`dialect+driver://username:password@host:port/database`
  - Dialect 包括SQLAlchemy dialect的标识名, 如sqlite,mysql,oracle, mssql. driver是被用来链接数据库的DBAPI的名字, 使用小写字母. 如果未指定，则将导入“默认”DBAPI（如果可用） - 此默认值通常是该后端可用的最广为人知的驱动程序。
  - 特殊字符的表示方式
  - 和其他的URL一样, 密码中可能使用的特殊字符需要经过 URL 编码才能正确解析。下面有一个url的例子,其中包括密码`kx%jj5/g`, 百分号和slash会别标识为%25和%2F
  - 使用urlib.parse来对特殊支付进行编码
  ```
  >>> import urllib.parse
  >>> urllib.parse.quote_plus("kx%jj5/g")
    'kx%25jj5%2Fg'
  ```
  - 下面列举了常见的链接, 想要查看所有dialect以及第三方dialect的详细信息, 查看链接
  - ### mysql
    - mysql dialect 使用mysql-python作为默认的DBAPI. 有许多可用的mysql DBAPI, 包括MySQL-connector-python和OurSQL(一个pypi包)
    - 使用pymysql作为 DBAPI `engine = create_engine('mysql+pymysql://root:huawei123@90.90.0.143/test')`
- ## engine Create API
  - create_engine
  - engine_from_config # 从配置文件创建engine
  - make_url: # 把string 变成url实例
  - URL
  - engine创建相关的api
- ## 一个create_engine()的实例
  ```
  # 数据连接全局共用一个数据库池
  db_engine = create_engine(conf["sqlalchemy"]["sql_url"], # 
                            echo=False,
                            pool_size=800,
                            pool_recycle=30,
                            pool_pre_ping=True)

  # 这个也放在全局 因为sessionmaker会申请一些全局属性，可能会引起内存泄漏
  db_session = sessionmaker(bind=db_engine, autocommit=True,
                            expire_on_commit=False)
  ``` 

# Session
记录一些session的问题
## link:
  - [SQLAlchemy session的autocommit autoflush详解](https://www.jianshu.com/p/b219c3dd4d1e)
  - https://zhuanlan.zhihu.com/p/48994990
  - https://zhuanlan.zhihu.com/p/98861210
## SQLAlchemy 的 session 是指什么？
- session 会在需要的时候（比如用户读取数据、更新数据时）和数据库进行通信，获取数据对象，并有一个池子来维护这些数据对象，保证你访问数据时不出现意外的问题
- session 和连接(connection) 不等同，session 通过连接和数据库进行通信
- session 是 Query 的入口
## session 的 autoflush 参数是干什么的，我到底要不要开启它？
- 首先，学习两个概念：flush 和 commit。
  - flush 的意思就是将当前 session 存在的变更发给数据库，换句话说，就是让数据库执行 SQL 语句。
  - commit 的意思是提交一个事务。一个事务里面可能有一条或者多条 SQL 语句
  - SQLAlchemy 在执行 commit 之前，肯定会执行 flush 操作；而在执行 flush 的时候，不一定执行 commit，这个主要视 autocommit 参数而定，后面会详细讲
- 当 autoflush 为 True 时（默认是 True），session 进行查询之前会自动把当前累计的修改发送到数据库（注意：autoflush 并不是说在 session.add 之后会自动 flush）
## session 的 autocommit 参数又是什么，它和 autoflush 的区别是什么？
- commit 对应的概念是事务（transaction），默认情况下，session 参数 autocommit 的值是 False(所有请求都相当于自动开启了事务（查询也是），即所有的事务需要手动提交)，SQLAlchemy 也推荐将它设置为 False。
- 当打开autocommit时，DMBS会为每一条SQL执行一个事务，也就是说，每一条SQL都是立即生效的。
- 当关闭autocommit时，客户端必须手动显式声明事务的开始和结束，具体能不能读到其它客户端产生的数据得看MVCC隔离层级的设置。