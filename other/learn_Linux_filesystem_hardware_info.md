# 文件系统和其他的硬件信息、系统版本
# 文件系统
- Linux 磁盘管理常用三个命令为 df、du 和 fdisk。
    - df（英文全称：disk full）：列出文件系统的整体磁盘使用量
    - du（英文全称：disk used）：检查磁盘空间使用量
    - fdisk：用于磁盘分区
    - ls 只能查看文件的大小，但是不能查看文件夹的
## du 和 df的区别
- du(disk usage)是通过搜索文件来计算每个文件的大小然后累加，du能看到的文件只是一些当前存在的，没有被删除的。他计算的大小就是当前他认为存在的所有文件大小的累加和。
- df(disk free)通过文件系统来快速获取空间大小的信息，当我们删除一个文件的时候，这个文件不是马上就在文件系统当中消失了，而是暂时消失了，当所有程序都不用时，才会根据OS的规则释放掉已经删除的文件， df记录的是通过文件系统获取到的文件的大小，他比du强的地方就是能够看到已经删除的文件，而且计算大小的时候，把这一部分的空间也加上了，更精确了。
- 当文件系统也确定删除了该文件后，这时候du与df就一致了。

## df 检查文件系统的磁盘空间占用情况。可以利用该命令来获取硬盘被占用了多少空间，目前还剩下多少空间等信息。
- link
  - https://blog.csdn.net/wisgood/article/details/17316663
- linux中df命令的输出清单的第1列是代表文件系统对应的设备文件的路径名（一般是硬盘上的分区）；第2列给出分区包含的数据块（1024字节）的数目；第3，4列分别表示已用的和可用的数据块数目。用户也许会感到奇怪的是，第3，4列块数之和不等于第2列中的块数。这是因为缺省的每个分区都留了少量空间供系统管理员使用。即使遇到普通用户空间已满的情况，管理员仍能登录和留有解决问题所需的工作空间。清单中Use% 列表示普通用户空间使用的百分比，即使这一数字达到100％，分区仍然留有系统管理员使用的空间。最后，Mounted on列表示文件系统的挂载点。
- -h 以人们较易阅读的 GBytes, MBytes, KBytes 等格式自行显示；
- -k/m 以 KBytes/MBytes  的容量显示各文件系统；
```
[root@localhost huawei]# df -h
Filesystem               Size  Used Avail Use% Mounted on
devtmpfs                  16G     0   16G   0% /dev
tmpfs                     16G     0   16G   0% /dev/shm
tmpfs                     16G   50M   16G   1% /run
tmpfs                     16G     0   16G   0% /sys/fs/cgroup
/dev/mapper/centos-root   92G   11G   77G  13% /
/dev/sda2                922M   97M  762M  12% /boot
/dev/sda1                476M  9.1M  467M   2% /boot/efi
/dev/mapper/centos-tmp   9.4G   36M  9.3G   1% /tmp
/dev/mapper/centos-home   94G  1.7G   92G   2% /home
/dev/mapper/centos-var   838G   92G  747G  11% /var
tmpfs                    3.2G     0  3.2G   0% /run/user/0
```
- 如果文件夹太大想要减容的话有个快捷方法就是在/home 里建一个软连接，指向大容量的


## du 对文件和目录磁盘使用的空间的查看[link](https://www.cnblogs.com/wanng/p/linux-du-command.html)
- -h ：以人们较易读的容量格式 (G/M) 显示；
- -a 将文件的容量也列出来
- -m/k 以 MBytes/KBytes 列出容量显示；
- -d 是 --max-depth=N 选项的简写，表示深入到第几层目录,超过指定层数目录则忽略
- -c 显示几个文件或目录各自占用磁盘空间的大小，还统计它们的总和
- -s: 显示目录总大小
``` shell
# 检查目录底下每个目录所占用的容量
du -sm path
du -h -d1 # 查看当前文件夹内各文件和文件夹的大小 # 有时命令会运行很久
du -sh # 查看当前文件夹的总大小
du -c log30.tar.gz log31.tar.gz
```

## fdisk是 Linux 的磁盘分区表操作工具。

## 磁盘格式化 
- mkfs [-t 文件系统格式] 装置文件名

## 磁盘检验 fsck（file system check）用来检查和维护不一致的文件系统。

## 磁盘挂载与卸除
- vim /etc/fstab/ 看挂载


## lsblk 用于列出所有可用块设备的信息
- link: http://ipcmen.com/lsblk
- lsblk 查看磁盘分区
```shell
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
├─nvme0n1p6 259:6    0    14G  0 part /recovery #代表在根目录下ls中的recovery占用的空间是一个分区
└─nvme0n1p7 259:7    0    11G  0 part [SWAP] # 交换空间
```
</br>

# 硬件信息
## GPU查看 `lspci|grep -i vga`
    - link: https://blog.csdn.net/dcrmg/article/details/78146797
## CPU `lscpu`
    - aarch64 为ARM
</br>

# 系统版本
```
uname -a
```
</br>

# CPU 架构
对此了解不全面，可能有错误
- 一共有两种架构x86_64和Altarch(又叫ARM？)
- ## ARM
    - 标识为ARMv8 / ARM64 / aarch64
- ## x86
</br>

# Linux 发行版本
## - [查看linux内核版本和发行版本](https://blog.csdn.net/networken/article/details/79771212?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control)
## centos
- AltArch
```
[root@agentX2 ~]# cat /etc/redhat-release
CentOS Linux release 7.6.1810 (AltArch)
```