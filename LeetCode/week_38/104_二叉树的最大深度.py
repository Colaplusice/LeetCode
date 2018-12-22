# @Time    : 2018/9/15 上午8:06
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


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
    result = sol.maxDepth(atree)
    print(result)
