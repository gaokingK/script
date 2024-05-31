import threading

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


if __name__ == '__main__':
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
