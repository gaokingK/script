1. #### read [option] [变量名] 接受键盘输入
   ![提示信息](https://images2015.cnblogs.com/blog/35158/201610/35158-20161011104351477-686622915.png)
2. #### echo
   1. -n 不换行输出 `echo -n "aaa" && echo "bbb"`
   2. -e 处理特殊字符: \a 发出警告声； \b 删除前一个字符；
3. #### [zsh 的命令行中快速输入sudo](http://www.ichenfu.com/2017/03/29/bash-zsh-fast-sudo/)
   - `bindkey -s '\e\e' '\C-asudo \C-e'`
4. #### tar
   - `tar -tzvf test.tar.gz ` 列出压缩文件内容
5. #### find
   是否可以使用find 查找目录结构如`\a\b\`，而不是去查找文件夹,单独find不能完成。
   `find  / -type d -name "b" |grep "\a\b"` 注意`b`写在find里面，而grep中写`b`而不是`b/`
   超哥提供了另外一种方法 `ls -F /*/*/*/*/*|grep /a/b/`但这样没有响应
   -cmin n 查询在过去n分钟内修改的文件(创建也是修改)
6. #### sed -i "1a aa" a.txt 如果a是空文件，会写不进去
7. #### ps -ef/ aux/ -aux的区别
   显示的风格不同;aux会截断命令,如果后面配合grep可能会影响效果;
8. #### linux 命令分割符 `;`/`&&`/`||`
    - 逻辑符
       `;` 命令会按顺序执行，即使中间命令使用方式不对，后续命令还会继续执行
       `&&`:当首个命令执行失败后，后续的命令不会执行。
       `||`:当首个命令执行失败后，后续的命令还会继续执行
    -  其他
       `&` 并行执行
       `$`

9.  #### 移动和复制文件夹时复制隐藏文件
    - `mv a/* a/.[^.]* target`
    - cp 和 mv 可以使用这样的方法 mv source_file1 source_file2 ... target_path

10. #### 软连接与硬链接
    - ln target linkname 创建指向target 的linkname
    - 软连接是ln -s 硬链接是ln 不加s
    - 修改链接要-snf 不能直接ln -s target new_linkname
11. #### linux 命令中的通配符是*，grep中的通配符是.
12. #### grep使用
    - --context=5 显示结果上下5行  
    - -c 显示结果符合的个数  
    - -a --text 不忽略二进制数据（当匹配到`\000 NUL` 会认为文件是二进制文件）如果不加 会显示匹配到二进制文件xxx 而不显示文件中的内容
    - 在文件中搜索 `grep  ".aaa." <通配符文件名 或者多个文件名已空格隔开>`
    - 在文件夹中递归搜索 -r <dir or *filetype>  `grep ".aaa." -r .`
    - -n 会在搜索结果中结果在文件中的行数
    - -v 排除含有结构的
    - 不知道怎么在grep中使用正则表达式，按照通常的写法写不出来,不知道扩展正则表达式都有什么
    - [懂了](celerycn.io/ru-men/celery-chu-ci-shi-yong)
    - grep 什么都不加是基本正则表达式、-E 扩展正则表达式、-P perl正则表达式
    - zgrep 搜索压缩文件
13. #### 使用命令新建文本文件（有的内核不需要-e参数）
   `echo -e 1\n2 > 1.txt`
11. #### find 的有效输出到文件中
    ```bash
    find / -name "*ython3.*" 2 > invalid.txt
    find / -name "*ython3.*" 1 > valid.txt
    ```
12. #### [脚本前指定解释器加-e 可以自动判断每条指令的执行结果，如果非0，脚本就会自动退出](https://www.cnblogs.com/dakewei/p/9845970.html)
    - shell 脚本是这样，别的不知道

### 通识
1. ### 环境变量应该在~/.bash_profile中定义
   1. `export XXX="xxx"`
