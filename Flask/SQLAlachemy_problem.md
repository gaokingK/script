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
