#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# 每M个人出局一个
# n个小朋友 m个一下
# ******************************开始写代码******************************


def L(n, m):
    child_list = set(range(1, n + 1))
    index = 1
    while len(child_list) > 1:
        # c = child_list.pop()
        # if index % m != 0:
        #     child_list.add(c)
        # child_list.add(99)
        # print(child_list)
        # index+=1
        #
        new_child = []
        for _, each in enumerate(child_list):
            if (index) % m != 0:
                new_child.append(each)
            index += 1
        print(new_child)
        child_list = new_child
    return child_list.pop()


# ******************************结束写代码******************************


_n = int(input())

_m = int(input())

res = L(_n, _m)

print(str(res) + "\n")
