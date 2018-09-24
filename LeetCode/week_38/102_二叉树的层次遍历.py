# @Time    : 2018/9/15 上午6:40
from collections import deque
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        queue_list = deque([(root, 0)])
        temp_dict = defaultdict(list)
        temp_dict[0] = [root.val]
        while queue_list:
            current_node = queue_list.popleft()
            if current_node[0].left:
                temp_dict[current_node[1] + 1].append(
                    current_node[0].left.val
                )
                queue_list.append((current_node[0].left, current_node[1] + 1))
            if current_node[0].right:
                temp_dict[current_node[1] + 1].append(
                    current_node[0].right.val
                )
                queue_list.append((current_node[0].right, current_node[1] + 1))
        return [value for value in temp_dict.values()]


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
