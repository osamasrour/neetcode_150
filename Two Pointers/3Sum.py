# 3Sum: https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
    	n = len(nums)
    	hashmap = dict()
    	res = set()

    	for i in range(n):
    		hashmap[nums[i]] = i

    	for i in range(0, n):
    		for j in range(i, n):
    			val = -(nums[i] + nums[j])
    			if i != j and val in hashmap and hashmap[val] not in [j, i]:
    				tri = sorted([nums[i], nums[j], val])
    				res.add(tuple(tri))
    	return list(res)
