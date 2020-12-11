from aocd import submit
from aocd import data

import re

# data="""35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576"""

preamble = 25


def calc_sums(numbers):
    sums = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            # don't sum the same numbers
            if i == j:
                continue
            sums.add(numbers[i] + numbers[j])
    return sums

if __name__ == '__main__':

    numbers = [int(number) for number in data.split('\n')]
    i = preamble - 1
    valid = True
    while valid:
        i += 1
        number = numbers[i]
        sums = calc_sums(numbers[i-preamble:i])
        valid = number in sums

    print(numbers[i])
    submit(numbers[i])

    # print(len(found))
    # submit(len(found))
