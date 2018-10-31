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
        print('-' * 10)


# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        record_dict = {}
        new_link = head
        previous_link = head
        while new_link:
            # 已出现
            if new_link.val in record_dict:
                previous_link.next = new_link.next
            else:
                record_dict[new_link.val] = 1
                previous_link = new_link
            new_link = new_link.next
        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    a.next = b
    c = ListNode(1)
    b.next = c
    d = ListNode(4)
    c.next = d
    e = ListNode(4)
    d.next = e
    a.Out_link()
    sol = Solution()
    sd = sol.deleteDuplicates(a)

    sd.Out_link()
