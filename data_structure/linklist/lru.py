# @Time    : 2018/9/12 上午8:52
class Node:
    def __init__(self, key=None, value=None):
        self.value = None
        self.key = key
        self.next = value


class NodeList:
    def __init__(self, capacity):
        self.first = None

    def add_node_last(self, node):
        if not isinstance(node, Node):
            raise TypeError("node type must be{}".format(Node.__name__))

        if not self.first:
            self.first = node

        temp = self.first
        while temp.next:
            temp = temp.next
        temp.next = node

    def add_node_first(self, key, value):
        node = Node(key=key, value=value)
        node.next = self.first
        self.first = node

    def __len__(self):
        temp = self.first
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def pop(self):
        pass

    def node_lru(self, key, value):
        temp = self.first
        pre = None
        while temp:
            if temp.key == key:
                self.move_node_to_first(pre, temp)
                return temp.value
            # not found  add in queue
            if not len(self) < capacity:
                self.pop()
            self.add_node_first(key=key, value=value)

    def move_node_to_first(self, per_node, move_node):
        if move_node == self.first:
            return
        if not per_node:
            raise AttributeError("per_node is None")

        per_node.next = move_node.next
        move_node.next = self.first
        self.first = move_node
