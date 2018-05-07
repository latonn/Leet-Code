#

# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols +
# and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # latonn's
        from collections import defaultdict
        if not nums:
            return 0

        result = {0: 1}
        for num in nums:
            tmp = defaultdict(int)
            for s, m in result.items():
                tmp[s + num] += m
                tmp[s - num] += m
            result = tmp

        return result[S]


if __name__ == '__main__':
    nums = [35,42,34,22,35,39,35,44,33,48,46,18,4,39,1,50,28,43,15,37]
    S = 36
    print(Solution().findTargetSumWays(nums, S))
