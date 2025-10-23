### 配置
```py
    # 这里使用mysql+pymysql而不是mysql的原因是:
    # 1. mysql是一个通用的前缀,需要指定具体的Python MySQL驱动
    # 2. pymysql是纯Python实现的MySQL驱动,不依赖MySQL-python这样的C扩展
    # 3. 如果只写mysql,SQLAlchemy会默认使用MySQL-python(MySQLdb)驱动,但该驱动:
    #    - 需要编译安装
    #    - 依赖MySQL客户端库
    #    - 不支持Python 3
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
```
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
# flush
- flush()后需要提交吗？如果回滚的话会被回滚吗
- flush() 的作用
flush() 会将当前会话中的所有挂起的 SQL 语句发送到数据库执行

它同步持久化上下文（session）与数据库，但不提交事务

主要目的是为了确保后续操作能获取到正确的数据库状态

提交与回滚的影响
需要显式提交：即使调用了 flush()，仍然需要调用 commit() 才能使更改永久生效

回滚会撤销 flush() 的更改：如果在 flush() 后调用 rollback()，所有已 flush 但未提交的更改都会被撤销
# 插入 # 新增
```py
db.add(price_obj) # add后不会有id，只能commit或者flush()后才有 commit后这个price_obj的id就不是none了
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

# 查询是否为none
query = query.filter(field_attr.is_(None))
select * FROM network_device 
WHERE network_device.is_deleted = 0 AND network_device.d_version = 'latest' AND network_device.sn IS NULL


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
- 不区分大小写
```py
db.query(self.model).filter_by(is_deleted=0, d_version=app_config.USE_DATA_VERSION)
query.filter(getattr(self.model, "owner").ilike(f"{value}"))

# SELECT * FROM network_device 
# WHERE network_device.is_deleted = 0 AND network_device.d_version = 'latest' AND lower(network_device.owner) LIKE lower('CN-jinweijiangod')

query.filter(collate(getattr(self.model, "owner"), 'utf8mb4_general_ci')==value)

# FROM virtual_machine, network_device 
# WHERE virtual_machine.is_deleted = 0 AND virtual_machine.d_version = 'latest' AND (network_device.owner COLLATE utf8mb4_general_ci) = 'CN-jinweijiangod'

```
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


self.db.query(ResourceRelationship).filter_by(relation_type="layer2_network-host").filter_by(relation_type="vpc-subnets").count()
0
self.db.query(ResourceRelationship).filter_by(relation_type="layer2_network-host").count()
2620
a=self.db.query(ResourceRelationship).filter_by(relation_type="layer2_network-host").filter_by(relation_type="vpc-subnets")
print(a.statement.compile(compile_kwargs={"literal_binds": True}).__str__())
SELECT resource_relationship.relation_type, resource_relationship.source_uid, resource_relationship.target_uid, resource_relationship.source_type, resource_relationship.target_type, resource_relationship.d_version, resource_relationship.id, resource_relationship.created_at, resource_relationship.updated_at, resource_relationship.is_deleted 
FROM resource_relationship 
WHERE resource_relationship.relation_type = 'layer2_network-host' AND resource_relationship.relation_type = 'vpc-subnets'
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
# 多个条件连接
from sqlalchemy import and_
result = session.query(User, Order).join(
    Order,
    and_(
        User.id == Order.user_id,
        User.status == 'active',
        Order.amount > 100
    )
).all()
# select ... from tbl_a join tbl_b on cond1 and cond2 ...
# 不可以使用func.and_ 语句会变成 select ... from tbl_a join tbl_b on and(cond1 , cond2) ... 会报错
```
### func.and_和 from sqlalchemy import and_的区别
方式	    导入方式	                        适用场景	                推荐度
and_	   from sqlalchemy import and_	    标准的 SQL 逻辑 AND	        ✅ 推荐
func.and_	from sqlalchemy import func	  也能用，但语义上不太准确	        ❌ 不推荐
更 Pythonic 的写法 实际上，SQLAlchemy 支持直接用 & 运算符代替 and_：
```py
query = session.query(User).filter(
    (User.age >= 18) & (User.status == 'active')
)
# 更简洁，和 Python 逻辑运算一致。
# 但要注意 必须加括号，因为 & 优先级问题。
```
### 查看未提交的修改
```py
session.new  # ：包含自上次提交以来添加到会话但尚未提交的所有对象。
session.dirty  #：包含自上次提交以来被修改的所有对象。
session.deleted  #：包含自上次提交以来被删除的所有对象。
# 使用db.session.rollback()可以清空未提交的更改
db.dirty
IdentitySet([])
db.new
IdentitySet([<app.models.access_log.AccessRecordData object at 0x00000295780A3A30>, <app.models.access_log.AccessRecordData object at 0x00000295790F47C0>])
db.rollback()
db.new
IdentitySet([])

# 注意bulk_insert_mappings 不会创建 ORM 对象，不会出现在 .new 中
# 数据未提交，对其他连接不可见，包括新开的 session
# 只有在当前 session 中查询	✅ 可行！	当前 session 能看到自己的未提交变更，只要你用同一个 session 查询
res = session.query(ResourceRelationship).filter(...).all()
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
pm_group_dos = query.order_by(desc(func.count(PhysicalMachine.id).label("count"))).limit(50).all()
# 根据其他列排序 根据重命名列
>>> stmt = (
...     select(Address.user_id, func.count(Address.id).label("num_addresses"))
...     .group_by("user_id")
...     .order_by("user_id", desc("num_addresses"))
... )

# 有子查询的话可能会改变排序结果
sub_query = query_obj.subquery()
query_obj = calc_cluster_data(sub_query)
if filter_cond.get("utilization"):
    query_obj = map_utilization_filter(filter_cond.get("utilization"), query_obj, sub_query)
count = query_obj.count()
query_obj = query_obj.order_by(StoreCluster.updated_at.desc())
# 对应的sql为 结果按updated_at排序
SELECT count(DISTINCT store_info.market_city_name_cn) AS market_count, count(store_info.cluster_id) AS store_count, anon_1.id, anon_1.cluster_name, anon_1.env, anon_1.domain, anon_1.tags, anon_1.created_at, anon_1.sku, anon_1.rancher_cluster_id, anon_1.k8s_ip, anon_1.ob_ip, anon_1.ob_vip, anon_1.updated_at, anon_1.ob_user_name, anon_1.lb_id, anon_1.ingress_ip 
FROM (SELECT store_cluster.id AS id, store_cluster.cluster_name AS cluster_name, store_cluster.env AS env, store_cluster.domain AS domain, store_cluster.tags AS tags, store_cluster.created_at AS created_at, store_cluster.sku AS sku, store_cluster.rancher_cluster_id AS rancher_cluster_id, store_cluster.k8s_ip AS k8s_ip, store_cluster.ob_ip AS ob_ip, store_cluster.ob_vip AS ob_vip, store_cluster.updated_at AS updated_at, store_cluster.ob_user_name AS ob_user_name, store_cluster.lb_id AS lb_id, store_cluster.ingress_ip AS ingress_ip 
FROM store_cluster 
WHERE store_cluster.is_deleted = 0 ORDER BY store_cluster.updated_at DESC) AS anon_1 LEFT OUTER JOIN store_info ON store_info.cluster_id = anon_1.id AND store_info.is_deleted = 0 GROUP BY anon_1.id ORDER BY store_cluster.updated_at DESC

query_obj = query_obj.order_by(StoreCluster.updated_at.desc())
sub_query = query_obj.subquery()
query_obj = calc_cluster_data(sub_query)
if filter_cond.get("utilization"):
    query_obj = map_utilization_filter(filter_cond.get("utilization"), query_obj, sub_query)
count = query_obj.count()
# 对应的sql为 结果没有按updated_at排序
SELECT count(DISTINCT store_info.market_city_name_cn) AS market_count, count(store_info.cluster_id) AS store_count, anon_1.id, anon_1.cluster_name, anon_1.env, anon_1.domain, anon_1.tags, anon_1.created_at, anon_1.sku, anon_1.rancher_cluster_id, anon_1.k8s_ip, anon_1.ob_ip, anon_1.ob_vip, anon_1.updated_at, anon_1.ob_user_name, anon_1.lb_id, anon_1.ingress_ip 
FROM (SELECT store_cluster.id AS id, store_cluster.cluster_name AS cluster_name, store_cluster.env AS env, store_cluster.domain AS domain, store_cluster.tags AS tags, store_cluster.created_at AS created_at, store_cluster.sku AS sku, store_cluster.rancher_cluster_id AS rancher_cluster_id, store_cluster.k8s_ip AS k8s_ip, store_cluster.ob_ip AS ob_ip, store_cluster.ob_vip AS ob_vip, store_cluster.updated_at AS updated_at, store_cluster.ob_user_name AS ob_user_name, store_cluster.lb_id AS lb_id, store_cluster.ingress_ip AS ingress_ip 
FROM store_cluster 
WHERE store_cluster.is_deleted = 0 ORDER BY store_cluster.updated_at DESC) AS anon_1 LEFT OUTER JOIN store_info ON store_info.cluster_id = anon_1.id AND store_info.is_deleted = 0 GROUP BY anon_1.id
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

                    
self.db.query(ResourceRelationship).filter(ResourceRelationship.relation_type.in_(["layer2_network-host", "vpc-subnets"])).count()
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

# 这种也是一致的
query_data = (db.query(ResourceRelationship.relation_type, target_model)
                .join(target_model, and_(target_model.resource_uid==ResourceRelationship.target_uid, ResourceRelationship.relation_type==f"{source_model.__tablename__}-{target_model.__tablename__}"))
                .filter(ResourceRelationship.source_uid==source_id)
                .filter(ResourceRelationship.d_version==app_config.USE_DATA_VERSION)
                .filter(ResourceRelationship.is_deleted==0)
                .filter(target_model.is_deleted==0)
                .all())
query_data = (db.query(ResourceRelationship.relation_type, target_model)
                .join(target_model, target_model.resource_uid==ResourceRelationship.target_uid)
                .filter(ResourceRelationship.source_uid==source_id)
                .filter(ResourceRelationship.relation_type==f"{source_model.__tablename__}-{target_model.__tablename__}")
                .filter(ResourceRelationship.d_version==app_config.USE_DATA_VERSION)
                .filter(ResourceRelationship.is_deleted==0)
                .filter(target_model.is_deleted==0)
                .all())
语义上无区别：只要 .join() 后的 .filter() 不影响连接关系，两种写法结果一致。

可读性角度：推荐使用第二种方式，将连接条件与查询过滤条件分开写。

性能角度：最终会编译成类似的 SQL（SQL不一样，可能sql的编译器在编译后是一样的），不影响数据库执行计划。             
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
