import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def solve():
    points = {}
    partOne = partTwo = 0
    for wire in range(2):
        steps = 0
        pos = [0, 0]
        for move in lines[wire].split(','):
            d = move[0]
            d = [-1, 0] if d == 'U' else [1, 0] if d == 'D' else [0, -1] if d == 'L' else [0, 1]
            for i in range(int(move[1:])):
                pos[0] += d[0]
                pos[1] += d[1]
                steps += 1
                if wire == 1:
                    if (pos[0], pos[1]) in points:
                        distance = abs(pos[0]) + abs(pos[1])
                        totalSteps = points[(pos[0], pos[1])] + steps
                        if partOne == 0 or distance < partOne:
                            partOne = distance
                        if partTwo == 0 or totalSteps < partTwo:
                            partTwo = totalSteps
                else:
                    points[(pos[0], pos[1])] = steps

    print(f'Part one: {partOne}')
    print(f'Part two: {partTwo}')

solve()
