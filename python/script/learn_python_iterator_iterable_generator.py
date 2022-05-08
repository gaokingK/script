#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 可迭代对象，迭代器，生成器
"""
可迭代对象：实现了__iter__方法
迭代器对象：实现了__iter__和__next__方法
生成器对象：使用yield语句实现了惰性触发，也是迭代器的一种;不同之处在于yield结束后会保存此时函数的状态。

使用：
    都能被for遍历
    迭代器和生成器能被next()调用
简便的方式是使用iter()变为迭代器
"""
# from itertools import Iterable
from typing import Iterable


class MyIterable:
    def __init__(self):
        self.data = [0, 2, 2]

    def __iter__(self):
        """
        这个方法返回一个迭代器, 只要定义了这个方法，就已经是Iterable了
        iter(obj)就会调用obj的__iter__
        """
        print("ok")
        return iter(self.data)


def debug_iterable():
    a = MyIterable()
    for i in a:
        print(i)


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.now = -1

    def __iter__(self):
        # 由于本身就是迭代器，这里就返回自己
        return self

    def __next__(self):
        while self.now < (len(self.data) - 1):
            self.now += 1
            return self.data[self.now]
        # 这里最后一定要raise异常，因为for和next会获取这里的返回值
        # for 能处理StopIteration异常
        raise StopIteration


def debug_iterator():
    list_a = [x for x in range(10)]
    a = MyIterator(list_a)
    print(next(a))
    print(next(a))
    print("continue")
    # 这里for会从2输出
    for i in a:
        print(i)


if __name__ == '__main__':
    # debug_iterable()
    debug_iterator()
    print("OK")
