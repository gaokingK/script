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
from  multiprocessing import Process, cpu_count
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
# cc = ",".join(list(set([f"\"{x.strip()}\"" for x in bb.split("、") if x])))
# print(cc)
def cpu_intensive_task(s):
    for i in range(10000000*s):
        n=10000*4444444*s
    print("%s结束了" % s)
def minExtraChar(s: str, dictionary: list) -> int:
    n = len(s)
    # mapping = [-1] * n
    mapping = [[] for _ in range(n)]
    valid_map = []
    for word in dictionary:
        start = 0
        for _ in range(s.count(word)):
            valid_map.append(word)
            try:
                index = s.index(word, start) - 1 + len(word)
            except Exception as e:
                print(word)
                raise e
            start = index + 1
            # mapping[index] = max(len(word), mapping[index])
            mapping[index].append(len(word))
    def dfs(i):
        if i<0:
            return 0
        if mapping[i]:
            # return min(dfs(i-mapping[i]), dfs(i-1) + 1)
            return min(min([dfs(i-mapping[i][x]) for x in range(len(mapping[i]))]), dfs(i-1) + 1)
        else:
            return dfs(i-1)+1
    # print(valid_map)
    print(mapping)
    return dfs(n-1)
    # return mapping

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        import math
        length = int(math.log(x, 10)) + 1
        L = length - 1
        for i in range(length // 2):
            if x // 10 ** L != x % 10:
                return False
            x = (x % 10 ** L) // 10
            L -= 2
        return True

if __name__ == '__main__':
    s=["leetscode", "iamaboynot", "dwmodizxvvbosxxw", "ecolloycollotkvzqpdaumuqgs","sdosi"]
    dictionary = [["leet","code","leetcode"],["ama","ia","ot","yno"],["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"],["flbri","uaaz","numy","laper","ioqyt","tkvz","ndjb","gmg","gdpbo","x","collo","vuh","qhozp","iwk","paqgn","m","mhx","jgren","qqshd","qr","qpdau","oeeuq","c","qkot","uxqvx","lhgid","vchsk","drqx","keaua","yaru","mla","shz","lby","vdxlv","xyai","lxtgl","inz","brhi","iukt","f","lbjou","vb","sz","ilkra","izwk","muqgs","gom","je"],['d', 'dos', 't', 'fgyr', 'i', 'si', 'hhbz', 'ihg']]
    for s,d in zip(s,dictionary):
        if s == "sdosi":
            print(minExtraChar(s,d))


    # for i in range (0,3):
    #     t1 = threading.Thread(target=producer)
    #     t2 = threading.Thread(target=consumer)
    #     t1.start()
    #     t2.start()
    #     t1.join()
    #     t2.join()
    #     print(semaphore._value)
    # print("program terminated")
    # b_time=time.time()
    # asyncio.run(main())
    # print(f"span time{time.time()-b_time}")


    # print(cpu_count())
    # processes = []
    # for i in range(cpu_count()):
    #     # p=Process(target=cpu_intensive_task, args=(i,))
    #     p = threading.Thread(target=cpu_intensive_task, args=(i,))
    #     p.start()
    #     processes.append(p)
    # # time.sleep(20)
    # for i in processes:
    #     i.join(timeout=1)
    #     print("join")
        
    pass
