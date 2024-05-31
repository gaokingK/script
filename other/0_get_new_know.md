# 一些知识网站, 没事的时候可以看一下上面
- https://martinfowler.com/eaaCatalog/index.html 
- [帮助中心]https://help.aliyun.com/document_detail/70478.html
- 术语库
# 共识
   - 对于doc, 把自己用的给记下来, 其他的了解下就行, 慢慢补充
   - SELECT column_name(s) FROM table1; # 意思是可以选择一个列或者多个列
   - [Unique [key] 而不用 [unique [key]]
   - [COLUMN_FORMAT {FIXED|DYNAMIC|DEFAULT}] 带关键字参数的

# windows
### 可以设置为不同窗口使用不同的输入法，这样就不用来回切换中英文了
- “开始”>“设置”>"设备">"输入">“高级键盘设置”；勾选“允许我为每个应用窗囗使用不同的输法”复选框即可。
- link：https://zhuanlan.zhihu.com/p/82643303
### 在命令行打开文件夹 explorer .
### 注册表编辑器好像是全字匹配的
### Registry Workshop 可以用来搜索替换windows中的路径https://blog.csdn.net/Melo_FengZhi/article/details/113919143
### where 与 gcm
- 获取可执行文件的路径， gcm也差不多
- link: https://stackoverflow.com/questions/304319/is-there-an-equivalent-of-which-on-the-windows-command-line

### 使用什么命令来查看cmd中输入的alias的完整路径呢
```
C:\Users\jw0013109>pip
Fatal error in launcher: Unable to create process using '"d:\softwares\python 2.7.18_64\python.exe"  "D:\softwares\Python27\Scripts\pip.exe"
# pip 应该是等于d:\softwares\python 2.7.18_64\python.exe D:\softwares\Python27\Scripts\pip.exe 
# 这些用什么去看呢？ 又是如何设置的呢？
```

# other
- 比如从[这里](https://github.com/Charmve)看到了cpp的图标以及一些常用的语言和框架、工具和环境
- 语义化版本 就是版本的命名 https://semver.org/lang/zh-CN/

# Hyper-V 和 WSL 2 是两个不同的微软虚拟化技术，它们提供的具体功能和用途大相径庭。下面我们详细探讨一下这两者的区别：

### Hyper-V

**Hyper-V** 是微软的硬件虚拟化产品，主要用于创建和管理虚拟机 (VM) 环境。它是一个全功能的虚拟化解决方案。

#### 特点：

1. **完整的虚拟化**：
   - **Hyper-V** 提供硬件级别的虚拟化，允许你创建完整的虚拟机，每个虚拟机都有自己的独立操作系统。
   
2. **多种使用场景**：
   - 主要用于运行高度隔离的环境，比如服务器虚拟化、创建开发和测试环境、运行旧版应用程序等。

3. **隔离性**：
   - 每个虚拟机都有独立的硬件资源（CPU、内存、磁盘、网络），完全隔离，不共享资源。

4. **管理工具**：
   - 提供 GUI 和命令行工具（如 Hyper-V 管理器和 PowerShell），用于管理和配置虚拟机。

5. **性能开销**：
   - 因为是完整的虚拟化，每个虚拟机都需要运行独立的操作系统，有一定的性能开销和资源消耗。

### WSL 2 (Windows Subsystem for Linux 2)

**WSL 2** 是微软提供的一个子系统，允许用户在 Windows 环境下运行 Linux 内核。它不是一个完整的虚拟化解决方案，而是旨在提供轻量级的、与 Windows 紧密集成的 Linux 环境。

#### 特点：

1. **轻量级虚拟化**：
   - **WSL 2** 使用一个轻量级的虚拟机，但其目的是提供一个与 Windows 密切集成的 Linux 环境，而不是一个完全隔离的独立系统。

2. **快速启动与低资源占用**：
   - WSL 2 启动速度很快，相比 Hyper-V 启动一个完整的虚拟机，WSL 2 更加高效。
   
3. **文件系统访问**：
   - 支持从 Windows 访问 Linux 文件系统和从 Linux 访问 Windows 文件系统，便于跨平台开发。

4. **集成开发环境**：
   - 适合开发者在 Windows 上使用 Linux 工具链，比如开发、构建和调试 Linux 应用。

5. **共享资源**：
   - 因为不是完全隔离的虚拟机，WSL 2 与主机系统共享资源，能更高效地使用 CPU 和内存。

### 区别总结

| 特点                | Hyper-V                                  | WSL 2                       |
|---------------------|------------------------------------------|-----------------------------|
| 类型                | 完整的虚拟化解决方案                      | 轻量级 Linux 子系统       |
| 使用场景            | 服务器虚拟化、测试环境、运行独立 OS       | 跨平台开发、运行 Linux 工具链 |
| 资源占用            | 较高，运行完整的操作系统                  | 较低，集成在 Windows 中   |
| 文件系统互访        | 独立，较为复杂                            | Windows 与 Linux 互访便捷 |
| 启动速度            | 较慢，需要启动完整 OS                     | 快速启动                   |
| 隔离性              | 高，每个 VM 独立                          | 较低，共享系统资源         |

### 选择

- **选择 Hyper-V**：如果你需要高度隔离的环境，创建多个完全独立的操作系统，进行服务器虚拟化或运行需要完整程度隔离的应用，Hyper-V 是更好的选择。

- **选择 WSL 2**：如果你是开发者，需要在 Windows 上运行 Linux 工具或进行跨平台开发，WSL 2 是更轻量级、更高效的选择，提供了更好的开发体验。


# 数据库url："https://101.133.168.19:3306/qdam?user=qdam&password=123456"
### jsonpath: https://apifox.com/help/reference/json-path/

### GMT、UTC、DST、CST时区代表的意义
- https://www.jianshu.com/p/735e8444cdda
### linux 设置时区
- link：https://blog.csdn.net/gezilan/article/details/79422864
- sudo timedatectl set-timezone 'Asia/Shanghai'
### Railway：免费容器托管平台
### 一些部署方式
   - https://waline.js.org/guide/deploy/railway.html#%E5%A6%82%E4%BD%95%E9%83%A8%E7%BD%B2
### CRLF(\r\n) 与 LF(\n)
- crlf 是windows的换行符格式，LF是Unix的
- vscode 可以通过修改setting-设置--》用户设置--》文本编辑器--》文件--》eol--》
设置为\n 但这样只能将新建的文件换行符设置为LF 而且要注意把user/ workspace/ folder都改掉
- 这样通过插件设置，每次保存的时候会自动转变 https://www.cnblogs.com/huanhuan55/p/17684406.html
### 带内ip和带外ip
- 带内ip是指通过普通的网络连接，使用和数据传输相同的路径对设备进行管理
- 带外ip使用专门的通道，利用不同于主要的网络连接和网络设备来连接和管理设备，如使用服务器的管理端口（如IPMI、iLO、DRAC等）通过管理网络进行设备连接。
- 带外管理提供了一个备用路由，以保证管理员在主网络出现故障时仍能连接和控制关键基础设施。带内管理则是在设备运转正常时使用的一个便捷方法。

### 饿汉式加载与懒汉式加载
- 饿汉式：声明的同时直接实例化。 特点：加载类时比较慢，但运行时获取对象的速度比较快，线程安全。
- 懒汉式：声明的时候不实例化。 特点：加载类时比较快，但运行时获取对象的速度比较慢，线程不安全。
### geofile
- ip和地理定位的关联信息，不是很精准
### VMware vSphere
  - VMware vSphere 不是特定的产品或软件。VMware vSphere是整个VMware套件的商业名称。
### msys(microsoft sys)
### NFS(Network File System)
- NFS 是Network File System的缩写，即网络文件系统。一种使用于分散式文件系统的协定，由Sun公司开发，于1984年向外公布。功能是通过网络让不同的机器、不同的操作系统能够彼此分享个别的数据，让应用程序在客户端通过网络访问位于服务器磁盘中的数据，是在类Unix系统间实现磁盘文件共享的一种方法

### 通用电子元器件的选用与检测
- book name 
- 103j 103 https://zhidao.baidu.com/question/145137526.html?qbl=relate_question_0K
### 任务栏图标闪烁
- link: https://blog.csdn.net/weixin_39631261/article/details/113504221
### Shebang & Hashbang
- 在计算领域中，Shebang（也称为Hashbang）是一个由井号和叹号构成的字符序列#!，其出现在文本文件的第一行的前两个字符。 在文件中存在Shebang的情况下，类Unix操作系统的程序载入器会分析Shebang后的内容，将这些内容作为解释器指令，并调用该指令，并将载有Shebang的文件路径作为该解释器的参数
   - https://blog.csdn.net/weixin_44966641/article/details/120598561
   - 后面必须指定的是绝对路径
### 各國語言(語系)代碼表
- https://hoohoo.top/blog/national-language-code-table-zh-tw-zh-cn-en-us-json-format/
- zh-tw zh-cn

### windows锁屏路径
   - https://images.metmuseum.org/CRDImages/ep/original/DP-20613-001.jpg
   - C:\Users\jw0013109\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
   - ren * *.jpg
### ELF文件
- 可执行文件
### MIME 类型字符串
- MIME 类型，即 Multipurpose Internet Mail Extensions，称为多用途互联网邮件扩展类型，用来标识和记录文件的打开方式，一些常见的类型包括：
   - text/plain：普通文本。
   - text/html：HTML文本。
   - application/pdf：PDF文档。
   - application/msword：Word文档。
   - image/png：PNG图片。
   - mage/jpeg：JPEG图片。
   - application/x-tar：TAR文件。
   - application/x-gzip：GZIP文件。
### 为什么在终端里面或者使用urllib就下不了的东西在浏览器里就能直接下载呢？---------------no
### 线程安全
   - 意思是不需要自己加锁，就能在并行访问时保证数据完整性
### cipher suite
- 保证网络连接的算法集
### 怎么阅读代码
- 调试
   - 在想看懂的地方打断点，看调用栈
   - 如果不知道这个模块什么时候用的，就在这里打断点，看调用栈
   - 看类的关系 ClassName.__mro__
- 看代码结构，有哪些层（重写几次），方法是怎么调用的
   - 比如Uniauto有wrapper层，有实际函数层还有dispath层
### Etag和if-match
- link：
   - https://zh.m.wikipedia.org/zh-hans/HTTP_ETag
   - https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/ETag
- Etag是http协议提供的若干机制中的一种缓存验证机制。
- 客户端第一次请求url时，服务器会使用摘要算法生成一个hash值存放在响应头的Etag字段当中，当客户端修改资源或者刷新资源时，会使用Etag字段来检测资源是否被修改，或者死否需求重新请求资源。
- 当修改资源时，会if-match：Etag；包含在请求头当中，如果要修改的资源已经被别人修改了，服务器会返回412.
- 当需要刷新资源时，会把if-none-match包含在请求头当中，如果资源没被修改，服务器会返回一个极短的响应，包含HTTP304（未修改）状态码，来告诉客户端说持有的资源是最新的，应该使用它。假如资源已经被修改，服务器会返回更新后的内容
### SSO (Single Sign On)单点登录
- 用户只需一次登录就可以访问所有相互信任的应用系统
- 当用户第一次访问应用系统1的时候，因为还没有登录，会被引导到身份认证系统中进行登录；根据用户提供的登录信息，认证系统进行身份校验，如果通过校验，应该返回给用户一个认证的凭据－－ticket；用户再访问别的应用的时候就会将这个ticket带上，作为自己认证的凭据，应用系统接受到请求之后会把ticket送到认证系统进行校验，检查ticket的合法性。如果通过校验，用户就可以在不用再次登录的情况下访问应用系统2和应用系统3了。
### 宏
- 宏在编程语言中通常被定义为一种能够扩展语言语法或执行特定任务的特殊指令。然而，Python 的设计理念之一是“简洁胜于复杂”，它更倾向于通过其他方式（如装饰器、生成器等）来实现相似的功能。
### smart（Self-Monitoring,Analysis and Reporting Technology）
### ip Vip
- VIP即Virtual IP Address，是实现HA（高可用）系统的一种方案，高可用的目的是通过技术手段避免因为系统出现故障而导致停止对外服务，一般实现方式是部署备用服务器，在主服务器出现故障时接管业务。 VIP用于向客户端提供一个固定的“虚拟”访问地址，以避免后端服务器发生切换时对客户端的影响
- VIP虽然名字上叫虚拟IP，却是实打实存在的一个IP，这个IP同时绑定在负载均衡设备上和提供服务的Realserver上
- 就是多台服务器对外暴漏的一个ip
### smartctl
- link: https://www.jianshu.com/p/d5389994fad1
- smartctl是常用的磁盘检查工具
- 查看磁盘是否支持`sudo smartctl -i /dev/sda1 `
   - ```
      # 最后两行 
      SMART support is: Available - device has SMART capability.          
      SMART support is: Enabled
       ```
- 手动开启支持smartctl `smartctl --smart=on --offlineauto=on --saveauto=on /dev/sda1`
- 显示磁盘的属性值`sudo smartctl -A /dev/sdl1`
   - VALUE：这是表格中最重要的信息之一，代表给定属性的标准化值，在1到253之间。253意味着最好情况，1意味着最坏情况。取决于属性和制造商，初始化VALUE可以被设置成100或200.

### XOR (exclusive OR) 更严格的or运算
- link: https://www.ruanyifeng.com/blog/2021/01/_xor.html
- 运算规则 
   ```
   1 ^ 0 = 1
   0 ^ 0 = 0
   1 ^ 1 = 0
   ```
   - 任何值 与 0 xor 都为自身
   - 自己和自己xor 结果为0
- 妙用：一个数组包含 n-1 个成员，这些成员是 1 到 n 之间的整数，且没有重复，请找出缺少的那个数字。
### 内存地址也是需要空间的
   - 地址一般由 文件号+块号+块内偏移组成，大概10个字节
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
### CentOS 与 RedHat 关系和区别
   - https://blog.csdn.net/u013967628/article/details/79542541
   - RedHat 发行版介绍
      - Red Hat 7/8/9 普通发行版、在2003年停止了开发，它的项目有 Fedora Project 这个项目所取代，并以 Fedora Core 这个名字发行并提供普通用户免费使用
      - Red Hat Enterprise Linux （RHEL）针对企业发行的版本
   - CentOS 就是这样在 RHEL 发布的基础上克隆再现的一个 Linux 发行版本，因为Redhat的大多数软件包是基于GPL发布的，所以他必须公开自己的RedHat的源码，而其他人只要遵循GPL协议，均可以在原软件包的技术上在开发和发布，所以Centos就诞生了。
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
### 32位与# 64位 # 0x
- 内存在计算机中使用一堆箱子来表示（这也是人们在讲解它的时候的画法），这些箱子被称为 “字”。根据不同的处理器以及操作系统类型，所有的字都具有 32 位（4 字节）或 64 位（8 字节）的相同长度；所有的字都使用相关的内存地址来进行表示（以十六进制数表示）。
- 在 0xf840000040 中，0x：表示这是一个十六进制数。f840000040：这是十六进制数的主体，它占用了 48 位（12 个字符）。在64位系统中，内存地址通常是 64 位长。
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
    redsi的string是二进制安全的，是指其可以包含任何数据（任何二进制的数据吧？），如jpg图片或者序列化的对象
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
