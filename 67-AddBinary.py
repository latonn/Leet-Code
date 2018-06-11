#

# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        i, j, sum = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or sum == 1:
            sum += int(a[i]) if i >= 0 else 0
            sum += int(b[j]) if j >= 0 else 0
            res = str(int(sum % 2)) + res
            i, j, sum = i-1, j-1, sum/2
        return res


if __name__ == '__main__':
    a = '11'
    b = '1'
    print(Solution().addBinary(a, b))

