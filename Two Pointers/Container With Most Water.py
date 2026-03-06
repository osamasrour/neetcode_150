# Container With Most Water: https://neetcode.io/problems/max-water-container/question?list=neetcode150

class Solution:
    def maxArea(self, heights: list[int]) -> int:
    	n = len(heights)
    	max_area = 0
    	l, r = 0, n - 1
    	while l < r:
    		d = r - l
    		h = min(heights[l], heights[r])
    		max_area = max(max_area, h * d)

    		if heights[l] < heights[r]:
    			l += 1
    		else:
    			r -= 1
    	return max_area

