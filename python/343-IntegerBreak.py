#

# Given a positive integer n, break it into the sum of at least two positive integers and maximize
# the product of those integers. Return the maximum product you can get.
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
#
# Note: You may assume that n is not less than 2 and not larger than 58.


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # latonn's
        # Explanation
        # https: // blog.csdn.net / liyuanbhu / article / details / 51198124
        res = 1
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        else:
            while n > 4:
                n -= 3
                res *= 3
        return res * n

        # kamyu's solution 1
        # if n < 4:
        #     return n - 1
        #
        # # integerBreak(n) = max(integerBreak(n - 2) * 2, integerBreak(n - 3) * 3)
        # ans = [0, 1, 2, 3]
        # for i in range(4, n + 1):
        #     ans[i % 4] = max(ans[(i - 2) % 4] * 2, ans[(i - 3) % 4] * 3)
        # return ans[n % 4]

        # kamyu's solution 2
        # if n < 4:
        #     return n - 1
        #
        # #  Proof.
        # #  1. Let n = a1 + a2 + ... + ak, product = a1 * a2 * ... * ak
        # #      - For each ai >= 4, we can always maximize the product by:
        # #        ai <= 2 * (ai - 2)
        # #      - For each aj >= 5, we can always maximize the product by:
        # #        aj <= 3 * (aj - 3)
        # #
        # #     Conclusion 1:
        # #      - For n >= 4, the max of the product must be in the form of
        # #        3^a * 2^b, s.t. 3a + 2b = n
        # #
        # #  2. To maximize the product = 3^a * 2^b s.t. 3a + 2b = n
        # #      - For each b >= 3, we can always maximize the product by:
        # #        3^a * 2^b <= 3^(a+2) * 2^(b-3) s.t. 3(a+2) + 2(b-3) = n
        # #
        # #     Conclusion 2:
        # #      - For n >= 4, the max of the product must be in the form of
        # #        3^Q * 2^R, 0 <= R < 3 s.t. 3Q + 2R = n
        # #        i.e.
        # #          if n = 3Q + 0,   the max of the product = 3^Q * 2^0
        # #          if n = 3Q + 2,   the max of the product = 3^Q * 2^1
        # #          if n = 3Q + 2*2, the max of the product = 3^Q * 2^2
        #
        # res = 0
        # if n % 3 == 0:            #  n = 3Q + 0, the max is 3^Q * 2^0
        #     res = 3 ** (n // 3)
        # elif n % 3 == 2:          #  n = 3Q + 2, the max is 3^Q * 2^1
        #     res = 3 ** (n // 3) * 2
        # else:                     #  n = 3Q + 4, the max is 3^Q * 2^2
        #     res = 3 ** (n // 3 - 1) * 4
        # return res


if __name__ == '__main__':
    n = 10
    print(Solution().integerBreak(n))