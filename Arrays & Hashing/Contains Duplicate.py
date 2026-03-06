# Contains Duplicate: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = len(nums)
        hash_of_list = set(nums)
        return False if len(hash_of_list) == nums_count else True

        
