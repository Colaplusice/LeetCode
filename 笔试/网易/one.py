# encoding=utf-8
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# a=2 3 4
# 好蠢

a = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]

# -*- coding:utf-8 -*-
class Solution:

    # array 二维列表
    def Find(self, target, array):
        for index, each in enumerate(array):
            for indexs, eachs in enumerate(each):
                if eachs == target:
                    return True
            # 比所有的列向量都大，从最后一行开始往右找


if __name__ == "__main__":
    ass = Solution()

    # res=ass.Find(10,a)
    # print(res)
    #
    for index, each in enumerate(a):
        for index, each in enumerate(each):
            where = ass.Find(each, a)
            if where is None:
                print(each)
