# 文档
  - https://www.thegeekstuff.com/2008/08/15-examples-to-master-linux-command-line-history/
  - https://linux.cn/article-10096-1.html
  - 鸟哥linux： https://wizardforcel.gitbooks.io/vbird-linux-basic-4e/content/150.html
# 通识
### sudo和sudo su 和su之间有什么区别啊
sudo 用于以当前用户的权限执行特定命令，提供了更细粒度的权限控制。输入当前用户的密码
sudo su 用于通过 sudo 切换到 root 用户，提供了安全性和权限隔离。输入当前用户的密码，根据配置来决定是否还要输入root的密码
su 用于在已知目标用户密码的情况下切换到其他用户，通常用于切换到 root 用户。切换到哪个用户，输入哪个用户的密码，后面什么不跟就切换到root用户
- sudo
```
sudo（Superuser Do）允许普通用户以超级用户（root）的权限来执行特定命令。
用户需要在 sudo 命令后指定要运行的命令，并在需要时输入自己的密码。系统管理员可以在配置文件（通常是 /etc/sudoers）中指定哪些用户或用户组可以使用 sudo，以及可以运行哪些命令。
sudo 的一个重要优势是可以实现细粒度的权限控制，允许不同用户执行不同的命令，而不必提供完整的 root 权限。
```
- sudo su：
```
sudo su 是通过 sudo 来以超级用户（root）身份启动一个新的 shell。它实际上是在当前用户上下文中切换到 root 用户，因此需要输入当前用户的密码，然后输入 root 用户的密码（如果被配置为需要 root 密码）。
使用 sudo su 可以在不直接暴露 root 用户密码的情况下切换到 root 用户，这有助于提高安全性。
```

- su：
```
su（Switch User）允许用户切换到其他用户账户，包括超级用户（root）。
使用 su 命令，用户需要输入目标用户的密码，然后可以在新的 shell 中执行命令。如果要切换到 root 用户，通常需要输入 root 用户的密码。
su 命令的主要限制是，只有具有特殊权限的用户（通常是系统管理员）才能使用它来切换到 root 用户。
```
- 有些命令不加sudo就没有输出
### 更换内核 debian 
- link：https://www.cnblogs.com/faberbeta/p/16339288.html
- 搜索新内核 apt-cache search linux-image
- 安装搜索到的新内核 apt install linux-image-5.10.0-13-amd64
- 查看可用的内核cat /boot/grub/grub.cfg |grep menuentry
- 修改grub文件使用上一步找到的可用内核
- grub-update
- reboot
### manjaro 最受欢迎的linux发行版 基于arch
### BSD和SystemV
   - 是Unix 操作系统的两种操作风格
### ctrl + R 搜索历史命令
- 输入一些东西后再按ctrl + R继续搜索  

### 查看架构 lscpu

### 包管理工具的区别在other/0_depoly_problem.md


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
### glob模式 Word Splitting IFS 分隔符 # 通配符
   - [Linux shell 通配符 / glob 模式](https://www.cnblogs.com/divent/archive/2016/08/11/5762154.html)
   - glob 模式（globbing）也被称之为 shell 通配符
   - shell 通配符 / glob 模式通常用来匹配目录以及文件，而不是文本！！！
   - [Shell中空格、双引号与Word Splitting、Double quoting扫盲介绍](https://blog.csdn.net/dreamerway/article/details/20380453) ----------------no
   - IFS(Internal Field Separator)
     - which is used to determine what characters to use as word splitting delimiters
     - 默认情况下，IFS包括：space, tab, newline 即：($' \t\n')
   - Word Splitting和Double quoting 就是分割出来的结果不同, 使用"str"分出来的结果就是Double quoting 见上
   ```sh
   mv *bak* a/ 会把xxx.bakxxx 和 xxxbakxxx移动到a中
   *.bak*只会移动前者
   *.bak[0-9]*

   ```
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


### linux 单用户模式
   centos 进入单用户模式 ro 改为rw（可读改为可写） `init=/bin/bash`
   修改完成后 `exec /sbin/init` 退出单用户模式
### yum /y/d/N 
   d 只下载不安装

### 配置文件


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

### service 文件 Linux添加自定义服务
- link:
   - https://juejin.cn/post/7037000593839243301
- Linux中.service文件是某项服务对应的配置文件，可用于systemd管理和控制的服务的设置。.service 文件通常包含3个模块，
   - [Unit]控制单元，表示启动顺序和依赖关系；
   - [Service]服务，表示服务的定义；
   - [Install]安装，表示如何安装配置文件。
- .service 文件配置的服务常用systemd管理。然而，systemd有系统和用户区分；
   - 系统（/user/lib/systemd/system/）、
   - 用户（/etc/lib/systemd/user/）。
   - `/etc/systemd/system/` 一般系统管理员手工创建的单元文件建议存放在`/etc/systemd/system/`目录下面。
- 可以对文件重命名，重命名后会提示systemctl daemon-reload 但知道原来的service服务stop前，原服务名仍能使用
- 服务启动失败后可以使用journalctl -xe来查看日志
- 
### proc 目录 根据pid显示进程信息
- link: https://www.cnblogs.com/DswCnblog/p/5780389.html
- ll /proc/<pid>
- cmdline — 启动当前进程的完整命令，但僵尸进程目录中的此文件不包含任何信息；  cat cmdline
- cwd — 指向当前进程运行目录的一个符号链接；就是工作目录
- exe — 指向启动当前进程的可执行文件（完整路径）的符号链接，通过/proc/N/exe可以启动当前进程的一个拷贝； 
- root — 指向当前进程运行根目录的符号链接；在Unix和Linux系统上，通常采用chroot命令使每个进程运行于独立的根目录； 
- 如果是服务，这三个目录都是不带服务中定义的根路径的

### linux 怎么通过进程pid找出所属的服务呢 方法3最有用

在 Linux 中，你可以通过进程的 PID（进程 ID）来查找所属的服务。通常，服务在 Linux 中是通过守护进程（daemon）形式运行的。
下面是几种常见的方法来找出一个进程所属的服务：
1. 使用 `ps` 命令：可以使用 `ps` 命令结合进程的 PID 来查找进程的详细信息，包括所属的服务。使用以下命令：
   ```bash
   ps -p <PID> -o comm=
   ```
   将 `<PID>` 替换为你要查找的进程的实际 PID。上述命令将返回指定 PID 的进程的命令名称（通常是可执行文件的名称）。根据约定，服务通常具有明确的命名规则，例如 `httpd`、`sshd`、`nginx` 等。因此，通过比对命令名称，你可以识别所属的服务。
2. 使用 `/proc` 文件系统：在 Linux 中，每个正在运行的进程都有一个对应的 `/proc/<PID>` 目录。你可以通过检查该目录中的信息来确定所属的服务。进入 `/proc/<PID>` 目录并查看 `exe` 符号链接的路径，它指向正在运行的进程的可执行文件。例如：
   ```bash
   ls -l /proc/<PID>/exe
   ```
   上述命令将显示进程可执行文件的路径。根据路径中的目录或文件名，你可以推断出所属的服务。
3. 使用 `systemctl` 命令：如果你使用的是基于 systemd 的 Linux 发行版，可以使用 `systemctl` 命令来查找所属的服务。执行以下命令：
   ```bash
   systemctl status <PID>
   ```
   替换 `<PID>` 为你要查找的进程的实际 PID。该命令将显示与该进程关联的服务的状态信息，其中包含服务名称。
请注意，这些方法可以提供关于进程所属的服务的线索，但并不是绝对准确的。有时进程名称和服务名称之间可能存在差异，或者一个服务可能由多个进程组成。因此，在分析进程所属服务时，需要结合其他信息进行综合判断。

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