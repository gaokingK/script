#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __new__、__init__、__call__各自的作用和之间的区别
# link: https://www.cnblogs.com/tkqasn/p/6524879.html
# __new__被用来创建对象并返回对象，是一个类方法；它在返回一个对象后，会自动的调用__init__方法，如果没有返回实例，就不会去自动调用init
# __init__被用来将传入的参数初始化给对象，是实例属性的初始化。他可以没有返回值，
# __call__ 方法和实例化没有多大关系了，定义了这个方法才能被使用函数的方式执行，然后调用__new__,__init__
# 是在对象创建后执行的方法


class Foo:
    def __init__(self):
        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        # 正常情况下重写new是要调用父类的方法, 要不创建出来类是NoneType
        # print("__new__")
        # return super(Foo, cls).__new__(cls, *args, **kwargs)

        # 可以用来创建别的类
        return object.__new__(Stranger, *args, **kwargs)


class Stranger:
    def __init__(self):
        print("Stranger __init")


def debugger():
    # 如果__new__返回的不是本类的实例，那么本类的init和生成类的init都不会调用
    f = Foo()
    print(type(f))


if __name__ == '__main__':
    debugger()
