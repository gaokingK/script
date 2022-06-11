#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
介绍一些python的解构方法
link:
    - https://www.cnblogs.com/wongbingming/p/13775370.html
"""
import sys

"""
To: sys.modules 记录导入的模块
link: https://www.cnblogs.com/zhaojingyu/p/9069076.html
sys.modules是一个全局字典，该字典是python启动后就加载在内存中。拥有字典的一切方法，key是module的名字，value是module对象
当某个模块第一次导入，字典sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。
"""
def debug_modules():
    print(sys.modules[__name__])
    print(sys.modules.values())
    print(sys.modules.keys())
    print(sys.modules.items())

"""
To: __module__、__class__、__import__
obj.__module__<str>:  obj所在的模块路径，相对与什么的路径，从根吗？
obj.__class__ <obj>: obj所属的类对象
__import__: 动态加载类和函数
"""
def debug_mci():
    moudle_str = "learn_python_class_obj_wingman"
    # from learn_python_class_obj_wingman import TestClass3
    __import__(moudle_str)
    TestClass3 = getattr(sys.modules[moudle_str], "TestClass3")
    test3_obj = TestClass3()
    print(test3_obj.__module__)  # learn_python_class_obj_wingman
    print(test3_obj.__class__)  #<class 'learn_python_class_obj_wingman.TestClass3'>
    print(test3_obj)


"""
To: __call__ 结合类
visibility_of_element_located
"""

"""
To: __eq__ 当使用=操作符来运算两个对象时，会调用的方法
问题：如果两个不同类型的对象来=运算，会调用谁的方法呢？
    - 谁在等号左边，就用谁的
"""
class Bad(object):
    def __eq__(self, other):
        return True

class Test:
    def __eq__(self, other):
        return False


def debug_eq():
    bad_obj_1 = Bad()
    bad_obj_2 = Bad()
    print(bad_obj_1 == bad_obj_2)  # true
    
    test_obj = Test()
    print(test_obj == bad_obj_1)  # false
    print(bad_obj_1 == test_obj)  # true

"""
To: obj.__mro__: 输出obj对象所属类的基类列表
"""

    

class Spam:
    numInstances = 0
    pass


class Sub(Spam):
    numInstances = 3

def debug_mro():
    # 基类列表
    print(Sub.__mro__)  # (<class '__main__.Sub'>, <class '__main__.Spam'>, <class 'object'>)


"""
__del__方法 用来销毁实例
link: https://blog.csdn.net/weixin_39724009/article/details/110785744
当删除一个实例时，python解释器也会默认调用一个方法，这个方法为__del__()方法
如论是手动调用del还是由python自动回收都会触发
- 定义了__del_()的实例无法被Python的循环垃圾收集器收集, 那怎么被python自动回收触发呢?可能是当清空栈帧的时候
- 如果对象有多个实例, del 某个实例时, __del__并不会立即执行,而是等所有实例被删除的时候执行   
- 当最终销毁对象时，将调用__del__方法。从技术上讲(在cPython中)，即不再有对您对象的引用，即对象超出范围.
- 也不能绝对保证将调用__del__  解释器可以以各种方式退出而不删除所有对象。
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
    debug_classmethod()
    # debug_del()
    print("hhh")
