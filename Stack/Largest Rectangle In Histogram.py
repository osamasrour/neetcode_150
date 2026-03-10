# Largest Rectangle In Histogram: https://neetcode.io/problems/largest-rectangle-in-histogram/question?list=neetcode150
# TODO(#3): it's O(n^2)
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        largest_area = 0
        stack: list[tuple[int, int]] = []
        for i in range(n):
            skiped = 0
            while stack and heights[i] < stack[-1][1]:
                poped_idx, poped_value = stack.pop()
                poped_area = poped_value * (i - poped_idx)
                skiped+=1
                largest_area = max(poped_area, largest_area)
            if stack:
                stack.append((i - skiped, heights[i]))
            else:
                stack.append((0, heights[i]))
        for i in range(len(stack)):
            poped_idx, poped_value = stack.pop()
            poped_area = poped_value * (n - poped_idx)
            largest_area = max(poped_area, largest_area)       
        return largest_area


obj = Solution()
heights = [7,1,7,2,2,4]
print(obj.largestRectangleArea(heights) == 8)
heights = [1,3,7]
print(obj.largestRectangleArea(heights) == 7)
heights=[3,6,5,7,4,8,1,0]
# index=[0,1,2,3,4,5,6,7]
"""
(3, 0) x 18
(6, 1) x 6
(5, 1) x 18
(7, 3) x 7
(4, 2) x 16
(8, 5) x 8
(1, 3)
"""
print(obj.largestRectangleArea(heights) == 20)