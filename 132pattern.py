class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        a3 = nums[0]
        for i in xrange(1, len(nums)-1):
            if a3 < nums[i]:
                for j in xrange(i+1, len(nums)):
                    if a3 < nums[j] < nums[i]:
                        return True
            else:
                a3 = nums[i]
        return False

