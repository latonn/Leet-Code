#

# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that
# A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are
# in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        partialSum = defaultdict(int)
        for i in A:
            for j in B:
                partialSum[i+j] += 1

        for k in C:
            for l in D:
                tmp = (k+l) *(-1)
                if tmp in partialSum:
                    count += partialSum[tmp]

        return count


if __name__ == '__main__':
    A = [-1, -1]
    B = [-1, 1]
    C = [-1, 1]
    D = [1, -1]
    print(Solution().fourSumCount(A, B, C, D))