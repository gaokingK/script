"""
dir: https://www.runoob.com/python/python-func-dir.html
dir() 获取当前范围内的变量,方法和定义的类型列表;
带参数时, 返回参数的属性方法列表, 如果参数包含__dir__则该方法被调用, 如果没有,dir()将最大限度的收集参数信息
"""


class Base:
    bb = ''

    def __init__(self):
        self.bbb = ""
        print(set(dir(self)) - set(dir(Base)))
        print(set(dir(self.__class__)) - set(dir(Base)))
        # print SubClass' new attribues' names ('aa' and 'bb' for example)


class SubClass(Base):
    def __init__(self):
        self.aaa = ''
        super(SubClass, self).__init__()

    aa = ''


def debugger():
    """
    dir(Base) 获取的Base属性只有bb 是不是只有类属性?
    dir(self) 获取的属性只有实例的属性
    dir(self.__class__) 获取的属性只有实例的类属性
    :return:
    """
    foo = SubClass()


if __name__ == '__main__':
    debugger()
