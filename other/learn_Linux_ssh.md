1. #### ssh 连接上去的默认路径是默认用户/或者连接使用的用户的默认～ 执行命令也是
1. ### Linux之间配置SSH互信（SSH免密码登录）
[lind](https://blog.csdn.net/linxc008/article/details/81278446)
将已经生成的公钥私钥对id_rsa.pub发送到其他的服务器上。
```shell
# 命令
ssh-copy-id -i /root/.ssh/id_rsa.pub 192.168.137.129
# 或者手动
ssh root@web-2 cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
```
2. ### 禁止root ssh [link](https://www.cnblogs.com/toughlife/p/5633510.html)
```
vim /etc/ssh/sshd**
service sshd restart
```
1. #### [linux-ssh远程后台执行脚本-放置后台执行问题](https://www.cnblogs.com/vijayfly/p/6264744.html) --------------------------no
- ssh user@ip "command" （多个命令需要用括号包括，防止后面的命令在本地执行？）
- 执行需要交互的命令 -t
  - 因为不加-t 不会分配终端（除非ssh user@ip），命令执行完就退出了，会提示“no tty ...”
  - -t 会让会话得到tty， 并保持登录状态
  - 指定多个-t有什么用？--------------------------no
  - 把命令写成多行，和本地一样单引号或者双引号包括
  - 能使用本地的变量 正常使用， 或者bash -c ，但是怎么使用远程的变量呢？-------------------------------------no
  - 执行脚本
    ```shell
    # 本地带有参数的脚本
    ssh root@ip 'base -s' < script.sh [parm1, parm2...] 
    # 执行远程的script 并传参呢
    ssh user@ip sh path/to/script [parm1, parm2...] 和正常一样
    ```