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
        node_stack = [root]
        depth = 1
        while node_stack:
            temp_stack = []
            for no in node_stack:
                if not no or (not no.left and not no.right):
                    return depth
                if no.left:
                    temp_stack.append(no.left)
                if no.right:
                    temp_stack.append(no.right)
            node_stack = temp_stack
            depth += 1
        return depth


if __name__ == "__main__":
    atree = TreeNode(1)
    btree = TreeNode(2)
    ctree = TreeNode(3)
    dtree = TreeNode(4)
    etree = TreeNode(5)

    atree.left = btree
    btree.left = dtree
    btree.right = etree

    atree.right = ctree
    sol = Solution()
    value = sol.minDepth(atree)
    print(value)
