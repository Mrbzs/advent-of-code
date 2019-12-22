import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
program = [int(num) for num in inputFile.read().rstrip().split(',')]
inputFile.close()

def partOne(a, b):
    arr = program[:]
    arr[1:3] = [a, b]

    for i in range(0, len(arr), 4):
        if arr[i] == 1:
            arr[arr[i + 3]] = arr[arr[i + 1]] + arr[arr[i + 2]]
        elif arr[i] == 2:
            arr[arr[i + 3]] = arr[arr[i + 1]] * arr[arr[i + 2]]
        else:
            return arr[0]

def partTwo():
    for noun in range(100):
        for verb in range(100):
            if partOne(noun, verb) == 19690720:
                return 100 * noun + verb

print(f'Part one: {partOne(12, 2)}')
print(f'Part two: {partTwo()}')
