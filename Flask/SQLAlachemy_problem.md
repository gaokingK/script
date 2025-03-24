# 问题
- sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1059, "Identifier name '<bound method ? of <class 'common.model.assign_task_model.AssignTask'>>' is too long")
  - 是因为Base里指定的__tablename__在模型类里没有定义，而base里的这个字段很长

- MySQL为后端时，string字段定义要给长度，默认允许为空
- 代码中定义的默认值在使用SQL语句插入时并不适用
### 如何排序
- link： https://blog.csdn.net/aimill/article/details/80812817
```
results = session.query(User).order_by(User.create_time.desc()).all() # 按create_time字段降序排列
session.query(User).order_by("create_time").all() # 从小到大
session.query(User).order_by("-create_time").all() # 从大到小
```
- 在定义模型时声明排序方式 # sqlalchemy 1.1之后就删除了

### AttributeError: 'NoneType' object has no attribute 'read'
```
  File "c:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-cmdbserv\lib\site-packages\pymysql\connections.py", line 782, in _read_bytes
    data = self._rfile.read(num_bytes)
AttributeError: 'NoneType' object has no attribute 'read'
# session()对象为空
```

### This session is provisioning a new connection;
```
  File "c:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-cmdbserv\lib\site-packages\sqlalchemy\orm\session.py", line 990, in _raise_for_prerequisite_state
    raise sa_exc.InvalidRequestError(
sqlalchemy.exc.InvalidRequestError: This session is provisioning a new connection; concurrent operations are not permitted (Background on this error at: https://sqlalche.me/e/20/isce)
# 并发问题，两个线程的session 交换了
OverView 类使用了一个实例变量 self.db 来存储数据库会话
当多个请求并发访问时(视图函数里导入了一个service实例，每次请求都是用这个实例)，这个实例变量会被多个请求共享和覆盖，导致混乱
```
