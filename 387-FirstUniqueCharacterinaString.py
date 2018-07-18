#

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(list)
        for i in range(len(s)):
            if s[i] in count.keys():
                count[s[i]][1] += 1
            else:
                count[s[i]] = [i, 1]

        ans = [count[x][0] for x in count.keys() if count[x][1] == 1]
        return min(ans) if len(ans) > 0 else -1


if __name__ == '__main__':
    # s = 'leetcode'
    s = ''
    print(Solution().firstUniqChar(s))

