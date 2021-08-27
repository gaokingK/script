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
if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    #p.join()
    demon()
