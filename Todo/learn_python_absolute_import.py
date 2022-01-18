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
# sys.chdir()带来的问题
    - 使用os.path.abspath(path)时会根据工作目录 与 path做拼接，如果path是以/开头的绝对路径时没有问题，但如果是相对路径（相对与执行脚本的路径，而不是脚本里面改到的路径）就会出问题
    [root@localhost detect]# python3 BalckWhite/src/BalckWhite.py -i  video2image/test_5_second/ 后面的路径是相对于detect的，而BalckWhite.py里把路径改到了detect/src/ 那么abspath获取test_5_scend时就会得到 xxx/detect/src/video2image/test_5_scend
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

"""
To: 修改sys.path然后再import
# src 执行命令 python3 BalckWhite.py
"""
"""
[root@localhost src]# tree
.
├── analyzer
│   ├── analyzer.py
│   ├── detection_analyzer.py
│   ├── detection_predictor.py
│   └── fake_analyzer.py
├── BalckWhite.py
├── dataset
│   ├── dataset_from_images.py
│   ├── dataset.py
│   ├── fake_dataset.py
│   └── __init__.py
├── predict
│   ├── balckwhite_screen.c
│   ├── balckwhite_screen_check.cpython-37m-aarch64-linux-gnu.so
│   ├── balckwhite_screen.py 
│   ├── build
│   │   └── temp.linux-aarch64-3.7
│   │       └── balckwhite_screen_check.o
│   ├── InputAndOutput.py
│   └── setup.py

9 directories, 27 files
"""
# BalckWhite.py 
"""
from from predict.balckwhite_screen import main as bs_main
"""
# balckwhite_screen.py 
"""
sys.path.insert(0, 'dataset')
from dataset_from_images import DatasetFromFiles
# from dataset.dataset_from_images import DatasetFromFiles 这样的话会报dataset not moudle， 下面加__init__.py也不行

sys.path.insert(0, 'processor')
from processor import Processor

sys.path.insert(0, 'analyzer')
from detection_predictor import DetectionPredictor
from balckwhite_screen_check import blackwhite_screen

os.environ["CUDA_VISIBLE_DEVICES"] = "3"
print(f"sys.path: {sys.path}\n \bwork_path:{os.getcwd()}")
# sys.path: ['predict', 'analyzer', 'processor', 'dataset', '/root/detect/BalckWhite/src', '/root/archiconda3/lib/python37.zip', '/root/archiconda3/lib/python3.7', '/root/archiconda3/lib/python3.7/li
b-dynload', '/root/archiconda3/lib/python3.7/site-packages']
# work_path:/root/detect/BalckWhite/src

"""
# 但是换个目录再运行python3 BlackWhite.py就会出错, 这是因为在src下运行时， src在path中，然后找predict时会因为src找到，然后src下面的包又在predict中找到了
# 好像也不是这个原因， 应该时将predict 与getcwd（）的结果拼接, 所以应该把这几个文件的绝对路径添加进去
"""
[root@localhost detect]# python3 BalckWhite/src/BalckWhite.py -i  video2image/test_5_secon
Traceback (most recent call last):
  File "BalckWhite/src/BalckWhite.py", line 3, in <module>
    from predict.balckwhite_screen import main as bs_main
  File "/root/detect/BalckWhite/src/predict/balckwhite_screen.py", line 11, in <module>
    from dataset_from_images import DatasetFromFiles
ModuleNotFoundError: No module named 'dataset_from_images'
# 改成这样
在BlackWhite.py里
prefix_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(prefix_path, "dataset"))
sys.path.insert(0, os.path.join(prefix_path, "predict"))
sys.path.insert(0, os.path.join(prefix_path, "processor"))
sys.path.insert(0, os.path.join(prefix_path, "analyzer"))

"""