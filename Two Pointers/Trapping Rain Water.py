# Trapping Rain Water: https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150
# TODO: make it O(n)
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n < 2: return 0
        start_idx = 0
        end_idx = n - 1
        for i in range(n):
        	if height[start_idx] < height[start_idx + 1]:
        		start_idx += 1
        	if height[end_idx] < height[end_idx -1]:
        		end_idx -= 1
        max_area = 0

        max_val = 0
        for i in range(start_idx, end_idx + 1):
        	max_val = max(height[i], max_val)
        for h in range(max_val, 0, -1):
        	arr_of_hs = []
        	for i in range(n):
        		if height[i] >= h:
        			arr_of_hs.append(i)
        	arr_len = len(arr_of_hs)
        	for j in range(arr_len - 1):
        		k = j + 1
        		area = (arr_of_hs[k] - arr_of_hs[j] - 1)
        		max_area += area
        return max_area
