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
# data = '''..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....'''
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

# data = '''M.S
# .A.
# M.S
# '''

# data = '''.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........'''

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
    if x == 0 or y == 0:
        return 0
    if d[y][x] == 'A':
        try:
            if ((d[y-1][x-1] == 'M' and d[y+1][x+1] == 'S') or (d[y-1][x-1] == 'S' and d[y+1][x+1] == 'M')) and ((d[y+1][x-1] == 'M' and d[y-1][x+1] == 'S') or (d[y+1][x-1] == 'S' and d[y-1][x+1] == 'M')):
                return 1
        except IndexError:
            return 0
    return 0

if __name__ == '__main__':



    res = sum(xmas_count(x, y) for y in range(dimy) for x in range(dimx))

    print(res)
    submit(res)
