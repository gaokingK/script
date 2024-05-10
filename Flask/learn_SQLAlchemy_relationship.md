# link
- https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html

# 简述
一对一：
一对多：在建表的时候将1端主键置于多端即可。
多对多：对于多对多关系，需要转换成1对多关系，那么就需要一张中间表来转换
```
# 下面各种关系需要的import
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```
# One To Many
父亲和儿子的关系是一对多（一个父亲有多个儿子），儿子和父亲的关系是多对一（多个儿子有一个父亲）
```
# 一个父亲有多个儿子
# 1. 把1端的主键作为外键放到多端表中
# 2. 在多端中指定releation("Child"), 来体现该条数据对应的多条多端数据 
# 注意命名
    - 类名、表名、releation()中的名、多端和1端新增数据的名、ForeignKey()中的名称
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
```

# backref的作用
- link: https://www.cnblogs.com/liangmingshen/p/9769975.html
- backref 对关系提供反向引用的声明

# secondary
- link：https://www.cnblogs.com/MilletChili/p/9177298.html
- 用来生成多对多映射的

# passive_deletes
- link：https://www.cnblogs.com/kirito-c/p/10900024.html

# lazy
- https://blog.csdn.net/bestallen/article/details/52601457
- 对某个有关系的列，在搜索这一行时，其相关的数据是否被加载的策略
