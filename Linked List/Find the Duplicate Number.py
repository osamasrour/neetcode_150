# Find the Duplicate Number: https://neetcode.io/problems/find-duplicate-integer/question?list=neetcode150

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast = nums[nums[0]]
        slow = nums[0]

        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow