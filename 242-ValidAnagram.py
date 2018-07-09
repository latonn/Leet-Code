# Time:  O(n)
# Space: O(1)

# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
import string


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # latonn's
        # cnts = [0] * 26
        # for c in t:
        #     cnts[ord(c) - ord('a')] += 1
        # left = 0
        # while left < len(s):
        #     cnts[ord(s[left]) - ord('a')] -= 1
        #     left += 1
        # return True if cnts.count(0) == 26 else False

        # kamyu's
        return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
