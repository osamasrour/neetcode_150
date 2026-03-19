# Trapping Rain Water: https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        full_area = 0
        max_l = 0
        l_wall = [0]
        for i in range(n):
            if height[i] >= max_l:
                max_l = height[i]
                l_wall.append(max_l)
            else:
                l_wall.append(max_l)
        
        max_r = 0
        r_wall = [0]
        for i in range(n - 1, -1, -1):
            if height[i] >= max_r:
                max_r = height[i]
                r_wall.append(max_r)
            else:
                r_wall.append(max_r)

        for i in range(n):
            area = min(l_wall[i], r_wall[n - i - 1]) - height[i]
            full_area += max(0, area)

        return full_area