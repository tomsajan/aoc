from aocd import data, submit

# data = '''2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8'''

if __name__ == '__main__':
    counter = 0
    for line in data.split('\n'):
        one, two = line.split(',')
        one_from, one_to = one.split('-')
        two_from, two_to = two.split('-')
        oneset = set(range(int(one_from), int(one_to)+1))
        twoset = set(range(int(two_from), int(two_to)+1))

        if oneset.issubset(twoset) or twoset.issubset(oneset):
            counter += 1


    print(counter)
    submit(counter)
    # submit(itemsum)