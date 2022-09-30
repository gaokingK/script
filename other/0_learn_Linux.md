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
### sh bash 不同
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
### manjaro 最受欢迎的linux发行版 基于arch
### [/etc/profile与/etc/profile.d/的作用](https://www.cnblogs.com/kevin1990/p/8641315.html)
   - /etc/profile是一个脚本，这个脚本在login shell启动的时候，就是在用户登录的时候还有su切换用户的时候会执行;Non-login shell 启动的时候不会
   - /etc/profile.d/是一个文件夹 可以在里面放一些脚本用来设置一些变量和运行一些初始化过程的，/etc/profile 中使用一个for循环语句来调用这些脚本
   - ####  (对所有用户都起作用的alias)[https://blog.csdn.net/littlehaes/article/details/103144509]
   - 但是在`/etc/profile.d/00-aliases.sh 权限是644就行` 里定义的alias只对root用户有用，普通用户需要在~/.bashrc 中引入
   - profile.d 的执行顺序 -----------------------------------------------------------------------------no
### BSD和SystemV
- 是Unix 操作系统的两种操作风格
### Linux不能称为"标准的Unix“而只被称为"Unix Like"的原因有一部分就是来自它的操作风格介乎两者之间

### 行内for 循环
```shell
for i in `seq 1 10`;do; echo $i;done
for file in `ls|grep apk`;do; adb install $file;done
# 最后一个分号可以不写
for file in `adb shell pm list package -3`;do;echo ${file#*:};done;
for file in `adb shell pm list package -3`;do;echo ${file#*:};done

```

### 字符串截取
(link)[https://www.cnblogs.com/hurryup/articles/10241601.html]
### 对过滤的文件进行操作
find . -type f -name "*.sh"|grep sh|xargs -i git add {}

### 禁止root ssh [link](https://www.cnblogs.com/toughlife/p/5633510.html)
```
vim /etc/ssh/sshd**
service sshd restart
```

### 杂
按 ctrl 在命令中 以单词为单位跳转


#### alias 重启的时候会有变化

### docker
`docker top android_1 | grep com.hexin | awk '{print $2;exit}`
```
 docker exec -it android_1 sh -c "ps -a|grep com.hexin" | awk '{print $2;exit}'
```
