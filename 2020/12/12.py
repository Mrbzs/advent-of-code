import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def part_one():
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    direction_index = 0
    pos = (0, 0)

    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command == 'L':
            direction_index = (direction_index - value // 90 + 4) % 4
        elif command == 'R':
            direction_index = (direction_index + value // 90) % 4
        else:
            move_index = {'N': 3, 'S': 1, 'E': 0, 'W': 2, 'F': direction_index}[command]
            pos = (pos[0] + value * directions[move_index][0], pos[1] + value * directions[move_index][1])

    return abs(pos[0]) + abs(pos[1])


def part_two():
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
            move_index = {'N': 3, 'S': 1, 'E': 0, 'W': 2}[command]
            waypoint = (waypoint[0] + value * directions[move_index][0], waypoint[1] + value * directions[move_index][1])

    return abs(pos[0]) + abs(pos[1])


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
