# 数组里数字的范围保证在0 ~ n-1 之间


def de_duplicate(nums):
    length = len(nums)
    for i in range(length):
        #  在数组中的标记位
        index = nums[i]
        if index > length:
            index -= length
        # index 放的是数的value值
        if nums[index] > length:
            return index
        # 标记位加上一个长度
        nums[index] += length


nums = [11, 12, 13, 14, 15, 16, 17, 17, 18]
result = de_duplicate(nums)

print(result)
