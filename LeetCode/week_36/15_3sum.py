def list_set(a_list):
    dicts = {}

    for each in a_list:
        each = tuple(each)
        if not dicts.get(each):
            dicts[each] = 1
        else:
            dicts[each] += 1
    return [list(k) for k, v in dicts.items()]


class Solution:
    def threeSum(self, nums):
        """
        排序整个list
        整体问题不大，用夹逼的思想
        遍历list,left,right逗比list的当前值要大
        如果==0，进行重复判断，添加进去
        如果<0:
        对left值进行增加
        如果>0 对right元素进行减小  可以循环减小，也可以每次只减少一个数
        超时问题:
        优化思想:
        减少重复的工作量 对于重复的value值不进行比较
        2.在逻辑判断上进行优化 先对left进行增加，因为value为负的元素比较多
        如果先从right进行减少的话就超时了
        :param nums:
        :return:
        """
        nums.sort()
        result_list = []
        # 后两个元素没有遍历的必要了
        for index in range(len(nums) - 2):
            # 除去两个数相等的情况
            if index == 0 or nums[index] > nums[index - 1]:
                left = index + 1
                right = len(nums) - 1
                # left = index+1
                # right = len(nums) - 1
                while left < right:
                    result = nums[index] + nums[left] + nums[right]
                    if result == 0:
                        result_list.append([nums[index], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # 对相同的值进行index减，优化的策略
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif result < 0:
                        while (
                            left < right and nums[index] + nums[left] + nums[right] < 0
                        ):
                            left += 1
                    else:
                        while (
                            left < right and nums[index] + nums[left] + nums[right] > 0
                        ):
                            right -= 1
        return list_set(result_list)


if __name__ == "__main__":
    sol = Solution()

    list_1 = [-1, 0, 1, 2, -1, -4]

    a = sol.threeSum(list_1)
    print(a)
