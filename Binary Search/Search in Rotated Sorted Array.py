# Search in Rotated Sorted Array: https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=neetcode150

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while r >= l:
            m = (l + r) // 2
            
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]: # we are in the left sorted part
                if nums[l] <= target < nums[m]: # the target in this part
                    r = m - 1
                else:
                    l = m + 1
            else: # we are in the right sorted part
                if nums[r] >= target > nums[m]: # the target in this part
                    l = m + 1
                else:
                    r = m - 1
        return -1