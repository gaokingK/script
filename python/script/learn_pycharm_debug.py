#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 了解 step into和step into my code的区别
# link: https://blog.csdn.net/qq_38866586/article/details/100107657
"""
step into 会一直执行，一行都不跳过，但是print()/time.time()这些会跳过, 但是inspect那个会进入，不知道为啥
step into my code ：my code就是除了库以外的文件，就是我们自己写的代码。
"""
import inspect
import time
from learn_python_get_func_name import get_function_name


def func1():
    print("run ...%s" % get_function_name())
    # print("run ...%s" % inspect.stack()[1][3])s
    start_time = time.time()
    time.sleep(1)


if __name__ == '__main__':
    func1()
