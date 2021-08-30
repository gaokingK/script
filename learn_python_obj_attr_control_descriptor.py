#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 上一篇了解了Python对象属性控制的方法，但若是想用这些方法去分别定义每个属性的行为，虽然能实现，但存在一些缺点
# 就是对属性的定制不够个性化，而对属性定制的更好的办法就是把这些要个性化定制的属性抽离出来，专门用一个类去描述这个属性
# 这个类就是描述符

"""
link:https://blog.csdn.net/qq_27825451/article/details/102457164?utm_medium=
distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242
link: https://blog.csdn.net/lilong117194/article/details/80111803

一个类只要实现了__get__、__set__、__delete__中的任意一个方法，就叫这个类为描述器/描述符（descriptor）
非资料描述器：只定义了__get__；意味着初始化后只能读取
资料描述器：定义了__set__、__delete__中的一个或者多个
描述符协议：描述符本质就是一个新式类，在这个新式类中至少使用了上述三个方法中的一个，这些魔术方法也被称为描述符协议。
描述符一般用于实现对象系统的底层功能（绑定和非绑定方法，类方法，静态方法 后面会有相关的介绍）

属性的 一般方法 和 访问控制行为
一般方法：通过__getattribute__、__getattr__、__setattr__、__delattr__ 控制属性的查找、设置、删除，所有属性
的相关行为都由他们来控制
访问控制行为： 对某个属性的单独控制方法，
例如，上例中假如要实现dog.age属性的类型设置（只能是整数，简单化了），如果单单去修改__setattr__方法满足它，
那这个方法便有可能不能支持其他的属性设置(比如假设存在另外一个属性 balance,那仍然不能控制其为整数，除非另外设置）
所以在类中通过__setter__等方法来设置属性的控制行为不能很好的解决问题，Python给出的解决方案是： __getattribute__、
__getattr__、__setattr__、__delattr__来实现属性查找、设置、删除等一般逻辑，而对属性的控制行为就由 属性对象 来控制，
在属性对象中定义这个属性的查找、设置、删除行为。
这个属性对象就是描述符对象。一般作为其他类对象的属性而存在，在其内部定义了三个方法(get、set、delete)来实现属性对象的查找、设置、删除行为

绑定行为和托管属性
绑定行为：在属性的访问、赋值、删除时还绑定发生了其他的事情，就是包括__getattribute__在内的属性三剑客所做的事情一样
托管属性： 描述符就是创建托管属性的一种方法，通过描述符去托管另一个类的相关属性，或者说是类属性的一个代理
"""


# 实际上这个名字应该是weight这种名字，因为他只代理一种属性
class RevealAccess:
    """
    如果里面定义__getattr__ __setattr__会生效吗？
    注意，描述符对象的__get__、__set__方法中使用了诸如self.val和self.val = val等语句，
    这些语句会调用__getattribute__、__setattr__等方法
    """
    def __init__(self, init_val=None, name='var'):
        self.val = init_val
        self.name = name

    def __get__(self, instance, owner):
        """
        定义试图取出描述符的值时的行为（只有作为描述符对象的实例调用才会生效）
        :param instance: 把描述符对象作为属性的类的实例
        :param owner: 把描述符对象作为属性的类
        """
        print("Retrieving [{}]".format(self.name))
        return self.val

    def __set__(self, instance, value):
        """
        定义当描述符的值改变时的行为
        :param instance:
        :param value: 描述符对象的值
        :return:
        """
        print("Updating [{}]".format(self.name))
        self.val = value


class MyClass:
    r = RevealAccess(10, "M_instance_x")
    y = 4

    def __init__(self, r=5):
        """
        当出现实例属性和类属性同名的情况下，类属性会被覆盖掉，因为是先初始化类属性，然后初始化实例属性
        :param r:
        """
        # self.r = r
        pass


def debug_descriptor():
    """
    属性x是一个描述符，x的value和name保存在描述符上，而不是实例m和类MyClass上,怎么理解这个保存在哪里的意思呢？
    这要结合前面的资料描述器和非资料描述器来理解
    :return:
    """
    m = MyClass()
    print(m.r)
    # # 为什么输出的是一个值，而不是一个实例对象呢，这是因为解析器发现属性是一个描述符的话，
    # # 就把m.r转换为m.__dict__["r"].__get__(None, m)来访问
    # print(m.__dict__)
    # print(MyClass.__dict__)
    # # 和上面说非资料描述器只能被读取不能被定义，而对实例m的x属性重新赋值是可以的，但是观察定义__set__和
    # # 未定义set方法后m.__dict__后发现，如果未定义set方法，对描述符同名的属性赋值后，__dict__中会出现一个同名的属性
    # # 这就说明重新赋值后的属性并不是原来的描述符对象了。这就理解了为什么说非资料描述器只能被读取而不能被重新定义了；另
    # # 外一个细节是对非资料描述器重新赋值后，再次访问的时候就不能触发__get__里定义的行为了（print Retrieving....)
    # m.r = 20
    # print(m.r)
    # print(m.__dict__)
    #
    # # RevealAccess 的实例仍然是正常的，但这里的实例和作为描述符的实例（m.r)是不一样的，观察二者的__dict__可知
    # r = RevealAccess(2, "R_instance")
    # print(r.val)
    # print(r.__dict__)
    #
    # # 描述器赋值如果是通过类的属性方式赋值，而不是类的实例方式赋值，描述器失效
    # print(MyClass.r)
    # print(MyClass.__dict__)
    # MyClass.r = 10
    # print(MyClass.r)
    # print(MyClass.__dict__)


if __name__ == '__main__':
    debug_descriptor()

