from aocd import submit
from aocd import data

import re

# data="""28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""


if __name__ == '__main__':

    numbers = [int(number) for number in data.split('\n')]
    numbers.sort()
    numbers = [0] + numbers + [numbers[-1] + 3]
    print(numbers)
    # print(len(found))
    # submit(len(found))

    i = 1
    ones = 0
    threes = 0
    while i < len(numbers):
        diff = numbers[i] - numbers[i-1]
        if diff == 1:
            ones += 1
        if diff == 3:
            threes += 1
        i += 1

    print(ones, threes, ones * threes)
    submit(ones * threes)
