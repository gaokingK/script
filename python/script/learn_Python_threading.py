import threading
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
    thread_global.value1={threading.current_thread().name: threading.current_thread().name}
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
    - 调用 callback 时，Future 对象是它的唯一参数。
"""
def some_func(param1):
    print(f"start with {param1}")
    time.sleep(param1)
    print(f"complete with {param1}")
    return param1

def callback(future):
    print(f"回调函数：函数执行结果{future.result()}")

"""
TO: 多线程写

"""

if __name__ == '__main__':
    # TO: threading.local()
    # test_dict={}
    # processes = []

    # thread_global = threading.local()
    # for i in range(5):
    #     t = threading.Thread(target=isolation_thread)
    #     # t = threading.Thread(target=isolation_thread, args=(test_dict,))
    #     processes.append(t)
    #     t.start()

    # for t in processes:
    #     t.join()

    #TO: 线程池的使用
    all_task = []
    parm_list =[1,2,3,4,5]
    with ThreadPoolExecutor(max_workers=2,thread_name_prefix="jjw") as t_pool:
        # 使用map
        # 如果timeout小于线程执行需要的时间，会报错concurrent.futures._base.TimeoutError
        # for result in t_pool.map(some_func, parm_list, timeout=2):
        #     pass

        # 使用submit
        # all_task=[t_pool.submit(some_func, p,) for p in parm_list[::-1]] # submit后就开始执行了 会全部提交
        # time.sleep(5)# 已经提交的子线程仍然在执行
        # results = [f.result() for f in all_task] # 使用future对象获取返回
        # wait(all_task,timeout=10, return_when=FIRST_COMPLETED)

        # for f in as_completed(all_task): # 使用as_completed
        #     print(f.result())

        # 添加回调函数
        all_task=[t_pool.submit(some_func, p,) for p in parm_list[::-1]]
        for f in all_task:
            f.add_done_callback(callback)
        pass
