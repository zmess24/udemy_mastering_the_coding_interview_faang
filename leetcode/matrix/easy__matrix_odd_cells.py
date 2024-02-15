class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for index in indices:
            r1 = index[0]
            c2 = index[1]

            for col in range(len(matrix[0])):
                matrix[r1][col] += 1
            
            for row in range(len(matrix)):
                matrix[row][c2] += 1
        

        odd = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] % 2 == 1:
                    odd += 1
        
        return odd