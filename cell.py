def numberOfLiveNeighbors(grid, x, y):
    result = 0
    minRow = 0 if (x == 0) else x-1
    maxRow = x if (x == len(grid)) else x+1 if (x+2 > len(grid)) else x+2
    minCol = 0 if y == 0 else y-1
    maxCol = y if y == len(grid[0]) else y+1 if (y+2 > len(grid)) else y+2

    for i in range(minRow, maxRow, 1):
        for j in range(minCol, maxCol, 1):
            if (not(i == x and j == y) and grid[i][j]):
                result += 1
    
    return result
    
def isCellAlive(grid, x, y):
    i = numberOfLiveNeighbors(grid, x, y)
    if (grid[x][y]):
        if (i < 2):
            return False
        elif (i > 3):
            return False
        else:
            return True
    elif (i == 3):
        return True
    else:
        return False


def getNextGrid(grid):
    rows = len(grid)    
    cols = len(grid[0]) 
    list = [[False]*cols for i in range(0, rows)]

    for i in range(0, rows):
        for j in range(0, cols):
            list[i][j] = isCellAlive(grid, i, j)
    
    return list
