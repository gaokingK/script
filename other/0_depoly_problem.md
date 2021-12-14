# 记录工具使用的问题
1. #### rpm(redhat package manager)
	- 原本是 Red Hat Linux 发行版专门用来管理 Linux 各项套件的程序，由于它遵循 GPL 规则且功能强大方便，因而广受欢迎。所以逐渐受到其他发行版的采用。RPM 套件管理方式的出现，让 Linux 易于安装，升级，间接提升了 Linux 的适用度
	- 如果系统的默认程序列表中不带,可以使用其他的包管理去安装
2. #### apt(Advanced Packaging Tool)
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
1. #### 安装PyQt5
    - 之前pip install PyQt5老是出错, 报错提示依赖的xxx不满足什么的,我以为是源里没有这个东西,结果看了这个链接,才发现有的包是需要依赖的
    - [基于arm64的ubuntu18.04的qt5与pyqt5环境搭建](https://blog.csdn.net/yikunbai5708/article/details/103569677)
	- 有些包是安到系统内的
	```shell
	pip install PyQt5 # 安后pip list里没有,而apt list里有
	```
2. #### pip
    - ~/.pip/pip.conf 配置文件 
	- pip --no-cache-dir disable the cache
	- rm -rf ~/.cache/pip 删除cache
	- --default-timeout=1000 或者卸载配置文件里timeout=1000
2. #### python3 多个版本安装  已有3.7 再装3.6 
	- 安装
      - 下载源码
      - 编译安装, 查看README.md
      - 多个版本共存 make altinstall
    - 问题
      - make test 时 `failed test_nntplib` 重新make clean; ./configure; make 就好了,不知为啥
      - 安装后发现python3.6不能 import ssl
      - ./configure --with-ssl 不行没有相关的参数
      - 安装openssl-dev 重新编译安装
2. #### redis安装
	 安装后reids-cli cu出现 connection refuse
	 1. systemctl status redis 
   
2. #### virtualenv
    - [看这个 virtualenv，virtualenvwrapper安装及使用 ](https://www.cnblogs.com/zixinyu/p/11308659.html)
	- [windows virtualenv 使用](https://www.cnblogs.com/cwp-bg/p/python.html)
	- [Linux下virtualenv与virtualenvwrapper详解 ](https://www.cnblogs.com/fengqiang626/p/11788200.html)
	- mkvirtualenv --help # 虽然指令中有些virtualenv关键字,但是不用写,写了会报错
    1. virtualenvwrapper 安装后要激活 `source /usr/local/bin/virtualenvwrapper.sh`
    2. 配置
    ```
   	if [ `id -u` != '0' ]; then

   	export VIRTUALENV_USE_DISTRIBUTE=1        # <-- Always use pip/distribute
   	export WORKON_HOME=$HOME/.virtualenvs       # <-- Where all virtualenvs will be stored
	# 指定virtualenv的路径 否则会报错virtualenvwrapper could not find virtualenv in your path
	export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
   	source /usr/local/bin/virtualenvwrapper.sh
   	export PIP_VIRTUALENV_BASE=$WORKON_HOME
   	export PIP_RESPECT_VIRTUALENV=true

    fi
    ```
	- -a workon env 后进入默认路径 `mkvirtualenv -a /home/huawei/Desktop/people/v2rayL test `
	- -p 指定python版本 `-p /usr/local/bin/python3.6`
	- --system-site-packages 使隔离环境能访问系统环境的python安装包 `mkvirtualenv -a /home/huawei/Desktop/people/v2rayL -p /usr/local/bin/python3.6 --system-site-packages v2rayL` # 不用加virtualenv关键字
3. #### 铜豌豆
   - https://www.atzlinux.com/allpackages.htm