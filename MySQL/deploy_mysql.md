# for win
- link:https://juejin.cn/post/6854573215290359821
- 只需要安装这一个就可以了
### 出现的问题：
- 运行mysqld --initialize --user=root --console提示data创建不成功时的路径合my.ini中配置的文件路径不一样
```
这是因为ini中的D:\softwares中的\s被转义了， 解决方法时把安装目录换到了D:\mysql-8.0.24-winx64
```
- net start mysql 提示：发生系统错误 2
    - link：https://blog.csdn.net/XIAOGUANG_/article/details/86468993
    - 这是因为运行mysql install 之后又更换了目录，解决方法是mysql remove 后mysql install
- 在添加环境变量的时候是把bin目录添加到系统变量里面
- 修改密码的语句是alter user user() identified by "XXX"; 把想设置的密码放到双引号里
- 带debug-test的是带测试用例的好像是