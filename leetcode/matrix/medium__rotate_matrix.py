class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) -1

        # Step 1. Reverse Matrix (e.g swap order of row)
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1
        
        # Swap rows with columns (e.g transpose)
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        return matrix