# 栈实现dfs 添加一个节点后必须break

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    '''
    this is just for tree,if the graph, have to exclude the visited node
    '''
    def dfs_recursion(self, root):
        if not root:
            return
        print(root.val)
        if root.left:
            self.dfs_recursion(root.left)
        if root.right:
            self.dfs_recursion(root.right)

    def dfs_stack(self, root):
        node_stack=[root]
        while node_stack:
            node=node_stack.pop()
            if root.left:
                node_stack.append(root.left)
            if root.right:
                node_stack.append(root.right)


if __name__ == '__main__':
    atree = TreeNode(1)
    btree = TreeNode(2)
    ctree = TreeNode(3)
    dtree = TreeNode(4)
    etree = TreeNode(5)
    '''
        1     
      2   3
    4       5
    '''

    atree.left = btree
    atree.right = ctree
    btree.left = dtree
    ctree.right = etree
    sol = Solution()
    # value = sol.dfs_recursion(atree)
    print('~'*20)
    value2 = sol.dfs_stack(atree)
