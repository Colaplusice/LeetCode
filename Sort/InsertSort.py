def Insert_sort(nums):
    flag = 0
    for index, i in enumerate(nums):
        temp_flag = flag
        if i < nums[temp_flag]:
            while i < nums[temp_flag] and temp_flag >= 0:
                Swich(nums, index, temp_flag)
                temp_flag -= 1
                # 每次往前置换一位 这个元素的index就减少一位,所以index也应该减少
                index -= 1
            flag += 1
        print(nums)

def Swich(list,index_a,index_b):
        temp=list[index_a]
        list[index_a]=list[index_b]
        list[index_b]=temp
if __name__ == '__main__':

    # a=[[0, 49], [1, 50], [2, 51], [3, 57], [4, 48]]

    Insert_sort(nums)