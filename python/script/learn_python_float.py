#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal,localcontext
# 浮点数的误差 link: https://docs.python.org/zh-cn/3/tutorial/floatingpoint.html
# 保留指定位数的小数：https://blog.csdn.net/liuweiyuxiang/article/details/100574386

def cat_decimal():
    """
    "%.3f" % (1.277)
    "{}".format(1.277, '.3f')
    """
def learn_decimal():
    """
    了解Decimal模块
    """
    # 注意使用字符串来创建，如果使用数字来创建，还是有误差的
    # a = Decimal("4.2")
    # b = Decimal("2.1")
    # print(a+b)

    # 使用上下文环境来控制计算的某些设置，如数字位数和四舍五入
    a = Decimal("1")
    b = Decimal("3")
    with localcontext() as ctx:
        ctx.prec = 30
        print(a/b)


def deviation():
    """
    浮点数计算时的误差 0.1
    因为浮点数在硬件中是以2为基数的小数表示表示的，即1/2、1/4、1/8、1/16、即只有乘2的幂次方
    能为1的小数才能使用2进制小数精确的表示出来。（或者应该说只有乘2的幂次方能为2的小数，因为1x2=2）
    换成10进程可能更好理解，比如1/3永远无法使用10进制小数完整表示出来
    总之，这种情况是二进制浮点数的本质特性，他不是python的错误，也不是代码的错误，
    而是在所有支持你的硬件中的浮点数运算的语言中都会出现
    """
    a = 4.1
    b = 2.2
    print(a+b)
    a = 4.2
    b = 2.1
    print(a+b)


if __name__ == '__main__':
    deviation()
    # learn_decimal()
