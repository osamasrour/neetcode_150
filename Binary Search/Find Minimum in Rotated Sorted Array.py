# Find Minimum in Rotated Sorted Array: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=neetcode150

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        current_min = float("inf")
        l, r = 0, n-1
        if n == 1: return nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        else:
            while l < r:
                m = l+((r- l) // 2)
                if nums[m] < nums[m + 1] and nums[m] < nums[l]: # WARNING: out of range for the one element array
                    r = m
                else:
                    l = m + 1
            return nums[l]






obj = Solution()

nums = [3,4,5,6,1,2]
print(obj.findMin(nums) == 1)

nums = [4,5,0,1,2,3]
print(obj.findMin(nums) == 0)

nums = [4,5,6,7]
print(obj.findMin(nums) == 4)

nums = [4]
print(obj.findMin(nums) == 4)

nums = [4, 5]
print(obj.findMin(nums) == 4)

nums = [5, 4]
print(obj.findMin(nums) == 4)

nums=[3,4,5,1,2]
print(obj.findMin(nums) == 1)