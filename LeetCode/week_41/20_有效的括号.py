class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if not len(s) % 2 == 0:
            return False
        key_dict = {'(': ')', "{": "}", "[": "]"}
        a_stack = []
        for each in s:
            if each in key_dict:
                a_stack.append(each)
            elif not a_stack or key_dict[a_stack.pop()]!=each:
                return False
        return not a_stack
