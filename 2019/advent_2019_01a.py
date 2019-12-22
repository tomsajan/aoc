from aocd import data
from math import floor

if __name__ == '__main__':
    sum = 0
    for n in data.split('\n'):
        mass = floor(float(n)/3)-2
        sum += mass
    print(sum)
