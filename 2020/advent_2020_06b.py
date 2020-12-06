from aocd import submit
from aocd import data
from collections import Counter

# data="""abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b"""

def count_yes(ans):
    people_count = len(ans.split('\n'))  # count lines
    ans = ans.replace('\n', '')
    counter = Counter(ans)
    result = 0
    for answer, count in counter.items():
        if count == people_count:
            result += 1
    return result




if __name__ == '__main__':

    answers = data.split('\n\n')
    counter = 0
    for ans in answers:
        counter += count_yes(ans)
    print(counter)
    submit(counter)