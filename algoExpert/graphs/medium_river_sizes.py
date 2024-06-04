# Define directions for moving up, right, down, and left
DIRECTIONS = [ 
    [-1, 0],  # Up
    [0, 1],   # Right
    [1, 0],   # Down
    [0, -1],  # Left
]

def riverSizes(matrix):
    # Initialize seen matrix with rows and cols equal to the input matrix
    seen = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Initialize answer array
    rivers = []
    
    # DFS function to calculate the size of a river
    def dfs(row, col):
        # Check if the current position is out of bounds or already seen or is land (0)
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col] or matrix[row][col] == 0: 
            return 0
        
        # Mark the current position as seen
        seen[row][col] = True

        # Initialize river size for this DFS call
        riverSize = 1
        
        # Explore all four directions
        for direction in DIRECTIONS:
            newRow, newCol = row + direction[0], col + direction[1]
            riverSize += dfs(newRow, newCol)

        return riverSize
    
    # Iterate through each row
    for row in range(len(matrix)):
        # Iterate through each column in the current row
        for col in range(len(matrix[0])):
            # If the current cell is part of a river and has not been seen
            if matrix[row][col] == 1 and not seen[row][col]:
                # Conduct DFS to find the size of the river
                riverSize = dfs(row, col)
                # Add the river size to the answer array
                rivers.append(riverSize)
    
    # Return the array of river sizes
    return rivers