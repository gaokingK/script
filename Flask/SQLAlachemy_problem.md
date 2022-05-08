### 如何排序
- link： https://blog.csdn.net/aimill/article/details/80812817
```
results = session.query(User).order_by(User.create_time.desc()).all() # 按create_time字段降序排列
session.query(User).order_by("create_time").all() # 从小到大
session.query(User).order_by("-create_time").all() # 从大到小
```
- 在定义模型时声明排序方式 # sqlalchemy 1.1之后就删除了