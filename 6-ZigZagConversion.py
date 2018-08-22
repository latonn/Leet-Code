#

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
# display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        dirs, dirsub, pos = [1, -1], 0, 0
        result = [[] for _ in range(numRows)]
        print(result)
        for i in range(len(s)):
            if pos == 0:
                dirsub = 0
            elif pos == numRows - 1:
                dirsub = 1
            result[pos].append(s[i])
            pos += dirs[dirsub] if numRows > 1 else 0

        ans = []
        for j in range(numRows):
            ans += result[j]
        # print(ans)
        return "".join(ans)


if __name__ == "__main__":
    # s = "PAYPALISHIRING"
    # numRows = 4
    s = "AB"
    numRows = 1
    print(Solution().convert(s, numRows))
