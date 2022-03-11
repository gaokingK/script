"""
# 类和对象相关的一些东西
类可以多次初始化吗? 可以
- self 只是一个约定俗成的名字
"""
import inspect
import learn_python_class_obj_wingman

from learn_get_func_name import get_function_name


def trace(cls):
    # https://stackoverflow.com/a/17019983/190597 (jamylak)
    attr_dict = inspect.getmembers(cls, lambda x: inspect.isfunction(x) or inspect.ismethod(x))
    for name, m in attr_dict:
        print(name, m)
        # setattr(cls, name, log(m))
    return cls


# @trace
class TestClass:
    def __init__(self, age=None):
        self.set_attr("func1")
        self.name = "ojbk"
        self.age = age

    def func1(self):
        print(self.name)
        print("s{}'s [{}] is running".format(self.__class__.__name__, get_function_name()))

    # def func2(self):
    #     print(getattr(a2, 'increase'))

    def set_attr(self, attr):
        # 获取子类和自己的方法，如果子类有，就获取子类的
        if hasattr(self, attr):
            print("have {}".format(attr))
            setattr(learn_python_class_obj_wingman, attr, getattr(self, attr))
            # getattr(self, attr)()
        else:
            print("no attr[{}]".format(attr))


class Child(TestClass):
    # def func1(self):
    #     super(Child, self).func1()
    #     print("{}'s [{}] is running".format(self.__class__.__name__, get_function_name()))

    def func2(self):
        print("{}'s [{}] is running".format(self.__class__.__name__, get_function_name()))


def debug_getattr():
    # 获取子类和自己的方法，如果子类有，就获取子类的
    # t = TestClass()
    c = Child()

    # t = TestClass()
    # t.set_attr()


def debug_decri():
    # 装饰类
    t = TestClass()
    # c = Child()
    # learn_class_obj_wingman.super_func()
    # c.name = "ojb"
    # learn_class_obj_wingman.super_func()
 q  
    trace(t)


"""
To：类可以多次初始化吗?
可以
"""
def debug_multi_init():
    t1 = TestClass(5)
    print(t1.age)
    # t2 = TestClass(t1)
    t2 = TestClass(TestClass(5))
    print(t2.age)  # 是个TestClass的实例


"""
To: self 只是一个约定俗成的名字
你的第一个参数是self(虽然你写成了PCO，但他指的就是类对象自己)，第二个参数是n
你调用时传入了两个参数，再加上self本身，就是三个参数了，所以报错没毛病

再一个，下边的HTTP_RecvReqWithBody，应该也会报错，报self未定义，因为在这个方法里，你的self被定义成了PC
"""


if __name__ == '__main__':
    # debug_getattr()
    # debug_decri()
    debug_multi_init()
