from aocd import data, submit


def chunks(L, n):
    """ Yield successive n-sized chunks from L.
    """
    for i in range(0, len(L), n):
        yield L[i:i+n]


def get_num_count(data, num):
    return len(list(filter(lambda x: x == num, data)))


if __name__ == '__main__':
    dimx = 25
    dimy = 6

    layer_pixels = dimx * dimy
    layers = [chunk for chunk in chunks(data, layer_pixels)]

    min_count = float('inf')
    min_layer = None
    for layer in layers:
        zero_count = get_num_count(layer, '0')
        if zero_count < min_count:
            min_count = zero_count
            min_layer = layer

    # print(f'{min_count} {get_num_count(min_layer, "1") * get_num_count(min_layer, "2")}')
    submit(get_num_count(min_layer, "1") * get_num_count(min_layer, "2"))