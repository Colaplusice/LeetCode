# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

# 你可以假设除了整数 0 之外，这个整数不会以零开头。
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        add_one = 1
        for index in range(len(digits) - 1, -1, -1):
            if add_one:
                if digits[index] == 9:
                    digits[index] = 0
                else:
                    digits[index] += 1
                    add_one = 0
        if add_one:
            extend_list = [1]
            extend_list.extend(digits)
            return extend_list
        return digits


a = Solution()
result = a.plusOne([9])

print(result)
