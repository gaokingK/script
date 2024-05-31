#!/usr/bin/env python
# -*- coding: utf-8 -*-
from learn_python_static_instance_classmethod import A

class Mycontex(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("进入enter")
        return self

    def do_self(self):
        print(self.name)
        raise AssertionError("555")

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出exit")
        if exc_type:
            print(exc_type, exc_value, traceback)
            return False

def change_dict(dict_obj):
    dict_obj["hi"]=5

if __name__ == '__main__':
    # with Mycontex('test') as mc:
    #     mc.do_self()
    # debug_overwrite()
    # print("OK")
    
    # 如果字典传入方法，方法内改了字典，外部对象的字典会被改变吗 会的
    # a=[{"b":"ss"}]
    # change_dict(a)
    # print(a)

    # 如果在for循环中传入呢 也会对
    a=[{"b":"ss"}] 
    for i in a:
        change_dict(i)
        print(i)
    print(a)
    pass
