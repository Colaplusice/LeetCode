#encoding=utf-8
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloorII(self, number):
        li=[0,1,2]
        for i in range(2,number):
            result=0
            for j in range(i+1):
                result+=li[j]
            li.append(result+1)
        return li[number]


if __name__ == '__main__':
    sol=Solution()

    print  sol.jumpFloorII(3)


