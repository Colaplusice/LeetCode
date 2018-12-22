# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.is_append = False


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node_list = [root]
        result_list = []
        while node_list:
            node = node_list.pop()
            if not node:
                continue
            result_list.append(node.val)
            node_list.append(node.right)
            node_list.append(node.left)
        return result_list


if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    sol = Solution()
    res = sol.preorderTraversal(a)
    print(res)
