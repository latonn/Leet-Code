# Time:  O(n * s), s is the sum of nums
# Space: O(s)

# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets
# such that the sum of elements in both subsets is equal.
#
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # latonn's
        from collections import defaultdict

        result = defaultdict(int)
        result[nums[0]] = 1
        for i in range(1, len(nums)):
            tmp = defaultdict(int)
            for s in result.keys():
                tmp[s + nums[i]] = 1
                tmp[s - nums[i]] = 1
            result = tmp

        return True if result.get(0, 0) else False

        # kamyu's
        # s = sum(nums)
        # if s % 2:
        #     return False
        #
        # dp = [False] * (s/2 + 1)
        # dp[0] = True
        # for num in nums:
        #     for i in range(1, len(dp)):
        #         if num <= i:
        #             dp[i] = dp[i] or dp[i - num]
        # return dp[-1]


if __name__ == '__main__':
    nums = [1, 5, 10, 5]
    print(Solution().canPartition(nums))