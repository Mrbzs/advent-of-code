import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
nums = [int(line.rstrip('\n')) for line in inputFile]
inputFile.close()

def partOne():
    for i in range(25, len(nums)):
        seen = set()
        found = False
        for j in range(i - 25, i):
            if nums[i] - nums[j] in seen:
                found = True
                break
            seen.add(nums[j])
        
        if not found:
            return nums[i]

def partTwo():
    invalid = partOne()
    start = end = 0
    total = nums[start]

    while total != invalid or start == end:
        if total + nums[end + 1] > invalid:
            total -= nums[start]
            start += 1
        else:
            end += 1
            total += nums[end]
    
    return min(nums[start:end+1]) + max(nums[start:end+1])
        
print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
