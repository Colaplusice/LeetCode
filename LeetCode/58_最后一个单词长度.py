# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        elif not s.strip():
            return 0
        sd = s.split()
        sd.reverse()
        return len(sd[0])


s = Solution()
sd = s.lengthOfLastWord("sdd a ")
print(sd)
