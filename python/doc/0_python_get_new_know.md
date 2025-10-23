### doc
- https://fasionchan.com/python-source/memory/refcnt-drawback/
- https://ebook-python-study.readthedocs.io/zh-cn/latest/python%E8%BF%9B%E9%98%B618%E5%9E%83%E5%9C%BE%E5%9B%9E%E6%94%B6GC.html

{"level":"error","ts":1737449894.9944735,"caller":"git/git.go:54","msg":"Error running git [fetch --recurse-submodules=yes --depth=1 origin --update-head-ok --force 22211589f8a68cc3fad0b556078fb10e2d5b95ce]: exit status 128\nerror: Server does not allow request for unadvertised object 22211589f8a68cc3fad0b556078fb10e2d5b95ce\n","stacktrace":"github.com/tektoncd/pipeline/pkg/git.run\n\tgithub.com/tektoncd/pipeline/pkg/git/git.go:54\ngithub.com/tektoncd/pipeline/pkg/git.Fetch\n\tgithub.com/tektoncd/pipeline/pkg/git/git.go:149\nmain.main\n\tgithub.com/tektoncd/pipeline/cmd/git-init/main.go:53\nruntime.main\n\truntime/proc.go:204"}{"level":"fatal","ts":1737449894.994577,"caller":"git-init/main.go:54","msg":"Error fetching git repository: failed to fetch [22211589f8a68cc3fad0b556078fb10e2d5b95ce]: exit status 128","stacktrace":"main.main\n\tgithub.com/tektoncd/pipeline/cmd/git-init/main.go:54\nruntime.main\n\truntime/proc.go:204"}


### 重载
- a,b = [1, 2, 3] 会报错
- a,b = [1, 2] 不会报错
### python中的异常有两类，一类是编译时错误（像包缺失）等会直接退出，一种是运行异常，这种不会退出
### 解释器运行起来的时候导入一个包，后面把包卸载了，解释器只要不重启，还是能正常运行的
### @dataclass
- @dataclass 是一个装饰器，用于装饰类以自动生成特殊方法，如 __init__()、__repr__()、__eq__() 等，以及管理类属性的初始化。这个装饰器是由 dataclasses 模块提供的，该模块从 Python 3.7 版本开始引入。
- 使用 @dataclass 可以简化数据存储类（data storage classes）的编写，这些类主要用于存储数据，而不包含业务逻辑。@dataclass 会自动为你生成初始化方法和其他一些实用的魔术方法。
```py

@dataclass
class Point:
    x: int
    y: int
# 创建 Point 类的实例
p = Point(1, 2)

# 访问属性
print(p.x)  # 输出: 1
print(p.y)  # 输出: 2
# 打印对象，自动生成的 __repr__ 方法
print(p)  # 输出: Point(x=1, y=2)
```
### for循环的一些问题
```py
# 内部更改循环
for i in range(3):
    i = 3
    print(i)
# 还是循环3次

# 还是5次
b = 5
for i in range(b):
    b=2
    print(i)

#  结果是1，3
b = [1,2,3,4]
for i in b:
    b.remove(i)
    print(i)
# 应该是可变对象去迭代，这个对象改变后循环的次数也会改变


res2 = [3,2]
for i in res2:
    res2.append(i)
Evaluating: res2 = [3,2]
for i in res2:
    res2.append(i) did not finish after 3.00 seconds.
```
### 偏函数
- 偏函数是一种把正常函数参数固定后得到的函数对象，通过function.partial创建
- 有利于代码的阅读，尤其是函数参数比较多的情况下
- 便于维护和修改，如果一个函数的参数被调用很多次但是参数只有几种，就可以创建几个不同的偏函数，如果要修改，只有修改偏函数
- 在future对象上添加回调函数时，由于规定回调参数只接受一个future类型的参数，可以使用偏函数将其他参数固定住
```py
from functools import partial

def power(base, exponent):
    return base ** exponent

# 创建一个新的偏函数，固定 exponent 参数为 2
square = partial(power, exponent=2)

# 现在可以直接调用 square 函数，只传递 base 参数
print(square(4))  # 输出: 16
print(square(5))  # 输出: 25

import asyncio
import functools
 
 
def callback(future, n):
    print('{}: future done: {}'.format(n, future.result()))
 
 
async def register_callbacks(all_done):
    print('registering callbacks on future')
    all_done.add_done_callback(functools.partial(callback, n=1))
    all_done.add_done_callback(functools.partial(callback, n=2))
 
 
async def main(all_done):
    await register_callbacks(all_done)
    print('setting result of future')
    all_done.set_result('the result')
 
 
event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    event_loop.run_until_complete(main(all_done))
finally:
    event_loop.close()
```
### chain #join
- link: https://blog.csdn.net/smart_liu8/article/details/81708620
- 作用是把多个可迭代对象给融合起来方便迭代
```
from itertools import chain
a = {5, 6}
b = [1, 2, 3]
c = ["a", "b"]
d = {"e": "g", "d": "h"}
for i in chain(a, b, c, d):
    print(i)
# 结果输出 5, 6, 1, 2, 3, a, b, e, g
```

### counter类
### help 参看帮助
- help(str) 查看str类型的方法
- help(str.index) 查看str类型某个方法的介绍
- dir("字符串") 查看某个变量所属类型的方法列表 这里是查看字符串的方法
- dir(str/list) 也可以这样写 直接写某个类型
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
### 字典与
- dict1 | dict2利用了Python 3.9+ 新引入的字典合并操作符，该操作符将dict2中的键值对添加到dict1中。如果两个字典中有相同的键，则dict2中的键值对会替换dict1中相应的键值对。
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
### strip(parm) 将字符串的左右两端的parm去掉
- 默认移除空格
```py
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x) # banana
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
## 如果有一个函数定义是def function2(pathname, *, parm2=False):我调用它的时候该怎么传参数呢
在 Python 中，当函数定义使用了 * 符号作为参数的一部分时，这意味着其后的参数（在这个例子中是 parm2）需要明确地使用关键字参数（keyword argument）的方式来传递。这种设计强制使代码的可读性和清晰性更高，因为调用者需要明确指定哪些参数被赋予了值。
对于你给出的函数定义：
```python
def function2(pathname, *, parm2=False):
    # 函数体
```
当你调用这个函数时，可以按以下方式进行：
只传递pathname参数：由于parm2有默认值False，所以如果你不需要修改parm2，可以只传递pathname参数。
```python
function2('your/pathname/here')
同时传递pathname和parm2参数：如果你需要修改parm2的值，你需要明确地指定parm2为关键字参数。
function2('your/pathname/here', parm2=True)
```

这里要注意的主要点是，由于使用了*，所以parm2（及之后的任何参数）必须以关键字参数的形式传入，不能仅仅依赖参数的位置。这是 Python 为了提高函数调用的清晰度所提供的一个功能。
- 如果函数定义中没有使用 * 来分隔位置参数和关键字参数，那么即使是设定为接受关键字的参数，也可以通过位置来传递。这是因为 Python 在函数调用时，默认是支持位置参数的，除非特别通过 * 来指定某个点之后的参数必须以关键字参数的形式出现。

## 表示正负无穷`float("inf") float("-inf")`
## float
- round对小数的精确度采用了四舍六入五成双的方式。
直接使用四舍五入，最后的结果可能会偏高。所以需要使用奇进偶舍的处理方法。
例如对于一个小数a.bcd，需要精确到小数点后两位，那么就要看小数点后第三位:   如果d小于5，直接舍去；如果d大于5，直接进位；
如果d等于5：d后面没有数据，且c为偶数，那么不进位，保留c。d后面没有数据，且c为奇数，那么进位，c变成(c + 1)
python中的decimal模块可以解决上面的烦恼 
decimal模块中，可以通过整数，字符串或原则构建decimal.Decimal对象。如果是浮点数，特别注意因为浮点数本身存在误差，需要先将浮点数转化为字符串。
                        
原文链接：https://blog.csdn.net/sinat_37967865/article/details/98086969
## formate 的罕见用法
```
Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(self.request))
```
## range
```
>>> for i in range(1,5,2):
...     print(i)
... 
1
3
# 如果for i in range(1,5,-2): 这样就不会有输出
```

## 集合和集合的运算 # set
- link：https://blog.csdn.net/isoleo/article/details/13000975
- set()会把字符串切割
```py
>>> set("34")
{'3', '4'}
```
- 不支持用索引取值 set("34")[0]会报错
```py
# 交集
a & b
# 并集
a | b
# 差
a - b # {1, 2} - {1, 3} 结果是2
# 增加
set_obj.add(a) # 只能单个元素
set_obj.update([a,b,c]) # 可以多个元素
# S^T或 s . symmetric _ difference _ update ( T )	补集。返回一个新集合,包括集合 S 和 T 中的元素,但不包括同时在其中的元素
# s <= T 或 S . issubset ( T )	子集测试。如果 S 与 T 相同或 S 是 T 的子集,返回 True ,否则返回 False 。可以用 S < T 判断 S 是否是 T 的真子集
# S >=Т或 S . issuperset (T)	超集测试。如果 S 与 T 相同或 S 是 T 的超集,返回 True ,否则返回 False 。可以用 S > T 判断 S 是否是 T 的真超集
s == t  # 判断集合相等
#  检查元素是否在集合中
print(1 in my_set)  # 输出：True
print(6 in my_set)  # 输出：False
# 但是不能这样
my_set in ["a", "b"] 这样怎样都是false
my_set in set(["a", "b"]) 这样怎样都是false
```
### filter(function, iterable)
- 保留function为true的
- 结果是个可迭代对象
- 即使可迭代对象为空，bool() 也是True， 要bool(list(filter())) 才能判断结果有没有值
- list(filter(lambda x: "2" in x['owner'], res)) # res是个列表，里面是字典
- 
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
