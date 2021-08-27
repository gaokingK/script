#!/usr/bin/python3
from functools import reduce


def calc_add(*args):
    sum = reduce(lambda x1, x2: x1 + x2, args)
    print("sum is {}".format(sum))


if __name__ == '__main__':
    calc_add(1, 2, 3)

    number = [1, 2, 3]
    calc_add(*number)
