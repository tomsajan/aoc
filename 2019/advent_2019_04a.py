from aocd import data, submit
from math import floor
import copy
import sys


def double(num):

    for i in range(0, 5):
        if num[i] == num[i+1]:
            if i<=3 and num[i+2] == num[i] or i>0 and num[i-1] == num[i]:
                continue
            return True
    return False


def is_six(num):
    return len(num) == 6


def monotony(num):
    for i in range(0, 5):
        # print(len(num), i)
        if num[i] > num[i+1]:
            return False
    return True

if __name__ == '__main__':
    rfrom, rto = map(int, data.split('-'))
    # rfrom = 99998
    # rto = 122222

    l1 = list(filter(is_six, [str(i) for i in range(rfrom, rto+1)]))
    l2 = list(filter(monotony, l1))
    l3 = list(filter(double, l2))

    print(len(l3))
    print(l3)
    submit(len(l3))


