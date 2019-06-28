#

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays
# whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
#
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        acc = {}
        acc.update({0:1})
        sum, count = 0, 0
        for num in nums:
            sum += num
            count += acc.get(sum - k, 0)
            acc.update({sum: acc.get(sum, 0)+1})
            # print(acc, count)
        return count


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))
