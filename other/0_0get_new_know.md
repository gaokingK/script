# other
### VMware vSphere
  - VMware vSphere 不是特定的产品或软件。VMware vSphere是整个VMware套件的商业名称。
### msys(microsoft sys)
### NFS(Network File System)
- NFS 是Network File System的缩写，即网络文件系统。一种使用于分散式文件系统的协定，由Sun公司开发，于1984年向外公布。功能是通过网络让不同的机器、不同的操作系统能够彼此分享个别的数据，让应用程序在客户端通过网络访问位于服务器磁盘中的数据，是在类Unix系统间实现磁盘文件共享的一种方法


# windows
### 注册表编辑器好像是全字匹配的
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

# Python 
### from openpyxl import load_workbook 处理excle表格
### if 类的某个实例会调用哪个方法
- https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html
- cmp时所有比较魔术方法的基类方法？
- 如果使用比较符时，会根据比较符来选择各自的魔术方法
    - __eq__(self, other)	定义相等运算符的行为	==
    - __ne__(self, other)	定义不等式运算符的行为	!=
    - __lt__(self, other)	 定义小于运算符的行为	<
    - __le__(self, other)	定义小于或等于运算符的行为	<=
    - __gt__(self, other)	定义大于运算符的行为	>
    - __ge__(self, other)	定义大于或等于运算符的行为	>=
- 如果不使用比较符，会使用__bool__；该方法需要一个返回值
### python3 input 与python2 input的区别
- link：https://www.runoob.com/python/python-func-input.html
- python3 的input等价于python2的raw_input
- python2 中的input相当于eval(raw_input())
### eval 与 exec
- link：http://c.biancheng.net/view/5683.html
- eval() 和 exec() 函数的功能是相似的，都可以执行一个字符串形式的 Python 代码（代码以字符串的形式提供），相当于一个 Python 的解释器。二者不同之处在于，eval() 执行完要返回结果，而 exec() 执行完不返回结果（文章后续会给出详细示例）。
### os.path.join()
- link: https://vimsky.com/zh-tw/examples/usage/python-os-path-join-method.html
- 如果'c:'和‘/path'都可以代表绝对路径部分。那麽將放棄所有先前連接的組件，並且從絕對路徑組件繼續進行連接
```
os.path.join("/path1", "/path2") # 结果是/path2 C://同理
```
### os.path.abspath 与 os.path.realpath
- link： https://blog.csdn.net/rainshine1190/article/details/85165059
- 前者返回一个目录的绝对路径。后者返回文件的标准路径，而不是软连接所在的路径
```
>>> os.path.abspath("python_modu")
'/root/python_modu'
>>> os.path.realpath("/usr/bin/python")
'/usr/bin/python2.7'
```
### windows 查看生成Python的编译器及版本信息
- link：https://www.jianshu.com/p/fbe87630617d
### 如果两个人使用的解释器一样的话，可以通过复制site—packages来把自己的包给别人
### 模块搜索路径和包导入
- link: https://www.cnblogs.com/ljhdo/p/10674242.html
- xxx.pth的作用 里面每一行都是一个目录的路径， 会在这个路径中搜索所需要的包，其作用和添加到Path中是相同的
- 把这个文件可以放在python安装的目录当中，也可以放在其下的lib/site-packages当中（如果是虚拟环境，也可以这样做）
- 但是这样做在pycharm中会带来一个新问题，如果两个attch 一个窗口的项目使用的是一个解释器的时候， 会让两个项目的目录结构在显示上不正常（真实的是正常的），解决办法就是使用不同的解释器。
### 接受输入
```
# ctrl + D 触发EOF
while True:
    a = input("ss")
    print(a)
    if a == "":
        break
a, b = input() # 就只能输入两个字符
a = sys.stdin.readline() 会将标准输入全部获取，包括末尾的'\n'，input()会把‘\n’忽略. 他们一遇到回车就结束了
sys.stdin.readlines() 能接受多行 按ctrl + D结束
```
### 解包*
```
# 第一种用处：用在定义时，表示定义的可变参数
def check(*args):
    if len(args) != 3:
        return False

a = [1, 2, 3]
check(a)
# print(args) ([1, 2, 3],)
# print(*args) [1, 2, 3]
# type(args) <class 'tuple'>
# type(*args) <class 'list'> # 只能把元组搞成列表
a, b, c = [1, 2, 3]
check(a, b, c)
# print(args) (1, 2, 3)
# print(*args) 1 2 3
# type(args) <class 'tuple'>
# type(*args) 报错 
check(*d)和check(a, b, c)是一样的
check(a=1, b=2, c=3) # 报错
# 第二种用处，用在调用时，对容器类型的参数加*是因为函数定义时是有多个参数
def check(a, b, c):
  pass
```
# linux
### 文档
  - https://www.thegeekstuff.com/2008/08/15-examples-to-master-linux-command-line-history/
### jq linux json处理器
  - https://wangchujiang.com/linux-command/c/jq.html
### ctrl + R 搜索历史命令
- 输入一些东西后再按ctrl + R继续搜索  
### command
- sh -c ps -Awwo nice,pid,ppid,comm,args|grep snmptrapd; kill -9 pid
- 查看端口使用lsof -i:27501
### 免密
```
本地客户端生成公私钥：（一路回车默认即可） ssh-keygen
上传公钥到要免密登录的服务器（这里需要输入密码）ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.235.22 
上面这条命令是写到服务器上的ssh目录下去了vim root/.ssh/authorized_keys可以看到客户端写入到服务器的 id_rsa.pub （公钥）内容。
客户端通过ssh连接远程服务器，就可以免密登录了。ssh root@192.168.235.22
```
### 关闭服务关不掉时先kill掉进程再service fuwuming stop
### diff A B
- link：
  - https://www.runoob.com/linux/linux-comm-diff.html
- diff log2014.log log2013.log  -y -W 50 并排格式输出
- diff A B 的结果
``` 
diff A B
> 表示此行B不为空，A是空行；< 表示此行A不为空，B是空行；| 表示此行A、B均不为空 
">"也可以理解为表示后面文件比前面文件多了1行内容
install:/etc/syslog-ng # diff syslog-ng.conf syslog-ng.conf.bakjjw
255,258c255,256 # 是不同的位置，c前面的是文件A的，后面的是B
# -- 上面的是文件A，下面的是文件B的
<             key-file("/etc/syslog-ng/key.d/Sever_Syslog.pem")
<             cert-file("/etc/syslog-ng/cert.d/Sever_Syslog.crt")
<             # key-file("/etc/syslog-ng/key.d/Server_syslog.key")
<             # cert-file("/etc/syslog-ng/cert.d/Server_syslog.crt")
---
>             key-file("/etc/syslog-ng/key.d/Server_syslog.key")
>             cert-file("/etc/syslog-ng/cert.d/Server_syslog.crt")
11,12d10 # 表示第一个文件比第二个文件多了第11和12行
< 2013-11
< 2013-12
```
- diff A B  -u 统一格式输出
```
它的第一部分，也是文件的基本信息：
--- A 2012-12-07 18:01:54.000000000 +0800
+++ B 2012-12-07 16:36:26.000000000 +0800
"---"表示变动前的文件，"+++"表示变动后的文件。
第二部分，变动的位置用两个@作为起首和结束。
　　 @@ -1,12 +1,10 @@
前面的"-1,12"分成三个部分：减号表示第一个文件（即A），"1"表示第1行，"12"表示连续12行。合在一起，就表示下面是第一个文件从第1行开始的连续12行。同样的，"+1,10"表示变动后，成为第二个文件从第1行开始的连续10行。
```
#### 执行系统命令
- tab 激活目录补全，左右键移动，上下键进入，enter执行命令
# Git
### client_global_hostkeys_private_confirm: server gave bad signature for RSA key 0: error in libcrypto
- link: https://stackoverflow.com/questions/67401049/pulling-from-git-fails-and-gives-me-following-error-client-global-hostkeys-priv
- 原因：
  - 是某些ssh版本的issue
  - 不影响
- 解决：
  - 未解决
  - 按照link上操作没有生效，可能是config这个文件的扩展名没有用

### Filename too long in Git for Windows
- link: https://stackoverflow.com/questions/22575662/filename-too-long-in-git-for-windows
- 解决：
  - git config --system core.longpaths true
- - 原因：
  - git 版本使用的是windows的老版本API，对字符长度的限制是260个

# todo
- 演示dict的items()与iteritems()的区别
从演示结果可以看出iteritems()对于大的dict性能方面是有很大的提升的
拥有10**4个item的dict就应该使用iteritems()，而不是items()。
同理对keys()、iterkeys()、values()、itervalues()也是适用的
### 私有属性
- `A.__private_property`可以用_ + A的基类名 + __ + private_property 访问到
- A 的父类为 B B的父类为C...... E的父类为object 那么A的基类就是E 如果有多个父类呢，那就按类的继承规则吧
- pycharm中ctrl+F12看到的方法中包括父类的
### 导入带路径带数字的的 server/100_HW/212_STRESS/EccCheck.py
```
在其他模块导入时，因为脚本路径含有数字开头的名称，无法直接import导入，所以，临时将本模块的所在目录加入系统路径
在其他模块导入时，请在文件开头添加以下代码：
import os
import re
import sys

file_path = os.path.realpath(__file__)
pattern = re.compile(r"(.*100_HW)")
ecc_path = os.path.join(pattern.match(file_path).group(), '201_STABILITY')
sys.path.append(ecc_path)

from EccCheck import EccCheck
以上路径仅适用于100_HW路径下的脚本，其他路径请自行修改
```
### 重载和重写
```
# 概念
https://blog.csdn.net/weixin_44806193/article/details/122161051
重载是在一个类中，方法名相同，参数不同，重写是子类与父类之间的；重载的参数个数、参数类型、参数的顺序可以不同，重写父类子方法参数必须相同；
class DeviceBase(object):
    """设备基类"""
    __init__中self.setupEnableComponents()
    
    def setupEnableComponents(self):
        """初始化设备允许创建的业务列表,由子类继承实现"""
        pass
    def addType():
        code
class Server(ServerBase, Dispatcher): # ServerBase继承于DeviceBase
    __init__ 中  super(Server, self).__init__()

    """智能计算服务器产品抽象，抽象整个服务器的操作，用例中先找到服务器对象，再对该对象进行操作  提供统一存储设备对象的封装"""
    def setupEnableComponents(self):
        for component, com_path in COMPONENTS:
            self.addType(component, com_path) # 调用的DeviceBase中的addType
       
初始化设备允许创建的业务列表,由子类继承实现
```
### 传递实例
```
Class A:
    @classmethod
    def sync(cls, device, criteria, force): 
        pass 
Class DeviceBase:
    self.classDict[fullName.lower()].sync(self, criteria, forceSync)
加入是DeviceBase的子类调用这个方法，self是子类
```