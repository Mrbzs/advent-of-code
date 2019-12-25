import sys
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
line = inputFile.read().rstrip()
inputFile.close()

def commandToASCII(command):
    res = []
    for char in command:
        res.append(ord(char))
    return res

forbidden = ['escape pod', 'infinite loop', 'molten lava', 'photons', 'giant electromagnet']
def run(program, i, base, command):
    output = ''
    room = ''
    commandIndex = done = 0
    directions = []
    items = []
    while 1:
        instruction = str(program[i]).zfill(5)
        if instruction[-2:] == '99':
            sys.exit()

        if i + 1 not in program:
            program[i + 1] = 0
        if i + 2 not in program:
            program[i + 2] = 0
        if i + 3 not in program:
            program[i + 3] = 0
        key1 = i + 1 if instruction[2] == '1' else program[i + 1] + base if instruction[2] == '2' else program[i + 1]
        key2 = i + 2 if instruction[1] == '1' else program[i + 2] + base if instruction[1] == '2' else program[i + 2]
        key3 = i + 3 if instruction[0] == '1' else program[i + 3] + base if instruction[0] == '2' else program[i + 3]
        if key1 not in program:
            program[key1] = 0
        if key2 not in program:
            program[key2] = 0
        if key3 not in program:
            program[key3] = 0

        if instruction[-1] == '1':
            program[key3] = program[key1] + program[key2]
            i += 4
        elif instruction[-1] == '2':
            program[key3] = program[key1] * program[key2]
            i += 4
        elif instruction[-1] == '3':
            program[key1] = command[commandIndex]
            commandIndex += 1
            i += 2
        elif instruction[-1] == '4':
            if program[key1] == 10:
                if len(output):
                    if output[0] == '-':
                        text = output[2:]
                        if text == 'north' or text == 'south' or text == 'east' or text == 'west':
                            directions.append(text)
                        elif text not in forbidden:
                            items.append(text)
                    elif output[0] == '=':
                        room = output[3:-3]
                if output == 'Command?' and commandIndex == len(command):
                    return (program, i + 2, base, directions, items, room)
                
                if room == 'Pressure-Sensitive Floor':
                    if output[28:45] == 'Analysis complete':
                        done = 1
                    if done:
                        print(output)
                output = ''
            else:
                output += chr(program[key1])
            i += 2
        elif instruction[-1] == '5':
            i = program[key2] if program[key1] else i + 3
        elif instruction[-1] == '6':
            i = i + 3 if program[key1] else program[key2]
        elif instruction[-1] == '7':
            program[key3] = 1 if program[key1] < program[key2] else 0
            i += 4
        elif instruction[-1] == '8':
            program[key3] = 1 if program[key1] == program[key2] else 0
            i += 4
        elif instruction[-1] == '9':
            base += program[key1]
            i += 2

def getPosition(y, x, direction):
    y += (direction == 'south') - (direction == 'north')
    x += (direction == 'east') - (direction == 'west')
    return (y, x)

def solve():
    visited = {}
    paths = [(dict(enumerate(int(i) for i in line.split(','))), 0, 0, 0, 0, '', '', '')]
    count = 0
    while count < len(paths):
        program, i, base, y, x, command1, command2, currentItems = paths[count]
        newProgram, newI, newBase, directions, items, room = run(program, i, base, commandToASCII(f'{command1}{command2}'))
        
        # State for not taking any items
        newStates = [(currentItems, '')]

        # States for taking items
        for item in items:
            newStates.append((''.join(sorted(currentItems + item)), f'take {item}\n'))

        for items, takeCommand in newStates:
            if room + items not in visited:
                visited[room + items] = 1
                for direction in directions:
                    newY, newX = getPosition(y, x, direction)
                    paths.append((dict(newProgram), newI, newBase, newY, newX, takeCommand, f'{direction}\n', items))
        count += 1

solve()
