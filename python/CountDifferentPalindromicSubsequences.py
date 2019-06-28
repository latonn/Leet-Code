class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        # refer from http://bookshadow.com/weblog/2017/11/20/leetcode-count-different-palindromic-subsequences/
        size = len(S)
        next = [{k : -1 for k in 'abcd'} for x in range(size + 1)]
        prev = [{k : -1 for k in 'abcd'} for x in range(size + 1)]
        for x in range(size):
            for k in 'abcd':
                if S[x] == k: prev[x][k] = x
                else: prev[x][k] = prev[x - 1][k]

        for x in range(size - 1, -1, -1):
            for k in 'abcd':
                if S[x] == k: next[x][k] = x
                else: next[x][k] = next[x + 1][k]

        dmap = [[0] * (size + 1) for x in range(size + 1)]

        def solve(i, j):
            if i > j: return 0
            if dmap[i][j]: return dmap[i][j]
            ans = 0
            for k in 'abcd':
                ii, jj = next[i][k], prev[j][k]
                if ii < 0: continue
                if ii < jj: ans += 1
                if ii <= j: ans += solve(ii + 1, jj - 1) + 1
            dmap[i][j] = ans % (10 ** 9 + 7)
            return dmap[i][j]

        return solve(0, size - 1)
