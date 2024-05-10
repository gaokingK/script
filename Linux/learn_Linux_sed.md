# sed(https://www.runoob.com/linux/linux-comm-sed.html）
## link:
    - [官方文档](https://www.gnu.org/software/sed/manual/html_node/sed-commands-list.html#sed-commands-list)
    - [详细](https://blog.csdn.net/hdyebd/article/details/83617292)
    - 官方文档 https://linux.cn/article-10232-1.html
    - https://blog.csdn.net/qq_35456705/article/details/112147560
    - https://blog.csdn.net/wgembed/article/details/8760123
    - https://blog.csdn.net/Sunny_Future/article/details/80174530
    - https://www.cnblogs.com/zakun/p/linux-cmd-sed.html
## 基本语法
`sed` 命令的基本语法为：
```
sed OPTIONS 'expression' input_file
```
其中：
- `OPTIONS`：可以是一些选项标志，例如 `-i` 表示直接在输入文件中修改。
- `'expression'`：是一个 `sed` 表达式，用于指定要执行的操作，包括文本匹配和替换等。
- `input_file`：要处理的输入文件。
- `echo aaa|sed 's/a/b/g'`

#### 一些命令
- 命令格式： 
    - `sed [option] '{arg1} {arg2} {arg3}' file_name` {option}是选项，{arg1}是用来匹配行的， 后面的{arg2}则代表对匹配的行的操作 {arg3}是操作内容
    - 如 `sed -e '{xxxx}i /\nhhhh' file_name` {xxxx}是用来匹配行的， 后面的i则代表对改行的操作
    - 单引号可以不需要，但不知道是不是存在一些必须加上的场景
- 加空行 https://www.cnblogs.com/zhanglong71/p/5424633.html
    - sed -i 'G' file 每行后面都加空行，空行也加
    - sed -i 'G;G' 加两个空行
    - sed -i '/^$/d;G' 把多余的空行删掉，然后每行后面加一个空行
    - sed -i '/pattern/G'在匹配行之后加入空行
    - sed -i '/^ *hosts:$/{x;p;x}' 在匹配行之前加入空行
- 一些匹配行的方式 
    - sed -i '/tar/i44' 在包括tar内容的行前面插入44
    - sed -i /^rule.*iles:$/ahhh prometheus-config.yaml ^匹配开头，$匹配结尾，.匹配任意字符，`*`匹配多次
    - 直接输入`+{}()` 这些都会当成字符去匹配，如果要是使用正则的元字符匹配，需要加上反斜杠转义
- sed -i '/^ *workers: *$/,/^ *$/{/10.0.5.89/d}' rootfs/deploy/inventory_dir/inventory_10.0.5.89.yaml
    - 在匹配到的行中操作
- 替换连续的多行 
    - `sed '/start_pattern/,/end_pattern/c\aaa' input_file`
    - c\aaa 是替换命令，用于将整个多行范围替换为 "aaa"。
- `sed '/start_string/,/end_string/d' filename` 删除两个特定字符串之间的行 可以删除多个
- `sed '/start_string/,+5d' filename` 删除一个特定字符串及其后面的五行
- 替换大小写`sed -e 's/\(.*\)/\L\1/' <<< "$a" `
- sed '/特定字符/a\'"$(<文件1)" 文件2 > 文件3 # 用于在匹配到 "特定字符" 的行后追加内容。 # 没有空格的地方不能有空格
    - "$(<文件1)" 是一个命令替换，用于将 "文件1" 中的内容插入到 sed 命令中。这样可以将文件1的内容作为变量传递给 sed 命令。
    - 文件2 是目标文件，你希望在其中的特定字符的下一行插入内容。
    - 文件3 是输出文件，结果将写入其中。
- sed -i s/yyyy/xxxx/g `grep yyyy -rl --include="*.txt" ./` 将当前目录(包括子目录)中所有txt文件中的yyyy字符串替换为xxxx字符串
    - -i 表示操作的是文件，符号 `` 括起来的grep命令，表示将grep命令的的结果作为操作文件
- echo "xxx" | sed '1s/^/2i /' | sed -i -f- prometheus-config.yaml 等价于`sed -i '1ixxx' prometheus-config.yaml`
    - 末尾的 / 代表输出空行的意思，因为操作的是标准输入
    - sed '1s/^/1i /'：该命令使用 sed 工具对标准输入进行操作。sed 是一个流式文本编辑器，'1s/^/1i /' 是 sed 的编辑脚本。该脚本中的 1s/^/1i / 表示在第一行之前插入 1i
    - sed -i -f- file2.txt：该命令将 file2.txt 文件作为输入，并将其内容传递给 sed 进行处理。-i 参数表示直接修改文件内容，而不是输出到标准输出。-f- 参数表示从标准输入读取 sed 的编辑脚本。
- echo "h1"  | sed '1s/^/\/proc_target\/i /'| sed -i -f- prometheus-config.yaml 等价于 `sed -i '/proc_target/ih1 prometheus-config.yaml`
- ` sed -n '/^Popeye/p' prometheus-config.yaml |sed -n 's![0-9][0-9]*/[0-9][0-9]*/[0-9][0-9]*!11/14/46!p'`
    - 把Popeye的生日改为11/14/46，假定您不知道Popeye的生日，设法用正则式查找出来 
    - 原来字符串是：Popeye Sailor:156-454-3322:945 Bluto Street, Anywhere, USA 29358:3/19/35:22350
- sed -n '/add_workers:/,/^$/p' your_file.yaml | sed '1d;$d'
    - /add_workers:/,/^$/p: 使用 /add_workers:/,/^$/ 来匹配 add_workers: 开始到空行结束的区块，并使用 p 打印这个区块。
    - sed '1d;$d': 使用 sed 去掉打印的结果中的第一行和最后一行，因为这些行是 add_workers: 和空行。
- sed "/workers:/{:a;N;/\n *-/{s//\n  - $new_ip/;b};ba}" your_file.yaml
    - {:a;N;/\n *-/{s//\n  - $new_ip/;b};ba}：这是一个 sed 表达式块它表示在匹配到的行上执行一系列操作
    - "/workers:/": 使用/pattern/来匹配包含workers:的行。
    - :a;N;/\n *-/{s//\n - $new_ip/;b};ba: 这是一个复杂的sed命令，它会在找到workers:行后，使用:a标签创建一个循环，在循环内使用N命令读取下一行。当读取到一个新行，且匹配到一个以-开始的行（即IP地址行），使用s//\n - $new_ip/命令在其之前插入新的IP地址。最后，使用b命令跳到标签:a重新执行循环，直到遍历完整个workers列表。
- sed -i '/^ *- /s/$/\n'"$new_comment"'/' your_file.yaml 对匹配到的每一行增加东西
    - /^ *- /：匹配以 - 开头的行，这是 IP 地址列表的行。
    - s/$/\n'"$new_comment"'/'：在匹配到的行尾插入新行注释。$ 表示行尾，\n 表示换行符，"$new_comment" 表示要插入的新行注释内容。
- sed '/./!d;:a;N;$!ba;s/\n/ /g' input.txt > output.txt 将多行空行合并成一行
    - /./!d：这是 sed 的地址范围表达式，它使用正则表达式匹配。/./ 表示匹配包含任意字符的行，而 !d 则表示对于不匹配的行执行删除操作。这一步的目的是删除空行，即只保留包含字符的行。
    - :a;N;$!ba;：这是 sed 的标签和循环命令。在这个部分中，我们使用标签 :a 来定义一个名为 a 的标签，然后使用 N 命令来读取下一行并追加到当前模式空间中。接着 $!ba; 表示如果不是最后一行，则跳转到标签 a，即重复读取下一行并追加到当前模式空间中，直到最后一行。
    - s/\n/ /g：这是 sed 的替换命令，用于在模式空间中执行文本替换。在这里，我们使用正则表达式 \n 来匹配换行符，而 / / 则是替换为空格。g 表示全局替换，即将模式空间中所有的换行符都替换为空格，从而将多行合并成一行。
    - 综合起来，上述 sed 命令的流程是：
        - 删除空行，只保留包含字符的行。
        - 逐行读取并追加到模式空间，形成一个多行的文本块。
        - 将文本块中的换行符替换为空格，从而将多行合并为一行。

#### OPTIONS
- 可以使用sed [opt] 4a\ "str_append" filename # 这样来输入（防止字符串来转义）
- **命令应该使用单引号不应该使用双引号** 不加引号的话应该用\来分割`sed -e 1a\ hhhh\ sss change_pc_90.90.0.140.md`
- -i 直接修改文件
  sed -ibakhhhh 'xxx' filename 上述命令将在原始文件上进行更改，并创建一个名为filename.bakhhhh的备份文件。
- -e<script>或--expression=<script> 以选项中指定的script来处理输入的文本文件。是预览，不会真的操作
  - 一条命令可以使用多个-e
- 搜索元字符：
  - & 保存搜索字符用来替换其他字符，如s/love/&2/，love替换为love2;
- -n或--quiet或--silent 仅显示script处理后的结果。(相当于是预览，实际并未处理)
  - `sed -n 's/hhh/aaa/p' filename` 这样才能只打印这一行 -n要配合p

#### 动作
- 多个命令使用;来分割
    - 这个匹配多行的后面怎么只能用一个sed动作呢？cat rootfs/deploy/files/prometheus-config.yaml |sed -n "/rule_files:/,/^ *$/p"|sed -n '1d;$d;p' 
    - 试试这样 `sed -n "/^ *master: *$/,/^ *$/{p;1d}" rootfs/deploy/inventory_dir/inventory_master.yaml`
    - {//!p}：这是在范围内执行的命令块（范围内的意思是不包括第一行和最后一行）。//!p 的意思是在范围内除了空行之外的所有行都会被打印出来。// 表示范围匹配的当前行，! 表示不匹配当前行，所以 {//!p} 表示打印不在范围内的行，即提取结果去除了范围内的第一行和最后一行。
- 动作用双引号括起来也可以
- 在匹配的行后面执行动作，匹配的条件可以是具体的行数，也可以是正则或者字符串
- p 打印 `sed -n 's/hhh/aaa/p' filename` 这样才能只打印这一行 -n要配合p
- $ 代表最后一行 `sed -e '$a\Hello World' example.txt`
- 使用正则`echo "xxxxx"|sed "s/re_/substance/g`
- a：新增
```cs
sed -e 4a\ newLine testfile # 在第4行后添加
```
- i：插入 `sed -e 4inewline` # 在第4行前添加
    - sed -i '/proc_target/i4h' prometheus-config.yaml 在含有proc_target的哪一行
    - 一条命令有多个插入动作时，可以使用多个-e来完成否则会把后面的动作表达式当成要插入的内容`sed -e "2i\ " -e "3i\ " file_name`
    - 命令中有一些命令样例
- ! ：表示后面的命令对所有没有被选定的行发生作用 `sed '1!d' input.in`
- r 从文件读取内容追加 `sed -i '$r test.txt' prometheus-config.yaml`
- w 写入，指定行内容重定向写入到指定文件
    - sed '/partten/w file_name' 处理的文件
    - 会清空后再写
- d 删除
    - 对匹配到的内容的行进行删除 `sed -i /匹配内容/d file` 
    - !d 对没有匹配到的内容删除 `free -m | tr -s ' ' | sed '/^Mem/!d' | cut -d" " -f2-4`
- s 替换 (是把匹配掉的替换，如果想替换整行就要匹配整行)
    -  `sed -i '1s/^/2hhh/' prometheus-config.yaml` 第一行开头增加2hhh 注意要使用用`/`结束
    - 匹配整行使用s/^$/sss/
    - 对某一行中的部分进行替换
        - sed -n '/http.*10.0.5.89/s/10.0.5.89/ddd/p' /apt/promtail/opt/promtail-config.yaml
    - sed -i "s/add_workers:/add_work/" inventory_10.0.5.89.yaml
    - 替换时引用分组，分组一定要用（）括起来，而且括号要用\来转义
        -  sed -i "s/\(add_workers:\)/hide_\1/" inventory_10.0.5.89.yaml

    - REPLACEMENT
        字符串，直接替换
        \N N可以为1～9, 引用匹配分组的内容。
        sed -e 's/#\(Port.+\)/\1/g' /etc/ssh/sshd_config
        sed -r -e 's/#(Port.+)/\1/g' /etc/ssh/sshd_config
        上面的两行等价将以#PORT开始的行#去掉，使用-r选项能够避免使用\(\)
        & 引用整个匹配内容
        sed -e s/^Port/#&/g /etc/ssh/sshd_config
        匹配以Port开头的行，并在前面加上#。
        \L 将后面的内容转为小写，直到遇到\U或\E结束
        \l 将后面的一个字符转为小写
        \U 将后面的内容转为大写，直到遇到\L或\E结束
        \u 将后面的一个字符转为大写
        \E 结束\L,\U的转换
        sed -r -e 's/(\b[^\s])/\u\1/g' /etc/ssh/sshd_config
        将所有单词首字母大写。
        FLAGS
        g 全局替换
        p 打印
        = 打印行号
        - p 打印使用匹配模式匹配到的行
        - 引用匹配结果
```cs
    STR="I'm from china(GRUANDDON)."

    echo $STR|sed -ne "s/^I.*\((.*)\)./\1/gp"
    结果： (GRUANDDON)

    关键点：    中间配置的内容可以使用\1 \2 ... 作为引用
```

- #### 注意
   - 在双引号中使用变量 https://qastack.cn/ubuntu/76808/how-do-i-use-variables-in-a-sed-command
   - 如果又多个符合匹配的结果，会将结果都打印出来，但是不会贪婪匹配
   - 符号要转义，否则就会每行后面都加`sed -i '/\[Service\]atest' xxx`
   - sed -i 'cluster1.yamld' prometheus-config.yaml 会将所有行替换为cluster1.yamld
   - string = "113/kbox_result_202110180959.txt" ls 113/*.txt|sed "s/*kbox_r.*t_//g" 为什么kbox的那个星号没有用，因为sed也能用正则，但是*号代表前个模式匹配0次或者多次， 但为什没有用呢？难道前面不是null吗
  	- 如何将命令的结果作为sed的输入
      - 方法一
         - link
            - https://www.thinbug.com/q/39317465
         - `cmd | sed -i '6r /dev/stdin' file_name` # 在第6行后插入
         - 输入换行`sed -e '1i /\nhhhh' file_name`
         - sed -i "1a aa" a.txt 如果a是空文件，会写不进去
      - 方法二： echo "h1"  | sed '1s/^/\/proc_target\/i /'| sed -i -f- prometheus-config.yaml
         - 调试的方法就是echo "h1" | sed '1s/^/\proc_target\/i /' |cat 输出的结果要和 sed -i "/proc_target/ixxx" 对应的上 
      - 方法三：sed -e '/proc_target/a\'$(echo aaa) prometheus-config.yaml
   - 动作应该使用单引号包括起来
   - 如何输入空格呢 
   - 使用 `/`作为内容的开始 `sed -i '/rule_files/a\  - /etc/alerts/common.yaml' prometheus-config.yaml` 如果a后面不加`\`后面的空格就不会显示



### 正则表达式基础
在 `sed` 中，正则表达式用于匹配文本。下面是一些正则表达式的基本概念：

- `.`：匹配任意一个字符包括空格。
- `*`：匹配前面的字符零次或多次。
- `+`：匹配前面的字符一次或多次。
- `?`：匹配前面的字符零次或一次。
- `^`：匹配行的开头。
- `$`：匹配行的结尾。
- `[]`：用于指定一个字符集，例如 `[abc]` 匹配 `a`、`b` 或 `c` 中的任意一个字符。
- `[^]`：用于指定一个字符集的补集，例如 `[^abc]` 匹配除了 `a`、`b` 和 `c` 之外的任意一个字符。

### `sed` 中的正则表达式

在 `sed` 中，正则表达式使用基本的正则表达式（BRE）或扩展的正则表达式（ERE）。默认情况下，`sed` 使用 BRE。要使用 ERE，可以在 `sed` 命令中添加 `-E` 选项。

下面是一些常用的正则表达式用法在 `sed` 中的应用：

1. 文本匹配：使用 `/pattern/` 来匹配包含 `pattern` 的文本行。
   ```
   sed '/pattern/ ...'
   ```
2. 行首匹配：使用 `^` 来匹配以 `pattern` 开头的文本行。
   ```
   sed '/^pattern/ ...'
   ```
3. 行尾匹配：使用 `$` 来匹配以 `pattern` 结尾的文本行。
   ```
   sed '/pattern$/ ...'
   ```
4. 单词匹配：使用 `\b` 来匹配单词边界。
   ```
   sed '/\bpattern\b/ ...'
   ```
5. 字符集匹配：使用 `[]` 来匹配指定字符集中的任意一个字符。
   ```
   sed '/[abc]/ ...'
   ```
6. 匹配数字：使用 `[0-9]` 来匹配数字字符。
   ```
   sed '/[0-9]/ ...'
   ```
7. 使用括号和反向引用：在 `sed` 中使用 `\(...\)` 来捕获文本，并在替换时使用 `\1`、`\2` 等进行反向引用。
   ```
   sed 's/\(pattern1\).*/\1/'
   ```
8. 非贪婪匹配：使用 `*?` 或 `+?` 来进行非贪婪匹配，尽可能匹配更少的字符。
   ```
   sed 's/.*?\(pattern\).*/\1/'
   ```
9. 其他特殊字符的转义：对于正则表达式中的特殊字符，如果想要匹配它们本身，需要使用反斜杠 `\` 进行转义。
这只是 `sed` 中使用正则表达式的一些基本用法，正则表达式非常强大和灵活，你可以根据具体的需求进行更复杂的文本匹配和替换操作。在实际使用中，你可能需要不断尝试和练习，以熟练掌握正则表达式的技巧。

### 保持空间是什么，怎么使用他
在 `sed` 中，保持空间（Hold space）是一个用于临时存储数据的缓冲区。`sed` 在处理输入文件的每一行时，都会将当前行的内容放入模式空间（Pattern space）。模式空间是 `sed` 处理的当前行，而保持空间是用于存储临时数据的区域，可以在处理不同行时使用它来保存一些额外的信息。

你可以使用 `h` 命令将模式空间中的内容复制到保持空间中，使用 `H` 命令将模式空间中的内容追加到保持空间的末尾。同样，使用 `g` 命令将保持空间中的内容复制到模式空间，使用 `G` 命令将保持空间中的内容追加到模式空间的末尾。

下面是一些常用的保持空间命令：

- `h`：将模式空间中的内容复制到保持空间中。
- `H`：将模式空间中的内容追加到保持空间的末尾。
- `g`：将保持空间中的内容复制到模式空间中。
- `G`：将保持空间中的内容追加到模式空间的末尾。
- `x`: 将当前模式空间与保持空间的内容进行交换。模式空间是 sed 处理的当前行，而保持空间是用于存储临时数据的缓冲区。
- `p`：打印模式空间的内容，即打印匹配到的行。
- `x`：再次将模式空间与保持空间进行交换，以恢复原始的模式空间内容。
举例说明，假设有一个文件 `file.txt` 包含以下内容：

```
apple
banana
cherry
```

现在，我们可以使用 `sed` 命令来实现保持空间的操作：

1. 使用 `h` 命令将第一行复制到保持空间，并将其打印出来：

   ```bash
   sed '1h;1!d;x' file.txt
   ```

   输出：
   ```
   apple
   ```

2. 使用 `H` 命令将每一行都追加到保持空间，并将其打印出来：

   ```bash
   sed 'H;1!d;x' file.txt
   ```

   输出：
   ```
   apple
   banana
   cherry
   ```

3. 使用 `g` 命令将保持空间中的内容复制到模式空间，并将其打印出来：

   ```bash
   sed 'H;1!d;g' file.txt
   ```
   输出：
   ```
   apple
   apple
   banana
   banana
   cherry
   cherry
   ```
4. 使用 `G` 命令将保持空间中的内容追加到模式空间的末尾，并将其打印出来：
   ```bash
   sed 'H;1!d;G' file.txt
   ```

   输出：
   ```
   apple

   apple
   banana

   banana
   cherry

   cherry
   ```

保持空间在 `sed` 中通常用于在处理文本时暂存一些数据，以供后续使用。在复杂的文本处理场景中，保持空间可以提供更大的灵活性和功能。
