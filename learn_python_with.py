#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 学习with语句的原理
# link：https://www.cnblogs.com/pythonbao/p/11211347.html
"""
上下文管理协议 和 上下文管理器
    上下文管理协议（Context Management Protocol）：支持该协议的对象要实现两个方法：__enter__/__exit__
    上下文管理器：是指支持上下文管理协议的对象。

通过with调用上下文管理器，也可以直接通过调用器方法来使用
自定义上下文管理器对软件中的资源进行管理，比如数据库连接，共享资源的访问控制等。
原理就是try...except..finally

执行过程：

"""


class MyContext(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        """
        as xx 中可以使用单个对象接收，也可以是多个对象，但多个对象必须使用元组包裹，不能只是用，分割
        """
        print("进入enter")
        return self

    def do_self(self):
        print("do {}".format(self.name))
        raise AssertionError("555")

    def __exit__(self, exc_type, exc_value, exec_traceback):
        """
        负责执行清理工作，比如释放资源
        如果执行过程中没有异常，或者BLOCK中执行了break、continue、return就以None调用exit（None，None，None）
        如果有异常，就使用sys.exec_info得到的异常信息为参数调用exit
        能捕捉with语句中的异常，比如as xxx 重载的参数个数不匹配
        """
        if exc_type:
            print(exc_type, exc_value, exec_traceback)
            return False
        # 上面无论返回True还是False，下面都不会执行，和其他return一样
        print("退出exit")


def raise_func():
    raise AssertionError("555")


def debug_cm():
    with MyContext('test') as (mc1):
        """
        as xx 语句是可选的，如果定义了，接受的是enter函数的返回值。
        1. 执行完 with xxx 就生成了上下文管理器对象cm
        2. 获取cm的exit方法，保存起来供以后使用，如果没有定义exit，那么就会报错
        3. 调用cm的enter方法，如果使用了as子句，将返回值赋值给as子句中的xx
        4. 执行BLOCk，这里面也可以调用外部方法，不是只能使用cm中的方法
        5. 不管执行完是否发生了异常，都执行exit
        6. exit如果返回false，就会重新跑出异常，让with之外的语句来处理异常，这也是通用做法；如果返回True，则无视
        """
        # BLOCK
        # mc.do_self()
        raise_func()
        # 如果发生了异常，无论exit返回True还是False，下面的语句都不会进行
        print("ok")


if __name__ == '__main__':
    debug_cm()
