import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()


def run(inputs):
    program = dict(enumerate(int(i) for i in line.split(',')))
    if len(inputs):
        program[0] = 2

    i = base = inputs_index = 0
    output = []
    while 1:
        instruction = str(program[i]).zfill(5)
        if instruction[-2:] == '99':
            return output

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
            program[key1] = inputs[inputs_index]
            inputs_index += 1
            i += 2
        elif instruction[-1] == '4':
            output.append(program[key1])
            i += 2
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
    output = run([])
    grid = ['']
    for cell in output[:-2]:
        if cell == 10:
            grid.append('')
        else:
            grid[-1] += chr(cell)

    part_one = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == '#' and grid[i + 1][j] == '#' and grid[i - 1][j] == '#' and grid[i][j + 1] == '#' and grid[i][j - 1] == '#':
                part_one += i * j
    print(f'Part one: {part_one}')

    # Part 2
    # What I did is print the path and then manually figure out the values of A, B and C. It was easy since the path is short

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pos = direction = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.' and grid[i][j] != '#':
                direction = '^>v<'.index(grid[i][j])
                pos = (i, j)

    path = ''
    move = count = 0
    while count != 4:
        dy, dx = directions[direction][0], directions[direction][1]
        y, x = pos[0] + dy, pos[1] + dx
        count = 0
        while (y >= len(grid) or y < 0 or x >= len(grid[0]) or x < 0 or grid[y][x] != '#' or count == 2) and count != 4:
            direction = (direction + 1) % 4
            dy, dx = directions[direction][0], directions[direction][1]
            y, x = pos[0] + dy, pos[1] + dx
            count += 1

        if count == 0:
            move += 1
            pos = (pos[0] + dy, pos[1] + dx)
        elif count != 4:
            if move > 0:
                path += f',{str(move)}'
            path += ',L' if count == 3 else ',R'
            move = 0

    path = path[1:] + f',{str(move)}'

    a = 'R,10,L,8,R,10,R,4'
    b = 'L,6,R,12,R,12,R,10'
    c = 'L,6,L,6,R,10'
    path = path.replace(a, 'A').replace(b, 'B').replace(c, 'C')

    inputs = []
    for char in f'{path}\n{a}\n{b}\n{c}\nn\n':
        inputs.append(ord(char))

    print(f'Part two: {run(inputs)[-1]}')


solve()
