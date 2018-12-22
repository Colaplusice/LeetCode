# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def Out_link(self):
        temp_node = self
        while temp_node:
            print(temp_node.val)
            temp_node = temp_node.next
        print("-" * 10)


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return

        while head and head.val == val:
            head = head.next
        if not head or not head.next:
            return head
        tmp_head = head.next
        pre_node = head
        while tmp_head:
            if tmp_head.val == val:
                pre_node.next = tmp_head.next
            else:
                pre_node = tmp_head
            tmp_head = tmp_head.next

        return head


if __name__ == "__main__":
    a = ListNode(1)
    # b = ListNode(1)
    # a.next = b
    # c = ListNode(1)
    # b.next = c
    # d = ListNode(4)
    # c.next = d
    # e = ListNode(4)
    # d.next = e
    a.Out_link()
    sol = Solution()
    sd = sol.removeElements(a, 1)

    sd.Out_link()
