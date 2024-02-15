# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rowLength = len(matrix) -1
        colLength = len(matrix[0]) - 1
        for row in range(rowLength):
            for col in range(colLength):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        
        return True
