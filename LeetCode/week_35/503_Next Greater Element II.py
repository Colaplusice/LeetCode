class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        # 储存的是tuple信息
        Stack_a = []
        for_result = len(nums)
        nums.extend(nums)
        final_list = [-1] * len(nums)
        for index, i in enumerate(nums):
            # 栈顶元素小于i 出栈 dict[i]=i 否则添加入栈继续遍历
            while Stack_a and Stack_a[-1][1] < i:
                result = Stack_a.pop()
                final_list[result[0]] = i
            Stack_a.append((index, i))
        return final_list[:for_result]


if __name__ == "__main__":
    a = Solution()
    a_list = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    # a_list = [5,4,3,2,1]
    # a.Insert_sort(a_list)
    # print(a_list)
    print(a.nextGreaterElements(a_list))
