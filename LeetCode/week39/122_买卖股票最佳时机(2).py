# @Time    : 2018/9/22 上午1:15


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        all_profit = 0
        for index in range(1, length):
            if prices[index] > prices[index - 1]:
                all_profit += prices[index] - prices[index - 1]
        return all_profit


if __name__ == '__main__':
    sol = Solution()
    result = sol.maxProfit([1, 2, 3, 4, 5])
    print(result)
