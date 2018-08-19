# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#dcxxi  621
class Solution:
    def romanToInt(self, s):
        DIC={'I':1,'V':5,'L':50,'X':10,'C':100,'D':500,'M':1000}
        max=DIC[s[0]]
        sum=0
        if len(s)==1:
            return DIC[s]
        for i in s:
            if DIC[i]>max:
                sum-=(max*2)
                sum+=DIC[i]
                max=DIC[i]
            else:
                sum+=DIC[i]
                max=DIC[i]
        return sum
sol=Solution()

mu=sol.romanToInt('MDCCCLXXXIV')
print(mu)