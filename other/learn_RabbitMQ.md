# 安装
## 验证是否安装
# 帮助
    - rabbitmqctl -h
# 管理

- sudo rabbitmqctl add_user myuser mypassword 
- sudo rabbitmqctl add_vhost myvhost
- sudo rabbitmqctl set_user_tags myuser mytag
- sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
- 查看用户 rabbitmqctl user list_users
- rabbitmqctl status
- 
# 152
用户 