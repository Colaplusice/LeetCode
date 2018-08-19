# -*- coding:utf-8 -*-
class Solution:
    #递归太慢了
    def jumpFloor_1(self, number):
        if number==1:
            return 1
        if number==2:
            return 2
        else:
            return self.jumpFloor_1(number-1)+self.jumpFloor_1(number-2)


    def jumpFloor(self,number):
            li=[0,1,2]
            for i in range(2,number):
                li.append(li[i-1]+li[i])

            return li[number]



a=Solution()
print a.jumpFloor(0)