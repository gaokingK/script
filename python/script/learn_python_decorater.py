#!/usr/bin/python3
"""
通过装饰器来对类或者函数添加额外的功能或者约束
"""
import inspect
import random
import time
import functools
import sys
import traceback

from learn_python_get_func_name import get_function_name
# from func_timeout import func_set_timeout, FunctionTimeOut

# 测试装饰器是什么时候执行的
# link: https://www.cnblogs.com/qiu-hua/p/12938930.html


# @func_set_timeout(1)
def test_func1():
    print("正在运行的函数名")
    time.sleep(5)


# 调用的效果: comment(func)(parm) 等价于 wrapper(parm)
def comment(func):
    def wrapper(*args, **kwargs):
        print("<function: {}> start...".format(func.__name__))
        func(*args, **kwargs)
        print("finally...")
    return wrapper


# @comment 等价于 comment(inner)
@comment
def debug_simple_decorater(a):
    print("main...")
    print("parm1: {}".format(a))


# 调用的效果: retry(wrap_parm)(func)(func_parm)
#        -> decorate(func)(func_parm)
#        -> wrapper(func_parm)
def retry(times):
    def decorater(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            nonlocal times
            while times > 0:
                print("<function: {}> start... attempt times: {}".format(func.__name__, times))
                try:
                    func(*args, **kwargs)
                    break
                except BaseException as err:
                    times -= 1
                    print("err[{}]".format(err))
                    time.sleep(3)
                finally:
                    print("finally...")
        # wrapper.__name__ = func.__name__
        return wrapper_func
    return decorater


@retry(5)
def debug_retry_decorater(a):
    print("main...")
    print("parm1: {}".format(a))
    if random.randint(0, 4) == 6:
        print("success!")
    else:
        raise AttributeError("fail")


def test_1():
    # To: 闭包不一定要避免有可变变量
    fl = []
    for i in range(1, 4):
        def g(i):
            def f():
                return i * i
            return f
        fl.append(g(i))
    return fl

"""
# To: 使用父函数的变量
下面的test2中你试图修改外部函数 test_2 的局部变量 var1，但没有使用 nonlocal 关键字来声明它。这会导致 UnboundLocalError，因为 Python 会认为你在 wrapper2 中定义了一个新的局部变量 var1，而不是使用外部函数的变量。
"""
def test_2():
    
    var1 = 1
    def wrapper2():
        print("partent var is %s" % var1)
        var1 ="2"
    wrapper2()


"""
exercise
测试怎么解决遇到重复异常时退出
"""
have_exception = True
func_stack = []
def catch_except(func):
    """用来测试遇到重复异常时退出"""
    def wrapper(*args, **kwargs):
        try:
            func_stack.append(func.__code__)
            func(*args, **kwargs)
        except AssertionError as e1:
            exc_type, exc_value, exc_obj_1 = sys.exc_info()
            # print(exc_obj_1)
            # e_1 = traceback.print_exception(exc_type, exc_value, exc_obj, limit=2,
            #                                 file=sys.stdout)
            e_1 = traceback.format_exc(limit=2)
            # raise e
            exception_handler()
            # kwargs["have_exception"] = have_exception
            try:
                func(*args, **kwargs)
            except AssertionError as e2:
                exc_type, exc_value, exc_obj_2 = sys.exc_info()
                # print(exc_obj_2)
                # e_2 = traceback.format_exc(limit=2)

                # print(e_1, end="\n\n")
                # print(e_2, end="\n\n")
                # if exc_obj_1 != exc_obj_2:
                print(func_stack)
                raise e2
    return wrapper


@catch_except
def test_catch_exception():
    get_function_name("start")
    # if have_exception:
    #     raise AssertionError("出错了")

    test_catch_exception_child()
    if have_exception:
        raise AssertionError("{}出错了".format(get_function_name()))
    get_function_name("end")


@catch_except
def test_catch_exception_child(have_exception=True):
    get_function_name("start")
    if have_exception:
        raise AssertionError("{}出错了".format(get_function_name()))
    get_function_name("end")


def exception_handler():
    global have_exception
    have_exception = False
    get_function_name("end")


"""
在类中使用装饰器
若是想被其他方法装饰(如其他模块的方法), 像正常方法使用就好
    只是实例方法被其他方法装饰后, 方法的类型会从method变成function

"""
class TestClass:

    def clear(func):
        def wrapper(self, *args, **kwargs):
            print("wrapper ...")
            func(self, *args, **kwargs)
        return wrapper

    @clear
    def no_name(self):
        print("go")


def debug_desc_in_class():
    t = TestClass()
    t.no_name()
    # t = Test()
    # t.test_a()


"""
装饰器在被装饰的函数被定义的时候执行，这通常是导入该模块时
def comment(func):
    print("ready") # 不管被装饰的函数执行多少次，这个语句只执行一次，并且在导入该模块时执行
    def wrapper(*args, **kwargs):
        print("<function: {}> start...".format(func.__name__))
        func(*args, **kwargs)
    return wrapper
# 多层装饰器，return 函数 之前的语句都会只执行一次，可以联想调用时的括号有几个，就能知道为什么了
"""


if __name__ == '__main__':
    # 创建闭包
    test_2()
    # debug_simple_decorater("b")  # comment(inner)("b") == inner("b")

    # debug_retry_decorater("b")  # retry(parm1)(inner2)("b") == inner2("b")

    # f1, f2, f3 = test_1()
    # print([f1(), f2(), f3()])

    # 在类中使用装饰器
    # debug_desc_in_class()
    # no_name()

    # 捕获异常
    # test_catch_exception()
