# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        length = len(nums)
        while index < length:
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
                index -= 1
                length -= 1
            index += 1
        print(nums)


if __name__ == "__main__":

    sol = Solution()
    sol.moveZeroes([0, 0, 1])
