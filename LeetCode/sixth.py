# 9. Palindrome Number
# Determine whether an integer is a palindrome. Do this without extra space.
class Solution:
    def isPalindrome(self, x):
        s=[]
        if(x<0):
            return False
        while(x/10>0):
            o=x%10
            x=int(x/10)
            s.append(o)
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

sol=Solution()
res=sol.isPalindrome(-312213)
print(res)