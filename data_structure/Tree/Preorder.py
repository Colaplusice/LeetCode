# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.is_append = False


class Solution:
    def preorderTraversal(self, root):

        ## 循环实现
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        alist = []
        result_list = []
        if not root:
            return result_list
        alist.append(root)
        result_list.append(root.val)
        root.is_append = True
        while alist:
            a = alist.pop()

            # a.is_append=True
            # result_list.append(a.val)
            # 添加左节点
            while a is not None:
                print('1')
                print(a)
                alist.append(a)
                if not a.is_append:
                    result_list.append(a.val)
                    a.is_append = True
                print(a.left)
                a = a.left
            while a is not None:
                alist.append(a)
                if not a.is_append:
                    result_list.append(a.val)
                    a.is_append = True
                a = a.right
            # alist.append(root.val)
            # root=root.left
        return result_list


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    sol = Solution()
    print(sol.preorderTraversal(a))
