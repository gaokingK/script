#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 继承和重载
"""
1. 子类init中不主动调用父类init, 会失去父类init中所添加的属性，但是可以获得父类的实例方法等方法
"""

class A:
    def __init__(self):
        self.name = "A"
        self.set_color()
        self.height = 55

    def set_color(self):
        self.color= "red"


class Aa(A):
    def __init__(self):
        self.name = "Aa"
        super().__init__()

    def print_nothing(self):
        print("nothing")


def debug_overwrite():
    # 测试子类init中不主动调用父类init, 会失去父类init中所添加的属性，但是可以获得父类的实例方法等方法
    aa = Aa()
    print(aa.name)
    # aa.set_color()
    print(aa.color)  # 会报错，但是运行过set_color就不会了
    print("ok")


if __name__ == '__main__':
    debug_overwrite()
