# Depth First Search

directions = [
    [-1, 0], # Up
    [0, 1], # Right
    [1, 0], # Down
    [0, -1], # Left
]

def traversal(matrix):
    seen = []

    for i in range(len(matrix)):
        seen.append([False for j in range(len(matrix[0]))])
        
    values = []
    
    dfs(matrix, 0, 0, seen, values)

    return values

def dfs(matrix, row, col, seen, values):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col]: 
        return
    
    values.append(matrix[row][col])
    seen[row][col] = True
    
    for i in range(len(directions)):
        currentDir = directions[i]
        rowToCheck = row + currentDir[0]
        colToCheck =  col + currentDir[1]

        dfs(matrix, rowToCheck, colToCheck, seen, values)