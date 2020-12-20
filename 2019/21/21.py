import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()


def run(inputs):
    program = dict(enumerate(int(i) for i in line.split(',')))
    output = i = input_index = base = 0
    temp = ''
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
            program[key1] = inputs[input_index]
            input_index += 1
            i += 2
        elif instruction[-1] == '4':
            if program[key1] == 10:
                print(temp)
                temp = ''
            elif program[key1] > 126:
                output = program[key1]
            else:
                temp += chr(program[key1])
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


def get_ascii(instructions):
    inputs = []
    for instruction in instructions:
        for char in instruction:
            inputs.append(ord(char))
        inputs.append(10)
    return inputs


def part_one():
    instructions = ['NOT A T', 'OR T J', 'NOT B T', 'OR T J', 'NOT C T', 'OR T J', 'AND D J', 'WALK']
    return run(get_ascii(instructions))


def part_two():
    instructions = ['NOT A J', 'NOT C T', 'AND H T', 'OR T J', 'NOT B T', 'AND A T', 'AND C T', 'OR T J', 'AND D J', 'RUN']
    return run(get_ascii(instructions))


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
