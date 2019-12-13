from math import gcd
import re
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = inputFile.readlines()
inputFile.close()

def solve():
    positions = []
    velocities = []
    periods = [0, 0, 0]
    for line in lines:
        x, y, z = [int(num) for num in re.findall('[\d-]+', line)]
        positions.append([x, y, z])
        velocities.append([0, 0, 0])
    
    states = [{}, {}, {}]
    step = lcm = 0
    while not lcm or step < 1000:
        # For part 2 find the period of each axis then find their LCM
        if not lcm:
            for p in range(3):
                if periods[p] == 0:
                    state = ''
                    for i in range(4):
                        state += str(positions[i][p]) + ',' + str(velocities[i][p]) + ' '
                    
                    if state in states[p]:
                        periods[p] = step
                    else:
                        states[p][state] = 1

            if 0 not in periods:
                lcm = 1
                for period in periods:
                    lcm = lcm * period // gcd(lcm, period)

        for i in range(4):
            for j in range(i + 1, 4):
                for p in range(3):
                    if positions[i][p] < positions[j][p]:
                        velocities[i][p] += 1
                        velocities[j][p] -= 1
                    elif positions[i][p] > positions[j][p]:
                        velocities[j][p] += 1
                        velocities[i][p] -= 1
        
        for i in range(4):
            for p in range(3):
                positions[i][p] += velocities[i][p]
        step += 1

        if step == 1000:
            partOne = 0
            for i in range(4):
                potential = kinetic = 0
                for p in range(3):
                    potential += abs(positions[i][p])
                    kinetic += abs(velocities[i][p])
                partOne += potential * kinetic
            print(f'Part one: {partOne}')

    print(f'Part two: {lcm}')

solve()
