import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read()
inputFile.close()

def partOne():
    phases = 100
    inputSignal = [int(i) for i in line]
    while phases > 0:
        outputSignal = []
        for i in range(len(inputSignal)):
            output = negative = 0
            for j in range(i, len(inputSignal), 2 * (i + 1)):
                for k in range(j, min(j + i + 1, len(inputSignal))):
                    output += -inputSignal[k] if negative else inputSignal[k]
                negative ^= 1
            outputSignal.append(abs(output) % 10)
        inputSignal = outputSignal
        phases -= 1
    return ''.join(str(i) for i in outputSignal[:8])

# After the given offset, all digits of pattern are 1 so each digit is the sum of itself + the elements to its right
# Digits are looped starting from the right to avoid computing sum for each digit
def partTwo():
    inputSignal = ([int(i) for i in line] * 10000)[int(line[:7]):]
    for i in range(100):
        total = 0
        for j in range(len(inputSignal) - 1, -1, -1):
            total += inputSignal[j]
            inputSignal[j] = total % 10
    return ''.join(str(i) for i in inputSignal[:8])

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
