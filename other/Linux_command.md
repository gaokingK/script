1. #### date 
   - [时间域](https://www.cnblogs.com/yy3b2007com/p/8098831.html)
   - `echo $(date +%y%m%d) ` m 是月 M 是分  中间的加号后面不能有空格 
   
2. #### xargs 怎么只接受一次参数 ------------------------------------------------no
3. #### ls 
   1. ls -t 按时间顺序显示
   2. ls -r 显示文件夹中
4. #### linux中单引号‘ ,双引号“, 反引号 ` `, $, $(), ${}与变量
   1. 使用$来使用变量 echo $a
   2. 变量赋值的时候, 如果含有空格 需要用单引号或者双引号
   3. 单引号剥夺了所有字符的特殊含义, 里面的就是单纯的字符, 双引号不会
   4. $(cmd) 会将命令的执行结果赋值给变量 如 `a=$(echo aaa)`; 反引号也可以 for line in `ls *.apk`
   5. ${ }中放的是变量，例如echo ${hello}取hello变量的值并打印，也可以不加括号比如$hello。
5. #### read [option] [变量名] 接受键盘输入
   ![提示信息](https://images2015.cnblogs.com/blog/35158/201610/35158-20161011104351477-686622915.png)
6. #### echo
   1. -n 不换行输出 `echo -n "aaa" && echo "bbb"`
   2. -e 处理特殊字符: \a 发出警告声； \b 删除前一个字符；
7. #### [zsh 的命令行中快速输入sudo](http://www.ichenfu.com/2017/03/29/bash-zsh-fast-sudo/)
   - `bindkey -s '\e\e' '\C-asudo \C-e'`
8. #### tar
   - [link](http://blog.chinaunix.net/uid-29132766-id-3862597.html)
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
9.  #### find
   - `find . -type d -name "*$(date +%Y%m%d)*" -o -maxdepth 1 -name "*$(date +%Y%m%d)*.txt" `  为什么会失败? ------------------------------no
   - 是否可以使用find 查找目录结构如`\a\b\`，而不是去查找文件夹,单独find不能完成。
      `find  / -type d -name "b" |grep "\a\b"` 注意`b`写在find里面，而grep中写`b`而不是`b/`
      超哥提供了另外一种方法 `ls -F /*/*/*/*/*|grep /a/b/`但这样没有响应
   - -cmin n 查询在过去n分钟内修改的文件(创建也是修改)
   - -ctime n n天修改
   - -amin n n 分钟读取
   - find 的有效输出到文件中
      ```bash
      find / -name "*ython3.*" 2 > invalid.txt
      find / -name "*ython3.*" 1 > valid.txt
      ```
   - -o -a -not: 
      -o 是或者的意思
      -a 是而且的意思  
      -not 是相反的意思
   - [link](https://blog.csdn.net/earthchinagl/article/details/79501778)
   - [linux find子目录，当前目录，指定（排除）目录查找文件](http://www.51gjie.com/linux/1025.html)
      ```shell
      find / -name "*tomcat.txt" -maxdepth 1 -print     //在当前目录中，查找包含tomcat.txt文件，-maxdepth 1表示查找深度为1
      # 指定(排除)目录查找文件
      find . -path "./code" -prune -o -name "*.txt" -print  //在当前目录除code之外的子目录内搜索 txt文件
      find . \(-path "./code" -o -path "./code2" \) -prune -o -name "*.txt" -print     //在当前目录及除code和code2之外的子目录中查找txt文件
      ```
   - -print ----------------------------no
      `find . -path "./tests" -prune -o -name "*.py" -print` 不加print会多输出一行 ./tests

10. #### nl filename 带行号显示文件内容
11. #### [linux 单引号‘ ,双引号“, 反引号 ` `, $, $(), ${}与变量](https://blog.csdn.net/qq_40491569/article/details/83688652)
12. #### [sed](https://www.runoob.com/linux/linux-comm-sed.html)
   1. 命令应该使用单引号不应该使用双引号
   2. -i 直接修改文件
   3. -e '$assssss' filename 在最后一行后添加aaaaaa
   4. $ 代表最后一行
   5. 最后一行追加 `sed -i '$a # This is a test' regular_express.txt`
   6. sed -i "1a aa" a.txt 如果a是空文件，会写不进去
13. #### ps -ef/ aux/ -aux的区别
   显示的风格不同;aux会截断命令,如果后面配合grep可能会影响效果;
11. #### linux 命令分割符 `;`/`&&`/`||`
    - 逻辑符
       `;` 命令会按顺序执行，即使中间命令使用方式不对，后续命令还会继续执行
       `&&`: 当某个命令执行失败后，后续的命令不会执行。
       `||`: 那么一遇到可以执行成功的命令就会停止执行后面的命令，而不管后面的命令是否正确。如果执行到错误的命令就是继续执行后一个命令，直到遇到执行到正确的命令或命令执行完为止。
    -  其他
       `&` 并行执行
       `$`

12. #### 移动和复制文件夹时复制隐藏文件
    - `mv a/* a/.[^.]* target`
    - cp 和 mv 可以使用这样的方法 mv source_file1 source_file2 ... target_path

13. #### 软连接与硬链接
    - ln target linkname 创建指向target 的linkname
    - 软连接是ln -s 硬链接是ln 不加s
    - 修改链接要-snf 不能直接ln -s target new_linkname
14. #### linux 命令中的通配符是*，grep中的通配符是.
15. #### grep
    - [Grep命令详解-9个经典使用场景](https://www.open-open.com/lib/view/open1426417914694.html)
    - [link](https://www.cnblogs.com/zhangyuhang3/p/6873900.html)
    - 如果没有必要，就不用在两头加`.*`
    - grep 如果只搜索文件夹a却不搜索a中的文件夹b
      - `grep -R --exclude-dir=/path/no/search/(可以有通配符) 'search pattern' /path/to/want/search`
      - des: `        agoods_btn_posb = 2\n` `grep ".*goods_btn_pos.*" -r tests/` 无结果 `grep ".*goods_btn_pos." -r tests/` 有结果 ---------------------no
    - -d skip 跳过子文件夹
    - -r 搜索子文件夹
    - 带符号时要转义， 要不搜索不出来`grep --help|grep '\-filename'`
    - -h -H 前者不显示文件名,后者显示
    - --context=5 显示结果上下5行  
    - -c 显示结果符合的个数  
    - -a --text 不忽略二进制数据（当匹配到`\000 NUL` 会认为文件是二进制文件）如果不加 会显示匹配到二进制文件xxx 而不显示文件中的内容
    - 在文件中搜索 `grep  ".aaa." <通配符文件名 或者多个文件名已空格隔开>`
    - -r 在文件夹中递归搜索 -r <dir or *filetype>  `grep ".aaa." -r .` 如果没有*.filetype 会报错
    - -n 会在搜索结果中结果在文件中的行数
    - -v 排除含有结果的
      - grep 中过滤grep的内容 ps -ef|grep xxx|grep -v grep
    - 不知道怎么在grep中使用正则表达式，按照通常的写法写不出来,不知道扩展正则表达式都有什么
      - [懂了](https://blog.csdn.net/yufenghyc/article/details/51078107))
      - grep 什么都不加是基本正则表达式、-E 扩展正则表达式、-P perl正则表达式
    - zgrep 搜索压缩文件
    - -w 精确匹配 - Fx 完全匹配
      ```
      $ grep -Fx ls_recurse_enable=YES  /etc/vsftpd/vsftpd.conf
      ls_recurse_enable=YES
      ```
    - -i 忽略大小写
    - 搜索这个或者那个
      - grep “des_a\|des_b\|des_c” a.text

16. #### 使用命令新建文本文件（有的内核不需要-e参数）
   `echo -e 1\n2 > 1.txt`

12. #### [脚本前指定解释器加-e 可以自动判断每条指令的执行结果，如果非0，脚本就会自动退出](https://www.cnblogs.com/dakewei/p/9845970.html)
    - shell 脚本是这样，别的不知道

13. #### linux中的通配符
    1. 命令中的通配符是. 
    2. 命令行下*是等于正则中的.*
### 通识
1. ### 环境变量应该在~/.bash_profile中定义
   1. `export XXX="xxx"`
