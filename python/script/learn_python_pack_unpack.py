"""
打包(封装）、解包（解构）、序列解包的高级用法
打包：  定义 函数的时候用
    * 在函数定义中，收集所有的 位置参数到一个新的元组，并将这个元组赋值给变量args
    ** 在函数定义中，收集所有的 关键字参数传递给一个字典，并将这个字典赋值给变量kwargs
解包：  调用 函数的时候使用
    * 在函数调用中，* 能够将元组或者列表解包成一个一个的 参数
    ** 在函数调用中， ** 会以键/值的形式解包一个字典，使其成为一个一个的 关键字参数

序列解包： https://blog.csdn.net/yilovexing/article/details/80576788
"""


def func(*args, **kwargs):
    print(f"可变参数: {args}, type is {type(args)}") if args else ''
    print(f"关键字参数: {kwargs}, type is {type(kwargs)}") if kwargs else ""
    kwargs.clear()
    print(f"关键字参数: {kwargs}, type is {type(kwargs)}") if kwargs else ""


def debug_unpack():
    # * 的使用方法
    # func(1, 2, 3)
    # func(*[1, 2, 3])
    # func(*{1, 2, 3})
    # func(*{"a": "b"})
    # # 如果可变参数是一个嵌套的容器会怎么样
    # func(*[[1, 2], [1, 2]])

    # ** 的使用方法
    # func(key_1="value_1", key_2="value_2")
    # 比较下面两个的不同
    func({"key_1": "value_1", "key_2": "value_2"})
    func(**{"key_1": "value_1", "key_2": "value_2"})
    func(id=7, id2=5)

    # 解包的是副本，不会影响真的值, 元组是不可变的
    # args = [1, 2, 3]
    # kwargs = {"key_1": "value_1", "key_2": "value_2"}
    # func(*args, **kwargs)
    # print(kwargs)


"""
序列解包
"""
def get_geek_unpack():
    s = 'ABCDEFGH'
    while s:
        x, *s = s
        print(x, s)


if __name__ == '__main__':
    debug_unpack()
    # get_geek_unpack()
