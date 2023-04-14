# doc comm
   1. [link1](http://www.gnu.org/software/bash/manual/bash.html#Process-Substitution)
   - https://wangchujiang.com/linux-command/c/find.html
# other
### tmux 
- link: http://www.ruanyifeng.com/blog/2019/10/tmux.html
- 新建窗口： ctrl + b, c
- 切换窗口：ctrl + b, n
 
### CentOS系统Tab补全功能
- link: https://blog.csdn.net/RunSnail2018/article/details/81185957
- yum install bash-completion
### pkill
- Linux pkill 用于杀死一个进程，与 kill 不同的是它会杀死指定名字的所有进程，类似于 killall 命令
- -t 指定开启进程的终端
- 也能发送信号
### 发送ctrl+c `sh', '-c', '\x03'`
### 应用一般安装在/usr/share/ /usr/local 下
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
### shell 多行注释
   ```shell
   # 方法1 block自定义的单词（可以是字符） 推荐
   :<<！
   被注释的内容
   block
   ！
   # or
   :'
   被注释的内容
   '
   ```
### 查看端口
   - 端口是否被占用`lsof -i 8080`
     - link: https://www.runoob.com/w3cnote/linux-check-port-usage.html
     - 应该用root来执行，否之看不到
   - netstat -tunlp 用于显示 tcp，udp 的端口和进程等相关情况。`netstat -tunlp | grep 8000`
     - -t (tcp) 仅显示tcp相关选项Administrator  
     - -u (udp)仅显示udp相关选项
     - -n 拒绝显示别名，能显示数字的全部转化为数字
     - -l 仅列出在Listen(监听)的服务状态
     - -p 显示建立相关链接的程序名
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
### 进程替换 与 Here document --------------no
   - 形如<(command)的写法叫做**process substitution**
   - [解释了底层怎样支持](https://www.oschina.net/question/113421_241288)
   - [进程替换](https://www.runoob.com/w3cnote/shell-process-substitution.html) ---------no
   - [Here document使用方法总结](https://blog.csdn.net/liumiaocn/article/details/86715953) -------------no
   - 可以把<(...)整体当做一个文件名，这个文件的内容就是()中脚本的执行结果，这样第二条命令简化为`bash -s stable <tmp.sh`
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
### alias 使用外部传参
   ```shell
   alias s='UpMachine(){ ssh root@$1;};UpMachine'
   $ s 192.168.22.2
   # 其实就是相当于写一个行命令 把参数不放在alias当中(怎么不放呢,就通过函数实现)
   ``` 
