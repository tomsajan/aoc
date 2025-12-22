from aocd import data, submit

# data = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''


def is_invalid(id):
    id = str(id)
    lenid = len(id)
    # if id[lenid//2:] == id[:lenid//2]:
    #     return True


    for i in range(1, lenid//2 + 1):
        if lenid % i != 0:
            continue
        if id[:i] * (lenid // i) == id:
            return True




    return False

def  range_generator(r):
    start, stop = r.split('-')
    start = int(start)
    stop = int(stop)
    for i in range(start, stop+1):
        yield i

if __name__ == '__main__':
    # for r in data.split(','):
    #     for id in range_generator(r)
    #         if

    s = sum( id for r in data.split(',') for id in range_generator(r) if is_invalid(id) )

    print(s)
    submit(s)
