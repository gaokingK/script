1. #### if test
   - [link](https://blog.csdn.net/qq_37960324/article/details/83145412)
   - [关于test的，选项好像也能通用](https://www.cnblogs.com/shaoshao/p/6809580.html)
   - -n str 当串的长度大于0时为真(串非空)
   - -e file_name 文件是否存在
   - [] bash 的内部命令，[和test是等同的。如果我们不用绝对路径指明，通常我们用的都是bash自带的命令。if/test结构中的左中括号是调用test的命令标识，右中括号是关闭条件判断的。这个命令把它的参数作为比较表达式或者作为文件测试，并且根据比较的结果来返回一个退出状态码。if/test结构中并不是必须右中括号，但是新版的Bash中要求必须这样。
   - true = 0 flase = 1 和python 刚好相反

2. #### 语句
   - `[ $? -ne 5 ] && echo "haha"` 不等于5就输出hahah
   - `[ $? -ne 5 ] && echo "haha" && echo "no"` ------------------------no