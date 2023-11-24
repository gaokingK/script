# 函数
- link：
    - https://www.runoob.com/linux/linux-shell-func.html
## 注意
- 函数定义时不需要定义参数，可以直接使用

# 参数和变量
## link：
- https://juejin.cn/post/7164574078442700807
## 对参数、变量一些操作
- 参数和变量或许是一种东西，本文还没有详细区分，主要介绍了内置变量和常用变量的一些操作
- 变量在使用时都需要加一个`$`
- shell脚本中定义的变量都是在当前的进程下有效，如果只想让在当前函数有效，就加上local 
- 函数中使用$1获取的是传给函数的变量，脚本中使用$1获取的是传给脚本的变量
## 内置变量
- 是一开始就存在或者被保留的，主要包括环境变量、位置变量和其他的特殊变量
### local 
- 通常在函数内使用，创建的是局部变量，不加local 关键字创建的是全局变量
### 环境变量
- 环境变量分为全局环境变量（对所有用户都生效）、局部变量（只对当前用户生效）；
- 定义全局变量可以在`/etc/profile.d`目录中通过单独的文件定义;定义局部变量可以在home下的.bash_profile和.bashrc中操作，还可以使用export a="xxx"(只在当前这个终端中有效)；因为这些文件的加载时机是不一样的
```
install:/etc/profile.d # ls
alias.ash   alljava.csh         bindkey.tcsh   csh.ssh           gawk.csh  krb5.sh   ls.bash  profile.csh  python.sh  site.sh              zzz-glib2.csh  zzz-groff.sh
alias.bash  alljava.sh          complete.bash  desktop-data.csh  gawk.sh   lang.csh  ls.tcsh  profile.sh   sh.ssh     xdg-environment.csh  zzz-glib2.sh
alias.tcsh  bash_completion.sh  complete.tcsh  desktop-data.sh   krb5.csh  lang.sh   ls.zsh   python.csh   site.csh   xdg-environment.sh   zzz-groff.csh
```
- 常见的环境变量有
```
install:/etc/profile.d # echo $PATH
/sbin:/usr/sbin:/usr/local/sbin:/root/bin:/usr/local/bin:/usr/bin:/bin
install:/etc/profile.d # echo $USER
root
install:/etc/profile.d # echo $UID
0
install:/etc/profile.d # echo $HOSTNAME
install
install:/etc/profile.d # echo $LANG
POSIX
```
### 位置变量
- $0代表被执行的脚本名，如果是软连接则为软链接的文件名而非实际文件名（这样就可以把脚本软链接到另外一个名字，通过区分$0的变化来执行不同的内容。）$1代表第一个位置传递的参数，以此类推

### 特殊变量
- `$?` 返回值最后一个命令的返回值,0表示正常退出
- `$#` 参数个数 获取传入脚本或函数的位置参数个数
- `$*` 全部位置参数 是所有参数的整体不能被展开
- `$@` 全部位置参数 是所有参数但可以被展开
- `$!` 后台进程pid 获取最后一个后台进程的pid
- `$$` 当前进程pid 获取当前进程的pid
- `$PPID` 父进程pid 获取当前进程的父进程pid
- `$RANDOM` 随机数字输出一个随机数
- `$FUNCNAME` 函数名 输出当前函数的名称
- `$LINENO` 行号 输出当前所在行的行号

## 对变量的操作
### 变量的定义
- 命令的执行结果作为变量
- master_inventory=$(find $inventory_dir -maxdepth 1  -type f -name $master_format  2>/dev/null)
### shift
- shift 命令：可以使脚本的所有参数位置向左移动一位（删除第一位，第二个参数变成了第一个，以此类推）
    - 因为shell脚本最多定位九个变量，所以需要 shift 来获取超出9个之外的 参数
```
 while (($# > 0))
 do
  echo "$1"
  shift
 done
```
### 变量的引用
```
var1=123
var2=var1
echo ${var2}  #var1
echo ${!var2} #123
# ${!prefix*} 或 ${!prefix@} 匹配prefix开头的所有变量名；输出的是变量名
echo ${!var*} # var1 var2
```
### 变量替换 变量默认值
- 主要用来检测变量是否有值，然后根据是否有值来决定要不要给其赋值
- 假如var为空或者未定义返回string，否则返回var
    - ${var:-string} return var if not var else string 但是只是返回， var 不被赋值
- {var:=string} var = var if not var else string ,var为空会被赋值
- {var:+string} var = var if not var else string ,var 为null 时不会被赋值 `echo ${res:+"2223"}` res为空输出null， res不为null时输出2223
- {var:?string} var = var if var else print string 若变量var为空，则把string输出到标准错误中，并从脚本中退出
- string 也可以是命令 `echo ${file:+$(ls 113/*.txt)}`
- var可以是变量名，也可以是位置变量 `var="default";[[ -n $1 ]] && var="$1"`等价于`${1:-"default"}`

### 变量长度
- 获取变量长度`var="abcdef"; echo ${#var}`
- 获取数组类型变量的长度 `${#var[@]}`
- 获取位置参数的个数 `${#@}`

### 截取字符串
```
var=abcde
# 从指定位置开始，到后面的全部，位置下标从0开始计数
echo ${var:2}  #cde
# 从指定位置开始，到后面取指定个数的字符
echo ${var:2:2} #cd
# 从结尾开始往前取指定个数的字符
echo ${var:(-2)}  #de
```
### 大小写转换
```
var=aBcD
# 大小写互换
echo ${var~~} #AbCd
# 全部大写
echo ${var^^} #ABCD
echo ${var,,} #abcd
```
### 按照匹配删除
- 从开头删除，不是从左往右搜索 `${var#Pattern}`;删除最长匹配`${var##Pattern}`
- 从结尾删除`${var%Pattern}`;删除最长`${var%%Pattern}`
- `*`代表任意字符匹配多次，`.`只匹配`.`

### 替换匹配
- 替换第一个匹配`${var/Pattern/Replacement}`;替换全部`${var//Pattern/Replacement}`
- 省略Replacement则匹配将被替换为空
- 从结尾开始；不是从右到左搜索`${var/%pattern/Replacement}`