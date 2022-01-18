
### 单引号会原样输出
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

### 模式匹配替换、替换 截取
   1. 模式匹配替换
      1. {var%pattern} 必须以pattern结尾(可以加*号嘛)，去掉patter匹配到的最短内容；{var%%pattern} 去掉patter匹配到的最长内容；
      2. {var#pattern} 必须以pattern开始，去掉patter匹配到的最短内容；{var##pattern} 去掉patter匹配到的最长内容；
   3. 不能嵌套吧？就是先给变量赋值，然后使用模式匹配替换

