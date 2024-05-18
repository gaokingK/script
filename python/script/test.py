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

# def filter_num(num_list):
#     b = [x for x in filter(lambda b: b != 2, num_list)]
#     print(b)
import math


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
    # filter_num([1, 2, 3, 4])
    print(isPalindrome(121))
