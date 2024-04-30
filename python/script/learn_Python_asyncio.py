"""
# asyncio（异步IO)是用来编写并发代码的库，使用async/await语法
# link:
- https://docs.python.org/zh-cn/3/library/asyncio.html

# 
- asyncio作为多个高性能python异步框架的基础，包括网络和网站服务、数据库连接、分布式任务队列
- 是构建IO密集型的最佳选择
- 提供高层级的API用来完成：同步并发代码、并发运行多个python协程并对执行过程实现完全的控制、控制子进程、执行网络IO和IPC、通过队列实现分布式任务
# 注意
- await语句必须在async 语句定义的函数里使用
- a coroutine function: an async def function;
- a coroutine object: an object returned by calling a coroutine function.
- Task对象被用来同时调用多个coroutine function,如果要想让多个函数并行，需要使用 asyncio.create_task(func_name(param_list))创建一个task，然后使用await task来完成
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
    await asyncio.sleep(delay)
    await asyncio.sleep(delay)
    print(content)

async def main():
    # await say_after(2, "hello")
    # await say_after(5, "hello") #用时7秒

    task1 = asyncio.create_task(say_after(2, "hello"))
    task2 = asyncio.create_task(say_after(2, "hello")) # 用时4秒
    await task1
    await task2


if __name__ == "__main__":
    b_time=time.time()
    asyncio.run(main())

    print(f"span time{time.time()-b_time}")