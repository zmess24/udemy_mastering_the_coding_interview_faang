# Define Directions
DIRECTIONS = [
    [-1, 0],  # Up
    [0, 1],   # Right
    [1, 0],   # Down
    [0, -1]   # Left
]

def removeIslands(matrix):
    # Initialize seen matrix with rows and cols equal to the input matrix
    seen = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # DFS Function to explore and mark the island
    def dfs(row, col, path):
        # Check if current row and col are out of bounds or already seen or is land (0)
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col] or matrix[row][col] == 0:
            return True

        # Check if the current cell is on the border, which makes it not an island
        if row == 0 or row == len(matrix) - 1 or col == 0 or col == len(matrix[0]) - 1:
            return False

        # Mark the current position as seen and add it to the path
        seen[row][col] = True
        path.append((row, col))

        is_island = True
        # Explore all four directions
        for direction in DIRECTIONS:
            # Get new row and column based on the direction
            newRow, newCol = row + direction[0], col + direction[1]
            # Recursively call dfs on the new row and column
            if not dfs(newRow, newCol, path):
                is_island = False

        return is_island

    # Mark row start & end, col start & end
    rowStart, rowEnd = 1, len(matrix) - 1
    colStart, colEnd = 1, len(matrix[0]) - 1
    # Iterate through each cell in the matrix (excluding borders)
    for row in range(rowStart, rowEnd):
        for col in range(colStart, colEnd):
            # If the current cell is part of an unvisited potential island
            if matrix[row][col] == 1 and not seen[row][col]:
                path = []
                if dfs(row, col, path):
                    # Convert all 1's to 0's for each index in the path if it's an island
                    for r, c in path: matrix[r][c] = 0

    # Return the modified matrix
    return matrix