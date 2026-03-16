# Search in Rotated Sorted Array: https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=neetcode150

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n-1
        while l < r:
            m = l +((r - l) // 2)
            if target <= nums[m] and target < nums[l]:
                l = m + 1
            else:
                r = m
        if nums[m] == target:
            return m
        else:
            return -1



obj = Solution()

nums = [3,4,5,6,1,2]
target = 1
print(obj.search(nums, target) == 4)

nums = [3,5,6,0,1,2]
target = 4
print(obj.search(nums, target) == -1)
