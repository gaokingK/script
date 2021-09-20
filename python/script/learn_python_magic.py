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


"""
__del__方法 用来销毁实例
link: https://blog.csdn.net/weixin_39724009/article/details/110785744?utm_medium=d
istribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-1.no_search_link&spm=1001.2101.3001.4242
当删除一个实例时，python解释器也会默认调用一个方法，这个方法为__del__()方法
如论是手动调用del还是由python自动回收都会触发
定义了__del_()的实例无法被Python的循环垃圾收集器收集, 那怎么被python自动回收触发呢?可能是当清空栈帧的时候
如果对象有多个实例, del 某个实例时, __del__并不会立即执行,而是等所有实例被删除的时候执行   
当最终销毁对象时，将调用__del__方法。从技术上讲(在cPython中)，即不再有对您对象的引用，即对象超出范围
也不能绝对保证将调用__del__  解释器可以以各种方式退出而不删除所有对象。
如前所述，__del__功能有些不可靠。在可能有用的情况下，请考虑使用__enter__和__exit__方法。
"""


class DelClass:
    def __del__(self):
        """
        必须显示调用父类的同名方法, 但这里使用super()调用无效
        这样才能保证在回收子类对象时，其占用的资源（可能包含继承自父类的部分资源）能被彻底释放
        断点打在这里无效
        :return:
        """
        pass
        print("run __del__")


def debug_del():
    # To __del__ 的执行流程
    d = DelClass()
    # 下面这一句会对输出有影响
    # c = d
    del d  # 因为还有c的缘故, 并没有调起__del__方法, 等下面流程走完了, 开始回收这块内存的时候,
    # 开始销毁对象,这是最后一个实例c被销毁时, 才调用了__del__
    print("OK")
    print("hhhOK")


if __name__ == '__main__':
    # bad_inst = Bad()
    # bad_inst.my_func()
    # fake_list = (3, 4, 5)
    # sample_sort_list(fake_list)
    # debug_classmethod()
    debug_del()
    print("hhh")
