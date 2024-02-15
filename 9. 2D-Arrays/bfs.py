# Breadth First Search

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
    queue = [[0,0]]

    while len(queue):
        currentPosition = queue.pop(0)
        row, col = currentPosition[0], currentPosition[1]

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]:
            continue

        seen[row][col] = True
        values.append(matrix[row][col])

        for i in range(len(directions)):
            currentDir = directions[i]
            rowToCheck = row + currentDir[0]
            colToCheck = col + currentDir[1]

            queue.append([rowToCheck, colToCheck])


    return values
