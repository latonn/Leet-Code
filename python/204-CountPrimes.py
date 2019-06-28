#

# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # latonn's
        if n < 3:
            return 0

        ans = [1] * n
        ans[0] = ans[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if ans[i] == 1:
                for j in range(i+i, n, i):
                    ans[j] = 0
        # print(ans)
        return sum(ans)


if __name__ == "__main__":
    n = 10
    print(Solution().countPrimes(n))

