#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 学习__str__和__repr__方法及其区别
# link：https://www.cnblogs.com/xiaoneng/p/11699633.html
# python中有两种方法控制对象转字符串str()和repr(), 他们会调用类中同名的下划线方法

# 了解str()和repr()区别
# link：https://www.cnblogs.com/xhyan/p/8404318.html


class T:
    def __init__(self):
        self.color = "red"

    def __str__(self):
        """
        需要将实例转化为字符串时调用 str(obj)时
        __str__的默认实现就是调用__repr__
        但是类转化为字符串时不调用这个
        :return:
        """
        # return None
        return "__str__ {}".format(self.color)

    def __repr__(self):
        """
        也是在将实例转化为字符串时调用，repr(obj)时
        但是类转化为字符串时不调用这个
        :return:
        """
        return "__repr__ {}".format(self.color)


def debugger():
    # 主要了解将对象实例的两种方法的区别,和各自的作用
    t = T()
    # 优先级
    # 直接查看对象时只显示repr中定义的，将字符串转化为字符串时调用str，如果str没有定义就按照repr中定义的
    print([t])
    print(t)

    # 虽然[t]和[repr(t)]打印的是一样的内容，但是前者是对象，后者是字符串
    a = [t, repr(t)]
    print(a)
    print(a[0].color)
    print(a[1].color)
    pass


def different_str_repr():
    """
    str被用作为终端用户创建输出；而repr()被主要用来开发调试。
    repr的目的是清晰；str的目的是可读
    """
    # 打印字符串时不同
    # s = "hello"
    # print(str(s))
    # print(repr(s))  # 带引号，和在命令行中输入"hello"然后按回车的输出，是把对象真实的值打印出来

    # data不同
    import datetime
    s = datetime.datetime.now()
    # print(str(s))
    # print(repr(s))

    # 对浮点数的精度 只有python2中有区别
    print(str(1.0/7.0))
    print(repr(1.0/7.0))
    pass


if __name__ == '__main__':
    # debugger()
    different_str_repr()
