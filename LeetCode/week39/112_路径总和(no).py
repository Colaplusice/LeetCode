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
        '''
        感觉是要dfs遍历 然后统计数据啊
        '''
        if not root:
            return False
        a_stack=[root]
        value=0
        while a_stack:
            current_node=a_stack.pop()
            value+=current_node.val
            if current_node.left:

                pass
            if current_node.right:
                pass

            if not current_node.left and not current_node.right:
                pass












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
    value = sol.levelOrder(atree)
    print(value)
