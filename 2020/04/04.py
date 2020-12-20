import os
import re

inputFile = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = [line for line in inputFile]
inputFile.close()


def part_one():
    valid = 0
    fields = set()
    for line in lines + ['\n']:
        if line == '\n':
            valid += len(fields) == 8 or (len(fields) == 7 and 'cid' not in fields)
            fields = set()
        else:
            for field in line.split(' '):
                fields.add(field[:3])

    return valid


def part_two():
    valid = 0
    fields = {}
    for line in lines + ['\n']:
        if line == '\n':
            valid += is_valid(fields)
            fields = {}
        else:
            for field in line.split(' '):
                fields[field[:3]] = field[4:].rstrip('\n')
    return valid


def is_valid(fields):
    if any(field not in fields for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        return False
    match = re.match(r'^(\d+)(in|cm)$', fields['hgt'])
    if not match:
        return False
    height, unit = match.groups()
    height = int(height)
    if unit == 'cm':
        if height > 193 or height < 150:
            return False
    elif height > 76 or height < 59:
        return False

    return all([
        1920 <= int(fields['byr']) <= 2002,
        2010 <= int(fields['iyr']) <= 2020,
        2020 <= int(fields['eyr']) <= 2030,
        fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        re.match('^#[0-9a-f]{6}$', fields['hcl']),
        re.match('^[0-9]{9}$', fields['pid'])
    ])


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')
