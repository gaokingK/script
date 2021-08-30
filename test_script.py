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



if __name__ == '__main__':
    # with Mycontex('test') as mc:
    #     mc.do_self()
    debug_overwrite()
    print("OK")
