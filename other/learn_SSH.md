# 远程连接windows环境
### 准备
- link：https://cloud.tencent.com/developer/article/1420930
- 安装openssh 客户端、服务器
    - 管理可选功能》添加功能
    - 或者使用命令行
    ```
    # 管理员身份启动 PowerShell
    # 要确保 OpenSSH 可用于安装
    PS C:\WINDOWS\system32> Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
    Name  : OpenSSH.Client~~~~0.0.1.0
    State : Installed # 或者是 NotPresent
    
    Name  : OpenSSH.Server~~~~0.0.1.0
    State : Installed
    #使用 PowerShell 安装服务器即可：
    Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
    ```
- 安装后进行一些初始化配置
```
# 管理员权限
# 需要开启 SSHD 服务：
Start-Service sshd
# 设置服务的自动启动：
Set-Service -Name sshd -StartupType 'Automatic'
# 确认一下防火墙是否是放开的：
Get-NetFirewallRule -Name *ssh* # OpenSSH-Server-In-TCP这个状态是 enabled
```

### 问题
- [root@localhost FlaskDemo]# ssh-copy-id git@90.90.0.140
/bin/ssh-copy-id: ERROR: failed to open ID file '/root/.pub': No such file or directory
        (to install the contents of '/root/.pub' anyway, look at the -f option)
    - 是公钥没有生成， 先用ssh-keygen生成
- 连接时遇到 `ssh: connect to host 90.90.0.224 port 22: Connection refused`
    - 可能是没有安装openssh服务器 https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse?source=recommendations
    - 可能是防火墙原因
        - 确认是否放开    
        - 关闭防火墙:https://www.cnblogs.com/mihoutao/p/13254520.html

- ssh 主机的端口可能不是22,可以通过vim ~/.ssh/config来修改对某台主机进行ssh连接时使用的端口
    - https://zhuanlan.zhihu.com/p/521340971

- 遇到一个问题 A主机上ssh root@b_ip 到B，在这个终端下再ssh root@b_ip就不行

- ssh 链接问题可以看/etc/log/secury日志
    - https://blog.csdn.net/GX_1_11_real/article/details/80423409
    - https://help.aliyun.com/document_detail/41470.htm?spm=a2c4g.41473.0.0.4e235f53GDOpjl#0b2ba7509557s

# windows sshpass 替代
- 再xshell中可以使用这个工具
- 可以安装putty来使用 putty是一个图形化界面，也是一个命令行工具 但是连上后会使用putty的终端打开
- https://www.jianshu.com/p/2c5df43f6423
- doc：https://the.earth.li/~sgtatham/putty/0.78/htmldoc/
- plink 也可以，是putty带的一个工具 这个是使用默认的终端plink -pw JianKong@123456 root@101.133.168.19
- 也可以安一个moba，然后用里面的sshpass，使用where sshpass找出sshpass.exe的位置

# ssh 命令
- link
    - https://www.jb51.net/article/115461.htm
- opt
    - -l 指定用户名 `ssh name@remoteserver -p 2222 #或者 ssh remoteserver -l name -p 2222`
    - -p 连接到远程主机指定的端口：`ssh remoteserver -l name -p 2222`
- 可以建立ssh隧道来进行本地、远程端口转发
    - link：https://www.cnblogs.com/Hi-blog/p/7473752.html
- ssh -vt username@ip 可以来debug链接过程，用来排错

# 本地端口和远程端口
- 其实都一样的， `ssh xxx@xxx -p 222` 对执行命令的机器来说， 222 就是要访问的远程端口， 对xxx来说， 222就是本地端口

### sshpass ssh带密码
    - link：
      - https://www.cnblogs.com/misswangxing/p/10637718.html
    ```
    # sshpass 命令的安装
    yum -y install sshpass
    # 使用 注意后面也要输入ssh
    sshpass -p passwd ssh root@192.168.11.11
    ```
### ssh 连接上去的默认路径是默认用户/或者连接使用的用户的默认～ 执行命令也是
### Linux之间配置SSH互信（SSH免密码登录）
    - [link](https://blog.csdn.net/linxc008/article/details/81278446)
    - 将已经生成的公钥私钥对id_rsa.pub发送到其他的服务器上。这样登录到其他服务器上时就不用输入密码了
    ```shell
    # 命令
    ssh-copy-id -i /root/.ssh/id_rsa.pub 192.168.137.129 
    # 或者手动
    ssh root@web-2 cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
    ```
### 禁止root ssh [link](https://www.cnblogs.com/toughlife/p/5633510.html)
  ```
  vim /etc/ssh/sshd**
  service sshd restart
  ```
### [linux-ssh远程后台执行脚本-放置后台执行问题](https://www.cnblogs.com/vijayfly/p/6264744.html) --------------------------no
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
