### 初始表
```py
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine(app_config.SQLALCHEMY_DATABASE_URI, **app_config.SQLALCHEMY_ENGINE_OPTIONS)

def init_db():
    Base.metadata.create_all(engine)
# 只能新建表，不能新建数据库，没有数据库会报错
```
### 查看查询语句
```py
# 获取编译后的查询 "literal_binds": True会将查询参数的值拼接到查询语句中
compiled_query = query.statement.compile(compile_kwargs={"literal_binds": True}).__str__()
print(compiled_query)
```
# 删除
```cs
# 删除查询对象
note=Note.query.get(1)
db.session.delete(note)
db.session.commit()

# 批量删除
db.session.query(Note).filter(Note.title=='测试').delete()
session.commit()
```
# 插入 # 新增
```py
db.add(price_obj) # add后不会有id，只能commit或者flush()后才有
db.commit() 
# 使用多的值插入或更新会报错吗 会的，初始化的时候就会报错 
b=ServerClusterCreateTicketData(**new_data)
Traceback (most recent call last):
    ...
  File "c:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-wukongiaasserv\lib\site-packages\sqlalchemy\orm\decl_base.py", line 2167, in _declarative_constructor
    raise TypeError(
TypeError: 'user_name' is an invalid keyword argument for ServerClusterCreateTicketData
# 更新也会报错
ticket_data_obj.update(new_data)
Traceback (most recent call last):
    ...
  File "c:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-wukongiaasserv\lib\site-packages\sqlalchemy\sql\crud.py", line 335, in _get_crud_params
    raise exc.CompileError(
sqlalchemy.exc.CompileError: Unconsumed column names: user_name
```
# 更新
```py
# 一般更新
user_obj = db_session.query(User).filter(User.id == 179074001).update({"name":"XXX"})
#  方法二 
ticket_data_obj = self.db.query(ServerClusterCreateTicketData).filter(ServerClusterCreateTicketData.ticket_id == ticket_id)
new_data = server_cluster_patch_ticket_schema.dump(payload)
ticket_data_obj.update(new_data) # 注意ticket_data_obj是查询对象，不是ServerClusterCreateTicketData对象
new_data = server_cluster_patch_ticket_schema.dump(payload)
ticket_data_obj.update(new_data)
# 方法三 引用更新，在原有的基础上更新
res = db_session.query(Student).update({Student.student_id:Student.student_id + 10},synchronize_session=False)
# 方法四
ticket_ = self.db.query(Ticket)\
                .filter(Ticket.id == ticket_id) \
                .filter(Ticket.is_deleted == 0) \
                .first()
ticket_.current_step = -1
self.db.commit()                
```

# 查询
- filter和filter_by: https://blog.csdn.net/weixin_40123451/article/details/112577491
- 同名字段
```py
# 设置别名 当两个表中有同名字段时
self.db.query(F5VIPPoolInfo.partition, F5VIPPoolInfo.name.label("pools_name"),）
# 通过 select_from() 来明确指定字段的来源。
query = session.query(User.name, Post.id.label('post_id')) \
    .select_from(User) \
    .join(Post, User.id == Post.user_id)
```
- 分页查询
```py
query_obj = query_obj.order_by(Ticket.id.desc())
count = query_obj.count()
paginated_query = query_obj.limit(page_size).offset((page - 1) * page_size)

res = paginated_query.all()
```
- 如果查询两个表，那么每个元素是个元组，元组中是每个表对象
- all()返回结果是一个列表, 每个元素是每行的查询结果可以使用.col_name或者[0]来访问（不管是查全表还是查某些列都可以）
```
t_ids = (self.db.query(Ticket.id)
                .join(ApprovalProcesses, Ticket.process_id == ApprovalProcesses.id)
                .filter(Ticket.current_step == 3, Ticket.is_deleted == 0, 
                        ApprovalProcesses.process_name == "创建集群流程").all())
# 结果是[(289,), (297,)] 取289 必须使用res[0][0]
# 查部分字段结果是一个元组， 查一个表结果是一个对象
self.db.query(Ticket.id).filter(xxx).first()结果是一个元组(289,) 取289是res[0]
```
- 如果查询部分字段，可以通过query.all()[0]._asdict()将数据转换为字典，但是如果查询的多个表，只会转换一个表的字段到结果中（可以为另一个表中字段设置label）（不知道查询全表可不可以用这个）

### 子查询
```py
# 创建子查询别名
子查询对象可以使用.c.col_name来使用查询的列
subquery = session.query(Post.user_id, func.count(Post.id).label('post_count')) \
    .group_by(Post.user_id).alias()

# 使用别名进行查询
query = session.query(User, subquery.c.post_count) \
    .join(subquery, User.id == subquery.c.user_id)

# 执行查询
result = query.all()
```
### 使用列名
- 使用子查询中的列，不能使用StoreCluster.sku 应该使用subquery.c.sku
```py
subquery = (db.session().query(StoreCluster.id, StoreCluster.cluster_name, StoreCluster.env,
                                StoreCluster.domain, StoreCluster.tags, StoreCluster.created_at, StoreCluster.sku)
                         .filter(StoreCluster.is_deleted == 0)).subquery()
query_obj = (db.session().query(StoreInfo.cluster_id, 
                                    func.count(distinct(StoreInfo.market_city_name_cn)).label("market_count"), 
                                    func.count().label("store_count"),
                                    subquery.c)
                         .group_by(StoreInfo.cluster_id)
                         .join(subquery, StoreInfo.cluster_id == subquery.c.id)
                         .filter(StoreInfo.is_deleted == 0))
query_obj = query_obj.having(case((StoreCluster.sku == "5+3", func.round(func.count()/256*100, 1)),
                                    (StoreCluster.sku == "9+6", func.round(func.count()/512*100, 1)),
                                    else_=func.round(func.count() * 100.0 / STANDARD_CAP, 1)
                                    ) > value)
```
### sqlalchemy one first scalar区别
- link:https://blog.csdn.net/u012089823/article/details/94650310
- scalar()多个结果会抛出异常 没有结果不会抛出异常
  
### 拼接查询对象
```py
filter_condition = User.age.between(25, 35)

# 使用filter_condition拼接到查询对象上
query = session.query(User).filter(User.name.like('A%')).filter(filter_condition)
```

### filter和filter_by的区别
- `filter`方法则更加灵活，可以处理更复杂的条件，包括使用运算符、函数和逻辑运算符； 
- filter_by() 只能筛选条件等于，不支持 大于 (>)和小于 (<)和 and_、or_查询
- filter不支持组合查询，只能连续调用filter来变相实现。而filter_by的参数是**kwargs，直接支持组合查询。
- filter用类名.属性名，比较用==，filter_by直接用属性名，比较用=
```py
session.query(Students).filter_by(name='yoyo', age=20).all()
q = sess.query(IS).filter_by(node=node, password=password).all()

```
- like 
```py
#  ~ 操作符是 SQLAlchemy 中的“非”操作符，它用来取反一个条件。所以 
# "except%"：这是一个字符串模式，% 是一个通配符，表示任意数量的任意字符。所以 "except%" 匹配任何以 "except" 开头的字符串。
query.filter(~ServerLDAP.store_name.like("except%"))
self.db.query(User.id, User.username).filter(User.username.like(f"%{op_user}%")).all()
# 注意如果op_user为None的时候 生成的SQL是select id, username where username like %None%;
```
- filter() 和 filter(None)是不一样的
```py
# filter(None) 会查不出来结果
WHERE ticket.is_deleted = 0 AND server_config_release_ticket_data.is_deleted = 0 AND server_config_release_data.is_deleted = 0 AND server_config_release_data.is_activate = 1 AND NULL
# filter()
WHERE ticket.is_deleted = 0 AND server_config_release_ticket_data.is_deleted = 0 AND server_config_release_data.is_deleted = 0 AND server_config_release_data.is_activate = 1
```


### join()
```py
# query 中参数的顺序很重要，第一个参数所代表的 table 就是 JOIN 时放在前面的那个 table。因此，此处 JOIN 的目标应该是 Account， 而不应该是 Bind 自身。
query_obj = (self.db.query(Ticket, ServerConfigReleaseTicketData, ServerConfigReleaseData)
                .filter(Ticket.is_deleted == 0).filter(ServerConfigReleaseTicketData.is_deleted == 0)
                .filter(ServerConfigReleaseData.is_deleted == 0).filter(ServerConfigReleaseData.is_activate == 1)
                .join(ServerConfigReleaseTicketData, ServerConfigReleaseTicketData.ticket_id == Ticket.id)
                .join(ServerConfigReleaseData, ServerConfigReleaseData.ticket_id == Ticket.id))
# 内连接
query = session.query(Parent).join(Child, Parent.id == Child.parent_id)

# 执行左连接查询
query = session.query(Parent).join(Child, Parent.id == Child.parent_id, isouter=True)
query = session.query(Parent).outerjoin(Child, Parent.id == Child.parent_id)

# 连接子查询
child_subquery = session.query(Child.id).filter(Child.parent_id == Parent.id).subquery()
# 使用子查询进行left JOIN
query = session.query(Parent).outerjoin(child_subquery, Parent.id == child_subquery.c.id)
```

### 查看未提交的修改
```py
session.new  # ：包含自上次提交以来添加到会话但尚未提交的所有对象。
session.dirty  #：包含自上次提交以来被修改的所有对象。
session.deleted  #：包含自上次提交以来被删除的所有对象。
```

### 去重
```py
# 单列去重
session.query(func.count(distinct(User.name))).scalar()
# 多列去重
session.query(Sites.site, Sites.aws_sku).distinct(Sites.site, Sites.aws_sku).all()
```
### 分组
```py
env_res = db.session().query(StoreCluster.env).filter(StoreCluster.is_deleted == 0).group_by(StoreCluster.env).all()
>  [('test',), ('dev',)]   
```

### having
```py
query = session.query(Post.user_id, func.count(Post.id).label('post_count')) \
    .group_by(Post.user_id) \
    .having(func.count(Post.id) > 5)  # 使用 having 过滤出帖子数大于 5 的用户
```

### 排序 
```py
# 正序
version_list = db.query(module.version).group_by(module.version).order_by("version").all() # 使用表中的字段名
version_list = db.query(module.version).group_by(module.version).order_by(module.version).all() # 使用模型属性
# 倒序
version_list = db.query(module.version).group_by(module.version).order_by(module.version.desc()).all()
# 根据其他列排序 根据重命名列
>>> stmt = (
...     select(Address.user_id, func.count(Address.id).label("num_addresses"))
...     .group_by("user_id")
...     .order_by("user_id", desc("num_addresses"))
... )

```

### 函数
```py
from sqlalchemy.sql import func
from sqlalchemy import func, or_
session.query(func.max(Article.read_num).scalar()
# 计数
db.session().query(StoreInfo.cluster_id, func.count(distinct(StoreInfo.market_city_name_cn)), func.count()).group_by(StoreInfo.cluster_id).all()
# 去空格
user_info = (self.db.query(User)
                    .filter(or_(func.trim(User.username) == name, User.user_code  == code)).scalar())
```

# 其他
### 执行顺序
```py
# 一下两个查询的sql语句是一样的
query_obj = (self.db.query(Ticket, ServerConfigReleaseTicketData, ServerConfigReleaseData)
                .filter(Ticket.is_deleted == 0).filter(ServerConfigReleaseTicketData.is_deleted == 0)
                .filter(ServerConfigReleaseData.is_deleted == 0).filter(ServerConfigReleaseData.is_activate == 1)
                .join(ServerConfigReleaseTicketData, ServerConfigReleaseTicketData.ticket_id == Ticket.id)
                .join(ServerConfigReleaseData, ServerConfigReleaseData.ticket_id == Ticket.id))
query_obj2 = (self.db.query(Ticket, ServerConfigReleaseTicketData, ServerConfigReleaseData)
                .join(ServerConfigReleaseTicketData, ServerConfigReleaseTicketData.ticket_id == Ticket.id)
                .join(ServerConfigReleaseData, ServerConfigReleaseData.ticket_id == Ticket.id)
                .filter(Ticket.is_deleted == 0).filter(ServerConfigReleaseTicketData.is_deleted == 0)
                .filter(ServerConfigReleaseData.is_deleted == 0).filter(ServerConfigReleaseData.is_activate == 1))
```


# 模型
### default字段和server_default字段
- link: https://blog.csdn.net/daletxt/article/details/123502457

- default的值是一个pyton表达式， SQLAlchemy的Python程序，打印出SQL语句的话，相当于向数据库表中该字段插入了default表达式的值值；（参考图中所有设置了default值的字段：int_default、bool_default、time_default、time_both_default，最终入库值均为default表达式的值，并且在insert的sql语句中均有体现）
- 而设置了server_default则走MySQL表结构中设置的DEFAULT值，打印SQL语句的话，相当于插入时没有插入该字段；（参考图中bool_server_default，值为0，对应insert的sql语句中没有该字段，time_server_default值为数据库默认的本地时间16:07）
- default与server_default同时设置时，default优先级高于server_default。（参考图中time_both_default字段，该字段生效的是default的utc日期字段，即表中数据为8:07，而不是数据库中默认的本地时间即16:07）

### 批量插入性能
- https://blog.csdn.net/tangsiqi130/article/details/131090117
### python sqlalchemy db.session 的commit()和colse()对session中的对象的影响
- https://blog.csdn.net/yuxuan89814/article/details/132597739
- 
# sqlalchemy 为什么读不到已经插入的数据，再次重启一次flask就能读取到了呢

# 创建所有表
```py
from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # 配置数据库URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁用修改监控

db.init_app(app) 
with app.app_context():
    db.create_all() 
```
