#

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order)
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i-1]:
                break

        if i == 0:
            nums.reverse()
        else:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    break
            for k in range(int((len(nums)-i)/2)):
                nums[i + k], nums[len(nums) - k - 1] = nums[len(nums) - k - 1], nums[i + k]
        print(nums)


if __name__ == '__main__':
    nums = [1, 3, 2]
    Solution().nextPermutation(nums)
