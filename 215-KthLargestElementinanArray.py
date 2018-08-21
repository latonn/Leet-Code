#

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in
# the sorted order, not the kth distinct element.
#
# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            pivotIdx = random.randint(left, right)
            newPivotIdx = self.findKthLargestHelper(left, right, pivotIdx, nums)
            if newPivotIdx == k-1:
                return nums[newPivotIdx]
            elif newPivotIdx > k-1:
                right = newPivotIdx - 1
            else:
                left = newPivotIdx + 1

    def findKthLargestHelper(self, left, right, pivotIdx, nums):
        pivotVal = nums[pivotIdx]
        newPivotIdx = left
        nums[pivotIdx], nums[right] = nums[right], nums[pivotIdx]
        for i in range(left, right):
            if nums[i] > pivotVal:
                nums[i], nums[newPivotIdx] = nums[newPivotIdx], nums[i]
                newPivotIdx += 1
            print(pivotVal, nums)
        nums[right], nums[newPivotIdx] = nums[newPivotIdx], nums[right]
        print('iteration: ', nums)
        return newPivotIdx


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))
