#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Bad(object):
    def __eq__(self, other):
        return True

    @staticmethod
    def my_func():
        pass


def sample_sort_list(sample_inst):
    print(sample_inst is [])
    if sample_inst is []:
        return
    sample_inst.sort()


class Spam:
    numInstances = 0

    @classmethod
    def count(cls):  # 对每个类做独立计数
        cls.numInstances += 1  # cls是实例所属于的最底层类

    def __init__(self):
        self.count()  # 将self.__class__传给count方法


class Sub(Spam):
    numInstances = 3


class Other(Spam):
    numInstances = 0


def debug_classmethod():
    x = Spam()
    y1, y2, y3 = Sub(), Sub(), Sub()
    z1, z2, z3 = Other(), Other(), Other()
    print(x.numInstances, y1.numInstances, z1.numInstances)  # 输出：(1, 2, 3)
    print(Spam.numInstances, Sub.numInstances, Other.numInstances)

# 基类列表
    print(Other.__mro__)


if __name__ == '__main__':
    # bad_inst = Bad()
    # bad_inst.my_func()
    # fake_list = (3, 4, 5)
    # sample_sort_list(fake_list)
    debug_classmethod()
    print()
