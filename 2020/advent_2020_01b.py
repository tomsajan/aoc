from aocd import data, submit
from math import floor

if __name__ == '__main__':
    data = tuple(int(d) for d in data.split('\n'))
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    print(i,j,k, i*j*k)
                    submit(j*i*k)
                    exit(0)
