class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        for each in nums:
            if each != val:
                nums[begin] = each
                begin += 1
        return begin


if __name__ == '__main__':

    sol = Solution()

    nums = sol.removeElement([3, 2, 2, 3], 3)
    print(nums)
