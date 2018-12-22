# @Time    : 2018/9/22 上午1:14

# 动态规划
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        index_i-1
        w[i][j]表示从第i行第j列往下走的最小路径
        w[i+1][j]=w[i][j-1],w[i][j+1]+w[i][j]
        value[i][j]=value[i-1]+min(a[index_i],index[i+1])
        a[i]=a[i-1]+min()
        """
        length = len(triangle)

        value = [i * [0] for i in range(1, length + 1)]
        value[0][0] = triangle[0][0]
        for list_index, each_list in enumerate(triangle):
            if list_index == 0:
                value[0][0] = triangle[0][0]
                continue
            for index, each_value in enumerate(each_list):
                if index == 0:
                    value[list_index][0] = (
                        value[list_index - 1][0] + triangle[list_index][0]
                    )
                    continue
                if index == len(each_list) - 1:
                    value[list_index][-1] = (
                        value[list_index - 1][-1] + triangle[list_index][-1]
                    )
                    continue
                value[list_index][index] = (
                    min(value[list_index - 1][index], value[list_index - 1][index - 1])
                    + triangle[list_index][index]
                )

        return min(value[-1])


if __name__ == "__main__":
    sol = Solution()
    result = sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(result)
