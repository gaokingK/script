1. #### if test
   - [link](https://blog.csdn.net/qq_37960324/article/details/83145412)
   - [关于test的，选项好像也能通用](https://www.cnblogs.com/shaoshao/p/6809580.html)
   - -n str 当串的长度大于0时为真(串非空)
     ```shell
     args=''
     [ -n $args] && echo "not null" # 结果是not null
     [ -n "$args"] && echo "not null" # 结果是无输出 这个是正确用法
     # 不加“”时该if语句等效于if [ -n ]，shell 会把它当成if [ str1 ]来处理，-n自然不为空，所以为正
     # 需要加双引号
     ```
   - -z str 串的长度为0时为真
   - [str] 串非空时为真 和 -n 有什么区别呢?--------------------no
   - -e file_name 文件是否存在
   - [] bash 的内部命令，[和test是等同的。如果我们不用绝对路径指明，通常我们用的都是bash自带的命令。if/test结构中的左中括号是调用test的命令标识，右中括号是关闭条件判断的。这个命令把它的参数作为比较表达式或者作为文件测试，并且根据比较的结果来返回一个退出状态码。if/test结构中并不是必须右中括号，但是新版的Bash中要求必须这样。
   - true = 0 flase = 1 和python 刚好相反

2. #### 语句
   - `[ $? -ne 5 ] && echo "haha"` 不等于5就输出hahah
   - `[ $? -ne 5 ] && echo "haha" && echo "no"` ------------------------no

3. #### continue break
   - link: http://c.biancheng.net/view/1011.html
   - break n n 表示跳出循环的层数，如果省略 n，则表示跳出当前的整个循环。break 关键字通常和 if 语句一起使用，即满足条件时便跳出循环。
   - continue n 
4. #### select in
   - link: http://c.biancheng.net/view/2829.html
   - select in 循环用来增强交互性，它可以显示出带编号的菜单
   - 就像for循环, 即使原内容没有了, 只会报错

5. #### for 
   - 语句
   ```
   huawei ~/Desktop/smoke% for dir in 11[1,4]; do echo $dir;done
   111
   114
   ```