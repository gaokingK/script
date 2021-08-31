#!/usr/bin/python3
import re


def choice_num(num="[40,256][88,888]"):
    # 把数字挑出来并放到列表中
    pattern1 = re.compile(r'(\d+)\D*')
    res = pattern1.findall(num)
    print(res)
    res = re.findall(r'(\d+)\D*', num)
    print(res)
    res = re.finditer(r'(\d+)', num)
    print([x.group() for x in res])

if __name__ == "__main__":
    choice_num()

