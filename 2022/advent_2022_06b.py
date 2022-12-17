from aocd import data, submit
# data='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

if __name__ == '__main__':
    l = len(data)
    for s in range(l-14+1):
        if len(set(data[s:s+14])) == 14:
            print(data[s:s+14])
            print(s+14)
            submit(s+14)
            break
