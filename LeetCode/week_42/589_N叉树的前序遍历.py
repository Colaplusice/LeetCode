# Definition for a Node.
# 多叉树前序遍历


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            result.append(node.val)
            for each_node in reversed(node.children):
                stack.append(each_node)
        return result

    def preorder_recursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def helper(node):
            if not node:
                return
            result.append(node.val)
            node_children = node.children
            while node_children:
                child = node_children.pop(0)
                helper(child)

        helper(root)
        return result


if __name__ == "__main__":
    ftree = Node(6, [])
    etree = Node(5, [])
    ctree = Node(3, [etree, ftree])
    btree = Node(2, [])
    dtree = Node(4, [])
    atree = Node(1, [ctree, btree, dtree])

    sol = Solution()
    # value = sol.preorder_recursive(atree)
    value = sol.preorder(atree)
    print(value)
