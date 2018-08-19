# encoding=utf-8
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class NodeList:
    def __init__(self):
        self.first = None

    def add_in_last(self, node):
        a = self.first
        if not a:
            self.first = node
            return
        while a.next:
            a = a.next
        a.next = node

    def add_by_value(self, value):

        '''

        :param value:int
        :return: None
        '''
        a = Node(value)
        if not self.first:
            self.first = a
        else:
            # 只是一个引用
            b = self.first
            while b.next:
                b = b.next
            b.next = a

    def output(self):
        a = self.first
        if not a:
            return
        else:
            b = a
            while b:
                print(b.val)
                b = b.next

    def add_list(self, b):
        c = NodeList()
        heada = self.first
        headb = b.first
        while heada and headb:
            if heada.val < headb.val:
                c.add_by_value(heada.val)
                heada = heada.next
            else:
                c.add_by_value(headb.val)
                headb = headb.next
        if not heada:
            c.add_in_last(headb)
        else:
            c.add_in_last(heada)
        self.first = c.first

        # 链表的转置

    def reverse(self):
        a=self.first
        if not a:
            return
        last_node=a
        temp_node=None
        while a.next:
            # record
            temp_node=a.next
            # update
            a.next=temp_node.next
            # record
            temp_node.next=last_node
            # update
            last_node=temp_node
        self.first=temp_node


if __name__ == '__main__':
    s = NodeList()
    s.add_by_value(1)
    s.add_by_value(2)
    s.add_by_value(3)
    s.add_by_value(4)
    s.reverse()
    s.output()
