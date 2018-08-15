# Time:  O(n)
# Space: O(1)

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
#
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
# Note
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.:


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # kaymu's
        def validPalindromeHelper(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return validPalindromeHelper(s, left, right - 1) or validPalindromeHelper(s, left + 1, right)
            left, right = left + 1, right - 1
        return True


if __name__ == '__main__':
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print(Solution().validPalindrome(s))
