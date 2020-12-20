import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
image = inputFile.read().rstrip()
inputFile.close()


def part_one():
    i = zeros = ones = twos = res = 0
    fewest = layer_size = 25 * 6
    for pixel in image:
        i += 1
        zeros += pixel == '0'
        ones += pixel == '1'
        twos += pixel == '2'
        if i % layer_size == 0:
            if zeros < fewest:
                fewest = zeros
                res = ones * twos
            zeros = ones = twos = 0
    return res


def part_two():
    layer_size = 25 * 6
    output = ''
    for i in range(layer_size):
        j = i
        while image[j] == '2':
            j += layer_size
        output += image[j] if len(output) % 26 else f'\n{image[j]}'
    return output


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
