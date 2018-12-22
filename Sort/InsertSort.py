def Insert_sort(nums):
    flag = 0
    for index, i in enumerate(nums):
        temp_flag = flag
        if i < nums[temp_flag]:
            while i < nums[temp_flag] and temp_flag >= 0:
                nums[index], nums[temp_flag] = nums[temp_flag], nums[index]
                temp_flag -= 1
                index -= 1
            flag += 1
        print(nums)


if __name__ == "__main__":

    Insert_sort(nums)
