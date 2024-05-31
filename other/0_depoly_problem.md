# 记录工具使用、部署、运行
# 通识
- 文件编译安装在/usr/local下
# 网络问题看learn_network.md
# chrome
- 调试时禁止跳转窗口
- 选中开发者工具偏上方的Preserve log，保留跳转前的相关记录
- https://blog.csdn.net/u010071211/article/details/89390854
# 问题
- 搜索时可以完全贴上
  - `build/temp.linux-aarch64-3.6/_sodium.c:57:20: fatal error: Python.h: No such`
- cannot execute binary file 是unranr这个程序不能执行
	```
	(yolov5) [root@localhost video_check]# unrar -x 1_新建文件夹.rar
   	bash: /usr/local/bin/unrar: cannot execute binary file
    ```
- python import error /usr/lib64/libstdc++.so.6: version `CXXABI_1.3.8' not found
	- link： http://www.xiaosongit.com/index/detail/id/900.html
	-当前gcc版本的某些库缺失， 安装新版本

- [cannot find -l**** 问题的解决办法](https://blog.csdn.net/yingyujianmo/article/details/49634511)
	- 原因是没有找到库文件 libname.so;编译软件时，经常出现这样的问题
	```
	/bin/ld: cannot find -latomic
	collect2: error: ld returned 1 exit status
	make[1]: *** [redis-server] Error 1
	make[1]: Leaving directory `/home/huawei/redis-6.2.0/src'
	make: *** [all] Error 2
	```
	- /usr/bin/ld: cannot find -lgfortran 就是libgfortran.so没有找到，或者被重命名了name.so.1等
	- 解决：
	```
	# 先在系统中查找下该文件, 报错提示的库名把l换成lib
	[huawei@localhost redis-6.2.0]$ locate libatomic
	/usr/lib64/libatomic.so.1
	/usr/lib64/libatomic.so.1.2.0
	/usr/local/mysql/lib/libatomic.so.1.2.0
	# 进入so.N所在的目录中，新建一个软连接，使其链接到已有的so文件
	[huawei@localhost redis-6.2.0]$ sudo ln -s /usr/lib64/libatomic.so.1 /usr/lib64/libatomic.so
	```
# windows 下的工具
- 报错先看是不是管理员权限打开的命令行
- 环境变量在用户还是系统的path添加都行，添加完记得重启终端，如果有windows Termianal 要把这个程序重启

## windows terminal
- 向里面添加gitbash 设置以便能打开gitbash：https://zhuanlan.zhihu.com/p/418321777
- 其实很容易把 PowerShell 和 Windows Terminal 混淆，它们是两个不同的软件。可以这么理解，PowerShell 是命令行程序，真正执行指令的程序，而 Windows Terminal 则是管理各种命令行的工具。单独使用 PowerShell 就行了，为什么还要 Windows Terminal 呢？那是因为 Windows 下不仅可以安装 CMD，还可以安装 PowerShell 5.1、PowerShell 7、WSL、Azure Cloud Shell等，它需要一个工具集中管理，它就是 Windows Terminal
- 安装与美化：https://zhuanlan.zhihu.com/p/352882990
## winget
- 可以输入中文
```
PS C:\Users\Quantdo> winget install plink
找不到与输入条件匹配的程序包。
PS C:\Users\Quantdo> winget search plink
名称   ID               版本   源
--------------------------------------
pp直连 bshuzhang.PPLink 11.0.2 winget
PS C:\Users\Quantdo> winget search PPֱ�� #输入的是pp直连，按完enter后就是这样子 
名称   ID               版本   源
--------------------------------------
pp直连 bshuzhang.PPLink 11.0.2 winget
PS C:\Users\Quantdo> winget install  PPֱ��
已找到 pp直连 [bshuzhang.PPLink] 版本 11.0.2
此应用程序由其所有者授权给你。
Microsoft 对第三方程序包概不负责，也不向第三方程序包授予任何许可证。
正在下载 https://www.ppzhilian.com/download/win/pp直连 Setup 11.0.2.exe
  ██████████████████████████████   105 MB /  105 MB
已成功验证安装程序哈希
正在启动程序包安装...
已成功安装
```

# make 
## 编译安装的流程
```
make
make test
make install 
make clean # 如果出错了需要重新make时
```
## 选项
-  make install PREFIX=/usr/local/redis # 安装到指定目录

# rar
	- 没有找到arm的
	- 使用包管理工具安装
	- 使用源码安装
		```
		1. 下载
		https://www.rarlab.com/download.htm
		2. 解压缩，然后make&&make install 就好了
		```
	- 使用
		- link
			- http://linux.51yip.com/search/rar
			- https://blog.csdn.net/zyw_anquan/article/details/8672024
		```
		rar a -r test.rar /home/zhangy/test      #压缩文件夹
		rar a test test* # 压缩文件
		# 解压
		unrar  x   file.rar #
		```
# 包管理工具
- Debian/Ubuntu 使用apt
- Fedora/Centos/RHEL使用yum

### 不同系统，不同架构适配
	- arm架构的源用CentOS-AltArch，CentOS-AltArch的镜像地址为：https://repo.huaweicloud.com/centos-altarch/
	- centos6请移步至centos-vault镜像, 配置方法与centos一致.
### rpm(redhat package manager)
	- 原本是 Red Hat Linux 发行版专门用来管理 Linux 各项套件的程序，由于它遵循 GPL 规则且功能强大方便，因而广受欢迎。所以逐渐受到其他发行版的采用。RPM 套件管理方式的出现，让 Linux 易于安装，升级，间接提升了 Linux 的适用度
	- 如果系统的默认程序列表中不带,可以使用其他的包管理去安装
### apt(Advanced Packaging Tool)
    - 更换源之前需要备份源
    ```shell
	cp source.list{,.bak}
	wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-bionic.list
	```

sudo apt-get update
    - [apt 命令与 apt-get，apt-cache 等命令是什么关系？](https://www.zhihu.com/question/41087866)
      - apt命令是一条linux命令, 适用于deb包管理式的操作系统
      - apt 可以看作 apt-get 和 apt-cache 命令的子集, 可以为包管理提供必要的命令选项,apt提供了大多数与apt-get及apt-cache有的功能, 但更方便使用
      - apt集成了apt-get apt-cache的常用命令 apt install = apt-get install , apt search = apt-cache search
    - [apt-cache apt-get](https://linux.cn/article-4933-1.html)
      - apt-get和apt-cache是Ubuntu Linux中的命令行下的包管理工具

### yum & rpm
- RPM-based Linux (RedHat Enterprise Linux, CentOS, Fedora, openSUSE) yum 适用的系统
- yum provides semanage # 查询semanage 这个命令是哪个包提供的，或者查询libcrypto.so.6在那个包中，然后再安装这个包
- rpm -ql ipmitool 查看ipmitool这个安装包是否安装（可以看出ipmitool未安装）
- rpm -qa ipmitool 检测ipmitool是否安装成功
- 更换源
    ```
	# 备份配置文件：
	cp -a /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
	# 下载新的CentOS-Base.repo文件到/etc/yum.repos.d/目录下
	wget -O /etc/yum.repos.d/CentOS-Base.repo https://repo.huaweicloud.com/repository/conf/CentOS-8-reg.repo
	# 清除原有yum缓存。
	yum clean all
	# 执行yum makecache（刷新缓存）或者yum repolist all（查看所有配置可以使用的文件，会自动刷新缓存）。
	```
- yum groupinstall 它安装一个安装包，这个安装包包涵了很多单个软件，以及单个软件的依赖关系。
- yum install 它安装单个软件，以及这个软件的依赖关系
### 问题
- 问题一
    ```
	[root@localhost huawei]# yum install python-dev --nogpgcheck
	Loaded plugins: fastestmirror, langpacks, product-id, search-disabled-repos, subscription-manager
	This system is not registered with an entitlement server. You can use subscription-manager to register.
	重新换了一个源
	```
- 问题
    ```
	[root@localhost huawei]# yum install python-devel
	Loaded plugins: fastestmirror, langpacks, product-id, search-disabled-repos, subscription-manager

	This system is not registered with an entitlement server. You can use subscription-manager to register.

	Loading mirror speeds from cached hostfile
	https://repo.huaweicloud.com/centos/7/os/aarch64/repodata/repomd.xml: [Errno 14] HTTPS Error 404 - Not Found
	# 先wget -O /tmp/a.xml https://xxxxx 试一下能不能wget， 然后在浏览器里试一下
	```
- 问题
	```
	curl#6 - “Could not resolve host: mirror.lzu.edu.cn； Unknown error“ 及telnet安装
	同上 先试下网络通不通ping mirror.lzu.edu.cn
	- 尝试使用root用户来yum， 141就是普通用户会出错
	```
# nginx
- nginx: [emerg] bind() to 127.0.0.1:31302 failed (13: Permission denied)
	- link: https://blog.csdn.net/RunSnail2018/article/details/81185138
	- 解决：
		- 1024以下端口启动时需要root权限, sudo nginx即可。
		- 端口大于1024
			- semanage port -l | grep http_port_t # 查看http允许访问的端口
			- semanage port -a -t http_port_t  -p tcp 8090 # 将要启动的端口加入到如上端口列表中
	- 另一种方式https://blog.csdn.net/qq_32448349/article/details/109725173
- nginx: [emerg] bind() to 127.0.0.1:31302 failed (98: Address already in use)
	- link： https://blog.csdn.net/weixin_38450689/article/details/75142404
	- 解决：
		- netstat -tunlp # 查看端口占用情况
			- 发现是nginx 占用 就pkill nginx
			- 或者fuser -k 80/tcp
		- 重新启动nginx
# 安装PyQt5
    - 之前pip install PyQt5老是出错, 报错提示依赖的xxx不满足什么的,我以为是源里没有这个东西,结果看了这个链接,才发现有的包是需要依赖的
    - [基于arm64的ubuntu18.04的qt5与pyqt5环境搭建](https://blog.csdn.net/yikunbai5708/article/details/103569677)
	- 有些包是安到系统内的
	```shell
	pip install PyQt5 # 安后pip list里没有,而apt list里有
	```
# wheel包命名规范
- link
    - [python之wheel 包命名规则、abi 兼容和安装](https://www.cnblogs.com/skiler/p/6866069.html)
	- [查看abi、pep425tags](https://blog.csdn.net/happywlg123/article/details/107281936)
- wheel 包的命名格式为 `{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl`
- 如何判断给定 wheel 包是否能够安装？
  - 通常判断依赖的时候，需要看下是否符合最低版本。不过 pip 判断给定 wheel 包的 abi 兼容的做法与此有些许差异。pip 的做法是，计算出一个支持的 abi tag 集合，然后判断目标 abi tag 是否在这个集合里。这个计算过程跟在打包时是一样的。这意味着，打包拓展的 CPython 需要跟安装的机器上的 CPython 版本是一致的，否则就装不了。对于“永远的2.7”来说，这不是什么问题；不过如果用的是 Python 3，又不能控制具体的 CPython 版本，对于 C 拓展还是现场编译安装比较靠谱。
  - 如何查看abi呢？
  ```cs
  # 最靠谱的方法：
  搜索pep425tags.py的位置，然后导入（这个环境是装的ancoada
  (yolov5) [root@localhost test]# find / -name "pep425tags.py" 2>/dev/null
  /root/archiconda3/lib/python3.7/site-packages/wheel/pep425tags.py
  /usr/lib/python3.6/site-packages/pip/pep425tags.py
  /usr/lib/python3.6/site-packages/setuptools/pep425tags.py
  >>> from wheel import pep425tags as a
  >>> print(a.get_supported())
  # 方法一 32位
  from pip import pep425tags
  print(pep425tags.get_supported())
  # 方法二 64位
  >>> import pip._internal.pep425tags
  >>> print(pip._internal.pep425tags.get_supported())
  ``` 
- `manylinux1`
  - manylinux1 wheels are built on a baseline linux environment based on Centos 5.11 and should work on most x86 and x86_64 glibc based linux environments.
# pip
	-u 如果以安装就升级到最新版
	- pip 离线安装 whl
		- 下的慢的话可以直接在浏览器里下载
		- `pip install /path/to/xxx.whl`
	- pip 配置文件位置
    	- linux： ~/.pip/pip.conf 配置文件 
		- windows : 如果两个都存在，会优先使用appdata下面的
			- C:\Users\Quantdo\pip
			- C:\Users\Quantdo\AppData\Roaming\pip\pip.ini
		- https://blog.csdn.net/weixin_50679163/article/details/122392249
	- pip --no-cache-dir disable the cache
	- rm -rf ~/.cache/pip 删除cache
	- --default-timeout=1000 或者卸载配置文件里timeout=1000
	- -f url： fetch： 增加一个源， 但不替换原来的源（如下） 
	- 某些版本找不到可能时因为没有对应架构的包，并不是没有版本
		```cs
		(yolov5) [root@localhost ~]# pip3 install 'torch==1.10.1+cpu' -f https://download.pytorch.org/whl/cpu/torch_stable.html --trusted-host=download.pytorch.org
		Looking in indexes: https://repo.huaweicloud.com/repository/pypi/simple
		Looking in links: https://download.pytorch.org/whl/cpu/torch_stable.html
		ERROR: Could not find a version that satisfies the requirement torch==1.10.1+cpu (from versions: 1.8.0, 1.8.1, 1.9.0, 1.10.0, 1.10.1)
		是因为1.10.1没有arm64的包
		```
	- pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='127.0.0.1', port=10809): Read timed out.
		- 重新运行pip install 命令解决
	- ssl 问题 
		- 可以尝试--trusted-host: `pip install lightgbm -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
		- 也可以尝试更换版本，我pip不行，pip3就好了
	- urllib3.exceptions.ProxyError: ('Unable to connect to proxy', SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1125)')))
		- urllib3 版本问题 安装pip install urllib3==1.25.11 这个版本试试
		- link：https://zhuanlan.zhihu.com/p/350015032
		- 原因是以前 urllib3 其实并不支持 https 代理，也就是说代理服务器的地址虽然大家配置的是 https，但是一直都是悄无声息地就按照 http 连接的，刚好代理服务器确实也只支持 http，所以皆大欢喜。现在 urllib3 要支持 https 代理了，那么既然配置代理是 https 就尝试用 https 的方式去连接，但是由于代理服务器其实只支持 http，所以没法处理请求，ssl 握手阶段就出错了。注意，这里的 https 是指代理服务器自己的，和我们要访问的目标网站无关。
    - pip 编译安装失败： xxx.h 缺失
        ```
		  build/temp.linux-aarch64-3.6/_sodium.c:57:20: fatal error: Python.h: No such file or directory
		   #include <Python.h>
		                      ^
		  compilation terminated.
		  error: command 'gcc' failed with exit status 1
		  ----------------------------------------
		  ERROR: Failed building wheel for pynacl
		Failed to build pynacl
		ERROR: Could not build wheels for pynacl, which is required to install pyproject.toml-based projects
		# 没有安装python-dev的头文件和静态库
		# 可以通过搜索这个东西来用那个python版本 sudo find / -name "Python.h" 2>/dev/null
		# 或者来安装python-dev
		sudo apt-get install python-dev   # for python2.x installs
		sudo apt-get install python3-dev  # for python3.x installs
		# 如果还是不行
		sudo apt-get install python3.6-dev # 不一定可以
		```
# python3 多个版本安装  已有3.7 再装3.6 
	- 安装
      - 下载源码
      - 编译安装, 查看README.md
      - 多个版本共存 make altinstall
    - 问题
      - make test 时 `failed test_nntplib` 重新make clean; ./configure; make 就好了,不知为啥
      - 安装后发现python3.6不能 import ssl
      - ./configure --with-ssl 不行没有相关的参数
      - 安装openssl-dev 重新编译安装
    - 依赖安装，主要分为：pip安装包时编译需要的依赖， 缺失依赖会造成xxx.h not found；另一种是依赖库缺失
      - link
        - python-dev: https://blog.csdn.net/weixin_33757911/article/details/93028630
        - 安装依赖库：https://blog.csdn.net/qq_27825451/article/details/100034135
      - 根据python版本选择python-dev安装
        - python-dev的包在centos的yum中不叫python-dev，而是python-devel.
        - 有多个版本的话， 为什么只安装了2.7的python-dev
            - python3 安装使用`yum install python3-devel`
## python vscode配置
- 安装python environment就可以使用虚拟环境了
## python 运行问题
- 只有远程执行python 脚本时才会报错：ImportError: DLL load failed: %1 不是有效的 Win32 应用程序。
    - 前提：win ssh 到 centos， 又连接到win， 执行命令 python Record_back_1204_001_可用版本.py
        ```
        Traceback (most recent call last):
          File "Record_back_1204_001_可用版本.py", line 6, in <module>
            from PyQt5.QtWidgets import QWidget, QApplication
        ImportError: DLL load failed: %1 不是有效的 Win32 应用程序。
        ```
        在交互环境中，导入也会报错，应该是导入包的原因； 另外在本地执行却没有问题。（这个python的tags、msc都是一样的）
    - 没有找到为什么环境相同，却还会出错
    - 解决：换了一个32位的python解释器运行就没错了
        ```
        # 出错的python环境版本
        Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
        # 好的 msc确实是32位的
        administrator@PCMICRO-BOAGF4U C:\Users\Administrator\Desktop\视频采集卡相关信息\record_542N2>C:\python_env\p3_32\Scripts\python.exe
        Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> from PyQt5.QtWidgets import QWidget, QApplication
        >>> exit()
      ```
- centos7 Python3终端中敲击方向键显示「^[[C^[[D」
	- link：https://www.linuxidc.com/Linux/2015-02/112891.htm
	- 查找得知，是由于系统缺少了readline相关模块。CentOS 5.8默认只安装了readline模块而没有安装readline-devel模块，所以只要安装下，然后重新编译

- Windows: TclError: Can't find a usable init.tcl in the following directories:
	- link:https://stackoverflow.com/questions/29320039/python-tkinter-throwing-tcl-error
	- 解决方法：
		- where python # 找到python路径
		- 复制D:\softwares\Python27\tcl 到D:\softwares\Python27\Lib  （好像只复制tk8.5）也可以
		- 然后重启pycharm
# redis安装和运行
- redhat 可以通过apt安装
```
$ curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
$ echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
$ sudo apt-get update
$ sudo apt-get install redis
```
- centos 安装，从源码安装[link](https://www.cnblogs.com/heqiuyong/p/10463334.html)
```
# 下载源码包 解压
$ wget https://download.redis.io/releases/redis-6.2.6.tar.gz
$ tar xzf redis-6.2.6.tar.gz
# cd切换到redis解压目录下，执行编译
$ cd redis-6.2.6
$ make # 会生成一个src文件夹可执行文件就在这里
# 此时可以验证是否安装好，./src/redis-server 
# 安装并指定安装目录
$ sudo make install PREFIX=/usr/local/redis
# 后台启动 启动时要在后面带上redis.conf
# 从 redis 的源码目录中复制 redis.conf 到 redis 的安装目录
sudo cp /usr/local/redis-5.0.3/redis.conf /usr/local/redis/bin/
# 修改 redis.conf 文件，把 daemonize no 改为 daemonize yes
# 后台启动 ./usr/local/redis/bin/redis-server redis.conf

# 设置开机启动 
# 添加开机启动服务 里面的ExecStart配置成自己的路径 
vi /etc/systemd/system/redis.service # 没有就新建
[Unit]
Description=redis-server
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/bin/redis.conf
PrivateTmp=true

[Install]
WantedBy=multi-user.target
# 设置开机启动
[root@localhost bin]# systemctl daemon-reload
[root@localhost bin]# systemctl start redis.service
[root@localhost bin]# systemctl enable redis.service
# 创建 redis 命令软链接
 ln -s /usr/local/redis/bin/redis-cli /usr/bin/redis
```
## redis 问题
- 安装后$reids-cli 出现 connection refuse
    - systemctl status redis 
- 编译时出现cannot find -l***问题 见上
- ./redis-server 时告警[link](https://joy-panda.blog.csdn.net/article/details/52006376)
  - 如果告警不解决就不会起来
  - 可以在redis.conf 中取消注释 ignore-warnings ARM64-COW-BUG 
  - 可以解决一些告警，但update kernel 不能解决，所以还是直接注释吧

# rabbitmq 安装
- link：
  - https://www.rabbitmq.com/install-rpm.html

# virtualenv
- ## link：
    - [看这个 virtualenv，virtualenvwrapper安装及使用 ](https://www.cnblogs.com/zixinyu/p/11308659.html)
	- [windows virtualenv 使用](https://www.cnblogs.com/cwp-bg/p/python.html)
	- [Linux下virtualenv与virtualenvwrapper详解 ](https://www.cnblogs.com/fengqiang626/p/11788200.html)
	- mkvirtualenv --help # 虽然指令中有些virtualenv关键字,但是不用写,写了会报错
- ## 问题
	- win 安装后运行./activate 提升因为在此系统上禁止运行脚本
		- https://www.jianshu.com/p/4eaad2163567
		- 使用管理员打开powershell 输入`set-executionpolicy remotesigned`
	- 使用workon project 没有反应，因为默认终端时powershell，好像哪里有问题，切换到cmd
	- 安装后创建环境时virtualenvwrapper could not find /home/huawei in your path
		- 环境变量里没有virtualenvwrapper
		```
		# 找到virtualenvwrapper路径，然后把这个路径加到path里
		sudo find /  -name "vituralenvwrapper" 2>/dev/null
		export VIRTUALENVWRAPPER_VIRTUALENV=/path/to/virtualenv
		```
	- source virtualenvwrapper.sh 时报错
    	- https://blog.csdn.net/weixin_44331765/article/details/107314708
		```
		[huawei@localhost root]$ source /home/huawei/.local/bin/virtualenvwrapper.sh 
		/bin/python: No module named virtualenvwrapper virtualenvwrapper.sh: There was a problem running the initialization hooks.
		If Python could not import the module virtualenvwrapper.hook_loader, check that virtualenvwrapper has been installed for VIRTUALENVWRAPPER_PYTHON=/bin/python and that PATH is set properly.
		# 需要把python改为python3的路径, 就好了
		export VIRTUALENVWRAPPER_PYTHON=/bin/python3
		```
- ##  安装（确保 virtualenv 已经安装了）：
	- 对于Windows，您可以使用 virtualenvwrapper-win 。 `pip install virtualenvwrapper-win`
	- 在Windows中，WORKON_HOME默认的路径是 %USERPROFILE%\Envs 。
- ## 配置
	- virtualenvwrapper 安装后要激活 `source /usr/local/bin/virtualenvwrapper.sh`
	```
	if [ `id -u` != '0' ]; then

	export VIRTUALENV_USE_DISTRIBUTE=1        # <-- Always use pip/distribute
	export WORKON_HOME=$HOME/.virtualenvs       # <-- Where all virtualenvs will be stored
	# 指定virtualenv的路径 否则会报错virtualenvwrapper could not find virtualenv in your path
	export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv # 这个路径时 不确定的
	source /usr/local/bin/virtualenvwrapper.sh
	export PIP_VIRTUALENV_BASE=$WORKON_HOME
	export PIP_RESPECT_VIRTUALENV=true
	fi
	```
	- -a workon env 后进入默认路径 `mkvirtualenv -a /home/huawei/Desktop/people/v2rayL test `
	- -p 指定python版本 `-p /usr/local/bin/python3.6`
	- --system-site-packages 使隔离环境能访问系统环境的python安装包 `mkvirtualenv -a /home/huawei/Desktop/people/v2rayL -p /usr/local/bin/python3.6 --system-site-packages v2rayL` # 不用加virtualenv关键字

- ## 基本使用
	- 创建一个虚拟环境：`$ mkvirtualenv [-p python_verison_path] my_project` 这会在 ~/Envs 中创建 my_project 文件夹。
	- 在虚拟环境上工作：`$ workon my_project`
	- 或者，您可以创建一个项目，它会创建虚拟环境，并在 $WORKON_HOME 中创建一个项目目录。 当您使用 workon myproject 时，会 cd 到项目目录中。`$ mkproject myproject`
	- virtualenvwrapper 提供环境名字的tab补全功能。当您有很多环境， 并且很难记住它们的名字时，这就显得很有用。workon 也能停止您当前所在的环境，所以您可以在环境之间快速的切换。
	- 停止是一样的：`$ deactivate`
	- 删除：`$ rmvirtualenv my_project`
- ## 其他有用的命令
	- `lsvirtualenv` 列举所有的环境。
	- `cdvirtualenv` 导航到当前激活的虚拟环境的目录中，比如说这样您就能够浏览它的 site-packages 。
	- `cdsitepackages` 和上面的类似，但是是直接进入到 site-packages 目录中。
	- `lssitepackages` 显示 site-packages 目录中的内容。
	- `virtualenvwrapper` 命令的完全列表 。
	- `cpvirtualenv oldenv newenv; rmvirtualenv oldenv` 重命名虚拟空间

### 铜豌豆
   - https://www.atzlinux.com/allpackages.htm
