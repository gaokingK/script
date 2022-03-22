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

def filter_num(num_list):
    b = [x for x in filter(lambda b: b != 2, num_list)]
    print(b)



if __name__ == '__main__':
    filter_num([1, 2, 3, 4])
