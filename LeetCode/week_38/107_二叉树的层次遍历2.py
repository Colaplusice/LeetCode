# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 例如：

# Definition for a binary tree node.
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        node_list = deque()
        node_list.append((root, 0))
        node_dict = defaultdict(list)
        node_dict[0] = [root.val]
        while node_list:
            current_node, node_level = node_list.popleft()
            if current_node.left:
                node_dict[node_level + 1].append(current_node.left.val)
                node_list.append((current_node.left, node_level + 1))

            if current_node.right:
                node_dict[node_level + 1].append(current_node.right.val)
                node_list.append((current_node.right, node_level + 1))

        result = sorted(node_dict.items(), reverse=True, key=lambda x: x[0])

        return list(map(lambda x: x[1], result))

        # return [value for value in node_dict.values()]


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
    result = sol.levelOrderBottom(atree)
    print(result)
