import math
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = inputFile.readlines()
inputFile.close()

def partOne():
    def getOrbits(orbited, orbits):
        if orbited not in graph:
            return 0
        total = 0
        orbits += 1
        for orbiter in graph[orbited]:
            total += orbits + getOrbits(orbiter, orbits)
        return total

    graph = {}
    for line in lines:
        orbited, orbiter = line.split(')')
        if orbited in graph:
            graph[orbited].append(orbiter[:-1])
        else:
            graph[orbited] = [orbiter[:-1]]

    return getOrbits('COM', 0)

def partTwo():
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

    distances = {start: 0}
    visited = {}
    while len(visited) < len(graph):
        minDistance = -1
        minKey = ''
        for key in graph:
            distance = math.inf if key not in distances else distances[key]
            if key not in visited and (minDistance == -1 or distance < minDistance):
                minDistance = distance
                minKey = key
        visited[minKey] = 1

        for vertex in graph[minKey]:
            if vertex not in distances or minDistance + 1 < distances[vertex]:
                distances[vertex] = minDistance + 1

    return distances[destination]

print(f'Part one: {partOne()}')
print(f'Part two: {partTwo()}')
