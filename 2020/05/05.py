import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def partOne():
    highest = total = lowest = 0
    for seat in lines:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
        highest = max(highest, row * 8 + col)
    return highest
    
def partTwo():
    highest = total = lowest = 0
    for seat in lines:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
        highest = max(highest, row * 8 + col)
        lowest = min(lowest, row * 8 + col) if lowest else row * 8 + col
        total += row * 8 + col

    # Total seat sum = sum(1 -> highest) - sum(1 -> lowest - 1)
    # Missing seat = total seat sum - current seat sum
    oneToNSum = lambda n: n * (n + 1) // 2
    return oneToNSum(highest) - oneToNSum(lowest - 1) - total

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
