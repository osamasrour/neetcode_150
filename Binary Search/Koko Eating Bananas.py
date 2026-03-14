# Koko Eating Bananas: https://neetcode.io/problems/eating-bananas/question?list=neetcode150

from math import ceil
class Solution:
    def eatTime(self, k, piles):
        totalTime = 0
        n = len(piles)
        for i in range(n):
            pile_time = (ceil(piles[i] / k))
            totalTime += pile_time
        return totalTime


    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        max_eat = 0
        max_val = 0
        min_val = float("inf")
        for i in piles:
            max_val = max(max_val, i)
            min_val = min(min_val, i)

        pair = dict() # eatTime: k
        for i in range(max_val, min_val - 1, -1):
            x = self.eatTime(i, piles)
            pair[x] = i
            if x <= h:
                max_eat = max(max_eat, x)
        return pair[max_eat]





obj = Solution()

piles = [1,4,3,2]
h = 9
print(obj.minEatingSpeed(piles, h) == 2)

piles = [25,10,23,4]
h = 4
print(obj.minEatingSpeed(piles, h) == 25)

piles=[3,6,7,11]
h = 8
print(obj.minEatingSpeed(piles, h) == 4)
exit()
piles=[312884470]
h=312884469
print(obj.minEatingSpeed(piles, h) == 2)

piles=[332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
h=823855818
print(obj.minEatingSpeed(piles, h) == 14)