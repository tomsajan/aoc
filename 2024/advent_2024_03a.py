from aocd import data, submit
from itertools import pairwise

import re
# data = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

pattern_mul = re.compile(r'mul\((\d+),(\d+)\)')

if __name__ == '__main__':
    res = sum(int(r[0]) * int(r[1]) for r in re.findall(pattern_mul, data))

    print(res)
    submit(res)
