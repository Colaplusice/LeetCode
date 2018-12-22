#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

nums = 0


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# 二叉搜索树，左节点小于根节点小于右节点
# ******************************开始写代码******************************


def Max_heapify(heap, Heapsize, root):
    global nums
    left = root * 2 + 1
    right = root * 2 + 2
    # lager=root
    # left child
    # if left < Heapsize and right < Heapsize and heap[left] > heap[right] > heap[
    #     root]:
    #     heap[left], heap[right] = heap[right], heap[left]
    #     nums += 1
    if right < Heapsize and heap[right] < heap[root]:
        nums += 1
        heap[right], heap[root] = heap[root], heap[right]
        Max_heapify(heap, Heapsize, right)

    if left < Heapsize and heap[left] > heap[root]:
        heap[left], heap[root] = heap[root], heap[left]
        nums += 1
        Max_heapify(heap, Heapsize, left)


def minSwapTime(values):
    global nums
    Heapsize = len(values)
    # 依次找到所有的根节点
    for i in range((Heapsize - 2) // 2, -1, -1):
        Max_heapify(values, Heapsize, i)
    return nums


# ******************************结束写代码******************************


_values_cnt = 0
_values_cnt = int(input())
_values_i = 0
_values = []
while _values_i < _values_cnt:
    _values_item = int(input())
    _values.append(_values_item)
    _values_i += 1

res = minSwapTime(_values)

print(str(res) + "\n")
