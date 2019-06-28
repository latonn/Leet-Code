# Time:  O(n)
# Space: O(1)

# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#
# Example:
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if ((i % 2) and nums[i - 1] > nums[i]) or (not (i % 2) and nums[i - 1] < nums[i]):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]


if __name__ == '__main__':
    nums = [3, 5, 2, 1, 6, 4, 7]
    Solution().wiggleSort(nums)
