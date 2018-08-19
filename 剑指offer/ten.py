#encoding=utf-8
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

class Solution:
    def rectCover(self, number):
        if number==0:
            return 0
        if number==1:
            return 1

        if number==2:
            return 2

        list=[1,2]
        for i in range(2,number):
            list.append(list[i-1]+list[i-2])

        return list[number-1]


if __name__ == '__main__':
    sol=Solution()

    result=sol.rectCover(3)
    print(result)