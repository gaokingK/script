#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 传参


class A:
    def __init__(self, ip, passwd=None):
        self.ip = ip
        self.passwd = passwd
        self.use_parm(self.ip, self.passwd)

    def use_parm(self, ip, passwd):
        if not ip:
            print("no ip parm")
        else:
            print(ip, passwd)


if __name__ == '__main__':
    a = A(4, passwd=5)

