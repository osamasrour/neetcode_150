# Products of Array Except Self: https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
    	n = len(nums)
    	preff = [1] * n
    	suff = [1] * n
    	res = [0] * n

    	for i in range(1, n):
    		preff[i] = nums[i - 1] * preff[i - 1]

    	for i in range(n -2, -1, -1):
    		suff[i] = nums[i + 1] * suff[i + 1]


    	for i in range(n):
    		res[i] = preff[i] * suff[i]

    	return res

