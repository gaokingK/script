# doc comm
   1. [link1](http://www.gnu.org/software/bash/manual/bash.html#Process-Substitution)
   - https://wangchujiang.com/linux-command/c/find.html
   - https://linuxpip.org/ 问题
   - 搜索用法就搜 man手册参数详细解释
# other
### 改变工作目录 cd xxxx; other command

### tmux 
- link:
   - http://www.ruanyifeng.com/blog/2019/10/tmux.html
   - https://www.51cto.com/article/664989.html

- 简单的使用流程
   - 新建会话tmux new -s my_session。
   - 在 Tmux 窗口运行所需的程序。
   - 按下快捷键Ctrl+b d将会话分离。
   - 下次使用时，重新连接到会话tmux attach-session -t my_session。

- 快捷键 ctrl + b + ? 显示所有的快捷键
```cs
Ctrl+b "：划分上下两个窗格。
新建窗口： ctrl + b, c
切换窗口：ctrl + b, n
Ctrl+b z //当前窗格全屏显示，再使用一次会变回原来大小。
滚屏 CTRL + B + [，//这时就可以用光标键来操作翻页滚屏 （只能一行一行的滚） ctrl+c退出
ctrl + b space 调整布局
```
- 兼容vim的操作方式
```cs
vim ~/.tmux.conf
setw -g mode-keys vi
tmux source-file ~/.tmux.conf // 重新载入配置文件
// 使用快捷键进入 copy-mode 模式，然后就可以像 vi 中一样操作了  Ctrl-u 向上滚半屏， Ctrl-d 向下滚半屏。
// 用快捷键进入 copy-mode 模式，然后按 / ，就可以输入关键字了，回车查找。
```
### pstree 查看进程关系 父进程和子进程
- `yum install -y psmisc`
- pstree 括号里的数字代表子进程的数量
- pstree -p 同时列出每个进程的PID
- -a 显示该行程的完整指令及参数, 如果是被记忆体置换出去的行程则会加上括号

### mount
- https://www.runoob.com/linux/linux-comm-mount.html
- mount /dev/hda1 /mnt 将前面的目录挂载到后面的目录上去
- 查看系统内的挂载信息 直接输入mount
- 挂载和递归挂载 bing rbing https://blog.csdn.net/realmeh/article/details/17888613
   - 区别的就拿来mount的目录，如果里面还有挂载的目录，那里面挂载目录的东西就不会被挂载到最新的目录里面，而rbind可以
   - 只挂载当下目录的文件，不挂载当下目录里面的文件夹这种理解是不正确的，两种挂载方式都是挂载子目录的
- 是这样吗
>mount --bind test1 test2为例，当mount --bind命令执行后，Linux将会把被挂载目录的目录项（也就是该目录文件的block，记录了下级目录的信息）屏蔽，即test2的下级路径被隐藏起来了（注意，只是隐藏不是删除，数据都没有改变，只是访问不到了）。同时，内核将挂载目录（test1）的目录项记录在内存里的一个s_root对象里，在mount命令执行时，VFS会创建一个vfsmount对象，这个对象里包含了整个文件系统所有的mount信息，其中也会包括本次mount中的信息，这个对象是一个HASH值对应表（HASH值通过对路径字符串的计算得来），表里就有 /test1 到 /test2 两个目录的HASH值对应关系。
命令执行完后，当访问 /test2下的文件时，系统会告知 /test2 的目录项被屏蔽掉了，自动转到内存里找VFS，通过vfsmount了解到 /test2 和 /test1 的对应关系，从而读取到 /test1 的inode，这样在 /test2 下读到的全是 /test1 目录下的文件。
https://www.cnblogs.com/weihua2020/p/13872964.html
>

### 用户 # user
- linux 更改用户名密码、新增用户
	- 新增用户`useradd name option`
	- 更改密码`passwd username` 
- 查看用户创建时间 https://www.jb51.net/article/139900.htm
### 命令补全 CentOS系统Tab补全功能
=======
- 新建窗口： ctrl + b, c
- 切换窗口：ctrl + b, n
```cs
Ctrl+b z：当前窗格全屏显示，再使用一次会变回原来大小。
```
 
### CentOS系统Tab补全功能
>>>>>>> 7ce39ce967aa6d11455c9b35a67440abec660ec7
- link: https://blog.csdn.net/RunSnail2018/article/details/81185957
- yum install bash-completion
### chroot # rootfs
- https://www.cnblogs.com/sparkdev/p/8556075.html
- 在 linux 系统中，系统默认的目录结构都是以 /，即以根 (root) 开始的。而在使用 chroot 之后，系统的目录结构将以指定的位置作为 / 位置。
- 主要作用有：
   - 增加了系统的安全性，限制了用户的权力：
   - 建立一个与原系统隔离的系统目录结构，方便用户的开发：
   - 切换系统的根目录位置，引导 Linux 系统启动以及急救系统等：
- `sudo chroot django pip install djangorestframework ` # 会报没有pip，这是需要把pip的路径贴上去`sudo chroot django /usr/local/bin/pip install djangorestframework requests daphne -i https://pypi.tuna.tsinghua.edu.cn/simple`
- 在隔离环境中安装软件
   ```
   $ sudo chroot ansible sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
   # 这里本地安装依赖，需要dns配置
   $ cp /etc/resolv.conf ansible/etc/resolv.conf
   $ sudo chroot ansible apk add ansible openssh-client
   ```
- 执行多条命令：使用bin/sh调用
   - sudo chroot django/ /bin/sh -c "cd /opt/apiserver;/usr/local/bin/daphne -b 127.0.0.1 -p 9990 apiserver.asgi:application"
### ifconfig # ip
- link:
   - ip: https://www.runoob.com/linux/linux-comm-ip.html
- 查看ip：https://blog.csdn.net/ITwang1/article/details/121069835
   - hostname -I |awk '{print $1}'
### pkill # kill
- pkill
   - Linux pkill 用于杀死一个进程，与 kill 不同的是它会杀死指定名字的所有进程，类似于 killall 命令
   - -t 指定开启进程的终端
   - 也能发送信号
- kill
   - kill -0 pid 不发送任何信号，但是系统会进行错误检查。该命令可以用来检查一个进程是否存在，若存在，即进程在运行，执行 echo $? 会返回 0
   ```
   $ kill -0 888888;echo $?
   -bash: kill: (888888) - No such process
   1
   [root@iZuf68h0usx91bux03msu1Z ~/j_go]
   ```
   - 若不存在，即进程已停止运行，执行 echo $? 会返回 1。
   - 该命令与 ps -p 命令功能相似，一般可以进行互换
   - 使用 kill -9 -1 命令可以终止当前用户下的所有进程。
   - killall firefox 终止所有名为 "firefox" 的进程。
   - 信号
      TERM (15) - 终止信号：
      默认的终止信号，发送后进程有机会优雅地进行清理工作后退出。
      INT (2) - 中断信号：
      当在终端上按下 Ctrl+C 时发送的信号，通常也可以用于终止进程。
      QUIT (3) - 退出信号：
      发送后，进程会终止，并且生成一个核心转储文件，用于调试。
      KILL (9) - 强制终止信号：
      发送后，进程会立即终止，无法进行清理操作。该信号可以终止无法通过其他信号终止的进程。
      STOP (19) - 暂停信号：
      发送后，进程会被暂停执行，可以使用 CONT 信号来恢复执行。
      CONT (18) - 恢复信号：
      发送后，恢复被 STOP 或 TSTP 信号暂停的进程的执行。
      HUP (1) - 终端挂起信号：
      当与终端连接的会话（例如终端窗口）关闭时发送的信号。
      USR1 (10) 和 USR2 (12) - 用户定义信号：
      这些信号可以由进程自定义使用，例如作为某种特定操作的触发器。
      TSTP (20) - 终端停止信号：
      当在终端上按下 Ctrl+Z 时发送的信号，暂停进程的执行。
      PIPE (13) - 管道破裂信号：
      当向一个已关闭的管道写入时发送的信号。
### 发送ctrl+c `sh', '-c', '\x03'`

### which whereis type locate find 
   - link: https://www.cnblogs.com/danmiao/p/10081620.html
   - which  查找命令是否存在，以及命令的存放位置在哪儿。
   - whereis 只能用于搜索程序名，而且只搜索二进制文件（参数-b）、man说明文件（参数-m）和源代码文件（参数-s）。如果省略参数，则返回所有信息。
   - type 用来区分某个命令到底是由shell自带的，还是由shell外部的独立二进制文件提供的。如果一个命令是外部命令，那么使用-p参数，会显示该命令的路径，相当于which命令
   - locate 
     locate命令实际是"find -name"的另一种写法，但是查找方式跟find不同，它比find快得多。因为它不搜索具体目录，而是在一个数据库(/var/lib/mlocate/mlocate.db)中搜索指定的文件。次数据库含有本地文件的所有信息，此数据库是linux系统自动创建的，数据库由updatedb程序来更新，updatedb是由cron daemon周期性建立的，默认情况下为每天更新一次
     ```
     [huawei@localhost redis-6.2.0]$ locate libatomic                                                  
     /usr/lib64/libatomic.so.1                                                                         
     /usr/lib64/libatomic.so.1.2.0                                                                     
     /usr/local/mysql/lib/libatomic.so.1.2.0 
     ```

### 标准输入 标准输出
   - link:
     - https://blog.csdn.net/huangjuegeek/article/details/21713809
     - https://segmentfault.com/a/1190000018650023
   - IO
     - I(Input)：从外部设备输入到内存
     - O(Output)：从内存输出到外部设备
     - 它们是/dev/stdin这个文件和/dev/stdout这个文件(连接文件)。
   - 使用
     - 0表示标准输入
     - 1表示标准输出
     - 2表示标准错误输出
     - `>` 默认为标准输出重定向，与 `1>` 相同
     - `2>&1` 意思是把 标准错误输出 重定向到 标准输出.
     - `&>file` 意思是把 标准输出 和 标准错误输出 都重定向到文件file中
     - 其中&的意思，可以看成是“The same as”、“与...一样”的意思`./conf >a1 2>&1` 2>&1的意思就是标准错误输出和标准输出一样，输出到a1中
     - 也可以分别定义 
        - `grep da * > file1 2>file2`
        - `grep da * > file1 2>&1`
        - `grep da * > file1 1>&2`但这里的file1没有内容，file1本来是有1的内容的，但是后面又被重定向了到和2一样了。就会都输出在控制台中
   - 管道符后面的内容可以从/dev/stdin 读入
     - cat file_name |awk xxxx |sh /dev/stdin # awk 后当成命令执行
### pgrep 显示进程的pid
- pgrep qoffer
### jq linux json处理命令
   - link: https://www.jianshu.com/p/6de3cfdbdb0e
   - cat json_file| json "."  格式化输出json文本
### file 
   - link: http://c.biancheng.net/linux/file.html
   - file file_name 查看文件信息
   - -b 不显示文件名
   - -i 可以输出文件的 MIME 类型字符串
   - -f 查看一个文本文件中所记录的文件的信息
   - 可以查看文件是否是可执行文件
      - link: https://blog.csdn.net/weixin_44966641/article/details/120598561

### lsof 列出系统啥进程打开了啥文件
   - link：https://www.runoob.com/w3cnote/linux-check-port-usage.html
   - lsof +d /usr/local/：显示目录下被进程开启的文件
### lsmod 显示的当前内核已经加载的模块和驱动
   - link: https://www.cnblogs.com/machangwei-8/p/10398706.html
   - 解析 scsi_mod            141973  7 scsi_dh,sg,libata,mptspi,mptscsih,scsi_transport_spi,sd_mod
      - 第1列：表示模块的名称，如scsi_mod表示scsi模块。
      - 第2列：表示模块的大小，如141973表示scsi_mod模块的大小为141973字节。
      - 第3列：表示依赖模块的个数，如7表示有7个模块依赖scsi_mod模块。
      - 第4列：表示依赖模块的内容
### modprobe 从 Linux kernel 中装载和卸载模块
   - link: https://einverne.github.io/post/2018/09/modprobe.html
   - 使用：modprobe module_name
   - modprobe 命令会查找 /lib/modules/'uname -r' 目录中的模块和文件 (uname -r 是内核版本），但是不会查找 /etc/modprobe.conf 和 /etc/modprobe.d/ 目录下配置所排除的内容。可以这样查找 ```find /lib/modules/`uname -r` -name ipmi*```

### top 
   - link:
      - https://blog.csdn.net/mp624183768/article/details/76175751
      - 
   - 默认 top 命令是按照 CPU 使用率排序的。
   - 按内存排序 shift + M
   - 按M能变换样式
   - -b 以非交互和非全屏模式运行
   - -d 5    更新延时设置为5秒
   - -u MySQL    只查看有效用户名为mysql的进程
   - -n 8    退出前屏幕再刷新10次
   - -p 通过指定监控进程ID来仅仅监控某个进程的状态
### strings
   - link: https://blog.csdn.net/test1280/article/details/80978717
   - string 工具可以对任何文件的内容进行分析，并输出可打印字符长度不小于4的串。
   - 这里“任何文件”，包括文本文件和二进制文件。其实“文本文件”和“二进制文件“两者并没有啥差别，所有的文件本质都是 Binary，文本文件只不过是一些特殊的 Binary 
   - -n 修改可打印字符串的最小长度
   - 使用场景
   ```
   # main.c 中有版本号， 我们可以通过已编译的main识别版本
   gcc -o main main.c
   strangs main|grep version_char
   # 定位main.c 源文件最后会编译到哪个 Binary 文件中
   strings -f * | grep "main.c中的字段"
   # 更多见link
   ```
### 重定向
   - 进程替换 与 Here document 做区分?
   ```
   command > file	将输出重定向到 file。
   command < file	将输入重定向到 file。
   command >> file	将输出以追加的方式重定向到 file。
   n > file	将文件描述符为 n 的文件重定向到 file。
   n >> file	将文件描述符为 n 的文件以追加的方式重定向到 file。
   n >& m	将输出文件 m 和 n 合并。
   n <& m	将输入文件 m 和 n 合并。
   << tag	将开始标记 tag 和结束标记 tag 之间的内容作为输入。 EOF
   ```
### 进程替换 与 Here document --------------no
   - 形如<(command)的写法叫做**process substitution**
   - [解释了底层怎样支持](https://www.oschina.net/question/113421_241288)
   - [进程替换](https://www.runoob.com/w3cnote/shell-process-substitution.html) ---------no
   - [Here document使用方法总结](https://blog.csdn.net/liumiaocn/article/details/86715953) -------------no
   - 可以把<(...)整体当做一个文件名，这个文件的内容就是()中脚本的执行结果，这样第二条命令简化为`bash -s stable <tmp.sh` 或 $(<file_name)
### 输出参数提示(redis) -----------------------------------no
### declare 
   - [link](https://www.runoob.com/linux/linux-comm-declare.html)
   - -A 定义一个map
   - -i 声明一个数值型
   - -p 查看一个变量类型
### shell 数据类型/语法
   - map [link](https://blog.csdn.net/wssnxcj/article/details/82907886)
   ```shell
   #必须先声明
   declare -A dic
   dic=([key1]="value1" [key2]="value2" [key3]="value3")
   ```
   - $@ 获取所有参数(不包括$0), $0脚本的地址,
### awk
   - link：
      - https://www.runoob.com/linux/linux-comm-awk.html
   - `{print $NF}` 输出切割后的最后一项; `'{print $(NF-1)}` 倒数第二项
   - 可以指定多个分隔符 `awk -F '[b,]' ` 先使用b，后使用，
   - length 方法获取字符串的长度 `echo ${str}|awk '{print length($0)'`
   - -F fs 指定输入文件折分隔符，fs是一个字符串或者是一个正则表达式，如-F:
     - echo "rootfs/deploy/a.txt"|awk -F/ '{print $2}'
#### 命令
   - awk '/workers:/ {getline; print $1}' your_file.yaml
      - 我们使用 /workers:/ 来匹配包含 workers: 的行。然后使用 getline 命令读取下一行，并使用 print $1 来打印第一个字段，即 IP 地址。
   - 合并 workers 和 add_workers 到一个新的列表中
      - awk '/workers:/ {workers=1; next} /add_workers:/ {workers=0} workers {print $0}' your_file.yaml
   - awk '/add_workers:/ {getline; print}' RS='[- ]+' FS='\n' your_file.yaml
      - /add_workers:/: 此处使用 /add_workers:/ 来匹配包含 add_workers: 的行。
      - {getline; print}: 使用 getline 命令读取下一行，然后使用 print 命令输出该行内容。
      - RS='[- ]+': 设置行分隔符为 [- ]+，即一个或多个连字符和空格。这样可以将 YAML 列表识别为单独的行。
      - FS='\n': 设置字段分隔符为换行符，这样我们可以读取整个 IP 地址行。
   - awk '/add_workers:/ {flag=1; next} /^ *$/ {flag=0} flag {print}' inventory_10.0.5.89.yaml
      - /add_workers:/ {flag=1; next}: 当匹配到 add_workers: 行时，设置标志 flag 为 1，并跳过下面的处理。
      - /^$/ {flag=0}: 当匹配到空行时，设置标志 flag 为 0，表示结束匹配 add_workers 区块。
      - flag {print}: 当标志 flag 为 1 时，打印当前行。
   - awk '/add_workers:/ {flag=1; next} /^[ a-zA-Z:]*$/ {flag=0} flag {print}' inventory_10.0.5.89.yaml
   - awk -v ip="$new_ip" '/workers:/ {found=1} {print} END {if (found) print ip}' your_file.yaml > tmp_file.yaml
      - -v ip="$new_ip": 使用-v参数，将Shell变量new_ip传递给awk中的变量ip。
      - '/workers:/ {found=1}: 当遇到包含workers:的行时，设置变量found为1。
      - {print}: 对于所有行，都打印输出。
      - END {if (found) print ip}: 在文件末尾（END）判断是否找到了包含workers:的行（即found为1），如果找到，则打印变量ip（新的IP地址）。
### scp
   - scp 文件 `scp file_path target_file_path/target_dir_path`  如果要重命名， target_file_path 不存在也可以
   - 如果要放到文件夹中 `scp file_path target_dir_path/.` dir_path/. 要加 `/.`
   - scp /dir/ /dest/dir会将dir这个文件夹和内容放到目的地，scp /dir/. 只会将里面的内容放到目的地
   - scp 可以直接带密码 scp username:passwd@ip:/path/to/file

### exit
   - 执行exit可使shell以指定的状态值退出。若不设置状态值参数，则shell以预设值退出。状态值0代表执行成功，其他值代表执行失败。
   - exit也可用在script，离开正在执行的script，回到shell。
### script 能够将终端的会话过程录制下来 ---------------------------------no
   - [link](https://www.cnblogs.com/cheyunhua/p/11136161.html)
   - 利用script记录某人行为
### 这些命令格式绝大多数为 command option file
### more
more 命令类似 cat ，不过会以一页一页的形式显示，更方便使用者逐页阅读，而最基本的指令就是按空白键（space）就往下一页显示，按 b 键就会往回（back）一页显示，而且还有搜寻字串的功能（与 vi 相似），使用中的说明文件，请按 h 。
- link:
  - https://www.runoob.com/linux/linux-comm-more.html
### less
   - [link](https://www.cnblogs.com/molao-doing/articles/6541455.html)
   - less 工具也是对文件或其它输出进行分页显示的工具，应该说是linux正统查看文件内容的工具，功能极其强大。less 的用法比起 more 更加的有弹性。
   - less file1 file2 `:n :p 切换文件（next/previous`
   - -N 显示每行的行号 :-N也可以
### cat
   - -n 对输入行编号 也只能编号了

### head
   - -n num 显示前num行，若num带-号，就只是从头显示，直到最后第num行
### tail
   - -n num 显示后num行，use -n +K to output starting with the Kth
### sort
- link
   - (https://www.cnblogs.com/51linux/archive/2012/05/23/2515299.html)
   - [ sort -n 与 -g 排序对比](https://www.cnblogs.com/z977690557/p/8945261.html)
- opt
   - -r 默认第一列进行排序并且是降序
   - -u unique 输出行中去除重复行。
   - -n 按数值的大小排序
   - -k 选择以哪个区间来排序
   - -t 可以在后面设定间隔符
   - 不加选项的时候 sort 命令将以默认的方式将文本文件的第一列以 ASCII 码的次序排列
```
sort -n -k 2 -t : facebook.txt # 对facebook的内容先以：来分割，按分割结果的第二列来排序
```

### Bash内建参数 和 bash 参数
    - -s 允许在调用交互式shell时设置位置变量, 可以将标准输入 作为命令 去使用参数
      > 因为你用bash -s...这个参数是如果有-s，或者选项处理之后没有别的参数，那么命令从标准输入读入。这个选项允许在调用交互式shell时设置位置变量
      link: https://www.oschina.net/question/113421_241288
    ```shell
    # test.sh
    #! /bin/sh
    echo $@
    echo $0,$1,$2

    $ cat test|bash -s stable # 输出的结果是 sh test.sh stable
    $ bash -s stable < <(cat test.sh) # d等上
    ``` 

### touch 
   - touch -r 文件 文件夹  # 意思是把文件的日期设置给文件夹。
   - 修改文件时间
      - link：https://blog.csdn.net/qq_39900031/article/details/123273907
      - touch -a： 修改文件的访问时间
      - touch -d： 同时修改文件的访问时间和修改时间，格式：touch -d “2021-01-02 09:32:21” 3.log
### linux 特殊符号和通配符 
   ```shell 
   # https://www.cnblogs.com/0zcl/p/6821213.html
   |     #管道符，或者（正则）
   >     #输出重定向
   >>    #输出追加重定向
   <     #输入重定向
   <<    #追加输入重定向
   ~     #当前用户家目录
   `` $() #引用命令被执行后的结果
   $     #以。。。结尾（正则）
   ^     #以。。。开头（正则）
   *     #匹配全部字符，通配符
   ？    #任意一个字符，通配符
   #       #注释
   &       #让程序或脚本切换到后台执行
   &&      #并且 同时成立
   [a-z]      #表示一个范围（正则，通配符）
   [abcd]     # 匹配abcd中任何一个字符
   [!abcd] # 表示不匹配括号里面的任何一个字符
   {}      #产生一个序列（通配符）{a..f}: a,b,c,d,e.....f
   # 以逗号分割的话就是原来的样子 {1,3,5}：1,3,5
   [[:digit:]]  # 匹配数字，还有别的类似的写法
   .       #当前目录的硬链接
   ..      #上级目录的硬链接
   ```
   - 通配符作用 cp a{,.bak} ; cp a a.bak
      - 但是不能反着来，cp a{.bak, .back} 就会报错
   - rm -rf 11{2..3} 怎么不弹出提示
   - [a-z] {a..z} 有什么区别?-----------------------------no
     - 后者既能用在mkdir上,又能用在rm上, 而前者只能用在rm上
### date 
   - [时间域](https://www.cnblogs.com/yy3b2007com/p/8098831.html)
   - `echo $(date +%y%m%d) ` m 是月 M 是分  中间的加号后面不能有空格 
   - `echo $(date +%ya_string%d) `  还可以这样替换，结果是2021a_string13
   
### xargs 怎么只接受一次参数 ------------------------------------------------no
### 文件时间 stat
- 查看时间：
   - 最近访问时间（Access）:使用cat、less等查看文件后会被修改
   - modify时间：内容被改变的时间
   - change时间：显示的是文件的权限、拥有者、所属的组、链接数发生改变时的时间。当然当内容改变时也会随之改变（即inode内容发生改变和Block内容发生改变时）
   - 改变内容会改变atime、mtime、ctime；chmod只会改变ctime
   - windows 上显示的修改时间是mtime
- 使用stat可以查看文件的三个时间以及其他状态
- 修改时间
   - 见touch使用
### ls 
   - ls -t 按时间顺序显示
   - ls -r 显示文件夹中
   - -R 若目录下有文件，则以下之文件亦皆依序列出
   - ls -d 显示目录
   - 查看文件的时间
      - link：https://blog.csdn.net/qq_39900031/article/details/123273907
      - ll --time=atime  //查看访问时间
      - ll --time=ctime  //查看改动时间
### 符号 linux中单引号‘ ,双引号“, 反引号 ` `, $, $(), ${}与变量；shell中各种括号的作用()、(())、[]、[[]]、{}
   - [shell中各种括号的作用()、(())、[]、[[]]、{}](https://blog.csdn.net/taiyang1987912/article/details/39551385?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-2.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-2.no_search_link) -------------------------------------------no
   - [linux 单引号‘ ,双引号“, 反引号 ` `, $, $(), ${}与变量](https://blog.csdn.net/qq_40491569/article/details/83688652)
   - [shell中的(),(()),{},=,==,[],[[]]几种语法用法](https://blog.csdn.net/Michaelwubo/article/details/81698307)
   - [] 和 `[[]]` 的区别见learn_shell_process_control.md
   - 不加引号、单引号、双引号的区别：
      - 单引号和双引号主要时为了包含有空格的
      - 单引号剥夺了所有字符的特殊含义, 里面的就是单纯的字符, 双引号不会
      - ![单引号：所见即所得。双引号：解析特殊符号，特殊符号有了原本的特殊意思 不加引号：比较特殊，支持通配符](https://images2015.cnblogs.com/blog/1038183/201705/1038183-20170507173906929-1826372684.png)
   - 使用$来使用变量 echo $a
   - 变量赋值的时候, 如果含有空格 需要用单引号或者双引号
   - $(cmd) 会将命令的执行结果赋值给变量 如 `a=$(echo aaa)`; 反引号也可以 for line in `ls *.apk`
      但 `echo $(cmd)` 和 `echo "$(cml)"`的结果为啥回不一样？----------------------------------------no
   - ${ }中放的是变量，例如echo ${hello}取hello变量的值并打印，也可以不加括号比如$hello。但加了括号可以对变量操作参见 变量替换
   - () 是开一个子shell执行里面的命令
   - 命令后加&显示pid 
      ```cs
      $ systemctl start prometheus2 &  # 服务返回的pid可能不正确建议使用pgrep prometheus
      [1] 22861
      tail -f /dev/null &
      [1] 22038
      ```
   - {} 用于生成序列 比如 mv a{.yaml,.bak} 就是相当于 mv a.yaml a.bak 注意{}可以放在任何地方，但是里面不要有空格出现在`{,}`着三个符号旁边
### read [option] [变量名] 接受键盘输入
   ![提示信息](https://images2015.cnblogs.com/blog/35158/201610/35158-20161011104351477-686622915.png)
### echo
   - -n echo本身默认最后会输出一个换行，要禁用最后的换行，可使用-n `echo -n "aaa" && echo "bbb"`
   - -e 表示启用解释反斜杠转义 处理特殊字符: \a 发出警告声； \b 删除前一个字符; \c不换行；
   - -E：默认带有禁用转义
   - 可以输出多个`echo "a" "a" ..`
   - 使用命令新建文本文件（有的内核不需要-e参数）  `echo -e 1\n2 > 1.txt`
   - 如果一个变量带有换行符 需要使用echo "$var" 才带有，如果使用 echo $var是没有换行符的
### tar zip
   - [link](http://blog.chinaunix.net/uid-29132766-id-3862597.html)
   - 如果a/中有b,c,d文件, 然后在a的父文件中tar .... a/ 那么解压出来 也会有个a/ 就不必在创建a/然后在-C a/了,那样就有两层；而是直接在目录D下`tar -zxvf file.tar.gz` 这下目录D下就会有a/了
   - -z 通过gzip指令处理备份文件
   - -v 显示处理信息
   - -f file 指定文件
      - 用-表示标准输入 `(cd backup && tar c .) | (cd backupArchives && tar xf -)`或 `docker export $(docker create python:3-alpine) | tar -C django -xf -`
         - https://www.v2ex.com/t/758589
         - 就是约定俗称，最初的原因就是这玩意天然不适合做文件名，刚好可以用来表达标准输入输出（按标准写法的话是直接用-O 表示标准输出，不写文件名就是标准输入
   - -c -x -A -t
      -c 建立新的备份文件 `tar -zcvf /tmp/etc.tar.gz /etc` 
      -A或--catenate 新增文件到已存在的备份文件。----------------------no
      -x 从备份文件中还原文件 
      -t 列出备份文件的内容
   - `tar -tzvf test.tar.gz ` 列出压缩文件内容
   - -C 解压到指定路径 如果不存在会报错 
   - -T 指定范本文件，其内含有一个或多个范本样式，让tar解开或建立符合设置条件的文件。 还可以这样
     - `find . -name "*.d" -o -name "*.conf" | tar -czvf etc.tar.gz -T -` ---------------------------------------这个 最后的- 是干啥的 见上面
   - tar --atime-preserve=system -zxvf autotest.tar.gz 原来的时间
   - **zip**
   - zip [option] dist.zip source
   - -q 不显示指令执行过程。
   - -r 递归处理，将指定目录下的所有文件和子目录一并处理。
### find
   - `*`是通配符 `.`不是
   - find 里面的选项可以加（）但必须注意空格，也需要把被包括的命令的全部参数给包括进去 比如`；`
   - find (path1[, path2]) （）带表必选参数，[]中的代表可选参数 如：`find 111 112 -name *.txt` 可以在112 111 中寻找txt
   - -name "" 要用双括号包围， 单括号也可以
   - `find . -type d -name "*$(date +%Y%m%d)*" -o -maxdepth 1 -name "*$(date +%Y%m%d)*.txt" `  为什么会失败? ------------------------------no
   - 是否可以使用find 查找目录结构如`\a\b\`，而不是去查找文件夹,单独find不能完成。看下面的-path选项
      `find  / -type d -name "b" |grep "\a\b"` 注意`b`写在find里面，而grep中写`b`而不是`b/`
      超哥提供了另外一种方法 `ls -F /*/*/*/*/*|grep /a/b/`但这样没有响应
   - -cmin n 查询在过去n分钟内修改的文件(创建也是修改)
      ```
      ---(+n)----------|----------(n)----------|----------(-n)---
            (n+1)*24H前|     (n+1)*24H~n*24H间   |n*24H内
      ```
   - -ctime n n天前修改过文件的状态 （显示的是文件的权限、拥有者、所属的组、链接数发生改变时的时间。当然当内容改变时也会随之改变（即inode内容发生改变和Block内容发生改变时）
   - -mtime n n天前修改过文件的内容
   - -amin n n分钟前读取过
   - -newer file1 ！file2：查找修改时间比file1新但是比file2旧的文件
   - -newermt "2016-12-06" t 解释t使用 date 命令 -d选项的参数格式
     `find ./log/20211028 -name "douyin*open_002*" -newermt "2021-10-28 03:02"`
   - find 的有效输出到文件中
      ```shell
      find / -name "*ython3.*" 2 > invalid.txt 
      find / -name "*ython3.*" 1 > valid.txt
      ```
   - -o -a -not: 
      -o 是或者的意思
      -a 是而且的意思  
      -not 是相反的意思
      - 逻辑符只对前后紧挨的选项起作用 `find -type d \( -path "*xbox_screen_shot*" -o -path "*log*" \) -ctime +7` 不加 括号 -type d 就只对 第一个-path 有用
   - [link](https://blog.csdn.net/earthchinagl/article/details/79501778) ---------------------------no
   - [link](https://www.cnblogs.com/chuyiwang/p/12779417.html) ---------------------------no
   - -regex 是从文件的全路径中调用正则匹配 -regextype 选择使用的正则格式
   - -path 模糊匹配路径 `find . -path '*20190326/access.log'` 如果查找的关键词没有从根路径开始那么前面的*是必要的如果
   - [linux find子目录，当前目录，指定（排除）目录查找文件](http://www.51gjie.com/linux/1025.html)
      ```shell
      find / -name "*tomcat.txt" -maxdepth 1 -print     //在当前目录中，查找包含tomcat.txt文件，-maxdepth 1表示查找最大深度为1 -mindepth 最小深度
      # 指定(排除)目录查找文件
      find . -path "./code" -prune -o -name "*.txt" -print  //在当前目录除code之外的子目录内搜索 txt文件
      find . \(-path "./code" -o -path "./code2" \) -prune -o -name "*.txt" -print     //在当前目录及除code和code2之外的子目录中查找txt文件
      find . \( -name "111*.txt" -o -name "112*.txt" \) 这个是能运行的， 注意空格（不加空格就不能运行）
      ```
   - -print ----------------------------no
      `find . -path "./tests" -prune -o -name "*.py" -print` 不加print会多输出一行 ./tests
   - find -name "aaa" 若是要使用通配符*是匹配所有字符任意次.就是匹配. 不知道加双引号有什么区别 
      - find -name xxx.log 可以找到xxx.log 但不能找到xxx.log2
   - -exec commond \;
      - [](https://www.jianshu.com/p/ea096af9d765)
      必须在命令后面加上终结符，终结符有两个：“；”和“+”。
      - 为什么必须有终结符？
         - 因为一个find后面可以有多个-exec cmd，所以必须要有终结符分割他们。如果不加，会包缺少参数。
      - 为什么要加“\”?
      “；”是shell的命令分隔符，如果只有“；”，那么这条命令就会被shell截断。
      ```shell
      - 其中“；”会对每一个find到的文件去执行一次cmd命令。而”+“让find到的文件一次性执行完cmd命令。
      [work@jkz ~]$ find . -maxdepth 1 -type f -name "*.log" -exec echo {} \; -exec echo {} +
      ./server02.log
      ./server03.log
      ./server00.log
      ./server01.log
      ./timing.log
      ./server.log
      ./server02.log ./server03.log ./server00.log ./server01.log ./timing.log ./server.log 输出到一块了
      `find . \( -name "111*.txt" -o -name "112*.txt" \) -exec cat {} \;` 注意结尾的反斜杠和； 否则会提示遗漏“-exec”的参数
      # 里面好像不能使用管道符
      $ find . \( -name "111*.txt" -o -name "112*.txt" \) \( -exec cat {}|wc -l \; \)
      wc: ';': 没有那个文件或目录
      wc: ')': 没有那个文件或目录
      0 总用量
      find: 遗漏“-exec”的参数
      # 不能使用管道符的
      find . \( -name "111*.txt" -o -name "112*.txt" \) \( -exec cat {} \; \)|wc -l
      find . -regextype posix-extended -regex ".*[[:digit:]]_test.py"
      ``` 
   - -ok：与-exe的作用相同，只不过以一种更安全的模式来执行，每次执行命令之前否会询问，让用户选择是否要执行
   - -prune是一个动作项，它表示当文件是一个目录文件时，不进入此目录进行搜索;-prune经常和-path或-wholename一起使用，以避开某个目录
     **注意：圆括号()表示表达式的结合。即指示 shell 不对后面的字符作特殊解释，而留给 find 命令去解释其意义。由于命令行不能直接使用圆括号，所以需要用反斜杠'\'进行转意(即'\'转意字符使命令行认识圆括号)。同时注意'′，′'两边都需空格。**
     在当前目录及除aa和bb之外的子目录中查找txt文件 　　
     `find . \( -path './dir0' -o -path './dir1' \) -prune -o -name '*.txt' -print`
   - -empty
   - -delete 直接删除查询结果（怎么删除文件夹呢）
      使用delete 和 -exec rm {} 删除文件夹会报错 ---------------------no
      ```
      find . -type d -name "__pycache__" -exec rm -r {} \; # 又执行一遍就好了
      [root@localhost src]# find . -type d -name "__pycache__" -exec rm -r {} \;
      find: ‘./processor/__pycache__’: No such file or directory
      find: ‘./dataset/__pycache__’: No such file or directory
      find: ‘./predict/__pycache__’: No such file or directory
      find: ‘./analyzer/__pycache__’: No such file or directory
      find: ‘./__pycache__’: No such file or directory

      ```
   - `find . -name "*.txt" -ctime -7 -exec grep  -H -E ".*jinshan.*open.*004.*" {} \;` grep在find -exec选项中显示文件名
   - 显示文件名 不显示路径 find . -name "*.log" -exec basename {} \;
   - -depth ---------------------------------------------------------no
     `find . -depth -name '__pycache__' -exec rm -rf {} ';'`
   - -build  ---------------------------------------------------------no
     ```shell
     find . -name '*.so.[0-9]*.[0-9]*' -exec rm -f {} ';'
     find build -name 'fficonfig.h' -exec rm -f {} ';' || true
     find build -name '*.py' -exec rm -f {} ';' || true
     find build -name '*.py[co]' -exec rm -f {} ';' || true
     ```
   - ### 对过滤的文件进行操作
      find . -type f -name "*.sh"|grep sh|xargs -i git add {}

### nl filename 带行号显示文件内容

### ps -ef/ aux/ -aux的区别
   - link: 
      - https://www.cnblogs.com/sexybear/p/Linux_ps.html
      - 不同：https://blog.csdn.net/qq_36025814/article/details/122232571
   - 显示的风格不同;aux会截断命令,如果后面配合grep可能会影响效果;
   - 都显示全部的系统进程和用户进程，但是列不一样，-aux会显示cpu和mem占用信息
### linux 命令分割符 `;`/`&&`/`||`
    - 逻辑符
       `;` 命令会按顺序执行，即使中间命令使用方式不对，后续命令还会继续执行
       `&&`: 当某个命令执行失败后，后续的命令不会执行。
       `||`: 那么一遇到可以执行成功的命令就会停止执行后面的命令，而不管后面的命令是否正确。如果执行到错误的命令就是继续执行后一个命令，直到遇到执行到正确的命令或命令执行完为止。
    -  其他
       `&` 并行执行
       `$`

### cp # mv 
   - 移动和复制文件夹时复制隐藏文件
      - `mv a/* a/.[^.]* target`
   - cp 和 mv 可以使用这样的方法 mv source_file1 source_file2 ... target_path; cp 多个文件
   - cp -r dir /path/to/target 会在target内有一个dir文件夹
   - cp -r dir/* /path/to/target/ 会把dir内的文件放在target下面

### ln 软连接与硬链接
    - ln target linkname 创建指向target 的linkname
    - 软连接是ln -s 硬链接是ln 不加s
    - 修改链接要-snf 不能直接ln -s target new_linkname
### grep
    - 怎么高亮输出中目标字符串, 如cat xxx|grep "str" 还显示xxx的全部内容,只是高亮str呢? --------------no
    - grep 怎么只搜索文件夹中的某个文件类型 -------------------------------------------------------no
    - grep 怎样直接从字符串中搜索，不用echo ------------------------------------------------------no
    - grep中的通配符是. *是匹配0次或者多次
    - link：
       - https://blog.csdn.net/kikajack/article/details/80020772
       - [Grep命令详解-9个经典使用场景](https://www.open-open.com/lib/view/open1426417914694.html)
       - [link](https://www.cnblogs.com/zhangyuhang3/p/6873900.html)
       - https://it.cha138.com/shida/show-432052.html
    - 如果没有必要，就不用在两头加`.*`
    - grep 如果只搜索文件夹a却不搜索a中的文件夹b
      - `grep -R --exclude-dir=/path/no/search/(可以有通配符) 'search pattern' /path/to/want/search`
      - des: `        agoods_btn_posb = 2\n` `grep ".*goods_btn_pos.*" -r tests/` 无结果 `grep ".*goods_btn_pos." -r tests/` 有结果 ---------------------no
    - -d skip 跳过子文件夹
    - -r 搜索子文件夹
    - -l 表示仅列出符合条件的文件名，用来传给sed命令做操作
    - –include="*.txt" 表示仅查找txt文件 可以有多个`sed -i s/park/break/g `grep park -rl --include="*.java" --include="*.aidl"`
    - 带符号时要转义， 要不搜索不出来`grep --help|grep '\-filename'`
      - grep "pattern\(\)"
    - -h -H 前者不显示文件名,后者显示
    - --context=5 显示结果上下5行  
    - -c 显示结果符合的个数 
    - -v,–invert-match 参数显示不符合的总行数
    - -a --text 不忽略二进制数据（当匹配到`\000 NUL` 会认为文件是二进制文件）如果不加 会显示匹配到二进制文件xxx 而不显示文件中的内容
    - 在文件中搜索 `grep  ".aaa." <通配符文件名 或者多个文件名已空格隔开>`
    - -r 在文件夹中递归搜索 -r <dir or *filetype>  `grep ".aaa." -r .` 如果没有*.filetype 会报错
    - -n 会在搜索结果中结果在文件中的行数
    - -v 排除含有结果的
      - grep 中过滤grep的内容 ps -ef|grep xxx|grep -v grep
    - 不知道怎么在grep中使用正则表达式，按照通常的写法写不出来,不知道扩展正则表达式都有什么
      - [懂了](https://blog.csdn.net/yufenghyc/article/details/51078107))
      - https://www.cnblogs.com/codelogs/p/16060372.html
      - grep 什么都不加是基本正则表达式、-E 扩展正则表达式、-P perl正则表达式
      - grep -E "RefFru|CardTyped" 搜索A或者B，如果A、B都存在会都显示 可以和别的选项结合 `ls *|grep -vE "tem|src"` 结果中排除tem和src
      - [[:digit:]]要这样用，有两个方括号
    - -跨行搜索 (有的版本好像没有用)
      - -z ` grep -Pzo "metadata:\s*\n  name:.*$" deployment.yaml`
      - egrep -o '(?s)# res_start.*?# res_end' 文件名(?s) 是一个正则表达式标志，用于启用 "dotall" 模式，使 . 可以匹配任意字符（包括换行符）。
      - grep -Pzo '(?s)(?<=# res_start\n).*?(?=# res_end)'
    - zgrep 搜索压缩文件
    - -F 它只能找固定的文本，而不是规则表达式。
      - grep -F step* 的*不是通配符了
    - -x 匹配整行
      - grep -x aaaa == grep '^aaaa$'
    - -w 精确匹配 - Fx 完全匹配 
      ```
      -w 只显示和搜索结果完全符合的行，就是行中不能有其他内容 可以使用正则 会忽略空格带来的不同
      -x 只显示和搜索结果完全符合的行，就是行中不能有其他内容 可以使用正则 不会忽略空格带来的不同
      -F 将样式视为固定字符串的列表。
      $ grep -Fx ls_recurse_enable=YES  /etc/vsftpd/vsftpd.conf
      ls_recurse_enable=YES
      ```
   - -A 1 'add_workers:': 使用 -A 1 来获取包含 add_workers: 的行以及下一行。
    - -i 忽略大小写
    - 搜索这个或者那个 grep搜索多个字符串
      - grep “des_a\|des_b\|des_c” a.text # 当使用基本正则表达式时，需要使用\转义符为|管道符转义。
      - 使用扩展模式，就不需要为|管道符添加转义符了 grep "des_a|des_b|des_c"
    - -o 只显示匹配的部分 
    - 结果所在行长度太长 可以用在行长度太长的 或者
      - grep -oE ".{0,20}$2.{0,20}" -o 只输出匹配的部分。 如果只加这个选项，那么就输出N行的$2。-E 使用扩展的正则(有人提到用-P，Perl正则，但是在我这里出现错误) 后面的正则表达式用来匹配前后20个字符。
      - grep xxx|cut -c1-n. 把grep输出结果给cut就行了. 其中n为你想输出的最后一个字符，你想输出前5个，n就等于5
      - https://zditect.com/article/11096204.htm 
    - -H  --with-filename : 在显示符合样式的那一行之前，表示该行所属的文件名 
       - `find . -name "*.txt" -ctime -7 -exec grep  -H -E ".*jinshan.*open.*004.*" {} \;` grep 在find -exec选项中显示文件名
    - 搜索选项 `grep "\-c"`  
    - -q 不打印任何标准输出, 但是有错误会打印; 如果有结果,返回0;如果有错误,返回错误码. 可用于if
    - 过滤重复的结果
      - cat  /home/qdam/qmarket*/*/*.log|grep topicid|grep -v topicid=300
      - cat  /home/qdam/qmarket*/*/*.log|grep -o "topicid=30[[:digit:]]"|uniq

   - pcre2grep或者pcregrep 不同的版本
      - -M 多行匹配，但仍需要写额外的换行符
      - pcre2grep -M 'xxx(\n|.)*xxx' file # 需要手动加入\n
      - pcre2grep -M '(?s)xxx.*xxx' file # (?s) 是一个正则表达式标志，用于启用 "dotall" 模式，使 . 可以匹配任意字符（包括换行符）。需要手动jiar
   - ripgrep
      - link:
         - https://zhuanlan.zhihu.com/p/401086621
         - https://docs.rs/regex/1.3.5/regex/#grouping-and-flags
         - https://gitcode.gitcode.host/docs-cn/ripgrep-docs-cn/GUIDE.html
      - chroot rootfs/ sbin/apk add ripgrep
      - rg -z -U -N -o --pcre2 '(?s)(?<=# res_start\n).*(?=# res_end)' prometheus-config.yaml
         - -z 参数用于处理跨行匹配。
         - -N 参数用于禁用二进制文件搜索。
         - -o 参数用于只输出匹配的内容，而不是整行内容。
         - --pcre2 表示使用的正则版本
         - (?s) 是一个正则表达式标志，用于启用 "dotall" 模式，使 . 可以匹配任意字符（包括换行符）。需要手动jiar

### mkdir
   - -v 在每个文件夹下都创建`mkdir -pv ./{nginx,mysql,httpd}/{files,templates,vars,tasks,handlers,meta,default}`

### [shell set](https://blog.csdn.net/t0nsha/article/details/8606886)
	- man set
	- [脚本前指定解释器加-e 可以自动判断每条指令的执行结果，如果非0，脚本就会自动退出](https://www.cnblogs.com/dakewei/p/9845970.html)
    - shell 脚本是这样，别的不知道
    - 等价于 set -e
    - 有弊端， 比如先删除后新建的语句（如果删除的不存在会报错导致脚本退出）
    - set -e pipefail 返回从右往左第一个非零返回值，即ls的返回值1
    ```shell
	# # test.sh
	set -o pipefail
	ls ./a.txt |echo "hi" >/dev/null
	echo $?
	$ ./test.sh
	ls: ./a.txt: No such file or directory
	# 设置了set -o pipefail，返回从右往左第一个非零返回值，即ls的返回值1
	# 注释掉set -o pipefail 这一行，再次运行，输出：
	ls: ./a.txt: No such file or directory
	0  # 没有set -o pipefail，默认返回最后一个管道命令的返回值
	```
      
# 通识
### linux中的通配符
    1. 命令中的通配符是. 
    2. 命令行下*是等于正则中的.*
    3. linux 命令中的通配符是*，grep中的通配符是. *是匹配多次

### 应用一般安装在/usr/share/ /usr/local 下

### 按 ctrl 在命令中 以单词为单位跳转

# commands
1. `cd /home/huawei/Desktop/autotest/;find . -type d -name "*$(date +%Y%m%d)*" -o -name "*$(date +%Y%m%d)*.txt" |tar -zcvf 111back.tar.gz -T -&&scp 111back.tar.gz huawei@90.90.0.152:/home/huawei/Desktop/smoke/.`
2. `mkdir -p 11{1..5};rm -rf 11[1-5]/*; for file in `ls *.gz`; do dir=$(echo $file|grep -E -o "[0-9]{3}"); tar -zxf $file -C $dir; cp $dir/*.txt $(ls ./${dir}/*.txt|sed "s/kbox_r.*t_/${dir}_/g"); done; find . -name "*.txt" -exec python3 find_author.py {} \;`
3. `for file in `find . -type f -name kbo*x*.txt`; do python3 find_author.py $file; done`
4. `for dir in `find / -type d -iname kbox 2>/dev/null`; do find $dir -type f -name "*.sh" 2>/dev/null; done;`
5. `for dir in 11[1,4]; do cd $dir; file=$(find . -type f -ctime -1 -name kbox*.txt); echo file:$file; [ ! -n "$file" ] && echo 'not file: ${#file}' &&cd ../&&continue; echo "getfile"; python3 ./../find_author.py $file; cp $file $dir.txt; cd ../; done`
- `sh -c ps -Awwo nice,pid,ppid,comm,args|grep snmptrapd; kill -9 pid`
- 创建命令软链接 `ln -s /usr/local/redis/bin/redis-cli /usr/bin/redis`

# 语法糖
```shell 
1. cp a{,.bak} # cp a a.bak
2. mkdir logs/2019{01..12}{01..30
3. rm 113/* 把113里的文件删除不删除113
```
