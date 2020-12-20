import os
import re

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def part_one():
    memory = {}
    mask = None
    for line in lines:
        if line[:4] == 'mask':
            mask = line[7:]
        else:
            address, value = map(int, re.findall(r'\d+', line))
            for i in range(len(mask)):
                bit = len(mask) - i - 1
                if mask[i] == '0':
                    value &= ~(1 << bit)
                elif mask[i] == '1':
                    value |= 1 << bit

            memory[address] = value

    return sum(memory.values())


def part_two():
    memory = {}
    mask = None
    for line in lines:
        if line[:4] == 'mask':
            mask = line[7:]
        else:
            start_address, value = map(int, re.findall(r'\d+', line))

            # Bruteforce since highest number of X in a mask is 9
            work_list = [(start_address, 0)]
            while len(work_list):
                address, i = work_list.pop()
                set_memory = True
                while i < len(mask):
                    bit = len(mask) - i - 1
                    if mask[i] == '1':
                        address |= 1 << bit
                    elif mask[i] == 'X':
                        work_list.append((address | 1 << bit, i + 1))
                        work_list.append((address & ~(1 << bit), i + 1))
                        set_memory = False
                        break
                    i += 1

                if set_memory:
                    memory[address] = value

    return sum(memory.values())


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
