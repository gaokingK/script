# 记录工具使用的问题
1. #### [centos redis install](https://www.cnblogs.com/autohome7390/p/6433956.html)
1. #### [v2ray ](https://qv2ray.net/getting-started/step1.html#linux-debian-ubuntu-and-their-derivatives)
1. #### redis安装
	 安装后reids-cli cu出现 connection refuse
	 1. systemctl status redis 
   
2. #### [windows virtualenv 使用](https://www.cnblogs.com/cwp-bg/p/python.html)
3. #### virtualenvwrapper 安装后要激活 `source /usr/local/bin/virtualenvwrapper.sh`
- 配置
```
if [ `id -u` != '0' ]; then

	export VIRTUALENV_USE_DISTRIBUTE=1        # <-- Always use pip/distribute
	export WORKON_HOME=$HOME/.virtualenvs       # <-- Where all virtualenvs will be stored
	source /usr/local/bin/virtualenvwrapper.sh
	export PIP_VIRTUALENV_BASE=$WORKON_HOME
	export PIP_RESPECT_VIRTUALENV=true

fi

```
# python
### pip 安装三方包时缺少visual c++ 
```
error: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27
```
- link:
  - https://www.jianshu.com/p/fbe87630617d
- 原因
  - Windows平台则通过下载编译好的Python安装使用，本地不一定具备C/C++编译环境。
  - 使用pip给python添加扩展/模块时，如果扩展/模块中包含有C/C++源码，安装脚本将试图寻找与编译生成Python的同版本编译器来编译生成该模块
- 解决办法
  - [下载 VCForPython27.msi](https://www.jb51.net/softs/600576.html#downintro2) 
  - 安装后问题解决

### pip install xxx ssl error问题 或者失去响应卡死一段时间
```
SSLError('_ssl.c:711: The handshake operation timed out'
```
- 未解决

### cmd中输入 python 进入微软商店
- link: https://blog.csdn.net/qq_34679675/article/details/107513409

### windows 下安装多个python版本
- link：
  - https://www.cnblogs.com/yinzhengjie/p/9106558.html
  - https://www.code05.com/question/detail/4750806.html
- 然后把python3的安装路径里为python.exe创建一个名为python3.exe的副本, 这样就能解决运行pip时报unable to create process 的error
- #### 如何区分不同的pip
  - pip2 install xxx && pip3 install xxx

### windows 下安装python后重命名了文件夹，cmd 运行pip报错fatal to launcher xxxx
```
C:\Users\jw0013109>pip
Fatal error in launcher: Unable to create process using '"d:\softwares\python 2.7.18_64\python.exe"  "D:\softwares\Python27\Scripts\pip.exe"
# d:\softwares\python 2.7.18_64\python.exe 这个路径不存在了，被重命名了
```
- link：
  - https://stackoverflow.com/questions/45517049/fatal-error-in-launcher-unable-to-create-process-using-in-python
  - https://bugs.python.org/issue6792
- 解决方法：`pythonx -m pip`
  - 可以使用mylink来创建符号链接来恢复被修改的路径
  - 我重装了
- 原因：
  - 这些东西好像是在注册表中存放的`HKEY_LOCAL_MACHINE\SOFTWARE\Python\PythonCore`
  - 是使用mkvirtualenv -p2.7 test2 的报错发现的
  ```
  PS C:\Users\jw0013109\Desktop\people> mkvirtualenv -p2 test2
   C:\Users\jw0013109\Envs is not a directory, creating
  PEP-514 violation in Windows Registry at HKEY_CURRENT_USER/PythonCore/3.8 error: could not load exe with value C:\Users\jw0013109\AppData\Local\Programs\Python\Python38\python.exe
  PEP-514 violation in Windows Registry at HKEY_LOCAL_MACHINE/PythonCore/2.7 error: could not load exe with value D:\softwares\Python 2.7.18_64\python.exe
  created virtual environment CPython2.7.18.final.0-64 in 4370ms
    creator CPython2Windows(dest=C:\Users\jw0013109\Envs\test2, clear=False, no_vcs_ignore=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\jw0013109\AppData\Local\pypa\virtualenv)
      added seed packages: pip==20.3.4, setuptools==44.1.1, wheel==0.37.1
    activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

  ```
