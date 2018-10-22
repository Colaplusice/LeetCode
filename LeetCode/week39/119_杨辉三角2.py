# @Time    : 2018/9/22 上午1:14
import operator
from functools import reduce


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if not rowIndex:
            return [1]
        row_list = [1]
        rowIndex += 1
        for row_num in range(1, rowIndex):
            row_list.append(
                int(
                    reduce(operator.mul, range(rowIndex - row_num, rowIndex))
                    / reduce(operator.mul, range(1, row_num + 1))
                )
            )
        return row_list


if __name__ == "__main__":
    sol = Solution()
    psd = sol.getRow(5)
    print(psd)
