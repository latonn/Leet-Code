#

# Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
# and the length of an increasing subsequence should be at least 2 .
#
# Example:
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note:
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of
# increasing sequence.


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # latonn
        # backtrack
        def helper(nums, idx, res, result):
            print(nums, idx, res, result)
            if len(res) >= 2:
                result.append(list(res))
            lookup = set()
            for i in range(idx, len(nums)):
                if (not res or nums[i] >= res[-1]) and nums[i] not in lookup:
                    lookup.add(nums[i])
                    res.append(nums[i])
                    helper(nums, i+1, res, result)
                    res.pop()

        result, res = [], []
        helper(nums, 0, res, result)
        return result

        # https://goo.gl/kdNDBd
        # dp = set()
        # for n in nums:
        #     for y in list(dp):
        #         if n >= y[-1]:
        #             dp.add(y + (n,))
        #     dp.add((n,))
        # return list(e for e in dp if len(e) > 1)


if __name__ == "__main__":
    nums = [4, 6, 7, 7]
    print(Solution().findSubsequences(nums))
