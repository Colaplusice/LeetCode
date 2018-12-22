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


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(1)
    a.next = b
    c = ListNode(1)
    b.next = c
    d = ListNode(4)
    c.next = d
    e = ListNode(4)
    d.next = e
    a.out_link()
