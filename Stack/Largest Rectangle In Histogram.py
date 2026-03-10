# Largest Rectangle In Histogram: https://neetcode.io/problems/largest-rectangle-in-histogram/question?list=neetcode150
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        largest_area = 0
        stack: list[tuple[int, int, int]] = []
        #               real, start, value
        for i in range(n):
            skiped = 0
            while stack and heights[i] < stack[-1][2]:
                poped_real, poped_idx, poped_value = stack.pop()
                poped_area = poped_value * (i - poped_idx)
                skiped+=1
                largest_area = max(poped_area, largest_area)
            if stack:
                stack.append((i, stack[-1][0] + 1, heights[i]))
            else:
                stack.append((i, 0, heights[i]))
        for i in range(len(stack)):
            poped_real, poped_idx, poped_value = stack.pop()
            poped_area = poped_value * (n - poped_idx)
            largest_area = max(poped_area, largest_area)       
        return largest_area
