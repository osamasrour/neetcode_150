#Valid Sudoku: https://neetcode.io/problems/valid-sudoku/question?list=neetcode150

class Solution:

	def is_valid_list(self, lst: list) -> bool:
		lst_h = set(lst)
		temp_lst = [x for x in lst if x != "."]
		return len(lst_h) -1 == len(temp_lst) 

	def isValidSudoku(self, board: list[list[str]]) -> bool:
		for i in range(0, 9):
			if self.is_valid_list(board[i]) != True:
				return False

		for i in range(0, 9):
			if self.is_valid_list([board[0][i], board[1][i], board[2][i], 
									board[3][i], board[4][i], board[5][i], 
									board[6][i], board[7][i], board[8][i]]) != True:
				return False

		row = 0
		col = 0
		for i in range(3):
			row = i * 3
			for j in range(3):
				col = j * 3
				if self.is_valid_list([board[row + 0][col + 0], board[row + 1][col + 0], board[row + 2][col + 0], 
						board[row + 0][col + 1], board[row + 1][col + 1], board[row + 2][col + 1], 
						board[row + 0][col + 2], board[row + 1][col + 2], board[row + 2][col + 2]]) != True:
					return False
		return True
