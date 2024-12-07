from aocd import data, submit
from itertools import pairwise

import re
# data = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''
#
# # data = '''..X...
# # .SAMX.
# # .A..A.
# # XMAS.S
# # .X....'''
# #
# # #
# data = '''....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX'''

class NoXmasException(Exception):
    pass

directions = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]

d = [list(line) for line in data.splitlines()]
dimy = len(d)
dimx = len(d[0])


def xmas_count(x, y):
    if x == 1 and y == 9:
        ...
    if d[y][x] == 'X':
        s = 0
        for dx, dy in directions:
            tx = x
            ty = y

            try:
                for char in 'XMAS':
                    try:
                        if d[ty][tx] != char or tx < 0 or ty < 0:
                           raise NoXmasException()
                        tx += dx
                        ty += dy
                    except IndexError:
                        # pass
                        raise NoXmasException()

            except NoXmasException:
                pass
            else:
                # print('x, y', x, y, 'dx dy', dx, dy)
                s += 1
        return s

    else:
        return 0


if __name__ == '__main__':



    res = sum(xmas_count(x, y) for y in range(dimy) for x in range(dimx))

    print(res)
    submit(res)
