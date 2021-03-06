#

# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
#
# Input:
# s = "abcd"
# t = "abcde"
#
# Output:
# e
#
# Explanation:
# 'e' is the letter that was added.


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict
        tDict = defaultdict(int)
        for c in t:
            tDict[c] += 1

        for c in s:
            tDict[c] -= 1
            if tDict[c] == 0:
                del tDict[c]

        return list(tDict.keys())[0]


if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t))


