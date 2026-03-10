# Largest Rectangle In Histogram: https://neetcode.io/problems/largest-rectangle-in-histogram/question?list=neetcode150
# TODO(#3): it's O(n^2)
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)

        largest_area = -1
        for i in range(n):
            current_width = 1

            prev = i - 1
            while prev >= 0 and heights[prev] >= heights[i]:
                current_width+=1
                prev-=1

            _next = i + 1
            while _next < n and heights[_next] >= heights[i]:
                current_width += 1
                _next+=1

            area = current_width * heights[i]
            largest_area = max(largest_area, area)

        return largest_area
