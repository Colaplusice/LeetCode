# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        numbers = 0
        value_dict = defaultdict(int)
        # 总和为0的数为1
        value_dict[0] = 1
        for each in nums:
            sum += each
            numbers += value_dict[sum - k]
            value_dict[sum] += 1

        return numbers


if __name__ == "__main__":
    sol = Solution()
    test_list = [1]

    test_num = 0
    sd = sol.subarraySum(test_list, test_num)
    print(sd)
