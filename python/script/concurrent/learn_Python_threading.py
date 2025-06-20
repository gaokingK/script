import threading
import functools
import time
from concurrent.futures import ThreadPoolExecutor,wait,FIRST_COMPLETED, as_completed
"""
TO: threading.local()
link: https://www.liaoxuefeng.com/wiki/1016959663602400/1017630786314240
# 线程隔离
- threading.local() 解决的是在同一个线程对象里的不同函数之间需要共享某些变量的问题，不用把所有的变量写进参数里，可以保存在local()对象中，不是解决不同线程之间需要共享某些状态的场景
- 如果创建一个全局字典，然后把每个变量自己的值保存在以thread为键的对象中也可以做到
"""
# 线程隔离
def isolation_thread():
    if not hasattr(thread_global, "value1"):
        thread_global.value1 = {}
    thread_global.value1.update({threading.current_thread().name: threading.current_thread().name})
    print(thread_global.value1)
    isolation_thread_after()

def isolation_thread_after():
    thread_global.value1.update({"222": 333})
    print(thread_global.value1)

"""
TO:线程的一些方法
获取当前运行线程名称和数量 threading.enumerate()
0:<_MainThread(MainThread, started 11816)>
1:<Thread(jjw_0, started daemon 18104)>
2:<Thread(jjw_1, started daemon 980)>
"""
"""
TO: 线程池的使用
link:https://www.cnblogs.com/goldsunshine/p/16878089.html
funture 对象：https://docs.python.org/zh-cn/3/library/asyncio-future.html
标准库为我们提供了concurrent.futures 模块，它提供了 ThreadPoolExecutor (线程池)和 ProcessPoolExecutor (进程池)两个类。
该模块通过 submit 返回的是一个 future 对象，它是一个未来可期的对象，通过它可以获取某一个线程执行的状态或者某一个任务执行的状态及返回值：

主线程可以获取某一个线程（或者任务的）的状态，以及返回值。
当一个线程完成的时候，主线程能够立即知道。
- 提交任务的方式
    - submit(fn, p)  fn是函数，p作为函数的参数 
        - submit 返回的是一个 future 对象，它是一个未来可期的对象，通过它可以获取某一个线程执行的状态或者某一个任务执行的状态及返回值：
        - submit过程是不阻塞的，即使[t_pool.submit(some_func, p,) for p in parm_list] param_list 大于线程池中线程个数，也会立即返回（submit只是一个提交动作，提交后由内部对象调度运行这些待运行的任务到线程池中）
        - 即使后面没有获取结果，也会等到所有子线程运行完后才结束
    - map(fn, *iterables, timeout=None) 对iterables中的每个元素使用fn方法，然后按iterables的顺序返回fn完成后的返回值，这个过程时阻塞的，
- 获取结果的方式
    - submit提交的
        - submit会返回future对象，可以通过future对象来获取任务执行状态和返回值 future_obj.result() 是阻塞的，需要任务执行完成后才会返回
            - 可以直接对all_task中的future调用result获取结果，也可以先获取状态然后在调用
    - map提交的 map返回的就是按传入参数的次序处理后的结果

- 获取执行状态的方式
    - wait方法 wait(fs, timeout=None, return_when=ALL_COMPLETED)
        - fs: 表示需要执行的序列
        - timeout: 等待的最大时间，如果超过这个时间即使线程未执行完成也将返回
        - return_when：表示wait返回结果的条件，默认为 ALL_COMPLETED 全部执行完成再返回，可选 FIRST_COMPLETED(是第一批线程池中执行队列中第一个执行完成的，并不一定是第一个添加的)
        - wait方法并不是获取返回值的，而是获取任务执行状态的
    - as_completed() 方法是一个生成器，在没有任务完成的时候，会一直阻塞。当有某个任务完成的时候，会 yield 这个任务，就能执行 for 循环下面的语句，然后继续阻塞住，循环到所有的任务结束。
        - yield任务的时候返回的是future对象
- 添加回调函数
    - future.add_done_callback(callback, *, context=None)
    - 调用 callback 时，Future 对象是它的唯一参数。如果该回调函数有多个参数，可以传入用其他参数生成的偏函数
"""
def some_func(param1):
    print(f"start with {param1}")
    time.sleep(param1)
    print(f"complete with {param1}")
    return param1

def callback(future,arg1):
    print(f"回调函数：函数{arg1}执行结果{future.result()}")

"""
TO: 多线程写

"""

"""
TO: daemon=True threading.Thread(target=update_data, daemon=True)中的daemon参数有什么作用
在 Python 的 threading.Thread 中，daemon 参数的作用是决定线程是否为 守护线程（Daemon Thread）。

什么是守护线程（Daemon Thread）？
守护线程的生命周期受主线程的影响：

非守护线程（daemon=False，默认值）：主程序不会在非守护线程完成之前退出，必须等待所有非守护线程结束后，主线程才能终止。主程序会等到 worker 完成（其实是无限循环）后，才会退出。这可能会导致主程序被无限阻塞。
守护线程（daemon=True）：主程序在结束时会强制终止所有守护线程，而不必等待守护线程完成。
daemon=True 的作用
将 daemon=True 设置为守护线程意味着：

后台运行：守护线程在主程序运行期间一直运行，但主程序终止后，守护线程会被立即停止，而不会等其完成。
非阻塞主程序退出：即使守护线程仍在运行，主程序也可以退出。主程序结束时，守护线程会被强制停止

守护线程的典型应用
实时更新任务：
如实时更新热力图、绘图线程等，可设置为守护线程，避免因主程序退出而阻塞。
后台任务：
例如日志记录、定时器等辅助功能线程，主程序退出时不需要等待其完成。

非守护线程的适用场景
关键任务：
必须完成的任务，例如文件下载、数据保存等。
需要明确完成的任务：
程序退出前需要确保所有线程完成工作。
"""

"""
TO: 使用线程池时 # max_worker的设置
- 虽然线程是轻量级的，但设置太大仍然可能带来 性能下降：
问题	原因
上下文切换频繁	操作系统要频繁调度，CPU 时间浪费
内存占用高	每个线程都占用一定栈空间，线程越多越占内存
竞争资源	如果任务操作 I/O 或共享变量，线程过多会产生争用
反而变慢	线程数太多可能导致程序比串行还慢（尤其是 CPU 密集型任务）
- 如果是 I/O 密集型任务（网络请求、磁盘 I/O 等）：
可以设置得相对 大一些（如几十或更多），因为线程大多在等 I/O。
- 如果是 CPU 密集型任务（数学计算、加密、图像处理等）：
不建议使用线程池，而是使用 ProcessPoolExecutor
如果硬要用线程池，max_workers 一般设置为：
import os
max_workers = os.cpu_count() or 4  # 推荐 = CPU 核心数
- 实践 cpu_count=8
with ThreadPoolExecutor(max_workers=10) as executor: # 25s
with ThreadPoolExecutor(max_workers=16) as executor: # 12s
with ThreadPoolExecutor(max_workers=18) as executor: # 11s
with ThreadPoolExecutor(max_workers=20) as executor: # 9.5s
with ThreadPoolExecutor(max_workers=21) as executor: # 10.97
with ThreadPoolExecutor(max_workers=23) as executor: # 12s

- 基本上为cpu_count的2倍 如果IO占用比较大就多一点


"""
if __name__ == '__main__':
    # TO: threading.local()
    test_dict={}
    processes = []

    thread_global = threading.local()
    for i in range(5):
        t = threading.Thread(target=isolation_thread)
        # t = threading.Thread(target=isolation_thread, args=(test_dict,))
        processes.append(t)
        t.start()

    for t in processes:
        t.join()

    #TO: 线程池的使用
    # all_task = []
    # parm_list =[1,2,3,4,5]
    # with ThreadPoolExecutor(max_workers=2,thread_name_prefix="jjw") as t_pool:
    #     # 使用map
    #     # 如果timeout小于线程执行需要的时间，会报错concurrent.futures._base.TimeoutError
    #     # for result in t_pool.map(some_func, parm_list, timeout=2):
    #     #     pass

    #     # 使用submit
    #     all_task=[t_pool.submit(some_func, p,) for p in parm_list[::-1]] # submit后就开始执行了 会全部提交
    #     time.sleep(10)# 已经提交的子线程仍然后台并行在执行
    #     # results = [f.result() for f in all_task] # 使用future对象获取返回
    #     # wait(all_task,timeout=10, return_when=FIRST_COMPLETED)

    #     # for f in as_completed(all_task): # 使用as_completed
    #     #     print(f.result())

    #     # 添加回调函数
    #     # all_task=[t_pool.submit(some_func, p,) for p in parm_list[::-1]]
    #     # for f in all_task:
    #     #     # f.add_done_callback(callback)
    #     #     f.add_done_callback(functools.partial(callback,arg1=2))
    #     pass
    # print("主进程结束")
