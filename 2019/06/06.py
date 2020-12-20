import math
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = inputFile.readlines()
inputFile.close()


def part_one():
    # Performs recursive DFS
    def get_orbits(orbited, orbits):
        if orbited not in graph:
            return 0
        total = 0
        orbits += 1
        for orbiter in graph[orbited]:
            total += orbits + get_orbits(orbiter, orbits)
        return total

    # Construct directed graph
    graph = {}
    for line in lines:
        orbited, orbiter = line.split(')')
        if orbited in graph:
            graph[orbited].append(orbiter[:-1])
        else:
            graph[orbited] = [orbiter[:-1]]

    return get_orbits('COM', 0)


def part_two():
    # Construct undirected graph
    graph = {}
    start = destination = ''
    for line in lines:
        orbited, orbiter = line.split(')')
        if orbiter[:-1] == 'YOU':
            start = orbited
        elif orbiter[:-1] == 'SAN':
            destination = orbited

        if orbited in graph:
            graph[orbited].append(orbiter[:-1])
        else:
            graph[orbited] = [orbiter[:-1]]
        if orbiter[:-1] in graph:
            graph[orbiter[:-1]].append(orbited)
        else:
            graph[orbiter[:-1]] = [orbited]

    # Dijkstra's algorithm
    distances = {start: 0}
    visited = {}
    while len(visited) < len(graph):
        min_distance = -1
        min_key = ''
        for key in graph:
            distance = math.inf if key not in distances else distances[key]
            if key not in visited and (min_distance == -1 or distance < min_distance):
                min_distance = distance
                min_key = key
        visited[min_key] = 1

        for vertex in graph[min_key]:
            if vertex not in distances or min_distance + 1 < distances[vertex]:
                distances[vertex] = min_distance + 1

    return distances[destination]


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
