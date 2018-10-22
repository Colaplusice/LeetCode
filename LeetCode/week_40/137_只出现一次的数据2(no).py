class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for each in nums:
            temp = a & each ^a


if __name__ == '__main__':
    sol = Solution()
    result = sol.singleNumber([2, 2, 3, 2])
    print(result)
