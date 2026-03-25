# Longest Repeating Character Replacement: https://neetcode.io/problems/longest-repeating-substring-with-replacement/question?list=neetcode150

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        p1=p2=0
        consume_k = 0

        lrcr = 0;
        curr_c = s[0]
        for i in range(1, n):
            c = s[i]
            if c == curr_c:
                p2 += 1
                print(f"p2 = {p2}")
            else:
                if (k - consume_k) > 0:
                    consume_k+=1
                else:
                    p1 = p2 + 1
                    p2 = p1
                    if p1 + 1 >= n:
                        break
                    i = p1
                    curr_c = s[i]
                    print(f"curr_c = {curr_c}")
                    consume_k = 0
            lrcr = max(lrcr, p2 - p1 + consume_k + 1)
        print(f"lrcr = {lrcr}")
        return lrcr


obj = Solution()

s = "XYYX"
k = 2
print(obj.characterReplacement(s, k) == 4)

s = "AAABABB"
k = 1
print(obj.characterReplacement(s, k) == 5)

s="AAAB"
k=0
print(obj.characterReplacement(s, k) == 3)

s="ABAA"
k=0
print(obj.characterReplacement(s, k) == 2)

s="ABBB"
k=2
print(obj.characterReplacement(s, k) == 4)