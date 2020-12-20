import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()


def part_one():
    program = [int(i) for i in line.split(',')]
    output = i = 0
    while i < len(program):
        instruction = str(program[i]).zfill(5)
        if instruction[-1] == '9':
            return output
        elif instruction[-1] == '3':
            program[program[i + 1]] = 1
            i += 2
        elif instruction[-1] == '4':
            output = program[program[i + 1]]
            i += 2
        else:
            p1 = program[i + 1] if instruction[2] == '1' else program[program[i + 1]]
            p2 = program[i + 2] if instruction[1] == '1' else program[program[i + 2]]
            program[program[i + 3]] = p1 + p2 if instruction[-1] == '1' else p1 * p2
            i += 4


def part_two():
    program = [int(i) for i in line.split(',')]
    output = i = 0
    while i < len(program):
        instruction = str(program[i]).zfill(5)
        if instruction[-1] == '9':
            return output
        elif instruction[-1] == '3':
            program[program[i + 1]] = 5
            i += 2
        elif instruction[-1] == '4':
            output = program[program[i + 1]]
            i += 2
        else:
            p1 = program[i + 1] if instruction[2] == '1' else program[program[i + 1]]
            p2 = program[i + 2] if instruction[1] == '1' else program[program[i + 2]]
            if instruction[-1] == '1':
                program[program[i + 3]] = p1 + p2
                i += 4
            elif instruction[-1] == '2':
                program[program[i + 3]] = p1 * p2
                i += 4
            elif instruction[-1] == '5':
                i = p2 if p1 else i + 3
            elif instruction[-1] == '6':
                i = i + 3 if p1 else p2
            elif instruction[-1] == '7':
                program[program[i + 3]] = 1 if p1 < p2 else 0
                i += 4
            elif instruction[-1] == '8':
                program[program[i + 3]] = 1 if p1 == p2 else 0
                i += 4


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
