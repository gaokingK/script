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
   - `{print $NF}` 输出切割后的最后一项; `'{print $(NF-1)}` 倒数第二项
   - 可以指定多个分隔符 `awk -F '[b,]' ` 先使用b，后使用，
   - length 方法获取字符串的长度 `echo ${str}|awk '{print length($0)'`
### scp
   - scp 文件 `scp file_path target_file_path/target_dir_path`  如果要重命名， target_file_path 不存在也可以
   - 如果要放到文件夹中 `scp file_path target_dir_path/.` dir_path/. 要加 `/.`
   - scp 可以直接带密码 scp username:passwd@ip:/path/to/file
### netstat
   - netstat -ntl |grep -v Active| grep -v Proto|awk '{print $4}'|awk -F: '{print $NF}' 获取正在使用的端口
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
   - -N 显示每行的行号
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

### ps -ef|-aux 区别 -------------------------no
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
### linux中单引号‘ ,双引号“, 反引号 ` `, $, $(), ${}与变量；shell中各种括号的作用()、(())、[]、[[]]、{}
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
   - ${ }中放的是变量，例如echo ${hello}取hello变量的值并打印，也可以不加括号比如$hello。但加了括号可以对变量操作参见 变量替换
   - () 是开一个子shell执行里面的命令
### read [option] [变量名] 接受键盘输入
   ![提示信息](https://images2015.cnblogs.com/blog/35158/201610/35158-20161011104351477-686622915.png)
### echo
   - -n 不换行输出 `echo -n "aaa" && echo "bbb"`
   - -e 处理特殊字符: \a 发出警告声； \b 删除前一个字符; \c不换行；
   - 可以输出多个`echo "a" "a" ..`
   - 使用命令新建文本文件（有的内核不需要-e参数）  `echo -e 1\n2 > 1.txt`
### [zsh 的命令行中快速输入sudo](http://www.ichenfu.com/2017/03/29/bash-zsh-fast-sudo/)
   - `bindkey -s '\e\e' '\C-asudo \C-e'`
### tar zip
   - [link](http://blog.chinaunix.net/uid-29132766-id-3862597.html)
   - 如果a/中有b,c,d文件, 然后在a的父文件中tar .... a/ 那么解压出来 也会有个a/ 就不必在创建a/然后在-C a/了,那样就有两层
   - -z 通过gzip指令处理备份文件
   - -v 显示处理信息
   - -f file 指定文件
   - -c -x -A -t
      -c 建立新的备份文件
      -A或--catenate 新增文件到已存在的备份文件。----------------------no
      -x 从备份文件中还原文件 
      -t 列出备份文件的内容
   - `tar -tzvf test.tar.gz ` 列出压缩文件内容
   - -C 解压到指定路径 如果不存在会报错 
   - -T 指定范本文件，其内含有一个或多个范本样式，让tar解开或建立符合设置条件的文件。 还可以这样
     - `find . -name "*.d" -o -name "*.conf" | tar -czvf etc.tar.gz -T -` ---------------------------------------这个 最后的- 是干啥的
   - tar --atime-preserve=system -zxvf autotest.tar.gz 原来的时间
   - **zip**
   - zip [option] dist.zip source
   - -q 不显示指令执行过程。
   - -r 递归处理，将指定目录下的所有文件和子目录一并处理。
### find
   - find 里面的选项可以加（）但必须注意空格，也需要把被包括的命令的全部参数给包括进去 比如`；`
   - find [path1, path find 111 112 -name *.txt 可以在112 111 中寻找txt
   - -name "" 要用双括号包围， 单括号也可以
   - `find . -type d -name "*$(date +%Y%m%d)*" -o -maxdepth 1 -name "*$(date +%Y%m%d)*.txt" `  为什么会失败? ------------------------------no
   - 是否可以使用find 查找目录结构如`\a\b\`，而不是去查找文件夹,单独find不能完成。
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
   - -path 模糊匹配路径 `find . -path '*20190326/access.log'`
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
      ```shell
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

### nl filename 带行号显示文件内容
### [sed](https://www.runoob.com/linux/linux-comm-sed.html）
- link:
    - [官方文档](https://www.gnu.org/software/sed/manual/html_node/sed-commands-list.html#sed-commands-list)
    - [详细](https://blog.csdn.net/hdyebd/article/details/83617292)
- #### 参数
     - 可以使用sed [opt] 4a\ "str_append" filename # 这样来输入（防止字符串来转义）
    - **命令应该使用单引号不应该使用双引号** 不加引号的话应该用\来分割`sed -e 1a\ hhhh\ sss change_pc_90.90.0.140.md`
    - -i 直接修改文件
    - -e<script>或--expression=<script> 以选项中指定的script来处理输入的文本文件。
- #### 动作
    - $ 代表最后一行
    - 使用正则`echo "xxxxx"|sed "s/re_/substance/g`
    - a：新增
    ```
    sed -e 4a\ newLine testfile # 在第4行后添加
    ```
    - i：插入 `sed -e 4inewline` # 在第4行前添加
    - ! ：表示后面的命令对所有没有被选定的行发生作用 `sed '1!d' input.in`
    - r 从文件读取
- #### 注意
  	- 如何将命令的结果作为sed的输入
        - link
            - https://www.thinbug.com/q/39317465
    - `cmd | sed -i '6r /dev/stdin' file_name` # 在第6行后插入
    - 输入换行`sed -e '1i /\nhhhh' file_name`
    - sed -i "1a aa" a.txt 如果a是空文件，会写不进去
    - string = "113/kbox_result_202110180959.txt" ls 113/*.txt|sed "s/*kbox_r.*t_//g" 为什么kbox的那个星号没有用，因为sed也能用正则，但是*号代表前个模式匹配0次或者多次， 但为什没有用呢？难道前面不是null吗

### ps -ef/ aux/ -aux的区别
    - 显示的风格不同;aux会截断命令,如果后面配合grep可能会影响效果;
### linux 命令分割符 `;`/`&&`/`||`
    - 逻辑符
       `;` 命令会按顺序执行，即使中间命令使用方式不对，后续命令还会继续执行
       `&&`: 当某个命令执行失败后，后续的命令不会执行。
       `||`: 那么一遇到可以执行成功的命令就会停止执行后面的命令，而不管后面的命令是否正确。如果执行到错误的命令就是继续执行后一个命令，直到遇到执行到正确的命令或命令执行完为止。
    -  其他
       `&` 并行执行
       `$`

### 移动和复制文件夹时复制隐藏文件
    - `mv a/* a/.[^.]* target`
    - cp 和 mv 可以使用这样的方法 mv source_file1 source_file2 ... target_path; cp 多个文件

### ln 软连接与硬链接
    - ln target linkname 创建指向target 的linkname
    - 软连接是ln -s 硬链接是ln 不加s
    - 修改链接要-snf 不能直接ln -s target new_linkname
### grep
    - 怎么高亮输出中目标字符串, 如cat xxx|grep "str" 还显示xxx的全部内容,只是高亮str呢? --------------no
    - grep 怎么只搜索文件夹中的某个文件类型 -------------------------------------------------------no
    - grep 怎样直接从字符串中搜索，不用echo ------------------------------------------------------no
    - [Grep命令详解-9个经典使用场景](https://www.open-open.com/lib/view/open1426417914694.html)
    - [link](https://www.cnblogs.com/zhangyuhang3/p/6873900.html)
    - 如果没有必要，就不用在两头加`.*`
    - grep 如果只搜索文件夹a却不搜索a中的文件夹b
      - `grep -R --exclude-dir=/path/no/search/(可以有通配符) 'search pattern' /path/to/want/search`
      - des: `        agoods_btn_posb = 2\n` `grep ".*goods_btn_pos.*" -r tests/` 无结果 `grep ".*goods_btn_pos." -r tests/` 有结果 ---------------------no
    - -d skip 跳过子文件夹
    - -r 搜索子文件夹
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
      - grep 什么都不加是基本正则表达式、-E 扩展正则表达式、-P perl正则表达式
      - grep -E "RefFru|CardTyped" 搜索A或者B，如果A、B都存在会都显示 可以和别的选项结合 `ls *|grep -vE "tem|src"` 结果中排除tem和src
    - zgrep 搜索压缩文件
    - -F 它只能找固定的文本，而不是规则表达式。
      - grep -F step* 的*不是通配符了
    - -x 匹配整行
      - grep -x aaaa == grep '^aaaa$'
    - -w 精确匹配 - Fx 完全匹配 
      ```
      $ grep -Fx ls_recurse_enable=YES  /etc/vsftpd/vsftpd.conf
      ls_recurse_enable=YES
      ```
    - -i 忽略大小写
    - 搜索这个或者那个 grep搜索多个字符串
      - grep “des_a\|des_b\|des_c” a.text # 当使用基本正则表达式时，需要使用\转义符为|管道符转义。
      - 使用扩展模式，就不需要为|管道符添加转义符了 grep "des_a|des_b|des_c"
    - -o 只显示匹配的部分
    - -H  --with-filename : 在显示符合样式的那一行之前，表示该行所属的文件名 
       - `find . -name "*.txt" -ctime -7 -exec grep  -H -E ".*jinshan.*open.*004.*" {} \;` grep 在find -exec选项中显示文件名
    - 搜索选项 `grep "\-c"`  
    - -q 不打印任何标准输出, 但是有错误会打印; 如果有结果,返回0;如果有错误,返回错误码. 可用于if

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
      

### linux中的通配符
    1. 命令中的通配符是. 
    2. 命令行下*是等于正则中的.*
    3. linux 命令中的通配符是*，grep中的通配符是.

# 通识
### 环境变量应该在~/.bash_profile中定义
   1. `export XXX="xxx"`

# commands
1. `cd /home/huawei/Desktop/autotest/;find . -type d -name "*$(date +%Y%m%d)*" -o -name "*$(date +%Y%m%d)*.txt" |tar -zcvf 111back.tar.gz -T -&&scp 111back.tar.gz huawei@90.90.0.152:/home/huawei/Desktop/smoke/.`
2. `mkdir -p 11{1..5};rm -rf 11[1-5]/*; for file in `ls *.gz`; do dir=$(echo $file|grep -E -o "[0-9]{3}"); tar -zxf $file -C $dir; cp $dir/*.txt $(ls ./${dir}/*.txt|sed "s/kbox_r.*t_/${dir}_/g"); done; find . -name "*.txt" -exec python3 find_author.py {} \;`
3. `for file in `find . -type f -name kbo*x*.txt`; do python3 find_author.py $file; done`
4. `for dir in `find / -type d -iname kbox 2>/dev/null`; do find $dir -type f -name "*.sh" 2>/dev/null; done;`
5. `for dir in 11[1,4]; do cd $dir; file=$(find . -type f -ctime -1 -name kbox*.txt); echo file:$file; [ ! -n "$file" ] && echo 'not file: ${#file}' &&cd ../&&continue; echo "getfile"; python3 ./../find_author.py $file; cp $file $dir.txt; cd ../; done`

# 语法糖
```shell 
1. cp a{,.bak} # cp a a.bak
2. mkdir logs/2019{01..12}{01..30
3. rm 113/* 把113里的文件删除不删除113
```
