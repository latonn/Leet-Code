#

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
# of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
#
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # latonn's
        size = len(nums)
        left, right, sum = 0, 0, 0
        result = size + 1
        while right < size:
            while right < size and sum < s:
                sum += nums[right]
                right += 1
            while left < right and sum >= s:
                result = min(result, right - left)
                sum -= nums[left]
                left += 1
        return result if result <= size else 0


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    print(Solution().minSubArrayLen(s, nums))
