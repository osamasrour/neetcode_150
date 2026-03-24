# Longest Substring Without Repeating Characters: https://neetcode.io/problems/longest-substring-without-duplicates/question?list=neetcode150

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        unique = dict()
        lswr = 0
        if n == 1:
            return 1
        for i in range(n):
            if not unique.get(s[i]) : # the s[i] not in the unique hashmap
                unique[s[i]] = i
                lswr = max(lswr, len(unique))
            else:
                j = unique[s[i]]
                delete_keys = []
                for k, v in unique.items():
                    if v <= j:
                        delete_keys.append(k)
                for key in delete_keys:
                    del unique[key]
                unique[s[i]] = i
                lswr = max(lswr, len(unique))
        lswr = max(lswr, len(unique))
        return lswr