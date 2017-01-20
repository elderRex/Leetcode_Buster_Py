def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    connected = [[-1] * len(grid[0])] * len(grid)
    island = 0
    for i in range(0, len(grid)):
        print len(grid[0])
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1 and connected[i][j] == -1:
                expand(grid, i, j)
                island += 1
    return island


direction = [0, 1, 0, -1, 0]


def expand(grid, i, j):
    global direction
    if i >= 0 and i <= len(grid) and j >= 0 and j <= len(grid[0]):
        grid[i][j] = 1

    for i in range(4):
        expand(grid, i + direction[i], j + direction[i + 1])