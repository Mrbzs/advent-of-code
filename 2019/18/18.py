import collections
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

grid = [line.rstrip() for line in lines]


def get_reachable_keys(grid, start, keys):
    bfs = collections.deque([(start, 1)])
    visited = {}
    reachable_keys = {}
    while bfs:
        pos, steps = bfs.popleft()
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y, x = pos[0] + direction[0], pos[1] + direction[1]

            next_cell = grid[y][x]
            if next_cell == '#' or (y, x) in visited:
                continue

            visited[(y, x)] = 1
            if next_cell.isupper() and next_cell.lower() not in keys:
                continue

            if next_cell.islower() and next_cell not in keys:
                reachable_keys[next_cell] = (steps, (y, x))
                continue

            bfs.append(((y, x), steps + 1))
    return reachable_keys


seen = {}


def get_shortest(grid, starts, keys):
    sorted_keys = ''.join(sorted(keys))
    if (starts, sorted_keys) in seen:
        return seen[(starts, sorted_keys)]

    reachable_keys = {}
    for i, start in enumerate(starts):
        for key, (steps, pos) in get_reachable_keys(grid, start, keys).items():
            reachable_keys[key] = (steps, pos, i)

    if len(reachable_keys) == 0:
        return 0
    else:
        paths = []
        for key, (steps, pos, i) in reachable_keys.items():
            new_starts = tuple(pos if j == i else start for j, start in enumerate(starts))
            paths.append(steps + get_shortest(grid, new_starts, keys + key))
        res = min(paths)

    seen[starts, sorted_keys] = res
    return res


def part_one():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return get_shortest(grid, tuple([(i, j)]), '')


def part_two():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                grid[i - 1] = grid[i - 1][:j - 1] + '@#@' + grid[i - 1][j + 2:]
                grid[i] = grid[i][:j - 1] + '###' + grid[i][j + 2:]
                grid[i + 1] = grid[i + 1][:j - 1] + '@#@' + grid[i + 1][j + 2:]

                starts = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
                return get_shortest(grid, tuple(starts), '')


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
