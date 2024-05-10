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

"""
局部变量和全局变量可以同名，但同名的话就用不了全局变量了，参照下面的
"""
"""
TO: # 值引用 地址引用 python中的变量在一个地方改变另外一个地方是否受影响
看是可变变量还是不可变变量，可变变量会受影响，不可变变量不会受影响
而且可变变量只有在改变的情况下才会影响原来的变量，赋值的就不会影响, （也不绝对看下面的To）
extend_conf(all_cluster_conf_dict[key])  这样即使不用返回值接受，也会改变的
"""
# a.py
a_dic = {"key": "hhh"}
a_str = "a_str"
# b.py
from a import a_dic, a_str


def change_dict_obj_test(a_str_value, **kwargs):
    a_dic.update(kwargs)
    # a_dic = kwargs # 这个就不会影响
    a_str = a_str_value + a_str # 不能写a_str 但同名的话就用但同名的话就用不了全局变量了，因为这个a_str是局部变量，还没有定义，所以就会报错
# c.py
from a import a_dic, a_str
from b import change_dict_obj_test


def test_change_dict_obj():
    for i in range(10):
        print(a_dic, a_str)
        change_dict_obj_test("a_%s" % str(i), **{"a_%s" % str(i): "hhh"})
        print(a_dic, a_str)


if __name__ == '__main__':
    test_change_dict_obj()

"""
To: 赋值也改变
"""
class ClusterConf(object):
    def __init__(self, conf_dict):
        conf_dict = self.convert_time(conf_dict)
        self.op_morning = conf_dict["op_morning"]
        self.op_settle = conf_dict["op_settle"]

def update_conf():
    # 补充配置
    cluster_conf = {}
    cluster_conf["amoduleset"] = list(set(cluster_conf.get("amoduleset")))
    cluster_conf["op_morning"]["prestart"] = cluster_conf["op_flow"]["end"]
    cluster_conf["op_settle"]["prestart"] = cluster_conf["op_night"]["end"]  # op_night.end
    cluster_conf["op_next"]["prestart"] = cluster_conf["op_morning"]["end"]  # op_morning.end
    cluster_conf["op_flow"]["prestart"] = cluster_conf["op_morning"]["end"]
    cluster_conf["op_night"]["prestart"] = cluster_conf["op_settle"]["end"]
    cluster_conf1 = ClusterConf(copy(cluster_conf))  # 只有这样才不会改变

"""
TO: 把字典里面的值传给a，改变a, 原来的也会改变
"""
def and_diff_cluster_conf(cluster_list):
    """
    合并不同cluster配置，用于多cluster overviewwx计算
    """
    res_conf = clusters_conf[cluster_list[0]]
    res_conf = copy(clusters_conf[cluster_list[0]]) # 这样才不会改变

    for cluster in cluster_list:
        # active_module_set = list(set(res_conf.active_module_set) | set(clusters_conf[cluster].active_module_set))
        res_conf.active_module_set = list(set(res_conf.active_module_set) | set(clusters_conf[cluster].active_module_set))
        res_conf.active_module_set = [1]
        pass

clusters_conf = init_conf()
and_diff_cluster_conf(["cluster1", "cluster2"])
