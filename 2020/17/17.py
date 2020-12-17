import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def get3DNeighbors(x, y, z, grid):
    neighbors = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if i != x or j != y or k != z:
                    neighbors += (i, j, k) in grid and grid[(i, j, k)] == '#'

    return neighbors

def get4DNeighbors(x, y, z, w, grid):
    neighbors = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if i != x or j != y or k != z or l != w:
                        neighbors += (i, j, k, l) in grid and grid[(i, j, k, l)] == '#'

    return neighbors

def partOne():
    grid = {}
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            grid[(x, y, 0)] = cell

    active = 0
    cycle = 1
    while cycle <= 6:
        newGrid = dict(grid)
        active = 0
        for x in range(-cycle, len(lines[0]) + cycle):
            for y in range(-cycle, len(lines) + cycle):
                for z in range(-cycle, cycle + 1):
                    if (x, y, z) not in grid:
                        grid[(x, y, z)] = '.'
                    neighbors = get3DNeighbors(x, y, z, grid)

                    if (grid[(x, y, z)] == '#' and 2 <= neighbors <= 3) or (grid[(x, y, z)] == '.' and neighbors == 3):
                        newGrid[(x, y, z)] = '#'
                        active += 1
                    else:
                        newGrid[(x, y, z)] = '.'
        
        grid = newGrid
        cycle += 1

    return active

def partTwo():
    grid = {}
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            grid[(x, y, 0, 0)] = cell

    active = 0
    cycle = 1
    while cycle <= 6:
        newGrid = dict(grid)
        active = 0
        for x in range(-cycle, len(lines[0]) + cycle):
            for y in range(-cycle, len(lines) + cycle):
                for z in range(-cycle, cycle + 1):
                    for w in range(-cycle, cycle + 1):
                        if (x, y, z, w) not in grid:
                            grid[(x, y, z, w)] = '.'
                        neighbors = get4DNeighbors(x, y, z, w, grid)

                        if (grid[(x, y, z, w)] == '#' and 2 <= neighbors <= 3) or (grid[(x, y, z, w)] == '.' and neighbors == 3):
                            newGrid[(x, y, z, w)] = '#'
                            active += 1
                        else:
                            newGrid[(x, y, z, w)] = '.'
        
        grid = newGrid
        cycle += 1

    return active

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
