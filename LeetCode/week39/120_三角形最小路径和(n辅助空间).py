# @Time    : 2018/9/22 上午1:14

# 动态规划
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        val[i]表示最后一层第i个节点的最小值
        """
        length = len(triangle)
        val = [0] * length

        triangle.reverse()
        print(triangle)
        # for index, each_node in enumerate(triangle[0]):
        #     val[index] = each_node

        for level_index, each_level in enumerate(triangle):
            val[0]=triangle[level_index][0]+val[0]
            for index, each_node in \
                    enumerate(each_level[1:], 1):
                val[index] = (
                        min(
                            each_level[index],
                            each_level[index - 1],
                        )
                        + val[index]
            )

        print(val)


if __name__ == "__main__":
    sol = Solution()

    result = sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(result)
