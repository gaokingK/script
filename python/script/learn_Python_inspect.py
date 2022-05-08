"""
inspect 模块用来收集python对象的信息,可以获取类或者函数的参数, 源码; 获取栈,解析帧;对对象进行类型检查等
收集对象的信息:
    inspect.getmember(obj)
"""
import inspect
import sys
from functools import wraps
from python.script.singleton import Singleton
from wingman import Wingman


"""
获取对象的信息
inspect.getmember(obj, [predicate]) 可选参数是一个预置条件, 可以以此为条件对obj的属性进行过滤, 类似filter
误区: 获取的是obj的属性, 如果把当前帧传进去,并不能获取当前帧中的变量, 而是会获取到frame对象的属性
和obj.__dict__是否一样?
"""
def debug_getmember():
    # To: inspect.getmembers 分别获取类实例/变量/方法或函数 的成员 在调试中看
    # 获取类实例 能获取实例的私有属性
    w = Wingman()
    print("显示获取的w.__dict__:[%s]" % w.__dict__)
    mems = inspect.getmembers(Wingman())
    mems = [x for x in filter(lambda x: "dict" in x[0], mems)]
    print("getmember 获取w.__dict__:[%s]" % mems)
    m = inspect.getmembers(Wingman(), lambda x: inspect.ismethod(x) or inspect.isfunction(x))

    # 获取变量, 只能获取这个str的方法,如help(str) 而不能获取var的内容
    # var = "this is wingman str!"
    # m = inspect.getmembers(var)

    # 获取方法的 并不能获取到方法的变量
    # m = inspect.getmembers(Wingman().introduce)
    print("ok")


"""
获取栈的信息
inspect.stack()获取当前的栈信息
inspect.currentframe() 当前帧 也可以通过sys._getframe来获取
inspect.currentframe().f_back 当前帧的下一帧调用者
inspect.frameinfo(inspect.currentframe()) 获取帧的信息
exercise: 获取当前函数的调用栈
"""
def get_call_stack():
    """
    获取当前函数的调用栈
    :return:
    """
    # who = inspect.getframeinfo(inspect.currentframe().f_back.f_back)[2]

    func_frames = []
    current_frame = inspect.currentframe()
    while hasattr(inspect.getframeinfo(current_frame), "function"):
        func_frames.append(inspect.getframeinfo(current_frame)[2])
        current_frame = current_frame.f_back
        if not current_frame:
            break
    print(func_frames)


def debug_get_call_stack(a):
    mark_a = "fuc"
    print(a)
    get_call_stack()


"""
exercise
在被装饰的方法中获取装饰器的变量, 会不会因为变量超出范围而无法获取?
能获取到, 但是获取不到装饰器里使用的外部变量,如 self.func_stack就获取不到
"""
# 1. 创建装饰类
class Ex(metaclass=Singleton):
    def __init__(self):
        self.func_stack = []

    def get_call_stack_dec(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_frame = inspect.currentframe()
            while hasattr(inspect.getframeinfo(current_frame), "function"):
                self.func_stack.append(inspect.getframeinfo(current_frame)[2])
                current_frame = current_frame.f_back
                if not current_frame:
                    break
            print(self.func_stack)
            func(*args, **kwargs)
        return wrapper


# 2. 准备装饰A().func_a 顺便测试下单例
class A(metaclass=Singleton):

    def __init__(self):
        self.name = 5
        # self.add_protery()

    def func_a(self):
        var1 = "a"
        m = inspect.currentframe().f_back
        print("func_a")

    # def add_protery(self):
    #     setattr(self, "more", wingman)


# 3. 动态添加装饰器
def debug_setattr():
    """
    To: 获取装饰器中的变量
    即获取Ex().get_call_stack_dec()中的func_stack
    """

    global a, b
    a, b = A(), A()
    ex = Ex()
    mems = inspect.getmembers(a)
    print(mems)

    for name, addr in mems:
        if name == "func_a":
            print("绑定了")
            setattr(a, name, ex.get_call_stack_dec(addr))

    # 获取实例a所有方法
    mems = inspect.getmembers(b, lambda x: inspect.ismethod(x))
    print(mems)
    # mems = [x[0] for x in filter(lambda x: "__" not in x[0], mems)]
    # print("valid: " + str(mems))
    for name, addr in mems:
        if name == "func_a":
            print("绑定了")
            setattr(b, name, ex.get_call_stack_dec(addr))
    # 获取b的方法,由于是单例, 所以绑定后的方法变成了function 所以这里看不到
    mems = inspect.getmembers(b, lambda x: inspect.isfunction(x) or inspect.ismethod(x))
    print(mems)
    a.func_a()


"""
exercise：
目录
- learn__python_inspect.py class AA在这里获取子类的实例中的属性
- learn_python_inspect_wingman1 classB(AA) 子类
- learn_python_inspect_wingman2 B的实例 有私有属性__doc__
调试:
在get_child_class_proerty 中打断点,在wingman2里debug
"""


class AA:
    """
    define class AA
    """
    def __init__(self):
        self.name = "AA"
        self.get_child_class_property()

    def get_child_class_property(self):
        """
        define func get_child...
        :return:
        """
        parm1 = "pass"
        a = inspect.stack()
        # 比较两者不同
        # current_frame_info = inspect.getframeinfo(inspect.currentframe())
        # current_frame = inspect.currentframe()

        #
        outter_farme = inspect.currentframe().f_back.f_back.f_back
        sys_frame = sys._getframe()
        pass

"""
inspect.stack() 很多frame 如果在调试的时候增加这个表达式， 打断点的模块会在中部，不会在两端, 而如果把这个写在程序中，第一个frame就是当前的
里面的frame里的frame>f_locals有在pycharme中显示的变量；frame>stacks是调用栈
但是不知道怎么获取stack这个变量
"""


if __name__ == '__main__':
    # debug_getmember()
    # debug_get_call_stack(4)
    debug_setattr()

    print("ok")
