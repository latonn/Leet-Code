#

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of
# the substring together.You may assume the given string consists of lowercase English letters only and its length will
# not exceed 10000.
#
# Example 1:
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
#
# Example 2:
# Input: "aba"
# Output: False
#
# Example 3:
# Input: "abcabcabcabc"
# Output: True
# Explanation: It 's the substring "abc" four times. (And the substring "abcabc" twice.)


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # latonn's
        sub = ""
        for i in range(len(s)):
            sub = sub + s[i]
            j = i + 1
            if len(s) % len(sub) == 0:
                while j != len(s) - len(sub):
                    if s[j:j+len(sub)] != sub:
                        break
                    j += len(sub)
            if j == len(s) - len(sub) and s[j:j+len(sub)] == sub:
                return True
            else:
                continue
        return False


if __name__ == "__main__":
    s = "bb"
    print(Solution().repeatedSubstringPattern(s))
