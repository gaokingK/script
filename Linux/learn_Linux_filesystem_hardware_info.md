# To：文件系统和其他的硬件信息、系统版本
## link：
- 备份文件后扩展https://juejin.cn/post/6939387305119612935
- 一些问题：https://juejin.cn/post/7185063214453882940
- 硬件和软件都有：https://juejin.cn/post/7185063214453882940
## 一些概念
- **索引节点，也就是 inode**，用来记录文件的元信息，比如 inode 编号、文件大小、访问权限、创建时间、修改时间、数据在磁盘的位置等等。索引节点是文件的唯一标识，它们之间一一对应，也同样都会被存储在硬盘中，所以索引节点同样占用磁盘空间。
- **文件系统和分区** 文件系统和分区是两个紧密相关但并不相同的概念，他们是属于同一个层级的概念，一个分区只有一种文件系统；
- 一块SCSI硬盘最大分区只能分三个主分区加一个扩展分区, 而扩展分区最多可分15个逻辑分区, 这是硬件限制，不能突破。
### 逻辑分区和扩展分区

在 Linux 系统中，逻辑分区（Logical Partitions）通常是在扩展分区（Extended Partition）中创建的。逻辑分区是用于进一步划分磁盘空间的分区类型。由于逻辑分区是在扩展分区中创建的，因此它们的设备名通常与物理分区有所区别。

逻辑分区的设备名通常以 "sda5"、"sda6" 等形式命名，其中 "sda" 是磁盘标识，数字表示分区号。例如，"sda5" 表示磁盘上的第一个逻辑分区。

如果你想从命名上区分逻辑分区，可以注意以下几点：

分区号： 逻辑分区的分区号通常是 5 开始的整数。例如，"sda5"、"sda6"、"sda7" 等。

设备名： 逻辑分区的设备名通常以磁盘标识和分区号组成，例如 "sda5"。与物理分区相比，逻辑分区的分区号往往较大。

挂载点： 通过查看分区的挂载点（如果已经挂载），你可能能够推断出逻辑分区的用途。逻辑分区的挂载点可能包括 "/home"、"/var"、"/usr" 等。

分区表信息： 使用命令如 fdisk -l 或 parted -l 查看分区表信息。逻辑分区通常位于扩展分区内。
# 文件系统
- link：
    - 一口气搞懂「文件系统」，就靠这 25 张图了：https://www.cnblogs.com/xiaolincoding/p/13499209.html
- Linux 磁盘管理常用三个命令为 df、du 和 fdisk。
    - df（英文全称：disk full）：列出文件系统的整体磁盘使用量
    - du（英文全称：disk used）：检查磁盘空间使用量
    - fdisk：用于磁盘分区
    - ls 只能查看文件的大小，但是不能查看文件夹的
## 软连接和硬链接
- 以l开头的是软链接 , 相当于快捷方式；以-开头的是硬链接
- 创建一个file的软链接 `ln -s  软链接` 创建一个file的硬链接 `ln hello 源文件 或 link hello 源文件 `
- 硬链接是多个目录项中的「索引节点」指向一个文件，也就是指向同一个 inode，但是 inode 是不可能跨越文件系统的，每个文件系统都有各自的 inode 数据结构和列表，所以硬链接是不可用于跨文件系统的。由于多个目录项都是指向一个 inode，那么只有删除文件的所有硬链接以及源文件时，系统才会彻底删除该文件。所以源文件删除的时候，硬链接还是可以使用的
- 目录下面的.和子目录下面的..都是指向目录的硬链接
- 软连接是相当于重新创建一个文件，就是重新创建一个inode，但是这个文件的内容是被连接的文件的地址，所以访问软链接的时候，其实是访问另外一个文件；所以软链接可以指向目录并且可以跨越文件系统。源文件删除的时候，软链接并不会被删除，而会变成一个死连接
## wei'sen'm
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
- 只输出特定的格式 https://developer.aliyun.com/article/87799
```cs
// -output={field_name1,field_name2...} 选项用于显示 df 命令某些字段的输出。
// 可用的字段名有: source, fstype, itotal, iused, iavail, ipcent, size, used, avail, pcent和 target
df --output=fstype,size,iused
```

## du 对文件和目录磁盘使用的空间的查看[link](https://www.cnblogs.com/wanng/p/linux-du-command.html)
- -h ：以人们较易读的容量格式 (G/M) 显示；
- -a 将文件的容量也列出来
- -m/k 以 MBytes/KBytes 列出容量显示；是整数
- -k显示的是文件所占磁盘块的大小
- -d 是 --max-depth=N 选项的简写，表示深入到第几层目录,超过指定层数目录则忽略
- -c 显示几个文件或目录各自占用磁盘空间的大小，还统计它们的总和
- -s: 显示目录总大小
- `find . -type f -exec du -hm {} + | sort -r | head -n 5`
``` shell
# 检查目录底下每个目录所占用的容量
du -sm path
du -h -d1 # 查看当前文件夹内各文件和文件夹的总大小 # 有时命令会运行很久
du -sh # 查看当前文件夹的总大小
du -c log30.tar.gz log31.tar.gz
```


## fdisk是 Linux 的磁盘分区表操作工具。
- link：https://linux.cn/article-10508-1.html
- fdisk -l 可以查看所有物理磁盘的大小和该磁盘下的分区
```cs
Disk /dev/sda: 30 GiB, 32212254720 bytes, 62914560 sectors //Disk /dev/sda: 这部分指示了磁盘的设备名。/dev/sda 是第一个磁盘。下面有第二个磁盘名/dev/sdb
// hda一般是指IDE接口的硬盘，hda指第一块硬盘，hdb指第二块硬盘,等等；sda一般是指SATA接口的硬盘，sda指第一块硬盘，sdb指第二块硬盘，等等
// 30 GiB, 32212254720 bytes, 62914560 sectors: 这是磁盘的容量信息，包括容量以 GiB 和字节表示，以及扇区数量。
Units: sectors of 1 * 512 = 512 bytes //Units: 这里说明了扇区的大小。
Sector size (logical/physical): 512 bytes / 512 bytes//Sector size (logical/physical): 这部分显示了逻辑扇区和物理扇区的大小。
I/O size (minimum/optimal): 512 bytes / 512 bytes//I/O size (minimum/optimal): 这部分指示了 I/O 操作的最小和最佳块大小。
Disklabel type: //dos Disklabel type: dos: 这表示磁盘使用的分区表类型是 DOS 分区表。
Disk identifier: 0xeab59449//Disk identifier: 0xeab59449: 这是磁盘的唯一标识符。
Device     Boot    Start      End  Sectors Size Id Type //接下来是分区信息：这里只有一个，有可能有多个
// /dev/sda1: 这是磁盘上的一个分区，具体是 /dev/sda 硬盘的第一个分区。
// Boot: 如果列有星号 *，表示这是引导分区。
// Start/End/Sectors/Size: 这些列显示了分区的起始扇区、结束扇区、总扇区数以及分区的大小。
// Id: 这是分区的标识符，例如，83 表示 Linux 分区。
// Type: 这是分区的类型。
/dev/sda1  *    20973568 62914559 41940992  20G 83 Linux

// 其他硬盘的信息 
Disk /dev/sdb: 10 GiB, 10737418240 bytes, 20971520 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

## 磁盘格式化 
- mkfs [-t 文件系统格式] 装置文件名

## 磁盘检验 fsck（file system check）用来检查和维护不一致的文件系统。

## 磁盘挂载与卸除
- vim /etc/fstab/ 看挂载
## mount
- https://www.runoob.com/linux/linux-comm-mount.html
- mount /dev/hda1 /mnt 将前面的目录挂载到后面的目录上去 cd /mnt 正常使用的是后面的目录
- 查看系统内的挂载信息 直接输入mount
- 挂载和递归挂载 bing rbing https://blog.csdn.net/realmeh/article/details/17888613
   - 区别的就拿来mount的目录，如果里面还有挂载的目录，那里面挂载目录的东西就不会被挂载到最新的目录里面，而rbind可以
   - 只挂载当下目录的文件，不挂载当下目录里面的文件夹这种理解是不正确的，两种挂载方式都是挂载子目录的
- 是这样吗
>mount --bind test1 test2为例，当mount --bind命令执行后，Linux将会把被挂载目录的目录项（也就是该目录文件的block，记录了下级目录的信息）屏蔽，即test2的下级路径被隐藏起来了（注意，只是隐藏不是删除，数据都没有改变，只是访问不到了）。同时，内核将挂载目录（test1）的目录项记录在内存里的一个s_root对象里，在mount命令执行时，VFS会创建一个vfsmount对象，这个对象里包含了整个文件系统所有的mount信息，其中也会包括本次mount中的信息，这个对象是一个HASH值对应表（HASH值通过对路径字符串的计算得来），表里就有 /test1 到 /test2 两个目录的HASH值对应关系。
命令执行完后，当访问 /test2下的文件时，系统会告知 /test2 的目录项被屏蔽掉了，自动转到内存里找VFS，通过vfsmount了解到 /test2 和 /test1 的对应关系，从而读取到 /test1 的inode，这样在 /test2 下读到的全是 /test1 目录下的文件。
https://www.cnblogs.com/weihua2020/p/13872964.html



## lsblk 用于列出所有可用块设备的信息 查看的是磁盘分区 df -h 看到是文件系统 两个命令通过mount on 和mountpoint对应
- link: http://ipcmen.com/lsblk
- TYPE：
    - disk 代表是磁盘
    - part 是分区
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
### lvm 逻辑卷管理
- link: 
    - https://juejin.cn/post/7080319811338633230
    - 逻辑卷LVM和磁盘配额简述: https://juejin.cn/post/7260034286279508024
    - LVM基本介绍与常用命令:https://www.cnblogs.com/jackruicao/p/6258812.html
- LVM是linux对硬盘分区的管理机制，为我们提供逻辑磁盘的概念，使文件系统不在关注底层物理磁盘的概念
- 物理卷（Physical Volume，PV）：就是真正的     物理硬盘     或      分区
- 卷组（Volume Group，VG）：将多个物理卷合起来就组成了卷组。组成同一个卷组的物理卷可以是同一块硬盘的不同分区，也可以是不同硬盘上的不同分区。我们可以把卷组想象为一块逻辑硬盘。
- 逻辑卷（Logical Volume，LV）：卷组是一块逻辑硬盘，硬盘必须分区之后才能使用，我们把这个分区称作逻辑卷。逻辑卷可以被格式化和写入数据。我们可以把逻辑卷想象为分区。
- 物理扩展（Physical Extend，PE）：PE 是用来保存数据的最小单元，我们的数据实际上都是写入 PE 当中的。PE 的大小是可以配置的，默认是 4MB。

### /dev/mapper
- link:
    - https://blog.csdn.net/u011495642/article/details/80197155
- /dev/mapper/Volume-lv_root的意思是说你有一个VG (volume group卷组)叫作Volume, 这个Volume里面有一个LV叫作lv_root。其实这个/dev/mapper/Volume-lv_root文件是一个连接文件，是连接到/dev/dm-0的，你可以用命令ll /dev/mapper/Volume-lv_root进行查看。
- 其实在系统里/dev/Volume/lv_root 和 /dev/mapper/Volume-lv_root以及/dev/dm-0都是一个东西，都可当作一个分区来对待。
## 一次简单的扩容硬盘未满（所有的分区未占满硬盘的空间），只是其中的某个分区满了
- 别的办法: 
    - https://juejin.cn/post/6939387305119612935
    - PV、VG、LV介绍：https://juejin.cn/post/7273025938937774120?searchId=202310121707024E4EB30EBCBEEC4BE0CF
```shell
df -h 找出快满的文件系统，比如这里是/dev/vda1
[root@root ~]# df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        477M     0  477M   0% /dev
tmpfs           490M     0  490M   0% /dev/shm
tmpfs           490M   50M  441M  11% /run
tmpfs           490M     0  490M   0% /sys/fs/cgroup
/dev/vda1        30G  2.8G   34G   9% / 
tmpfs            98M     0   98M   0% /run/user/0
# 通过lsblk来看硬盘是否有空间 发现还有1G (因为vda下面有两个vad1和vda2，40G-1023M-38G等于是还有1G)
[root@root ~]# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
vda    253:0    0   40G  0 disk
├─vda2 253:2    0 1023M  0 part [SWAP]
└─vda1 253:1    0   38G  0 part /

扩展分区：
如果您的分区是 LVM（Logical Volume Management）卷，您可以使用 lvextend 命令来扩展它。首先，查找逻辑卷的名称和卷组，然后执行以下命令：
sudo lvextend -l +100%FREE /dev/vda1 
或者 指定增加的大小
sudo lvextend -L +1G /dev/vda1 
刷新分区:
resize2fs /dev/vda1 
```
## lvextend 
- --resizefs # 加上这个后the filesystem type would have been automatically deduced, avoiding trying to use resize2fs in lieu of `xfs_growfs'.
## 问题
### resize2fs /dev/centos/root 刷新分区时Couldn‘t find valid filesystem superblock.
- 由于系统为centos7系统，文件格式为xfs
- 所以需要使用以下命令刷新lv `xfs_growfs  /dev/centos/root`

### Couldn't create temporary archive name.
- link：https://unix.stackexchange.com/questions/389539/lvm-couldnt-create-temporary-archive-name
- lvextend -An -L+5G /dev/mapper/vg08_root # 禁用了元数据备份

### 文件被占用
- 直接接触占用 fuser -km /home/

### 如何使用dd命令生成一个大小为500M的文件？
- dd if=/dev/zero of=/bigfile bs=1024k count=500

# 硬件信息

## GPU查看 `lspci|grep -i vga`
    - link: https://blog.csdn.net/dcrmg/article/details/78146797

## CPU `lscpu`
###  CPU 架构
对此了解不全面，可能有错误
- 一共有两种架构x86_64和Altarch(又叫ARM？)
- ARM
    - 标识为ARMv8 / ARM64 / aarch64
- x86

## 硬盘

### HDD HHD SSD sata sas nvme
- SSD是固态硬盘、HDD是机械硬盘、HHD是混合硬盘。
- IDE、SATA和SAS分别是链接电脑主板的接口类型
- IDE是之前的接口类型：https://blog.csdn.net/weixin_44395686/article/details/105228268
- sas SAS是并行SCSI接口之后开发出的全新接口

## 内存
-  `lsmem` 查看硬件
- free 查看内存大小
    - -m 以M为单位

# 系统版本 # uname
```
uname -a
```



# Linux 发行版本
## - [查看linux内核版本和发行版本](https://blog.csdn.net/networken/article/details/79771212?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control)
## centos
- AltArch
```
[root@agentX2 ~]# cat /etc/redhat-release
CentOS Linux release 7.6.1810 (AltArch)
```
## uname -r
## cat /etc/issue
# 权限 # 文件权限
- 如果某个用户没有某个文件夹的权限，也是能够进去这个文件夹的，只是ll会提示没有permissions
- user_a进入test，root删除root后重新创建test，把user_a的权限全部取消，user_a任然能ll，但是看不到文件了，重新进入后提示没有权限
# chown
- 用于更改文件或目录的所有者（owner）。 
- chown [新所有者]:[新所属组] 文件或目录 `chown boslog logs` `chown -R boslog logs` 前者只是把文件夹的权限，后者还有里面文件的权限

### chmod u+x file 表示为文件的所有者增加可执行权限
   - [link](https://www.cnblogs.com/du-jun/p/11550968.html)
   - u+x 是两个部分u、+x
      - u、g、o、a
        - u 当前用户、g当前用户组、o其他、a所有人
      - +x 可执行
        - +w 可读
        - r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该文件是个子目录或者该文件已经被设定过为可执行。 

# umask
- umask（文件创建掩码）是一种权限掩码，它用于确定在创建新文件或目录时默认权限的值。umask 值是从默认权限中减去的，因此它表示不允许设置的权限位。
- umask 值通常是全局设置的，适用于所有用户和所有文件夹。这意味着，默认情况下，所有新创建的文件和目录都受到相同的 umask 影响。
- 目录的默认权限是0777，文件的默认权限是0666，这是固定的，但umask的值不是固定的，假设当前用户的umask为0022，那么当创建一个目录时新目录的权限就是0777-0022=0755（这只是一个把运算简单化了，实际的是https://blog.csdn.net/Code_LT/article/details/121077060）

### 引起的问题，root用户起一个日志采集进程，这个采集进程会在/boslog/mave/logs/下产生日志文件，受不同服务器上umask值的影响这些文件的权限是有可能不一样的，想在想让boslog这个用户也有日志文件的只读权限。
- 不同服务器上的umask值不一样，这会使不同服务器上新产生的mave.log的权限不一样
- 假如mave.log 以前的权限是640，给他改成了644，但是当mav.log回滚的时候又会变成640了
- 尝试chown -R 把文件夹当前属主更改为boslog，但是使用root新创建的文件由于umask的原因还是不能被boslog访问
- 最后的解决方法
```cs
1. 判断umask最后一位是否为0，是的话继续下一步
2. 使用chmod 为文件夹增加boslog的访问权限 chmod -R o+r /boslog/mave/logs
3. 更改目录的ACL权限来为boslog用户增加以后新产生文件的访问权限 setfacl -m d:u:boslog:r /boslog/mave/logs
```

# ACL # getfacl # setfacl 
- 文件系统 ACL（访问控制列表）:https://www.cnblogs.com/sparkdev/p/5536868.html
- 如果存在一个目录，使用setfacl -m d:u:boslog:r dir——name 为dir分配boslog的读权限后，只有新增加的文件能访问，以前的文件不能访问，而且ll也会提示没有权限，但是能进入
    - -m 修改acl权限
    - d 代表修改文件夹的，如果是文件setfacl -m u:boslog:r file_path
    - u:后面跟修改的用户
    - r增加的权限 增加写就是w
- 文件删除后acl信息也会删除，新创建的同名的也不会是原来的
- 应该是只有文件的属主才能对该文件执行setfacl命令