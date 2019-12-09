import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = inputFile.readlines()
inputFile.close()

def partOne():
    return sum([int(mass) // 3 - 2 for mass in lines])

def partTwo():
    total = 0
    for line in lines:
        mass = int(line)
        while mass > 8:
            mass = mass // 3 - 2
            total += mass
    return total

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
