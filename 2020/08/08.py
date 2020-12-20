import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def part_one():
    seen = set()
    i = accumulator = 0
    while i not in seen:
        seen.add(i)
        instruction, operand = lines[i].split(' ')
        if instruction == 'jmp':
            i += int(operand)
        else:
            i += 1
            if instruction == 'acc':
                accumulator += int(operand)

    return accumulator


def part_two():
    for changed in range(len(lines)):
        if lines[changed] == 'acc':
            continue

        seen = set()
        i = accumulator = 0
        while i not in seen:
            seen.add(i)
            instruction, operand = lines[i].split(' ')
            if i == changed:
                instruction = 'jmp' if instruction == 'nop' else 'nop'
            if instruction == 'jmp':
                i += int(operand)
            else:
                i += 1
                if instruction == 'acc':
                    accumulator += int(operand)

            if i >= len(lines):
                return accumulator


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
