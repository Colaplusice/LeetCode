# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Input: "babad"
# Output: "bab"  bavvvvaab
#  Note: "aba" is also a valid answer.


class Solution:
    # def longestPalindrome(self, s):
    #     '''
    #     用动态规划来做
    #     s[x][y]=x-->y 是否为回文
    #     当x==y时为回文
    #     当x==y+1时，如果相等则为回文
    #     否则s[x][y]==s[x-1][y-1]+str[x]==str[y]if s[x-1][y-1]是回文
    #     :param s:
    #     :return:
    #     '''
    #     s_len = len(s)
    #     matrix = [[0] * s_len]
    #     for i in range(s_len):
    #         for j in range(i):
    #             value_1 = s[i - 1][j - 1] + 1 if s[i] == s[j] else s[i - 1][j - 1]
    #             # s[i][j] = max(s[i - 1][j - 1] + 1 if s[i] == s[j])
    #
    #         pass

    def longestPalindrome_2(self, s):
        max_length = 0
        len_s=s.__len__()
        start = 1
        matrix = [[0] * len_s] * len_s
        for i in range(len_s - 1):
            matrix[i][i] = 1
            if s[i] == s[i + 1]:
                matrix[i][i + 1] = 1
                start = i
                max_length = 2

        for len in range(3, len_s):  # 长长度
            for i in range(len_s - len + 1):  # 起点
                j=i+len-1
                if s[i + 1][j-1] and s[i] == s[j]:
                    s[i][j] = 1
                    max_length = len
                    start = i
        print(start)
        print(max_length)
        return s[start:max_length + start]


sol = Solution()
sd = sol.longestPalindrome_2('aba')
print(sd)
