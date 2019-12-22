import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()

def run(input1, program, i, base):
    while 1:
        instruction = str(program[i]).zfill(5)

        if i + 1 not in program:
            program[i + 1] = 0
        if i + 2 not in program:
            program[i + 2] = 0
        if i + 3 not in program:
            program[i + 3] = 0
        key1 = i + 1 if instruction[2] == '1' else program[i + 1] + base if instruction[2] == '2' else program[i + 1]
        key2 = i + 2 if instruction[1] == '1' else program[i + 2] + base if instruction[1] == '2' else program[i + 2]
        key3 = i + 3 if instruction[0] == '1' else program[i + 3] + base if instruction[0] == '2' else program[i + 3]
        if key1 not in program:
            program[key1] = 0
        if key2 not in program:
            program[key2] = 0
        if key3 not in program:
            program[key3] = 0

        if instruction[-1] == '1':
            program[key3] = program[key1] + program[key2]
            i += 4
        elif instruction[-1] == '2':
            program[key3] = program[key1] * program[key2]
            i += 4
        elif instruction[-1] == '3':
            program[key1] = input1
            i += 2
        elif instruction[-1] == '4':
            return (program[key1], program, i + 2, base)
        elif instruction[-1] == '5':
            i = program[key2] if program[key1] else i + 3
        elif instruction[-1] == '6':
            i = i + 3 if program[key1] else program[key2]
        elif instruction[-1] == '7':
            program[key3] = 1 if program[key1] < program[key2] else 0
            i += 4
        elif instruction[-1] == '8':
            program[key3] = 1 if program[key1] == program[key2] else 0
            i += 4
        elif instruction[-1] == '9':
            base += program[key1]
            i += 2

def solve():
    program = dict(enumerate(int(i) for i in line.split(',')))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    paths = [((0, 0), program, 0, 0)]
    visited = {(0, 0): 1}
    newPaths = []
    grid = {(0, 0): '.'}

    steps = empty = 1
    found = 0
    # BFS
    while len(paths):
        for path in paths:
            for move in range(1, 5):
                direction = directions[move - 1]
                pos = (path[0][0] + direction[0], path[0][1] + direction[1])
                if pos not in visited:
                    visited[pos] = 1
                    output, newProgram, newI, newBase = run(move, dict(path[1]), path[2], path[3])
                    if output == 2:
                        if not found:
                            print(f'Part one: {steps}')
                            grid[pos] = 'O'
                            oxygen = pos
                            found = 1
                    elif output == 1:
                        grid[pos] = '.'
                        empty += 1
                        newPaths.append((pos, newProgram, newI, newBase))
                    else:
                        grid[pos] = '#'

        paths = newPaths[:]
        newPaths = []
        steps += 1

    minutes = 0
    while empty > 0:
        newGrid = dict(grid)
        for i, j in grid:
            if grid[(i, j)] == '.':
                if grid[(i + 1, j)] == 'O' or grid[(i - 1, j)] == 'O' or grid[(i, j + 1)] == 'O' or grid[(i, j - 1)] == 'O':
                    newGrid[(i, j)] = 'O'
                    empty -= 1
        grid = newGrid
        minutes += 1
    
    print(f'Part two: {minutes}')

solve()
