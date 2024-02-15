# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            found = self.binarySearch(matrix[row], target)
            if found:
                return True
        
        return False

    def binarySearch(self, row, target):
        left, right = 0, len(row) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target == row[mid]:
                return True
            elif target < row[mid]:
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1
        
        return False