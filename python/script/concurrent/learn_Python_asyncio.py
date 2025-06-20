"""
# asyncio（异步IO)是用来编写并发代码的库，使用async/await语法
# link:
- https://docs.python.org/zh-cn/3/library/asyncio.html
- 深入理解Python异步编程(中) https://zhuanlan.zhihu.com/p/677693677
- https://v3u.cn/a_id_208
- https://www.liujiangblog.com/course/python/83
# 
- asyncio作为多个高性能python异步框架的基础，包括网络和网站服务、数据库连接、分布式任务队列
- 是构建IO密集型的最佳选择
- 提供高层级的API用来完成：同步并发代码、并发运行多个python协程并对执行过程实现完全的控制、控制子进程、执行网络IO和IPC、通过队列实现分布式任务
- 是基于协程做异步IO编写单线程并发脚本的基础设施，核心组件有事件循环、任务、协程、未来对象(Future)以及其他一些扩充和辅助性质的模块。
# 注意
- await语句必须在async 语句定义的函数里使用
- a coroutine function: an async def function;
- a coroutine object: an object returned by calling a coroutine function.
- Task对象被用来同时调用多个coroutine function,如果要想让多个函数并行，需要使用 asyncio.create_task(func_name(param_list))创建一个task，然后使用await task来完成

- async await yield语句
    - 再最开始的python版本中，携程需要使用到yield语句来完成将执行权由当前函数交回到调用者的手中，这和生成器有些相似，毕竟二者都使用了yield关键字，但协程和生成器是两种东西：协程消费数据，生成器生产数据
    - 在 Python 中调用协程对象1的 send() 方法时，第一次调用必须使用参数 None, 这使得协程的使用变得十分麻烦。因此，我们可以借助 Python 自身的特性来避免这一问题，比如，创建一个装饰器：
    - 当我们用这个装饰器装饰协程时，每次创建新的协程对象它就会自己帮我们调用 send(None), 由于这个装饰器使用的很频繁，因此，从 Python3.5 开始，这个装饰器就演变为了关键字 async.
    - 对于关键字 await 来说，我们可以把它看做 yield from 的替代，而 yield from 的作用大致和下面的循环相同：
    await 等价于 yield from
    yield from iterator 等价于：
    for x in iterator:
        yield x
- 事件循环
    - 事件循环可以看成一个死循环，循环中不断检查所有事件列表
    - 事件循环取出协程执行后，如果协程未执行完，会将协程再次放到事件/协程队列中。
    - 应用开发者通常应当使用高层级的 asyncio 函数，例如 asyncio.run()，应当很少有必要引用循环对象或调用其方法。
"""
import asyncio
import time
"""
To: hello_world
1. 使用async语句定义函数
2. 在函数中使用await语句定义要io的代码
3. 使用asyncio.run(func_name(para_list))调用async定义的函数

"""

import asyncio

async def say_after(delay, content):
    # 下面的两个await 语句会顺序执行
    await asyncio.sleep(delay)
    await asyncio.sleep(delay)
    print(content)

async def main():
    # await say_after(2, "hello")
    # await say_after(5, "hello") #用时7秒
    # 通过print(asyncio.current_task()) 会发现当前运行的任务是这个main()函数
    # create_task是创建任务，并将任务加入事件循环，然后执行下一行代码 注意任务并不会立即开始执行
    task1 = asyncio.create_task(say_after(2, "function sleep 4s complete"))
    task2 = asyncio.create_task(say_after(1, "function sleep 2s complete")) # 用时4秒
    time.sleep(15)# awit的时候事件循环中任务才开始执行，是按加入的顺序执行的，不是awit的顺序，比如这里即使await task2 也是执行的task1

    await task1 # 这里会等待task1执行完成后才执行下一行代码（如果事件循环中有别的任务在执行，会等别的任务执行后再执行await的任务，等await执行的任务完成后再返回）
    # res = await task1 # 可以获取返回值
    await task2

"""
TO: 使用事件循环
"""
def useEventLoop():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.gather(
            say_after(2, "hello"),
            say_after(2, "hello")
        ))
    finally:
        loop.close()

"""
TO: async 是个装饰器
"""
def async_copy(func):
    def warpper(*args, **kws):
        generator = func(*args, **kws)
        generator.send(None)
        return generator
    return warpper

"""
TO: 在async函数中运行
# 在异步环境中运行同步函数又不想阻塞主线程，可以用线程池包装：

resp = await asyncio.to_thread(client.DescribeInstanceTypeConfigs, req)
"""
if __name__ == "__main__":
    b_time=time.time()

    asyncio.run(main()) # 用时4秒
    
    # useEventLoop() # 用时4秒

    print(f"span time{time.time()-b_time}")
