# 给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
#
# 我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
#
# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路:
        用plist记录前n个数据的相加值
        plist[1]为前0，1个数字的相加值
        plist[2]为index为0，1，2的相加值

        如果遍历到第i个数，前i-1个数的相加值==[i+1:n]个数的相加值即成功
        在注意下细节就好
        """
        if len(nums) == 0:
            return -1
        plist = []
        values = 0
        for each in nums:
            values += each
            plist.append(values)

        last = len(plist) - 1
        for index, each in enumerate(nums):
            if 0 == plist[last] - plist[index] and index is 0:
                print("here")
                return 0
            if index > 0 and plist[index - 1] == plist[last] - plist[index]:
                return index
        return -1


if __name__ == "__main__":
    sol = Solution()
    lists = [0, -1, -1, -1, -1, -1]

    print(sol.pivotIndex(lists))
