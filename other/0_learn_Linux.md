# 文档
  - https://www.thegeekstuff.com/2008/08/15-examples-to-master-linux-command-line-history/
# 通识
### manjaro 最受欢迎的linux发行版 基于arch
### BSD和SystemV
   - 是Unix 操作系统的两种操作风格
### ctrl + R 搜索历史命令
- 输入一些东西后再按ctrl + R继续搜索  
# 细节
### Linux不能称为"标准的Unix“而只被称为"Unix Like"的原因有一部分就是来自它的操作风格介乎两者之间
### 设置代理
   - link：https://www.cnblogs.com/daijiabao/p/11358743.html
   ```
   export proxy="http://192.168.5.14:8118"
   export http_proxy=$proxy
   export https_proxy=$proxy
   export ftp_proxy=$proxy
   export no_proxy="localhost, 127.0.0.1, ::1" # 不适用代理的
   ```
### 终端 ctrl-c, ctrl-z, ctrl-d
   - ctrl-c:( kill foreground process ) 发送 SIGINT 信号给前台进程组中的所有进程，强制终止程序的执行；
   - ctrl-z:( suspend foreground process ) 发送 SIGTSTP 信号给前台进程组中的所有进程，常用于挂起一个进程，而并非结束进程，用户可以使用使用fg/bg操作恢复执行前台或后台的进程。
      - fg命令在前台恢复执行被挂起的进程，此时可以使用ctrl-z再次挂起该进程，bg命令在后台恢复执行被挂起的进程，而此时将无法使用ctrl-z再次挂起该进程；
     - 正在使用vi编辑一个文件时，需要执行shell命令查询一些需要的信息，可以使用ctrl-z挂起vi，等执行完shell命令后再使用fg恢复vi继续编辑你的文件（当然，也可以在vi中使用！command方式执行shell命令，但是没有该方法方便） 
   - ctrl-d: ( Terminate input, or exit shell ) 一个特殊的二进制值，表示 EOF，作用相当于在终端中输入exit后回车；
   - ctrl-/: 发送 SIGQUIT 信号给前台进程组中的所有进程，终止前台进程并生成core 文件
   - ctrl-s/q: 中断/恢复 控制台输出
   - 控制字符都是可以通过stty命令更改的，可在终端中输入命令"stty -a"查看终端配置

### shell 命令的执行过程
   - 从shell命令的执行过程说起，执行shell命令的本质其实就是执行一系列系统调用，简单来说就是在执行execve(2)系统调用时将跟命令语句相关的三部分信息传递给它：
   ```
   1、The file to execute: This can be a binary program or a script.
   2、An array of arguments: A list of strings that tell the program what to do.
   3、An array of environment variables
   ```
   `rm myfile myotherfile` 执行这条语句的过程中shell解释器首先做的工作是分解命令语句
   使用 Word Splitting 分割成[rm] [myfile] [myotherfile]
   但如果` rm Children of Men - Chapter 1.pdf` 会被分割成[rm] [Children] [of] [Men] [-] [Chapter] [1.pdf] 这时双引号就派上用场了, 加上双引号能够屏蔽空格作为IFS功能
   ```
    var="Children of Men - Chapter 1.pdf"
    rm "$var"
   ```
### 查看用户信息
   - link：https://blog.csdn.net/newdriver2783/article/details/8059368
   - w命令用于显示已经登录系统的用户的名称，以及他们正在做的事
   - who命令用于列举出当前已登录系统的用户名称。
   - 使用whoami命令查看你所使用的登录名称
   - last命令可用于显示特定用户登录系统的历史记录
### glob模式 Word Splitting IFS 分隔符
   - [Linux shell 通配符 / glob 模式](https://www.cnblogs.com/divent/archive/2016/08/11/5762154.html)
   - glob 模式（globbing）也被称之为 shell 通配符
   - shell 通配符 / glob 模式通常用来匹配目录以及文件，而不是文本！！！
   - [Shell中空格、双引号与Word Splitting、Double quoting扫盲介绍](https://blog.csdn.net/dreamerway/article/details/20380453) ----------------no
   - IFS(Internal Field Separator)
     - which is used to determine what characters to use as word splitting delimiters
     - 默认情况下，IFS包括：space, tab, newline 即：($' \t\n')
   - Word Splitting和Double quoting 就是分割出来的结果不同, 使用"str"分出来的结果就是Double quoting 见上
### sh和bash的不同
   - 定义函数时不同, sh 的函数不能带括号?
   - sh 不支持function
   - bash -n xxx.sh shell脚本语法检查
### 引用
```
# in ~/.bash_profile 
# include .bashrc if it exists
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```
### (文件描述符 fd)[https://blog.csdn.net/yushuaigee/article/details/107883964]
   -  `echo log > /dev/null 2>&1`
### bash -c "cmd or path_to_script_what_have_exec_permission" 使用bash执行命令，命令要用双括号，
### [Linux Crontab 定时任务](https://www.runoob.com/w3cnote/linux-crontab-tasks.html)
   - [时间表达式预览](https://tool.lu/crontab/)
### [linux 在命令行下的快捷键](https://blog.csdn.net/u014429186/article/details/52629029)

### chmod u+x file 表示为文件的所有者增加可执行权限
   - [link](https://www.cnblogs.com/du-jun/p/11550968.html)
   - u+x 是两个部分u、+x
      - u、g、o、a
        - u 当前用户、g当前用户组、o其他、a所有人
      - +x 可执行
        - +w 可读
        - 
### linux 单用户模式
   centos 进入单用户模式 ro 改为rw（可读改为可写） `init=/bin/bash`
   修改完成后 `exec /sbin/init` 退出单用户模式
### yum /y/d/N 
   d 只下载不安装

### 行内for 循环
```shell
for i in `seq 1 10`;do; echo $i;done
for file in `ls|grep apk`;do; adb install $file;done
# 最后一个分号可以不写
for file in `adb shell pm list package -3`;do;echo ${file#*:};done;
for file in `adb shell pm list package -3`;do;echo ${file#*:};done
for obj in `maint_debug_cli lsobj Cpu`;do echo $obj';'; maint_debug_cli getprop $obj.Id; done
for p in `maint_debug_cli lsobj Policy1Class|grep -vEi "fan|mem|dts|margin|let"`;do echo "$p:";sn=$(maint_debug_cli getprop $p.SensorName);maint_debug_cli getpro
p $sn.SensorName;done;
```

### 字符串截取
(link)[https://www.cnblogs.com/hurryup/articles/10241601.html]


### 禁止root ssh [link](https://www.cnblogs.com/toughlife/p/5633510.html)
```
vim /etc/ssh/sshd**
service sshd restart
```

### docker


### jq linux json处理器
  - https://wangchujiang.com/linux-command/c/jq.html


### 免密
```
本地客户端生成公私钥：（一路回车默认即可） ssh-keygen
上传公钥到要免密登录的服务器（这里需要输入密码）ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.235.22 
上面这条命令是写到服务器上的ssh目录下去了vim root/.ssh/authorized_keys可以看到客户端写入到服务器的 id_rsa.pub （公钥）内容。
客户端通过ssh连接远程服务器，就可以免密登录了。ssh root@192.168.235.22
```
### 关闭服务关不掉时先kill掉进程再service fuwuming stop
### diff A B
- link：
  - https://www.runoob.com/linux/linux-comm-diff.html
- diff log2014.log log2013.log  -y -W 50 并排格式输出
- diff A B 的结果
``` 
diff A B
> 表示此行B不为空，A是空行；< 表示此行A不为空，B是空行；| 表示此行A、B均不为空 
">"也可以理解为表示后面文件比前面文件多了1行内容
install:/etc/syslog-ng # diff syslog-ng.conf syslog-ng.conf.bakjjw
255,258c255,256 # 是不同的位置，c前面的是文件A的，后面的是B
# -- 上面的是文件A，下面的是文件B的
<             key-file("/etc/syslog-ng/key.d/Sever_Syslog.pem")
<             cert-file("/etc/syslog-ng/cert.d/Sever_Syslog.crt")
<             # key-file("/etc/syslog-ng/key.d/Server_syslog.key")
<             # cert-file("/etc/syslog-ng/cert.d/Server_syslog.crt")
---
>             key-file("/etc/syslog-ng/key.d/Server_syslog.key")
>             cert-file("/etc/syslog-ng/cert.d/Server_syslog.crt")
11,12d10 # 表示第一个文件比第二个文件多了第11和12行
< 2013-11
< 2013-12
```
- diff A B  -u 统一格式输出
```
它的第一部分，也是文件的基本信息：
--- A 2012-12-07 18:01:54.000000000 +0800
+++ B 2012-12-07 16:36:26.000000000 +0800
"---"表示变动前的文件，"+++"表示变动后的文件。
第二部分，变动的位置用两个@作为起首和结束。
　　 @@ -1,12 +1,10 @@
前面的"-1,12"分成三个部分：减号表示第一个文件（即A），"1"表示第1行，"12"表示连续12行。合在一起，就表示下面是第一个文件从第1行开始的连续12行。同样的，"+1,10"表示变动后，成为第二个文件从第1行开始的连续10行。
```
#### 执行系统命令
- tab 激活目录补全，左右键移动，上下键进入，enter执行命令