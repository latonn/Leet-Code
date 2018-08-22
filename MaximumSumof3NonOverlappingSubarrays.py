class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # refer from http://bookshadow.com/weblog/2017/10/01/leetcode-maximum-sum-of-3-non-overlapping-subarrays/
        size = len(nums)
        nsize = size - k + 1
        sums = [0] * nsize
        maxa = [0] * nsize
        maxb = [0] * nsize
        total = 0
        for x in range(size):
            total += nums[x]
            if x >= k - 1:
                sums[x - k + 1] = total
                total -= nums[x - k + 1]
        maxn, maxi = 0, 0
        for x in range(nsize):
            if sums[x] > maxn:
                maxn, maxi = sums[x], x
            maxa[x] = (maxn, maxi)
        maxn, maxi = 0, nsize - 1
        for x in range(nsize - 1, -1, -1):
            if sums[x] > maxn:
                maxn, maxi = sums[x], x
            maxb[x] = (maxn, maxi)
        ansn, ansi = 0, None
        for x in range(k, nsize - k):
            va, ia = maxa[x - k]
            vb, ib = maxb[x + k]
            if sums[x] + va + vb > ansn:
                ansn = sums[x] + va + vb
                ansi = [ia, x, ib]
        return ansi 
