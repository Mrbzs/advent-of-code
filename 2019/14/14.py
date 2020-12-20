import math
import os

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = inputFile.readlines()
inputFile.close()


def solve():
    reactions = {}
    amounts = {}
    # Preprocess into dict for faster location of product
    for line in lines:
        left, right = line[:-1].split(' => ')
        amount, product = right.split(' ')
        amounts[product] = int(amount)
        reactions[product] = []
        for ingredient in left.split(', '):
            amount, reactant = ingredient.split(' ')
            reactions[product].append((int(amount), reactant))

    fuel = ores = 1
    change = 1000000
    # Using binary search for part2 to find most fuel produced under 1 trillion ores
    while change > 1 or ores > 1000000000000:
        ores = 0
        needed = {'FUEL': fuel}
        extra = {}
        while len(needed):
            # Pick a product from dict
            product = list(needed)[0]

            # Check if we have extra product
            if product in extra:
                if extra[product] > needed[product]:
                    extra[product] -= needed[product]
                    del needed[product]
                    continue
                else:
                    needed[product] -= extra[product]
                    del extra[product]

            # Find number of times to make reaction
            times = math.ceil(needed[product] / amounts[product])

            # Store extra product from the reaction
            extra_product = times * amounts[product] - needed[product]
            if extra_product > 0:
                if product in extra:
                    extra[product] += times * amounts[product] - needed[product]
                else:
                    extra[product] = times * amounts[product] - needed[product]

            # Add product's reactants to needed dict
            for amount, reactant in reactions[product]:
                if reactant == 'ORE':
                    ores += amount * times
                elif reactant in needed:
                    needed[reactant] += amount * times
                else:
                    needed[reactant] = amount * times
            del needed[product]

        if fuel == 1:
            print(f'Part one: {ores}')

        if ores > 1000000000000:
            change = 1 if change < 4 else change // 2
            fuel -= change
        else:
            fuel += change

    print(f'Part two: {fuel - 1}')


solve()
