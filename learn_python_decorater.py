#!/usr/bin/python3
import random
import time
import functools

# from func_timeout import func_set_timeout, FunctionTimeOut


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


# 调用的效果: retry(wrap_parm)(func)(func_parm)
#        -> decorate(func)(func_parm)
#        -> wrapper(func_parm)
def retry(times):
    def decorater(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
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
        return wrapper
    return decorater




# @comment 等价于 comment(inner)
@comment
def inner(a):
    print("main...")
    print("parm1: {}".format(a))


@retry(5)
def inner2(a):
    print("main...")
    print("parm1: {}".format(a))
    if random.randint(0, 4) == 6:
        print("success!")
    else:
        raise AttributeError("fail")


def test_1():
    fl = []
    for i in range(1, 4):
        def g(i):
            def f():
                return i * i
            return f
        fl.append(g(i))
    return fl





# 在类中使用装饰器
class TestClass:
    pass

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



if __name__ == '__main__':
    # inner("b")  # comment(inner)("b") == inner("b")

    # inner2("b")  # retry(parm1)(inner2)("b") == inner2("b")

    # f1, f2, f3 = test_1()
    # print([f1(), f2(), f3()])

    # 在类中使用装饰器
    debug_desc_in_class()
    # no_name()

