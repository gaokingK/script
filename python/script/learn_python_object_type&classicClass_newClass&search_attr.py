#!/usr/bin/env python
# -*- coding: utf-8 -*-
# type 和 object的关系是怎样呢？
# link: https://www.cnblogs.com/MY0213/p/8735440.html
# link2： https://www.cnblogs.com/busui/p/7283137.html

# Python是动态语言还是静态语言，是强类型还是弱类型
# link：https://blog.csdn.net/qq_34685213/article/details/102943769

# 新式类和经典类：
# https://www.cnblogs.com/blackmatrix/p/5630515.html
# 不是很准 https://blog.csdn.net/fragmentalice/article/details/85163662

# 属性的访问、属性的查找顺序
# link：https://blog.csdn.net/lilong117194/article/details/80111803
"""
type 和 object的关系是怎样呢？
# 他们之间的关系很鸡和蛋之间的关系，现有谁没法说，是共生的关系，没法同时出现
# 在面向对象体系中存在两种关系:
    继承关系：可以查看__bases__属性
    类型实例关系： 如fuck是一个小狗，可以查看__class__属性,也可以type()查看
object是继承关系的顶端，所有数据类型的顶端都是他，type也是；type是类型实例关系的顶端，所有对象都是他的实例，object也是
object是一个type；type是一种object

python中的对象关系一共有三种：
1）元类 type是所有元类的父类
2）object 他是所有类的父亲，大部分我们使用的类型都是在这个
3）实例 是对象关系链的末端，不能被子类化和实例化
"""

"""
python是动态语言，是强类型的
什么是动态语言和静态语言：
    他们的判别的标准在于 类型检查 发生的阶段：如果发生在编译阶段，就是静态语言，反之如果发生在运行阶段，就是动态类型语言。
那我们怎么区别动态语言和静态语言呢？
    我们也不知道检查发生在那个阶段，毕竟我们只写代码，类型检查其实就是查看变量的类型，静态语言因为在编译阶段就需要知道变量的类型，
    所以我们必须显示的声明变量的类型 如果java中 float f = 0.5
Python是动态语言
静态语言只需要编译器，动态语言只需要解释器？对吗 ----------------------no

强类型和弱类型？
    强类型语言有更强的类型检查机制，表达式计算中会做严格的类型检查
    弱类型语言允许各种变量类型之间做一些运算 如javascript
"""

"""
新式类、经典类的区别？
怎么定义？
    python2及以前版本才有经典类，python中只有新式类
    由任意内置类型（object这些）派生出来的类，只要一个内置类型在类树的某个位置，都属于新式类
    不由任意类型派生出来的类，为经典类
    class AAA(object):
        新式类
        pass
    class AAA():
        经典类
        pass
# MRO（方法和属性的搜索顺序）不同， 多重继承是才有这种区别：
    经典类似从左到右，深度优先
    新式类是从左到右，不是广度优先， 而是C3算法，某些情况下和广度优先结果一样
    可以用classname.mro()来查看
# 经典类mro的问题
- mro是方法解析顺序（Method Resolution Order）用来确定python在多重继承的情况下找到正确的方法或者属性
- 经典类mro存在的问题是在多重继承的情况下会存在结果不直观、某些基类会在搜索路径中出现多次，某些基类会被意外跳过的情况
    - 某些基类可能会被访问多次： 经典类的 MRO 中，当遍历到某个类的基类时，并不会检查这个基类是否已经被访问过。这样，如果多个子类继承自同一个基类，在 MRO 遍历中，这个基类的方法可能会被执行多次，这可能会导致一些意料之外的副作用，尤其是在涉及到状态变更时。
    - 某些基类会被意外地跳过： 如果继承结构中存在重叠，DFS 的算法可能会在到达某个应当被调用的基类之前就已经返回，这意味着这个基类的方法会被跳过，导致它的某些功能不会按预期执行。
- 举例说明结果不直观 j
"""
"""
TO:举例说明结果不直观 
"""
class A:
    def save(self):
        print("Save method from A")

class B(A):
    pass

class C(A):
    def save(self):
        print("Save method from C")

class D(B, C):
    pass
class E(C, B):
    pass

d_instance = D()
d_instance.save() 
# 我们可能期望输出来自类 C 的 save 方法，因为按照常理我们会查看第一父类 B，由于 B 没有定义自己的 save 方法，我们会转向下一个父类 C。然而，因为经典类使用的是深度优先搜索，实际上，它将继续在 A 中搜索，从而找到基类A的方法

e_instance = E()
e_instance.save() 
# 虽然D/E基类是一样的，可是由于dfs的查找规则，会导致查找到的方法和父类的顺序有直接关系
# 新式类的mro（）结果虽然也和第一父类的顺序有关系，但只会在第一父类间有区别，祖类之间是没有区别的
# 新式类的mro()
# D.mro()
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# E.mro()
# [<class '__main__.E'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

"""
属性访问的优先规则：属性一般存储在__dict__中，但是在对象属性、类属性、基类属性中是怎样一个查找规则呢
1. 查找属性的第一步是搜索基类列表type(b).mro, 知道找到属性的第一个定义，将该属性的值赋值给desc；
2. 判断desc的类型，可以为数据描述符、非数据描述符、普通属性、未找到等
3. 若是数据描述符，返回调用desc.get(b, type(b))的结果，结束。否则下一步
4. 若是非数据描述符、普通属性、未找到等，就查找实例b的实例属性即b.dict, 找到就返回并结束执行，否则进行下一步
5. 如果未在b.dict中找到，就重新回到desc值的判断上：
    a. 若为非数据描述符，就调用desc.get(b, type(b)),返回结果，结束
    b. 若为普通属性，直接返回结果并结束执行
    c. 若desc为空（未找到），抛出AttributeError，结束
"""
