from aocd import data, submit
from itertools import pairwise

import re
# data = '''47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47'''


rules = {}

def process_rules(raw_rules):
    raw_rules = raw_rules.strip()
    for rule in raw_rules.split():
        first, second = rule.split('|')
        if first not in rules:
            rules[first] = {
                'before': set(),
                'after': set()
            }
        if second not in rules:
            rules[second] = {
                'before': set(),
                'after': set()
            }
        rules[first]['after'].add(second)
        rules[second]['before'].add(first)

def filter_updates(update):
    # print('u', update)
    for i in range(len(update)):
        u = update[i]
        if u not in rules:
            continue
        left = update[:i]
        right = update[i+1:]

        if any(l in rules[u]['after'] for l in left):
            return False

        if any(r in rules[u]['before'] for r in right):
            return False

        left = list(filter(lambda x: x in rules, left))
        right = list(filter(lambda x: x in rules, right))


        if set(left) - rules[u]['before'] == set() and set(right) - rules[u]['after'] == set():
            continue

    return True

if __name__ == '__main__':
    raw_rules, raw_updates = data.split('\n\n')
    process_rules(raw_rules)

    updates = [line.split(',') for line in raw_updates.strip().split()]
    # print(updates)

    valid_updates = list(filter(filter_updates, updates))
    # print(valid_updates)
    s = sum(int(update[len(update)//2]) for update in valid_updates)
    print(s)
    # print(res)
    submit(s)
