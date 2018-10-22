def max_array(nums):
    return_value = nums[0]
    sum = 0
    for each in nums:
        if sum < 0:
            sum = 0
        sum += each
        if sum > return_value:
            return_value = sum
    return return_value


length = int(input())
a_list = [int(each) for each in input().strip().split(' ')]
print(max_array(a_list))
