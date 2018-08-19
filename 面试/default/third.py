#encoding=utf-8
# 输入一个链表，从尾到头打印链表每个节点的值。

class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next


a=ListNode(val=1)
b=ListNode(val=2)
c=ListNode(val=3)
d=ListNode(val=4)
e=ListNode(val=5)
a.next=b
b.next=c
c.next=d
d.next=e


def out(listNode):
    while(listNode!=None):
        print(listNode.val)
        listNode=listNode.next
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        a=[]
        listNode=self.reverse(listNode)
        while listNode!=None:
            a.append(listNode.val)
            listNode=listNode.next
        return a
    def reverse(self,listNode):
        if listNode is None or listNode.next is None:
            return listNode
        else:
            a1=self.reverse(listNode.next)
            a1.next=ListNode
            listNode.next=None


out(a)
print('------')
s=Solution()
s.reverse(a)

