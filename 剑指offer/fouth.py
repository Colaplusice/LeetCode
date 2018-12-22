# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点 输入前序遍历和中序遍历
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            print(pre)
            print(tin)
            ancestor = TreeNode(pre[0])
            leftIndex = tin.index(pre[0])
            ancestor.left = self.reConstructBinaryTree(
                pre[1 : leftIndex + 1], tin[:leftIndex]
            )
            ancestor.right = self.reConstructBinaryTree(
                pre[leftIndex + 1 :], tin[leftIndex + 1 :]
            )
            return ancestor


if __name__ == "__main__":
    a = Solution()
    pre_list = range(1, 8)
    tin_list = [3, 2, 4, 1, 6, 5, 7]
    ancestor = a.reConstructBinaryTree(pre_list, tin_list)
