import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def partOne():
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    directionIndex = 0
    pos = (0, 0)
    
    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command == 'L':
            directionIndex = (directionIndex - value // 90 + 4) % 4
        elif command == 'R':
            directionIndex = (directionIndex + value // 90) % 4
        else:
            moveIndex = {'N': 3, 'S': 1, 'E': 0, 'W': 2, 'F': directionIndex}[command]
            pos = (pos[0] + value * directions[moveIndex][0], pos[1] + value * directions[moveIndex][1])

    return abs(pos[0]) + abs(pos[1])

def partTwo():
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    waypoint = (1, 10)
    pos = (0, 0)

    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command in ['L', 'R']:
            while value:
                waypoint = (waypoint[1], -waypoint[0]) if command == 'L' else (-waypoint[1], waypoint[0])
                value -= 90
        elif command == 'F':
            pos = (pos[0] + waypoint[0] * value, pos[1] + waypoint[1] * value)
        else:
            moveIndex = {'N': 3, 'S': 1, 'E': 0, 'W': 2}[command]
            waypoint = (waypoint[0] + value * directions[moveIndex][0], waypoint[1] + value * directions[moveIndex][1])

    return abs(pos[0]) + abs(pos[1])

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
