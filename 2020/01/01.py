import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
nums = [int(line.rstrip('\n')) for line in inputFile]
inputFile.close()

def partOne():
    seen = set()
    for num in nums:
        if 2020 - num in seen:
            return num * (2020 - num)
        seen.add(num)

def partTwo():
    seen = set([nums[0]])
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            if 2020 - nums[i] - nums[j] in seen:
                return nums[i] * nums[j] * (2020 - nums[i] - nums[j])
        seen.add(nums[i])

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
