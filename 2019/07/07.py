import itertools
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read()
inputFile.close()

def partOne():
    def getOutput(input1, input2):
        program = [int(i) for i in line.split(',')]
        output = i = inputNum = 0
        while i < len(program):
            instruction = str(program[i]).zfill(5)
            if instruction[-1] == '9':
                return output
            elif instruction[-1] == '3':
                program[program[i + 1]] = input1 if inputNum == 0 else input2
                inputNum += 1
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

    res = 0
    for sequence in list(itertools.permutations([0, 1, 2, 3, 4])):
        output = 0
        for phase in sequence:
            output = getOutput(phase, output)
        res = max(res, output)
    return res

def partTwo():
    res = 0
    for feedbackSequence in list(itertools.permutations([5, 6, 7, 8, 9])):
        inputs = [[phase] for phase in feedbackSequence]
        inputs[0].append(0)
        running = [True] * 5
        progresses = [0] * 5
        program = [int(i) for i in line.split(',')]
        programs = [program[:] for i in range(5)]
        while True in running:
            for i in range(5):
                instruction = str(programs[i][progresses[i]]).zfill(5)
                if instruction[-1] == '9':
                    running[i] = False
                elif instruction[-1] == '3':
                    if len(inputs[i]):
                        programs[i][programs[i][progresses[i] + 1]] = inputs[i][0]
                        inputs[i] = inputs[i][1:]
                        progresses[i] += 2
                elif instruction[-1] == '4':
                    inputs[(i + 1) % 5].append(programs[i][programs[i][progresses[i] + 1]])
                    progresses[i] += 2
                else:
                    p1 = programs[i][progresses[i] + 1] if instruction[2] == '1' else programs[i][programs[i][progresses[i] + 1]]
                    p2 = programs[i][progresses[i] + 2] if instruction[1] == '1' else programs[i][programs[i][progresses[i] + 2]]
                    if instruction[-1] == '1':
                        programs[i][programs[i][progresses[i] + 3]] = p1 + p2
                        progresses[i] += 4
                    elif instruction[-1] == '2':
                        programs[i][programs[i][progresses[i] + 3]] = p1 * p2
                        progresses[i] += 4
                    elif instruction[-1] == '5':
                        progresses[i] = p2 if p1 else progresses[i] + 3
                    elif instruction[-1] == '6':
                        progresses[i] = progresses[i] + 3 if p1 else p2
                    elif instruction[-1] == '7':
                        programs[i][programs[i][progresses[i] + 3]] = 1 if p1 < p2 else 0
                        progresses[i] += 4
                    elif instruction[-1] == '8':
                        programs[i][programs[i][progresses[i] + 3]] = 1 if p1 == p2 else 0
                        progresses[i] += 4
        res = max(res, inputs[0][-1])
    return res

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
