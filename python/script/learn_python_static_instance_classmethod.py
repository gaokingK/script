#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# 实例方法、类方法的区别、静态方法的区别：https://www.cnblogs.com/wcwnina/p/8644892.html
访问对象：实例、实例和类、实例和类；静态方法也不能直接调用也需要一个对象
方法能访问的资源：类和实例的属性、类的属性、都不能访问（访问的资源逐渐搜索）
这里能访问的资源和调用的对象没有区别，比如即使用实例访问类方法，类方法中仍然不能访问实例属性

# 绑定方法与非绑定方法 https://blog.csdn.net/HHG20171226/article/details/93229831
- 绑定的意思是绑定给谁，在调用的时候就把谁当成第一个参数传入
- 绑定方法分为类方法和实例方法
- 非绑定方法为静态方法

@staticmethod @classmethod 这些装饰器是只有装饰作用吗
它们的作用不仅仅是“装饰”那么简单，而是：

✅ 改变方法的绑定方式和调用行为！
@staticmethod 会将函数变成一个普通函数放在类的命名空间里，不会自动传入 self 或 cls 参数。
@classmethod 会让方法的第一个参数变成 cls，自动传入调用它的类本身。
"""


class A:
    name = "gougo"

    def __init__(self):
        self.color = "5"

    def print_color(self):
        print(self.name)
        print(self.color)

    @classmethod
    def print_name(cls):
        print(cls.name)

    @classmethod
    def print_cls_name(cls):
        print(f"cls.__name__is {cls.__name__}")

    @staticmethod
    def print_nothing():
        print("nothing")


"""
To: 使用类方法实现一个计数器
"""
class Spam:
    numInstances = 0

    @classmethod
    def count(cls):  # 对每个类做独立计数
        cls.numInstances += 1  # cls是实例所属于的最底层类

    def __init__(self):
        self.count()  # 里面虽然没有参数，是隐式的将self.__class__传给count方法


class Sub(Spam):
    numInstances = 3


class Other(Spam):
    numInstances = 0


def debug_classInstanceCounter():
    x = Spam()
    y1, y2, y3 = Sub(), Sub(), Sub()
    z1, z2, z3 = Other(), Other(), Other()
    print(x.numInstances, y1.numInstances, z1.numInstances)  # 输出：(1, 6, 3)
    print(Spam.numInstances, Sub.numInstances, Other.numInstances)  # 输出：(1, 6, 3)

if __name__ == '__main__':
    a = A()
    a.print_color()
    # A.print_color()

    # a.print_name()
    # A.print_name()

    # a.print_nothing()
    # A.print_nothing()

    # A.print_cls_name()

    # debug_classInstanceCounte()
    print("ok")
