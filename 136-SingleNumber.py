#

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # latonn's
        ans = []
        for num in nums:
            if num not in ans:
                ans.append(num)
            else:
                ans.remove(num)
        return ans[0]

        # kamyu's
        # import operator
        # from functools import reduce
        # return reduce(operator.xor, nums)


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))
