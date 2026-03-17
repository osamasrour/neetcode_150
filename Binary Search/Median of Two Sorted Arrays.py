# Median of Two Sorted Arrays: https://neetcode.io/problems/median-of-two-sorted-arrays/question?list=neetcode150

# TODO(#5): This solution needs to be more explained.

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        is_odd = not (half * 2 == total)

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - (i + 1) -1

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if is_odd:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1 
