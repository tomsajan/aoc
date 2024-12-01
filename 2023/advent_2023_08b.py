from aocd import data, submit

from math import lcm
from collections import Counter
from itertools import cycle
#
#data = '''LR
#
#11A = (11B, XXX)
#11B = (XXX, 11Z)
#11Z = (11B, XXX)
#22A = (22B, XXX)
#22B = (22C, 22C)
#22C = (22Z, 22Z)
#22Z = (22B, 22B)
#XXX = (XXX, XXX)'''
#
#

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

    
    currents = [x for x in desert_map.keys() if x.endswith('A')]
    periods = []
    current = None
    for c in currents:
        steps = 1
        current = c
        
        for instruction in cycle(instructions):
            #print(current)
            #current = [desert_map[x][instruction] for x in current]
            current = desert_map[current][instruction]

            if current.endswith('Z'):
                print(steps)
                periods.append(steps)
                break

            steps += 1

    print(periods)
    print(lcm(*periods))
    submit(lcm(*periods))
 #   submit(steps)
