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