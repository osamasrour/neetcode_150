# Best Time to Buy and Sell Stock: https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy = float("inf")
        profit = 0
        for i in range(n):
            if buy > prices[i]:
                buy = prices[i]
            profit = max(profit, prices[i] - buy)
        return profit
