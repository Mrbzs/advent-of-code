import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def getLineInfo(line):
    policy, password = line.split(': ')
    count, char = policy.split(' ')
    num1, num2 = map(int, count.split('-'))

    return num1, num2, char, password

def partOne():
    valid = 0
    for line in lines:
        low, high, char, password = getLineInfo(line)
        valid += low <= password.count(char) <= high

    return valid

def partTwo():
    valid = 0
    for line in lines:
        pos1, pos2, char, password = getLineInfo(line)
        valid += (password[pos1 - 1] == char) ^ (password[pos2 - 1] == char)

    return valid

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
