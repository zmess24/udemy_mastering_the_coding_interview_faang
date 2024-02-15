# https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right = 0, len(matrix[0])
        top, down = 0, len(matrix)

        while left < right and top < down:
            # Iterate left to right
            for col in range(left, right):
                ans.append(matrix[top][col])
            top += 1

            # Iterate up to down
            for row in range(top, down):
                ans.append(matrix[row][right-1])
            right -= 1

            if not (left < right and top < down):
                break

            # Iterate right to left
            for col in range(right, left, -1):
                ans.append(matrix[down-1][col-1])
            down -= 1
            
            # Iterate down to up
            for row in range(down, top, -1):
                ans.append(matrix[row-1][left])
            left += 1

        return ans