# @Time    : 2018/9/22 上午1:13
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        a_stack = [root]
        first = None
        while a_stack:
            node = a_stack.pop()
            if not first:
                first = TreeNode(node.val)
            else:
                tmp = first
                while tmp.right:
                    tmp = tmp.right
                tmp.right = TreeNode(node.val)
                tmp.left = TreeNode(None)

            if node.right:
                a_stack.append(node.right)
            if node.left:
                a_stack.append(node.left)

        root = first
        return root

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
            self.final_list.append('->'.join([str(a) for a in self.tree_list]))
            self.tree_list.pop()
            return
        self.get_the_path(root.left)
        self.get_the_path(root.right)
        self.tree_list.pop()


if __name__ == "__main__":
    atree = TreeNode(1)
    btree = TreeNode(2)
    ctree = TreeNode(3)
    dtree = TreeNode(4)
    etree = TreeNode(5)
    ftree = TreeNode(6)

    atree.left = btree
    btree.left = ctree
    btree.right = dtree
    atree.right = etree
    etree.right = ftree
    sol = Solution()
    value = sol.flatten(atree)
    a = [value]
    while a:
        value = a.pop()
        if value:
            print(value.val)
        else:
            print(None)
            continue
        a.append(value.left)
        a.append(value.right)
