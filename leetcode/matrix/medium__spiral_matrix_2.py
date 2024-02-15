class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0]* n for _ in range(n)]
        left, right = 0, n
        top, down = 0, n
        value = 1

        while left < right:

            # Iterate left
            for col in range(left, right):
                arr[top][col] = value
                value += 1
            top += 1

            # Iterate down
            for row in range(top, down):
                arr[row][right-1] = value
                value += 1
            right -=1

            # Iterate right
            for col in range(right, left, -1):
                arr[down-1][col-1] = value
                value += 1
            down -= 1

            # Iterate up
            for row in range(down, top, -1):
                arr[row-1][left] = value
                value += 1
            left += 1
    
        return arr