# 问题
- 当mysql作为database时，使用String/Integer数据类型需要注意的地方
  - ip = Column(String(12)) # 必须显示标识长度 
- "Identifier name '<bound method ? of <class 'common.model.test2_model.Child'>>_ibfk_1' is too long") 使用声明系统创建一个表时表名太长。
  - 是把__tablename__写成了__tablename_
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
 