# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return_value = nums[0]
        sum = 0
        for each in nums:
            if sum < 0:
                sum = 0
            sum += each
            if sum > return_value:
                return_value = sum
        return return_value


sol = Solution()
a = [1, 2]

res = sol.maxSubArray(a)
print(res)
