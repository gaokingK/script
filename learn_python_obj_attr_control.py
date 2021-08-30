#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 对 Python对象属性控制的相关方法 __getattr__、__getattribute__、__setattr__、__delattr__的介绍
# link1 https://blog.csdn.net/lilong117194/article/details/80111803

# link2 https://blog.csdn.net/qq_27825451/article/details/102457160?utm_
# medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7
# Edefault-4.base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-4.base


class Animal:
    run = True


class Dog(Animal):
    fly = False

    def __init__(self, age):
        self.age = age

    def __getattr__(self, item):
        """
        可以用来定义 访问的属性不存在 时的行为
        注意，这里就不能调用父类的同名方法
        """
        print("call __getattr__, args[{}]".format(item))
        if item == 'height':
            return 70
        elif item == 'weight':
            return 30
        # 如果不想定义未知属性时的行为，那么访问的时候也不会报错
        # super().__getattr__(item) 会报错

    def __getattribute__(self, item):
        """
        这个方法又被称为 属性拦截器（或者为属性绑定行为） 因为python在访问属性或者方法的时候， 都会调用这个方法
        我们可以自定义这个方法，比如加上查看权限，或者打印日志
        但是要注意最后调用父类的这个方法，防止没有返回
        """
        print("call __getattribute__, args[{}]".format(item))
        # 对不同属性定义绑定行为
        if item == "age":
            print("haha")
        # 这里其实也能定义未知属性或者方法的行为，属性没有问题，但是方法会有问题
        if item == "method":
            print("这是没有定义的属性或者方法")
        # 注意不能使用.来访问对象的属性，因为这样的访问会调用__getattribute__, 会造成无限递归; 可以用super()来避免这个问题
        return super(Dog, self).__getattribute__(item)
        # return self.item 这样是不行的item这里是个字符串 相当于 b="age" dog.b是访问不到的
        # return self.age 这样就会造成循环引用的问题 这里就知道为什么说这个getattribute是通用性的了，
        # 因为访问每个属性都会进到这个魔术方法里来

    def __setattr__(self, key, value):
        """
        可以借助他来自定义某个属性的赋值行为，不管这个属性是否存在，都可以对任意属性的任何变化都定义单独的规则
        使用中要防止无限递归
        使用中要区分对象属性和类属性(? 应该是注意设置对象属性不会对类属性生效的意思吧？）
        """
        print("call __setattr__, args[{}]".format((key, value)))
        super().__setattr__(key, value)

    def __delattr__(self, item):
        """
        用于定义删除对象属性时的行为
        使用时要注意防止无限递归
        """
        print("call __delattr__, args[{}]".format(item))
        super().__delattr__(item)

    def sound(self):
        return "wang wang"


def respective_attr():
    # 查看各自的属性
    dog = Dog(1)
    print("dog.__dict__: {}".format(dog.__dict__))
    print("Dog.__dict__: {}".format(Dog.__dict__))
    print("Animal.__dict__: {}".format(Animal.__dict__))
    # 可以看到dog.__dict__中只有一个age属性，并没有fly属性
    # Python 中对象的属性具有层次性（实例对象、类对象、基类对象），属性在哪个对象上定义，属性就会出现在哪个对象的__dict中
    # 但是如果赋值，就会有
    dog.fly = False
    print("dog.__dict__: {}".format(dog.__dict__))


def getattr_and_getattribute():
    """
    通过下面的输出可以看出来， __getattribute是实例对象查找属性或者方法的入口，然后才会根据一定的
    规则去在各个__dict__中查找相应的属性值或者方法对象，如果有就触发绑定的行为，没有找到会调用__getattr__
    """
    # 实例化对象dog
    dog = Dog(1)
    # 访问dog对象的age属性, 属性拦截器
    print('dog.age:', dog.age)
    # 访问dog对象的fly属性
    print('dog.fly:', dog.fly)
    # 访问dog对象的sound方法
    print('dog.sound:', dog.sound())
    # 对于未存在的方法或者属性
    print(dog.weight)
    print(dog.dd)
    print(dog.dd())
    """
    __getattribute__称之为“属性、方法拦截器”，不管是属性还是方法，第一步就是先访问__getattribute__；
    而__getattr__仅仅针对的是属性，不针对方法，即访问未存在的方法的时候依然还是会报错。
    __getattribute__针对的是访问已经存在的（属性和方法）；__getattr__针对的是访问未存在的（属性）。
    __getattribute__和__getattr__虽然针对每一个访问的key，一定要有对应的返回值（参见前文），
    但是返回的东西却不是一样的，即__getattribute__返回父类的__getattribute__函数，
    而__getattr__返回我希望为未知属性设置的那个值或者是异常信息。
    """
    # 对于在__getattrbute__里定义的属性或者方法
    # print(dog.method)
    # print(dog.method())


def debug_setattr():
    dog = Dog(1)
    dog.age = 2
    dog.agg2 = 2  # 正常情况下就可以这样


def debug_delattr():
    # __delattr__只能够删除 已经存在的、实例属性，对于不存在的属性和类属性(因为它是属于类的)是不能够删除的
    dog = Dog(1)
    del dog.age
    del dog.fly
    print(dog.__dict__)


if __name__ == '__main__':
    # respective_attr()
    # getattr_and_getattribute()
    # debug_setattr()
    debug_delattr()
