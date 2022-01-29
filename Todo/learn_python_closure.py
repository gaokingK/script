"""
python 闭包原理
link: https://www.cnblogs.com/yssjun/p/9887239.html

什么是闭包
1. 有嵌套函数，（c中不能嵌套函数）
2. 内部函数引用外部函数的局部变量
3. 外部函数的返回值必须是内部函数


闭包的延时绑定
link: http://ask.athena.huawei.com/sw/question/546931052707311616/
局部变量和全局变量：
    python中，非局部变量绑定的是空间，而不是值本身.
    闭包函数引用了外部作用域的自由变量m, 只有在内部函数（闭包函数）被调用的时候才会搜索变量m的值, 所以返回闭包时牢记一点：返回函数不要引用任何循环变量，
    或者后续会发生变化的变量。
    在debug_generate_func() 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
    如何理解“只有在内部函数（闭包函数）被调用的时候才会搜索变量m的值”
        可以定义一个函数，f = lambda a: a*b; 这里的函数 f，其中有一个未知的变量 b，我们其实并没有定义它，但是我们依然能得到 f，并不会因为 f 里面有东西未定义就报错，这就表明了 f 在生成的时候并没有去执行函数里面的内容
        而真正运行的时候才会报错f(2)
延时绑定
    Python的延迟绑定其实就是只有当运行嵌套函数（闭包函数）的时候，才会引用外部变量i，不运行的时候，并不会去找i的值
    匿名函数中的i并不是立即引用后面循环中的i值的，而是在运行嵌套函数的时候，才会查找i的值，这个特性也就是延迟绑定

# 一种说法
延时绑定？不就是 lazy evaluation 吗（迫真）
那“闭包的延时绑定特性”不就是 function 的 partial evaluation 吗（迫真）
背后的原理
延迟绑定怎么知道绑定的外层函数的局部变量？，在栈中的局部变量在函数后退出后就销毁了, 那有什么办法可以不立即这么做？


"""


"""
To: 闭包中引用可变参数
"""
def debug_generate_func():
    func_list = []
    for i in range(4):
        def func():
            j = i  # 这样是无效的
            return j * j
        func_list.append(func)
        # 如果一定要引用循环变量？方法2是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
        # def func(a):
        #     def g():
        #         return a * a
        #     return g
        # func_list.append(func(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    # 另外一种原理一样的形式
    # func_list = [lambda i = i: i * i for i in range(4)]  # i也可以命名为j
    # 添加了一个i=i后，就给匿名函数，添加了一个默认参数，而python函数中的默认参数，是在python 解释器遇到def(i=i)或lambda 关键字时，就必须初始化默认参数，此时for i in range(4)，每循环一次，匿名函数的默认参数i，就需要找一次i的引用，i=0时，第一个匿名函数的默认参数值就是0，i=1时，第二个匿名函数的默认参数值就是1，以此类推
    func_list = [lambda j=i: j * i for i in range(4)]  # i是引用的外部参数， h是外部传的参数，用来固定值，输出想要的结果
    for func in func_list:
        print(func())


"""
To: 延时绑定的变种
"""
def debug_bind():
    func_list = [lambda j=i: j * i for i in range(4)]
    for func in func_list:
        # print(func())
        print(func(3)) # 这就是因为只有当运行嵌套函数（闭包函数）的时候，虽然前一次传给他的参数已经保存下来了（通过传给另外一个参数），但这里又传了一个新值。


"""
To: 延时绑定的原理
运行完再看
- 闭包空间就是一个元组，元素为cell对象, 每个cell对象又包含闭包内容和其它的内容
- 每个lambda函数引用外部函数的局部变量name和i这才形成了闭包
- 我在局部函数中把i值最后改成100,可以看到最后所有闭包空间中的int都是100了, 这个很合理，因为我改的是
    局部变量，你引用了i(这里我感觉既不是值传递也不是引用传递, 更不是共享传参, 就好像我盯着i这个标签一样，你怎么变，我最终值就怎么变)
- 可以看到multipliers()调用之后就会出现延迟绑定, 即我所有匿名函数(这里是否是匿名函数没有关系), 最终闭包空间的所有值都是100
- 延迟绑定只是一个表面现象
"""
def principle():
    name = "-------------"
    i = 0
    ret = list()
    for _ in range(3):
        lambda_func = lambda x: i * x + (print(name) is None) - 1
        # 可能是作为区分输出用的，不是，是作为外部函数的局部变量让lambda_func去引用的
        # lambda_func = lambda x: i * x
        ret.append(lambda_func)
        print(lambda_func.__closure__)
        print("the closure variable i: {}".format(hex(id(lambda_func.__closure__[0].cell_contents))))
        i += 1
    i = 100

    return ret


def debug_principle():
    for item in principle():
        print("the lambda function output: {}".format(item(2)))
        print("闭包中的cell对象组成的元组成： {}".format(item.__closure__))
        print("取出闭包空间中的整数: {}".format(item.__closure__[0].cell_contents))

    for number in list([0, 1, 2, 100]):
        print(hex(id(number)))


if __name__ == '__main__':
    # debug_generate_func()
    # debug_bind()
    debug_principle()
