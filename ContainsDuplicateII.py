class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for key,value in enumerate(nums):
            if value in d and key-d[value] <= k:
                return True
            d[value]=key
        return False 
