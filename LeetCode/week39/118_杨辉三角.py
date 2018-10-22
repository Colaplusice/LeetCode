# @Time    : 2018/9/22 上午1:13
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        return_list = [[1]]
        for each_row in range(1, numRows):
            row_list = [1]
            for i in range(1, each_row):
                row_list.append(return_list[each_row - 1][i - 1] + return_list[each_row - 1][i])
            row_list.append(1)
            return_list.append(row_list)
        return return_list


if __name__ == '__main__':
    sol = Solution()
    psd = sol.generate(5)
    print(psd)
