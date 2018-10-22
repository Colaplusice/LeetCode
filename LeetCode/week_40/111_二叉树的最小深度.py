# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        if root.left:
            return self.minDepth(root.left)+1
        if root.right:
            return self.minDepth(root.right)+1
        return 1

if __name__ == '__main__':
    atree = TreeNode(1)
    btree = TreeNode(2)
    atree.left = btree
    sol = Solution()
    value = sol.minDepth(atree)
    print(value)
