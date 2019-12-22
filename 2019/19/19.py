import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()

def run(input1, input2):
    program = dict(enumerate(int(i) for i in line.split(',')))
    output = i = base = inputNum = 0
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
            if inputNum == 0:
                program[key1] = input1
                inputNum = 1
            else:
                program[key1] = input2
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

def partOne():
    res = prevStart = 0
    for i in range(50):
        first = True
        for j in range(prevStart, 50):
            if run(j, i) == 1:
                if first:
                    prevStart = j
                first = False
                res += 1
    
    return res

def partTwo():
    i = 10
    prevStart = 0
    while 1:
        j = prevStart
        while run(j, i) == 0:
            j += 1
        prevStart = j
        
        if run(j + 99, i - 99) == 1:
            return j * 10000 + i - 99
        i += 1

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
