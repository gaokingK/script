### awk
- link：
    - https://www.runoob.com/linux/linux-comm-awk.html
    - 判断: https://blog.csdn.net/shallnet/article/details/38821311
- awk是一种强大的脚本语言，用于数据的模式匹配和处理，完成数据的抽取
- 使用单引号而不是双引号；如果使用双引号，里面的内容会被当成字符串传递给bash，而不是一个awk命令；使用单引号 ' 来包围 awk 的命令，这样 Bash 会将 {print $1} 传递给 awk，awk 会正确地解释和执行它。以下是正确的命令：
- `{print $NF}` 输出切割后的最后一项; `'{print $(NF-1)}` 倒数第二项
- 可以指定多个分隔符 `awk -F '[b,]' ` 先使用`b`，后使用`,`;或者使用awk -F "abc" 指定abc作为分隔符 
- length 方法获取字符串的长度 `echo ${str}|awk '{print length($0)'`
- -F fs 指定输入文件折分隔符，fs是一个字符串或者是一个正则表达式，如-F:
    - echo "rootfs/deploy/a.txt"|awk -F/ '{print $2}'
- echo "aaa\"aaa" |awk -F "\\\"" '{print $1}' 输出aaa 注意反斜杠和冒号的转义
  
- 判断的使用方法
  - 写法1：`awk '位置变量 比较元字符 比较参数 {print 位置变量}'`
  - 写法2：`awk '[逻辑操作符]{if(位置变量 ~比较参数 [ 逻辑操作符 位置变量 比较元字符 比较参数])print 位置变量 }'`
  - 比较元字符
    - <       小于
    - <=    小于等于
    - ==   等于
    - !=     不等于
    - >     大于
    - >=    大于等于
    - ~     匹配正则表达式
    - !~     不匹配正则表达式
  - 比较参数可以是位置变量，也可以是是自定义的字符串如`awk '{if($1~/^....user/)print}' group_file2` 判断group_file2分割后的第一个元素是否是任意4位字符后跟user，如果有就输出
### 为什么要用单引号把脚本括起来
- 在使用 awk 命令时，通常我们会通过单引号 ' 包裹 awk 的脚本部分。这主要有以下几个原因：
- 防止 Shell 提前扩展:Shell（比如 ）会处理双引号 " " 里面的特殊字符（如 $ 符号变量扩展和反引号命令替换等），但单引号 ' ' 里的内容会被当作纯文本字符串处理。由于 awk 脚本经常包含像 {}、$之类的特殊字符，如果不用单引号包裹起来，Shell 会尝试去解释这些特殊字符，导致awk\ 表达式没法正确传递。
- 内部引用问题:使用单引号可以避免内部的双引号需要被转义。如果使用双引号，内部的双引号都需要用反斜线 \ 来做转义处理，这使得表达式变得更加复杂和难以阅读。

### print和printf的不同：https://blog.csdn.net/qq_35696312/article/details/88169556
- print在显示多个结果的时候以逗号分隔，结果将这几部分的内容自动使用分隔符进行分隔，且不需要添加换行符\n
- printf可以更加灵活的控制某一个字段的输出格式，通过使用诸如%-12s,%3.1f等格式化方法
- 格式化能力：printf 支持复杂的格式化，而 print 不支持。
- 换行符：print 自动添加换行符，而 printf 需要你手动添加 \n。
- 使用场景：如果你需要简单的输出，使用 print。如果你需要控制输出的格式，使用 printf。
# cut 只能指定单个分隔符
   - link:
       - https://www.cnblogs.com/yychuyu/p/13347444.html
       - https://www.cnblogs.com/now-fighting/p/3537375.html
   - -b ：以字节为单位进行分割（就不用搭配-d了）。这些字节位置将忽略多字节字符边界，除非也指定了 -n 标志
   - -c ：以字符为单位进行分割。（就不用搭配-d了）
   - -d 指定分隔符`cut -d: xxxx`默认为制表符。
   - -f 根据-d指定的分隔符来分割，从1开始`cut -d: -f1 xxx`
   - 注意
       - 对于选项-b, -c, -f，只能在一个命令被指定其中的一项。
       - 如果命令中没有指定FILE或者FILE是"-"，则默认是读取标准输入。
   - --output-delimiter=STRING 使用STRING作为输出内容中的分隔符，而不是使用原来标准输入中的分隔符。
   - 关于显示的内容（-f, -b, -c都可以使用，编号都是从1开始）
       - N 显示第n个
       - N- 从第N个到末尾都显示
       - N-M 从第N个到第M个
       - -M 从第一个到第M个
   - 显示最后一个`echo'maps.google.com' | rev | cut -d'.' -f 1 | rev`
   ```cs
   其中，-b/-c/-f 后跟选取的字节/字符/片段，num 从 1 开始，格式如下：
   num ： 选取第num个字节/字符/片段；
   num1,num2,num3 : 选取第num1,num2,num3的字节/字符/片段
   num- : 选取第num个字节/字符/片段一直到结尾；
   num1-num2 : 选取第num1到num2的字节/字符/片段；
   -num : 选取第1个到num个的字节/字符/片段；
   ```
# tr
   - 命令用于转换或删除文件中的字符。
   - -s, --squeeze-repeats：缩减连续重复的字符成指定的单个字符 
   - 小写字母全部转换成大写字母`cat testfile |tr a-z A-Z `
# dd 用于读取，转换，并输出数据
- if 指定读取的文件，默认是标准输入
- of 输出文件名，默认为标准输出。
- bs=bytes：同时设置读入/输出的块大小为bytes个字节。
- count=blocks：仅拷贝blocks个块，块大小等于ibs指定的字节数。
- 生成大文件 `dd if=/dev/zero of=res.txt bs=1M count=5` bs的单位可以是k M G
  - /dev/zero是一个特殊的设备文件，它提供了无限的零字节（\0）
- 将testfile文件中的所有英文字母转换为大写，然后转成为testfile_1文件 `dd if=testfile_2 of=testfile_1 conv=ucase `
- 生成一个内容全是“hi”的5MB文件`yes "hi" | head -c 5242880 > file.txt`
  - yes "hi": 这个命令会无限输出字符串"hi"和换行符。
  - head -c 5242880: 这个命令会从管道中读取前5MB的内容（因为1MB=1048576字节，所以5MB就是5242880字节）然后停止。
### 命令
```sh
# 打印文件中的特定列
awk '{print $2, $5}' filename #这将会打印文件 filename 中的第二和第五列。
# 计算文件中列的总和
awk '{sum += $1} END {print sum}' filename # 这将计算文件 filename 中第一列的总和。
# 条件打印
awk '$1 > 100' filename #这将打印所有第一列值大于100的行。
# 使用分隔符
awk -F, '{print $1, $3}' filename # 使用 -F 选项指定分隔符，这里是逗号。这将打印由逗号分隔的文件 filename 中的第一和第三列。
# 格式化输出
awk '{printf "%-10s %-8s\n", $1, $2}' filename # 这将格式化打印第一列和第二列，第一列为宽度 10 的左对齐字符串，第二列为宽度 8 的左对齐字符串。
# 模式匹配与处理 
awk '/pattern/ {print $0}' filename # 只打印那些包含某种模式 pattern 的行。
# 对列进行数学运算
awk '{print $1 * $2}' filename # 打印文件 filename 中第一列和第二列相乘的结果。
# 制定 BEGIN 和 END 块 
awk 'BEGIN {print "Start Processing"} {print $0} END {print "End Processing"}' filename #在处理文件 filename 前后，打印 “Start Processing” 和 “End Processing”。
# 内置变量的使用 
awk 'NR==1, NR==5 {print NR, $0}' filename # 打印文件 filename 的第一行到第五行，并在每行前面加上行号（NR 是行号变量）。
# 替换和输出到另一个文件

awk '{sub(/pattern/, "replacement")}1' filename > newfile # 在文件 filename 中把 pattern 替换为 replacement，并把结果输出到 newfile 文件中。
```
- awk '/workers:/ {getline; print $1}' your_file.yaml
    - 我们使用 /workers:/ 来匹配包含 workers: 的行。然后使用 getline 命令读取下一行，并使用 print $1 来打印第一个字段，即 IP 地址。
- 合并 workers 和 add_workers 到一个新的列表中
    - awk '/workers:/ {workers=1; next} /add_workers:/ {workers=0} workers {print $0}' your_file.yaml
- awk '/add_workers:/ {getline; print}' RS='[- ]+' FS='\n' your_file.yaml
    - /add_workers:/: 此处使用 /add_workers:/ 来匹配包含 add_workers: 的行。
    - {getline; print}: 使用 getline 命令读取下一行，然后使用 print 命令输出该行内容。
    - RS='[- ]+': 设置行分隔符为 [- ]+，即一个或多个连字符和空格。这样可以将 YAML 列表识别为单独的行。
    - FS='\n': 设置字段分隔符为换行符，这样我们可以读取整个 IP 地址行。
- awk '/add_workers:/ {flag=1; next} /^ *$/ {flag=0} flag {print}' inventory_10.0.5.89.yaml
    - /add_workers:/ {flag=1; next}: 当匹配到 add_workers: 行时，设置标志 flag 为 1，并跳过下面的处理。
    - /^$/ {flag=0}: 当匹配到空行时，设置标志 flag 为 0，表示结束匹配 add_workers 区块。
    - flag {print}: 当标志 flag 为 1 时，打印当前行。
- awk '/add_workers:/ {flag=1; next} /^[ a-zA-Z:]*$/ {flag=0} flag {print}' inventory_10.0.5.89.yaml
- awk -v ip="$new_ip" '/workers:/ {found=1} {print} END {if (found) print ip}' your_file.yaml > tmp_file.yaml
    - -v ip="$new_ip": 使用-v参数，将Shell变量new_ip传递给awk中的变量ip。
    - '/workers:/ {found=1}: 当遇到包含workers:的行时，设置变量found为1。
    - {print}: 对于所有行，都打印输出。
    - END {if (found) print ip}: 在文件末尾（END）判断是否找到了包含workers:的行（即found为1），如果找到，则打印变量ip（新的IP地址）。
