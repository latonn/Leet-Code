#

# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result, i = 1, n
        while i != 0:
            if i % 2 == 1:
                result *= x
            x *= x
            i = int(i/2)
            # print(i, x, result)

        return result if n > 0 else 1 / result


if __name__ == '__main__':
    x = 2.00000
    n = -2
    print(Solution().myPow(x, n))
