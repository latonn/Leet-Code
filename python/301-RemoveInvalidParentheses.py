#

# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
# Input: "()())()"
# Output: ["()()()", "(())()"]
#
# Example 2:
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
#
# Example 3:
# Input: ")("
# Output: [""]


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # refer from http://bookshadow.com/weblog/2015/11/05/leetcode-remove-invalid-parentheses/
        def dfs(s):
            init = calc(s)
            if init == 0:
                return [s]

            ans = []
            for i in range(len(s)):
                if s[i] in ('(', ')'):
                    ns = s[:i] + s[i+1:]
                    if ns not in visited and calc(ns) < init:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans

        def calc(s):
            lp = rp = 0
            for c in s:
                lp += {'(': 1, ')': -1}.get(c, 0)
                rp += lp < 0
                lp = max(lp, 0)
            return lp + rp

        visited = set([s])
        return dfs(s)


if __name__ == "__main__":
    s = "()())()"
    print(Solution().removeInvalidParentheses(s))
