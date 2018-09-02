# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, gene
class Solution:
    def countAndSay(self, n):
        fron = '1'
        for i in range(1, n):
            pre = None
            num = 0
            new_fron = ''
            for each in fron:
                if each == pre:
                    num += 1
                else:
                    if num != 0:
                        new_fron += str(num) + pre
                        pre = each
                        num = 1
            fron = new_fron
        print(fron)
        return fron


sol = Solution()
str = sol.countAndSay(2)
