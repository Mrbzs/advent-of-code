import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def part_one():
    highest = 0
    for seat in lines:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
        highest = max(highest, row * 8 + col)
    return highest


def one_to_n_sum(n):
    return n * (n + 1) // 2


def part_two():
    highest = total = lowest = 0
    for seat in lines:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
        highest = max(highest, row * 8 + col)
        lowest = min(lowest, row * 8 + col) if lowest else row * 8 + col
        total += row * 8 + col

    # Total seat sum = sum(1 -> highest) - sum(1 -> lowest - 1)
    # Missing seat = total seat sum - current seat sum
    return one_to_n_sum(highest) - one_to_n_sum(lowest - 1) - total


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
