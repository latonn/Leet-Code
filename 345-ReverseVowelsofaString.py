#

# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # latonn's
        left, right = 0, len(s) - 1
        slist = list(s)
        while True:
            while left < len(s) and slist[left].lower() not in 'aeiou':
                left += 1
            while right > 0 and slist[right].lower() not in 'aeiou':
                right -= 1

            if left >= right:
                break

            slist[left], slist[right] = slist[right], s[left]
            left += 1
            right -= 1
        return ''.join(slist)


if __name__ == '__main__':
    s = 'a.'
    print(Solution().reverseVowels(s))
