# Find Minimum in Rotated Sorted Array: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=neetcode150

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        if n == 1: return nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        else:
            while l < r:
                m = l+((r- l) // 2)
                if nums[m] < nums[m + 1] and nums[m] < nums[0]:
                    r = m
                else:
                    l = m + 1
            return nums[l]