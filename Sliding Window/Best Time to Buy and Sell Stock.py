# Best Time to Buy and Sell Stock: https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # naive approach 26ms
        n = len(prices)
        profit = 0
        for i in range(n):
            buy = prices[i]
            for j in range(i + 1, n):
                sell = prices[j]
                profit = max(profit, sell - buy)

        return profit
obj = Solution()

prices = [10,1,5,6,7,1]
print(obj.maxProfit(prices) == 6)

prices = [10,8,7,5,2]
print(obj.maxProfit(prices) == 0)