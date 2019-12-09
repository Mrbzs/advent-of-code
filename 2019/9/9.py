import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read()
inputFile.close()

def run(input1):
    program = dict(enumerate(int(i) for i in line.split(',')))
    output = i = base = 0
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
            program[key1] = input1
            i += 2
        elif instruction[-1] == '4':
            output = program[key1]
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

print(f'Part one: {run(1)}')
print(f'Part two: {run(2)}')
