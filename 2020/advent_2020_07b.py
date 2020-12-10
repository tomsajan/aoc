from aocd import submit
from aocd import data

import re

RE_CHILD_BAG = re.compile(r'\s*(?P<count>\d+\s+)?\s*(?P<color>([\w\s]+))\s+bag')

def parse_bag_line(line):
    parent, children = line.split('contain')
    parent = parent.rsplit('bag')[0].strip()
    children = children.rstrip('.').strip().split(',')


    child_dict = {}
    for child in children:
        # no other bag
        parsed = RE_CHILD_BAG.match(child).groupdict()
        if parsed['color'] == 'no other':
            child_dict = {}
            break
        child_dict[parsed['color']] = int(parsed['count'])

    # print(child_dict)


    return parent, child_dict



def get_children_count(parent, relations):
    count = 0
    for child, child_mult in relations[parent].items():
        count += child_mult * (1 + get_children_count(child, relations))
    return count

if __name__ == '__main__':

    bag_lines = data.split('\n')
    relations = {}

    for bag in bag_lines:
        parent, children = parse_bag_line(bag)
        relations[parent] = children


    count = get_children_count('shiny gold', relations)

    print(count)
    submit(count)