# 安装和配置
## 验证是否安装
    - 需要先切到root用户下，反正是有些用户不能用
    - 输入rabbitmqctl 看有没有反应
    - 输入rabbitmqctl status 看是否启动
    - 查看版本`sudo rabbitmqctl status | grep rabbit # 结果{rabbit,"RabbitMQ","3.7.3"}`
## 安装
- link：
    - https://www.cnblogs.com/jimlau/p/12029985.html
    - https://www.cnblogs.com/web424/p/6761153.html
- 安装erlang
    - 由于RabbitMQ是基于Erlang（面向高并发的语言）语言开发，所以在安装RabbitMQ之前，需要先安装Erlang. Erlang在默认的YUM存储库中不可用，因此您将需要安装EPEL存储库
    - 检查erlang是否安装`erl -version`
    - 如果未安装
    ```
    yum -y install epel-release
    yum -y install erlang socat
    ```
- 安装RabbitMQ
    - RabbitMQ为预编译并可以直接安装的企业Linux系统提供RPM软件包。 唯一需要的依赖是将Erlang安装到系统中
    - 下载RabbitMQ `wget https://repo.huaweicloud.com/rabbitmq-server/v3.5.0/rabbitmq-server-3.5.0-1.noarch.rpm`
    - 通过运行导入GPG密钥：`rpm –import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc`
    - 运行RPM安装RPM包：`rpm -Uvh rabbitmq-server-3.6.10-1.el7.noarch.rpm`
    - 查看运行状态 `service rabbitmq-server status`
## 配置
- 启动 `systemctl start rabbitmq-server`
- 开机自启 `systemctl enable rabbitmq-server`
# 帮助
    - rabbitmqctl -h
# 管理
- 需要创一个RabbitMQ账户：
    - sudo rabbitmqctl add_user myuser mypassword 
    - sudo rabbitmqctl add_vhost myvhost
    - sudo rabbitmqctl set_user_tags myuser mytag
    - sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
- 查看用户 rabbitmqctl user list_users
- rabbitmqctl status
- 启动服务 sudo rabbitmqctl-server 也可以通过添加 -detached 参数在后台运行
- 永远不要通过 kill 命令来进行停止 RabbitMQ 运行，使用 rabbitmqctl 命令来进行停止 RabbitMQ ：rabbitmqctl stop
# 152
- 用户 broker_url="amqp://guest1:guest@90.90.0.152:5672//