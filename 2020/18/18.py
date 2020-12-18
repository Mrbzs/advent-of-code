import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()

def resolveBracket(stack, addFirst=False):
    i = len(stack) - 1
    while stack[i] != '(':
        i -= 1
    stack.pop(i)

    if addFirst:
        compute(stack, ['+'], i)

    compute(stack, ['+', '*'], i)

def compute(stack, operators, i):
    while i < len(stack):
        if stack[i] in operators:
            if stack[i] == '+':
                stack[i-1:i+2] = [stack[i - 1] + stack[i + 1]]
            elif stack[i] == '*':
                stack[i-1:i+2] = [stack[i - 1] * stack[i + 1]]
            i -= 1
        i += 1

def partOne():
    res = 0
    for equation in lines:
        stack = []
        for char in equation:
            if char != ' ':
                if char == ')':
                    resolveBracket(stack)
                else:
                    stack.append(int(char) if char.isdigit() else char)

        compute(stack, ['+', '*'], 0)
        res += stack[0]

    return res

def partTwo():
    res = 0
    for equation in lines:
        stack = []
        for char in equation:
            if char != ' ':
                if char == ')':
                    resolveBracket(stack, True)
                else:
                    stack.append(int(char) if char.isdigit() else char)

        compute(stack, ['+'], 0)
        compute(stack, ['*'], 0)
        res += stack[0]

    return res

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
