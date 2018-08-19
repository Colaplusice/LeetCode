# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        self.stack1.append(node)
        self.stack2=[each for each in reversed(self.stack1)]
        # write code here
    def pop(self):
        a=self.stack2.pop()
        self.stack1=[each for each in reversed(self.stack2)]
        return a
        # return xx
if __name__ == '__main__':
    a=Solution()
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.pop())
    a.push(4)
    print(a.pop())
    a.push(5)
    print(a.pop())
    print(a.pop())



