class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self):
        self.first_node = None

    def add(self, node):
        if not self.first_node:
            self.first_node = node

        else:
            temp = self.first_node
            while temp.next:
                temp = temp.next

            temp.next = node

    def out(self):
        temp = self.first_node
        while temp:
            print(temp.value)
            temp = temp.next

    def reverse(self):
        temp = self.first_node
        last_node = self.first_node
        c_node = None
        while temp.next:
            c_node = temp.next
            temp.next = c_node.next
            c_node.next = last_node
            last_node = c_node

        self.first_node = c_node

    def add_list(self, bList):
        temp_1 = a_list.first_node
        temp_2 = bList.first_node

        is_add = 0
        while temp_2:
            temp_1.value += temp_2.value
            if is_add:
                temp_1.value += 1
                is_add = 0
            if temp_1.value > 9:
                temp_1.value %= 10
                is_add = 1

            temp_1 = temp_1.next
            temp_2 = temp_2.next


if __name__ == "__main__":
    a_list = LinkList()
    b_list = LinkList()
    a = Node(1)
    b = Node(2)
    c = Node(3)

    d = Node(4)
    e = Node(9)
    a_list.add(a)
    a_list.add(b)
    a_list.add(c)
    a_list.reverse()
    b_list.add(d)
    b_list.add(e)
    b_list.reverse()

    a_list.add_list(b_list)

    # a_list.reverse()

    a_list.out()
