from aocd import submit
from aocd import data

import re

RE_CHILD_BAG = re.compile(r'\s*(?P<count>\d+\s+)?\s*(?P<color>([\w\s]+))\s+bag')
# data=""""""

def parse_bag_line(line):
    parent, children = line.split('contain')
    parent = parent.rsplit('bag')[0].strip()
    children = children.rstrip('.').strip().split(',')

    # try:
    child_set = {RE_CHILD_BAG.match(child).groupdict()['color'] for child in children}
    # except:
    #     print(children)
        # exit(0)
    if 'no other' in child_set:
        child_set = {}

    return parent, child_set

def find_parents_for(child, relations):
    parents = set()
    for parent, children in relations.items():
        if child in children:
            parents.add(parent)
    return parents


if __name__ == '__main__':

    bag_lines = data.split('\n')
    # print(bag_lines)
    relations = {}

    for bag in bag_lines:
        parent, children = parse_bag_line(bag)
        relations[parent] = children

    found = set()
    to_check = set()
    checked = set()

    shiny_gold_parents = find_parents_for('shiny gold', relations)
    found.update(shiny_gold_parents)
    to_check.update(shiny_gold_parents)
    checked.add('shiny gold')

    # print(shiny_gold_parents)
    while to_check:
        parent_to_check = to_check.pop()
        new_parents = find_parents_for(parent_to_check, relations)
        unchecked_parents = new_parents - checked
        to_check.update(unchecked_parents)
        found.update(new_parents)

    print(found)
    print(len(found))
    submit(len(found))

    # print(relations)
    # submit(counter)