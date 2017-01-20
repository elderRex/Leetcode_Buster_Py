def maxKilledEnemies(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0
    row_len = len(grid)
    col_len = len(grid[0])
    col_kill = [0] * col_len
    row, max = 0, 0
    for i in range(0, row_len):
        for j in range(0, col_len):
            # print 'i',i
            if grid[i][j] == 'W':
                continue
            if grid[i][j - 1] == 'W' or j == 0:
                row = self.get_kill_row(i, j, col_len, grid)
                # print row,i
            if grid[i - 1][j] == 'W' or i == 0:
                col_kill[j] = self.get_kill_col(i, j, row_len, grid)
                # print col_kill
            if grid[i][j] == '0':
                # print 'in',row,col_kill
                # print 'ij',i,j
                # print 'max',max, row
                max = row + col_kill[j] if row + col_kill[j] > max else max

    return max


def get_kill_row(self, row, col, col_len, grid):
    kill = 0
    for j in range(col, col_len):
        if grid[row][j] == 'W':
            break
        if grid[row][j] == 'E':
            kill += 1
    return kill


def get_kill_col(self, row, col, row_len, grid):
    kill = 0
    for i in range(row, row_len):
        # print grid[i][col]
        if grid[i][col] == 'W':
            break
        if grid[i][col] == 'E':
            kill += 1
    return kill