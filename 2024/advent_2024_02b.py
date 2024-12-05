from aocd import data, submit
from itertools import pairwise


# data = '''7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9'''

def kill_one(report):
    report = list(map(int, report.split()))
    for i in range(len(report)):
        clone = report[:]
        del clone[i]
        yield clone

def report_modifier(report):
    return any(is_report_safe(mod_report) for mod_report in kill_one(report))

def is_report_safe(report):

    if sorted(report) != report and sorted(report, reverse=True) != report:
        # not ascending and not descending
        return False
    return all(1 <= abs(i-j) <=3  for (i, j) in pairwise(report))

if __name__ == '__main__':


    result = sum(report_modifier(report) for report in data.splitlines())
    print(result)
    msubmit(result)
