# With BFS

directions = [
    [-1, 0], # Up
    [0, 1], # Right
    [1, 0], # Down
    [0, -1] # Left
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    # Reverse to 0
                    grid[row][col] = "0"
                    # Reverse all connected 1 to 0 using BFS
                    queue = [[row, col]]

                    while len(queue):
                        currPosition = queue.pop(0)
                        currRow, currCol = currPosition[0], currPosition[1]

                        for direction in directions:
                            nextRow, nextCol = currRow + direction[0], currCol + direction[1]

                            if (nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[0])):
                                continue

                            if grid[nextRow][nextCol] == "1":
                                queue.append([nextRow, nextCol])
                                grid[nextRow][nextCol] = "0"

        return count