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
