import os
import re

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

fields = []
tickets = []
validTickets = []
for line in lines:
    if line != '' and 'ticket' not in line:
        if line[0].isnumeric():
            tickets.append(list(map(int, line.split(','))))
        else:
            fields.append([line[:line.index(':')], *map(int, re.findall(r'\d+', line))])


def part_one():
    valid = set()
    for field in fields:
        for j in range(1, len(field), 2):
            for value in range(field[j], field[j + 1] + 1):
                valid.add(value)

    res = 0
    for ticket in tickets:
        valid_check = True
        for value in ticket:
            if value not in valid:
                res += value
                valid_check = False

        if valid_check:
            validTickets.append(ticket)

    return res


def part_two():
    # Precompute valid fields for each ticket column
    valid_fields = []
    for i in range(len(validTickets[0])):
        valid_fields.append((i, []))
        for j in range(len(fields)):
            ranges = fields[j][1:]
            in_range = True
            for ticket in validTickets:
                if not (ranges[0] <= ticket[i] <= ranges[1] or ranges[2] <= ticket[i] <= ranges[3]):
                    in_range = False
                    break

            if in_range:
                valid_fields[i][1].append(j)

    # Sort ticket columns in order of number of least possibilities of fields that fit its ranges 
    valid_fields.sort(key=lambda x: len(x[1]))

    # Use backtracking to bruteforce the fields to each column. Maybe backtracking isn't needed 
    # if the puzzle is designed to have only 1 possible field for each column if done in this way
    field_index = column_index = 0
    chosen_fields = [None] * len(validTickets[0])
    while column_index < len(fields):
        column, possible_fields = valid_fields[column_index]
        if possible_fields[field_index] in chosen_fields:
            field_index += 1

            # Backtrack if we reached the end and no valid field to use
            while field_index == len(possible_fields):
                column_index -= 1
                column, possible_fields = valid_fields[column_index]
                field_index = possible_fields.index(chosen_fields[column]) + 1
                chosen_fields[column] = None
        else:
            chosen_fields[column] = possible_fields[field_index]
            field_index = 0
            column_index += 1

    res = 1
    for column in range(len(chosen_fields)):
        if 'departure' in fields[chosen_fields[column]][0]:
            res *= validTickets[0][column]

    return res


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
