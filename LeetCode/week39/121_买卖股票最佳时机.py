# @Time    : 2018/9/22 上午1:14
import sys


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pre_min = sys.maxsize
        max_profit = 0
        for each in prices:
            if each < pre_min:
                pre_min = each

            elif each - pre_min > max_profit:
                max_profit = each - pre_min
        return max_profit


sol = Solution()

sol.maxProfit([7, 1, 5, 3, 6, 4])
