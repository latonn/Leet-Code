#
#

# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpMax = [float('-inf') for i in range(len(nums))]
        dpMin = [float('inf') for j in range(len(nums))]
        dpMax[0], dpMin[0] = nums[0], nums[0]
        result = nums[0]
        for k in range(1, len(nums)):
            dpMax[k] = max(max(dpMax[k-1] * nums[k], dpMin[k-1] * nums[k]), nums[k])
            dpMin[k] = min(min(dpMax[k-1] * nums[k], dpMin[k-1] * nums[k]), nums[k])
            result = dpMax[k] if dpMax[k] > result else result

        # print(dpMax)
        # print(dpMin)
        return result


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print(Solution().maxProduct(nums))
