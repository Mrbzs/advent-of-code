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
            fields.append([line[:line.index(':')], *map(int, re.findall('\d+', line))])

def partOne():
    valid = set()
    for field in fields:
        for j in range(1, len(field), 2):
            for value in range(field[j], field[j + 1] + 1):
                valid.add(value)

    res = 0
    for ticket in tickets:
        validCheck = True
        for value in ticket:
            if value not in valid:
                res += value
                validCheck = False

        if validCheck:
            validTickets.append(ticket)

    return res

def partTwo():
    # Precompute valid fields for each ticket column
    validFields = []
    for i in range(len(validTickets[0])):
        validFields.append((i, []))
        for j in range(len(fields)):
            ranges = fields[j][1:]
            inRange = True
            for ticket in validTickets:
                if not (ranges[0] <= ticket[i] <= ranges[1] or ranges[2] <= ticket[i] <= ranges[3]):
                    inRange = False
                    break
            
            if inRange:
                validFields[i][1].append(j)

    # Sort ticket columns in order of number of least possibilities of fields that fit its ranges 
    validFields.sort(key=lambda x: len(x[1]))

    # Use backtracking to bruteforce the fields to each column. Maybe backtracking isn't needed 
    # if the puzzle is designed to have only 1 possible field for each column if done in this way
    fieldIndex = columnIndex = 0
    chosenFields = [None] * len(validTickets[0])
    while columnIndex < len(fields):
        column, possibleFields = validFields[columnIndex]
        if possibleFields[fieldIndex] in chosenFields:
            fieldIndex += 1

            # Backtrack if we reached the end and no valid field to use
            while fieldIndex == len(possibleFields):
                columnIndex -= 1
                column, possibleFields = validFields[columnIndex]
                fieldIndex = possibleFields.index(chosenFields[column]) + 1
                chosenFields[column] = None
        else:
            chosenFields[column] = possibleFields[fieldIndex]
            fieldIndex = 0
            columnIndex += 1

    res = 1
    for column in range(len(chosenFields)):
        if 'departure' in fields[chosenFields[column]][0]:
            res *= validTickets[0][column]

    return res

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
