#### 介绍
The Python SQL Toolkit and Object Relational Mapper
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.
- SQLAlchemy Object Relational Mapper 提供了一种将用户定义的Python类与数据库 以及 这些类的实例与相应表中的行关联起来的方法。 它包括一个透明的同步对象及其相关行之间状态的所有更改的系统：Unit of work，以及用户定义的类及其相互之间定义的关系表示数据库查询的系统（查询）
#### 版本 1.x 2.0 
This tutorial covers the well known SQLAlchemy ORM API that has been in use for many years. As of SQLAlchemy 1.4, there are two distinct styles of ORM use known as 1.x style and 2.0 style, the latter of which makes a wide range of changes most prominently around how ORM queries are constructed and executed.

#### links
- [doc]: https://www.osgeo.cn/sqlalchemy/orm/tutorial.html **教程好像是1.4的**

#### 使用
##### 问题
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
  


##### 连接
- echo 参数 能看到生成的所有SQL
- 使用ORM时，我们通常不使用 Engine 直接创建；相反，它被ORM在幕后使用，稍后我们将看到。
- 惰性链接， 创建时虽然有返回，但并未实际尝试链接到数据库，而是在第一次要求它对数据库执行任务时发生
- [不同的数据库url](https://www.osgeo.cn/sqlalchemy/core/engines.html#database-urls)
##### 声明映射
- "使用ORM时，配置过程首先描述将要处理的数据库表，然后定义 将映射到这些表 的自己的类" 这个类不是指我们所定义的类吧?
- 当我们的类被构造时，Declarative使用descriptors替换了Column；这种行为被称为 instrumentation . “instructed”映射类将为我们提供 在SQL上下文中引用表 以及 从数据库中持久化和加载列值 的方法。
  
##### 创建一个模式
- 上面的User类通过Declarative system 被构造, 通过User, 我们定义了关于我们表的信息,这些信息被称为table metadata. 这个object被 SQLAlchemy 用来表示一个特殊表的信息, 这个表被称为Table object, 并且here Declarative 已经为我们搞了一个. 我们可以查看这个object 通过`User.__table__`
- 当我们声明User时, Declartive 使用Python metaclass来完成声明, 为了在类声明完成后执行额外的activities, 他(Declartive)然后创建 Table object 根据我们的规则, 并且通过构造一个mapping object关联他(Declartive?).这个对象是一个我们通常不需要直接处理的幕后对象（尽管它可以在我们需要的时候提供关于我们的映射的大量信息）
- Table object 是 MetaData的成员, 后者有一个更大的collection, 当使用Declartive时, 可以通过 声明性基类(Base) 的metadata属性去访问
- 这个 MetaData 是一个 registry 其中包括向数据库发出一组有限的模式生成命令的能力。用 MetaData 为尚未存在的所有表向数据库发出create table语句
- ###### 经典映射
  - 尽管强烈建议使用声明性系统，但使用sqlacalchemy的ORM不需要声明性系统
  - 不通过Declartive, 任何普通的类都一一映射到Table使用mapper(), 这种用法称为经典映射
- ###### 最小表描述vs完整描述
  - 面对不同的数据库, 在类似于create table 这种语句构造上的区别,及解决办法
  - 熟悉create table语法的用户可能会注意到上面生成的SQL中varchar列的生成没有长度；在sqlite和postgresql上，这是一个有效的数据类型，但在其他数据类型上，这是不允许的

##### 创建映射类的实例
- 即使在下面的语句中,我们并没有指定id的值, 当我们访问id的时候仍然能得到一个None,而不是python抛出一个Attribute 异常. SQLAlchemy`s instrumention 一般在第一次被访问时produces被映射的属性的默认值. 对于那些实际上指定了一个值的属性, instrumenttation 系统会跟踪这些值为了在最终的INSERT 语句发出到database的时候使用
- ###### 使用Declartive 系统定义的类已经提供了一个构造函数,能自动接受与映射的列匹配的关键字的名字, 如果重新定义,原有的会覆盖

##### 创建Session
- Session 是会话对象, 是ORM操作database的句柄, 在create_engine同样的等级, 创建一个Session类
- 如果没有create_engine时, 可以先穿件Session类,然后使用` Session.configure(bind=engine)`去连接Session
- ###### Session的生命周期
  - (何时构造一个Session, 何时提交Session, 何时关闭?)[https://www.osgeo.cn/sqlalchemy/orm/session_basics.html#session-faq-whentocreate]
  - 很大部分取决于要build的应用的类型,
  - Session是对像的局部工作空间, 特定数据库连接的本地工作区
- session 创建出来时和engine联系在一起,但并没有打开任何连接, 当第一次被使用时,会从engine维护的连接池中取出一个连接, 并且保持这个链接直到提交所有改变或者关闭这个链接
     0
##### Adding and Updating Objects
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

##### 回滚
- 使用session.rollback()
- 只有这一种使用方法吗? ---------------------------no
- 只能回滚当前事务中的吗? 提交后的会话中能回滚吗 ----------------------no
  
##### 查询
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