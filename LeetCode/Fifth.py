# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Input: "babad"
# Output: "bab"  bavvvvaab
#  Note: "aba" is also a valid answer.
class Solution:
    def longestPalindrome(self, s):
        key=[]
        restr=''
        de=True
        lens=0
        for each in s:
            if each not in key:
                key.append(each)
            else:
                key.append(each)
                # 判断是不是回文
                for i in range(len(key)):
                    if key[i] != key[len(key) - i - 1]:
                        # key=key[key.index(each)+1:]
                        de=False
                        print('false')
                        break
                if de==True:
                    print('true')
                    print(key)
                    if(len(key)>len(restr)):
                        restr=str(key)
                else:
                    de=True
        print(restr)
sol=Solution()
sol.longestPalindrome('babab')