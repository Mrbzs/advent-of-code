from natsort import natsorted
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = inputFile.readlines()
inputFile.close()

def solve():
    def getScore(row, col):
        gradients = {}
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if (row != i or col != j) and lines[i][j] == '#':
                    # - at the end separates same gradient in opposite direction
                    if row == i:
                        gradient = '0' if col > j else '0-'
                    elif col == j:
                        gradient = 'inf' if row > i else 'inf-'
                    else:
                        # 0 padding is for consistent sorting
                        gradient = str((i - row) / (col - j)).ljust(20, '0') if j > col else str((i - row) / (col - j)).ljust(20, '0') + '-'

                    if gradient in gradients:
                        gradients[gradient].append((i, j))
                    else:
                        gradients[gradient] = [(i, j)]
        return gradients

    res = bestRow = bestCol = 0
    bestGradients = {}
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == '#':
                gradients = getScore(row, col)
                if len(gradients) > res:
                    res = len(gradients) # Number of unique gradients
                    bestRow = row
                    bestCol = col
                    bestGradients = gradients
    
    # Sort values for each gradient by manhattan distance
    for gradient in bestGradients:
        bestGradients[gradient].sort(key=lambda x: abs(bestRow - x[0]) + abs(bestCol - x[1]))

    # Separate gradients into 4 quadrants going clockwise starting from top right
    g1 = []
    g2 = []
    g3 = []
    g4 = []
    for gradient in bestGradients:
        if gradient[0] == '-':
            if gradient[-1] == '-':
                g4.append(gradient)
            else:
                g2.append(gradient)
        else:
            if gradient[-1] == '-':
                g3.append(gradient)
            else:
                g1.append(gradient)

    # Numerical sorting
    # inf -> 0 -> inf- -> 0- -> inf
    gradients = natsorted(g1, reverse=True) + natsorted(g2) + natsorted(g3, reverse=True) + natsorted(g4)

    partTwo = count = i = 0
    while 1:
        if count == 200:
            break
        if len(bestGradients[gradients[i]]):
            partTwo = bestGradients[gradients[i]][0]
            bestGradients[gradients[i]] = bestGradients[gradients[i]][1:]
            count += 1
        i = (i + 1) % len(gradients)

    print(f'Part one: {res}')
    print(f'Part two: {partTwo[1] * 100 + partTwo[0]}')

solve()
