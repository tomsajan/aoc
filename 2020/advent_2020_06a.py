from aocd import submit
from aocd import data

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
    ans = ans.replace('\n', '')
    return len(set(ans))


if __name__ == '__main__':

    answers = data.split('\n\n')
    counter = 0
    for ans in answers:
        counter += count_yes(ans)
    print(counter)
    submit(counter)