from aocd import data, submit
from collections import namedtuple


# data = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''


def is_symbol(x):
    return x != '.' and not x.isdigit()


def get_number_boundaries(data, x, y, dimx):
    xend = get_number_end_x(data, x, y, dimx)
    xstart = get_number_start_x(data, x, y)
    return xstart, xend

def find_numbers(data, x, y):
    dimx = len(data[0])
    dimy = len(data)
    number_set = set()
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if y+i<0 or y+i>=dimy or x+j<0 or x+j>=dimx:
                continue
            if data[y+i][x+j].isdigit():
                xstart, xend = get_number_boundaries(data, x+j, y+i, dimx)
                number_set.add((xstart, xend, y+i, get_number(data, xstart, y+i, xend)))
    return number_set
def gear_value(data, x, y):
    if data[y][x] != '*':
        return 0
    number_set = find_numbers(data, x, y)
    print(number_set)
    if len(number_set) == 2:
        val = 1
        for num in number_set:
            val *= num[3]
        return val
    else:
        return 0
    

def get_number_end_x(data, x, y, dimx):
    while x+1 < dimx and data[y][x+1].isdigit():
        x += 1
    return x

def get_number_start_x(data, x, y):
    while x >= 1 and data[y][x-1].isdigit():
        x -= 1
    return x

def get_number(data, x, y, xend):
    assert xend - x <= 2
    assert x >= 0
    assert y >= 0
    assert x < len(data[0])
    assert y < len(data)
    return int(data[y][x:xend+1])

def is_part(data, x, y, xend, dimx, dimy):
    if x > 0:  # neni u okraje
        if is_symbol(data[y][x-1]):
            return True
        if y > 0:
            if is_symbol(data[y - 1][x - 1]):
                return True
        if y < dimy-1:
            if is_symbol(data[y + 1][x - 1]):
                return True
            
    if xend < dimx -1:  # neni u okraje
        if is_symbol(data[y][xend+1]):
            return True
        if y > 0:
            if is_symbol(data[y - 1][xend + 1]):
                return True
        if y < dimy-1:
            if is_symbol(data[y + 1][xend + 1]):
                return True
            
    if y > 0:
        for i in range(x, xend +1):
            if is_symbol(data[y-1][i]):
                return True

    if y < dimy-1:
        for i in range(x, xend +1):
            if is_symbol(data[y+1][i]):
                return True
    return False

if __name__ == '__main__':

    data = data.splitlines()
    
    suma = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            suma += gear_value(data, x, y)
            
    print(suma)
    submit(suma)
    