# sqlalchemy 问题
- sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1059, "Identifier name '<bound method ? of <class 'common.model.assign_task_model.AssignTask'>>' is too long")
  - 是因为Base里指定的__tablename__在模型类里没有定义，而base里的这个字段很长
- MySQL为后端时，string字段定义要给长度，默认允许为空

# flask其他组件问题
- app.register_blueprint(assign_task, url_perfix="/assign_task") 能接受关键字参数，所以参数名写错也不会报错，这里url_perfix写错了就导致路由未注册成功。