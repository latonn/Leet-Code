#

# Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad
# for each step:
#
# Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps
# permitted. Output the minimum number of steps to get n 'A'.
#
# Example 1:
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Note:
# The n will be in the range [1, 1000].

import math


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        primeArray = []
        for i in range(2, n+1):
            if self.isPrime(i):
                dp[i] = i
                primeArray.append(i)
            else:
                for j in primeArray:
                    if i % j == 0:
                        maxFactor = int(i/j)
                        dp[i] = dp[maxFactor] + int(i/maxFactor)
                        break
                print(dp, primeArray)
        return dp[n]

    def isPrime(self, num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


if __name__ == '__main__':
    n = 8
    print(Solution().minSteps(n))
