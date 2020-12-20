import os
import re

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def part_one():
    buses = list(map(int, re.findall(r'\d+', lines[1])))
    timestamp = int(lines[0])
    earliest = res = -1

    for bus in buses:
        bus_earliest = timestamp + bus - timestamp % bus
        if earliest == -1 or bus_earliest < earliest:
            earliest = bus_earliest
            res = (earliest - timestamp) * bus

    return res


def part_two():
    buses = lines[1].split(',')
    arr = []
    for i, bus in enumerate(buses):
        if buses[i] != 'x':
            arr.append((i, int(buses[i])))

    product = t = 1
    for i, bus in arr:
        # Add the product of previous numbers to t until we find a number that divides the current bus.
        # This ensures that t stays divisible by the previous numbers. Adding the product of the previous 
        # numbers only works because they are prime
        while (t + i) % bus:
            t += product
        product *= bus

    return t


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
