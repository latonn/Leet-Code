#

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest
# to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # latonn's
        nums.sort()
        mindiff = float("INF")
        result = 0
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - sum)
                if diff < mindiff:
                    mindiff, result = diff, sum

                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
