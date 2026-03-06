# Min Stack: https://neetcode.io/problems/minimum-stack/question?list=neetcode150

class MinStack:

    def __init__(self):
    	self.stack = []
    	self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stack) == 1:
        	self.min_stack.append(val)
        elif self.min_stack[-1] >= val:
        	self.min_stack.append(val)

    def pop(self) -> None:
    	popped = self.stack.pop()
    	if self.min_stack[-1] == popped:
    		self.min_stack.pop()
        

    def top(self) -> int:
    	return self.stack[-1]
        

    def getMin(self) -> int:
    	return self.min_stack[-1]
