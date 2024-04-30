"""
# 多线程和多进程
# link
    - 信号量：https://www.cnblogs.com/renpingsheng/p/7202818.html
# 并行计算：https://python-parallel-programmning-cookbook.readthedocs.io/zh-cn/latest/chapter2/
"""
from multiprocessing import Process
import time

def f(name):
    while True:
        time.sleep(0.5)
        print('hello', name)

def demon():
    while True:
        time.sleep(1)
        print("run")

"""
To: 信号量
- 见learn_IPC.md
s1.acquire() 信号量值-1
s1.release() 信号量值+1
可以一直release()这样信号量会一直加1

查看信号量值使用semaphore._value
"""
def learn_semaphore():
    import time
    import threading

    s1=threading.Semaphore(5)	#添加一个计数器，值为5

    def foo():
        s1.acquire()	#计数器获得锁
        time.sleep(2)	#程序休眠2秒
        print("ok",time.ctime())
        s1.release()	#计数器释放锁


    for i in range(20):
        t1=threading.Thread(target=foo,args=())	#创建线程
        t1.start()	

"""
#TO 线程锁
lock = threading.Lock()
def thread_safe_function():
    lock.acquire()
    try:
        pass
    finally:
        lock.release()
for i in range(5):
    thread = threading.Thread(target=thread_safe_function)
    thread.start()
"""


if __name__ == '__main__':
    # p = Process(target=f, args=('bob',))
    # p.start()
    # #p.join()
    # demon()

    learn_semaphore()
