# 记录工具使用、部署、运行
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
# linux 更改用户名密码、新增用户
	- 新增用户`useradd name option`
	- 更改密码`passwd username`
# rpm(redhat package manager)
	- 原本是 Red Hat Linux 发行版专门用来管理 Linux 各项套件的程序，由于它遵循 GPL 规则且功能强大方便，因而广受欢迎。所以逐渐受到其他发行版的采用。RPM 套件管理方式的出现，让 Linux 易于安装，升级，间接提升了 Linux 的适用度
	- 如果系统的默认程序列表中不带,可以使用其他的包管理去安装
# apt(Advanced Packaging Tool)
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

# yum 
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
- 不同系统，不同架构适配
	- arm架构的源用CentOS-AltArch，CentOS-AltArch的镜像地址为：https://repo.huaweicloud.com/centos-altarch/
	- centos6请移步至centos-vault镜像, 配置方法与centos一致.
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
- 问题一
	```
	curl#6 - “Could not resolve host: mirror.lzu.edu.cn； Unknown error“ 及telnet安装
	同上 先试下网络通不通ping mirror.lzu.edu.cn
	- 尝试使用root用户来yum， 141就是普通用户会出错
	```
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
  ```
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
	- pip 离线安装 whl
		- 下的慢的话可以直接在浏览器里下载
		- `pip install /path/to/xxx.whl`
    - ~/.pip/pip.conf 配置文件 
	- pip --no-cache-dir disable the cache
	- rm -rf ~/.cache/pip 删除cache
	- --default-timeout=1000 或者卸载配置文件里timeout=1000
	- -f url： fetch： 增加一个源， 但不替换原来的源（如下） 
	- 某些版本找不到可能时因为没有对应架构的包，并不是没有版本
		```
		(yolov5) [root@localhost ~]# pip3 install 'torch==1.10.1+cpu' -f https://download.pytorch.org/whl/cpu/torch_stable.html --trusted-host=download.pytorch.org
		Looking in indexes: https://repo.huaweicloud.com/repository/pypi/simple
		Looking in links: https://download.pytorch.org/whl/cpu/torch_stable.html
		ERROR: Could not find a version that satisfies the requirement torch==1.10.1+cpu (from versions: 1.8.0, 1.8.1, 1.9.0, 1.10.0, 1.10.1)
		是因为1.10.1没有arm64的包
		```
	- ssl 问题 
		- 可以尝试--trusted-host: `pip install lightgbm -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
		- 也可以尝试更换版本，我pip不行，pip3就好了
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
# redis安装
	 安装后reids-cli cu出现 connection refuse
	 1. systemctl status redis 
   
# virtualenv
- ## link：
    - [看这个 virtualenv，virtualenvwrapper安装及使用 ](https://www.cnblogs.com/zixinyu/p/11308659.html)
	- [windows virtualenv 使用](https://www.cnblogs.com/cwp-bg/p/python.html)
	- [Linux下virtualenv与virtualenvwrapper详解 ](https://www.cnblogs.com/fengqiang626/p/11788200.html)
	- mkvirtualenv --help # 虽然指令中有些virtualenv关键字,但是不用写,写了会报错
- ## 问题
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

1. #### 铜豌豆
   - https://www.atzlinux.com/allpackages.htm