#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from operator import *
import re


def calculator(a, b, k):
    """
    两个数加、减、乘、除、幂，5种运算的简易计算器

    :param a: 数字
    :param b: 数字
    :param k: 操作算法
    :return: 计算结果
    """
    try:
        return {
            '+': add,
            '-': sub,
            '*': mul,
            '/': truediv,
            '**': pow
        }[k](a, b)
    except Exception as e:
        print(e)


def calc_ave():
    """
    输出该句段中英文单词长度的平均值
    """
    try:
        word = input()
        if re.compile(r'[^A-Za-z ]+').findall(word):
            print("Please check the words again!!!")
            exit(0)
        regx = re.compile(r'\w+')
        word_list = regx.findall(word)
        ave = 0
        for per_word in word_list:
            ave = ave + len(per_word)
        print("%.2f" % float(ave/len(word_list)))
    except Exception as e:
        print(e)


def check_continue():
    """
    判断给定的整数n能否表示成连续的m(m>1)个正整数之和，如：
    15=1+2+3+4+5
    15=4+5+6
    15=7+8
    """
    num = int(input())
    if num & (num - 1) == 0:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    # calculator()
    # calc_ave()
    check_continue()
