# Valid Anagram : https://neetcode.io/problems/is-anagram/question?list=neetcode150

class Solution:

    def make_map(self, s: str) -> dict:
        d: dict[str, int] = dict()
        
        for i in s:
            if i in d.keys():
                val = d.get(i)
                d[i] = val+1;
            else:
                d.update({i: 1})
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        map_s = self.make_map(s)
        map_t = self.make_map(t)
        if len(map_s) != len(map_t): return False
        for k, v in map_s.items():
            if map_t.get(k) != map_s.get(k): return False
        return True
