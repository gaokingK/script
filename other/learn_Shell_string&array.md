
### 把命令赋值给字符串，再执行命令
```cs
aa="systemctl list-units --all|grep mave" # 管道符左右要加空格，否则均会被识别为systemctl的选项
${aa}

```
### 单引号 双引号 不带引号 
- 单引号会原样输出
- 双引号里面可以有变量，双引号里面可以出现转义字符
- 不使用引号的情况下字符串中间不可以有空格
```shell
function variable_in_string(){
	num=100
	echo "$num"
	echo ''$num''
	echo $num
	echo '$num'
}

variable_in_string
```
# array
   - 定义数组：使用array=(item1 item2 item3)定义数组。
   - 访问元素：使用${array[index]}来访问数组中的元素。
   - 获取数组长度：使用${#array[@]}获取数组的长度。
   - 遍历数组：使用for item in "${array[@]}"来遍历数组中的元素。
   - 直接使用不赋值给变量，为什么带括号会报错呢 for file in "a" b c ;do echo $file;done
# 字符串
### 字符串比较
   - = 和 == 等价
   - ==的功能在[[]]和[]中的行为是不同的,如下:
   ```shell
   [[ $a == z* ]] # 如果$a以"z"开头(模式匹配)那么将为true
   [[ $a == "z*" ]] # 如果$a等于z*(字符匹配),那么结果为true
   [ $a == z* ] # File globbing 和word splitting将会发生
   [ "$a" == "z*" ] # 如果$a等于z*(字符匹配),那么结果为true
   ```
   - != 不等于,如:if [ "$a" != "$b" ] 这个操作符将在[[]]结构中使用模式匹配.
   - < 和 >,在ASCII字母顺序下. 需要使用转义否则会被解释为重定向
   - z 字符串为"null".就是长度为0.
   - -n 字符串不为"null" 必须要用双引号
   - **注意 习惯于使用""来包括测试字符串是一种好习惯** 在 [] 中使用-n 必须要用双引号把变量引起来; 使用一个未被""包括的字符串来使用!-z, 或者未用""引用的字符串本身,放到[]结构中, 虽然一般情况下(没有空格的字符串)可以工作,但这是不安全的;
### 字符串操作
   - 拼接字符串：使用$var1$var2形式将两个变量或者字符串连接起来。
      - invalid_file=$invalid_file$file 如果想要重复使用一个变量，记得定义时不要加$
      - 如果有空格和\n等需要转义的要使用双引号包括
   - 截取子串：使用${string:position:length}形式来截取字符串的子串。
   - 查找子串：使用${string#substring}或${string%substring}来查找字符串中某个子串并进行删除。
   - 替换子串：使用${string/substring/replacement}或${string//substring/replacement}来替换字符串中的子串。
   - 转换大小写：使用${string,,}将字符串转换为小写，${string^^}将字符串转换为大写。
### 模式匹配替换、替换 截取
   1. 模式匹配替换
      1. {var%pattern} 必须以pattern结尾(可以加*号嘛)，去掉patter匹配到的最短内容；{var%%pattern} 去掉patter匹配到的最长内容；
      2. {var#pattern} 必须以pattern开始，去掉patter匹配到的最短内容；{var##pattern} 去掉patter匹配到的最长内容；
   3. 不能嵌套吧？就是先给变量赋值，然后使用模式匹配替换

### 大小写转换
- link：https://www.cnblogs.com/codeking100/p/10196434.html
```cs
此方法为bash 4.0以后新增，bash 4.0 2009年发布

$ test="abcDEF"

# 把变量中的第一个字符换成大写

$ echo ${test^}
AbcDEF

# 把变量中的所有小写字母，全部替换为大写
$ echo ${test^^}
ABCDEF

# 把变量中的第一个字符换成小写
$ echo ${test,}
abcDEF

# 把变量中的所有大写字母，全部替换为小写
$ echo ${test,,}
abcdef
```