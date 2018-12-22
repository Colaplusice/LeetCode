# 动态规划
class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        """
        value_arr[i][j] 第i行 第j列的最小值
        """
        value_arr = [[0] * len(A) for _ in range(len(A))]
        for row_index, each_row in enumerate(A):
            if row_index == 0:
                value_arr[row_index] = each_row
                continue
            for value_index, each_value in enumerate(each_row):
                if value_index == 0:
                    value_arr[row_index][value_index] = (
                        min(
                            value_arr[row_index - 1][value_index],
                            value_arr[row_index - 1][value_index + 1],
                        )
                        + each_value
                    )
                    continue
                if value_index == len(each_row) - 1:
                    value_arr[row_index][value_index] = (
                        min(
                            value_arr[row_index - 1][value_index],
                            value_arr[row_index - 1][value_index - 1],
                        )
                        + each_value
                    )
                    continue
                value_arr[row_index][value_index] = (
                    min(
                        value_arr[row_index - 1][value_index - 1],
                        value_arr[row_index - 1][value_index],
                        value_arr[row_index - 1][value_index + 1],
                    )
                    + each_value
                )
        return min(value_arr[-1])


if __name__ == "__main__":
    sol = Solution()
    res = sol.minFallingPathSum([[10, -98, 44], [-20, 65, 34], [-100, -1, 74]])
    print(res)
