#

# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
# Input: 27
# Output: true
# Example 2:
#
# Input: 0
# Output: false
# Example 3:
#
# Input: 9
# Output: true
# Example 4:
#
# Input: 45
# Output: false
#
# Follow up:
# Could you do it without using any loop / recursion?


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # latonn's
        while n >= 3:
            if n % 3 != 0:
                return False
            n = int(n/3)
        return True if n == 1 else False

        # kamyu's
        # https://github.com/kamyu104/LeetCode/blob/master/Python/power-of-three.py
        # return n > 0 and (math.log10(n) / math.log10(3)).is_integer()


if __name__ == '__main__':
    n = 0
    print(Solution().isPowerOfThree(n))
