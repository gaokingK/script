## if test
- link：
  - [link](https://blog.csdn.net/qq_37960324/article/details/83145412)
  - https://blog.csdn.net/m0_37814112/article/details/103053802
  - [关于test的，选项好像也能通用](https://www.cnblogs.com/shaoshao/p/6809580.html)
      - test [判断条件]  && 结果为true时做的 || echo "not exist" 为false做的
         - `test 2 -eq 2  && echo a || echo b`
         - 不能执行命令吗
         ```sh
         test `ps -ef|grep bio` && echo "yes" || echo "no"
         - bash: test: too many argument
         ```
      - `[[]]` 和 `[]` 相当于test
         - [ 2 -eq 2 ] && echo a || echo b
         - [[ 2 -eq 2 ]] && echo a || echo b
      - 请使用一行linux代码帮我实现：条件A为真  则判断B，如果B为真 执行C，B为假执行D，A为假则什么也不执行
      `[ conditionA ] && { [ conditionB ] && commandC || commandD; } || true`

  - https://www.cnblogs.com/kaishirenshi/p/9729800.html
  - 文本 https://blog.csdn.net/Mr_LeeHY/article/details/76383091
### 注意
- [] 一定要和中间的东西使用空格隔开
- 判断命令的执行结果
   - https://www.jianshu.com/p/9097c60d8e8c
   ```cs
   if ... fi 语句；
   if ... else ... fi 语句；
   if ... elif ... else ... fi 语句。
   # foo 是一个函数 但换成命令也是可以的
   if [ "$(foo 'NO')" == "It's not YES" ]; then
      echo "Match: NO"
   fi
   # 带判断命令的执行结果
   OUT1="$(foo 'YES')"
   if [ $? -eq 0 -a "${OUT1}" == "It's YES" ]; then
      echo "Match: YES"
   fi
   # 可以直接使用grep判断，因为grep没有搜索到时返回1，搜索到时返回0
       if   grep "add_workers:" $inventory_path  ; then # 这样如果搜索到会输出搜索结果
           echo "searched"
       else
           echo "no searched"
       fi
       if [[ `grep "worker" $inventory_path` ]]; then # 这样不会输出搜索到的结果 一个单括号也可以的
           echo "searched"
       else
           echo "no searched"
       fi
    select c1 as ciCode, lower(c3) as Brand, lower(c4) as DeviceType,c5 as assetType,c6 as deployDb,c7 as '@sourceip',c8 as netDeviceCurr,c9 as netDeviceAdmin from tb_rich_table_2 where latest = 1;
    ```
### 选项
- -n str 当串的长度大于0时为真(串非空)
  ```shell
  if [ 3 -ne 2 ];then echo yes;else echo no;fi # 注意方括号两边的空格，没有会报错
  args=''
  [ -n $args] && echo "not null" # 结果是not null
  [ -n "$args"] && echo "not null" # 结果是无输出 这个是正确用法
  # 不加“”时该if语句等效于if [ -n ]，shell 会把它当成if [ str1 ]来处理，-n自然不为空，所以为正
  # 单括号中变量必须要加双引号； 双对中括号，变量不用加双引号
  ```
- 取非 [ ! expr ] 注意空格 可以是带选项的
- -z str 串的长度为0时为真 
- [str] 串非空时为真 和 -n 有什么区别呢?--------------------no
  - -z 检测字符串长度是否为零。如果字符串长度为零（即字符串是空的），则返回 true。
  - -n 检测字符串长度是否非零。如果字符串长度非零（即字符串有内容），则返回 true。
- -e file_name 文件或者文件夹是否存在
- -x file　　　　　用户可执行为真 
- -d 文件 判断文件是否存在，并且是否为目录文件
- [] bash 的内部命令，[和test是等同的。如果-我们不用绝对路径指明，通常我们用的都是bash自带的命令。if/test结构中的左中括号是调用test的命令标识，右中括号是关闭条件判断的。这个命令把它的参数作为比较表达式或者作为文件测试，并且根据比较的结果来返回一个退出状态码。if/test结构中并不是必须右中括号，但是新版的Bash中要求必须这样。
- true = 0 flase = 1 和python 刚好相反
- -gt 大于 -lt 小于 -  -ge 大于等于 -le 小于等于 -eq是等于 -ne是不等于
```sh
if cat 111-tmp.txt | grep ting1
then
    echo found
else
   echo "no found"
fi
if [ $# -ne 3 ]
then
    echo "num no eq 3"
else
    echo "num eq 3"
fi
```
- 逻辑判断
```cs
[ ! EXPR ] 逻辑非，如果 EXPR 是false则返回为真。
[ EXPR1 -a EXPR2 ] 逻辑与，如果 EXPR1 and EXPR2 全真则返回为真。
[ EXPR1 -o EXPR2 ] 逻辑或，如果 EXPR1 或者 EXPR2 为真则返回为真。
[ ] || [ ] 用OR来合并两个条件
[ ] && [ ] 用AND来合并两个条件
```
- [ -t FD ] 如果文件描述符 FD （默认值为1）打开且指向一个终端则返回为真

### 浮点数比较 # bc
- 可以比较 `[[ echo "scale=2 0.3 > 0.4"|bc -eq 1 ]]` True 的结果为1 false的结果为0

### 字符串比较
- 利用字符串运算符 =~ 直接判断strA是否包含strB。
```sh
# 结果都是包含
strA="helloworld"
strB="low"
if [[ $strA =~ $strB ]];then
    echo "包含"
fi
if [[ $A == *$B* ]];then
    echo "包含"
fi

```

### [] 和 [[]]
- link:
   - https://blog.csdn.net/Michaelwubo/article/details/81698307
- 单对中括号，变量必须要加双引号, 双对不用加 `[ -n "$pid" ]; [[ -n $pid ]] `
- 双括号中，不能使用 -a -o 对多个条件进行连接，`[[]]`内外都不行; 但是&& || 内外都可以用
- ksh( Korn Shell) 只支持`[]`
- 单括号中可以使用-a -o，但必须在括号内;
- 单括号中可以使用`&&`和`||`,但必须在括号外

- unary operator expected 
   - link: https://cloud.tencent.com/developer/ask/sof/102515287
   - if [] 报错[: -ne: unary operator expected
   - 首先，您需要知道[ ... ]是一个命令，而不是一个语法元素。它是test命令的变体。[是命令，... ]是传递给它的参数。]应该是最后一个参数。
   - 问题是传递给[的参数是由[解析的，而不是由bash解析的，而且if语法元素本身不会在执行的测试的非零返回值上抛出错误。
   - 解决方法是使用[[ (扩展测试)。Bash将检查传递给[[的参数的语法
   - 进一步阅读：http://tldp.org/LDP/abs/html/testconstructs.html

### 语句
   - `[ $? -ne 5 ] && echo "haha"` 不等于5就输出hahah
   - `[ $? -ne 5 ] && echo "haha" && echo "no"` ------------------------no

## continue break
   - link: http://c.biancheng.net/view/1011.html
   - break n n 表示跳出循环的层数，如果省略 n，则表示跳出当前的整个循环。break 关键字通常和 if 语句一起使用，即满足条件时便跳出循环。
   - continue n 

### while
```sh
while : 相当于其他语言的while True
while [ $a -le 5 ];do
    if [ $a -eq 3 ];then
        break
    fi
    echo "a=$a"
    a=$[$a+1]
done
```

## select in
   - link: http://c.biancheng.net/view/2829.html
   - select in 循环用来增强交互性，它可以显示出带编号的菜单
   - 就像for循环, 即使原内容没有了, 只会报错

## for 
- link: https://www.cnblogs.com/liuyuelinfighting/p/16396308.html
   - 语句
   ```sh
   huawei ~/Desktop/smoke% for dir in 11[1,4]; do echo $dir;done
   111
   114

   for line in $@
   do
   cat << EOF
      $line
   EOF
   done

   for i in {1..4} //1,2,3,4
   ```

### 单行命令
```shell
[5 -eq 6] && echo equal || no equal
[[ expr ]] && { [[ expr ]] && expr1 || expr2; }
[[ expr ]] && { expr1;expr2 } || { expr3; expr4 }
```
