from aocd import data, submit
from math import floor

if __name__ == '__main__':
    data = data.split('\n')
    for i in data:
        for j in data:
            if int(i) + int(j) == 2020:
                print(i,j,int(i)*int(j))
                submit(int(i)*int(j))
                exit(0)
