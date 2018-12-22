class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, x):
        temp = self
        while temp.next:
            temp = temp.next
        temp.next = x

    def out(self):
        temp = self
        while temp:
            print(temp.val)
            temp = temp.next
        print("*******")

    def Reverse(self):
        temp = None
        last = self
        if not self:
            return
        while self.next:
            temp = self.next
            self.next = temp.next
            temp.next = last
            last = temp

        self.val = temp.val
        self.next = temp.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        temp_1 = l1
        temp_2 = l2
        is_add = 0
        while temp_1 and temp_2:
            temp_1.val += temp_2.val
            if is_add:
                temp_1.val += is_add
                is_add = 0
            if temp_1.val > 9:
                is_add = 1
            temp_1 = temp_1.next
            temp_2 = temp_2.next

        l1.out()
        return l1


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(2)
    te_1 = ListNode(4)
    te_2 = ListNode(3)
    l1.add(te_1)
    l1.add(te_2)

    l1.Reverse()
    l2 = ListNode(5)
    te_3 = ListNode(6)
    te_4 = ListNode(4)
    l2.add(te_3)
    l2.add(te_4)
    l2.Reverse()
    l1.out()
    l2.out()
    # l3=sol.addTwoNumbers(l1, l2)
    # l3.out()/
