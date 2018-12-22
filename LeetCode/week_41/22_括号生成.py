class Solution:
    def generateParenthesis(self, n):
        a_list = []

        def helper(left, right, str_s):
            if left > 0:
                helper(left - 1, right, str_s + "(")
            if right > left:
                helper(left, right - 1, str_s + ")")
            if left == right == 0:
                a_list.append(str_s)

        helper(n, n, "")
        return a_list
