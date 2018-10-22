class MagicDictionary:
    def __init__(self):
        self.dicts = {}
        """
        Initialize your data structure here.
        """

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dicts = {}
        for each in dict:
            print(each)
            self.dicts.setdefault(len(each), [])
            self.dicts[len(each)].append(each)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        # 一个字母换成另一个字母，存在dicts中，首先即word和dicts中的每个单词必须差一个字母
        # 或者多一个字母，通过求两字符串的编辑距离来实现 ，动态规划
        l = len(word)
        self.dicts.setdefault(l, [])
        for each in self.dicts[l]:
            result = self.min_distance(word, each)
            if result:
                return True
        return False

    def min_distance(self, str_a, str_b):
        n = 0
        for i in range(len(str_a)):
            if str_a[i] != str_b[i]:
                n += 1
        if n != 1:
            return False
        return True


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
dict = ["hello", "leetcode"]
obj.buildDict(dict)
word = 'leetcodd'
param_2 = obj.search(word)

print(param_2)
