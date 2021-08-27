import random
import time


def bubble_sort(cln):
    length = len(cln)
    for i in range(1, length):
        flag = True
        for j in range(0, length-i):
            if cln[j] > cln[j+1]:
                cln[j], cln[j+1] = cln[j+1], cln[j]
                flag = False
        if flag:
            break


if __name__ == '__main__':
    collection = random.sample([x for x in range(20)], 10)
    print("未排序:{}".format(collection))
    l_time = time.process_time()
    bubble_sort(collection)
    r_time = time.process_time()
    print("已排序:{}".format(collection))
    print("耗时:{}".format(r_time - l_time))
