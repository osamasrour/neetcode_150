# Permutation in String : https://neetcode.io/problems/permutation-string/question?list=neetcode150

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1= len(s1)
        n2= len(s2)

        # check if s1 is permutation of s2
        h1 = set(s1)
        for l in range(0, n2 - n1 + 1):
            counter = 0
            container = set()
            for i in range(n1):
                if s2[l + i] in h1 and s2[l + i] not in container:
                    counter += 1
                    container.add(s2[l+i])
                    print("s2[l] = `", s2[l], "`, s2[l+i] = `", s2[l+i], "`, counter = ", counter)

            if counter == n1: return True
        return False
        



s1 = "abc"
s2 = "lecabee"
print(Solution().checkInclusion(s1, s2) == True)

s1 = "abc"
s2 = "lecaabee"
print(Solution().checkInclusion(s1, s2) == False)

s1="adc"
s2="dcda"
print(Solution().checkInclusion(s1, s2) == True)

s1="trinitrophenylmethylnitramine"
s2="dinitrophenylhydrazinetrinitrophenylmethylnitramine"
print(Solution().checkInclusion(s1, s2) == True)


