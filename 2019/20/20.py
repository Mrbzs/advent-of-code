import collections
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
grid = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def is_outer(pos):
    y, x = pos
    return y == 2 or x == 2 or y == len(grid) - 3 or x == len(grid[0]) - 3


def get_path(grid, start, end, jumps, part_two=False):
    bfs = collections.deque([(start, 0, 0)])
    visited = {}
    while bfs:
        pos, steps, level = bfs.popleft()
        if pos in jumps and jumps[pos] not in visited:
            if part_two:
                new_level = level - 1 if is_outer(pos) else level + 1
            else:
                new_level = 0

            if new_level >= 0:
                bfs.append((jumps[pos], steps + 1, new_level))
                visited[(jumps[pos][0], jumps[pos][1], new_level)] = 1
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y, x = pos[0] + direction[0], pos[1] + direction[1]
            if (y, x) == end and level == 0:
                return steps + 1

            next_cell = grid[y][x]
            if next_cell != '.' or (y, x, level) in visited:
                continue

            visited[(y, x, level)] = 1
            bfs.append(((y, x), steps + 1, level))


def solve():
    portals = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                direction = None
                if grid[i - 1][j].isupper():
                    direction = (-1, 0)
                elif grid[i + 1][j].isupper():
                    direction = (1, 0)
                elif grid[i][j - 1].isupper():
                    direction = (0, -1)
                elif grid[i][j + 1].isupper():
                    direction = (0, 1)

                if direction is not None:
                    portal = ''
                    for k in range(1, 3):
                        if direction[0] < 0 or direction[1] < 0:
                            portal = grid[i + direction[0] * k][j + direction[1] * k] + portal
                        else:
                            portal += grid[i + direction[0] * k][j + direction[1] * k]

                    if portal in portals:
                        portals[portal].append((i, j))
                    else:
                        portals[portal] = [(i, j)]

    jumps = {}
    start = end = None
    for portal in portals:
        if portal == 'AA':
            start = portals[portal][0]
        elif portal == 'ZZ':
            end = portals[portal][0]
        else:
            jumps[portals[portal][0]] = portals[portal][1]
            jumps[portals[portal][1]] = portals[portal][0]

    print(f'Part one: {get_path(grid, start, end, jumps)}')
    print(f'Part two: {get_path(grid, start, end, jumps, True)}')


solve()
