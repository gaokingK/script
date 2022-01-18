# 一些知识网站, 没事的时候可以看一下上面
- https://martinfowler.com/eaaCatalog/index.html 
# 共识
   - 对于doc, 把自己用的给记下来, 其他的了解下就行, 慢慢补充
   - SELECT column_name(s) FROM table1; # 意思是可以选择一个列或者多个列
   - [Unique [key] 而不用 [unique [key]]
   - [COLUMN_FORMAT {FIXED|DYNAMIC|DEFAULT}] 带关键字参数的
### MVCC(Mutil-Version Concurrency Control) 多版本并发控制
   - 是一种并发控制的方法， 一般在数据库管理系统中， 实现对数据库的并发访问
### 有些错误别着急，重试，重启 说不定就好了    
### mssql 指微软的SQLServer数据库服务器 ms sql
### RFC-1738 URL组合规范大概是
### [帮助中心]https://help.aliyun.com/document_detail/70478.html
### json 布尔值类型
   - true; false
### semanage
   - semanage命令 是用来查询与修改SELinux默认目录的安全上下文。
### erlang
   - Erlang是一种通用的面向并发的编程语言，它由瑞典电信设备制造商爱立信所辖的CS-Lab开发，目的是创造一种可以应对大规模并发活动的编程语言和运行环境。
   - Erlang是运行于虚拟机的解释性语言，但是也包含有乌普萨拉大学高性能Erlang计划（HiPE）开发的本地代码编译器
   - 进程间上下文切换对于Erlang来说仅仅 只是一两个环节，比起C程序的线程切换要高效得多得多了。
### IOPS（Input/Output Operations Per Second）
   - 是一个用于计算机存储设备（如硬盘（HDD）、固态硬盘（SSD）或存储区域网络（SAN））性能测试的量测方式，可以视为是每秒的读写次数
### VNC
   - Virtual Network Console 虚拟网络控制台， 可以连接到远程环境，像ssh一样
### libsodium 
   - Sodium is a modern, easy-to-use software library for encryption, decryption, signatures, password hashing and more. 
   - https://doc.libsodium.org/
### URL中%2F,%2B等特殊字符
   - link： https://blog.csdn.net/w892824196/article/details/108198197
   -  %2B 表示+号
### MSVC 微软VC运行库
   - VC运行库，是Visual C++的运行库。很多程序在编制的时候，使用了微软的运行库，大大减少了软件的编码量，却提高了兼容性。但运行的时候，需要这些运行库。这些运行库简称就是MSVC。
### BMP(Basic Multilingual Plane)
   - 基本多文种平面，BMP(Basic Multilingual Plane)，或称第零平面(Plane 0)，是Unicode中的一个编码区段
   - 是表示各种语言的
### Seafile
   - Seafile 是一个开源的文件云存储平台
### wayland和weston的介绍
   - [Linux图形系统] https://blog.csdn.net/ztguang/article/details/80452717
   - Wayland是一套display server(Wayland compositor)与client间的通信协议，而Weston是Wayland compositor的参考实现。它们定位于在Linux上替换X图形系统

### GPG
   - 目前最流行、最好用的加密工具之一。
   - [使用](https://www.ruanyifeng.com/blog/2013/07/gpg.html)
### 缩写
   - noop 没有操作
      no operate
   - RTFM(Read The Fucking Manual)
   - noqa 
      no quality assurance
   - PGO
      Profile Guided optimization 
   - LTO 
     Link Time Optimization (LTO)
   - GA(Generally Available) 通用版本
   - 关系数据库管理系统(RDBM)
### 术语
   - 性能抖动
   - 句柄(session orm database)
### 从请求中拿到数据后，再添加一些数据的过程叫什么？ ----------------------------------------------no
### 接口中的用到的临时数据，叫什么？ ----------------------------------------------no
### Grokking The System Design Interview（系统设计）
   - Grokking The System Design Interview（系统设计）
### ptaishanpublic2:Huawei123@90.90.64.10 
   - 用户名:密码@ip
### [linux下EOF写法梳理](https://www.cnblogs.com/gzxbkk/p/10298799.html)
   - EOP (end of file )表示自定义终止符, 可以随意设置别名, 在linux按ctrl-d就代表EOF
   - << :标准输入来自命令行的一对分隔号(EOF就是分隔符)的中间内容.
    ```shell
    # 怎么输入wang呢 ------------------no
    cat << wang > haha.txt
    > ggggggg
    > 4444444
    > 6666666
    > wang
    ```

### 非选项参数
### 提示符号错误的时候,首先去排除是否是看起来相同, 可能是中文的,最好的办法是从未报错的地方复制一个过来
### 程序运行时依赖的内存结构, 命名空间 ------------------------------------------未
   - 堆栈里放的帧
### 二进制安全
    redsi的string是二进制安全的，是指其可以包含任何数据，如jpg图片或者序列化的对象
### 幂等
    多次执行后结果一致
### 正则表达式
    在linux中，正则表达式分为正则表达式、扩展正则表达式和Perl 的正则表达式，不知道别的也是不是这样分的
    [扩展正则表达式](https://blog.csdn.net/yufenghyc/article/details/51078107)
### 流程图
   [link](https://blog.csdn.net/L_786795853/article/details/108878289)
```mermaid
graph LR
A[hh] --> B[hh]
```
### pycharm 不能预览markdown
   在setting>Languages_**>markdown 中显示 “ there are no available preview providers” 
   [解决方法](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360001515959-markdown-support-plugin-preview-not-working-in-linux)
   是jdk的问题
# Redis command
    hkeys 
    hgetall

    
#### Flask如何保证线程安全
[关于flask线程安全的简单研究](https://www.cnblogs.com/fengff/p/9087660.html)
简单结论：处理应用的server并非只有一种类型，如果在实例化server的时候如果指定threaded参数就会启动一个ThreadedWSGIServer，而ThreadedWSGIServer是ThreadingMixIn和BaseWSGIServer的子类，ThreadingMixIn的实例以多线程的方式去处理每一个请求
只有在启动app的时候将threded参数设置为True，flask才会真正以多线程的方式去处理每一个请求。

# 奇怪的
- 点击关闭美团的弹窗是, pyautogui的左键点击无效, 但手动能点击, 使用xdotool也点不掉, 更改点击时长也点不掉, 结果使用pg的右键点击就关闭了