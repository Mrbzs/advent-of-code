import os
import re

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def partOne():
    memory = {}
    mask = None
    for line in lines:
        if line[:4] == 'mask':
            mask = line[7:]
        else:
            address, value = map(int, re.findall('\d+', line))
            for i in range(len(mask)):
                bit = len(mask) - i - 1
                if mask[i] == '0':
                    value &= ~(1 << bit)
                elif mask[i] == '1':
                    value |= 1 << bit

            memory[address] = value

    return sum(memory.values())

def partTwo():
    memory = {}
    mask = None
    for line in lines:
        if line[:4] == 'mask':
            mask = line[7:]
        else:
            startAddress, value = map(int, re.findall('\d+', line))

            # Bruteforcing since highest number of X in a mask is 9
            worklist = [(startAddress, 0)]
            while len(worklist):
                address, i = worklist.pop()
                setMemory = True
                while i < len(mask):
                    bit = len(mask) - i - 1
                    if mask[i] == '1':
                        address |= 1 << bit
                    elif mask[i] == 'X':
                        worklist.append((address | 1 << bit, i + 1))
                        worklist.append((address & ~(1 << bit), i + 1))
                        setMemory = False
                        break
                    i += 1
                
                if setMemory:
                    memory[address] = value
    
    return sum(memory.values())

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
