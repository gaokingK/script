1. #### 软连接与硬链接
    - ln target linkname 创建指向target 的linkname
    - 软连接是ln -s 硬链接是ln 不加s
    - 修改链接要-snf 不能直接ln -s target new_linkname
1. #### linux 命令中的通配符是*，grep中的通配符是.
1. #### grep使用
    - 在文件中搜索 `grep  ".aaa." <通配符文件名 或者多个文件名已空格隔开>`
    - 在文件夹中递归搜索 -r <dir or *filetype>  `grep ".aaa." -r .`
    - -n 会在搜索结果中展示行数
1. #### 使用命令新建文本文件（有的内核不需要-e参数）
    `echo -e 1\n2 > 1.txt`
2. #### find 的有效输出到文件中
    ```bash
    find / -name "*ython3.*" 2 > invalid.txt
    find / -name "*ython3.*" 1 > valid.txt
    ```
3. #### [脚本前指定解释器加-e 可以自动判断每条指令的执行结果，如果非0，脚本就会自动退出](https://www.cnblogs.com/dakewei/p/9845970.html)
    - shell 脚本是这样，别的不知道
