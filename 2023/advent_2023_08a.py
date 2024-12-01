from aocd import data, submit

from collections import Counter
from itertools import cycle



def parse_lines(lines):
    d = {}
    for line in lines:
        splits = line.split(' = ')
        key = splits[0]
        values = splits[1]
        splits = values.split(', ')
        left = splits[0].replace('(', '')
        right = splits[1].replace(')', '')
        d[key] = {'L': left, 'R': right}
    return d


if __name__ == '__main__':
    lines = data.split('\n')
    instructions = lines[0]
    lines = lines[2:]

#    print(lines)
    desert_map = parse_lines(lines)
#    print(desert_map)

    
    steps = 1
    current = 'AAA'
    end = 'ZZZ'
    for instruction in cycle(instructions):
        #print(current)
        current = desert_map[current][instruction]
        if current == end:
            break

        steps += 1

    print(steps)
    submit(steps)
