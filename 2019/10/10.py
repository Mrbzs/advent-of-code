from math import inf
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def solve():
    def get_score(row, col):
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

    part_one = best_row = best_col = 0
    best_gradients = {}
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == '#':
                gradients = get_score(row, col)
                if len(gradients) > part_one:
                    part_one = len(gradients)  # Number of unique gradients
                    best_row = row
                    best_col = col
                    best_gradients = gradients

    # Sort values for each gradient by manhattan distance
    for key in best_gradients:
        best_gradients[key].sort(key=lambda x: abs(best_row - x[0]) + abs(best_col - x[1]))

    # Separate gradients into 4 quadrants going clockwise starting from top right
    quadrants = [[], [], [], []]
    for quadrant, gradient in best_gradients:
        quadrants[quadrant].append(gradient)

    # Sort gradients in each quadrant
    for quadrant in range(4):
        quadrants[quadrant].sort(reverse=True)

    count = 0
    while 1:
        for quadrant in range(4):
            for gradient in quadrants[quadrant]:
                points = best_gradients[(quadrant, gradient)]
                if len(points):
                    part_two = points[0]
                    count += 1

                    if count == 200:
                        print(f'Part one: {part_one}')
                        print(f'Part two: {part_two[1] * 100 + part_two[0]}')
                        return


solve()
