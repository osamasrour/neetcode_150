# Longest Consecutive Sequence: https://neetcode.io/problems/longest-consecutive-sequence/question?list=neetcode150
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        nums_set = set(nums)
        min_n = nums[0]
        max_n = nums[0]
        for i in nums:
        	if min_n > i: min_n = i
        	if max_n < i: max_n = i

        visit_lst = [None] * (max_n - min_n + 1)
        for i in range(min_n, max_n + 1):
        	if not (i in nums_set):
        		visit_lst[i - min_n] = None
        	else:
        		visit_lst[i - min_n] = 1
        
        longest_count = 0
        currunt_count = 0
        for i in visit_lst:
        	if i == 1:
        		currunt_count += 1
        		if longest_count < currunt_count:
        			longest_count = currunt_count
        	else:
        		currunt_count = 0
        return longest_count
