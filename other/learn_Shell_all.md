### 出错后继续执行 什么都不写的话会出错后继续执行
- https://www.cnblogs.com/my_life/articles/7085461.html
```cs
set -o errexit #增加这句话，出错之后就会退出啦
set -e #这句话和上一句是一样的，写一个就好了
```
### 命令执行结果赋值给变量 permission denied
```
inventory_path2=echo "$inventory_path"|awk -F rootfs/ '{print $2}'
要这样 var=`command` 或者 var=$(command)
```
### 脚本debug # shell调试
- https://blog.csdn.net/qq_27546717/article/details/123130393
- 前面1个加号的是命令 两个加号的是一行命令拆分出来的
```
[root@10.0.5.89 ~/jjw-deploy0529]
$ sh -x update -i inventory_10.0.5.89.yamll
+ set -e
+ '[' 2 -eq 0 ']'
+ get_opts -i inventory_10.0.5.89.yamll
+ getopts :i: argvs
+ case $argvs in
+ update_worker inventory_10.0.5.89.yamll
+ inventory_path=inventory_10.0.5.89.yamll
+ sed -i 's/^.*add_workers:/\        hide_add_workers:/' inventory_10.0.5.89.yamll # 这一行的内容是经过变量替换的
sed: can't read inventory_10.0.5.89.yamll: No such file or directory 报错了，说明是上面一行出错的

```
### 获取脚本当前目录
- link：https://www.cnblogs.com/tudou1179006580/p/14875214.html
- script_dir=$(cd $(dirname $0);pwd)