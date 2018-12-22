# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return
        node_stack = [(root, "")]
        res = []

        while node_stack:
            node, value = node_stack.pop()
            if not node.left and not node.right:
                res.append(value + str(node.val))

            if node.left:
                node_stack.append((node.left, value + str(node.val) + "->"))
            if node.right:
                node_stack.append((node.right, value + str(node.val) + "->"))
        return res


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
    final_list = sol.binaryTreePaths(atree)
    print(final_list)
