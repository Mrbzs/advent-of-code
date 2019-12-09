import re

start = 124075
end = 580769

def partOne():
    return sum([re.match(r'^1*2*3*4*5*6*7*8*9*$', str(i)) != None and re.search(r'(.)\1', str(i)) != None for i in range(start, end + 1)])

def partTwo():
    return sum([re.match(r'^1*2*3*4*5*6*7*8*9*$', str(i)) != None and re.search(r'(.)\1(?<!\1..)(?!\1)', str(i)) != None for i in range(start, end + 1)])

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
