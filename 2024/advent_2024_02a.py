from aocd import data, submit
from itertools import pairwise


# data = '''7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9'''

def is_report_safe(report):
    report = list(map(int, report.split()))
    if sorted(report) != report and sorted(report, reverse=True) != report:
        # not ascending and not descending
        return False
    return all(1 <= abs(i-j) <=3  for (i, j) in pairwise(report))

if __name__ == '__main__':


    result = sum(is_report_safe(report) for report in data.splitlines())
    print(result)
    submit(result)
