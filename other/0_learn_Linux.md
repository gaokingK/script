1. #### bash -c "cmd or path_to_script_what_have_exec_permission" 使用bash执行命令，命令要用双括号，
1. #### [Linux Crontab 定时任务](https://www.runoob.com/w3cnote/linux-crontab-tasks.html)
   - [时间表达式预览](https://tool.lu/crontab/)
2. #### [linux 在命令行下的快捷键](https://blog.csdn.net/u014429186/article/details/52629029)

3. #### chmod u+x file 表示为文件的所有者增加可执行权限
   1. [link](https://www.cnblogs.com/du-jun/p/11550968.html)
   2. u+x 是两个部分u、+x
      - u、g、o、a
        - u 当前用户、g当前用户组、o其他、a所有人
      - +x 可执行
        - +w 可读
        - 
4. #### linux 单用户模式
   centos 进入单用户模式 ro 改为rw（可读改为可写） `init=/bin/bash`
   修改完成后 `exec /sbin/init` 退出单用户模式
5. #### yum /y/d/N 
   d 只下载不安装
6. #### manjaro 最受欢迎的linux发行版 基于arch
7. #### [/etc/profile与/etc/profile.d/的作用](https://www.cnblogs.com/kevin1990/p/8641315.html)
   /etc/profile是一个脚本，这个脚本在login shell启动的时候，就是在用户登录的时候还有su切换用户的时候会执行;Non-login shell 启动的时候不会
   /etc/profile.d/是一个文件夹 可以在里面放一些脚本用来设置一些变量和运行一些初始化过程的，/etc/profile 中使用一个for循环语句来调用这些脚本
8. #### BSD和SystemV
- 是Unix 操作系统的两种操作风格
1. #### Linux不能称为"标准的Unix“而只被称为"Unix Like"的原因有一部分就是来自它的操作风格介乎两者之间

### vim
   1. 在 10 - 20 行添加 # 注释 `:10,20s/^/#/g`
   2. vim 里打开别的文件 -----------------------------no
   3. vim 配置------------------------------no


### 行内for 循环
```shell
for i in `seq 1 10`;do; echo $i;done
for file in `ls|grep apk`;do; adb install $file;done
# 最后一个分号可以不写
for file in `adb shell pm list package -3`;do;echo ${file#*:};done;
for file in `adb shell pm list package -3`;do;echo ${file#*:};done

```

### 字符串截取
(link)[https://www.cnblogs.com/hurryup/articles/10241601.html]
### 对过滤的文件进行操作
find . -type f -name "*.sh"|grep sh|xargs -i git add {}

### 禁止root ssh [link](https://www.cnblogs.com/toughlife/p/5633510.html)
```
vim /etc/ssh/sshd**
service sshd restart
```

### 杂
shell 中进入函数 在函数名上按# 会在函数定义和函数引用处
ctrl shift v 在vim中粘贴
按 ctrl 在命令中 以单词为单位跳转

### 磁盘空间
lsblk 查看磁盘分区
```
root@huawei-PC:~# lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda           8:0    1 931.5G  0 disk /media/huawei/5035ed46-b220-44b4-ac07-9e3dcd4fc2fe
sr0          11:0    1  1024M  0 rom  # sr开头的是系统
nvme0n1     259:0    0 238.5G  0 disk 
├─nvme0n1p1 259:1    0   300M  0 part /boot/efi
├─nvme0n1p2 259:2    0   1.5G  0 part /boot
├─nvme0n1p3 259:3    0    15G  0 part /
├─nvme0n1p4 259:4    0    15G  0 part 
├─nvme0n1p5 259:5    0 181.7G  0 part /data
├─nvme0n1p6 259:6    0    14G  0 part /recovery 代表在根目录下ls中的recovery占用的空间是一个分区
└─nvme0n1p7 259:7    0    11G  0 part [SWAP] 交换空间
```
查看磁盘空间
```
ls 只能查看文件的大小，但是不能查看文件夹的
du -h -d1 查看当前文件夹内各文件和文件夹的大小
```
vim /etc/fstab/ 看挂载


####  对所有用户都起作用的alias ()[https://blog.csdn.net/littlehaes/article/details/103144509]
   - 但是在`/etc/profile.d/00-aliases.sh 权限是644就行` 里定义的alias只对root用户有用，普通用户需要在~/.bashrc 中引入
   - profile.d 的执行顺序 -----------------------------------------------------------------------------no
#### alias 重启的时候会有变化

### docker
`docker top android_1 | grep com.hexin | awk '{print $2;exit}`
```
 docker exec -it android_1 sh -c "ps -a|grep com.hexin" | awk '{print $2;exit}'
```
