import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line for line in inputFile]
inputFile.close()


def part_one():
    res = 0
    questions = set()
    for line in lines + ['\n']:
        if line == '\n':
            res += len(questions)
            questions = set()
        else:
            for question in line.rstrip('\n'):
                questions.add(question)

    return res


def part_two():
    res = people = 0
    count = {}
    for line in lines + ['\n']:
        if line == '\n':
            for question in count:
                if count[question] == people:
                    res += 1
            people = 0
            count = {}
        else:
            people += 1
            for question in line.rstrip('\n'):
                if question not in count:
                    count[question] = 0
                count[question] += 1

    return res


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
