#

# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the
# maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
#
# Note:
# The given number is in the range [0, 10^8]


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numlist = list(str(num))
        left = right = 0
        index = len(numlist) - 1
        for i in reversed(range(len(numlist))):
            if numlist[i] > numlist[index]:
                index = i
            elif numlist[index] > numlist[i]:
                left, right = i, index
        numlist[left], numlist[right] = numlist[right], numlist[left]

        return int("".join(numlist))


if __name__ == "__main__":
    num = 123
    print(Solution().maximumSwap(num))
