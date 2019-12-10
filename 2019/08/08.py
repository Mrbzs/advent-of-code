import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
image = inputFile.read()
inputFile.close()

def partOne():
    i = zeros = ones = twos = res = 0
    fewest = layerSize = 25 * 6
    for pixel in image:
        i += 1
        zeros += pixel == '0'
        ones += pixel == '1'
        twos += pixel == '2'
        if i % layerSize == 0:
            if zeros < fewest:
                fewest = zeros
                res = ones * twos
            zeros = ones = twos = 0
    return res

def partTwo():
    layerSize = 25 * 6
    output = ''
    for i in range(layerSize):
        j = i
        while image[j] == '2':
            j += layerSize
        output += image[j] if len(output) % 26 else f'\n{image[j]}'
    return output
        
print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
