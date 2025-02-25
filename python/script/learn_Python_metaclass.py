#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 元类 link：https://www.cnblogs.com/tkqasn/p/6524879.html
# 重复 link2:https://blog.csdn.net/a2011480169/article/details/87891753
"""
# 一：类也是对象
# 大多数编程语言中，类就是一组用来描述如何生成一个对象的代码段，但Python中不止如此，类也是一种对象。虽然他可以通过实例化来创建一个对象，
# 但他本身仍是一个对象，也就当然可以赋值给别人等等

# 二：动态的创建类
# 这里动态的意思就是根据收到的条件做出选择 有两种办法
# 第一种办法是直接返回已经创建好的类
"""


class ObjectA:
    def __init__(self):
        self.ability = "gaga"

    def sing(self):
        print(self.ability)


class ObjectB:
    def __init__(self):
        self.ability = "gagaga"

    def sing(self):
        print(self.ability)


def create_by_return_code(condition):
    # 类定义的代码写在哪里都是一样的，也可以写在这个方法里，或者if里
    if condition:
        return ObjectA
    else:
        return ObjectB
"""
# 第二种方法是使用type()
# 当我们使用关键字class时Python在幕后做的事情就是动态创建类，这是通过元类来实现的
# type的两种用法，返回对象的类型，通过type手动创建类 type(类名, 父类的元组, 包含属性的字典(名称和值)] 可为空，但不能为None
手动创建时需要传入三要素： 名字、继承关系、命名空间
xxx.__name__/xxx.__bases__/xxx.__dict__
"""


def create_by_type():
    # 创建一个类
    # 我们已经知道，代码写在哪里没关系，这里就写在方法内
    # 注意里面要写self
    def sing(self):
        print("aoaoaos")
    # 从头创建类
    # MyClass = type(name="MyClass", bases=(), dict={"sing": sing, "ability": "aoao"}) # 不能这样
    # MyClass = type("MyClass", (), {"sing": sing, "ability": "aoao"})
    # 从已有的类创建类
    MyClass = type("MyClass", (ObjectA, ), {"sing": sing})
    return MyClass


def debug_class_creator():
    # 创建类的方法
    # MyClass = create_by_return_code(True)
    MyClass = create_by_type()
    m = MyClass()
    m.sing()
    print(m.ability)
"""
# 三：什么是元类
# 元类就是创建类的类，我们使用类来创建实例，使用元类来创建类 如：
>>> c = Chird()
<__main__.Chird object at 0x000002F2EA2CD518>
>>> type(c)
<class '__main__.Chird'>
>>> type(Chird)
<class 'type'>
type就是Python在背后用来创建所有类的元类，是Python的内建元类，那为什么不按照命名来写为Type呢？可能是与str、dict等保持一致
使用元类主要是为了创建类的时候自动的改变类
"""
# 以 使用元类来将对象的属性名变为大写的属性名 为例来展示使用自定义的元类

# 方式一
# 元类只需要返回一个类就行，我们从最简单的开始，使用函数当做元类
# 元类会自动接收type接收的参数
def upper_attr(class_name, class_parents, class_attr):
    """元类必须返回一个类对象，这里元类的作用是将属性名变为大写"""
    attr = dict((name.upper(), value) for name, value in class_attr.items() if not name.startswith("__"))
    return type(class_name, class_parents, attr)


# 方式二
# 使用类来当元类, 元类必须继承自type
class UpperAttrMetaClass(type):
    """通过改写__init__方法来控制对象的创建"""
    # def __new__(upperattr_metaclass, class_name, class_parents, class_attr):
    #     attr = dict((name.upper(), value) for name, value in class_attr.items() if not name.startswith("__"))
    #
    #     # return type(class_name, class_parents, attr)
    #     # 这样并不是OOP，而是直接调用了type, 我们应该改写父类方法
    #
    #     # 若是用type.__new__这个类就必须是type的子类？
    #     return super().__new__(upperattr_metaclass, class_name, class_parents, attr)

    # 上面的命名不符合传统名称
    def __new__(cls, name, bases, dct):
        uppercase_attr = dict((name.upper(), value) for name, value in dct.items() if not name.startswith("__"))
        return super().__new__(cls, name, bases, uppercase_attr)


# python3 中使用元类是这样的
"""
当该类被调用的时候，python会做如下事情来先创建这个类
1）如果这个类中有__metaclass__这个属性，Python会通过这个属性在内存中创建一个类对象
2）如果没有__metaclass__这个属性，Python会在父类中寻找，找不到就在模块层次中寻找，如果都找不到，就用type来创建这个类对象
注意：
- 并不是需要创建后才能知道类的属性都有什么，而是文件初始化后就知道了，然后再拿这些属性去用元类建一个类对象
- 类属性 类能访问到的资源包括：所有方法和类变量
"""
class Foo(metaclass=UpperAttrMetaClass):
    bar = "bip"


def debug_show_metaclass():
    print(Foo.__dict__)


# 插曲语法糖 字典 zip
class ObjectCreater:
    def __init__(self2):
        self2.color = "red"


class ObjectCreater2():
    def __init__(self):
        print(self)
        self.color = "red2"


# 小插曲，如果子类继承了多个类，那么子类属性是继承父类A呢还是父类B呢？谁在前面继承谁
class Chird(ObjectCreater2, ObjectCreater):
    pass

"""
TO: 元类和继承 
python在执行时，会先初始化一下文件中定义的类，初始完后，就知道了这个类有哪些方法等其他属性，这时，会用这些知道的属性在元类中重新建一个类出来
"""
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print("__new__")
        dct['my_method'] = lambda self: "Hello"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    bar = 5
    def __init__(self):
        self.bar = "hhh"
        print("start init")

    def my_method(self):
        print(self.bar)
        return "Hello   xxxxxx"

class MyClass2(MyMeta):
    pass



if __name__ == '__main__':
    # c = Chird()
    # debug_class_creator()
    # debug_show_metaclass()
    print("ok")
    obj2 = MyClass()
    print(obj2.my_method())
    # print(MyClass2().my_method())
