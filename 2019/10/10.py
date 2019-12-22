from math import inf
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def solve():
    def getScore(row, col):
        gradients = {}
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if (row != i or col != j) and lines[i][j] == '#':
                    if row == i:
                        gradient = 0
                        quadrant = 3 if col > j else 1
                    elif col == j:
                        gradient = inf
                        quadrant = 0 if row > i else 2
                    else:
                        gradient = (i - row) / (col - j)
                        if gradient > 0:
                            quadrant = 2 if col > j else 0
                        else:
                            quadrant = 3 if col > j else 1

                    if gradient in gradients:
                        gradients[(quadrant, gradient)].append((i, j))
                    else:
                        gradients[(quadrant, gradient)] = [(i, j)]
        return gradients

    partOne = bestRow = bestCol = 0
    bestGradients = {}
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == '#':
                gradients = getScore(row, col)
                if len(gradients) > partOne:
                    partOne = len(gradients) # Number of unique gradients
                    bestRow = row
                    bestCol = col
                    bestGradients = gradients
    
    # Sort values for each gradient by manhattan distance
    for key in bestGradients:
        bestGradients[key].sort(key=lambda x: abs(bestRow - x[0]) + abs(bestCol - x[1]))

    # Separate gradients into 4 quadrants going clockwise starting from top right
    quadrants = [[], [], [], []]
    for quadrant, gradient in bestGradients:
        quadrants[quadrant].append(gradient)

    # Sort gradients in each quadrant
    for quadrant in range(4):
        quadrants[quadrant].sort(reverse=True)

    partTwo = count = 0
    while 1:
        for quadrant in range(4):
            for gradient in quadrants[quadrant]:
                points = bestGradients[(quadrant, gradient)]
                if len(points):
                    partTwo = points[0]
                    points = points[1:]
                    count += 1

                    if count == 200:
                        print(f'Part one: {partOne}')
                        print(f'Part two: {partTwo[1] * 100 + partTwo[0]}')
                        return 

solve()
