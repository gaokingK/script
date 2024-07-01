import multiprocessing
from multiprocessing import Queue
import threading
import time

"""
TO: 多进程通信
1. 子进程不能访问主进程的的变量，子线程可以
2. 使用队列(同样是在主进程中声明的变量，普遍变量不能被子进程访问，队列变量就可以) 不是这样的，使用队列时也必须将队列作为参数传入
3. 使用server process
既然上面三种方式都证明了子进程要使用主线程中的变量，都要这些变量作为参数传入子进程，那这三种方式有区别吗
    - 有区别，第一种方式虽然能让子进程访问主进程的变量，但是子进程不能修改，修改的是变量的复制
    - 而二三种方法修改的是一个对象，他们的区别就是队列和server process的区别
"""
def task_func(l):
    # print(f", {var1}")
    l.append("5")


def task_use_queue(queue_obj):
    print(f"from queue get:{queue_obj.get()}")

def f(i, d, l):
    d[i] = '1'
    l.reverse()

if __name__ == "__main__":
    l_time = time.time()
    # TO: 多进程通信1
    # var1 = "hhh"

    # TO: 多进程通信2
    queue = Queue()
    p_list = []
    l = list()
    for i in range(5):
        p = multiprocessing.Process(target=task_func, args=(l,))
        # p = multiprocessing.Process(target=task_use_queue, args=(queue,))
        # p = threading.Thread(target=task_func, args=(i,))
        p.start()
        p_list.append(p)

    for p in p_list:
        queue.put("a")
        p.join()
    print(f"多线程处理后的l:{l}")
    
    # TO: 多进程通信3
    # with Manager() as manager:
    # # with open("./tmp.json") as f:
    #     p_list = []
    #     # d= dict()
    #     # l = list(range(10))
    #     d = manager.dict()
    #     l = manager.list(range(10))
    #     for i in range(4):
    #         p = Process(target=f, args=(i,d, l))
    #         p.start()
    #         p.join()
    #         p_list.append(p)

    #     for p in p_list:
    #         p.join()
    #     print(d)
    #     print(l)
    print(f"span time: {time.time() - l_time}")

    
