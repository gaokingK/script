#!/usr/bin/python3
"""
string = "113/kbox_result_202110180959.txt"
ls 113/*.txt|sed "s/*kbox_r.*t_//g" 为什么kbox前的那个星号没有用，因为sed也能用正则，但是*号代表前个模式匹配0次或者多次， 但为什没有用呢？难道前面不是null吗

[a-z0-9]([-a-z0-9]*[a-z0-9])? == [a-z0-9][-a-z0-9]*
"""
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

"""
re.search() 返回一个匹配的对象
re.findall() 返回一个列表, 里面是匹配到的内容, 如果里面有分组的话,只显示分组的
"""
if __name__ == "__main__":
    choice_num()

