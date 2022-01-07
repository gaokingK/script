1. #### 共识
   - 对于doc, 把自己用的给记下来, 其他的了解下就行, 慢慢补充
   - SELECT column_name(s) FROM table1; # 意思是可以选择一个列或者多个列
   - [Unique [key] 而不用 [unique [key]]
   - [COLUMN_FORMAT {FIXED|DYNAMIC|DEFAULT}] 带关键字参数的
2. #### [帮助中心]https://help.aliyun.com/document_detail/70478.html
3. ### IOPS（Input/Output Operations Per Second）
   - 是一个用于计算机存储设备（如硬盘（HDD）、固态硬盘（SSD）或存储区域网络（SAN））性能测试的量测方式，可以视为是每秒的读写次数
4. ### VNC
   - Virtual Network Console 虚拟网络控制台， 可以连接到远程环境，像ssh一样
5. ### libsodium 
   - Sodium is a modern, easy-to-use software library for encryption, decryption, signatures, password hashing and more. 
   - https://doc.libsodium.org/
6. ### URL中%2F,%2B等特殊字符
   - link： https://blog.csdn.net/w892824196/article/details/108198197
   -  %2B 表示+号
7. ### MSVC 微软VC运行库
   - VC运行库，是Visual C++的运行库。很多程序在编制的时候，使用了微软的运行库，大大减少了软件的编码量，却提高了兼容性。但运行的时候，需要这些运行库。这些运行库简称就是MSVC。
8. #### BMP(Basic Multilingual Plane)
   - 基本多文种平面，BMP(Basic Multilingual Plane)，或称第零平面(Plane 0)，是Unicode中的一个编码区段
   - 是表示各种语言的
9.  #### Seafile
   - Seafile 是一个开源的文件云存储平台
11. #### wayland和weston的介绍
   - [Linux图形系统] https://blog.csdn.net/ztguang/article/details/80452717
   - Wayland是一套display server(Wayland compositor)与client间的通信协议，而Weston是Wayland compositor的参考实现。它们定位于在Linux上替换X图形系统

11. #### GPG
   - 目前最流行、最好用的加密工具之一。
   - [使用](https://www.ruanyifeng.com/blog/2013/07/gpg.html)
11. #### 缩写
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
11. #### 术语
   1. 性能抖动
   2. 句柄(session orm database)
12. #### 从请求中拿到数据后，再添加一些数据的过程叫什么？ ----------------------------------------------no
13. #### 接口中的用到的临时数据，叫什么？ ----------------------------------------------no
14. #### Grokking The System Design Interview（系统设计）
   - Grokking The System Design Interview（系统设计）
11. #### ptaishanpublic2:Huawei123@90.90.64.10 
   - 用户名:密码@ip
11. #### [linux下EOF写法梳理](https://www.cnblogs.com/gzxbkk/p/10298799.html)
   1. EOP (end of file )表示自定义终止符, 可以随意设置别名, 在linux按ctrl-d就代表EOF
   2. << :标准输入来自命令行的一对分隔号(EOF就是分隔符)的中间内容.
    ```shell
    # 怎么输入wang呢 ------------------no
    cat << wang > haha.txt
    > ggggggg
    > 4444444
    > 6666666
    > wang
    ```

12. #### 非选项参数
13. #### 提示符号错误的时候,首先去排除是否是看起来相同, 可能是中文的,最好的办法是从未报错的地方复制一个过来
14. #### 程序运行时依赖的内存结构, 命名空间 ------------------------------------------未
   3. 堆栈里放的帧
15. #### 二进制安全
    redsi的string是二进制安全的，是指其可以包含任何数据，如jpg图片或者序列化的对象
16. #### 幂等
    多次执行后结果一致
17. #### 正则表达式
    在linux中，正则表达式分为正则表达式、扩展正则表达式和Perl 的正则表达式，不知道别的也是不是这样分的
    [扩展正则表达式](https://blog.csdn.net/yufenghyc/article/details/51078107)
18. #### 流程图
   [link](https://blog.csdn.net/L_786795853/article/details/108878289)
```mermaid
graph LR
A[hh] --> B[hh]
```
1. #### pycharm 不能预览markdown
   在setting>Languages_**>markdown 中显示 “ there are no available preview providers” 
   [解决方法](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360001515959-markdown-support-plugin-preview-not-working-in-linux)
   是jdk的问题
2. #### Redis command
    hkeys 
    hgetall

    
#### Flask如何保证线程安全
[关于flask线程安全的简单研究](https://www.cnblogs.com/fengff/p/9087660.html)
简单结论：处理应用的server并非只有一种类型，如果在实例化server的时候如果指定threaded参数就会启动一个ThreadedWSGIServer，而ThreadedWSGIServer是ThreadingMixIn和BaseWSGIServer的子类，ThreadingMixIn的实例以多线程的方式去处理每一个请求
只有在启动app的时候将threded参数设置为True，flask才会真正以多线程的方式去处理每一个请求。

### 奇怪的
- 点击关闭美团的弹窗是, pyautogui的左键点击无效, 但手动能点击, 使用xdotool也点不掉, 更改点击时长也点不掉, 结果使用pg的右键点击就关闭了