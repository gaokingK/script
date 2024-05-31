# from functools import reduce

# strict_mode =False
# if strict_mode:
#     la = lambda a,b: a and b
# else:
#     la = lambda a,b: a or b
#
# exec_mode = lambda a,b: a and b if strict_mode else lambda a,b: a or b
#
# a = [None, False, True]
# print(reduce(la, a))
# print(reduce(exec_mode, a))
import asyncio  
import os
import threading
import time
import random
from  multiprocessing import Process, cpu_count
import copy
# The optional argument gives the initial value for the internal
# counter;
# it defaults to 1.
# If the value given is less than 0, ValueError is raised.
semaphore = threading.Semaphore(0)

def consumer():
    semaphore.release()
    print("consumer is waiting.")
    # Acquire a semaphore
    # The consumer have access to the shared resource
    print("Consumer notify : consumed item number %s " % item)

def producer():
    global item
    time.sleep(0.5)
    # create a random item
    item = random.randint(0, 1000)
    print("producer notify : produced item number %s" % item)
        # Release a semaphore, incrementing the internal counter by one.
    # When it is zero on entry and another thread is waiting for it
    # to become larger than zero again, wake up that thread.
    semaphore.release()

def printNumber(x):
    print(x)


async def say_after1(delay, content):
    print("say_after1 begin")
    await asyncio.sleep(delay)
    print(content)

async def say_after2(delay, content):
    print("say_after2 begin")
    await asyncio.sleep(delay)
    print(content)

async def main():
    # await say_after(2, "hello")
    # await say_after(5, "hello")
    task1 = asyncio.create_task(say_after1(2, "hello1"))
    print("main_pause1")
    print(asyncio.get_event_loop())
    print(asyncio.get_running_loop())
    task2 = asyncio.create_task(say_after2(3, "hello2"))
    print("main_pause2")
    print(asyncio.get_event_loop())
    print(asyncio.get_running_loop())
    time.sleep(1)
    print("main_pause3")

    await task1

    print("main_pause4")
    time.sleep(5)
    print("main_pause5")

    await task2
# bb = """10.201.81.142、10.201.81.143"""
# cc = " OR ".join([f"`ip`!=\"{x.strip()}\"" for x in bb.split("、") if x])
# print(cc)


def cpu_intensive_task(s):
    for i in range(10000000*s):
        n=10000*4444444*s
    print("%s结束了" % s)


balance = 0  

async def change_it_without_lock(n):  

    global balance  

    balance = balance + n  
    balance = balance - n  

    print(balance)  




if __name__ == '__main__':
    b_time=time.time()

    a = [{"3":2}, {"4":5}]
    for item in a:
        item.update({"7":9})
    print(a)
    # loop = asyncio.get_event_loop()  

    # res = loop.run_until_complete(  
    #     asyncio.gather(change_it_without_lock(10), change_it_without_lock(8),  
    #                 change_it_without_lock(2), change_it_without_lock(7)))  
    # print(balance)

    # asyncio.run(main())

    # for i in range (0,3):
    #     t1 = threading.Thread(target=producer)
    #     t2 = threading.Thread(target=consumer)
    #     t1.start()
    #     t2.start()
    #     t1.join()
    #     t2.join()
    #     print(semaphore._value)
    # print("program terminated")



    # print(cpu_count())
    # processes = []
    # for i in range(cpu_count()):
    #     # p=Process(target=cpu_intensive_task, args=(i,))
    #     p = threading.Thread(target=cpu_intensive_task, args=(i,))
    #     p.start()
    #     processes.append(p)
    # time.sleep(20)

    # for i in processes:
    #     i.join()
    #     print("join")
        




    print(f"span time{time.time()-b_time}")
    pass
