# Evaluate Reverse Polish Notation: https://neetcode.io/problems/evaluate-reverse-polish-notation/question?list=neetcode150
import math
class Solution:

	def operate(self, lhs: int, operation: str, rhs: int) -> int:
		if operation == "+":
			return lhs + rhs
		elif operation == "-":
			return lhs - rhs
		elif operation == "*":
			return lhs * rhs
		elif operation == "/":
			# return math.ceil(lhs / rhs) # round up
			# return math.floor(lhs / rhs) # round down
			if (lhs > 0 and rhs > 0) or (lhs < 0 and rhs < 0):
				return math.floor(lhs / rhs)
			else:
				return math.ceil(lhs / rhs)

		else:
			raise ValueError(f"Unkown opration`{opration}`")

	def evalRPN(self, tokens: list[str]) -> int:
		stack = []
		n = len(tokens)
		for i in range(n):
			stack.append(tokens[i])
			if tokens[i] in "/*-+":
				stackLenght = len(stack)
				result = self.operate(int(stack[stackLenght - 3]), stack[stackLenght - 1], int(stack[stackLenght - 2]))
				for _ in range(3): stack.pop()
				stack.append(str(result))
		assert(len(stack) == 1)
		return int(stack[0])
