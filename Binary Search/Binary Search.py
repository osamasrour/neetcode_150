# Binary Search: https://neetcode.io/problems/binary-search/question?list=neetcode150
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            middle = (l + r) // 2
            if target < nums[middle]:
                r = middle - 1
            elif target > nums[middle]:
                l = middle + 1
            else:
                return middle
        return -1