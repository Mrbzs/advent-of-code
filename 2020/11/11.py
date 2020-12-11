import os

def getInputGrid():
    inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
    grid = [[cell for cell in line.rstrip('\n')] for line in inputFile]
    inputFile.close()
    return grid

def getOccupiedNeighbors(grid, row, col):
    neighbors = 0
    for i in range(max(row - 1, 0), min(len(grid), row + 2)):
        for j in range(max(col - 1, 0), min(len(grid[row]), col + 2)):
            neighbors += grid[i][j] == '#' and (i != row or j != col)

    return neighbors

def getOccupiedDirectionalNeighbors(grid, row, col):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    neighbors = 0
    for direction in directions:
        y, x = row + direction[0], col + direction[1]
        while 0 <= y < len(grid) and 0 <= x < len(grid[row]):
            if grid[y][x] != '.':
                neighbors += grid[y][x] == '#'
                break
            y += direction[0]
            x += direction[1]
    
    return neighbors

def partOne():
    grid = getInputGrid()
    changed = True
    while changed:
        changed = False
        occupied = 0

        newGrid = []
        for row in range(len(grid)):
            newGrid.append([])
            for col in range(len(grid[row])):
                neighbors = getOccupiedNeighbors(grid, row, col)
                cell = grid[row][col]
                newCell = '#' if cell == 'L' and neighbors == 0 else 'L' if cell == '#' and neighbors >= 4 else cell
                newGrid[-1].append(newCell)
                changed |= newCell != cell
                occupied += newCell == '#'

        if not changed:
            return occupied
        
        grid = newGrid


def partTwo():
    grid = getInputGrid()
    changed = True
    while changed:
        changed = False
        occupied = 0

        newGrid = []
        for row in range(len(grid)):
            newGrid.append([])
            for col in range(len(grid[row])):
                neighbors = getOccupiedDirectionalNeighbors(grid, row, col)
                cell = grid[row][col]
                newCell = '#' if cell == 'L' and neighbors == 0 else 'L' if cell == '#' and neighbors >= 5 else cell
                newGrid[-1].append(newCell)
                changed |= newCell != cell
                occupied += newCell == '#'

        if not changed:
            return occupied
        
        grid = newGrid
        
print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
