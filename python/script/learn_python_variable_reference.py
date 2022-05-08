"""
python变量引用相关 了解这两个错误的概念就可以了, 这个文章写的不好,有很多不清晰容易让人困惑的措辞
link: https://www.cnblogs.com/yssjun/p/9873689.html
两种错误: UnboundLocalError/NameError
    NameError: 变量在哪里都没有找到
    UnboundLocalError: 如果这个变量引用了尚未绑定的local变量, 会raise; 属于NameError的子类
可见性与绑定
    在python中想要引用一个变量, 这个变量必须是可见且绑定的, 并不像c或者c++, 声明并定义变量后就可以使用
"""

# 代码展示
"""
print(a) # NameError

my_function()  # NameError
def my_function():
    pass
    

def outer_func():
    loc_var = "local variable"
    def inner_func():
        loc_var += " in inner func"  # UnboundLocalError
        return loc_var
    return inner_func

clo_func = outer_func()
clo_func()
"""

"""
可见性与绑定
绑定操作:
    import 声明
    作为函数的参数
    类或者函数的定义
    赋值操作(赋给别人还接受别人的赋值?)
    for 循环的首标
    异常捕获中as子句的赋值
code block: 作为一个unit被执行的一段python文本, 例如一个module/def/class 
local variable: 变量在一个code block中被绑定, 这个变量便是这个block中的一个local variable 
global variable: 变量在module中被绑定
free variable: 变量在一个block中被引用, 但不是在这里被定义的, 这个变量就是
scope: 暂且认为他是变量可见性的范围, 
Free variable是一个比较重要的概念，在闭包中引用的父函数中的局部变量是一个free variable，而且该free variable被存放在一个cell对象中
"""
# 又一个例子
import sys

def add_path(new_path):
    path_list = sys.path

    if new_path not in path_list:
        import sys
        sys.path.append(new_path)
add_path('./')