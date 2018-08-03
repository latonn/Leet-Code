#

# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
#
# Example 1:
# Input: "A"
# Output: 1
#
# Example 2:
# Input: "AB"
# Output: 28
#
# Example 3:
# Input: "ZY"
# Output: 701


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # latonn's
        sList = list(s)

        ans = pos = 0
        while sList:
            ans += (ord(sList.pop()) - ord("A") + 1) * (26 ** pos) if pos > 0 else (ord(sList.pop()) - ord("A") + 1)
            pos += 1
            # print(ans, sList)
        return ans


if __name__ == "__main__":
    s = "AAA"
    print(Solution().titleToNumber(s))
