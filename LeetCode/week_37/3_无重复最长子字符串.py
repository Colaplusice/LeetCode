class Solution:
    def lengthOfLongestSubstring(self, s):
        key = []
        lens = 0
        for index_i, i in enumerate(s):
            if i not in key:
                key.append(i)
                lens = max(lens, len(key))
            else:
                lens = max(lens, len(key))
                begin = key.index(i) + 1
                key = key[begin:]
                key.append(i)
        return lens


if __name__ == "__main__":
    a = Solution()
    ma = a.lengthOfLongestSubstring("nfpdmpi")
    print(ma)
