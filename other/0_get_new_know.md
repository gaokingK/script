# 一些知识网站, 没事的时候可以看一下上面
- https://martinfowler.com/eaaCatalog/index.html 
- [帮助中心]https://help.aliyun.com/document_detail/70478.html
- 术语库
# 共识
   - 对于doc, 把自己用的给记下来, 其他的了解下就行, 慢慢补充
   - SELECT column_name(s) FROM table1; # 意思是可以选择一个列或者多个列
   - [Unique [key] 而不用 [unique [key]]
   - [COLUMN_FORMAT {FIXED|DYNAMIC|DEFAULT}] 带关键字参数的
### 关于文件夹命名、文件命名
- linux可以随意命名
- windows只允许空格、数字、字母和除`/\:<>*`等的字符，可以自己试一下
- 文件名不符合规范可能时文件创建失败的原因
### 回调函数
- link：https://www.cnblogs.com/-wenli/p/10970136.html
- 讲了回调函数的一些设计方面的概念，并没有多大用
- 回调函数三要素
   - 中间函数：接受传入的函数的函数
   - 起始函数：调用中间函数的函数
   - 回调函数：被传入的函数
- 回调函数的作用
   - 有利于模块解耦
   - 有利于是程序更灵活
- 阻塞式回调与延迟式回调
   - 起始函数调用中间函数，中间函数执行完后起始函数继续执行
   - 延迟式回调：多于多线程有关
### RPM 软件包名中的 el5、el6、el7 是什么？
   - https://blog.csdn.net/liaowenxiong/article/details/117136545
   - EL 是 Red Hat Enterprise Linux 的简写。
   - EL6 表示软件包可以在 Red Hat 6.x，CentOS 6.x，CloudLinux 6.x 进行安装
   - EL5 表示软件包可以在 Red Hat 5.x，CentOS 5.x，CloudLinux 5.x 进行安装
   - EL7 表示软件包可以在 Red Hat 7.x，CentOS 7.x，CloudLinux 7.x 进行安装
# 名词
- 状态机
```
python按特定规则切割如下字符串怎么做
把 'cmd | grep -E "AA|BB" | grep -E "CC| DD|EE"' 切割成 ['cmd',  "grep -E 'AA|BB'", "grep -E 'CC| DD|EE'"]
说明：切割规则是以|为分隔符，但是不包括处于一对引号中的|。

写一个状态机吧
开始状态 s0
s0 - 任意字符除了 | 和 " -> s0
s0 - " -> s1
s0 - | -> s2
s1 - 任意字符除了 | 和 " -> s1
s1 - " -> s0
s1 - | -> s1
接受 s2
然后照着状态机去写代码 （下面忽略）
网上找了一个状态机转正则的库 fsm2regex，生成出来的正则是 c+(a+$+b(a+c)*b)(a+b(a+c)*b)*c，其中 a 代表“任意字符除了 | 和 "”，b 代表 "，c 代表 |，结果不能用在这里好像……
```
### shlex 切割字符
```
# 试试这个
import shlex


cmd_str = shlex.shlex('cmd | grep -E "AA|BB" | grep -E "CC| DD|EE"', posix=True)
cmd_str.quotes = '"'
cmd_str.whitespace = '|'
cmd_str.whitespace_split = True
cmd_str = list(cmd_str)
b = []
for item in cmd_str:
    b.append(item.strip())
print(b)
# ['cmd', 'grep -E AA|BB', 'grep -E CC| DD|EE']
# 或者
if we read the pattern literally, " | " (| prefixed and suffixed with single space) is the delimiter.
cmd.split(" | ") will do the job
```
### python交互中导入的方法，在原方法改变后，这里的不生效
### MVCC(Mutil-Version Concurrency Control) 多版本并发控制
   - 是一种并发控制的方法， 一般在数据库管理系统中， 实现对数据库的并发访问
### 有些错误别着急，重试，重启 说不定就好了    
- postman发不了请求了，最后发现是本机开代理了
### mssql 指微软的SQLServer数据库服务器 ms sql
### RFC-1738 URL组合规范大概是
### json 布尔值类型
   - true; false、
### 包命名
```
https://download.libsodium.org/libsodium/releases/README.html
Libsodium distribution files
The files in this [directory](https://download.libsodium.org/libsodium/releases) are signed with Minisign, and, for the manually-generated ones, with GPG as well.

The relevant public keys can be found in the libsodium documentation.

LATEST.tar.gz is a direct link to the latest stable version of the source code. It is an automated daily copy of the stable branch in the Git repository.
libsodium-x.y.z.tar.gz is the source code of version x.y.z. These files are immutable. They don't receive any bug fixes or security updates. These will have to wait until a new point version is released.
libsodium-x.y.z-mingw.tar.gz contain pre-built libraries for Windows, built using MingW on MSYS2. These archives include Win32 and Win64 versions of the static and shared libraries, as well as the debugging symbols. These files are immutable. The code having been compiled is exactly the one from the point release, without any bug or security fixes.
libsodium-x.y.z-msvc.zip contains pre-built libraries for Windows, built using Visual Studio. These archives include Win32 and Win64 versions of the static and shared libraries, built for Visual Studio 2015, 2017, 2019 and 2022, as well as the debugging symbols. These files are immutable. The code having been compiled is exactly the one from the point release, without any bug or security fixes.
libsodium-x.y.z-stable.tar.gz is the source code of x.y.z with bug fixes, security fixes and minor improvements immediately backported from the next version being currently in development. These additions over the point release are guaranteed to never change the behavior or API. Version x.y.z-stable is always fully compatible with version x.y.z. New features or breaking changes will never be introduced in a stable set of changes. libsodium-x.y.z-stable.tar.gz is an automated daily copy of the stable branch in the Git repository.
libsodium-x.y.z-stable-mingw.tar.gz and libsodium-x.y.z-stable-msvc.zip are pre-built libraries for Windows of x.y.z-stable. They are updated when the additions actually produce different code, or when major updates of Visual Studio or MinGW have been released.
.sig files are detached GPG signatures, and .minisig files are Minisign signatures, that can be verified with:
minisign -P RWQf6LRCGA9i53mlYecO4IzT51TGPpvWucNSCh1CBM0QTaLn73Y7GFO3 -m <file>

stable versions are regularly updated. Signatures should be used to verify them. If you need to pin a specific stable version, check out the relevant revision from the stable branch of the Git repository.

Development code is only available in Git, and should never be used in production.
```
### MSYS2
- MSYS2 is a collection of tools and libraries providing you with an easy-to-use environment for building, installing and running native Windows software.
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

# 自动化工厂
- 文档中心
- 巡检
# pc测试
视频测试
# ovs

# compass-ci

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

# 奇怪的
- 点击关闭美团的弹窗是, pyautogui的左键点击无效, 但手动能点击, 使用xdotool也点不掉, 更改点击时长也点不掉, 结果使用pg的右键点击就关闭了
## 因为代理的错误
- `res = requests.post(url=f"http://90.90.0.224:8088/record` 却连到90.90.0.64:8080
```
[2022-02-21 14:53:49,967]<tid=281473365832192>INFO [/var/local/FlaskDemo/web_api/service/video_service.py][line 16] - send record to http://90.90.0.224:5010
[2022-02-21 14:53:49,970]<tid=281473365832192>DEBUG [/root/archiconda3/lib/python3.7/site-packages/urllib3/connectionpool.py][line 205] - Starting new HTTP connection (1): 90.90.64.10:8080
[2022-02-21 14:53:56,057]<tid=281473365832192>DEBUG [/root/archiconda3/lib/python3.7/site-packages/urllib3/connectionpool.py][line 393] - http://90.90.64.10:8080 "POST http://90.90.0.224:5010/record HTTP/1.1" 504 74879
```
   - 而且在别的机器上也没浮现，这是因为这台机器上设置了代理
- celery 获取不到rquest.get().json() 不用celery却能够获取
```
# code
put_video_handler(args) # 这里是正常执行的
put_video_handler.apply_async(args=(args,)) # 这里就会爆出下面的错误

@celery_app.task()
def put_video_handler(video_path):
    logger.info("video put start")
    res = requests.post(url=f"{record_server}/video_put", data=json.dumps({"file_name": video_path}))
    print(res.json())
# celery log
[2022-02-22 15:18:36,456: ERROR/ForkPoolWorker-64] Task web_api.service.video_service.testa[4bceab73-3a36-4526-9fa5-58e356d952d5] raised unexpected: JSONDecodeError('Expecting value: line 1 column 1 (char 0)
')
Traceback (most recent call last):
  File "/root/archiconda3/lib/python3.7/site-packages/celery/app/trace.py", line 451, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/root/archiconda3/lib/python3.7/site-packages/celery/app/trace.py", line 734, in __protected_call__
    return self.run(*args, **kwargs)
  File "/var/local/FlaskDemo/web_api/service/video_service.py", line 51, in testa
    res = res.json()
  File "/root/archiconda3/lib/python3.7/site-packages/requests/models.py", line 897, in json
    return complexjson.loads(self.text, **kwargs)
  File "/root/archiconda3/lib/python3.7/json/__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "/root/archiconda3/lib/python3.7/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/root/archiconda3/lib/python3.7/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```
- 分析 res.text发现 是w3拦截了，但是很奇怪为什么不交给异步就没关系，后来发现是borker没有加到代理白名单里，加入，解决