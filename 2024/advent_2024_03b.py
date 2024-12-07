from aocd import data, submit
from itertools import pairwise

import re
# data = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

pattern_mul = re.compile(r'mul\((\d+),(\d+)\)')
pattern_common = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")


def do_mul(mul):
    numbers = re.search(pattern_mul, mul).groups()
    return int(numbers[0]) * int(numbers[1])

if __name__ == '__main__':
    # res = sum(int(r[0]) * int(r[1]) for r in re.findall(pattern_mul, data))
    mul_list = []
    enabled = True
    for r in re.findall(pattern_common, data):
        # print(r)
        if r.startswith('mul') and enabled:
            mul_list.append(r)
        if r == 'do()':
            enabled = True
        if r == "don't()":
            enabled = False
        # print(r)
    res = sum(do_mul(r) for r in mul_list)
    print(res)
    submit(res)
