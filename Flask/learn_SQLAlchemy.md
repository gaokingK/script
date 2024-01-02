# 介绍
- is The Python SQL Toolkit and Object Relational Mapper
- SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.
- SQLAlchemy Object Relational Mapper 提供了一种将用户定义的Python类与数据库 以及 这些类的实例与相应表中的行关联起来的方法。 它包括一个透明的同步对象及其相关行之间状态的所有更改的系统：Unit of work，以及用户定义的类及其相互之间定义的关系表示数据库查询的系统（查询）
### 版本 1.x 2.0 
This tutorial covers the well known SQLAlchemy ORM API that has been in use for many years. As of SQLAlchemy 1.4, there are two distinct styles of ORM use known as 1.x style and 2.0 style, the latter of which makes a wide range of changes most prominently around how ORM queries are constructed and executed.
- 本文档是按照1.4翻译的, 但是可能会假如一些1.3的

### links
- [doc]: https://www.osgeo.cn/sqlalchemy/orm/tutorial.html **教程好像是1.4的**
- [1.4 en](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- [1.3 en](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)

# 空链接去原文里找
- 还是要全面翻译啊, 要不第二次都看不到

# 使用
### 问题
- [创建一个没有主键的表](https://docs.sqlalchemy.org/en/14/faq/ormconfiguration.html#faq-mapper-primary-key) ----------------------no
- 多对多关系有方向吗? 为什么说BlogPost.keyword是多对多关系
- 正常建立一个模型需要怎么做？
- 为什么要写基类， 是像其他类的继承这些作用吗 
	- [使用mixin组合映射层次](https://www.osgeo.cn/sqlalchemy/orm/declarative_mixins.html)
- 声明性基类到底是什么
- Django里的ORM体系是怎样的, metadata是怎样被生成的
- 使用`session.query(User).filter(....)` 进行查询时, 是从当前事务中进行查询的吗? 当前事务是当前会话对象中所存储的吗? 或者说: 当前事务和当前会话对象是什么关系?
	> 查询会话时，可以看到它们被刷新到当前事务中：
	```
	>>> session.add(fake_user)
	>>> session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
	[<User(name='Edwardo', fullname='Ed Jones', nickname='eddie')>, <User(name='fakeuser', fullname='Invalid', nickname='12345')>]
	```
- 只有这一种使用方法吗?
- 只能回滚当前事务中的吗? 提交后的会话中能回滚吗
- 如何查看生成的SQL?
	


### 连接到数据库 使用orm时,并不需要显式的创建引擎
- 例子: 连接到 内存数据库SQListe
```
>>> from sqlalchemy import create_engine
>>> engine = create_engine('sqlite:///:memory:', echo=True)
```
- echo 参数 能看到生成的所有SQL, echo参数能开启SQLAlchemy的日志, 是通过python的logging实现的
- create_engine() 返回一个Engine的实例, 具有和数据库交互的核心接口, 通过[dialect]()处理DBAPI的细节来适配.
- ##### [Lazy Connecting]， 创建时虽然有返回，但并未实际尝试链接到数据库，而是在第一次要求它对数据库执行任务时发生
- 第一次调用engine.execute或者engine.connect()是, Engine建立一个在真正的DBAPI连接到数据库, 之后会使用它来执行SQL
- 当使用ORM时，我们通常不使用 [Engine]() 直接创建；相反，它被ORM在幕后使用，稍后我们将看到。
- [不同的数据库url](https://www.osgeo.cn/sqlalchemy/core/engines.html#database-urls)


### 声明映射
- "使用ORM时，配置过程首先描述将要处理的数据库表，然后定义 将映射到这些表 的自己的类" 这个类不是指我们所定义的类吧? ----no
- 现在的SQLAlchemy中, 上面两个任务被Declarative Extensions 这个系统一块执行了, 这个系统语序我们创建 包括 对要映射的数据库的描述指令 的 类.
- 使用声明式系统映射的类是根据基类定义的，该基类维护与该基相关的类和表的目录 - 这称为**声明式基类**。我们的应用程序通常在一个通用导入的模块中只有这个base的一个实例。
- 例子: 使用声明式基类定义一个类
```
>>> from sqlalchemy.orm import declarative_base
>>> Base = declarative_base()
# 现在, 就有了一个base, 我们可以根据它来定义任何个被映射的类, 先定义一个user表, 一个名为 User 的新类将是我们将此表映射到的类。在这个类中,我们定义要映射的表的细节, 主要是表名以及列的名称和数据类型：
>>> from sqlalchemy import Column, Integer, String
>>> class User(Base):
...     __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String)
...     fullname = Column(String)
...     nickname = Column(String)
...
...     def __repr__(self):
...        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)
```
- 上面的__repr__方法是可选的, 这里定义它是为了更好的格式化user obj
- 使用Declarative的类最少要有一个__tablename__属性, 并且至少一个列是主键(at least one Column which is part of a primary key 主键能有很多列吗?) -----------------no
- SQLAlchemy 本身从不对类所引用的表做出任何假设，包括它没有关于名称、数据类型或约束的内置约定。
- 但这并不意味着需要样板； 相反，我们鼓励您使用辅助函数和 mixin 类创建自己的自动化约定，在[ Mixin and Custom Base Classes.] 中有详细描述。
- 当我们的类被构造时，Declarative使用descriptors替换了Column；这种行为被称为 instrumentation . “instructed”映射类将为我们提供 在SQL上下文中引用表 以及 从数据库中持久化和加载列值 的方法。
- 除了映射过程对我们的类所做的事情之外，该类在其他方面仍然主要是一个普通的 Python 类，我们可以为其定义应用程序所需的任意数量的普通属性和方法。 
	
### 创建一个模式
- 上面的User类通过Declarative system 被构造, 通过User, 我们定义了关于我们表的信息,这些信息被称为table metadata. 这个object被 SQLAlchemy 用来表示一个特殊表的信息, 这个表被称为Table object, 并且here Declarative 已经为我们搞了一个. 我们可以查看这个object 通过`User.__table__`
- 当我们声明User时, Declartive 使用Python metaclass来完成声明, 为了在类声明完成后执行额外的activities, 他(Declartive)然后创建 Table object 根据我们的规则, 并且通过构造一个mapping object关联他(Declartive?).这个对象是一个我们通常不需要直接处理的幕后对象（尽管它可以在我们需要的时候提供关于我们的映射的大量信息）
- Table object 是 MetaData的成员, 后者有一个更大的collection, 当使用Declartive时, 可以通过 声明性基类(Base) 的metadata属性去访问
- 这个 MetaData 是一个 registry 其中包括向数据库发出一组有限的模式生成命令的能力。用 MetaData 为尚未存在的所有表向数据库发出create table语句
- ###### 经典映射
	- 尽管强烈建议使用声明性系统，但使用sqlacalchemy的ORM不需要声明性系统
	- 不通过Declartive, 任何普通的类都一一映射到Table使用mapper (), 这种用法称为经典映射
- ###### 最小表描述vs完整描述
	- 面对不同的数据库, 在类似于create table 这种语句构造上的区别,及解决办法
	- 熟悉create table语法的用户可能会注意到上面生成的SQL中varchar列的生成没有长度；在sqlite和postgresql上，这是一个有效的数据类型，但在其他数据类型上，这是不允许的

### 创建映射类的实例
- 即使在下面的语句中,我们并没有指定id的值, 当我们访问id的时候仍然能得到一个None,而不是python抛出一个Attribute 异常. SQLAlchemy`s instrumention 一般在第一次被访问时produces被映射的属性的默认值. 对于那些实际上指定了一个值的属性, instrumenttation 系统会跟踪这些值为了在最终的INSERT 语句发出到database的时候使用
- ###### 使用Declartive 系统定义的类已经提供了一个构造函数,能自动接受与映射的列匹配的关键字的名字, 如果重新定义,原有的会覆盖

### 创建Session
- Session 是会话对象, 是ORM操作database的句柄, 在create_engine同样的等级, 创建一个Session类
- 如果没有create_engine时, 可以先穿件Session类,然后使用` Session.configure(bind=engine)`去连接Session
- ###### Session的生命周期
	- (何时构造一个Session, 何时提交Session, 何时关闭?)[https://www.osgeo.cn/sqlalchemy/orm/session_basics.html#session-faq-whentocreate]
	- 很大部分取决于要build的应用的类型,
	- Session是对像的局部工作空间, 特定数据库连接的本地工作区
- session 创建出来时和engine联系在一起,但并没有打开任何连接, 当第一次被使用时,会从engine维护的连接池中取出一个连接, 并且保持这个链接直到提交所有改变或者关闭这个链接
		 0
### Adding and Updating Objects
- `session.add(user_obj)` 持久化obj
	- 此时实例在**pending**状态, 还没有发出SQL, Session会立即发出SQL去持久化obj一旦obj被需要时, 使用的**flush**机制, 一旦我们查询这个obj在数据库中, 所有**pending**的信息首先会被刷新,然后查询会被立即进行
- **identity map** 一旦具有特定主键的对象出现在 Session ，所有SQL查询 Session 将始终为该特定的主键返回同一个python对象；如果试图在会话中放置第二个已持久化且具有相同主键的对象，也会引发错误。
- `session.dirty`
- `session.new`
- `session.commit()` 提交剩余的改变到数据库, 并且提交整个过程中始终运行的事务, 会发出相关sq语句的声明;会话引用的连接资源现在返回到连接池。此会话的后续操作将在 new 事务，它将在第一次需要时重新获取连接资源
- **重新加载** 默认情况下，当第一次在新事务中访问前一个事务时，sqlAlchemy将刷新该事务中的数据，以使最新状态可用。重新加载的级别是可配置的
- ###### Session 状态
	- 如果没有主键，实际插入时，它将在四个可用“对象状态”中的三个之间移动- 瞬态 ， 悬而未决的 和 持久的 . 
	- (Quickie对象状态简介)[https://www.osgeo.cn/sqlalchemy/orm/session_state_management.html#session-object-states]

### 回滚
- 使用session.rollback()
- 只有这一种使用方法吗? ---------------------------no
- 只能回滚当前事务中的吗? 提交后的会话中能回滚吗 ----------------------no
	
# 查询
- session.query() 创建一个Query obj, 参数可以是类和class-instrumented 相互组合的多个或者单个参数
```python
>>> for instance in session.query(User).order_by(User.id):
...     print(instance.name, instance.fullname)
```

- Query 也接受ORM-instrumented descriptors 作为参数, 当多个类实体或者column-based实体传给query函数, 返回的结果表示为元组
```python
>>> for name, fullname in session.query(User.name, User.fullname):
...     print(name, fullname)
```

- 返回的元组由Row class提供,是已命名的元组, 可被当成一般的python obj, 表示属性的名称和属性相同, 表示类的名字和类相同
```python
>>> for row in session.query(User, User.name).all():
...    print(row.User, row.name)
```

- ColumnElement.label()  您可以使用 ColumnElement.label() 构造控制各个列表达式的名称
```python
>>> for row in session.query(User.name.label('name_label')).all():
...    print(row.name_label)
```

- 假如调用Session.query() 的结果中存在多个实体, 可以使用aliaed()控制某个完整实体(如 User)的名字
    - 意思是结果中可能有User/Adminer....等多种对象,可以给某个对象换个名吗? 那有什么意义呢? ------------------no

- Query 基础的操作包括发布LIMIT和OFFSET, 最方便的是使用Python的slices, 常常和ORDER_BY结合使用
```python
>>> for u in session.query(User).order_by(User.id)[1:3]:
...    print(u)
```
- 以及使用filter_by()过滤结果, 传入关键字参数
```python
>>> for name, in session.query(User.name).\
...             filter_by(fullname='Ed Jones'):
```
- 或者是使用更领过的SQL构造的filter(), 能在映射类上使用具有类级属性的常规python运算符
```python
>>> for name, in session.query(User.name).\
...             filter(User.fullname=='Ed Jones'):
```

- Query 对象是完全生成的，**这意味着大多数方法调用都会返回一个新的 Query 对象，在该对象上可以添加更多条件。** 例如，要查询名为“ed”且全名为“Ed Jones”的用户，您可以调用 filter() 两次，它使用 AND 连接条件
### 连接多个查询条件
- 假设有种情况，请求中包含的过滤条件不固定，可以使用这种办法来根据到来的条件动态的拼接查询条件
```py
query = Book.query

if title:
	query = query.filter(Book.title.ilike(f"%{title}%"))

if author:
	query = query.filter(Book.author.ilike(f"%{author}%"))

if genre:
	query = query.filter(Book.genre.ilike(f"%{genre}%"))
## 或许也可以这样
parm = (Book.title.ilike(f"%{title}%"),Book.genre.ilike(f"%{genre}%") )
query = query.filter(*parm)
```
- 进一步封装
```py
def build_query(base_query, conditions):
    """
    Build a dynamic query based on the given conditions.

    Args:
    - base_query: The base SQLAlchemy query object.
    - conditions: A dictionary of conditions to filter the query.

    Returns:
    - The modified query object.
    """
    query = base_query

    for field, value in conditions.items():
        # Assuming 'ilike' for case-insensitive substring matching
        query = query.filter(getattr(Book, field).ilike(f"%{value}%"))

    return query

# 在路由处理函数中
def search_books():
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')

    # 基础查询
    base_query = Book.query

    # 构建条件字典
    conditions = {}
    if title:
        conditions['title'] = title
    if author:
        conditions['author'] = author
    if genre:
        conditions['genre'] = genre

    # 使用 build_query 函数构建查询
    query = build_query(base_query, conditions)

    # 执行查询
    result = query.all()

    # 将查询结果转换为 JSON 响应
    books = [{'title': book.title, 'author': book.author, 'genre': book.genre} for book in result]
    return jsonify(books)	
```

### [常用筛选器运算符](https://www.osgeo.cn/sqlalchemy/orm/tutorial.html#common-filter-operators)
- like 呈现like运算符，它在某些后端不区分大小写，在其他后端区分大小写。对于保证不区分大小写的比较，请使用 ColumnOperators.ilike()
- 大多数后端不直接支持iLike。对于那些 ColumnOperators.ilike() 运算符呈现一个表达式，该表达式与应用于每个操作数的下SQL函数组合在一起。
- 对于AND/OR/ 确保使用and_/or_而不是python的操作符
- ColumnOperators.match() uses a database-specific MATCH or CONTAINS function; its behavior will vary by backend and is not available on some backends such as SQLite.****

### 返回list和scalars
- 是Query的各种方法
- 当Query返回关于ORM-mapped对象的列表时, 列表中的条目是由SQL执行结果集基于主键去重的, 即如果SQL查询返回两个id=7的行,你之后得到一个id=7的USER对象, 当查询单独列的时候这种情况不会应用
- []为什么结果和query.count不一样呢?](https://www.osgeo.cn/sqlalchemy/faq/sessions.html#faq-query-deduplicating)
- Query.one() 找到多行和找不到行都会报错 对于希望处理“未找到项目”和“找到多个项目”不同的系统来说，方法是很好的；例如RESTful Web服务，它可能希望在未找到结果时引发“404未找到”，但在找到多个结果时引发应用程序错误。

### 使用文本SQL
- 不完整的SQL可以通过test构造
- 完整的可以通过from_statement()可以构造完整的SQL, 如果没有进一步的说明，ORM将根据列名将ORM映射中的列与SQL语句返回的结果相匹配; 更好地将映射列定位到SQL中的文本, 可以通过TextClause.columns()
- 如果不想让返回完整的对象(USER)而是对象的某个属性, 也是可以的
  
### 计数
- Query.count() 确定返回多少行
- Query.count() 曾经是一个非常复杂的方法，当它试图猜测是否需要围绕现有查询的子查询时，并且在某些特殊情况下它不会做正确的事情. 现在它每次都使用一个简单的子查询, 只有两行长并且没每次返回正确的值. 如果特定语句绝对不能容忍子查询的存在，请使用 func.count()。
- Query.count 生成的SQL来看, sqlAlchemy总是将我们正在查询的内容放入子查询中，然后计算其中的行数. 在某些情况下，这可以简化为 SELECT count(*) FROM table(或许是这种语句比上面的放入子查询中的更简单?) 但是，现代版本的sqlacalchemy并不试图猜测这是什么时候合适，因为可以使用更明确的方法发出准确的sql。
- 对于需要具体指示“要计数的事物”的情况，我们可以直接使用表达式 func.count() 指定“计数”函数，该表达式可从 expression.func 构造中获得。 下面我们使用它来返回每个不同用户名的计数：
```python
>>> from sqlalchemy import func
SQL>>> session.query(func.count(User.name), User.name).group_by(User.name).all()
[(1, u'ed'), (1, u'fred'), (1, u'mary'), (1, u'wendy')] # ed 有1个
```
- 如果我们直接用 User 主键表示计数，则可以删除 Query.select_from() 的用法
- 子查询和 `select count(*) from table` 是等价的吗?------------------------------------------no

# 关系
### 建立关系
- 一对多(一个用户可以有多个邮箱, 再建一个Address表)  ForeignKey
```python
>>> from sqlalchemy import ForeignKey
>>> from sqlalchemy.orm import relationship

>>> class Address(Base):
...     __tablename__ = 'addresses'
...     id = Column(Integer, primary_key=True)
...     email_address = Column(String, nullable=False)
...     user_id = Column(Integer, ForeignKey('users.id'))
...     # 引入了ForeignKey构造, 应用于column上, 指示这个列的值应该被限制为远程列中存在的值
...     user = relationship("User", back_populates="addresses")
...     # 告诉ORM Address 类本身应链接到 User 类, 以address.user方式使用
...     def __repr__(self):
...         return "<Address(email_address='%s')>" % self.email_address

>>> User.addresses = relationship(
...     "Address", order_by=Address.id, back_populates="user")
	# 附加的 relationship() 指令放置在 User.addresses 属性下的 User 映射类上。

```
- 这是关系数据库的一个核心特性，是将原本不相关的表集合转换为具有丰富重叠关系的“粘合剂”
- relationship() 用两表外键间的关系,来判断Adress.user是多对一
- relationship.back_populates参数 声明为引用属性名时的补充; 是SQLAlchemy常用的属性relationship.backref的一个更新的版本(后者更没有被丢弃)
- 通过这样做，每个关系（）可以对反向表达的相同关系做出明智的决定
- 多对一的反面总是一对多
- [基本的关系模式](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#relationship-patterns)
- Address.user 和 User.addresses 这两个互补关系被称为双向关系，是SQLAlchemy ORM 的一个关键特性
- relationship中的某些参数, 如User这个涉及到对方类的,可以使用string去指定,(假设使用的是声明性系统), 一旦所有的映射完成,这些string被等同于python表达式, 是因为为了生成实际的参数.
> 大多数（但不是全部）关系数据库中的外键约束只能链接到主键列或具有唯一约束的列。
  	复合主键
	瀑布引用操作, 属于关系数据库原生的函数. 外键列可以根据被引用列或行中的更改自动更新自己
	自引用外键 外键可以引用自己的表
- 从metadata中创建需要创建的表, 会跳过已有的表吗 会 `Base.metadata.create_all(engine)`

### 使用相关对象
- 当关系被建立好后, 新建立一个对象, 其相关的对象也会被创建(在User表中插入一行后, 其相关的adress对象也能被访问)--------------no
- 相关的对象以collection type类型出现(默认是python list), [可以自定义](https://docs.sqlalchemy.org/en/14/orm/collections.html#custom-collections)
- 可以直接在user对象上添加Address对象
- 在双向关系中, 一方添加的元素会自动在另一方向上可见(), 这种行为基于属性的on-change事件发生, 并且是在python中计算, 并不需要SQL 
```python
>>> jack.addresses[1]
<Address(email_address='j25@yahoo.com')>
>>> jack.addresses[1].user
<User(name='jack', fullname='Jack Bean', nickname='gjffdd')>
```
- 在数据库中添加jack然后commit, jack以及相应address集合中的两个Address成员也同时被添加到session中, 这种过程称为**级联**
- 当查询jack时, 只会得到jack, 不会有address相关的SQL; 当查看jack时, 可以观察到有突然issue的SQL, 这就是lazy loading 的一个例子, 现在这个address collection 是加载过的,和普通list一样了, 后面会介绍一些优化加载collection的一些方法.
```python
>>> jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')
>>> jack.addresses
[]
>>> jack.addresses = [
...                 Address(email_address='jack@google.com'),
...                 Address(email_address='j25@yahoo.com')]
```

# 使用连接查询
- query.filter() 能根据两表相关的列放到一起
- query.join()实现SQL join 语法
  - 当两表之间仅有一个foreign key时, Query.join很容易连接两表, 但是如果他们之间没有外键或者有几个, 那么最好满足下面的一个form
  ```
  query.join(Address, User.id==Address.user_id)          # explicit condition
  query.join(User.addresses)                             # specify relationship from left to right
  query.join(Address, User.addresses)                    # same, with explicit target
  query.join(User.addresses.and_(Address.name != 'foo')) # use relationship + additional ON criteria
  ```
- outer join 使用Query.outerjoin()
	```
	query.outerjoin(User.addresses)   # LEFT OUTER JOIN
	```
- [Query.join认可的调用样式,以及文档](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.join)
  -  Query.join() 对于任何SQL Fluent应用程序来说，都是一种重要的使用中心方法
- 如果有多个实体, 怎么从中选择?
  - Query.join() 方法通常会从实体列表中最左边的项目开始，当 ON 子句被省略时，或者 ON 子句是一个普通的 SQL 表达式。 要控制 JOIN 列表中的第一个实体，请使用 Query.select_from() 方法：
  `query = session.query(User, Address).select_from(Address).join(User)`

### 使用别名 
- 当查询跨越多个表时, 如果表需要被引用多次, SQL往往需要这个表被命名为其他的名字, 以便于能和其他引用此表的做出区别?命名难道是同一个表有些地方命名,有些地方不命名?
- 例子: 连接address两次, 查找同时有两个email地址的user
- 除了通过上面用的PropComparator.of_type方法, 还可以通过Query.join()方法连接到具体的目标 通过单独的indicate

### 使用子查询
- Query适合生成用于子查询的SQL
- 例子: load user对象以及其拥有每个user拥有address的个数; 最好的办法是先得到address以user.id排序的个数,然后连接父表.
```
SELECT users.*, adr_count.address_count FROM users LEFT OUTER JOIN
    (SELECT user_id, count(*) AS address_count
        FROM addresses GROUP BY user_id) AS adr_count
    ON users.id=adr_count.user_id
```
- 通从内到外生成上面的SQL. statement accessor通过一个特殊的Query生成SQL并返回, 这个Query是select()构造的一个实例, [详见-没必要看](https://docs.sqlalchemy.org/en/14/core/tutorial.html)
```
>>> from sqlalchemy.sql import func
>>> stmt = session.query(Address.user_id, func.count('*').\
...         label('address_count')).\
...         group_by(Address.user_id).subquery()
```
- 上面的func() 是代表SQL中的函数(如count()), Query 上的 subquery() 方法生成一个 SQL 表达式构造，表示嵌入在alias中的 SELECT 语句
- 语句创建完成后, 它就可以像访问一个表一样来访问, 其中的列可以通过c来访问(stmt.c代表所有的列, stmt.c.address_count 代表其中的address_count类)
```
for u, count in session.query(User, stmt.c.address_count).outerjoin(stmt, user.id==stmt.c.user_id).order_by(User.id):
	print(u, count)
```

### 从子查询中选择实体
- 上面的例子仅仅从子查询中得到了一个 包含一列的结果, 如何将这个结果映射到一个实体呢? 可以使用aliased()去把一个被映射的类即alias 关联到一个子查询
```
>>> stmt = session.query(Address).\
...                 filter(Address.email_address != 'j25@yahoo.com').\
...                 subquery()
>>> addr_alias = aliased(Address, stmt)
>>> for user, address in session.query(User, addr_alias).\
...         join(addr_alias, User.addresses):
...     print(user)
...     print(address)
```

### Exists
- 在SQL中, Exists 是一个布尔运算符, 这个运算符返回True如果表达式的结果包含任何行, 它可以在许多场景中代替join，也可以用于定位相关表中(是否)存在相应行的行
- 显式的exists构造
```
>>> from sqlalchemy.sql import exists
>>> stmt = exists().where(Address.user_id==User.id)
>>> for name, in session.query(User.name).filter(stmt):
...     print(name)
# SQL
select user.name as users_name from users
where exist(select * from addresses where address.user.id=user.id)
```
- Query 还有多个可以自动使用exists的运算符, 上面的语句也可以通过在User.address上通过comparator.any()方法实现.
```
>>> for name, in session.query(User.name).\
...         filter(User.addresses.any()):
...     print(name)
```
- 上面的comparator.any()也可以接受约束
```
>>> for name, in session.query(User.name).\
...     filter(User.addresses.any(Address.email_address.like('%google%'))):
...     print(name)
# SQL
SELECT users.name AS users_name FROM users
WHERE EXISTS (SELECT 1 FROM addresses WHERE users.id = addresses.user_id AND addresses. email_address LIKE ?) [...] ('%google%',)
```
- 对于多对一关系, comparator.has() 等同于 comparator.any() **~代表NOT**
```
>>> session.query(Address).filter(~Address.user.has(User.name=='jack')).all()
```

### 常见的关系运算符
- 列举了所有的关系操作符, 每一个都有其API文档
```
comparator.__eq__(介绍的是eq的作用) 
```

# eager loading(急加载)
回想下前面介绍的懒加载. 如果我们想要减少查询的数量(在许多情况下，很大程度上), 我们就可以应用eager load到查询操作.SQLAlchemy提供了三种类型的紧急加载，其中两种是自动的，第三种涉及自定义条件. 这三种方法通常都是通过名为query options的函数调用. 这些函数通过 Query.options() 方法向 Query 提供关于我们希望如何加载各种属性的附加指令。

### selectinload
- 立即加载一组对象以及相关集合时好的选择
- 会发出两个select语句, 第二个select是用来完全加载与第一次加载出来的结果关联的集合
- 被称为selectin,是因为select使用In子句来一次定位多个对象的相关行.
- 举例: 加载同一个用户的address
```
>>> from sqlalchemy.orm import selectinload
>>> jack = session.query(User).options(selectinload(User.addresses)).filter_by(name='jack').one()
# SQL 查询了user和user关联的addr, 查询关联的addr是通过...
select users.id, users.name, users.fullname, users.nickname from users where users.name=?("jack");
select addr.user_id, ... from addr where addr.user_id in ? order by addr.id [...] (5,);
```

### joinedload
- joinedload是另外一个更广为人知的 自动急装函数. 默认join的方式是left outer join, 以便于主要对象和相关对象能一次加载出来.
- 举例: 和上面一个例子一样 注意即使jack的address已经加载, query仍然会发出额外的join
```
>>> from sqlalchemy.orm import joinedload
>>> jack = session.query(User).\
...                        options(joinedload(User.addresses)).\
...                        filter_by(name='jack').one()
>>> jack
<User(name='jack', fullname='Jack Bean', nickname='gjffdd')>
>>> jack.addresses
[<Address(email_address='jack@google.com')>, <Address(email_address='j25@yahoo.com')>]
# SQL select * from user left outer join addr on user.id=addr.id where user.name = xxx order by addr.id
```
- Query 应用 "唯一" 策略, 基于对象标识符, 来返回实体. 所以上面即使外连接产生了两行, 但仍然只有一个user实体返回. 这特别是为了joined eagerloading 使用时不受查询结果影响
- selectinload 是一种较新的eager load形式, 倾向于加载相关的集合; joinedload更适合多对一关系, 这是由于事实上只有一行关于主表和相关表的对象被返回;
- 也存在另外一种加载格式 suberyload, 当在某些后端使用复合主键时，它可以代替 selectinload() 使用。
- ##### joinedload() 不是join的替代
  - 通过joinedload()匿名创建出来的连接, 它不影响这个查询结果. order_by 或者 filter()使用中不能引用这些被命别名的表(也被称为用户空间, 是通过query.join构造出来的). 这样做的基本原理是，joinedload() 仅用于影响相关对象或集合作为优化细节加载的方式 - 可以添加或删除它而不影响实际结果。
  - [更多请参照joined eagerloading 之禅](https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html#zen-of-eager-loading)
### Explicit join + Eagerload
- 第三种急装的方式: 当我们显示的构造join为了定位主要的行, 并且还想要将额外的表用于主表相关的对象的上时. 这个功能通过contains_eager()提供支持, 并且对那种在一个查询里既需要过滤相同的对象,又需要预加载多对一对象时尤其有用
- 例子: 加载address和相关的user 对象, 过滤出来名为jack的user, 并且使用contains_eager() 将 user这个列映射到addr.user属性(意思是使用这个函数为addr添加user属性)
```
>>> from sqlalchemy.orm import contains_eager
>>> jacks_addresses = session.query(Address).\
...                             join(Address.user).\
...                             filter(User.name=='jack').\
...                             options(contains_eager(Address.user)).\
...                             all()
>>> jacks_addresses
[<Address(email_address='jack@google.com')>, <Address(email_address='j25@yahoo.com')>]

>>> jacks_addresses[0].user
<User(name='jack', fullname='Jack Bean', nickname='gjffdd')>
# SQL SELECT * FROM addresses JOIN users ON users.id = addresses.user_id WHERE users.name = ?
[...] ('jack',)
```
### 有关急装的信息, 包括如何配置各种默认的加载形式, 查看 [Relationship Loading Techniques](https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html)

# 删除
- 例子: 删除jack, 然后进行count query 得到0, 然后发现jack的addr对象还存在. 分析提交的SQL, 原来是每个addr对象的只是把其中user_id列置空, 行并没有删除; SQLAlchemy并不假设删除级联, 必须告诉它才能让他删除

### 配置删除/孤儿删除 级联
- 在user address关系上配置cascade 选项去改变这个删除时的行为. 虽然SQLALchemy允许你去添加新属性和关系在任何时间, 但此时这种情况需要移除关系, 
- 例子: 完全删除关系, 先关闭session; 重新声明
```
>>> session.close
ROLLBACK
>>> BASE = declartive_base()
# 重新声明User类, 添加addr关系, 其中包括级联配置
略
# 重新创建Address, 注意这种情况下已经通过User创建过了Addr.user关系
略
# 然后通过Query.get()获取jack obj, 从其相应的collection中移除一个addr obj, 然后这个obj会被删除.
```
- 为什么通过del 移除, 就能实际删除这个obj? --------------------no
##### 参考 
- 级联的细节和配置: https://docs.sqlalchemy.org/en/14/orm/cascades.html#unitofwork-cascades
- 级联功能能被顺畅的结合到关系数据库的ON/Delete/Cascade功能上: https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes

# 建立多对多关系
- 会假如一些其他的功能
- 例子: 写一个博客, 用户能写BlogPost item, 有Keyword和其关联
- 创建一个简单的多对多, 我们需要从创建一个未被映射的Table来作为相关表
```
>>> from sqlalchemy import Table, Text
>>> # association table
>>> post_keywords = Table('post_keywords', Base.metadata,
...     Column('post_id', ForeignKey('posts.id'), primary_key=True),
...     Column('keyword_id', ForeignKey('keywords.id'), primary_key=True)
... )
```
- 比起直接声明一个映射类来声明表的方式, 上面直接声明一个表. Table是一个构造函数, 所以每个column参数是被一个逗号分割, Column 对象也有明确的名称，而不是从指定的属性名称中获取。
- 定义BlogPost/ Keyword; 双方都使用relationship()构造,每个构造都将 post_keywords 表称为关联表
```
# 声明code 略
注意这个init 是可选的当使用 Declarative时
```
- 上面定义的多对多关系是BlogPost.keywords
- 定义多对多关系的特点是名为secondary的关键字参数, 它引用了标识关联表的Table obj. 这个表只有标识关系两端的两个列, 如果还有其他的列比如自己的主键, 或者其他表的外键, SQLAlchemy需要一个不同的使用模式: [association obj](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#association-pattern)
- 例子, 怎么再向里面添加关系, 比如给BlogPost添加author. 需要添加另外一个双向关系, 不过这样会有一个问题:一个单独的用户可能会有多个blog post.(-------------------no 为什么这是一个问题?) 并且 当访问User.posts时, 想要能够过滤结果, 以免加载整个集合, 需要在releation(lazy="dynamic"), 会在这个属性上使用不一样的加载策略
```
# 添加一个关系
# 创建新表
# 用法和之前的没有很大区别, 添加一些item
# 这是干什么? ------------no
# 使用any操作定位 keywords 字段是firstpost属性的blog posts
# 查找user是wendy的posts, 让query缩小范围到user是父对象的.
# 或者可以使用Wendy的post关系, 这是一个dynamic关系, 来直接从这里查询
```

# 名词
- Once we have our statement, it behaves like a Table construct
  - 意思是这个语句可以被当成一个表来使用
- Query 对象是 查询返回的结果如Query.count()方法的正确调用方式是
```python
>>> session.query(User).filter(User.name.like('%ed')).count()
2
```
- 级联
- lazy loading(延迟加载) 与 eager loading(急装)
  - 