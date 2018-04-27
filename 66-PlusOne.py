#

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each
# element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry, newDigit = [], 0
        lastDigit = digits.pop()
        while lastDigit == 9:
            carry.append(0)
            if not digits:
                digits.append(1)
                newDigit = 1
                break
            else:
                lastDigit = digits.pop()

        if carry.count(0) == 0:
            return digits + [lastDigit + 1]
        else:
            if newDigit == 0:
               digits += [lastDigit + 1]
            while carry.count(0) != 0:
                digits.append(carry.pop())
        return digits


if __name__ == '__main__':
    digits = [2, 8, 9]
    print(Solution().plusOne(digits))
