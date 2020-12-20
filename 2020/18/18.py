import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def resolve_bracket(stack, add_first=False):
    i = len(stack) - 1
    while stack[i] != '(':
        i -= 1
    stack.pop(i)

    if add_first:
        compute(stack, ['+'], i)

    compute(stack, ['+', '*'], i)


def compute(stack, operators, i):
    while i < len(stack):
        if stack[i] in operators:
            if stack[i] == '+':
                stack[i - 1:i + 2] = [stack[i - 1] + stack[i + 1]]
            elif stack[i] == '*':
                stack[i - 1:i + 2] = [stack[i - 1] * stack[i + 1]]
            i -= 1
        i += 1


def part_one():
    res = 0
    for equation in lines:
        stack = []
        for char in equation:
            if char != ' ':
                if char == ')':
                    resolve_bracket(stack)
                else:
                    stack.append(int(char) if char.isdigit() else char)

        compute(stack, ['+', '*'], 0)
        res += stack[0]

    return res


def part_two():
    res = 0
    for equation in lines:
        stack = []
        for char in equation:
            if char != ' ':
                if char == ')':
                    resolve_bracket(stack, True)
                else:
                    stack.append(int(char) if char.isdigit() else char)

        compute(stack, ['+'], 0)
        compute(stack, ['*'], 0)
        res += stack[0]

    return res


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
