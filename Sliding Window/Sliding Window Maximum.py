# Sliding Window Maximum: https://neetcode.io/problems/sliding-window-maximum/question?list=neetcode150

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        iter_count = n - k + 1

        res = []
        for l in range(iter_count):
            r = l + k - 1
            res.append(max(nums[l: r + 1]))
        
        return res