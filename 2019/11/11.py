import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()

def partOne(startColor):
    program = dict(enumerate(int(i) for i in line.split(',')))
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0
    robot = (0, 0)
    ship = {robot: startColor}
    res = i = base = outputType = 0
    while 1:
        instruction = str(program[i]).zfill(5)
        if instruction[-2:] == '99':
            return ship

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
            program[key1] = 0 if robot not in ship else ship[robot]
            i += 2
        elif instruction[-1] == '4':
            if outputType == 0:
                ship[robot] = program[key1]
            else:
                if program[key1] == 0:
                    direction = 3 if direction == 0 else direction - 1
                else:
                    direction = (direction + 1) % 4
                robot = (robot[0] + directions[direction][0], robot[1] + directions[direction][1])
            i += 2
            outputType ^= 1
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

def partTwo():
    ship = partOne(1)
    height = width = 0
    
    # I checked that all values are positive before doing this
    for i, j in ship:
        height = max(height, i + 1)
        width = max(width, j + 1)

    res = ''
    for i in range(height):
        res += '\n'
        for j in range(width):
            res += '.' if (i, j) not in ship or ship[(i, j)] == 0 else '#'
    return res

print(f'Part one: {len(partOne(0))}')
print(f'Part two: {partTwo()}')
