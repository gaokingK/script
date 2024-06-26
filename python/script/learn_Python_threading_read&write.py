import os,sys
import json
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
import glob
import pandas as pd
import threading

def read_file(file):
    print(file)
    file = os.path.join(os.path.dirname(__file__), file)
    if not os.path.isfile(file):
        return 
    with open(file, 'r', encoding="utf-8") as f:
        data = f.readlines()
    return data

def get_result(future):
    df.append(future.result())

def write2f(f_obj, parm1):
    lock.acquire(blocking=False)
    for i in range(10000):
        f_obj.writelines([f"hhh{parm1}\n"])
    lock.release_lock()



if __name__ == "__main__":
    start_time = time.time()
    lock = threading.Lock()
    df = []
    # 使用线程池
    # with ThreadPoolExecutor(23) as executor: # 创建 ThreadPoolExecutor 
    #     # 提交任务方式1
    #     # future_list = [executor.submit(read_file, file) for file in os.listdir(os.path.dirname(__file__))] 

    #     # 提交任务方式2
    #     future_list = [executor.submit(read_file, file) for file in glob.glob(pathname=os.path.join(os.path.dirname(__file__),"*.py"))] 

    
    # # 获取返回值方法1
    # for future in as_completed(future_list):
    #     future.add_done_callback(get_result)
    # 获取返回值方法2
    # for future in as_completed(future_list):
    #     result = future.result() # 获取任务结果
    #     # df = df.append(result,ignore_index=True)

    # 串行读取
    # for file in glob.glob(pathname=os.path.join(os.path.dirname(__file__),"*.py")):
    #     df.append(read_file(file))

    # 多线程写
    t_list = []
    with open("tmp.json", "w") as f:

        for i in range(100):
            t = threading.Thread(target=write2f, args=(f,i))
            t.start()
            t_list.append(t)
        for t in t_list:
            t.join()

        # 线程池
        # with ThreadPoolExecutor(max_workers=10) as pool:
        #     future_list = [pool.submit(write2f, f) for i in range(100)]
        # 顺序写
        # for i in range(100):
        #     write2f(f)
    print(time.time()-start_time)
