import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()


def part_one():
    phases = 100
    input_signal = [int(i) for i in line]
    output_signal = []
    while phases > 0:
        output_signal = []
        for i in range(len(input_signal)):
            output = negative = 0
            for j in range(i, len(input_signal), 2 * (i + 1)):
                for k in range(j, min(j + i + 1, len(input_signal))):
                    output += -input_signal[k] if negative else input_signal[k]
                negative ^= 1
            output_signal.append(abs(output) % 10)
        input_signal = output_signal
        phases -= 1
    return ''.join(str(i) for i in output_signal[:8])


# After the given offset, all digits of pattern are 1 so each digit is the sum of itself + the elements to its right
# Digits are looped starting from the right to avoid computing sum for each digit
def part_two():
    input_signal = ([int(i) for i in line] * 10000)[int(line[:7]):]
    for i in range(100):
        total = 0
        for j in range(len(input_signal) - 1, -1, -1):
            total += input_signal[j]
            input_signal[j] = total % 10
    return ''.join(str(i) for i in input_signal[:8])


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
