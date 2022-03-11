# sqlalchemy 问题
- sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1059, "Identifier name '<bound method ? of <class 'common.model.assign_task_model.AssignTask'>>' is too long")
  - 是因为Base里指定的__tablename__在模型类里没有定义，而base里的这个字段很长
- MySQL为后端时，string字段定义要给长度，默认允许为空

# flask其他组件问题
- app.register_blueprint(assign_task, url_perfix="/assign_task") 能接受关键字参数，所以参数名写错也不会报错，这里url_perfix写错了就导致路由未注册成功。

### Flask如何保证线程安全
[关于flask线程安全的简单研究](https://www.cnblogs.com/fengff/p/9087660.html)
简单结论：处理应用的server并非只有一种类型，如果在实例化server的时候如果指定threaded参数就会启动一个ThreadedWSGIServer，而ThreadedWSGIServer是ThreadingMixIn和BaseWSGIServer的子类，ThreadingMixIn的实例以多线程的方式去处理每一个请求
只有在启动app的时候将threded参数设置为True，flask才会真正以多线程的方式去处理每一个请求。