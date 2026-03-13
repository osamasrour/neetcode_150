# Search a 2D Matrix: https://neetcode.io/problems/search-2d-matrix/question?list=neetcode150
from math import ceil
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix[0]) # number of elements in one row
        m = len(matrix) # number of rows
        length = m * n
        l, r = 1, length
        while l <= r:
            middle  = ((l + r) // 2)
            middleM = ceil(middle / n) -1
            middleN = (middle % n) -1
            if matrix[middleM][middleN] > target:
                r = middle - 1
            elif matrix[middleM][middleN] < target:
                l = middle + 1
            else:
                return True
        return False

obj = Solution()

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
print(obj.searchMatrix(matrix, target) == True)

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 15
print(obj.searchMatrix(matrix, target) == False)

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=13
print(obj.searchMatrix(matrix, target) == False)

matrix=[[1,3]]
target=1
print(obj.searchMatrix(matrix, target) == True)

matrix=[[1]]
target=0
print(obj.searchMatrix(matrix, target) == False)

matrix=[[1,1]]
target=2
print(obj.searchMatrix(matrix, target) == False)
