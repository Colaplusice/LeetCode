# @Time    : 2018/9/10 下午10:40

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def print_path(self):
        if not self.val:
            return
        a_stack = [self]
        while a_stack:
            current_node = a_stack.pop()
            print(current_node.val)
            if not current_node.left and not current_node.right:
                if current_node.left:
                    a_stack.append(current_node.left)
            if current_node.right:
                a_stack.append(current_node.right)


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.is_symmetric(root.left, root.right)

    def is_symmetric(self, left, right):

        if not left and not right:
            return True
        if left.val == right.val:
            return self.is_symmetric(left.left, right.right) and \
               self.is_symmetric(left.right, right.left)
        return False



if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    e = TreeNode(2)

    c = TreeNode(3)
    f = TreeNode(3)
    d = TreeNode(4)
    g = TreeNode(4)
    a.left = b
    a.right = e

    b.left = c
    b.right = d

    e.right = f
    e.left = g
    sol = Solution()

    result=sol.isSymmetric(a)
    print(result)