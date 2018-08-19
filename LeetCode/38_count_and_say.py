# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, gene
class Solution:
    def countAndSay(self, n):
        fron=[]
        for i in range(n):
            if len(fron)==0:
                fron.append(1)
            else:
                num=fron[i-1]
                num=str(num)
                for each in num:
                    print(each,end=' ')

sol=Solution()

str=sol.countAndSay(1)