# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.tree_list = []
        self.final_list = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.get_the_path(root)
        return_list = self.final_list
        self.final_list = []
        return return_list

    def get_the_path(self, root):
        if not root:
            return
        self.tree_list.append(root.val)
        if not root.left and not root.right:
            self.final_list.append(
                '->'.join([str(a) for a in self.tree_list]))
            self.tree_list.pop()
            return
        self.get_the_path(root.left)
        self.get_the_path(root.right)
        self.tree_list.pop()


if __name__ == '__main__':
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
