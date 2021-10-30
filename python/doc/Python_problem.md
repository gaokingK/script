### 通识

2. #### 鸭子类型
   - 介绍？
   - 这个特性的用处？
3. #### 三元表达式 lambda
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

   ```
4. #### timeit的使用
   1. [link](https://www.cnblogs.com/Uncle-Guang/p/8796507.html)
      - 关于timeer类的描述有误， 不是用timer对象去调用
    - 直接看这两个方法
    - timeit.timit()
    - timeit.repeate()   
5. #### f字符串中输出{}
   - [link](https://stackoverflow.com/questions/5466451/how-can-i-print-literal-curly-brace-characters-in-a-string-and-also-use-format)
   - `f"{{}}"`
   - `hello = "HELLO"\n print(f"{{{hello.lower()}}}") # 输出{hello}`
6. #### @overload ---------------------------------no
7. #### python中path相关的
   1. 环境变量：PATH和sys.path 以及PYTHONPATH
      1. PATH 是系统的环境变量
      2. sys.path 是python的搜索模块的路径集
      3. PYTHONPATH 是环境变量PATH中的一个值， 默认是空
      4. sys.path始化时默认包含了输入脚本所在的目录（或者当前目录）， PYTHONPATH 和python安装目录
      5. 修改PYTHONATH影响sys.path
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
   2. 文件路径的操作封装在os.path里的方法
      1. [Python3 OS 文件/目录方法](https://www.runoob.com/python3/python3-os-file-methods.html)
        
8. #### import moudle 中搜索模块的顺序
   1. 输入脚本的目录
   2. PYTHONPATH中的目录
   3. Python默认的安装路径中
   4. 实际上，解释器由 sys.path 变量指定的路径目录搜索模块，该变量初始化时默认包含了输入脚本（或者当前目录）， PYTHONPATH 和安装目录。这样就允许 Python程序了解如何修改或替换模块搜索目录。

9.  #### python2.x和python3.x 中range的不同以及python2中xrange
    - python2 中的range返回一个list，python3中返回一个可迭代对象
    - python2 中xrange返回一个生成器
10. #### a = b 赋值时创建对象的顺序
    - 参照learn_python_namespace_scrope
11. #### if condition1 and condition2 的执行顺序
    - 如果condition1 为false, 就直接返回了,不会在执行condition2, 于是我们可以这样`a=4;res = True if hasattr(a, "add") and a.add(5) else False`
12. #### list.pop/remote/del 区别
    - a.remove(value)  删除首个符合条件的元素;返回空
    - a.pop(index) 删除索引并且返回
    - del a[start[, end]] 删除下标, 可以是范围
    - 值必须都有效,否则会报错
13. #### dict.setdefault(key, value)
    - 字典中的value能为空和None
    - 如果字典中a有值(即使为空或者None), 执行该方法后还是原样, 如果没有, 就等同于添加一个新键值对
14. #### 类方法、静态方法、实例方法

15. #### copy.copy 与 copy.deepcopy不同的原因
    [link](https://blog.csdn.net/u010712012/article/details/79754132)
    与其他的OOP语言存储变量不同，Python中为变量赋值，并不是将值赋给变量，而是将对值的引用复制给变量
    ```
    a = [1,2,3]
    b = a 将对变量a的引用赋值给b
    b[0] = 5这不是赋值，而是改变b[0]数据块所指的值
    ```
    简单的object，copy与deepcopy没有区别，而复杂的object(对象中嵌套对象的)，copy与deepcopy在是引用还是复制其子对象（如嵌套在里面的list）就有所

16. #### 单例模式的几种实现方法
    [link](https://www.cnblogs.com/huchong/p/8244279.html)
    某些类我们希望在程序运行期间只有一个实例存在，比如读取配置信息的appconfig类
17. #### 实现单例的几种方法
    ##### 通过模块
    python的模块就是一个天然的单例模式，模块在第一次导入时会生成.pyc文件，在以后import的时候，会直接加载.pyc文件，而不会再重新执行模块代码

18. #### 关于对数据的称呼 如变量和数据对象的理解 如a = 1
    - 1 就是数据对象, a就是变量
    - 变量三要素 标识/类型/值 其中的值就是数据对象 标识是内存中的地址, 但这个地址存的是数据还是这个变量呢? 即数据对象和变量究竟对等不对等
    - 变量就是对象的别名, 我们可以通过变量找到对象,进而操纵对象
    - 标识是数据对象在内存中的地址
    - 在python总, 数据对象并不是只指向内存地址, 地址中存放值, 数据对象是一个结构体,当中有数据的值, 还有辅助的变量如维护引用计数的值
  
19. #### 绝对引用 绝对导入absolute_import和unicode_literals 与相对导入, python3 默认是绝对导入
    - from __future__ import absolute_import
    - 前者是为了解决自定义文件名和包名冲突的情况 如果自定义了一个string.py 会和库中的string冲突
    - 后者是为了解决编码问题,由于python2 是assic编码,导入此模块后,当前文件下的编码就是unicode
20. #### python传参的时候还是值引用还是地址引用[link](https://www.cnblogs.com/loleina/p/5276918.html)
    - 参数 形参做为函数内部的局部变量开辟内存空间
    - 值引用 形参存储的是实参的值，实际上是实参的一个副本
    - 地址引用 形参存储的是实参的地址
    - python中不支持指定 地址引用或者值引用。python中是传对象引用，如果传入的是可变对象，那么实参就不会改变，如果传入的是可变对象，那么就会改变
    - c支持选择地址引用还是值引用[link](https://www.cnblogs.com/hahahakc/p/14241166.html)

21. ##### python 理解赋值 [link](https://blog.csdn.net/dta0502/article/details/80827359)
    - a = xxx 将对象xxx赋值给变量a
    - 赋值语句总是建立对象的引用，而不是复制对象
22. ##### b=a 是普通复制，copy是顶层复制，deepcopy是全部复制
    - 对于列表 list[:] 效果和copy一样
23. ##### 建议代码中避免出现魔数,即0, 1这样数字, 应用true/false或自定义可读性高的变量代替, 提高代码可读性可维护性
24. ##### 建议使用logging模块或者traceback来记录异常。
25. ##### 返回None无意义可以删除，函数不写return，默认返回值即为None
26. ##### eval 的灵活性和危险性
    [link](https://blog.csdn.net/liuchunming033/article/details/87643041)
    返回传入字符串格式的表达式的结果，变量赋值时，把等号右边的表达式写成字符串的格式，将这个字符串作为eval的参数
    eval 也可以被用来执行系统命令 如`eval("__import__('os').system('ls /Users/chunming.liu/Downloads/')")` 所以很危险

27. ##### (for else)/(while else)/(try else)
    for 如果正常结束 else中内容会执行 
    while 如果正常结束 else中内容会执行
    try 是如果try中的内容正常执行了，执行else中内容
    总的来说都是正常结束了，会执行else中内容
28. ##### 方法和函数的区别
    方法绑定在对象上面，通过对象调用; 方法被调用时,self会自动加到函数参数列表首位;method 就是封装了一个func和一个对象
    函数可以独立运行
29. ##### 通过变量引用的方式创建变量
30. ##### 获取函数信息
    func.__code__ 对象
    inspect.stack()， inspect.signature()， sys._getframe()等api应该可以获取调用my_super的函数的第一个参数
    [异常信息](https://www.cnblogs.com/oddcat/articles/11362961.html) 

31. ##### timeit 
    只能在ipython的交互式命令行中直接使用
    其他版本的python命令行中也能使用
32. ##### python 中空和None的区别
    [link](https://blog.csdn.net/qq_34152244/article/details/100639985)
    None 是一个单例对象
    空值只代表这个对象的值是空的，'' [] {} 他们之间也并不相等
    None is 任何对象都是False，除非他自己
    如果__eq__方法没被重载过，'' [] 等空值 == None 的结果也是False，并且使用== 和None比较也是不符合PEP8规范的。
    is 比 == 快很多

33. ##### 字符串连接时编译和运行
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
34. ##### [Python 中 is 和 == 的不同]https://blog.csdn.net/qq_34152244/article/details/100639985)
    python 中没有===比较符，只有is 和==
    比较对象无非是比较对象的两个东西，对象的值和对象在内存中的地址(id(obj))
    is是二者都比较，`==` 只比较对象的值
        `==`比较两个对象的值是否相等，相当于调用`__eq__()`方法，即`a==b`等同于`a.__eq__(b)`。
    注意的一些问题：
    - ###### a == b 所调用的是a的__eq__方法，这个方法是可以被重载的
    - ###### 类的实例即使值一样，== 也是返回false
    - ###### 注意小整数池和字符串池的影响
35. ##### python 解释器中的小整数池机制和关于字符串的intern 机制（字符串驻留）
    [link](https://blog.csdn.net/qq_26442553/article/details/82195061)
    小整数池机制是对于[-5, 256] 范围内的整数，一旦被创建出来就不会被回收掉，存在于整个生命周期内。（还有一种说法是这些小整数对象直接在内存中创建了一份，后面使用时直接从小整数对象池中引用）
    关于字符串的intern机制简单来说就是维护一个字典， 这个字典维护字符串的值（为key）和内存中的地址（为value）每次创建字符串对象的时候都会现在这个字典中进行比较，如果存在相同的值就会返回地址，没有就会创建。相当于python对于字符串也采用了**对象池**机制
    小整数池是有范围的，intern机制对字符串也有一个约束：
    字符创的长度不能大于20，必须全部是由字母、数字、下划线组成的字符才会被放到字符串池中（如果长度为1， 啥都相同）
    - ##### 命令行中这些机制 和 程序运行时这些机制 的不同
        [link](https://www.cnblogs.com/lilz/p/9410319.html)
        在python文件中 内容相同就相同
        在命令行中，同一个代码块中内容相同就相同

36. ##### 代码块 不确定
    Python程序由代码块组成，
    确定： 缩进不一样的
    不确定：代码块作为程序的一个最小执行单位来执行，一个模块，一个类，一个函数，交互式命令行中的一行代码，都是一个代码块
37. ##### step out、step into、step into mycode run to cursor 
    对语法糖没有用
    step out  是跳出当前执行的子函数 
    step into 是进入子函数（如print就不会进入，yaml.load_all()就会进入）
    step into mycode 是进入自己子函数中
38. ##### [UnicodeDecodeError 这个是编码问题](https://blog.csdn.net/qq284489030/article/details/80561963)
    `UnicodeDecodeError: 'gbk' codec can't decode byte 0xab in position 234: illegal multibyte sequence`
    在使用yaml从文件load时遇到这样的问题，还以为是里面的中文不符合yaml的格式
    出错行`    special_letter: "line 含有特殊字符的加单引号后相当于r"xxx"'`
39. ##### [CPython、IPython等不同的python解释器](https://blog.csdn.net/xyisv/article/details/79389626)
    他们是指不同实现方式的python解释器
    CPython
        - 是指用C语言实现的Python解释器，是官方版本的解释器，也是世界上最流行的Python解释器
    PyPy
        - 这个解释器的目标是执行速度，采用JIT技术，对代码进行动态编译，所以可以显著提高代码的执行速度
        - 绝大多数的代码都可以在PyPy下运行，但执行结果可能和CPython解释器有些不同
    Jython
        - 运行在Java平台下的解释器，把python代码编译成Java字节码
40. ##### [Java中字节码和机器指令、JIT技术](https://blog.csdn.net/TheLudlows/article/details/87568456)
    - 字节码不可以被机器直接运行，而是经过JVM翻译成对应的机器指令，逐条读入，逐条翻译解释才能运行
41. ##### python 只有6种数据类型，里面没有float，python中是怎么保存浮点数呢
    python中有6中标准数据类型，数字（不只是int，还包括float、复数等） 字符串 元组 等。。
    除此之外还有别的数据类型，bool 日期等
42. ##### 可变类型与不可变类型
    重新赋值后id()都会变的
    一个变量如果是不可变类型的变量，并不是说他不能被修改
    但是从内存地址来说，如果这个地址存储的是可变类型变量，那么如果变量改变了，他还存在这里
    如果一个不可变类型被改变了，那地址也会更改
    不可变：int str tuple 元组的内容是不可变的，但是其中如果嵌套的有列表这些可变数据类型a，那么可以通过改变这个a的值来改变元组的值，这是元组对已经绑定的可变对象的绑定关系是不可变的，就是元组里的索引一旦绑定了一个对象，就不能修改这个绑定，不能再将这个索引绑定到其它对象。但是如果元组的元素包含可变对象，那元组的内容是可以改变的，因为可变对象的值可以改变
43. ##### `python -m venv` -m参数的含义 相当于import,叫做当做模块来启动，不同的加载py文件的方式，主要是影响——sys.path 这个属性。sys.path 就相当于liunx中的PATH。
44. ##### 使用python3的venv来创建虚拟环境
    ```python
    python3 -m venv venv_name
    . venv_name/bin/activate
    # 然后终端提示符前面出现了你的venv_name
    ```
45. ##### python 模块和包
    模块是单个的文件(*.py), 包是一组模块
46. ##### pop(key[,default]) 
    从低点对象中移除key，并且返回该key的value，如果default给的话就返回default，如果key不存在会raise KeyError
47. ##### __init__的作用
    
### 异常
1. 'str' object does not support item assignment 
    - 因为str类型的对象属于不可变类型
    - `'string'[1]='string'[2]`
### 语法糖
1. `return (rv[0] if rv else None) if one else rv`
2. 列表生成式
    ```python
    [int(x) for x in range(5)]
    [x+y for x,y in zip(1,2)]
    ```