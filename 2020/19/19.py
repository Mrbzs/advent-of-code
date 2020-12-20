import os
import re

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()
rules = {}
messages = []

for line in lines:
    if line != '':
        if line[0].isdigit():
            number, rule = line.split(': ')
            rules[number] = rule[1] if '"' in rule else rule
        else:
            messages.append(line)


def solve():
    expression = ['0']
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            if '|' in rules[expression[i]]:
                paths = expression[i].split(' | ')
                criteria = ['(']
                for j in range(len(paths)):
                    criteria.extend(rules[paths[j]].split(' ') + ['|'])
                criteria[-1] = ')'
                expression[i:i + 1] = criteria
            else:
                expression[i:i + 1] = rules[expression[i]].split(' ')
            i -= 1

        i += 1

    regex = '^' + ''.join(expression) + '$'
    return sum([1 if re.match(regex, message) else 0 for message in messages])


def part_one():
    return solve()


def part_two():
    rule_eight = ''
    rule_eleven = ''
    for i in range(1, 7):
        rule_eight += '42 ' * i + '| '
        rule_eleven += '42 ' * i + '31 ' * i + '| '

    rules['8'] = rule_eight[:-3]
    rules['11'] = rule_eleven[:-3]
    return solve()


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
