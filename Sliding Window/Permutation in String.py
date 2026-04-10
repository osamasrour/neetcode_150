# Permutation in String : https://neetcode.io/problems/permutation-string/question?list=neetcode150

class Solution:

    def makeHashMap(self, string: str) -> dict[str, int] :
        d = dict()
        for i in range(len(string)):
            if d.get(string[i]) != None:
                d[string[i]] += 1
            else:
                d[string[i]] = 1
        return d


    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1= len(s1)
        n2= len(s2)

        hm1 = self.makeHashMap(s1)
        l = 0
        while l < n2 - n1 + 1:
            match_counter = 0
            hm2Window = self.makeHashMap(s2[l: l + n1])
            for k, v in hm2Window.items():
                if hm1.get(k) == v:
                    match_counter += 1
            if match_counter == len(hm1):
                return True
            l+= 1
        return False