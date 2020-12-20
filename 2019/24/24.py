import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def count_neighbors(grid, i):
    return (i // 5 > 0 and grid[i - 5] == '#') + (i // 5 < 4 and grid[i + 5] == '#') + (i % 5 > 0 and grid[i - 1] == '#') + (
                i % 5 < 4 and grid[i + 1] == '#')


def count_neighbors_2(levels, level, i, j):
    neighbors = 0
    if level - 1 in levels:
        neighbors += i == 0 and levels[level - 1][1][2] == '#'
        neighbors += j == 0 and levels[level - 1][2][1] == '#'
        neighbors += i == 4 and levels[level - 1][3][2] == '#'
        neighbors += j == 4 and levels[level - 1][2][3] == '#'
    if level + 1 in levels:
        y, x, dy, dx = 0, 0, 0, 0
        if i == 1 and j == 2:
            y, x, dy, dx = 0, 0, 0, 1
        elif i == 2 and j == 1:
            y, x, dy, dx = 0, 0, 1, 0
        elif i == 3 and j == 2:
            y, x, dy, dx = 4, 0, 0, 1
        elif i == 2 and j == 3:
            y, x, dy, dx = 0, 4, 1, 0

        if dy or dx:
            while y < 5 and x < 5:
                neighbors += levels[level + 1][y][x] == '#'
                y += dy
                x += dx

    neighbors += i > 0 and levels[level][i - 1][j] == '#'
    neighbors += j > 0 and levels[level][i][j - 1] == '#'
    neighbors += i < 4 and levels[level][i + 1][j] == '#'
    neighbors += j < 4 and levels[level][i][j + 1] == '#'
    return neighbors


def part_one():
    seen = {}
    state = ''.join(lines)
    while state not in seen:
        seen[state] = 1
        next_state = ''
        for i in range(len(state)):
            neighbors = count_neighbors(state, i)
            if state[i] == '#' and neighbors != 1:
                next_state += '.'
            elif state[i] == '.' and (neighbors == 1 or neighbors == 2):
                next_state += '#'
            else:
                next_state += state[i]
        state = next_state

    biodiversity = 1
    res = 0
    for cell in state:
        if cell == '#':
            res += biodiversity
        biodiversity *= 2
    return res


def part_two():
    levels = {0: [list(line) for line in lines]}
    levels[0][2][2] = '?'
    min_level = max_level = count = 0
    minutes = 200
    while minutes > 0:
        new_levels = {}
        for level in levels:
            new_levels[level] = [cell[:] for cell in levels[level]]
        for level in range(min_level - 1, max_level + 2):
            if level not in levels:
                levels[level] = [list('..?..') if i == 2 else list('.....') for i in range(5)]
                new_levels[level] = [list('..?..') if i == 2 else list('.....') for i in range(5)]
            for i in range(5):
                for j in range(5):
                    neighbors = count_neighbors_2(levels, level, i, j)
                    if levels[level][i][j] == '#' and neighbors != 1:
                        new_levels[level][i][j] = '.'
                    elif levels[level][i][j] == '.' and (neighbors == 1 or neighbors == 2):
                        new_levels[level][i][j] = '#'
                        min_level = min(min_level, level)
                        max_level = max(max_level, level)
                    else:
                        new_levels[level][i][j] = levels[level][i][j]

                    if minutes == 1:
                        count += new_levels[level][i][j] == '#'
        levels = new_levels
        minutes -= 1
    return count


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
