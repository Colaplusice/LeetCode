from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_out_tree_node(self, root):
        node_queue = deque([root])
        while node_queue:
            current_node = node_queue.popleft()
            print(current_node.val)
            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

    def dfs(self):
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
    value = sol.bfs_out_tree_node(atree)
