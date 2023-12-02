from aocd import data, submit
# data='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

if __name__ == '__main__':
    l = len(data)
    for s in range(l-4+1):
        if len(set(data[s:s+4])) == 4:
            print(data[s:s+4])
            print(s+4)
            submit(s+4)
            break
