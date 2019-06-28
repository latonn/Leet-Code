#

# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
# [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result
# overflows.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # latonn's
        # using binary search method to avoid TIME LIMIT EXCEEDED
        polarity = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            dvsiter = divisor
            count = 1
            if dividend < dvsiter:
                break
            # mindset of binary search method
            while dividend >= dvsiter + dvsiter:
                dvsiter <<= 1
                count <<= 1
            dividend -= dvsiter
            quotient += count

        if polarity:
            return -quotient
        else:
            return quotient - 1 if quotient >= 2147483648 else quotient


if __name__ == "__main__":
    dividend, divisor = 7, -3
    print(Solution().divide(dividend, divisor))

