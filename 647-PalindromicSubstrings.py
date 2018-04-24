#

# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings
# even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
# Note:
# The input string length won't exceed 1000.


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) and ((i - j < 2) or dp[j+1][i-1])
                count = count + 1 if dp[j][i] else count
                # print(dp, count)
        return count + len(s)


if __name__ == '__main__':
    s = 'aba'
    print(Solution().countSubstrings(s))
