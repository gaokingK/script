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
import threading
import time
import random

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

import asyncio

async def say_after(delay, content):
    await asyncio.sleep(delay)
    await asyncio.sleep(delay)
    print(content)

async def main():
    # await say_after(2, "hello")
    # await say_after(5, "hello")
    task1 = asyncio.create_task(say_after(2, "hello"))
    task2 = asyncio.create_task(say_after(2, "hello"))
    await task1
    await task2
bb = """
10.201.81.142、10.201.81.143、10.201.81.144、10.201.81.145、10.201.81.148、10.201.81.14、10.201.81.15、10.201.81.56、10.201.81.57、10.201.81.58、10.201.97.37、10.201.97.38、10.201.97.39、10.201.97.41、10.201.97.42、10.201.97.46、10.201.97.47、10.201.97.48、10.201.97.52、10.201.97.53、10.201.97.54、10.201.97.57、10.201.97.58、10.201.97.59、10.231.81.191、10.231.81.192、10.231.81.193、10.231.81.194、10.231.81.195、10.231.81.196、10.231.82.153、10.231.82.154、10.231.97.36、10.231.97.37、10.231.97.38、10.231.97.39、10.231.97.41、10.231.97.43、10.231.97.44、10.231.97.45、10.231.97.46、10.231.97.47、10.231.97.48、10.231.97.49、10.231.97.52、10.231.97.56、10.231.97.57、10.231.97.58、10.231.97.59、10.201.34.73、10.231.1.71、10.232.107.58、、10.201.34.73、10.201.81.14、10.201.81.142、10.201.81.143、10.201.81.144、10.201.81.145、10.201.81.148、10.201.81.15、10.201.81.56、10.201.81.57、10.201.81.58、10.201.97.37、10.201.97.38、10.201.97.39、10.201.97.41、10.201.97.42、10.201.97.43、10.201.97.46、10.201.97.47、10.201.97.48、10.201.97.49、10.201.97.52、10.201.97.53、10.201.97.54、10.201.97.57、10.201.97.58、10.201.97.59、10.231.1.71、10.231.81.191、10.231.81.192、10.231.81.193、10.231.81.194、10.231.81.195、10.231.81.196、10.231.81.62、10.231.81.65、10.231.82.153、10.231.82.154、10.231.97.36、10.231.97.37、10.231.97.38、10.231.97.39、10.231.97.41、10.231.97.42、10.231.97.43、10.231.97.44、10.231.97.45、10.231.97.46、10.231.97.47、10.231.97.48、10.231.97.49、10.231.97.52、10.231.97.54、10.231.97.56、10.231.97.57、10.231.97.58、10.231.97.59"""
# cc = " OR ".join([f"`ip`!=\"{x.strip()}\"" for x in bb.split("、") if x])
cc = ",".join([f"\"{x.strip()}\"" for x in bb.split("、") if x])
print(cc)
if __name__ == '__main__':
    # for i in range (0,3):
    #     t1 = threading.Thread(target=producer)
    #     t2 = threading.Thread(target=consumer)
    #     t1.start()
    #     t2.start()
    #     t1.join()
    #     t2.join()
    #     print(semaphore._value)
    # print("program terminated")
    b_time=time.time()
    asyncio.run(main())

    print(f"span time{time.time()-b_time}")
