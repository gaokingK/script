#### 简介
- Linux 磁盘管理常用三个命令为 df、du 和 fdisk。
    - df（英文全称：disk full）：列出文件系统的整体磁盘使用量
    - du（英文全称：disk used）：检查磁盘空间使用量
    - fdisk：用于磁盘分区


#### df 检查文件系统的磁盘空间占用情况。可以利用该命令来获取硬盘被占用了多少空间，目前还剩下多少空间等信息。
- -h 以人们较易阅读的 GBytes, MBytes, KBytes 等格式自行显示；
- -k/m 以 KBytes/MBytes  的容量显示各文件系统；
  
#### du 对文件和目录磁盘使用的空间的查看
- -h ：以人们较易读的容量格式 (G/M) 显示；
- -a 将文件的容量也列出来
- -m/k 以 MBytes/KBytes 列出容量显示；
``` shell
# 检查根目录底下每个目录所占用的容量
$ du -sm /*
# ls 只能查看文件的大小，但是不能查看文件夹的
du -h -d1 # 查看当前文件夹内各文件和文件夹的大小
```

#### fdisk是 Linux 的磁盘分区表操作工具。

#### 磁盘格式化 
- mkfs [-t 文件系统格式] 装置文件名

#### 磁盘检验 fsck（file system check）用来检查和维护不一致的文件系统。

#### 磁盘挂载与卸除
- vim /etc/fstab/ 看挂载


#### lsblk 用于列出所有可用块设备的信息
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
