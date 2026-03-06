# Valid Palindrome: https://neetcode.io/problems/is-palindrome/question?list=neetcode150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set(list("abcdefghijklmnopqrstuvwxyz0123456789"))
        new_s = ""
        lower_s = s.lower()
        for i in lower_s:
        	if i not in alphanumeric:
        		continue
        	new_s += i
        print(new_s)
        n = len(new_s)

        for i in range(n):
        	if new_s[i] != new_s[n - i - 1]:
        		return False
        return True
