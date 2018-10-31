# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only hold integers within
# the 32-bit signed integer range.
#  For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        if x > int(2147483647):
            return 0
        elif x > 0:
            x = str(x)
            x = x[::-1]
            while x.startswith("0"):
                x = x[1:]
            if int(x) > int(2147483647):
                return 0
            return int(x)
        elif x < 0:
            x = str(x)
            print(x)
            x = self.reverse(int(x[1:]))
            x = "-" + str(x)
            if int(x) > int(2147483647):
                return 0
            return int(x)
        else:
            return int(x)


s = Solution()
a = s.reverse(1534236469)
print(a)
