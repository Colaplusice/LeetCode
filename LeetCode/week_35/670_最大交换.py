# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
# 把每个位置上最大的数都找出来，然后位置遍历


class Solution:
    def maximumSwap(self, num):

        """e
             :type num: int
             :rtype: int
             从后往前遍历，如果当前的数比max_num大
             当前的数为max_num.当前Index为max_index
             否则，当前的Index为min_index.
             要和min_index交换的Index为max_index
             如果当前数和Max_num相等，pass
             防止污染max_index的值
             
             之所以要添加chang_index 防止前面的数比当前的数大。
             只用max_index的话，反而可能会变小，只有当前面的数比max_index小
             才可以将max_index作为change_index
         """

        num = list(str(num))
        max_num = -100
        max_index = 0
        change_index = 0
        small_index = 0
        # 找出每个元素下一个最大的数

        num.reverse()
        for index, i in enumerate(num):
            i = int(i)
            if i > max_num:
                max_num = i
                max_index = index
            if i == max_num:
                pass
            else:
                change_index = max_index
                small_index = index
        switch(num, small_index, change_index)
        num.reverse()
        return int("".join(num))


def switch(lists, index_a, index_b):
    temp = lists[index_a]
    lists[index_a] = lists[index_b]
    lists[index_b] = temp


sol = Solution()
print(sol.maximumSwap(98368))
