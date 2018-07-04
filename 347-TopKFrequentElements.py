#

# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # latonn's
        from collections import defaultdict
        nums.sort()
        cnt, num = 0, nums[0]
        result = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] == num:
                cnt += 1
            else:
                result[num] = cnt
                num, cnt = nums[i], 1
        if num in result.keys():
            result[num] += 1
        else:
            result[num] = cnt
        ans = sorted(result.items(), key=lambda x: x[1])
        answer = []
        for i in range(k):
            answer.append(ans.pop(-1)[0])
        return answer


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
