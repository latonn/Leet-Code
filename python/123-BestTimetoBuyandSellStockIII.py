#

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy
# again).
#
# Example 1:
#
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        p1 = [0 for _ in range(len(prices))]
        p2 = [0 for _ in range(len(prices))]

        p1[0] = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            p1[i] = max(p1[i-1], prices[i] - minPrice)

        p2[-1] = 0
        maxPrice = prices[-1]
        for j in range(len(prices) - 2, -1, -1):
            maxPrice = max(maxPrice, prices[j])
            p2[j] = max(p2[j+1], maxPrice - prices[j])

        ans = 0
        for i in range(len(prices)):
            if p1[i] + p2[i] > ans:
                ans = p1[i] + p2[i]

        return ans


if __name__ == "__main__":
    prices = [3, 3, 5, 0, 0, 3, 1, 4, 0]
    print(Solution().maxProfit(prices))

