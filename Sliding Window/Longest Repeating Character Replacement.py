# Longest Repeating Character Replacement: https://neetcode.io/problems/longest-repeating-substring-with-replacement/question?list=neetcode150

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l=0
        lrcr = 0
        windowSize = 0
        counter = dict()
        for r in range(n):
            counter[s[r]] = counter.get(s[r], 0) + 1
            mostFreq=max(counter.values())
            windowSize = r - l + 1
            if windowSize - mostFreq > k:
                counter[s[l]]-=1
                l += 1
            lrcr = max(lrcr, r-l+1)
        return lrcr