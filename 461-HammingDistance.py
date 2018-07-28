# Time Complexity:  O(1)
# Space Complexity: O(1)
#
# The Hamming distance between two integers is the number
# of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note: 0 ≤ x, y < 2**31.
#
# Example:
#
#     Input: x = 1, y = 4
#     Output: 2
#
#     Explanation:
#     1   (0 0 0 1)
#     4   (0 1 0 0)
#            ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Solution1
        distance = 0
        z = x ^ y
        print(z)
        while z:
            distance += 1
            z &= z - 1
        return distance

        # Solution2
        # z = bin(x ^ y)
        # return z.count('1')


if __name__ == '__main__':
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
