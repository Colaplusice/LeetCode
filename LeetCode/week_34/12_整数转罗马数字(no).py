class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        IMMMM
        """
        str_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        result_str = ""
        if num >= 1000:
            result_str += "M" * (num // 1000)
            print(result_str)
            num = num % 1000
        if num >= 500:
            result_str += "D" * (num // 500)
            num = num % 500
        if num >= 100:
            result_str += "C" * (num // 100)
            num = num % 100
        if num >= 50:
            result_str += "L" * (num // 50)
            num = num % 50
        if num >= 10:
            result_str += "X" * (num // 10)
            num %= 10
        if num >= 5:
            result_str += "V" * (num // 5)
            num %= 5
        if num >= 1:
            result_str += "I" * num
        print(result_str)
        return result_str


s = Solution()
result = s.intToRoman(1999)
