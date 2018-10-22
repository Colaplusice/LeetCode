# @Time    : 2018/9/22 上午1:12
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return (
            (root.val == sum and not root.left and not root.right)
            or self.hasPathSum(root.left, sum - root.val)
            or self.hasPathSum(root.right, sum - root.val)
        )


if __name__ == "__main__":
    atree = TreeNode(1)
    btree = TreeNode(2)
    ctree = TreeNode(3)
    dtree = TreeNode(4)
    etree = TreeNode(5)

    atree.left = btree
    atree.right = ctree
    btree.left = dtree
    ctree.right = etree
    sol = Solution()
    value = sol.hasPathSum(atree, 3)
    print(value)
