#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1. 继承和重载以及实例化中绑定属性的过程
    子类重载父类的init情况下
        子类init前:绑定父类和子类的类成员变量到self(不知道谁先谁后) -> 子类init中: 绑定子类的实例变量绑定self ->
        父类的init: 绑定父类的实例变量到self
1. 子类init中不主动调用父类init, 会失去父类init中所添加的属性，但是可以获得父类的实例方法等方法, 子类如果没有init 会调用父类的
2. 在父类中获取子类独有的属性 link: http://cn.voidcc.com/question/p-gtondtnq-vo.html
"""


class A:
    temp_A = ""
    def __init__(self):
        """
        子类调用这个方法时, self是子类的实例, 而不是A的实例
        """
        self.name = "A"
        self.set_color()
        self.height = 55

    def set_color(self):
        self.color= "red"


class Aa(A):
    def __init__(self):
        """
        这个时候self就有了temp_Aa, temp_A了
        """
        self.name = "Aa"
        super().__init__()

    def print_nothing(self):
        print("nothing")

    temp_Aa = "a"


def debug_overwrite():
    # 测试子类init中不主动调用父类init, 会失去父类init中所添加的属性，但是可以获得父类的实例方法等方法
    aa = Aa()
    print(aa.name)
    # aa.set_color()
    print(aa.color)  # 会报错，但是运行过set_color就不会了
    print("ok")


if __name__ == '__main__':
    debug_overwrite()
