#
#

# Given a non-empty string s and a dictionary wordDict containing a list
# of non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words. You may assume the dictionary
# does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]


if __name__ == '__main__':
    s = 'abcd'
    wordDict = ['a', 'abc', 'b', 'cd']
    print(Solution().wordBreak(s, wordDict))
