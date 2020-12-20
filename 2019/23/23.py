import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()


def solve():
    inputs = [[i] for i in range(50)]
    programs = [dict(enumerate(int(i) for i in line.split(','))) for j in range(50)]
    bases = [0] * 50
    progresses = [0] * 50
    outputs = [[] for i in range(50)]
    nat = prev = part_one = None
    idle = [False] * 50
    while 1:
        for computer in range(50):
            i = progresses[computer]
            base = bases[computer]
            program = programs[computer]
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
                if len(inputs[computer]):
                    program[key1] = inputs[computer][0]
                    inputs[computer] = inputs[computer][1:]
                else:
                    program[key1] = -1
                    idle[computer] = True
                i += 2
            elif instruction[-1] == '4':
                idle[computer] = False
                outputs[computer].append(program[key1])
                if len(outputs[computer]) == 3:
                    if outputs[computer][0] == 255:
                        if not part_one:
                            print(f'Part one: {outputs[computer][2]}')
                            part_one = 1
                        nat = (outputs[computer][1], outputs[computer][2])
                    else:
                        inputs[outputs[computer][0]].extend(outputs[computer][1:])
                    outputs[computer] = []
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
                bases[computer] += program[key1]
                i += 2
            progresses[computer] = i

        if nat and False not in idle:
            if nat == prev:
                print(f'Part two: {nat[1]}')
                return
            inputs[0].extend([nat[0], nat[1]])
            prev = nat
            nat = None


solve()
