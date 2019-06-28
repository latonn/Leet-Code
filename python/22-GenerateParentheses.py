#

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def helper(self, tot, l, r, pars, result):
        if l < tot:
            self.helper(tot, l + 1, r, pars + '(', result)
        if r < tot and r < l:
            self.helper(tot, l, r + 1, pars + ')', result)
        if l == tot and r == tot:
            result.append(pars)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.helper(n, 0, 0, '', result)
        return result


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))
