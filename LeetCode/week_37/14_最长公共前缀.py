# 输入: ["flower","flow","flight"]
# 输出: "fl"
class Solution:
    def longestCommonPrefix(self, strs):

        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        tmp = strs[0]
        for each_word in strs[1:]:
            min_length = min(len(tmp), len(each_word))
            for i in range(min_length):
                if tmp[i] != each_word[i]:
                    tmp = each_word[:i]
                    break
            tmp = tmp[:min_length]
        return tmp


sol = Solution()
sts = ["dog", "racecar", "car"]
sol.longestCommonPrefix(sts)
