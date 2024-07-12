"""
TO：了解协程的yield实现方式时，对yield语句有疑问，进一步了解下生成器（generator）
"""

# 参考：https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128
# 惰性求值
# generator保存的是算法, 每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误 

# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator(注意，定义generator 有多种方法)

# generator 也是可迭代对象, 即可以使用for去遍历， 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

# 因为我们的函数并没有像通常意义那样返回。return隐含的意思是函数正将执行代码的控制权返回给函数被调用的地方。
# 而"yield"的隐含意思是控制权的转移是临时和自愿的，我们的函数将来还会收回控制权。

# send()的作用 见后面 link: https://blog.csdn.net/xibeichengf/article/details/78989971


def simple_generator():
    a = [x for x in range(10) if x % 2 == 0]
    print(f"type's of a is {type(a)}")
    a = (x for x in range(10) if x % 2 == 0)
    print(f"type's of a is {type(a)}")


def func_generator(max):
    n = 0
    a, b = 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "done"


def yield_return(num=0):
    """
    yield语句的返回值
    因为赋值语句从等号右边开始
    # https://blog.csdn.net/qq_28915777/article/details/108186963
    :param num:
    :return:
    """
    while True:
        y = yield num  # y 的赋值等同与下面一句(不使用send的情况下）
        # s = print("1") s 的值为None
        print("y: {}".format(y))


"""
TO: send() 和next() 的区别
- 都可以调用生成器运行一次 
- send()可以向生成器发送给一个值，这个值被yield 语句等号左边的值接受，next() 其实是send(None)
"""
def simple_generator_send(num=2):
    while True:
        num *= 2
        # send(parm) 的作用是在yield语句执行后的赋值语句里对等号左边的参数赋值，赋值为parm
        # 相当于next()语句执行后又传一个值

        # 注意：在generator刚初始化好，还没被用过时，send(parm)只能send(None), 否则就会遇到错误：
        # TypeError: can't send non-None value to a just-started generator
        # 这是为什么呢？generator 不是执行完yield语句才暂停吗，这样的话下一步就是赋值了，为什么不能赋值呢，难道第一次没有执行yield
        # 语句吗？ 确实是的，观察普通的generator（即yield 的左边没有等号的）发现初始化的时候也没有返回yield 右边的变量
        # 为什么没有执行呢？这就很弱智了，想一想，如果一个函数被初始化后（fun1 = func )，那么他会被立即执行一遍嘛？显然不会的
        # It is done to 'start' the generator. It is just something that needs to be done.
        # It makes some sense when you think about it since the first time you call send() the generator has not
        # reached the keyword yield yet.
        # 当你第一次调用生成器时，它还没有开始执行，因此没有挂起的 yield 表达式可以接收发送的值。
        # 第一次调用生成器时，使用 send(None) 启动生成器并使其运行到第一个 yield 表达式处。

        # send(None) 和 next()的作用是一样的
        # yield num  # 这样使用send(parm) 发送的参数不会影响next()的结果, 即无效
        num = yield num  # 这样有效

"""
TO: yield from obj 这个obj必须是iterable对象，不能是普通对象，作用和yield一样的
简化了生成器的嵌套，如果没有yield 只能通过for循环来一次次调用子生成器；yield from 可以将外部调用者send()过来的值转到子生成器中，并且调用者和子生成器之间的通信也会变得复杂
协程中最好使用yield from 这样不仅可以使用语句提供的双向通道，可以随心所欲的在进程中传递数据，而不用关系数据是否可以被yield
"""
def subgen():
    while True:
        # 这种写法必须send(1)后调用next()一次
        x = yield 
        yield x+1
        # 这种写法不用 但x的定义有问题
        # x = yield x+1

def gen():
    yield from subgen()

def main_3():
    g = gen()
    next(g)                # 驱动生成器g开始执行到第一个 yield
    retval = g.send(1)     # 看似向生成器 gen() 发送数据
    print(retval)          # 返回2
    g.throw(StopIteration) 

if __name__ == '__main__':
    # simple_generator()

    # 斐波拉契数列
    # for i in func_generator(5):
    #     print(i)

    # 获取return 返回的值
    # fi = func_generator(4)
    # while True:
    #     try:
    #         print(next(fi))
    #     except StopIteration as e:
    #         print(e.value)
    #         break

    # 测试yield的返回值

    # a = yield_return(0)
    # 这样输出和下面的输出好像不一样 其实是一样的，不过是y: None 先全部输出，可以理解为print中的内容必须全部被计算出来
    # print("{0:*^4} \t {1:*^4} \t {2:*^4}".format(next(a), next(a), next(a)))
    # print(next(a))
    # print(next(a))
    # print(next(a))

    # 了解send的作用
    # s = simple_generator_send()
    # print(s.send(None))

    # yield from
    main_3()
    pass
