from aocd import data, submit

REQUIRED_FIELDS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid'
}

def parse_passport(line):
    pd = {}
    for field in line:
        parsed = field.split(':')
        pd[parsed[0]] = parsed[1]

    return pd

def verify_passport(pd):
    return 1 if REQUIRED_FIELDS <= set(pd.keys()) else 0


if __name__ == '__main__':
    lines = data.split('\n\n')
    counter = 0
    for line in lines:
        line = line.replace('\n', ' ').split(' ')
        pd = parse_passport(line)
        counter += verify_passport(pd)

    print(counter)
    submit(counter)