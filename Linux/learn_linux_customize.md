# TO
linux中关于自定义的一些文件的介绍、怎么去自定义
### shell有多种，比如bash、zsh、csh、ksh、sh、tcsh等因此，制作功能时，要先搞清楚，你使用的是哪种shel
### 自动补全和菜单补全
- link: https://blog.csdn.net/guoxuce/article/details/65632995
### doc
- link:
    - https://wiki.archlinux.org/title/Bash#History_completion
    - Linux From Scratch （简体中文版) https://lctt.github.io/LFS-BOOK/lfs-systemd/chapter07/systemd-custom.html
### 有些配置文件为啥以rc结尾
- “rc”，它是“runcomm”的缩写――即“run command”(运行命令)的简写。
>“rc” 是取自 “runcom”, 来自麻省理工学院在 1965 年发展的 CTSS系统。相关文献曾记载这一段话：”具有从档案中取出一系列命令来执行的功能；这称为 “run commands” 又称为 “runcom”，而这种档案又称为一个 runcom (a runcom)。
- rc”是很多脚本类文件的后缀，这些脚本通常在程序的启动阶段被调用，通常是Linux系统启动时。
- Linux或Unix的许多程序在启动时，都需要“rc”后缀的初始文件或配置文件。

### 一些配置文件的作用
- /etc/profile: 此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行.并从/etc/profile.d目录的配置文件中搜集shell的设置.此文件默认调用/etc/bash.bashrc文件。
- /etc/bashrc:为每一个运行bash shell的用户执行此文件.当bashshell被打开时,该文件被读取.
- ~/.bash_profile/~/.bash_login/~/.profile:用户登录执行，source立即生效。每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该文件仅仅执行一次!默认情况下,他设置一些环境变量,执行用户的.bashrc文件.
    - 环境变量应该在~/.bash_profile中定义
- ~/.bashrc:每次打开新窗口时执行。该文件包含专用于你的bashshell的bash信息。与/etc/bashrc冲突则执行前者～。只对当前用户生效
- ~/.bash_logout:当每次退出系统(退出bashshell)时,执行该文件. 

### [/etc/profile与/etc/profile.d/的作用](https://www.cnblogs.com/kevin1990/p/8641315.html)
   - /etc/profile是一个脚本，这个脚本在login shell启动的时候，就是在用户登录的时候还有su切换用户的时候会执行;Non-login shell 启动的时候不会
   - /etc/profile.d/是一个文件夹 可以在里面放一些脚本用来设置一些变量和运行一些初始化过程的，/etc/profile 中使用一个for循环语句来调用这些脚本
   - ####  (对所有用户都起作用的alias)[https://blog.csdn.net/littlehaes/article/details/103144509]
   - 但是在`/etc/profile.d/00-aliases.sh 权限是644就行` 里定义的alias只对root用户有用，普通用户需要在~/.bashrc 中引入
   - profile.d 的执行顺序 -----------------------------------------------------------------------------no

### 自定义补全
- https://juejin.cn/post/6844903458261172237
- 搜索 linux 自动补全函数
### bash命令根据历史记录补全
```
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'
```
### alias
- alias 使用外部传参
   ```shell
   alias s='UpMachine(){ ssh root@$1;};UpMachine'
   $ s 192.168.22.2
   # 其实就是相当于写一个行命令 把参数不放在alias当中(怎么不放呢,就通过函数实现)
   ``` 
- alias 重启的时候会有变化
- (对所有用户都起作用的alias)[https://blog.csdn.net/littlehaes/article/details/103144509]

### [zsh 的命令行中快速输入sudo](http://www.ichenfu.com/2017/03/29/bash-zsh-fast-sudo/)
   - `bindkey -s '\e\e' '\C-asudo \C-e'`

### set 命令的主要作用是设置SHELL的属性
- link: https://blog.csdn.net/qq_35435999/article/details/125762975
- set -o vi 使用 vi 风格的行编辑界面
- set -o emacs 使用 emacs 风格的行编辑界面
### bind
- bind -p 查看所有绑定
- "\C-w" ctrl + w
- bind '"b": self-insert' 设置一个新的键绑定 将b绑定为直接输入

### inputrc bash交互舒适度的
- 这里是完整的选项说明：https://www.gnu.org/software/bash/manual/html_node/Readline-Init-File-Syntax.html
- menu-complete:https://unix.stackexchange.com/questions/24419/terminal-autocomplete-cycle-through-suggestions
```
vim ~/.inputrc
set completion-ignore-case on 终端terminal 补全设置为大小写不敏感
bind TAB:menu-complete 
# 保存，重新打开终端就可以了
```

### Terminal 里如何强化 Reversh Search
- https://blog.csdn.net/weixin_30338743/article/details/96640080

### 设置终端颜色$PS1
- link：
    - https://blog.csdn.net/pipisorry/article/details/39584489
    - https://bbs.huaweicloud.com/blogs/detail/313226
- PS1是Linux终端用户的一个环境变量，用来定义命令行提示符样式和内容的参数。
- 查看当前内容 set|grep -i ps1
- 暂时使用
    - `export PS1="\[\e[37;40m\][\[\e[32;40m\]\u\[\e[37;40m\]@\h \[\e[36;40m\]\w\[\e[0m\]]\n\$ "`
    - `export PS1="\[\e[37;40m\][\[\e[32;40m\]\u\[\e[31;40m\]@$(hostname -I |awk '{print $1}') \[\e[36;40m\]\w\[\e[0m\]]\n\$ "`
    - `export PS1="\[\e[37;40m\][\[\e[32;40m\]\t|\u\[\e[31;40m\]@$(hostname -I |awk '{print $1}') \[\e[36;40m\]\w\[\e[0m\]]\n\$ "` 
- 一些变量
    - `\[`开始一个非打印字符序列，可用于将终端控制序列嵌入到提示中
    - `\]`结束一个非打印字符序列
    - `\e` ASCII 转义字符 (033)
- 颜色定义
```cs
export PS1="\[\e[37;40m\][\[\e[32;40m\]\u\[\e[37;40m\]@\h \[\e[36;40m\]\w\[\e[0m\]]\n\$ "
# 解释：颜色的格式是\[\e[37;40m\]+要用这个颜色渲染的内容,比如\[\e[37;40m\][, 就是把[用前面那个颜色表示出来;\[\e[37;40m\]@\h 就是把@和\h代表的主机名和一个空格用前面的颜色表示出来
[root@iZuf68h0usx91bux03msu1Z ~/j_go/monitor/gopath/src/github.com/prometheus/mysqld_exporter]
$
# 也可以直接\e[37;40m 因为\[是一个非打印字符序列的开始标志 
# \e也可以替换为\033
# \e[F;Bm]，其中“F“为字体颜色，编号为30-37；“B”为背景颜色，编号为40-47时控制颜色，编号为0-8时控制命令行样式，0m的时候会覆盖F的格式，5m的话是颜色变化，文字闪烁https://zhuanlan.zhihu.com/p/340003720
# F可以省略
# 最后要加一个\e[0m否则命令行里的输入也会跟着最后一个样式
```
- 使用变量、命令、函数和shell脚本
```cs
# 使用变量
STARTCOLOR='\e[0;34m';
ENDCOLOR="\e[0m"
export PS1="$STARTCOLOR\u@\h \w> $ENDCOLOR"
# 使用命令
export PS1="\!|\h|$(uname -a)|\$?> "
# 使用函数
function httpdcount {
  ps aux | grep httpd | grep -v grep | wc -l
}
export PS1='\u@\h [`httpdcount`]> '
```
### 控制 PS1、PS2、PS3、PS4 和 PROMPT_COMMAND
- link：
    - https://bbs.huaweicloud.com/blogs/313225
- PROMPT_COMMAND在显示 PS1 变量之前执行 PROMPT_COMMAND 的内容。
```cs
ramesh@dev-db ~> export PROMPT_COMMAND="date +%k:%m:%S"
22:08:42
ramesh@dev-db ~>
[Note: This displays the PROMPT_COMMAND and PS1 output on different lines]
# 如果要在与 PS1 相同的行中显示 PROMPT_COMMAND 的值，请使用 echo -n ，如下所示。
ramesh@dev-db ~> export PROMPT_COMMAND="echo -n [$(date +%k:%m:%S)]"
[22:08:51]ramesh@dev-db ~>
[Note: This displays the PROMPT_COMMAND and PS1 output on the same line]
```
# other
