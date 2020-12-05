from aocd import submit
from aocd import data
import re

data2 = r"""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

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

ECL_VALUES = {
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
}

RE_HCL = re.compile(r'^#[0-9a-f]{6}$')
RE_PID = re.compile(r'^[0-9]{9}$')


def verify_int_range(value, low, high):
    # print(value)
    try:
        value = int(value)
    except:
        return False
    else:
        return low <= value <= high


def verify_byr(value):
    return verify_int_range(value, 1920, 2002)


def verify_iyr(value):
    return verify_int_range(value, 2010, 2020)


def verify_eyr(value):
    return verify_int_range(value, 2020, 2030)


def verify_hgt(value):
    if value.endswith('cm'):
        # print(value)
        return verify_int_range(value.rstrip('cm'), 150, 193)
    elif value.endswith('in'):
        # print(value)
        return verify_int_range(value.rstrip('in'), 59, 76)
    else:
        return False


def verify_hcl(value):
    return bool(RE_HCL.match(value))


def verify_ecl(value):
    return value in ECL_VALUES


def verify_pid(value):
    return bool(RE_PID.match(value))


def verify_cid(value):
    return True


def parse_passport(line):
    pd = {}
    for field in line:
        parsed = field.split(':')
        pd[parsed[0]] = parsed[1]

    return pd


def verify_passport(pd):
    if not REQUIRED_FIELDS <= set(pd.keys()):
        # print(f'RF: {pd.keys()}')
        return 0
    for key, value in pd.items():
        # call verify function for each field
        if not globals()[f'verify_{key}'](value):
            # print(f'{key}: {value}')
            return 0

    return 1


if __name__ == '__main__':

    lines = data.split('\n\n')
    counter = 0
    for line in lines:
        line = line.replace('\n', ' ').split(' ')
        pd = parse_passport(line)
        counter += verify_passport(pd)

    print(counter)
    submit(counter)