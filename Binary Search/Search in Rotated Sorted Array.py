# Search in Rotated Sorted Array: https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=neetcode150
# TODO(#4): Prettify the code, make it less spaghetti.
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        l, r = 0, n-1
        if nums[l] == target: return l
        if nums[r] == target: return r
        while l <= r:
            m = l +((r - l) // 2)
            if nums[r] < nums[l]: # handle the un sorted part
                if target < nums[l]:
                    # the target in the R part
                    if nums[m] > nums[l]:
                        l = m + 1
                    else:  # nums[m] < nums[l]
                        if nums[m] < target:
                            l = m
                        elif nums[m] > target:
                            r = m
                        else:
                            return m
                elif target > nums[l]:
                    # the target in the L part
                    if nums[m] < nums[l]:
                        r = m - 1
                    else: # nums[m] > target
                        if nums[m] < target:
                            l = m + 1
                        elif nums[m] > target:
                            r = m + 1
                        else:
                            return m
                else:
                    return l
            else:
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
        if nums[m] == target:
            return m
        else:
            return -1
