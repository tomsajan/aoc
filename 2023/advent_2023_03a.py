from aocd import data, submit
from collections import namedtuple

# 
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

def get_number_end_x(data, x, y, dimx):
    while x+1 < dimx and data[y][x+1].isdigit():
        x += 1
    return x

def get_number(data, x, y, xend):
    assert xend - x <= 2
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
    dimy = len(data)
    dimx = len(data[0])
    
    
    suma = 0
    x = 0
    y = 0
    
    while y < dimy:
        x = 0
        while x < dimx:
            if data[y][x].isdigit():
                number_end = get_number_end_x(data, x, y, dimx)
                if is_part(data, x, y, number_end, dimx, dimy):
                    nn = get_number(data, x, y, number_end)
                    print(nn, x, y)
                    
                    suma += nn
                    x = number_end
        
            x += 1
        y += 1
    print(suma)
    submit(suma)