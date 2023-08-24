### 进不去os，停留在emengercy mode fasck failed with exit status 4 
- link：https://unix.stackexchange.com/questions/107876/fsck-died-with-status-code-4
- 按提示看日志 jourtcl 
- 跳到末尾， 看爆红内容
- 发现是 fasck failed with exit status 4 是磁盘检查美过
- fsck -y path 日志中有路径红色的 # 或者 fsck.ext4 -pvf /dev/sda1
- 输入exit

### os 进不去 报 corruption of in-memory data detected shutting down filesystem 
- https://blog.csdn.net/u010033674/article/details/108205712
- 按提示看日志 jourtcl 
- 跳到末尾， 看爆红内容
- ls查看当前目录，ls -l dev/mapper查看那个是XXX-root文件；
- 使用xfs_repair命令修复XXX-root文件：`xfs_repair -L /dev/mapper/centos-root` xfs_repair第一次报无效命令，换成.exe 再报错，再换成xfs_reparie就好了 怀疑是把_写成-了
- 进行重新启动`init 6`
- 挂载镜像 ipmcset -t vmm -d connect -v nfs://70.176.56.99/iso/iso2/centos/CentOS-7.8/CentOS-7-x86_64-DVD-2003.iso
- 解除挂载镜像 ipmcset -t vmm -d disconnec
- 消除一个告警 0x
```
telnet上去  bmc ip
把/opt/pme/conf/language/event_lang_template_v2.xml 复制到/data/opt/pme/conf/language/event_lang_template_v2.xml
cp /opt/pme/conf/language/event_lang_template_v2.xml /data/opt/pme/conf/language/event_lang_template_v2.xml
并执行 killall sensor_alarm
```
- bmc 登不上
![repair bmc](../imgs/2022-09-15_191339.png)
```
telnet  name Administrator Admin@9000
ipmcget -d ip
# 如果是dhcp
ipmcset -d ipmode -v static
ipmcset -d ipaddr -v 70.176.19.23 255.255.0.0 70.176.0.1
```
- bmc 登不上2
![repair_bmc2](../imgs/repair_bmc2.png)
```
telnet  name Administrator Admin@9000
ipmcget -d ip
# 如果是双网口并且ip的网卡在聚合网口
ipmcset -d ac -v 0
```
- product ID为空，导致环境被占用不释放 `#关闭定制化开关 ipmitool raw 0x30 0x90 0x21 0x04 0x00`
- 删除双系统引导
```
1.OS引导在同一分区：
	a.通过fdisk -l看EFI所在分区
	b.挂载分区，mount /dev/sdb1 /mnt/
	c.进入cd /mnt/EFI/文件夹
	d.rm -rf 多余的系统引导文件夹，重新生成grub文件grub2-mkconfig
2.OS引导不在同一分区：
	a.通过fdisk -l查看多余OS所在分区
	b.发fdisk /dev/sda进入分区操作模式，输d,输入需要删除的分区号，多个分区重复该步骤
	c.确认没问题了输入w,将修改应用，否则输入q不保存退出,重新执行以上步骤
```
### 硬盘都在/dev下
### 进不去os，停留在emengercy mode fasck failed with exit status 4 
- link：https://unix.stackexchange.com/questions/107876/fsck-died-with-status-code-4
- 按提示看日志 jourtcl 
- 跳到末尾， 看爆红内容
- 发现是 fasck failed with exit status 4 是磁盘检查美过
- fsck -y path 日志中有路径红色的 # 或者 fsck.ext4 -pvf /dev/sda1
- 输入exit

### os 进不去 报 corruption of in-memory data detected shutting down filesystem 
- https://blog.csdn.net/u010033674/article/details/108205712
- 按提示看日志 jourtcl 
- 跳到末尾， 看爆红内容
- ls查看当前目录，ls -l dev/mapper查看那个是XXX-root文件；
- 使用xfs_repair命令修复XXX-root文件：`xfs_repair -L /dev/mapper/centos-root` xfs_repair第一次报无效命令，换成.exe 再报错，再换成xfs_reparie就好了 怀疑是把_写成-了
- 进行重新启动`init 6`
### os 进不去 报Failed to start Switch Root
- mount /dev/sda序号 /sysroot

### os 进不去 journatl 报Failed to mount /sysroot
- https://blog.csdn.net/zhezhebie/article/details/114276961
- xfs_repair -v -L /dev/dm-0 或者xfs_repair -L /dev/sda3
- 然后输入 reboot 就起来了
### os内修改ip
- https://developer.aliyun.com/article/486538

### 修改os密码
```
passwd username # 输入两次，提示路径找不到也不用管
```
### 某个键不能用了
- 看复制粘贴能显示这个键不能 还可以开启menu-complete来用tab显示含有这个键的文件
- bind -p 查看对应的键后面是不是self-insert
- 如果没有就 把 "b": self-insert 放到文件中，bind -f file_path 把b换成你自己失灵的键
- 或者bind '"b": self-insert'
### code=exited status=203/exec 错误
- link:https://blog.csdn.net/wangxiaozhonga/article/details/125322210
- 因为服务的可执行程序找不到了，就是service文件里的程序找不到了

### 有service启动不来时，可以systemctl deamon-relaod 后重新systemctl start xxx