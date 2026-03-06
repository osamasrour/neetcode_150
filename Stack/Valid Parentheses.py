# Valid Parentheses: https://neetcode.io/problems/validate-parentheses/question?list=neetcode150

class Solution:
    def isClose(self, open: str, close: str) -> bool:
    	Parentheses = {
    		"(": ")",
    		"{": "}",
    		"[": "]"
    	}

    	return Parentheses.get(open) == close



    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
        	if len(stack) == 0:
        		stack.append(p)
        	else:
        		if self.isClose(stack[-1], p): stack.pop()
        		else:
        			stack.append(p)
        return len(stack) == 0
