#encoding=utf-8
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。

class Solution:
    def Fibonacci_1(self, n):
        '''递归 非常慢.'''
        if n==1 or n==2:
            return 1

        else:
            return self.Fibonacci_1(n-1)+self.Fibonacci_1(n-2)

    def Fibonacci(self,n):
        if n==0:
            return 0
        a=[]
        a.append(1)
        a.append(1)
        # a.append(a[i-1]+a[i-2] for i  in range(2,38))
        # print(list(a))
        for i in xrange(2,n):
            a.append(a[i-1]+a[i-2])

        return a[n-1]


if __name__ == '__main__':
    sol=Solution()
    print  sol.Fibonacci(20)