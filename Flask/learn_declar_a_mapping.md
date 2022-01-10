# 问题
- 当mysql作为database时，使用String/Integer数据类型需要注意的地方
  - ip = Column(String(12)) # 必须显示标识长度 
# 声明基类
- 主文档中已经简单介绍了声明一个映射类的方式, 但某些场景下, 可能还需要一些其他的方式, SQLAlchemy也提供了相应的方法
- link
  - [Mapping与Declarative详解](https://blog.csdn.net/haoxun06/article/details/104401259)
  - [创建SQLAlchemy的ORM类的基类](https://blog.csdn.net/wenxuansoft/article/details/46561905)
- ## 声明基类的方式
  - SQLAlchemy需要分别创建表, 创建类,然后通过mapping函数把表里的每条记录和python对象映射起来
    ```
    from sqlalchemy import Table, MetaData, Column, Integer, String,
    from sqlalchemy.orm import mapper
    
    # 数据库的元数据，你可以认为它是一个容器，装载了所有的表结构
    metadata = MetaData()
    
    # 数据库中的news_article表
    article = Table("news_article", metadata,
            Column("id", Integer, primary_key=True),
            Column("title", String)``
            )
    
    # 这是一个普通的Article类
    class Article:
      def __init__(self, title):
        self.title = title
    
    # 通过mapper函数进行映射关联
    mapper(Article, article)
    # 使用方式和现在一样,都是通过session
    ```
  - 新的ORM映射不需要手动通过mapping函数来关联table与类之间的关系，可以直接通过声明（Declarative ）系统（我不知道这样翻译对不对）来定义一个类，这个类会直接映射到数据库的表，declarative 把 Table、mapper、还有类这三者放在一块进行声明，从而实现了ORM的映射
    ```
    from sqlalchemy.ext.declarative import declarative_base
 
    Base = declarative_base()
    
    class Article(Base): # 
      __tablename__ = 'news_article'
      id = Column(Integer, primary_key=True)
      title = Column(String(50))
    ```
    - 这个类必须继承基类 Base，Base 就是我们的声明系统，这样就完成了Table与类之间的映射关系，而背后的操作都是通过一个declarative_base 工厂方法构造的声明系统完成的。
- MetaData被用来创建表或者删除表
  ```
  # 可以重复执行
  Base.metadata.create_all(engine)
  # 只创建user表
  User.metadata.create_all(engine)
  ```
- 创建自己的ORM基类
  - 例子: 提供一个自定义的ORM基类, 所有基于此基类的ORM model 都有一个字段或方法
    ```
    class BaseModelMixin(object):
        """ 为所有Model提供公用方法 """
    
        @declared_attr
        def id(self):
            return  Column(String(32),primary_key=True,default=uuid.uuid4().hex)#唯一性的UUID
    
        def test(self):
            pass
    
    ModelBase=DeclarativeBase(cls=BaseModelMixin)
    ```
  - 要为为DeclarativeBase提供一个cls参数，该参数的成员会被ModelBase继承或mixin.
  - 为基类增加Column不能直接定义，只能通过@declared_attr修饰符定义。

# Engine
Engine 是SQLAlchemy 应用的入口. 是数据库及其DBAPI的大本营, 通过连接池和Dialect传送到SQLAlchemy应用, 描述如何去和特定的数据库/DBAPI集合进行对话.![总体架构](https://docs.sqlalchemy.org/en/13/_images/sqla_engine_arch.png)
引擎同时引用方言和池，它们一起解释 DBAPI 的模块功能以及数据库的行为。
- ## link:
  - https://docs.sqlalchemy.org/en/13/core/engines.html#mysql
- ## 问题
  - dialect是指什么?
    - 是不同的database需要不同的url吗?
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