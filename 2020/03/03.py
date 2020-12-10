import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def partOne():
    trees = 0
    pos = (0, 0)
    
    while pos[0] < len(lines):
        trees += lines[pos[0]][pos[1]] == '#'
        pos = (pos[0] + 1, (pos[1] + 3) % len(lines[0]))

    return trees

def partTwo():
    res = 1
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    for slope in slopes:
        trees = 0
        pos = (0, 0)
        
        while pos[0] < len(lines):
            trees += lines[pos[0]][pos[1]] == '#'
            pos = (pos[0] + slope[0], (pos[1] + slope[1]) % len(lines[0]))

        res *= trees

    return res

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
