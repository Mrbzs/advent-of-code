import collections
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

grid = [line.rstrip() for line in lines]

def getReachableKeys(grid, start, keys):
    bfs = collections.deque([(start, 1)])
    visited = {}
    reachableKeys = {}
    while bfs:
        pos, steps = bfs.popleft()
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y, x = pos[0] + direction[0], pos[1] + direction[1]

            nextCell = grid[y][x]
            if nextCell == '#' or (y, x) in visited:
                continue

            visited[(y, x)] = 1
            if nextCell.isupper() and nextCell.lower() not in keys:
                continue

            if nextCell.islower() and nextCell not in keys:
                reachableKeys[nextCell] = (steps, (y, x))
                continue

            bfs.append(((y, x), steps + 1))
    return reachableKeys

seen = {}
def getShortest(grid, starts, keys):
    sortedKeys = ''.join(sorted(keys))
    if (starts, sortedKeys) in seen:
        return seen[(starts, sortedKeys)]

    reachableKeys = {}
    for i, start in enumerate(starts):
        for key, (steps, pos) in getReachableKeys(grid, start, keys).items():
            reachableKeys[key] = (steps, pos, i)

    if len(reachableKeys) == 0:
        return 0
    else:
        paths = []
        for key, (steps, pos, i) in reachableKeys.items():
            newStarts = tuple(pos if j == i else start for j, start in enumerate(starts))
            paths.append(steps + getShortest(grid, newStarts, keys + key))
        res = min(paths)

    seen[starts, sortedKeys] = res
    return res

def partOne():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return getShortest(grid, tuple([(i, j)]), '')

def partTwo():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                grid[i - 1] = grid[i - 1][:j - 1] + '@#@' + grid[i - 1][j + 2:]
                grid[i] = grid[i][:j - 1] + '###' + grid[i][j + 2:]
                grid[i + 1] = grid[i + 1][:j - 1] + '@#@' + grid[i + 1][j + 2:]

                starts = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
                return getShortest(grid, tuple(starts), '')

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')