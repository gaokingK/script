#! encoding=utf-8
"""
# 绝对导入，相对导入以及from __future__ import absolute_import作用
先了解一个场景： 自己有个文件也叫string 和python中（包括2.x和3.x） bulti-in中的string重名
    那么导入string是导入的那个呢？ 是自己定义的那个
    怎么可以使用bulti-in的那个呢？ absolute_import 能解决这个问题吗？ 不能， 无论是否有这一句， 都是用的自定义的（python2 python3 都是）

# link(https://docs.python.org/3/reference/import.html)
# link(https://www.jianshu.com/p/04701cb81e38)
相对导入只能在包（package）中执行
# link(https://segmentfault.com/q/1010000000458562)
"""
from __future__ import absolute_import
import string
print(string.ascii_uppercase)
from string import ascii_lowercase
print(ascii_lowercase)
print(string.ascii_lowercase)
