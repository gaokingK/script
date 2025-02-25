
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
   - 遍历数组：使用for item in "${array[@]}"来遍历数组中的元素。 可以不加双引号
   - 直接使用不赋值给变量，为什么带括号会报错呢 for file in "a" b c ;do echo $file;done
   - 将命令的结果放在列表里`array=($(命令))` `for f in "${array[@]}";do echo 2$f;done `来验证
### 字符串转为列表
```sh
在 Bash 中对多行文本进行按行分割并放入数组的常见方法是使用 read 命令的 -a（数组）选项，结合 while 循环和管道操作。这里有一个示例脚本，它展示了如何将多行文本分割到一个数组（列表变量）中：
bash
#!/bin/bash

# 定义多行文本
multiline_text="line1
line2
line3
line4"

# 读取每一行并添加到数组中
IFS=$'\n' # 如果是可打印字符比如空格和字符 IFS='s '
read -rd '' -a line_array <<<"$multiline_text"
# 在 Bash 中，$'\n' 是一种特殊的引用表示法，这种表示法使得你可以用转义序列来表示不可打印的字符。这里的 $ 符号让 shell 知道这是一个转义序列。在单引号之间的 \n 表示一个换行符，而不是字面上的反斜杠加上一个 n 字符。
# IFS=$'\n' 这条语句的含义是，内部字段分隔符（IFS）被设置为换行符，这样 read 命令就会以换行符为界来分隔文本。
# 如果不使用 $ 符号，IFS='\n' 会被识别为两个字面字符：一个反斜线 \ 和一个 n，而不会解析为换行符。所以，在 Bash 脚本中使用 $ 是很重要的，因为它确保了转义序列正确地被解释和使用。

# 显示数组的内容
for line in "${line_array[@]}"; do
    echo "$line"
done
在这个脚本中：
multiline_text 变量包含了你的多行文本。
IFS=$'\n' 设置了 IFS 变量为换行符，这是多行文本的自然分割点。
read -rd '' -a line_array <<<"$multiline_text" 命令读取 multiline_text 变量，并根据 IFS 的值（换行符）将其分割到 line_array 数组中。-d '' 指定了一个空的分隔符，这允许 read 读取结束于 NUL 字符的输入，而 <<< 是将字符串重定向给读取命令的 Bash 特性。
for 循环遍历数组并输出每一行。
确保在执行此操作后，将 IFS 重置回其原始值，以避免潜在的副作用：
bash
IFS=$' \t\n'
上面的命令将 IFS 重置为默认的空白字符：空格、Tab 和换行符。
使用这种方式，你可以将任何多行字符串分割到 Bash 数组中。
```
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
      - res=${res}hhh 改变变量
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
# ${}中可以进行的其他操作
在 Bash 中，`${file%.zip}` 是一种参数扩展的语法，它用于从字符串变量（如文件名）中删除指定的后缀或前缀。Bash 提供了多种字符串操作的方式，以下是一些常见的用法：

### 1. **删除文件名的后缀**

- **`${file%.zip}`**：删除字符串中最右侧匹配的 `.zip` 后缀。
  ```bash
  file="example.zip"
  echo "${file%.zip}"  # 输出 "example"
  ```
- **`${file%%.zip}`**：删除字符串中最左侧匹配的 `.zip` 后缀（如果字符串包含多个 `.zip`，则删除最左边的一个及其右边的所有内容）。

  ```bash
  file="example.zip.123.zip"
  echo "${file%%.zip}"  # 输出 "example"
  ```

### 2. **删除文件名的前缀**

- **`${file#prefix}`**：删除字符串中最左侧匹配的 `prefix` 前缀。

  ```bash
  file="prefix_example.txt"
  echo "${file#prefix_}"  # 输出 "example.txt"
  ```

- **`${file##prefix}`**：删除字符串中最右侧匹配的 `prefix` 前缀（如果字符串包含多个 `prefix`，则删除最右边的一个及其左边的所有内容）。

  ```bash
  file="prefix_prefix_example.txt"
  echo "${file##prefix_}"  # 输出 "example.txt"
  ```

### 3. **替换字符串中的内容**

- **`${file/old/new}`**：替换字符串中的第一个匹配 `old` 的部分为 `new`。

  ```bash
  file="example.txt"
  echo "${file/.txt/.md}"  # 输出 "example.md"
  ```

- **`${file//old/new}`**：替换字符串中所有匹配 `old` 的部分为 `new`。

  ```bash
  file="example.txt.txt"
  echo "${file//.txt/.md}"  # 输出 "example.md.md"
  ```

### 4. **获取文件的路径、文件名和扩展名**

- **获取文件的路径**（去掉文件名部分）：

  ```bash
  filepath="/home/user/example.txt"
  echo "${filepath%/*}"  # 输出 "/home/user"
  ```

- **获取文件的文件名**（去掉路径部分）：

  ```bash
  echo "${filepath##*/}"  # 输出 "example.txt"
  ```

- **获取文件的扩展名**：

  ```bash
  echo "${filepath##*.}"  # 输出 "txt"
  ```

- **获取文件名不带扩展名**：

  ```bash
  filename="example.txt"
  echo "${filename%.*}"  # 输出 "example"
  ```

### 5. **默认值和替代值**

- **`${var:-default}`**：如果 `var` 未设置或为空，则使用 `default` 作为替代值。

  ```bash
  echo "${name:-John}"  # 如果 $name 未定义或为空，则输出 "John"
  ```

- **`${var:=default}`**：如果 `var` 未设置或为空，则将其设置为 `default` 并返回 `default`。

  ```bash
  echo "${name:=John}"  # 如果 $name 未定义或为空，则设置并输出 "John"
  ```

- **`${var:+alternate}`**：如果 `var` 已设置且非空，则使用 `alternate`，否则返回空值。

  ```bash
  name="Alice"
  echo "${name:+Bob}"  # 输出 "Bob"
  ```

- **`${var:?error_message}`**：如果 `var` 未设置或为空，则显示 `error_message` 并退出脚本。

  ```bash
  echo "${name:?Variable not set}"  # 如果 $name 未定义或为空，则输出错误信息并退出
  ```

### 6. **获取字符串长度**

- **`${#var}`**：获取字符串的长度。

  ```bash
  name="Alice"
  echo "${#name}"  # 输出 "5"
  ```

### 总结

Bash 的参数扩展提供了强大的字符串操作功能，特别适用于处理文件路径、文件名、前缀、后缀等操作。通过熟练掌握这些语法，你可以更高效地编写脚本来处理文件和目录操作。