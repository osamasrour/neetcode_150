# Two Integer Sum II: https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        last = n - 1
        front = 0
        while numbers[front] + numbers[last] != target:
        	if numbers[front] + numbers[last] > target:
        		last -= 1
        	else:
        		front+= 1
        return [front+1, last+1]

        	