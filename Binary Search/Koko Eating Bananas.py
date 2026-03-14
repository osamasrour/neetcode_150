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
        max_val = 0
        for e in piles:
            max_val = max(max_val, e)
        l, r = 1, max_val
        # print([x for x in range(l, max_val + 1)])
        max_k_time = 0
        k_result = -1
        while l <= r:
            k = (l + r) // 2
            k_time = self.eatTime(k, piles)
            # print(f"l = {l}, r = {r}")
            if k_time > h:
                l = k + 1
            elif k_time < h:
                r = k - 1
                if k_time > max_k_time:
                    max_k_time = k_time
                    k_result = k
            
            else:
                if k_time > max_k_time:
                    max_k_time = k_time
                    k_result = k
                break
            # print(f"k = {k}, k_time = {k_time}")
            # print(f"l = {l}, r = {r}")
            # input()
        return k_result






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

piles=[312884470]
h=312884469
print(obj.minEatingSpeed(piles, h) == 2)

piles=[332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
h=823855818
print(obj.minEatingSpeed(piles, h) == 14)

piles=[1,1,1,999999999]
h=10
print(obj.minEatingSpeed(piles, h) == 142857143)