# Koko Eating Bananas: https://neetcode.io/problems/eating-bananas/question?list=neetcode150

from math import ceil
class Solution:
    def isValidEatTime(self, k, piles, h):
        totalTime = 0
        n = len(piles)
        for i in range(n):
            pile_time = (ceil(piles[i] / k))
            totalTime += pile_time
        return totalTime <= h


    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        max_val = max(piles)
        l, r = 1, max_val
        k = 0
        while l <= r:
            m = ((l + r) // 2)
            if self.isValidEatTime(m, piles, h):
                k = m
                r = m - 1
            else:
                l = m + 1
        return k