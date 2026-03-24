# Longest Substring Without Repeating Characters: https://neetcode.io/problems/longest-substring-without-duplicates/question?list=neetcode150

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        unique = set()

        lswr = 0
        for i in range(n):
            if not unique:
                unique.add(s[i])
                lswr = 1
                continue
            if s[i] in unique:
                lswr = max(len(unique), lswr)
                unique.clear()
                unique.add(s[i])

            else:
                unique.add(s[i])
        lswr = max(len(unique), lswr)
        return lswr


obj = Solution()

s = "zxyzxyz"
print(obj.lengthOfLongestSubstring(s) == 3)

s = "xxxx"
print(obj.lengthOfLongestSubstring(s) == 1)

s=" "
print(obj.lengthOfLongestSubstring(s) == 1)

s="dvdf"
print(obj.lengthOfLongestSubstring(s) == 3)