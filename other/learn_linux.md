1. #### nl filename 带行号显示文件内容
1. [sed](https://www.runoob.com/linux/linux-comm-sed.html)
- -i 直接修改文件
- -e '$assssss' filename 在最后一行后添加aaaaaa
- $ 代表最后一行

### Linux之间配置SSH互信（SSH免密码登录）
[lind](https://blog.csdn.net/linxc008/article/details/81278446)
将已经生成的公钥私钥对id_rsa.pub发送到其他的服务器上。
```shell
# 命令
ssh-copy-id -i /root/.ssh/id_rsa.pub 192.168.137.129
# 或者手动
ssh root@web-2 cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
```

### vim
1. 在 10 - 20 行添加 # 注释 `:10,20s/^/#/g`


### 行内for 循环
```shell
for i in `seq 1 10`;do; echo $i;done
for file in `ls|grep apk`;do; adb install $file;done
# 最后一个分号可以不写
for file in `adb shell pm list package -3`;do;echo ${file#*:};done;
for file in `adb shell pm list package -3`;do;echo ${file#*:};done

```
### 单引号和双引号的区别
单引号内的东西都会原样输出
双引号不会

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


### 对所有用户都起作用的alias ()[https://blog.csdn.net/littlehaes/article/details/103144509]
### grep 中过滤grep的内容 ps -ef|grep xxx|grep -v grep
```
    [root@testdb2 ~]# grep -Fx ls_recurse_enable=YES  /etc/vsftpd/vsftpd.conf
    ls_recurse_enable=YES



    -w 精确匹配

    -Fx  完全匹配
```

### docker
`docker top android_1 | grep com.hexin | awk '{print $2;exit}`
```
 docker exec -it android_1 sh -c "ps -a|grep com.hexin" | awk '{print $2;exit}'
```
