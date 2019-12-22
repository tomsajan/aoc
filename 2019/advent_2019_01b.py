from aocd import data, submit
from math import floor


def fuel(fm):
    mass = floor(fm/3)-2
    if mass > 0:
        return mass
    return 0


def module_fuel(module_mass):
    f = fuel(module_mass)
    mf_sum = f
    while f > 0:
        f = fuel(f)
        mf_sum += f
    return mf_sum


if __name__ == '__main__':
    sum = 0
    for n in data.split('\n'):
        sum += module_fuel(int(n))
    print(sum)
    submit(sum)
