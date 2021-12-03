from aocd import submit
from aocd import data
import numpy as np
from collections import Counter

import re

# data="""L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""


def get_counts(plan, x, y):
    xleft = max(0, x-1)
    yleft = max(0, y-1)
    return Counter(plan[xleft:x+2, yleft:y+2].reshape(-1).tolist())

def new_gen(plan):
    new = np.empty(plan.shape, plan.dtype)
    for x in range(plan.shape[0]):
        for y in range(plan.shape[1]):
            counts = get_counts(plan, x, y)
            if plan[x, y] == 'L' and counts.get('#', 0) == 0:
                new[x, y] = '#'
            elif plan[x, y] == '#' and counts.get('#', 0) - 1 >= 4:  # -1 because the field itself is also counted in the counts
                new[x, y] = 'L'
            else:
                new[x, y] = plan[x, y]

    return new


if __name__ == '__main__':
    c = 0
    lines = data.split('\n')
    new_plan = np.array([list(line) for line in lines], dtype='|U1')
    plan = np.empty(new_plan.shape, dtype='|U1')
    while not np.array_equal(plan, new_plan):
        print(c)
        plan = new_plan
        # print(plan)
        new_plan = new_gen(plan)
        # print()
        c += 1

    cnt = Counter(plan.reshape(-1).tolist())
    print(cnt)
    submit(cnt['#'])

