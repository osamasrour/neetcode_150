# Minimum Window Substring: https://neetcode.io/problems/minimum-window-with-characters/question?list=neetcode150

class Solution:
    def makeHashMap(self, string: str) -> dict[str, int] :
        d = dict()
        for i in range(len(string)):
            if d.get(string[i]) != None:
                d[string[i]] += 1
            else:
                d[string[i]] = 1
        return d

    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)

        hms = self.makeHashMap(s)
        hmt = self.makeHashMap(t)

        l, r = 0, ns - 1
        while r - l + 1 >= nt:
            if s[l] in hmt and s[r] in hmt:
                if hms[s[l]] > hmt[s[l]] and hms[s[r]] == hmt[s[r]]:
                    hms[s[l]]-=1
                    l +=1
                    continue

                elif hms[s[l]] == hmt[s[l]] and hms[s[r]] > hmt[s[r]]:
                    hms[s[r]]-=1
                    r-=1
                    continue

                elif hms[s[l]] == hmt[s[l]] and hms[s[r]] == hmt[s[r]]:
                    return s[l:r+1]

                else:
                    rec_l = self.minWindow(s[l+1:r+1], t)
                    rec_r = self.minWindow(s[l:r], t)
                    return rec_l if len(rec_l) < len(rec_r) else rec_r

            if s[l] not in hmt:
                l += 1
                continue
            if s[r] not in hmt:
                r -= 1
                continue

        return ""