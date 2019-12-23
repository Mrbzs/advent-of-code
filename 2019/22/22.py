import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
shuffles = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def partOne():
    cards = [i for i in range(10007)]
    for shuffle in shuffles:
        if shuffle[0] == 'd':
            if shuffle[5] == 'w':
                inc = int(shuffle[20:])
                newCards = cards[:]
                count = 0
                for i in range(10007):
                    cards[count] = newCards[i]
                    count = (count + inc) % 10007
            else:
                cards = cards[::-1]
        else:
            value = int(shuffle[4:])
            cards = cards[value:] + cards[:value]
    return cards.index(2019)

def partTwo():
    # Implemented after reading forum post since I realized I didn't have the mathematical background required
    # https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/
    size = 119315717514047
    iterations = 101741582076661
    increment_mul = 1
    offset_diff = 0

    for shuffle in shuffles:
        if shuffle[0] == 'd':
            if shuffle[5] == 'w':
                increment_mul = increment_mul * pow(int(shuffle[20:]), size - 2, size) % size
            else:
                increment_mul *= -1
                offset_diff = (offset_diff + increment_mul) % size
        else:
            offset_diff = (offset_diff + int(shuffle[4:]) * increment_mul) % size

        increment = pow(increment_mul, iterations, size)
        offset = offset_diff * (1 - increment) * pow((1 - increment_mul) % size, size - 2, size) % size

    return (offset + 2020 * increment) % size

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
