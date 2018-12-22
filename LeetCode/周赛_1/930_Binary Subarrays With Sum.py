from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        [1, 0, 1, 0, 1]
        """
        value_dict = defaultdict(int)
        value_dict[0] = 1
        sum = 0
        numbers = 0
        for each in A:
            sum += each
            numbers += value_dict[sum - S]
            value_dict[sum] += 1
        return numbers


if __name__ == "__main__":

    sol = Solution()
    res = sol.numSubarraysWithSum([1, 0, 1, 0, 1], 2)
    print(res)
