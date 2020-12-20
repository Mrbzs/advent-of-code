import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
nums = [int(line.rstrip('\n')) for line in inputFile]
inputFile.close()


def part_one():
    nums.sort()
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)
    one_jolt = three_jolt = 0
    for i in range(1, len(nums)):
        one_jolt += nums[i] - nums[i - 1] == 1
        three_jolt += nums[i] - nums[i - 1] == 3

    return one_jolt * three_jolt


def part_two():
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


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
