#encoding=utf-8
# 输入一个整数，输出该数二进制表示中的个数。其中负数用补码表示。

class Solution:
    def NumberOf1(self, n):
        li=[]
        rev=0
        if n<0:
            n=abs(n)
            rev=1
        while n>=1:
            if n%2==0:
                li.append('0')
            else:
                li.append('1')
            n/=2

        str=''.join(reversed(li))
        if rev==1:

            result=(int(str)+1)
            pass
        print(str)


if __name__ == '__main__':
    sol=Solution()
    sol.NumberOf1(2)