# If you need to import additional packages or classes, please import here.
# 不用暴力
import time
def split(start, num):
    # 组合的个数
    combination = 0
    if num <= 0:
        return combination
    if num == 1:
        combination +=1
        return combination
    else:
        combination+=1
        #for i in range(1, num):
        # 去重方法，对于a+b 对b从a开始拆分
        for i in range(start, num):
            if i + i -1 >= num:
                return combination
                break
            else:
                if i == 1:
                    combination += split(i, num - i)
                else:
                    combination += split(i, num - i )
        return combination
                
                
def func():
    # please define the python3 input here. 
    # For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    while True:
        try:
            one_mouse = int(input())
            start_time = time.perf_counter()
            print(split(1, one_mouse))
            print("spend time %0.3fs" %(time.perf_counter()-start_time))
        except EOFError:
            break
            
            
if __name__ == "__main__":
    func()
