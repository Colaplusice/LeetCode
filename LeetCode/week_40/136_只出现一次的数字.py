class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for each in nums:
            result ^= each
        return result


if __name__ == "__main__":
    sol = Solution()
    result = sol.singleNumber([2, 2, 1])
    print(result)
