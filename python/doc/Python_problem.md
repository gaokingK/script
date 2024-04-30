# link
- [How collections.deque works?](https://zhuanlan.zhihu.com/p/63502912) -------no
# 通识
### import 时出现 no moudle named xxx
```
import sys
sys.path.append(os.dirname(os.getcwd()))
```
### 这是为什么，为什么不幂等
```
>>> [i for i in range(10) if i%2==0]
[0]
>>> 5%2
1
>>> bool(5%2==0)
False
>>> bool(4%2==0)
True
>>> a = [i for i in range(10) if i %2==0]
>>> a
[0, 2, 4, 6, 8]
>>> [i for i in range(10) if i %2==0]
[0, 2, 4, 6, 8]
>>> [i for i in range(10) if i%2==0]
[0, 2, 4, 6, 8]
>>>

```
### list_type.append("xxx")返回是空 所以不能return list_a.append("xx")
### with open # open
    - open 操作符link: https://www.runoob.com/python/python-func-open.html
      - r：读
      - w：覆盖写（从开头写）
      - a：追加写（在末尾写）
      - r+ == r+w（可读可写，文件若不存在就报错(IOError)）
      - w+ == w+r（可读可写，文件若不存在就创建）
      - a+ == a+r（可追加可写，文件若不存在就创建）
      - 对应的，如果是二进制文件，就都加一个b就好啦：‘rb’　　‘wb’　　‘ab’　　‘rb+’　　‘wb+’　　‘ab+’
        - t是windows平台特有的所谓text mode(文本模式),区别在于会自动识别windows平台的换行符。
        - 类Unix平台的换行符是\n，而windows平台用的是\r\n两个ASCII字符来表示换行，python内部采用的是\n来表示换行符。
        - rt模式下，python在读取文本时会自动把\r\n转换成\n.
        - wt模式下，Python写文件时会用\r\n来表示换行。
    - with open("./python/script/RESTFull_Api/res.json/aa") 打开目录下的aa文件
    - with open("aa") 打开程序source path下的aa文件
    - 打开utf-8编码的中文文件出现：UnicodeDecodeError: 'gbk' codec can't decode byte 0xff in position 0: illegal multibyte sequence
    ```
    #  with open(file_path, encoding="gbk", errors='ignore') as f: 改成下面这样就好了，好像是打开模式的原因
    #  with open(file_path, "r", encoding="utf-8", errors='ignore') as f: 
    ```
    - Python 使用 json.dump() 保存文件时中文会变成 Unicode。在打开写出文件时加入 encoding="utf8"，在dump时加入 ensure_ascii=False 即可解决。
    
### python 命令行中如果导入的方法修改了，需要重新导入，或者关闭命令行再重新打开，重新导入
### sort/sorted区别
    - sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作
    - sort是在原来的list上操作， sorted 返回一个新的
    - sorted(iterable, key=None, reverse=False)
        - key 是用来排序的值，默认是可迭代对象中的第一个元素（如果有嵌套的话）可返回对迭代对象中的元素的操作
        - 取相反数排序 `sorted([5,3,4,1,7,9], key=lambda x: x*-1)`
        - 指定按迭代对象中的哪一个值排序 `sorted([[3,4], [3,2,7]], key=lambda x: x[1])`
        - 按字典的value排序 `sorted({"a": "4", "b": "1", "c": 1}.items(), key = lambda x: x[1])`
        - 若是想完成 “先按xx排序， 再按xxx排序”这种， 就把key=（xx, xxx）
        - 还可以按照字典中没有的值来排序如 dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)))

### python -i -c 
    - -i -i其实就是执行文件内容或者执行命令后再进入交互模式。不会去读取$PYTHONSTARTUP这个配置文件。
    - -c 执行命令`python -i -c "print 'hello world'"`
### print(str, file_obj) # 输入到文件当中， file默认是file=sys.stdout，所以如果是file_obj就不输出到控制台了
### round
```
round(float(5/9), 4) * 1
0.5556
round(float(5/9), 4) * 10
5.556
round(float(5/9), 4) * 100
55.559999999999995
round(float(5/9), 4) * 10 * 10
55.56
```
### Error while finding module specification for 'web_main.py'
```
[huawei@localhost FlaskDemo]$ python3 -m web_main.py
/bin/python3: Error while finding module specification for 'web_main.py' (AttributeError: module 'web_main' has no attribute '__path__')
# 目录结构
[huawei@localhost FlaskDemo]$ ls -la
total 28
drwxr-xr-x  7 huawei huawei  255 Jan 14 10:03 .
drwxr-xr-x. 4 root   root     44 Jan 14 09:55 ..
drwxr-xr-x  7 huawei huawei   91 Jan 14 09:55 common
drwxr-xr-x  3 huawei huawei  127 Jan 14 09:55 .idea
-rw-r--r--  1 huawei huawei    0 Jan 14 09:55 __init__.py
drwxr-xr-x  2 huawei huawei   21 Jan 14 10:00 log
-rw-------  1 huawei huawei 1568 Jan 14 09:59 nohup.out
drwxr-xr-x  2 huawei huawei   37 Jan 14 10:03 __pycache__
-rw-r--r--  1 huawei huawei  666 Jan 14 09:55 Readme.md
-rw-r--r--  1 huawei huawei  387 Jan 14 09:55 requestments.txt
-rw-r--r--  1 huawei huawei  859 Jan 14 09:55 run.log
-rw-r--r--  1 huawei huawei    0 Jan 14 09:55 run.log.2021-12-30_10-44
-rw-r--r--  1 huawei huawei 1405 Jan 14 09:55 ssh_test.py
-rw-r--r--  1 huawei huawei  148 Jan 14 09:55 test.py
drwxr-xr-x  7 huawei huawei   99 Jan 14 09:55 web_api
-rw-r--r--  1 huawei huawei  369 Jan 14 09:55 web_main.py
# 删除一些东西就好了
[huawei@localhost FlaskDemo]$ rm -rf run.log* __pyc* nohu* run.log*
```
### 函数的参数能分多次传进去吗？
### split(delimiter, maxsplit) 指定切割次数，从左往右切割
### python 类成员
   ```
   class TestProperty:
    name = "aaa" # 这里name相当于self.name
    def __init__(self, name=None):
        if name:
            self.name = name
   ```

### 字符串
### Python 如何声明变量类型
   - from typing import List def hello(con: List)
### 模块级别与功能级别 不重要
   - http://blog.sina.com.cn/s/blog_6b9b69f10100w1xr.html
### return 和 break 的区别
   - for 循环中的return 能终止循环吗？ 可以终止    
### 涉及到字符串匹配的把 a， b都sorted()后再对比
   - sorted(iterable, /, *, key=None, reverse=False)
   - key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。 默认值为 None (直接比较元素)。
   - 是稳定的
   ```
   dict2 = sorted(dict1) # 只有key
   dict3 = sorted(dict1.items(), key=lambda x: x[1],reverse=True)
   ```
### 进制转换
   - link: https://blog.csdn.net/weixin_43353539/article/details/89444838
   - 有两种方法, 一种是内置的函数,一种是format函数
   - 其他进制转10进制 int(n, 2/8/16) # n是字符串 后面的是n的进制
   - 其他进制转其他进制 先转为10进制 bin/oct/int/hex 
     - 如hex(int('10', 2)) 二进制转16进制
   - 使用format函数进行格式化数字操作

###  3>=2 <6
### 鸭子类型
   - 介绍？
   - 这个特性的用处？
### enumerate
   - `for value, index in enumerate(list[, 枚举起始位置])`
### 三元表达式 lambda、lambda无参数的语法
   ```python
   from functools import reduce

   strict_mode =False
   if strict_mode:
       la = lambda a,b: a and b
   else:
       la = lambda a,b: a or b
   
   exec_mode = lambda a,b: a and b if strict_mode else lambda a,b: a        or b
   
   a = [None, False, True]
   print(reduce(la, a))
   print(reduce(exec_mode, a))
   # 无参数的语法
   [lambda : i * i for i in range(4)] 
   ```
### timeit的使用
    - [link](https://www.cnblogs.com/Uncle-Guang/p/8796507.html)
      - 关于timeer类的描述有误， 不是用timer对象去调用
    - 直接看这两个方法
    - timeit.timit()
    - timeit.repeate()   
### f字符串中输出{}
   - [link](https://stackoverflow.com/questions/5466451/how-can-i-print-literal-curly-brace-characters-in-a-string-and-also-use-format)
   - `f"{{}}"`
   - `hello = "HELLO"\n print(f"{{{hello.lower()}}}") # 输出{hello}`
### @overload ---------------------------------no
### path pyth # 路径 python中path相关的
- 环境变量：PATH和sys.path 以及PYTHONPATH
    - PATH 是系统的环境变量
    - sys.path 是python的搜索模块的路径集
        - sys.path.insert(0, "path1") # 将path1加入搜索路径中, 2个必选参数
        - import 相关：https://blog.csdn.net/weixin_38256474/article/details/81228492
    - PYTHONPATH 是环境变量PATH中的一个值， 默认是空
    - sys.path始化时默认包含了输入脚本所在的目录（python path/to/script, path/to 会在path中）， PYTHONPATH 和python安装目录
    - 修改PYTHONATH影响sys.path
    ```shell
    huawei ~/Desktop/people/pc_kbox/pc_kbox% export PYTHONPATH="/5555555"
    huawei ~/Desktop/people/pc_kbox/pc_kbox% python3
    >>> import sys
    >>> sys.path
    ['', '/5555555', '/usr/lib/python37.zip', '/usr/lib/python3.7', '/usr/lib/python3.7/lib-dynload', '/home/huawei/.local/lib/python3.7/site-packages', '/usr/local/lib/python3.7/dist-packages', '/usr/lib/python3/dist-packages']

    # 奇怪的是这种现象
    huawei ~/Desktop/people/pc_kbox/pc_kbox% export PYTHONPATH="5555555"
    huawei ~/Desktop/people/pc_kbox/pc_kbox% python3                     
    >>> import sys
    >>> sys.path
    ['', '/home/huawei/Desktop/people/pc_kbox/pc_kbox/5555555', '/usr/lib/python37.zip', '/usr/lib/python3.7', '/usr/lib/python3.7/lib-dynload', '/home/huawei/.local/lib/python3.7/site-packages', '/usr/local/lib/python3.7/dist-packages', '/usr/lib/python3/dist-packages']
    >>> 
    ```
- 文件路径的操作封装在os.path里的方法, 此外，还有shutil该库为python内置库，是一个对文件及文件夹高级操作的库，可以与os库互补完成一些操作，如文件夹的整体复制，移动文件夹，对文件重命名等。
    - link:
        - [os.path()模块](https://www.runoob.com/python3/python3-os-path.html)
        - [Python3 OS 文件/目录方法](https://www.runoob.com/python3/python3-os-file-methods.html)
    - 如果文件打不开，先使用os.getcwd()看下工作目录是哪里
    ```
    # 如果目录名字为中文 需要转码处理
        uPath = unicode(cPath,'utf-8')
        for fileName in os.listdir(uPath) :
            print fileName
    # 获取文件时间
        os.path.getmtime() 函数是获取文件最后修改时间
        os.path.getctime() 函数是获取文件最后创建时间
        获取的是时间戳 time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1654914448.7850325))
    # 按时间排序
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        获取文件和时间的字典
        file_dict = {key: value for key,value in zip(os.listdir(download_path), [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(os.path.join(download_path, file)))) for file in os.listdir(download_path)])}
    os.path.abspath("path") # path的绝对路径 最后一个/也会被去掉 os.path.abspath("/root/") # 输出/root
    os.path.splittext(path)[-1] 获取后缀名
    os.getcwd() # 返回当前工作目录
    os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
    os.sep 系统的路径分隔符 win 为 "\\"; Unix 为 "/"
    os.path.basename(path) # 文件名带格式 按格式判断
    os.path.dirname(path) # 文件所在文件夹名 是按格式判断的
    os.path.isdir(path) # path存在，且是文件夹、不是按格式判断的
    os.path.isfile(path) # path存在，且是文件、不是按格式判断的
    os.rmdir(path) # 删除文件夹，文件夹非空的话会报错
    os.removedirs() # 递归删除目录
        - os.removedirs("./test2/test1") # test1如果为null，就删除，然后删除test2
    - os.walk() # 遍历文件夹下的所有文件
    shutil.rmtree("path") # 空不空都能删除
    - 复制文件：https://www.jb51.net/article/145522.htm
        - https://www.jb51.net/article/145522.htm
        - shutil.copyfile("file.txt","file_copy.txt")

    ```
- file
    - w+ 读不到原本文件的内容了
    - r+ 从开头读 如果文件不存在会报错
### python2.x和python3.x 中range的不同以及python2中xrange
    - python2 中的range返回一个list，python3中返回一个可迭代对象
    - python2 中xrange返回一个生成器
    - python3 3/2=1.5 python2种3/2=1
### a = b 赋值时创建对象的顺序
    - 参照learn_python_namespace_scrope
### if condition1 and condition2 的执行顺序
    - 如果condition1 为false, 就直接返回了,不会在执行condition2, 于是我们可以这样`a=4;res = True if hasattr(a, "add") and a.add(5) else False`
### import moudle 中搜索模块的顺序
    - 输入脚本的目录
    - PYTHONPATH中的目录
    - Python默认的安装路径中
    - 实际上，解释器由 sys.path 变量指定的路径目录搜索模块，该变量初始化时默认包含了输入脚本（或者当前目录）， PYTHONPATH 和安装目录。这样就允许 Python程序了解如何修改或替换模块搜索目录。
    - 竟然还能`from ..Host.HostBase import HostBase` 此语句所在的文件是在Host文件夹下，即HostBase.py和此文件在同一目录下
### list.pop/remote/del 区别
    - a.remove(value)  删除首个符合条件的元素;返回空
    - a.pop(index) 删除索引并且返回
    - del a[start[, end]] 删除下标, 可以是范围
    - 值必须都有效,否则会报错
#### dict
    - dict.setdefault(key, value)
        - 字典中的value能为空和None
        - 如果字典中a有值(即使为空或者None), 执行该方法后还是原样, 如果没有, 就等同于添加一个新键值对
    - dict.pop("key") 
        - 从字典中删除一个键，如果键不存在会报错
        - 返回这个键的值
    - dict.popitem() 返回并删除字典中的最后一对键和值。
3. #### 类方法、静态方法、实例方法

4. #### copy.copy 与 copy.deepcopy不同的原因
    [link](https://blog.csdn.net/u010712012/article/details/79754132)
    与其他的OOP语言存储变量不同，Python中为变量赋值，并不是将值赋给变量，而是将对值的引用复制给变量
    ```
    a = [1,2,3]
    b = a 将对变量a的引用赋值给b
    b[0] = 5这不是赋值，而是改变b[0]数据块所指的值
    ```
    简单的object，copy与deepcopy没有区别，而复杂的object(对象中嵌套对象的)，copy与deepcopy在是引用还是复制其子对象（如嵌套在里面的list）就有所

5. #### 单例模式的几种实现方法
    [link](https://www.cnblogs.com/huchong/p/8244279.html)
    某些类我们希望在程序运行期间只有一个实例存在，比如读取配置信息的appconfig类
6. #### 实现单例的几种方法
    ##### 通过模块
    python的模块就是一个天然的单例模式，模块在第一次导入时会生成.pyc文件，在以后import的时候，会直接加载.pyc文件，而不会再重新执行模块代码

7. #### 关于对数据的称呼 如变量和数据对象的理解 如a = 1
    - 1 就是数据对象, a就是变量
    - 变量三要素 标识/类型/值 其中的值就是数据对象 标识是内存中的地址, 但这个地址存的是数据还是这个变量呢? 即数据对象和变量究竟对等不对等
    - 变量就是对象的别名, 我们可以通过变量找到对象,进而操纵对象
    - 标识是数据对象在内存中的地址
    - 在python总, 数据对象并不是只指向内存地址, 地址中存放值, 数据对象是一个结构体,当中有数据的值, 还有辅助的变量如维护引用计数的值
  
8.  #### 绝对导入absolute_import和unicode_literals 与相对导入, python3 默认是绝对导入
    - 前者是为了解决自定义文件名和包名冲突的情况 如果自定义了一个string.py 会和库中的string冲突
    - 后者是为了解决编码问题,由于python2 是assic编码,导入此模块后,当前文件下的编码就是unicode
9.  #### python传参的时候还是值引用还是地址引用[link](https://www.cnblogs.com/loleina/p/5276918.html)
    - 参数 形参做为函数内部的局部变量开辟内存空间
    - 值引用 形参存储的是实参的值，实际上是实参的一个副本
    - 地址引用 形参存储的是实参的地址
    - python中不支持指定 地址引用或者值引用。python中是传对象引用，如果传入的是可变对象，那么实参就不会改变，如果传入的是可变对象，那么就会改变
    - c支持选择地址引用还是值引用[link](https://www.cnblogs.com/hahahakc/p/14241166.html)

10. ##### python 理解赋值 [link](https://blog.csdn.net/dta0502/article/details/80827359)
    - a = xxx 将对象xxx赋值给变量a
    - 赋值语句总是建立对象的引用，而不是复制对象
11. ##### b=a 是普通复制，copy是顶层复制，deepcopy是全部复制
    - 对于列表 list[:] 效果和copy一样
12. ##### 建议代码中避免出现魔数,即0, 1这样数字, 应用true/false或自定义可读性高的变量代替, 提高代码可读性可维护性
13. ##### 建议使用logging模块或者traceback来记录异常。
14. ##### 返回None无意义可以删除，函数不写return，默认返回值即为None
15. ##### eval 的灵活性和危险性
    [link](https://blog.csdn.net/liuchunming033/article/details/87643041)
    返回传入字符串格式的表达式的结果，变量赋值时，把等号右边的表达式写成字符串的格式，将这个字符串作为eval的参数
    eval 也可以被用来执行系统命令 如`eval("__import__('os').system('ls /Users/chunming.liu/Downloads/')")` 所以很危险

16. ##### (for else)/(while else)/(try else)
    for 如果正常结束 else中内容会执行 
    while 如果正常结束 else中内容会执行
    try 是如果try中的内容正常执行了，执行else中内容 但是try中如果有return 就不会走到else中；else中可以使用try中建的变量
    总的来说都是正常结束了，会执行else中内容
    最后一个循环break不会走else，最后一个循环continue会else, 因为continue也相当于是走完循环了啊
    for 中如果抛出异常被捕获了，也会走到else
17. ##### 方法和函数的区别
    方法绑定在对象上面，通过对象调用; 方法被调用时,self会自动加到函数参数列表首位;method 就是封装了一个func和一个对象
    函数可以独立运行
18. ##### 通过变量引用的方式创建变量
19. ##### 获取函数信息
    func.__code__ 对象
    inspect.stack()， inspect.signature()， sys._getframe()等api应该可以获取调用my_super的函数的第一个参数
    [异常信息](https://www.cnblogs.com/oddcat/articles/11362961.html) 

20. ##### timeit 
    只能在ipython的交互式命令行中直接使用
    其他版本的python命令行中也能使用
21. ##### python 中空和None的区别
    [link](https://blog.csdn.net/qq_34152244/article/details/100639985)
    None 是一个单例对象
    空值只代表这个对象的值是空的，'' [] {} 他们之间也并不相等
    None is 任何对象都是False，除非他自己
    如果__eq__方法没被重载过，'' [] 等空值 == None 的结果也是False，并且使用== 和None比较也是不符合PEP8规范的。
    is 比 == 快很多

22. ##### 字符串连接时编译和运行
    ```python
    >>> s1 = "hell"
    >>> s1 + "o" is s2
    >>> s2 = "hello"
    False
    >>> "hell" + "o" is s2
    True
    >>>
    # 说明shell和IDE在这方面没有差异
    s1 = "hell"
    s2 = "hello"
    print(s1 + "o" is s2)  # False
    print("hell" + "o" is s2)  # True
    #因为"hell" + "o"在编译时已经变成了"hello"，而s1+"o"因为s1是一个变量，他们会在运行时进行拼接，所以没有被intern
    ```
23. ##### [Python 中 is 和 == 的不同]https://blog.csdn.net/qq_34152244/article/details/100639985)
    python 中没有===比较符，只有is 和==
    比较对象无非是比较对象的两个东西，对象的值和对象在内存中的地址(id(obj))
    is是二者都比较，`==` 只比较对象的值
        `==`比较两个对象的值是否相等，相当于调用`__eq__()`方法，即`a==b`等同于`a.__eq__(b)`。
    注意的一些问题：
    - ###### a == b 所调用的是a的__eq__方法，这个方法是可以被重载的
    - ###### 类的实例即使值一样，== 也是返回false
    - ###### 注意小整数池和字符串池的影响
24. ##### python 解释器中的小整数池机制和关于字符串的intern 机制（字符串驻留）
    [link](https://blog.csdn.net/qq_26442553/article/details/82195061)
    小整数池机制是对于[-5, 256] 范围内的整数，一旦被创建出来就不会被回收掉，存在于整个生命周期内。（还有一种说法是这些小整数对象直接在内存中创建了一份，后面使用时直接从小整数对象池中引用）
    关于字符串的intern机制简单来说就是维护一个字典， 这个字典维护字符串的值（为key）和内存中的地址（为value）每次创建字符串对象的时候都会现在这个字典中进行比较，如果存在相同的值就会返回地址，没有就会创建。相当于python对于字符串也采用了**对象池**机制
    小整数池是有范围的，intern机制对字符串也有一个约束：
    字符创的长度不能大于20，必须全部是由字母、数字、下划线组成的字符才会被放到字符串池中（如果长度为1， 啥都相同）
    - ##### 命令行中这些机制 和 程序运行时这些机制 的不同
        [link](https://www.cnblogs.com/lilz/p/9410319.html)
        在python文件中 内容相同就相同
        在命令行中，同一个代码块中内容相同就相同

25. ##### 代码块 不确定
    Python程序由代码块组成，
    确定： 缩进不一样的
    不确定：代码块作为程序的一个最小执行单位来执行，一个模块，一个类，一个函数，交互式命令行中的一行代码，都是一个代码块
26. ##### step out、step into、step into mycode run to cursor 
    对语法糖没有用
    step out  是跳出当前执行的子函数 
    step into 是进入子函数（如print就不会进入，yaml.load_all()就会进入）
    step into mycode 是进入自己子函数中
27. ##### [UnicodeDecodeError 这个是编码问题](https://blog.csdn.net/qq284489030/article/details/80561963)
    `UnicodeDecodeError: 'gbk' codec can't decode byte 0xab in position 234: illegal multibyte sequence`
    在使用yaml从文件load时遇到这样的问题，还以为是里面的中文不符合yaml的格式
    出错行`    special_letter: "line 含有特殊字符的加单引号后相当于r"xxx"'`
28. ##### [CPython、IPython等不同的python解释器](https://blog.csdn.net/xyisv/article/details/79389626)
    他们是指不同实现方式的python解释器
    CPython
        - 是指用C语言实现的Python解释器，是官方版本的解释器，也是世界上最流行的Python解释器
    PyPy
        - 这个解释器的目标是执行速度，采用JIT技术，对代码进行动态编译，所以可以显著提高代码的执行速度
        - 绝大多数的代码都可以在PyPy下运行，但执行结果可能和CPython解释器有些不同
    Jython
        - 运行在Java平台下的解释器，把python代码编译成Java字节码
29. ##### [Java中字节码和机器指令、JIT技术](https://blog.csdn.net/TheLudlows/article/details/87568456)
    - 字节码不可以被机器直接运行，而是经过JVM翻译成对应的机器指令，逐条读入，逐条翻译解释才能运行
30. ##### # python 只有6种数据类型，里面没有float，python中是怎么保存浮点数呢
    python中有6中标准数据类型，数字（不只是int，还包括float、复数等） 字符串 元组 等。。
    除此之外还有别的数据类型，bool 日期等
31. ##### 可变类型与不可变类型
    重新赋值后id()都会变的
    一个变量如果是不可变类型的变量，并不是说他不能被修改
    但是从内存地址来说，如果这个地址存储的是可变类型变量，那么如果变量改变了，他还存在这里
    如果一个不可变类型被改变了，那地址也会更改
    不可变：int str tuple 元组的内容是不可变的，但是其中如果嵌套的有列表这些可变数据类型a，那么可以通过改变这个a的值来改变元组的值，这是元组对已经绑定的可变对象的绑定关系是不可变的，就是元组里的索引一旦绑定了一个对象，就不能修改这个绑定，不能再将这个索引绑定到其它对象。但是如果元组的元素包含可变对象，那元组的内容是可以改变的，因为可变对象的值可以改变
32. ##### `python -m venv` -m参数的含义 相当于import,叫做当做模块来启动，不同的加载py文件的方式，主要是影响——sys.path 这个属性。sys.path 就相当于liunx中的PATH。
33. ##### 使用python3的venv来创建虚拟环境
    ```python
    python3 -m venv venv_name
    . venv_name/bin/activate
    # 然后终端提示符前面出现了你的venv_name
    ```
34. ##### python 模块和包
    模块是单个的文件(*.py), 包是一组模块
35. ##### pop(key[,default]) 
    从低点对象中移除key，并且返回该key的value，如果default给的话就返回default，如果key不存在会raise KeyError
36. ##### __init__的作用
    
### 异常
1. 'str' object does not support item assignment 
    - 因为str类型的对象属于不可变类型
    - `'string'[1]='string'[2]`

- TypeError: coercing to Unicode: need string or buffer, generator found
```
>>> [os.path.getmtime(os.path.join(download_path, file) for file in os.listdir(download_path))] # 这里的括号加错了，应该是这样
>>> [os.path.getmtime(os.path.join(download_path, file)) for file in os.listdir(download_path)] 
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "d:\softwares\python27\lib\genericpath.py", line 62, in getmtime
    return os.stat(filename).st_mtime
TypeError: coercing to Unicode: need string or buffer, generator found
```
### 语法糖
1. `return (rv[0] if rv else None) if one else rv`
2. 列表生成式
    ```python
    [int(x) for x in range(5)]
    [x+y for x,y in zip(1,2)]
    ```
