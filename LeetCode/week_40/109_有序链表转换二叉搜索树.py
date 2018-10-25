# Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def helper(head, tail):
            if head == tail:
                return None
            if head.next == tail:
                return TreeNode(head.val)

            temp_node = head
            mid_node = head
            while temp_node != tail and temp_node.next != tail:
                mid_node = mid_node.next
                temp_node = temp_node.next.next
            treeNode = TreeNode(mid_node.val)
            treeNode.left = helper(head, mid_node)
            treeNode.right = helper(mid_node.next, tail)
            return treeNode

        return helper(head, None)
    def level_out_tree_node(self, root):
        node_queue = deque([root])
        while node_queue:
            current_node = node_queue.popleft()
            print(current_node.val)
            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

if __name__ == '__main__':
    atree = ListNode(1)
    btree = ListNode(2)
    ctree = ListNode(3)
    dtree = ListNode(4)
    etree = ListNode(5)
    atree.next = btree
    btree.next = ctree
    ctree.next = dtree
    dtree.next = etree

    sol = Solution()
    value = sol.sortedListToBST(atree)
    sol.level_out_tree_node(value)
