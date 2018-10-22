class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class NodeList():
    def __init__(self):
        self.first = None

    def add_last(self, val):
        if not self.first:
            self.first = Node(val)
            return
        temp = self.first
        while temp.next:
            temp = temp.next

        temp.next = Node(val)

    def out(self):
        temp=self.first
        while temp:
            print(temp.val)
            temp=temp.next

if __name__ == '__main__':
    node=NodeList()
    node.add_last(1)
    node.add_last(2)
    node.add_last(3)
    node.add_last(4)

    node.out()

