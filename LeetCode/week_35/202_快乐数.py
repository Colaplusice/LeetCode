# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sd = {}
        while n != 1:
            if n in sd:
                return False
            sd[n] = 1
            new_n = 0
            s = n
            while s >= 1:
                new_n += (s % 10) ** 2
                s //= 10
            n = new_n
        return True


sol = Solution()

result = sol.isHappy(19)

print(result)
