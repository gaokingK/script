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