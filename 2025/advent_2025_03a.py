from aocd import data, submit

# data = '''987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# '''


def get_joltage(bank):
    maxx = max({int(battery) for battery in bank[:-1]})  # max without lastt
    # print(maxx)
    maxind = bank.find(str(maxx))
    mixx = max({int(battery) for battery in bank[maxind+1:]})
    mixind = bank.find(str(mixx), maxind+1)
    joltage = int(f'{maxx}{mixx}')
    print(joltage)
    return joltage

if __name__ == '__main__':
    # for r in data.split(','):
    #     for id in range_generator(r)
    #         if

    s = sum( get_joltage(bank) for bank in data.splitlines())

    print(s)
    submit(s)
