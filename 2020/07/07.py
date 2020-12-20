import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line.rstrip('\n') for line in inputFile]
inputFile.close()


def part_one():
    graph = {}
    for line in lines:
        outside, inside = line.split(' contain ')
        outside = outside[:outside.rindex(' ')]
        for bag in inside.split(', '):
            bag = bag[bag.index(' ') + 1:bag.rindex(' ')]
            if bag not in graph:
                graph[bag] = set()
            graph[bag].add(outside)

    res = set()
    paths = ['shiny gold']
    while len(paths):
        bag = paths.pop()
        if bag not in res:
            res.add(bag)

            if bag in graph:
                for outside in graph[bag]:
                    paths.append(outside)

    return len(res) - 1


def part_two():
    graph = {}
    for line in lines:
        outside, inside = line.split(' contain ')
        outside = outside[:outside.rindex(' ')]
        if 'no other' not in line:
            if outside not in graph:
                graph[outside] = []
            for bag in inside.split(', '):
                graph[outside].append((bag[bag.index(' ') + 1:bag.rindex(' ')], int(bag[:bag.index(' ')])))

    res = 0
    paths = [('shiny gold', 1)]
    while len(paths):
        bag, count = paths.pop()

        if bag in graph:
            for inside, amount in graph[bag]:
                res += count * amount
                paths.append((inside, count * amount))

    return res


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
