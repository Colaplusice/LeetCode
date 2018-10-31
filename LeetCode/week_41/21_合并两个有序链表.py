# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        current_node = head
        while l1 and l2:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
                current_node = current_node.next
            else:
                current_node.next = l2
                l2 = l2.next
                current_node = current_node.next
        if l1:
            current_node.next = l1
        else:
            current_node.next = l2

        return head.next


if __name__ == '__main__':

    sol = Solution()
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    c = ListNode(1)
    d = ListNode(4)
    c.next = d
    e = ListNode(4)
    d.next = e

    result = sol.mergeTwoLists(a, c)

    while result:
        print(result.val)
        result = result.next
