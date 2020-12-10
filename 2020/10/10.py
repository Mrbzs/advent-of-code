import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
nums = [int(line.rstrip('\n')) for line in inputFile]
inputFile.close()

def partOne():
    nums.sort()
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)
    oneJolt = threeJolt = 0
    for i in range(1, len(nums)):
        oneJolt += nums[i] - nums[i - 1] == 1
        threeJolt += nums[i] - nums[i - 1] == 3

    return oneJolt * threeJolt

def partTwo():
    nums.sort()
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)
    
    res = 1
    added = {-1: 0, 0: 0}

    for i in range(1, len(nums) - 1):
        # Check if number can be removed
        if nums[i] - nums[i - 1] == 1 and nums[i + 1] - nums[i] == 1:
            # We need to minus the number of combinations added 2 numbers ago. They will be invalid
            # after the previous number and current number are removed from them
            added[i] = res - added[i - 2]
            res = res * 2 - added[i - 2]
        else:
            added[i] = 0

    return res
        
print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
