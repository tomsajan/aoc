from aocd import submit
from aocd import data

# data="""BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL"""

def parse_ticket(ticket_data):
    # make it a binary representation an convert to int with base 2
    row = int(ticket_data[0:7].replace('B', '1').replace('F', '0'), 2)
    col = int(ticket_data[7:10].replace('R', '1').replace('L', '0'), 2)
    sid = 8 * row + col

    return row, col, sid


if __name__ == '__main__':

    #lines = data.split('\n\n')
    print(data)

    SIDS = set()
    for line in data.split('\n'):
        row, col, sid = parse_ticket(line)
        SIDS.add(sid)

    print(sorted(SIDS))
    previous = 0
    for sid in sorted(SIDS):
        if sid-previous == 2:  # one space between the sids
            break
        previous = sid
    print(sid-1)
    submit(sid-1)