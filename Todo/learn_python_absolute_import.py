#! encoding=utf-8
"""
# 绝对导入，相对导入以及from __future__ import absolute_import作用; 解决模块找不到的原因和几种方法
先了解一个场景： 自己有个文件也叫string 和python中（包括2.x和3.x） bulti-in中的string重名
    那么导入string是导入的那个呢？ 是自己定义的那个
    怎么可以使用bulti-in的那个呢？ absolute_import 能解决这个问题吗？ 不能， 无论是否有这一句， 都是用的自定义的（python2.7 python3.x 都是）

有说python2.4及之前的版本会因absolute_import而不同: https://blog.csdn.net/caiqiiqi/article/details/510508006
from __future__ import absolute_import 引入了绝对导入这个特性
    pkg/
    pkg/init.py
    pkg/main.py 
        main里import string
    pkg/string.py
    在python2.4及之前 python 会查找当前目录下是否有string, 这里就找到了, 然后你导入的就是自定义的string, 但是就无法使用bulit-in中的了, 这时引入绝对导入这个特性就可以解决这个问题,
    import string 导入bulti-in string; from pkg import string导入自定义的string

绝对导入和相对导入
    从上面这个例子可以看到, import xx 这种特性是绝对引入,  from pkg import xxx 是相对导入
    相对导入只能在包（package）中执行


# link(https://docs.python.org/3/reference/import.html)
# link(https://www.jianshu.com/p/04701cb81e38)
# link(https://segmentfault.com/q/1010000000458562)

# 解决模块找不到的原因和几种方法 http://c.biancheng.net/view/4645.html
# import moudle 中搜索模块的顺序
   3. 输入脚本的目录
   4. PYTHONPATH中的目录
   5. Python默认的安装路径中
   6. 实际上，解释器由 sys.path 变量指定的路径目录搜索模块，该变量初始化时默认包含了输入脚本（或者当前目录）， PYTHONPATH 和安装目录。这样就允许 Python程序了解如何修改或替换模块搜索目录。
# 有些模块需要显示导入
"""


from __future__ import absolute_import
import string
print(string.ascii_uppercase)
from string import ascii_lowercase
print(ascii_lowercase)
print(string.ascii_lowercase)

"""
To: 有些模块需要显示导入
"""
def test_explicit_import():
    import logging # 这样导入config会报错
    import logging.config # 必须这样导入才不报错
    logging.config.fileConfig() 
