#!/usr/bin/python3
"""
实现单例的几种方式以及销毁单例的方法
[单例的作用](link：https://www.cnblogs.com/shenbuer/p/7724091.html):
    单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问, 从而方便对实例个数的控制并节约系统资源, 如资源管理器
"""
from weakref import WeakValueDictionary

# 单例元类


class Singleton(type):
    _instances = WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class A(metaclass=Singleton):
    pass


# 单例装饰器
def singleton(cls,):
    """
    不知为什么方法二和方法三都没有用,只有在打了断点的调试模式下时候才有用
    :param cls:
    :return:
    """
    # _instances = {}
    _instances = WeakValueDictionary()
    # tips: 直接换会有错, 因为_instance[cls]=** 等号右边的子句中创建出来的类实例并没有任何一个强引用,
    # 只有 WeakValueDictionary() 中的一个弱引用，于是触发了垃圾回收机制，所以字典实际上是空的，
    # 于是我们后面的 return 语句自然就会报错 KeyError。 解决办法如下

    def _get_instance(*args, **kwargs):
        if cls not in _instances:
            # 方法一
            # _instances[cls] = cls(*args, **kwargs)
            # 方法二
            # cls_instance = cls(*args, **kwargs)
            # _instances[cls] = cls_instance
        # return _instances[cls]
            # 方法三
            return _instances.setdefault(cls, cls(*args, **kwargs))
    return _get_instance


"""
删除单例
如何彻底删除单例, 可以借助weakValueDictionary(), 这是一个弱引用类型
link: https://blog.csdn.net/qq_41967784/article/details/119351353
"""


@singleton
class A:
    def __del__(self):
        print("__del__ run")


def debug_del_singleton():
    # To 彻底删除单例对象
    a = A()
    print("a id is {}".format(id(a)))
    del a
    b = A()
    print("b id is {}".format(id(b)))
    # 会发现两个id一样, 这是因为del的实例还在单例装饰器中的字典中被存在, 而这种引用是强引用, 所以实例所指向的数据对象不会被回收
    # 可以借助弱引用来实现丢弃此处的引用来达到真正销毁的效果 即将字典变成WeakValueDictionary()来实现
    c = [x for x in range(10)]
    print(id(c))
    del c
    c = [x for x in range(10)]
    print(id(c))

# def singleton(cls):
#     _instance = WeakValueDictionary()
#
#     # @wraps(cls)
#     def single(*args, **kwargs):
#         if cls not in _instance:
#             cls_instance = cls(*args, **kwargs)
#             _instance[cls] = cls_instance
#         return _instance[cls]
#     return single


if __name__ == '__main__':
    debug_del_singleton()
