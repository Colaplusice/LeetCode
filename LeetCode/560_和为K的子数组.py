# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

from collections import deque


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        all = 0
        a_que = deque()
        while nums:
            a = nums.pop()
            a_que.append(a)
            if sum(a_que) == k:
                all += 1
                a_que.popleft()
            elif sum(a_que)>k:
                a_que.popleft()
        return all


if __name__ == '__main__':
    sol = Solution()
    test_list=[-1,-1,1]
    test_num=0
    sd = sol.subarraySum(test_list, test_num)
    print(sd)
