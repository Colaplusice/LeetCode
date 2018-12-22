# @Time    : 2018/9/22 上午1:12
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def helper(nums, length):
            if not nums:
                return
            root_index = length // 2
            root = TreeNode(nums[root_index])
            root.left = helper(nums[:root_index], root_index)
            root.right = helper(nums[root_index + 1 :], length - root_index - 1)
            return root

        return helper(nums, len(nums))


if __name__ == "__main__":
    tree_list = [3, 5, 8]

    sol = Solution()
    value = sol.sortedArrayToBST(tree_list)
