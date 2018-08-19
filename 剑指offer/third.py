# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        a=[]
        listNode=self.reverse(listNode)
        while listNode!=None:
            a.append(listNode.val)
            listNode=listNode.next
        return a
    # 非递归来实现转置
    def reverse(self,listNode):
        if listNode is None:
            return listNode
        currentNode=None
        revNode=None
        while(listNode):
            currentNode=listNode
            returnNode=listNode
            listNode=listNode.next
            currentNode.next=revNode
            revNode=currentNode
        return currentNode

        #递归实现
    def reverse_2(self,listNode):
        returnNode=None
        if  not listNode.next:
            return listNode
        else:
            a= self.reverse_2(listNode.next)
            a.next=listNode
            listNode.next=None
        
            return listNode



if __name__ == '__main__':
    a = ListNode(0)
    t=a
    for i in range(1,5):
        s=ListNode(i)
        t.next=s
        t=s
    while t:
        print(t.val)
        t = t.next

    print('*'*40)

    sol=Solution()
    b=sol.reverse_2(a)
    while a:
        print(a.val)
        a = a.next

