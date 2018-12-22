class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def out_link(self):
        temp_node = self
        while temp_node:
            print(temp_node.val, end=" ")
            temp_node = temp_node.next
        print()


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return node


if __name__ == "__main__":
    a = ListNode(4)
    b = ListNode(5)
    a.next = b
    c = ListNode(1)
    b.next = c
    d = ListNode(9)
    c.next = d
    a.out_link()
    sol = Solution()
    res = sol.deleteNode(a)
    res.out_link()
