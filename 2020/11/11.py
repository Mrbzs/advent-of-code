import os


def get_input_grid():
    input_file = open(os.path.dirname(__file__) + '/input.txt', 'r')
    grid = [[cell for cell in line.rstrip('\n')] for line in input_file]
    input_file.close()
    return grid


def get_occupied_neighbors(grid, row, col):
    neighbors = 0
    for i in range(max(row - 1, 0), min(len(grid), row + 2)):
        for j in range(max(col - 1, 0), min(len(grid[row]), col + 2)):
            neighbors += grid[i][j] == '#' and (i != row or j != col)

    return neighbors


def get_occupied_directional_neighbors(grid, row, col):
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


def part_one():
    grid = get_input_grid()
    changed = True
    while changed:
        changed = False
        occupied = 0

        new_grid = []
        for row in range(len(grid)):
            new_grid.append([])
            for col in range(len(grid[row])):
                neighbors = get_occupied_neighbors(grid, row, col)
                cell = grid[row][col]
                new_cell = '#' if cell == 'L' and neighbors == 0 else 'L' if cell == '#' and neighbors >= 4 else cell
                new_grid[-1].append(new_cell)
                changed |= new_cell != cell
                occupied += new_cell == '#'

        if not changed:
            return occupied

        grid = new_grid


def part_two():
    grid = get_input_grid()
    changed = True
    while changed:
        changed = False
        occupied = 0

        new_grid = []
        for row in range(len(grid)):
            new_grid.append([])
            for col in range(len(grid[row])):
                neighbors = get_occupied_directional_neighbors(grid, row, col)
                cell = grid[row][col]
                new_cell = '#' if cell == 'L' and neighbors == 0 else 'L' if cell == '#' and neighbors >= 5 else cell
                new_grid[-1].append(new_cell)
                changed |= new_cell != cell
                occupied += new_cell == '#'

        if not changed:
            return occupied

        grid = new_grid


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
