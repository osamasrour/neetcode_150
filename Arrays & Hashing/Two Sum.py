# Two Sum : https://neetcode.io/problems/two-integer-sum/question?list=neetcode150

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums), 1):
        	for j in range(len(nums) -1, -1, -1):
        		if (nums[i] + nums[j] == target) and i != j:
        			return [i, j]
