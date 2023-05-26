# TO
linux中关于自定义的一些文件的介绍、怎么去自定义

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
### 终端terminal 补全设置为大小写不敏感
```
vim ~/.inputrc
set completion-ignore-case on
# 保存，重新打开终端就可以了
```
### 设置终端颜色$PS1
- link：https://blog.csdn.net/pipisorry/article/details/39584489
- PS1是Linux终端用户的一个环境变量，用来定义命令行提示符样式和内容的参数。
- 查看当前内容 set|grep ps1
- 暂时使用`export PS1="\[\e[37;40m\][\[\e[32;40m\]\u\[\e[37;40m\]@\h \[\e[36;40m\]\w\[\e[0m\]]\n\$ "`
# other
