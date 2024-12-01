from aocd import data, submit
from math import inf

# data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

# data='''seeds: 79 14 55 13
# 
# seed-to-soil map:
# 50 98 2
# 52 50 48
# 
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
# 
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
# 
# water-to-light map:
# 88 18 7
# 18 25 70
# 
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
# 
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
# 
# humidity-to-location map:
# 60 56 37
# 56 93 4'''
# 
class Range:
    def __init__(self, dst, src, length):
        self.start = src
        self.end = src + length - 1
        self.dst = dst
        self.shift = dst - src

    def map(self, number):
        assert self.start <= number <= self.end
        return number + self.shift

    def __str__(self):
        return f'<{self.start}, {self.end}> -> {self.dst} ({self.shift})'


class Mapper:
    def __init__(self, map_data):
        self.ranges = []
        for dst, src, length in map_data:
            self.ranges.append(Range(dst, src, length))

        self.ranges.sort(key=lambda x: x.start)

    def __str__(self):
        s = []
        for r in self.ranges:
            s.append(r.__str__())
        return '\n'.join(s)
       
    def map(self, number):
        for r in self.ranges:
            if r.start <= number <= r.end:
                return r.map(number)
        return number


def chain_mapper(mappers, seeds):
    
    for mapper in mappers:
        seeds  = list(map(mapper.map, seeds))
    return seeds

def chain_mapper_single(mappers, seed):
    
    for mapper in mappers:
        seed  = mapper.map(seed)
    return seed

 
 
 
if __name__ == '__main__':
    print("hello")

#    m = Mapper([[50, 98, 2], [52, 50, 48]])
#    print(m)
#    print(m.map(-1))
#    print(m.map(20))
#    print(m.map(52))
#    print(m.map(99))
#    print(m.map(150))

    sections = data.split('\n\n')
    seeds = [int(seed) for seed in sections[0].replace('seeds: ', '').split()]
#    print(seeds)

    mappers = []
    for section in sections[1:]:
        section_lines = section.split('\n')[1:]
        section_lines_parsed = []
        for line in section_lines:
            section_lines_parsed.append([int(num) for num in line.split()])
        #print(section_lines_parsed)
        mappers.append(Mapper(section_lines_parsed))
    #print(mappers)
    
    mini = inf
    seedlen=len(seeds)
    for i in range(0, len(seeds), 2):
        print('seedstart', seeds[i], 'range', seeds[i+1])
        for seed in range(seeds[i], seeds[i]+seeds[i+1]):
            loc = chain_mapper_single(mappers, seed)
            if seed % 100000 == 0:
                print('  current seed', seed, 'loc', loc)
            if loc < mini:
                mini = loc

    print(mini)



