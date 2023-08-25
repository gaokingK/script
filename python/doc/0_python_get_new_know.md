### 封装、继承、多态
- link：https://zhuanlan.zhihu.com/p/112421024
封装 , 这是定义类的 准则，单个类
    - 根据 职责 将 属性 和 方法 封装 到一个抽象的 类 中，
继承 , 这是设计类的 技巧，父与子
    - 主要体现是实现代码的 重用，相同的代码不需要重复的编写
    - 子类可以在父类功能上进行重写，扩展类的功能
多态, 不同的 子类对象调用 相同的 父类方法，产生 不同的 执行结果，可以增加代码的外部 调用灵活度
    - 多态以 继承 和 重写 父类方法 为前提
    - 多态是调用方法的技巧，不会影响到类的内部设计
### 逻辑运算符的优先级问题
- if "V6" or "V7" in self.productname
    - 会先计算or
### mmap --- 内存映射文件支持
- 打开已加载到内存中的对象
### isalnum()
- isalnum() 方法检测字符串是否由字母和数字组成。
### pprint.pformat(value)
### operator 模块
- https://www.runoob.com/python3/python-operator.html
- operator 模块提供了一套与 Python 的内置运算符对应的高效率函数。例如，operator.add(x, y) 与表达式 x+y 相同。
## counter类
- link: https://www.cnblogs.com/zhenwei66/p/6593395.html
- 计算值出现的次数, 并能做一些运算

## string 字符串的一些方法
- test_str = "she is a dog"
- endwith 以什么结尾 `test_str.endwith("dog")`

### python 函数中显示声明参数类型也不能强制转换
```
def func(b: int):
    print(b)
func("b") # 照样可以正常运行

```
### 有序字典 orderdict
- link:https://blog.csdn.net/weixin_42307036/article/details/99294242
- 普通字典的键不一定按插入的顺序；而有序字典的键是按插入的先后顺序排列的，即使修改键对应的值不能改变它的顺序
- 普通的dict的其中一个区别是 dict.popitem() 会移除最后一个键值对，并返回键值对，不能移除第一个键值对；OrderedDict的popItem()方法可以移除第一个键值对，并返回该键值对。 用法：排序字典.popitem(last=False)
- 将指定键移动到字典头或者尾部move_to_end(key, last=True)
- 可以实现O(1)复杂度的LRU缓存算法
```
# 普通字典
no_order = {}
no_order["b"] = "b"
no_order["a"] = "a"
no_order
{'a': 'a', 'b': 'b'}
# 有序字典
from collections import OrderedDict
order_dict = OrderedDict()
order_dict["b"] = "b"
order_dict["a"] = "a"
order_dict
OrderedDict([('b', 'b'), ('a', 'a')])
```
### all/any 
- link
    - https://www.jianshu.com/p/65b6b4a62071
- all()："有‘假’为False，全‘真’为True，iterable为空是True"
- any()："有‘真’为True，全‘假’为False，iterable为空是False"
- iterable为空指的是 里面的元素都是空
```
bool([[]])
True
bool([[], []])
True
all([[], []])
False
all([]) # 这种指的是iterable为空
True
```
### 字典生成式
- link: https://www.cnblogs.com/wxj1129549016/p/9515721.html
```
dict(zip('abc', [1, 2, 3]))
dic = {i:2*i for i in range(3)} # {0: 0, 1: 2, 2: 4}
```

## formate 的罕见用法
```
Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(self.request))
```

## 集合和集合的运算
- link：https://blog.csdn.net/isoleo/article/details/13000975
```
# 交集
a & b
# 并集
a | b
# 差
a - b # {1, 2} - {1, 3} 结果是2
```
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
* 的用处就是把一个列表对象变成几个对象 a=[1,2] ；*a ==（1，2）
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
- 字典unpack时默认是解包键，如果键的数量和接受值的个数不一样的话也会报错
```
a={"x": "1", "y": "2", "z": "3"}
b,c=a
Traceback (most recent call last):
  File "D:\software\PyCharm 2023.1\plugins\python\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
b,c,d = a
```
### 演示dict的items()与iteritems()的区别
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