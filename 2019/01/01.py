import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def part_one():
    return sum([int(mass) // 3 - 2 for mass in lines])


def part_two():
    total = 0
    for line in lines:
        mass = int(line)
        while mass > 8:
            mass = mass // 3 - 2
            total += mass
    return total


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
