import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
nums = list(map(int, [line.rstrip('\n') for line in inputFile][0].split(',')))
inputFile.close()


def simulate(n):
    last_spoken = {}
    current = prev = None
    for i in range(n):
        current = nums[i] if i < len(nums) else i - 1 - last_spoken[prev] if prev in last_spoken else 0
        last_spoken[prev] = i - 1
        prev = current

    return current


print(f'Part one: {simulate(2020)}')
print(f'Part two: {simulate(30000000)}')
